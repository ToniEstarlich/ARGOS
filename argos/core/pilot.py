from argos.config.identity import ARGOS_IDENTITY
from argos.core.llm import OllamaClient


class Pilot:
    """Main reasoning interface for ARGOS."""

    def __init__(self, model: str = "qwen3:8b") -> None:
        self.llm = OllamaClient(model=model)

    def analyse(self, goal: str, tasks: list[str]) -> str:
        task_text = "\n".join(
            f"- {task}"
            for task in tasks
        )

        prompt = f"""
You are the reasoning engine inside ARGOS.

ARGOS identity:

{ARGOS_IDENTITY}

CURRENT GOAL:

{goal}

CURRENT TASKS:

{task_text}

Analyse the current situation.

Identify:
1. The most important problem.
2. The best next action.
3. Why that action has the highest expected value.
4. What information is missing.
5. What should happen after the action.

Do not execute anything.
Do not invent revenue, customers or results.

Return a concise strategic recommendation.
"""

        return self.llm.generate(prompt)