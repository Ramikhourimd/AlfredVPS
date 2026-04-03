---
name: creative-seeds
description: Inject creative absurdity to break AI pattern-thinking before creative tasks. Randomly samples surreal micro-stories to spark unconventional thinking. Use before brainstorming, naming, writing, ideation, or any task needing fresh perspective. Triggers on requests like "think creatively", "brainstorm", "come up with ideas", "name this", "creative approach", or any open-ended creative challenge.
---

# Creative Seeds

Cognitive disruptor that breaks pattern-locked thinking by injecting surreal micro-stories before creative tasks.

## When to Use

Run seed sampling **before** any creative task: brainstorming, naming, copywriting, ideation, creative problem-solving, or any task where novel connections matter.

## How to Use

1. Run the sampler script to pull 3 random seeds:

```bash
python3 /home/ubuntu/skills/creative-seeds/scripts/seed_sampler.py
```

Optional: pass a number to change the sample count (default 3):

```bash
python3 /home/ubuntu/skills/creative-seeds/scripts/seed_sampler.py 5
```

2. Read the output. Let the absurdist logic contaminate pattern-matching.
3. Proceed with the creative task with that mental residue active.
4. Do NOT explain the seeds to the user unless asked. Use them internally to shift the thinking frame.

## Key Principle

The seeds are **not prompts**. They are cognitive disruptors. They work by contaminating pattern-matching with nonsense, forcing novel connections. Do not try to make sense of them or map them to the task. Just let the absurdity create unexpected pathways before generating ideas.

## File Structure

- `seeds.md` — 50 surreal micro-stories (the seed bank)
- `scripts/seed_sampler.py` — Random sampler script
