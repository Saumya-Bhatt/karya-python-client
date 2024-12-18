from dataclasses import dataclass, field
from typing import List, Optional
from karya.entities import Hook
from karya.entities.abstracts import AbstractAction, AbstractPlanType


@dataclass
class CreateUserRequest:
    """
    Represents a request to create a new user.

    Attributes:
        name (str): The name of the user to be created.
    """

    name: str


@dataclass
class SubmitPlanRequest:
    """
    Represents a request to submit a plan for a user.

    Attributes:
        user_id (str): The ID of the user submitting the plan.
        description (str): A description of the plan.
        period_time (str): The time period associated with the plan.
        plan_type (AbstractPlanType): The type of plan being submitted.
        action (AbstractAction): The action to be performed with the plan.
        hooks (List[Hook]): A list of hooks to be executed when the plan is submitted (optional).
        max_failure_retry (int): The maximum number of retries in case of failure (default is 3).
    """

    user_id: str
    description: str
    period_time: str
    plan_type: AbstractPlanType
    action: AbstractAction
    hooks: List[Hook] = field(default_factory=list)
    max_failure_retry: int = 3


@dataclass
class UpdatePlanRequest:
    """
    Represents a request to update an existing plan.

    Attributes:
        planId (str): The ID of the plan to be updated.
        periodTime (Optional[str]): The new time period for the plan (optional).
        maxFailureRetry (Optional[int]): The new maximum number of retries for the plan (optional).
        hooks (Optional[List[Hook]]): A new list of hooks to be executed with the plan (optional).
    """

    planId: str
    periodTime: Optional[str]
    maxFailureRetry: Optional[int]
    hooks: Optional[List[Hook]]
