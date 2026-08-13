# ARGOS

## Autonomous Business & Development Pilot

ARGOS is an experimental autonomous multi-agent LLM system designed to help
freelancers and small businesses identify, execute, measure and optimise
legitimate revenue-generating activities under human supervision.

ARGOS combines a local Large Language Model, goal management, planning,
tasks, persistent state, specialised agents and tools into a continuously
improving business-development system.

> **Current development goal:** investigate whether an autonomous AI pilot
> can help an individual or small business systematically discover and
> execute valuable opportunities.

---

# Research Question

> How can an autonomous multi-agent LLM system help new freelancers and
> small businesses identify, execute and optimise revenue-generating
> activities under human supervision?

The project investigates the practical use of autonomous AI agents for
business development, with particular attention to:

- autonomous planning
- goal-oriented reasoning
- multi-agent collaboration
- tool use
- persistent memory
- measurable outcomes
- human supervision
- safety and permissions
- continuous improvement

---

# Vision

The long-term vision of ARGOS is a personal business and development pilot
that can operate continuously while keeping the human operator in control.

Instead of simply answering questions, ARGOS should eventually be able to:

1. Understand a business goal.
2. Analyse the current situation.
3. Identify opportunities.
4. Research available options.
5. Generate a plan.
6. Prioritise actions by expected value.
7. Request approval when required.
8. Execute permitted actions.
9. Measure the results.
10. Store useful knowledge.
11. Learn from previous results.
12. Re-plan continuously.

The intended architecture is a controlled autonomous loop:

```text
OBSERVE
   ↓
THINK
   ↓
PLAN
   ↓
REQUEST APPROVAL
   ↓
ACT
   ↓
MEASURE
   ↓
LEARN
   ↓
REPLAN
   ↺

```

## Architecture
```
                         ┌─────────────┐
                         │    ARGOS    │
                         │ Orchestrator│
                         └──────┬──────┘
                                │
              ┌─────────────────┼─────────────────┐
              ↓                 ↓                 ↓
            GOALS             STATE            TASKS
              │                 │                 │
              │                 ├── Assets       │
              │                 ├── Memory       │
              │                 └── Results      │
              │                                   │
              └─────────────────┬─────────────────┘
                                ↓
                              PILOT
                                │
                                ↓
                         Local LLM / Ollama
                                │
                                ↓
                             Qwen
                                │
                ┌───────────────┼───────────────┐
                ↓               ↓               ↓
           STRATEGIST       RESEARCHER       ANALYST
                │               │               │
                └───────────────┼───────────────┘
                                ↓
                              TOOLS
                                │
                ┌───────────────┼───────────────┐
                ↓               ↓               ↓
            Filesystem         Git           Browser
                                │
                                ↓
                              RESULT
                                │
                                ↓
                             MEMORY
```
Current Architecture

The project is being developed incrementally.
```
ARGOS
│
├── core/
│   ├── llm.py
│   ├── pilot.py
│   └── database.py
│
├── config/
│   └── identity.py
│
├── goals/
│   ├── goal.py
│   └── manager.py
│
├── tasks/
│   ├── task.py
│   └── manager.py
│
├── projects/
│   ├── asset.py
│   └── asset_manager.py
│
├── agents/
├── skills/
├── tools/
├── memory/
└── monitoring/
```
Some components are currently prototypes and will evolve as the system
develops.