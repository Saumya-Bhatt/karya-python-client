# Karya Python Client

This here is the Python client to interract with [Karya - the open sourced distributed job scheduler](https://github.com/Saumya-Bhatt/karya)

> Current Stable Version : **0.1.0**

Refer to the [API Docs](https://saumya-bhatt.github.io/karya-python-client)

## Getting Started

A stable version of the client will be published to PyPi soon.

### Useage Examples

A list of samples to configure different plans with various actions and hooks can be found [here]()

### Using the Client

Do refer to the [Client API Documentation](https://saumya-bhatt.github.io/karya-python-client/#module-karya.commons.client) to understand the various methods and classes provided by the client.

1. Create a config object:

    ```python
    from karya.commons.config import ClientConfig
    from karya.commons.entities.enums import Portocol

    ## point this to where the Karya server is running
    config = ClientConfig(
        protocol=Portocol.HTTP,
        host='localhost',
        port=8080
    )

    ## For localsetup, a default config is provided as: ClientConfig.dev()
    ```

2. Create a client object:

    ```python
    from karya.clients.KaryaRestClient import KaryaRestClient

    client = KaryaRestClient(config)
    ```

3. Creat a user. Only a user configured in the Karya server can be used to create a client object.

    ```python
    from karya.commons.entities.requests import CreateUserRequest

    create_user_request = CreateUserRequest(name="python-client")
    user = await client.create_user(create_user_request)
    ```

4. Specify the action that you would want to trigger once the task is scheduled.

    ```python
    from karya.commons.entities.models.Action import RestApiRequest
    from karya.commons.entities.models.HttpBody import JsonBody

    ## For example, we shall be making a POST request to a local server
    action = RestApiRequest(
        protocol=Protocol.HTTPS,  # Use HTTPS for secure communication
        base_url="localhost",  # Base URL for the REST API
        method=Method.POST,  # HTTP method for the request (POST)
        headers={"content-type": "application/json"},  # Set the content type to JSON
        body=JsonBody.from_dict(
            {"message": "Hello from python client"}
        ),  # JSON body to send in the request
        timeout=2000,  # Timeout for the request (in milliseconds)
    )
    ```

5. Submit the plan to Karya

    ```python
    from karya.commons.entities.requests import SubmitPlanRequest
    from karya.commons.entities.models.Plan import Recurring

    # For example, we shall be submitting a recurring plan
    plan_request = SubmitPlanRequest(
        user_id=user.id,  # Use the created user's ID
        description="Make a recurring API call from python client",  # Description of the plan
        period_time="PT7S",  # Time period between each execution (7 seconds)
        max_failure_retry=3,  # Retry count in case of failure
        plan_type=Recurring(  # Define a recurring plan
            end_at=None,  # No specific end time, so it will continue indefinitely
        ),
        action=rest_action,  # The action to be executed as part of the plan (REST API call)
    )

    plan = await client.submit_plan(plan_request)
    ```

6. And you're done! The plan will be executed as per the schedule:

    - The action will be triggered every 7 seconds.
    - The action will make a POST request to `localhost` with the JSON body `{"message": "Hello from python client"}`
    - The request will have a timeout of 2 seconds.