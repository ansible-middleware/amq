amq_broker
==========

Installs and configures [Apache ActiveMQ Artemis](https://activemq.apache.org/components/artemis/) or [Red Hat AMQ Broker](https://www.redhat.com/en/technologies/jboss-middleware/amq) services.


Dependencies
------------

The roles depends on the `redhat_csp_download` role of [middleware_automation.redhat_csp_download](https://github.com/ansible-middleware/redhat-csp-download) collection.
To install, from the collection root directory, run:

    ansible-galaxy collections install -r requirements.yml


Versions
--------

| AMQ VERSION | Release Date      | Artemis Version | Notes           |
|:------------|:------------------|:----------------|:----------------|
| `AMQ 7.9`   | 2021.Q3           | `2.18.0`        |[Release Notes](https://access.redhat.com/documentation/en-us/red_hat_amq/2021.q3/html-single/release_notes_for_red_hat_amq_broker_7.9/index)|
| `AMQ 7.8`   | 2020.Q4           | `2.16.0`        |[Release Notes](https://access.redhat.com/documentation/en-us/red_hat_amq/2020.q4/html-single/release_notes_for_red_hat_amq_broker_7.8/index)|

<!--start argument_specs-->
Role Defaults
-------------

| Variable | Description | Default |
|:---------|:------------|:--------|

Role Variables
--------------

| Variable | Description | Required |
|:---------|:------------|:---------|

<!--end argument_specs-->


Example Playbook
----------------
```
---
- hosts: all
  collections:
    - middleware_automation.amq
  roles:
    - amq_broker
```