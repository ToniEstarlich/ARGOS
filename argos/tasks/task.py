from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal


TaskStatus = Literal[
    "pending",
    "in_progress",
    "completed",
    "failed",
    "cancelled",
]


@dataclass
class Task:
    title: str
    description: str
    priority: int = 5
    status: TaskStatus = "pending"

    created_at: datetime = field(default_factory=datetime.now)

    def summary(self) -> str:
        return (
            f"[{self.status.upper()}] "
            f"P{self.priority} - {self.title}\n"
            f"{self.description}"
        )