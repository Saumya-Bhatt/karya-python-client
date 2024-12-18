from abc import ABC


class AbstractPlanType(ABC):
    """
    An abstract base class representing a plan type.

    This class serves as a base for defining different types of plans. It does not
    contain any specific functionality but is meant to be subclassed by more specific
    plan types.
    """

    pass


class AbstractAction(ABC):
    """
    An abstract base class representing an action.

    This class serves as a base for defining different types of actions. It does not
    contain any specific functionality but is meant to be subclassed by more specific
    action types.
    """

    pass
