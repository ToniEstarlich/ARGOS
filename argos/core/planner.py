from argos.goals.goal import Goal
from argos.tasks.manager import TaskManager


class Planner:
    """Create an initial action plan from an ARGOS goal."""

    def __init__(self, task_manager: TaskManager) -> None:
        self.task_manager = task_manager

    def create_initial_plan(self, goal: Goal) -> None:
        self.task_manager.create_task(
            title="Analyse current assets",
            description=(
                "Identify skills, projects, knowledge, software, "
                "audience, network and other assets available to pursue the goal."
            ),
            priority=1,
        )

        self.task_manager.create_task(
            title="Research opportunities",
            description=(
                "Identify legitimate opportunities compatible with "
                "the goal and current assets."
            ),
            priority=2,
        )

        self.task_manager.create_task(
            title="Rank opportunities",
            description=(
                "Compare opportunities by potential revenue, effort, "
                "risk, scalability and automation potential."
            ),
            priority=3,
        )

        self.task_manager.create_task(
            title="Select first experiment",
            description=(
                "Choose the highest-value opportunity to test first."
            ),
            priority=4,
        )