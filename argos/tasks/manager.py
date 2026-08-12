from typing import List, Optional

from argos.tasks.task import Task


class TaskManager:
    """Manage ARGOS tasks."""

    def __init__(self) -> None:
        self._tasks: List[Task] = []

    def create_task(
        self,
        title: str,
        description: str,
        priority: int = 5,
    ) -> Task:
        task = Task(
            title=title,
            description=description,
            priority=priority,
        )

        self._tasks.append(task)
        return task

    def list_tasks(self) -> List[Task]:
        return list(self._tasks)

    def get_next_task(self) -> Optional[Task]:
        pending = [
            task for task in self._tasks
            if task.status == "pending"
        ]

        if not pending:
            return None

        return min(pending, key=lambda task: task.priority)

    def start_task(self, task: Task) -> None:
        task.status = "in_progress"

    def complete_task(self, task: Task) -> None:
        task.status = "completed"

    def fail_task(self, task: Task) -> None:
        task.status = "failed"