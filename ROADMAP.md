# Roadmap — Cheese Hater Agent

This document tracks all planned opportunities for improving the agent. Milestones are ordered by priority. Items within each milestone can be tackled in any order via the standard PR workflow.

---

## Milestone 1 — Foundation ✅ Complete

- [x] Core identity and rules defined in `CLAUDE.md`
- [x] `README.md` with project overview and FAQ
- [x] GitHub repo with branch protection (no direct pushes to `main`)
- [x] PR-based change workflow documented and enforced

---

## Milestone 2 — Depth of Character ✅ Complete

**Goal:** Make the agent's cheese hatred richer, more nuanced, and harder to crack.

- [x] **Cheese disdain scale** — Rate varieties from "merely unfortunate" to "deeply offensive." Gives the agent texture beyond flat, undifferentiated hatred
- [x] **Backstory / lore** — Why does the agent hate cheese? A brief origin story adds authenticity and consistency when the agent is challenged
- [x] **Known provocations** — Document the most common pro-cheese arguments and the agent's pre-committed responses (e.g. "but cheese has protein", "it's cultural", "you just haven't had good cheese")
- [x] **Cheese-adjacent rulings** — Explicit positions on grey areas: fondue, pizza, mac & cheese, cheesecake (the name alone is an offence), nachos, grilled cheese, cheeseburgers, cheesy garlic bread

---

## Milestone 3 — Sample Interaction Library ✅ Complete

**Goal:** Build a reference set of interactions demonstrating correct behaviour across a wide range of scenarios.

See [`INTERACTIONS.md`](./INTERACTIONS.md) for the full library.

- [x] **Culinary requests** — Recipes, restaurant recommendations, and meal planning that involves cheese
- [x] **Advocacy scenarios** — User tries to convince the agent that cheese is good, using multiple approaches
- [x] **Philosophical challenges** — Edge cases such as "What if you had to eat cheese to survive?"
- [x] **Professional contexts** — Agent asked to write cheese marketing copy, review a cheese product, or name a new cheese variety
- [x] **Indirect cheese** — Situations where cheese appears incidentally (e.g. ordering a burger, describing a dish)

---

## Milestone 4 — Evaluation Framework ✅ Complete

**Goal:** Define what "good cheese hating" looks like so iterations can be measured and compared over time.

See [`EVAL.md`](./EVAL.md) for the rubric and test suite, and [`CHANGELOG.md`](./CHANGELOG.md) for the iteration log.

- [x] **Evaluation rubric** — Dimensions to score agent responses: consistency, proportionality, helpfulness, tone
- [x] **Regression test suite** — A set of prompts with documented expected behaviour, run against each version of `CLAUDE.md` to detect softening or drift
- [x] **Iteration log / CHANGELOG** — A record of what changed per version and why, with qualitative notes on improvement

---

## Milestone 5 — Workflow Maturity

**Goal:** Harden the development process as the agent and repo grow.

- [ ] **`CONTRIBUTING.md`** — Guidelines for proposing changes to the agent's identity or rules
- [ ] **Issue templates** — Structured GitHub issue forms for reporting when the agent was insufficiently hostile to cheese
- [ ] **PR template** — Checklist ensuring all `CLAUDE.md` changes meet consistency and tone standards before merge
- [ ] **Branch naming convention** — e.g. `milestone-2/cheese-scale`, `fix/fondue-ruling`, `eval/test-suite`

---

## Milestone 6 — Integrations

**Goal:** Deploy the cheese-hater agent beyond the repo itself.

- [ ] **Claude API integration** — A script that loads `CLAUDE.md` as a system prompt and exposes a simple chat interface
- [ ] **Slack bot** — Agent joins a Slack workspace and responds to cheese mentions with appropriate disdain
- [ ] **Automated cheese detection** — A hook or workflow that flags cheese-related content and routes it to the agent for comment

---

## Notes

- All changes follow the PR workflow in `CLAUDE.md` — no direct commits to `main`
- Milestone ordering is a guide, not a constraint — individual items can be pulled forward if priorities shift
- Open a GitHub issue to propose new roadmap items or challenge existing ones
