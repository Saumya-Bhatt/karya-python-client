##########################################
Welcome to Karya Python Client!
##########################################

Karya is an open source distributed job scheduler platform written in Kotlin.

A user can submit a plan to Karya, defining how they want to run a job, and Karya will execute the job according to the plan.  
This documentation covers the Karya API client, a Python library for interacting with the Karya service.

To read more about Karya, visit the `Karya GitHub page <https://github.com/Saumya-Bhatt/karya>`_

##########
Overview
##########

This documentation will help you get started with the Karya API client. It includes usage examples as well as detailed API docs to help you understand how to interact with the Karya platform and start scheduling jobs!

The client can be installed via pip::

   pip install karya-client

The distribution files can also be found here - `GitHub Releases page <https://github.com/Saumya-Bhatt/karya-python-client/releases>`_.

####################
Usage Examples
####################

These are some usage examples to help you get started with the Karya API client.

*******************************
Scheduling a Recurring API Call
*******************************

.. automodule:: samples.make_recurring_api_call
   :members:
   :undoc-members:
   :show-inheritance:

******************************************
Scheduling a Delayed Job with Failure Hook
******************************************

.. automodule:: samples.make_delayed_api_call_with_failure_hook
   :members:
   :undoc-members:
   :show-inheritance:

**************************************************
Scheduling a Delayed Job with a Chained Karya Call
**************************************************

.. automodule:: samples.make_delayed_chained_karya_call
   :members:
   :undoc-members:
   :show-inheritance:

*****************************************************
Scheduling a Recurring Job to Push a Message to Kafka
*****************************************************

.. automodule:: samples.make_recurring_push_to_kafka
   :members:
   :undoc-members:
   :show-inheritance:

*****************************************
Scheduling a Delayed Job to Send an Email
*****************************************

.. automodule:: samples.make_delayed_email_request
   :members:
   :undoc-members:
   :show-inheritance:

*****************************************************
Scheduling a Recurring Job to Send a Message to Slack
*****************************************************

.. automodule:: samples.make_recurring_slack_request
   :members:
   :undoc-members:
   :show-inheritance:

################
Client Module
################

The `client` module contains the clients for interracting with the Karya Server. It also has the necessary config entities, requests and response classes.

Given below are the List of Karya Python Clients implmenting different communication protocols.

.. automodule:: karya.clients
   :members:
   :undoc-members:
   :show-inheritance:

****************
Configs
****************

The `configs` module contains the configuration entities used to initialize the Karya Client.

.. automodule:: karya.clients.config
   :members:
   :undoc-members:
   :show-inheritance:

****************
Request Entities
****************

The `requests` module contains the request entities used to make requests to the Karya Server.

.. automodule:: karya.clients.requests
   :members:
   :undoc-members:
   :show-inheritance:

******************
Response Entities
******************

The `responses` module contains the response entities returned by the Karya Server.

.. automodule:: karya.clients.responses
   :members:
   :undoc-members:
   :show-inheritance:

################
Entities Module
################

The `entities` module defines the core entities that are used by the system.

.. automodule:: karya.entities
   :members:
   :undoc-members:
   :show-inheritance:

****************
Abstract Module
****************

The `abstract` module contains the abstract classes whose implmentations are provided in the other classes. This is done so that it is easier to mock the classes for testing as well as make it easy to add new implementations.

.. automodule:: karya.entities.abstracts
   :members:
   :undoc-members:
   :show-inheritance:

****************
Enums Module
****************

The `enums` module contains the enums used by the system.

.. automodule:: karya.entities.enums
   :members:
   :undoc-members:
   :show-inheritance:

****************
Actions Module
****************

The `actions` module contains the classes that define the actions that can be configured while forming the `Plan` or while configuring a `Hook`.

.. automodule:: karya.entities.actions
   :members:
   :undoc-members:
   :show-inheritance:

******************
Plan Types Module
******************

The `plan_types` module contains the classes that define the different types of plans that can be submitted to the Karya Server.

.. automodule:: karya.entities.plan_types
   :members:
   :undoc-members:
   :show-inheritance: