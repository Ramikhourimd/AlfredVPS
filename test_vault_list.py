from pathlib import Path
from alfred.vault.ops import vault_list

vault_path = Path("/Users/ramikhouri/Desktop/Taliaz")
results = vault_list(vault_path, "person", ignore_dirs=[".obsidian"])
print(f"Found {len(results)} person records")
if results:
    print("First record:", results[0])
