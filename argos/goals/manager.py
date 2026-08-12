from typing import Optional

from argos.goals.goal import Goal
from argos.goals.storage import GoalStorage


class GoalManager:
    """Create, retrieve and persist ARGOS goals."""

    def __init__(self, storage: Optional[GoalStorage] = None) -> None:
        self.storage = storage or GoalStorage()
        self._active_goal = self.storage.load()

    def create_goal(
        self,
        target: float,
        currency: str,
        period: str,
        income_type: str,
        description: str,
    ) -> Goal:
        goal = Goal(
            target=target,
            currency=currency,
            period=period,
            income_type=income_type,
            description=description,
        )

        self._active_goal = goal
        self.storage.save(goal)

        return goal

    def get_active_goal(self) -> Optional[Goal]:
        return self._active_goal

    def clear_goal(self) -> None:
        self._active_goal = None
        self.storage.save(None)