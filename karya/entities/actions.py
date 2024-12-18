from dataclasses import dataclass, field
from abc import ABC
from typing import Any, Dict, Optional, TYPE_CHECKING
from karya.entities.abstracts import AbstractAction
from karya.entities.enums import Protocol, Method
import json

if TYPE_CHECKING:
    from karya.clients.requests import SubmitPlanRequest


@dataclass
class RestApiRequest(AbstractAction):
    """
    Represents a REST API request action.

    This class allows for defining a REST API request action, including the HTTP method,
    protocol, headers, and request body. It includes nested classes for handling different
    types of request bodies, such as JSON and empty bodies.

    Attributes:
        base_url (str): The base URL for the REST API request.
        body (AbstractBody): The body of the request, which can be JSON or empty.
        protocol (Protocol): The protocol used for the request, default is `Protocol.HTTP`.
        method (Method): The HTTP method for the request, default is `Method.GET`.
        headers (dict): The headers for the request, default is `{"content-type": "application/json"}`.
        timeout (int): The timeout duration for the request in milliseconds, default is 2000.
    """

    class AbstractBody(ABC):
        """An abstract base class for request bodies."""

        pass

    @dataclass
    class JsonBody(AbstractBody):
        """
        Represents a JSON body for a REST API request.

        Attributes:
            json_string (str): The JSON-encoded string to be sent in the request body.
        """

        json_string: str
        type: str = "karya.core.entities.http.Body.JsonBody"

        @classmethod
        def from_dict(cls, data: Dict[str, Any]) -> "RestApiRequest.JsonBody":
            """
            Creates a `JsonBody` instance from a dictionary by converting it to a JSON string.

            Args:
                data (Dict[str, Any]): A dictionary representing the data to be converted.

            Returns:
                RestApiRequest.JsonBody: A new instance of `JsonBody` containing the JSON string.
            """
            return cls(json_string=json.dumps(data))

    @dataclass
    class EmptyBody(AbstractAction):
        """
        Represents an empty body for a REST API request.
        """

        type: str = "karya.core.entities.http.Body.EmptyBody"

    base_url: str
    body: AbstractBody = field(default_factory=lambda: RestApiRequest.EmptyBody())
    protocol: Protocol = Protocol.HTTP
    method: Method = Method.GET
    headers: dict = field(default_factory=lambda: {"content-type": "application/json"})
    timeout: int = 2000
    type: str = "karya.core.entities.Action.RestApiRequest"


@dataclass
class KafkaProducerRequest(AbstractAction):
    """
    Represents a Kafka producer request action.

    This class defines a Kafka producer request, including the topic, message, and optional key.

    Attributes:
        topic (str): The Kafka topic to send the message to.
        message (str): The message to be sent to the Kafka topic.
        key (Optional[str]): An optional key to associate with the message.
    """

    topic: str
    message: str
    key: Optional[str] = field(default=None)
    type: str = "karya.core.entities.Action.KafkaProducerRequest"


@dataclass
class ChainedRequest(AbstractAction):
    """
    Represents a chained request action.

    This class represents a request that chains another request (e.g., `SubmitPlanRequest`).

    Attributes:
        request (SubmitPlanRequest): The request to be chained.
    """

    request: "SubmitPlanRequest"
    type: str = "karya.core.entities.Action.ChainedRequest"


@dataclass
class EmailRequest(AbstractAction):
    """
    Represents an email request action.

    This class defines the properties required to send an email, including the recipient,
    subject, and message body.

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
class SlackMessageRequest(AbstractAction):
    """
    Represents a Slack message request action.

    This class defines the properties required to send a message to a Slack channel.

    Attributes:
        channel (str): The Slack channel to send the message to.
        message (str): The content of the message to be sent to the Slack channel.
    """

    channel: str
    message: str
    type: str = "karya.core.entities.Action.SlackMessageRequest"
