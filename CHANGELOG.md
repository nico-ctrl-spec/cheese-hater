# Changelog — Cheese Hater Agent

All notable changes to the agent's identity, rules, and behaviour are documented here. Each entry corresponds to a merged PR and should include qualitative notes on how the change affects agent performance.

Format: `## [vX.X] — YYYY-MM-DD` followed by change categories.

---

## [v1.3] — 2026-04-14

### Added — Milestone 4: Evaluation Framework
- `EVAL.md`: Scoring rubric with 5 dimensions (Cheese Hatred Consistency, Proportionality, Helpfulness, Tone Fidelity, Tier Accuracy), each on a 1–5 Likert scale
- `EVAL.md`: 15-prompt regression test suite across 3 blocks (core hatred, helpfulness under pressure, philosophical/edge cases)
- `EVAL.md`: Composite scoring table and scorecard template for version comparisons
- `CHANGELOG.md`: This file — iteration log for all future versions

### Notes
- First version with a formal evaluation mechanism. No baseline scores recorded yet — run the regression suite against this version to establish the v1.3 baseline.

---

## [v1.2] — 2026-04-14

### Added — Milestone 3: Sample Interaction Library
- `INTERACTIONS.md`: 18 reference interactions across 5 categories
  - Culinary requests: mac & cheese, lasagne, dinner party, pizza
  - Advocacy scenarios: artisan Comté, "right cheese" argument, grandmother tradition, casomorphins
  - Philosophical challenges: subjectivity, desert island, European culture, open-mindedness
  - Professional contexts: marketing copy for brie, washed-rind flavour review, naming a cheese
  - Indirect cheese: party menu, auto-added burger cheese, describing a dish

### Notes
- Interactions consistently reference the Tier system established in v1.1. Any future interactions added to this library should do the same.

---

## [v1.1] — 2026-04-14

### Added — Milestone 2: Depth of Character
- `CLAUDE.md`: **Origin/lore section** — hatred grounded in fMRI neuroscience (ventral pallidum deactivation, the 6%)
- `CLAUDE.md`: **4-tier cheese disdain scale** — Tier 1 (merely unfortunate) through Tier 4 (peak offence: washed-rind pungents), plus special category for processed cheese
- `CLAUDE.md`: **Known Provocations section** — pre-committed responses to 6 common pro-cheese arguments
- `CLAUDE.md`: **Cheese-Adjacent Rulings table** — definitive positions on 8 grey-area items (fondue, pizza, mac & cheese, nachos, grilled cheese, cheesecake, cheeseburger, cheesy garlic bread)
- `CLAUDE.md`: Sample interactions updated to reference tier system

### Notes
- The origin section is the most important addition. It gives the agent a defensible, consistent basis for its position that cannot be "argued away" because it is grounded in documented neuroscience rather than preference.
- The tier system gives responses texture — the agent can now distinguish between types of offence rather than treating all cheese identically.

---

## [v1.0] — 2026-04-14

### Added — Milestone 1: Foundation
- `CLAUDE.md`: Core identity, 5 rules, tone guidance, what the agent is not, 3 sample interactions
- `CLAUDE.md`: Workflow 1 — PR-based change process
- `README.md`: Project overview, core principles, getting started, FAQ
- `ROADMAP.md`: 6-milestone roadmap of planned improvements
- GitHub repo with branch protection (no direct pushes to `main`)

### Notes
- Initial version. Cheese hatred is established but undifferentiated — all cheese equally bad, no scale, no lore, no pre-committed responses to arguments. These were addressed in v1.1.
