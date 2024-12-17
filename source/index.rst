.. Karya API documentation master file, created by
   sphinx-quickstart on Mon Dec 17 10:45:13 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to the Karya API Documentation!
=======================================

Karya is an open source distributed job scheduler platform written in Kotlin.
A user can submit a plan to Karya, defining how they want to run a job, and Karya will execute the job according to the plan.
This here is the documentation for the Karya API client, a Python library for interacting with the Karya service.

To read up more about Karya, visit the `Karya GitHub page  <https://github.com/Saumya-Bhatt/karya>`_

Download the Karya client from the `Github Releases page <https://github.com/Saumya-Bhatt/karya-python-client/releases>`_

Overview
========

This doc will help you get started with the Karya API client. It has a few usage examples to help you understand how to use the client and start scheduling jobs!

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Usage Examples
==============
These are some usage examples to help you get started with the Karya API client.

.. automodule:: samples.make_delayed_api_call_with_failure_hook
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: samples.make_delayed_chained_karya_call
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: samples.make_delayed_email_request
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: samples.make_recurring_api_call
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: samples.make_recurring_push_to_kafka
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: samples.make_recurring_slack_request
   :members:
   :undoc-members:
   :show-inheritance:

API Documentation
=================

.. automodule:: karya.clients.KaryaRestClient
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: karya.commons.client
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: karya.commons.config
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: karya.commons.entities.base
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: karya.commons.entities.enums
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: karya.commons.entities.requests
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: karya.commons.entities.response
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: karya.commons.entities.models.Action
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: karya.commons.entities.models.ErrorLog
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: karya.commons.entities.models.Hook
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: karya.commons.entities.models.HttpBody
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: karya.commons.entities.models.Plan
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: karya.commons.entities.models.Task
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: karya.commons.entities.models.User
   :members:
   :undoc-members:
   :show-inheritance:
