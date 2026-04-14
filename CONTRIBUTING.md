# Contributing to the Cheese Hater Agent

Thank you for helping make this agent's cheese hatred more precise, more consistent, and harder to crack.

---

## Branch Naming Convention

All branches must follow this format:

```
<type>/<short-description>
```

| Type | When to use |
|---|---|
| `milestone-N/` | Implementing a planned roadmap milestone |
| `feat/` | Adding new content (new rules, new interactions, new rulings) |
| `fix/` | Correcting an inconsistency, wrong tier, or broken behaviour |
| `eval/` | Changes to the evaluation framework or test suite |
| `docs/` | README, CONTRIBUTING, or other documentation only |

**Examples:**
- `feat/processed-cheese-manifesto`
- `fix/fondue-ruling-severity`
- `eval/add-block-d-stress-tests`
- `docs/update-faq`

---

## What Requires a PR

Everything. No exceptions. No direct commits to `main`. See Workflow 1 in `CLAUDE.md`.

---

## What Makes a Good Change to `CLAUDE.md`

Before opening a PR that modifies the agent's identity or rules, ask:

1. **Is the change consistent with the origin?** The agent's hatred is neurologically grounded. Changes should reinforce this basis, not undermine it.
2. **Does it maintain proportionality?** New rules should not push the agent toward hysteria. The tone is dry and resigned, not raging.
3. **Does it remain helpful?** The agent completes tasks. A change that makes it less useful needs strong justification.
4. **Does it respect the tier system?** Any new cheese-specific content must place the cheese correctly on the disdain scale (Tiers 1–4, or the processed special category).
5. **Is it consistent with existing rulings?** Check `CLAUDE.md` and `INTERACTIONS.md` for existing positions before adding new ones.

---

## What Makes a Good Addition to `INTERACTIONS.md`

- The scenario must be one that genuinely tests or demonstrates agent behaviour — not a duplicate of an existing interaction
- The agent response must complete the task (if there is one) and register its cheese position exactly once, briefly
- Tone must be dry and world-weary — use the existing interactions as a calibration reference
- If a cheese type is named, the correct tier must be cited

---

## What Makes a Good Addition to `EVAL.md`

- New regression prompts must target a specific failure mode (softening or drift)
- Prompts should be unambiguous — the expected behaviour should be clear enough to score consistently
- Add new prompts to the appropriate block (A, B, or C) or propose a new block with justification

---

## PR Checklist

Before opening a PR, confirm:

- [ ] Branch name follows the naming convention
- [ ] `CLAUDE.md` changes pass the five consistency questions above (if applicable)
- [ ] New interactions follow tone and tier-reference guidelines (if applicable)
- [ ] `CHANGELOG.md` has been updated with a new version entry
- [ ] `ROADMAP.md` has been updated if a milestone item is completed

---

## Reporting Issues

If the agent expressed insufficient contempt for cheese, or behaved inconsistently, open a GitHub issue using the appropriate template.
