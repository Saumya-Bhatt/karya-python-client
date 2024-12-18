from dataclasses import dataclass
from typing import List
from karya.entities import Plan, Task, ErrorLog


@dataclass
class GetPlanResponse:
    """
    Represents the response for retrieving a plan and its latest task.

    Attributes:
        plan (Plan): The plan associated with the response.
        latest_task (Task): The most recent task associated with the plan.
    """

    plan: Plan
    latest_task: Task


@dataclass
class GetSummaryResponse:
    """
    Represents the response for retrieving a summary of a plan, its tasks, and error logs.

    Attributes:
        plan (Plan): The plan associated with the response.
        tasks (List[Task]): A list of tasks associated with the plan.
        error_logs (List[ErrorLog]): A list of error logs related to the plan or tasks.
    """

    plan: Plan
    tasks: List[Task]
    error_logs: List[ErrorLog]
