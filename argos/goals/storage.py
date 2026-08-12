import json
from dataclasses import asdict
from pathlib import Path
from typing import Optional

from argos.goals.goal import Goal


class GoalStorage:
    """Persist ARGOS goals to a JSON file."""

    def __init__(self, path: str = "data/goals.json") -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def save(self, goal: Optional[Goal]) -> None:
        if goal is None:
            self.path.write_text("null", encoding="utf-8")
            return

        data = asdict(goal)

        # datetime is not directly JSON serialisable.
        data["created_at"] = goal.created_at.isoformat()

        self.path.write_text(
            json.dumps(data, indent=2),
            encoding="utf-8",
        )

    def load(self) -> Optional[Goal]:
        if not self.path.exists():
            return None

        raw = self.path.read_text(encoding="utf-8")

        if not raw.strip() or raw.strip() == "null":
            return None

        data = json.loads(raw)

        return Goal(
            target=data["target"],
            currency=data["currency"],
            period=data["period"],
            income_type=data["income_type"],
            description=data["description"],
            status=data.get("status", "active"),
        )