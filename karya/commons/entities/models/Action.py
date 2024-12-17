from typing import Optional
from dataclasses import dataclass, field
from karya.commons.entities.base import ActionType, HttpBodyType
from karya.commons.entities.enums import Method, Protocol
from karya.commons.entities.models.HttpBody import EmptyBody

from typing import TYPE_CHECKING

# TYPE_CHECKING is used to prevent circular imports while providing hints during static analysis.
if TYPE_CHECKING:
    from karya.commons.entities.requests import SubmitPlanRequest


@dataclass
class RestApiRequest(ActionType):
    """
    Represents an HTTP request action that can be executed as part of a plan.

    Attributes:
        base_url (str): The base URL for the API request.
        body (HttpBodyType): The body of the HTTP request, represented as an HTTP body type.
        protocol (Protocol): The protocol used for the request (e.g., HTTP, HTTPS). Defaults to HTTP.
        method (Method): The HTTP method to be used (e.g., GET, POST, etc.). Defaults to GET.
        headers (dict): A dictionary of HTTP headers for the request. Defaults to content-type as application/json.
        timeout (int): The timeout duration for the request, in milliseconds. Defaults to 2000ms.
    """

    base_url: str
    body: HttpBodyType = field(default_factory=lambda: EmptyBody())
    protocol: Protocol = Protocol.HTTP
    method: Method = Method.GET
    headers: dict = field(default_factory=lambda: {"content-type": "application/json"})
    timeout: int = 2000
    type: str = "karya.core.entities.Action.RestApiRequest"


@dataclass
class SlackMessageRequest(ActionType):
    """
    Represents an action that sends a message to a Slack channel.

    Attributes:
        channel (str): The Slack channel where the message will be sent.
        message (str): The content of the Slack message.
    """

    channel: str
    message: str
    type: str = "karya.core.entities.Action.SlackMessageRequest"


@dataclass
class EmailRequest(ActionType):
    """
    Represents an action to send an email.

    Attributes:
        recipient (str): The recipient's email address.
        subject (str): The subject of the email.
        message (str): The body content of the email.
    """

    recipient: str
    subject: str
    message: str
    type: str = "karya.core.entities.Action.EmailRequest"


@dataclass
class KafkaProducerRequest(ActionType):
    """
    Represents an action that publishes a message to a Kafka topic.

    Attributes:
        topic (str): The Kafka topic where the message will be published.
        message (str): The content of the Kafka message.
        key (Optional[str]): The optional key for the Kafka message, used for partitioning.
    """

    topic: str
    message: str
    key: Optional[str] = field(default=None)
    type: str = "karya.core.entities.Action.KafkaProducerRequest"


@dataclass
class ChainedRequest(ActionType):
    """
    Represents an action that chains multiple requests into a single action.

    Attributes:
        request (SubmitPlanRequest): The request that is part of the chain. This can be another plan submission request.
    """

    request: "SubmitPlanRequest"
    type: str = "karya.core.entities.Action.ChainedRequest"
