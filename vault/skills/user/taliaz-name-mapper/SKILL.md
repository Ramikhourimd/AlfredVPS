---
name: taliaz-name-mapper
description: Normalizes and maps therapist names between Hebrew and English. Solves the critical name-matching problem for Taliaz data integration. Use this skill to standardize names before joining data from different sources (e.g., user-provided CSV files with Hebrew names and API data with English names).
---

# Taliaz Name Mapper Skill

A dedicated skill to solve the Hebrew ↔ English name-matching problem permanently. This skill uses the official therapist reference table from `taliaz-data-loader` as the canonical source for name mapping.

## Problem Solved

Taliaz operational data comes from multiple sources with inconsistent naming:

| Source | Name Format | Example |
|--------|-------------|---------|
| **API (Meetings)** | English | "Ori Shukrun" |
| **User CSV (Availability)** | Hebrew | "אורי שוקרון" |
| **Reference Files** | Both | Hebrew + English columns |

Without proper normalization, data joins fail silently, causing missing values in reports.

## Features

| Feature | Description |
|---------|-------------|
| **Bidirectional Mapping** | Hebrew → English and English → English (idempotent) |
| **Fuzzy Matching** | Handles typos and minor variations (configurable threshold) |
| **Batch Processing** | Normalize entire DataFrame columns efficiently |
| **Validation** | Report unmapped names with suggestions |
| **Integration** | Works seamlessly with `taliaz-data-loader` |

## Data Source

The name mapper uses the **therapists table** from `taliaz-data-loader` as its canonical mapping source:

| Column | Purpose |
|--------|---------|
| `English Name` | Canonical name (target format) |
| `Hebrew Name` | Hebrew name (source format for user CSVs) |

This ensures a single source of truth for all name mappings.

## Usage

### Command Line

```bash
# Normalize a single name
python3 scripts/name_mapper.py normalize "אורי שוקרון"
# Output: Ori Shukrun

# Normalize a CSV file column
python3 scripts/name_mapper.py normalize-csv \
  --input /path/to/availability.csv \
  --column "Therapists Name" \
  --output /path/to/normalized.csv

# Validate names in a CSV (report unmapped)
python3 scripts/name_mapper.py validate \
  --input /path/to/availability.csv \
  --column "Therapists Name"

# Show all known mappings
python3 scripts/name_mapper.py list-mappings
```

### Python API

```python
from pathlib import Path
import sys
sys.path.insert(0, str(Path("/home/ubuntu/skills/taliaz-name-mapper/scripts")))
sys.path.insert(0, str(Path("/home/ubuntu/skills/taliaz-data-loader/scripts")))

from name_mapper import TaliazNameMapper
from data_loader import TaliazDataLoader

# Initialize with therapist data from data-loader
loader = TaliazDataLoader()
mapper = TaliazNameMapper(loader.therapists_df)

# Normalize a single name
english_name = mapper.normalize("אורי שוקרון")
# Returns: "Ori Shukrun"

# Normalize is idempotent for English names
english_name = mapper.normalize("Ori Shukrun")
# Returns: "Ori Shukrun"

# Normalize a DataFrame column
import pandas as pd
availability_df = pd.read_csv("availability.csv")
availability_df["therapist_name_en"] = mapper.normalize_column(
    availability_df["Therapists Name"]
)

# Fuzzy match with confidence score
result = mapper.fuzzy_match("Uri Shokrun")
# Returns: {"name": "Ori Shukrun", "confidence": 0.92}

# Validate and get unmapped names with suggestions
unmapped = mapper.validate(availability_df["Therapists Name"])
# Returns: [{"input": "Unknown Name", "suggestions": ["Similar Name (85%)"]}]

# Get mapping statistics
stats = mapper.get_stats()
# Returns: {"total_mappings": 28, "hebrew_names": 28, "english_names": 28}
```

### Integration with Data Loader

The recommended workflow is to use the name mapper immediately after loading availability data:

```python
from data_loader import TaliazDataLoader
from name_mapper import TaliazNameMapper

# Load all data
loader = TaliazDataLoader()
data = loader.load_monthly_data("2025-12", "/path/to/availability.csv")

# Initialize mapper with therapist data
mapper = TaliazNameMapper(data["therapists"])

# Normalize the availability names to match meetings data
availability_df = data["availability"]
availability_df["therapist_name"] = mapper.normalize_column(
    availability_df["therapist_name"]
)

# Now the names will match when joining with meetings_df
meetings_df = data["meetings"]
merged = meetings_df.merge(
    availability_df,
    left_on="therpaist_name",
    right_on="therapist_name",
    how="left"
)
# All matching names will now join correctly!
```

## Mapping Rules

### Priority Order

1. **Exact Hebrew Match**: If input matches a Hebrew name exactly, return the corresponding English name
2. **Exact English Match**: If input matches an English name exactly, return it unchanged (idempotent)
3. **Fuzzy Match**: If no exact match, try fuzzy matching with configurable threshold (default: 85%)
4. **Fallback**: If no match found, return original input and log a warning

### Normalization Steps

Before matching, names are normalized:
1. Strip leading/trailing whitespace
2. Collapse multiple spaces to single space
3. Unicode normalization (NFKC)
4. Handle special characters (quotes, dashes)

### Fuzzy Matching

Fuzzy matching uses the SequenceMatcher algorithm to find similar names:

| Threshold | Behavior |
|-----------|----------|
| 0.95+ | Very strict, only minor typos |
| 0.85 (default) | Balanced, catches common variations |
| 0.70 | Lenient, may produce false positives |

## Error Handling

| Scenario | Behavior |
|----------|----------|
| Empty/None input | Returns empty string |
| Unknown name (no match) | Returns original, logs warning |
| Fuzzy match found | Returns match, logs info with confidence |
| Invalid therapists_df | Raises ValueError |

## Validation Report

The `validate()` method returns detailed information about unmapped names:

```python
unmapped = mapper.validate(names_series)
# Returns:
[
    {
        "input": "Unknown Person",
        "suggestions": [
            "Similar Person (78%)",
            "Another Similar (72%)"
        ]
    },
    {
        "input": "Another Unknown",
        "suggestions": []  # No similar names found
    }
]
```

## Performance

| Operation | Performance |
|-----------|-------------|
| Single name lookup | < 1ms |
| 1,000 names | < 100ms |
| 10,000 names | < 1 second |

The mapper uses dictionary-based lookups for O(1) exact matches and caches fuzzy match results.

## Dependencies

- pandas
- difflib (standard library)

## Notes

- The mapper is **stateless** - it does not modify the source therapists table
- All mappings are **case-sensitive** (Hebrew names are case-insensitive by nature)
- The mapper **does not persist** learned mappings - use the reference table for permanent additions
- For new therapists, add them to `User_type+User_Fee.xlsx` in `taliaz-data-loader`
