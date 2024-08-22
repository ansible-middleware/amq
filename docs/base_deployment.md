# Base deployment

In its most basic form, the collection will download the installation zipfile, and execute
the installation of the software including its operative dependencies, and configuration of
the service and its systemd controlling unit.
The guide will rely on podman containers, but it can easily be adapted to other virtual machine
or cloud providers, or even bare-metal.


## Prerequisites

### Dependencies

On the machine running this guide, you'll need RHEL 9.2+, or in detail:

* python 3.11+
* ansible-core >= 2.16
* podman 5.1+

Then install the collections:

```bash
ansible-galaxy collection install containers.podman
ansible-galaxy collection install middleware_automation.amq
```

And python deps, for instance via pip:

```bash
pip install lxml jmespath
```

### Prepare the instances

We will create a podman container using the ubi-init image.

```bash
podman run --privileged -d --name=amq1 ubi9/ubi-init:latest
```


## Create the inventory

Now let's prepare the inventory:

```bash
mkdir inventory inventory/group_vars inventory/host_vars
cat << EOF > inventory/hosts
[amq]
amq1 connection=podman
EOF
```

As you can see, we just listed the instance by name, setting the Ansible connection driver to `podman`.
We could alternatively set it in `ansible.cfg`.


## All defaults configuration

We will let the amq collection use all defaults.

The playbook itself needs nothing else than the collection role invocation, except in this case we need the `sudo` package which is not installed by default in the ubi-init images:

```yaml
- name: Prepare instance
  hosts: all
  tasks:
   - name: install sudo
     package:
       name: sudo
- name: Playbook for ActiveMQ Artemis
  hosts: all
  vars:
    activemq_firewalld_enable: false
  roles:
   - middleware_automation.amq.activemq
```


## Run installation of activemq

Now that we have our inventory ready with all configuration, we can create a playbook and execute the deployment, with the commnad:

```bash
ansible-playbook -i inventory/ deploy.yml
```


## Deployment and validation

Hopefully the execution will end successfully, returning the following output at the end:

```
PLAY RECAP *******************************************************************************************************
amq1                       : ok=173  changed=29   unreachable=0    failed=0    skipped=48   rescued=0    ignored=0
```

We can now inspect if the desired configuration was applied correctly.

```bash
podman exec -ti amq1 tail -n 3 /var/log/activemq/amq-broker/artemis.log
2024-07-30 16:00:25,453 INFO  [org.apache.activemq.artemis] AMQ241001: HTTP Server started at http://0.0.0.0:8161
2024-07-30 16:00:25,455 INFO  [org.apache.activemq.artemis] AMQ241002: Artemis Jolokia REST API available at http://0.0.0.0:8161/console/jolokia
2024-07-30 16:00:25,455 INFO  [org.apache.activemq.artemis] AMQ241004: Artemis Console available at http://0.0.0.0:8161/console
```


## Futher reading

You can find this guide in asciinema format at [this link](https://asciinema.org/a/670220).


# Base configuration

Now that we have a container with a working deployment of amq, we can start applying changes to
our configuration, and run ansible-playbook to iteratively update our installation.


## Version (update)

The installed activemq version is specified using the `activemq_version` parameter for the `activemq` role.
The collection default will change over time, using the most recent available version that has been tested.

However, it is sometimes unwanted to operate updates without changing the underlying configuration, so the
installed version can be pinned (2.34.0 is the collection default at the time of writing):

```yaml
activemq_version: 2.34.0
```

Let's update `inventory/group_vars/amq.yml` file with the line above, so that all hosts in the `amq` group
will be covered.

If we now launch ansible-playbook, we will have a plain execution with no changes (since nothing changed
when we pinned the version to the already installed one).


```bash
ansible-playbook -i inventory/ deploy.yml

[...]

PLAY RECAP ******************************************************************************************************
amq1                       : ok=149  changed=0   unreachable=0    failed=0    skipped=43   rescued=0    ignored=0
```

Now, we want to update to 2.36, so in `inventory/group_vars/amq.yml` we set:

```yaml
activemq_version: 2.36.0
```

and we run again:

```bash
ansible-playbook -i inventory/ deploy.yml

[...]

RUNNING HANDLER [middleware_automation.amq.activemq : Restart and enable instance amq-broker for activemq service] **********************************************************
changed: [amq1]

PLAY RECAP ******************************************************************************************************
amq1                      : ok=155  changed=4    unreachable=0    failed=0    skipped=45   rescued=1    ignored=0
```

You will notice many changes were done to apply the update, and at the end of the play the service was restarted;
that is not always the case, because activemq polls its configuration and will automatically reload, without restarting,
if some of those changes are applied to its configuration. Let's try that in the next paragraph.

## Queues and topics

The default configuration applied by the collection is the same as what the `artemis create` command would generate.
In yaml, is looks like so:

```yaml
activemq_addresses:
  - name: queue.in
    anycast:
      - name: queue.in
  - name: queue.out
    anycast:
      - name: queue.out
  - name: DLQ
    anycast:
      - name: DLQ
  - name: ExpiryQueue
    anycast:
      - name: ExpiryQueue
```

Let's say we want to create an additional multicast topic, so we take the yaml above and copy to `inventory/group_vars/amq.yml`, adding the new config at the end (watch indentation, it's important!):

```yaml
activemq_version: 2.36.0
activemq_addresses:
  - name: queue.in
    anycast:
      - name: queue.in
  - name: queue.out
    anycast:
      - name: queue.out
  - name: DLQ
    anycast:
      - name: DLQ
  - name: ExpiryQueue
    anycast:
      - name: ExpiryQueue
  - name: importantTopic.pubsub
    multicast:
      - name: importantTopic.pubsub.name
```

and we iterate:

```bash
ansible-playbook -i inventory/ deploy.yml

[...]

RUNNING HANDLER [middleware_automation.amq.activemq : Restart handler] ******************************************************************************************************
skipping: [amq1]


PLAY RECAP ******************************************************************************************************
amq1                      : ok=147  changed=1    unreachable=0    failed=0    skipped=45   rescued=1    ignored=0
```

This time, the restart handler was not triggered, but we can still verify the topic configuration has been picked up by
the service by looking at the logs:

```bash
podman exec -ti amq1 tail /var/log/activemq/amq-broker/artemis.log

(2.16) ~/Development/amq (property_file *)$ podman exec -ti amq1 tail /var/log/activemq/amq-broker/artemis.log
[...]
2024-07-31 09:29:12,994 INFO  [org.apache.activemq.artemis.core.server] AMQ221003: Deploying ANYCAST queue ExpiryQueue on address ExpiryQueue
2024-07-31 09:29:12,995 INFO  [org.apache.activemq.artemis.core.server] AMQ221080: Deploying address importantTopic.pubsub supporting [MULTICAST]
2024-07-31 09:29:13,000 INFO  [org.apache.activemq.artemis.core.server] AMQ221003: Deploying MULTICAST queue importantTopic.pubsub.name on address importantTopic.pubsub
2024-07-31 09:29:13,035 INFO  [org.apache.activemq.artemis.core.server] AMQ221056: Reloading configuration: bridges
```

Many configurations can changed [this way](https://activemq.apache.org/components/artemis/documentation/2.32.0/config-reload.html), and way many more are possible with a restart.

