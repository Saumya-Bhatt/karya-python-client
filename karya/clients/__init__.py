import httpx
import dataclasses
from karya.clients.config import ClientConfig
from karya.entities import User, Plan
from karya.clients.requests import (
    CreateUserRequest,
    SubmitPlanRequest,
    UpdatePlanRequest,
)
from karya.clients.responses import (
    GetPlanResponse,
    GetSummaryResponse,
    ListPlanResponse,
)


class KaryaRestClient:
    """
    A client for interacting with the Karya API over REST.

    This client provides methods to manage users and plans, such as creating a user,
    submitting a plan, fetching plans, updating plans, and getting summaries of plans.
    """

    api_version = "v1"
    _plans_endpoint = f"{api_version}/plan"
    _users_endpoint = f"{api_version}/user"

    def __init__(self, config: ClientConfig):
        """
        Initializes the KaryaRestClient.

        Args:
            config (ClientConfig): The configuration object containing base URL and other settings.

        Sets up an asynchronous HTTP client and assigns the base URL from the provided config.
        """
        super().__init__()
        self.client = httpx.AsyncClient()
        self.base_url = config.get_base_url()

    async def create_user(self, request: CreateUserRequest) -> User:
        """
        Creates a new user by sending a POST request to the Karya API.

        Args:
            request (CreateUserRequest): The request object containing user data.

        Returns:
            User: A User object containing the details of the created user.

        Raises:
            httpx.HTTPStatusError: If the request fails with a non-2xx status code.
        """
        url = f"{self.base_url}/{self._users_endpoint}"
        response = await self.client.post(url, json=dataclasses.asdict(request))
        response.raise_for_status()
        return User(**response.json())

    async def get_user(self, username: str) -> User:
        """
        Retrieves the details of a specific user by username.

        Args:
            username (str): The username of the user to retrieve.

        Returns:
            User: A User object containing the details of the requested user.

        Raises:
            httpx.HTTPStatusError: If the request fails with a non-2xx status code.
        """
        url = f"{self.base_url}/{self._users_endpoint}"
        params = {"username": username}
        response = await self.client.get(url=url, params=params)
        response.raise_for_status()
        return User(**response.json())

    async def submit_plan(self, request: SubmitPlanRequest) -> Plan:
        """
        Submits a new plan to the Karya API.

        Args:
            request (SubmitPlanRequest): The request object containing plan data.

        Returns:
            Plan: A Plan object containing the details of the submitted plan.

        Raises:
            httpx.HTTPStatusError: If the request fails with a non-2xx status code.
        """
        url = f"{self.base_url}/{self._plans_endpoint}"
        response = await self.client.post(url, json=dataclasses.asdict(request))
        response.raise_for_status()
        return Plan(**response.json())

    async def get_plan(self, plan_id: str) -> GetPlanResponse:
        """
        Retrieves the details of a specific plan by ID.

        Args:
            plan_id (str): The ID of the plan to retrieve.

        Returns:
            GetPlanResponse: A response object containing the plan details.

        Raises:
            httpx.HTTPStatusError: If the request fails with a non-2xx status code.
        """
        url = f"{self.base_url}/{self._plans_endpoint}/{plan_id}"
        response = await self.client.get(url)
        response.raise_for_status()
        return GetPlanResponse(**response.json())

    async def update_plan(self, request: UpdatePlanRequest) -> Plan:
        """
        Updates an existing plan with new details.

        Args:
            request (UpdatePlanRequest): The request object containing updated plan data.

        Returns:
            Plan: A Plan object containing the updated plan details.

        Raises:
            httpx.HTTPStatusError: If the request fails with a non-2xx status code.
        """
        url = f"{self.base_url}/{self._plans_endpoint}/{request.id}"
        response = await self.client.patch(url, json=dataclasses.asdict(request))
        response.raise_for_status()
        return Plan(**response.json())

    async def cancel_plan(self, plan_id: str) -> Plan:
        """
        Cancels a specified plan by ID.

        Args:
            plan_id (str): The ID of the plan to cancel.

        Returns:
            Plan: A Plan object reflecting the canceled plan.

        Raises:
            httpx.HTTPStatusError: If the request fails with a non-2xx status code.
        """
        url = f"{self.base_url}/{self._plans_endpoint}/{plan_id}"
        response = await self.client.post(url)
        response.raise_for_status()
        return Plan(**response.json())

    async def get_summary(self, plan_id: str) -> GetSummaryResponse:
        """
        Retrieves the summary for a specific plan by ID.

        Args:
            plan_id (str): The ID of the plan for which to retrieve the summary.

        Returns:
            GetSummaryResponse: A response object containing the summary data.

        Raises:
            httpx.HTTPStatusError: If the request fails with a non-2xx status code.
        """
        url = f"{self.base_url}/{self._plans_endpoint}/{plan_id}/summary"
        response = await self.client.get(url)
        response.raise_for_status()
        return GetSummaryResponse(**response.json())

    async def list_plans(self, user_id: str, page: int) -> ListPlanResponse:
        """
        Retrieves a list of plans for a specific user by username.

        Args:
            username (str): The username of the user for which to retrieve plans.
            page (int): The page number to retrieve (default is 0).

        Returns:
            ListPlanResponse: A resopnse object containing the list of plans.

        Raises:
            httpx.HTTPStatusError: If the request fails with a non-2xx status code.
        """
        url = f"{self.base_url}/{self._plans_endpoint}"
        params = {"user_id": user_id, "page": page}
        response = await self.client.get(url=url, params=params)
        response.raise_for_status()
        return ListPlanResponse(**response.json())

    async def close(self) -> None:
        """
        Closes the HTTP client connection.

        This should be called when the client is no longer needed to ensure that
        resources are cleaned up properly.
        """
        await self.client.aclose()
