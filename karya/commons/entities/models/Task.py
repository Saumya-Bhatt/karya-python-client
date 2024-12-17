from karya.commons.entities.enums import TaskStatus
from typing import Optional
from dataclasses import dataclass


@dataclass
class Task:
    """
    Represents an individual task that is part of a plan's execution.

    A task is a unit of work that is executed as part of a plan. It can be in various statuses (e.g., CREATED, PROCESSING, SUCCESS, FAILURE)
    and has timestamps for tracking its lifecycle (when it was created, when it was executed, and when it is scheduled to be executed next).

    Attributes:
        id (str): The unique identifier for the task.
        plan_id (str): The ID of the plan to which this task belongs.
        partition_key (int): A key used for partitioning tasks. It could be used for distributing work across different workers or machines.
        status (TaskStatus): The current status of the task (e.g., CREATED, PROCESSING, SUCCESS, FAILURE).
        created_at (int): The timestamp indicating when the task was created (Unix timestamp).
        executed_at (Optional[int]): The timestamp indicating when the task was executed. This is optional because a task may not have been executed yet.
        next_execution_at (Optional[int]): The timestamp indicating when the task is scheduled to be executed next. This is optional and may be `None` for one-time tasks.
    """

    id: str
    plan_id: str
    partition_key: int
    status: TaskStatus
    created_at: int
    executed_at: Optional[int]
    next_execution_at: Optional[int]
