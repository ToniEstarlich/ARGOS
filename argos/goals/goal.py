from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal


IncomeType = Literal["active", "passive", "mixed"]
GoalStatus = Literal["draft", "active", "paused", "completed"]


@dataclass
class Goal:
    target: float
    currency: str
    period: str
    income_type: IncomeType
    description: str

    status: GoalStatus = "active"
    created_at: datetime = field(default_factory=datetime.now)

    def summary(self) -> str:
        return (
            f"{self.description}\n"
            f"Target: {self.currency} {self.target:.2f}/{self.period}\n"
            f"Income type: {self.income_type}\n"
            f"Status: {self.status}"
        )