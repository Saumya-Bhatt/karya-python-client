from typing import Any, Dict
import json
from karya.commons.entities.base import HttpBodyType
from dataclasses import dataclass


@dataclass
class JsonBody(HttpBodyType):
    """
    Represents a JSON body to be included in an HTTP request.

    This class is used to encapsulate a JSON payload as a string. It provides a method to convert a dictionary
    into a JSON string and store it within the object. This can be used as the body of an HTTP request when
    performing actions like sending data to an API.

    Attributes:
        json_string (str): The JSON string representing the body of the HTTP request.
    """

    json_string: str
    type: str = "karya.core.entities.http.Body.JsonBody"

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "JsonBody":
        """
        Converts a dictionary to a JsonBody instance by serializing the dictionary into a JSON string.

        Args:
            data (Dict[str, Any]): A dictionary that represents the data to be serialized into JSON.

        Returns:
            JsonBody: An instance of JsonBody with the serialized JSON string.
        """

        return cls(json_string=json.dumps(data))


@dataclass
class EmptyBody(HttpBodyType):
    """
    Represents an empty body for an HTTP request.

    This class is used to represent a request body that does not contain any data. It can be used in situations
    where the HTTP request does not need to include any body content, such as a DELETE or GET request.
    """

    type: str = "karya.core.entities.http.Body.EmptyBody"
