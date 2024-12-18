from dataclasses import dataclass
from abc import ABC
from typing import Optional, List
from karya.entities.enums import TaskStatus, PlanStatus, Trigger
from karya.entities.abstracts import AbstractAction, AbstractPlanType


@dataclass
class User:
    """
    Represents a user in the system.

    Attributes:
        id (str): The unique identifier for the user.
        name (str): The name of the user.
        created_at (int): The timestamp when the user was created.
    """

    id: str
    name: str
    created_at: int


@dataclass
class Task:
    """
    Represents a task associated with a plan.

    Attributes:
        id (str): The unique identifier for the task.
        plan_id (str): The ID of the plan to which the task belongs.
        partition_key (int): The partition key for the task.
        status (TaskStatus): The status of the task (e.g., Pending, Completed, Failed).
        created_at (int): The timestamp when the task was created.
        executed_at (Optional[int]): The timestamp when the task was executed, or `None` if not executed.
        next_execution_at (Optional[int]): The timestamp for the next task execution, or `None` if not applicable.
    """

    id: str
    plan_id: str
    partition_key: int
    status: TaskStatus
    created_at: int
    executed_at: Optional[int]
    next_execution_at: Optional[int]


@dataclass
class Hook:
    """
    Represents a hook that triggers an action.

    A hook defines a trigger and an action to be performed when the trigger condition is met.

    Attributes:
        trigger (Trigger): The event or condition that triggers the hook.
        action (AbstractAction): The action to be performed when the hook is triggered.
        max_retry (int): The maximum number of retries for the hook action in case of failure (default is 3).
    """

    trigger: Trigger
    action: AbstractAction
    max_retry: int = 3


@dataclass
class Plan:
    """
    Represents a plan for a user.

    A plan contains metadata, actions, hooks, and other details related to a user's scheduled activities.

    Attributes:
        id (str): The unique identifier for the plan.
        user_id (str): The ID of the user who owns the plan.
        description (str): A description of the plan.
        period_time (str): The time period for which the plan is valid.
        type (AbstractPlanType): The type of the plan (e.g., Recurring, OneTime).
        status (PlanStatus): The status of the plan (e.g., Active, Completed, Failed).
        max_failure_retry (int): The maximum number of retries allowed in case of failure.
        action (AbstractAction): The action associated with the plan.
        hook (List[Hook]): A list of hooks associated with the plan.
        parent_plan_id (Optional[str]): The ID of the parent plan if this is a sub-plan, or `None` if not applicable.
        created_at (int): The timestamp when the plan was created.
        updated_at (int): The timestamp when the plan was last updated.
    """

    id: str
    user_id: str
    description: str
    period_time: str
    type: AbstractPlanType
    status: PlanStatus
    max_failure_retry: int
    action: AbstractAction
    hook: List[Hook]
    parent_plan_id: Optional[str]
    created_at: int
    updated_at: int


@dataclass
class ErrorLog:
    """
    Represents an error log associated with a plan or task.

    An error log records the details of an error, including the type of error, the error message, and
    the associated timestamp.

    Attributes:
        plan_id (str): The ID of the plan that generated the error.
        error (str): A description of the error.
        type (AbstractErrorLogType): The type of error log (either `HookErrorLog` or `ExecutorErrorLog`).
        timestamp (int): The timestamp when the error occurred.
    """

    class AbstractErrorLogType(ABC):
        """An abstract base class for error log types."""

        pass

    @dataclass
    class HookErrorLog(AbstractErrorLogType):
        """
        Represents an error log for a hook.

        This type of error log is used when there is an error in executing the hook action.
        """

        pass

    @dataclass
    class ExecutorErrorLog(AbstractErrorLogType):
        """
        Represents an error log for an executor.

        This type of error log is used when there is an error related to task execution.

        Attributes:
            task_id (str): The ID of the task that encountered the error.
        """

        task_id: str

    plan_id: str
    error: str
    type: AbstractErrorLogType
    timestamp: int
