from typing import Optional
from dataclasses import dataclass
from karya.entities.abstracts import AbstractPlanType


@dataclass
class Recurring(AbstractPlanType):
    """
    Represents a recurring plan type.

    This class extends the `AbstractPlanType` and represents a plan that repeats
    periodically. It includes an optional `end_at` field to specify when the recurring
    plan should end.

    Attributes:
        end_at (Optional[str]): The optional end date for the recurring plan (can be `None`).
    """

    end_at: Optional[str]
    type: str = "karya.core.entities.PlanType.Recurring"


@dataclass
class OneTime(AbstractPlanType):
    """
    Represents a one-time plan type.

    This class extends the `AbstractPlanType` and represents a plan that occurs only once.
    """

    type: str = "karya.core.entities.PlanType.OneTime"
