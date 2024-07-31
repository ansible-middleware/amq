# Ha configuration with active/standby nodes

This guide will show how to deploy activemq on two nodes, configured with active/standby [high availability](https://activemq.apache.org/components/artemis/documentation/latest/ha.html#terminology).
In this setup, the two instances act as a single messaging node, with the 'primary' (active) instance brokering
all messages, and the 'backup' instance standing-by on a lock, ready to pick up the 'active' work as soon
as the 'primary' instance terminates, or fails.

The guide will rely on podman containers, but it can easily be adapted to other virtual machine or cloud providers,
or even bare-metal.


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

We will create two podman containers using the [ubi-init image](https://catalog.redhat.com/software/containers/ubi8/ubi-init/5c359b97d70cc534b3a378c8), sharing the same network.

Lets create the network first:

```bash
podman network create amq
```

We will create the containers inside the network like the following command, but hold on and skip to the next paragraph:

```bash
podman run --network=amq -d --name=amq1 ubi9/ubi-init:latest
```

### Prepare a shared file-system

Artemis activemq supports a set of [shared store filesystems](https://activemq.apache.org/components/artemis/documentation/latest/ha.html#shared-store) with different characteristics. 
For the sake of keeping it simple, in this guide, and thanks to fact we are using containers, we will rely on a shared directory on the containerization host, mounted on both containers.

```bash
mkdir sharedfs
podman run --network=amq --privileged -d --name=amq1 --volume sharedfs:/opt/amq/amq-broker/data/shared:rw,z ubi9/ubi-init:latest
podman run --network=amq --privileged -d --name=amq2 --volume sharedfs:/opt/amq/amq-broker/data/shared:rw,z ubi9/ubi-init:latest
```

Note that in the mounted path above `/opt/amq/` is the default installation root directory, and `/opt/amq/amq-broker/` is the default amq instance directory.


## Create an inventory with two nodes

Now lets prepare the inventory:

```bash
mkdir inventory inventory/group_vars inventory/host_vars
cat << EOF > inventory/hosts
[amq]
amq1 ansible_connection=podman
amq2 ansible_connection=podman
EOF
```

As you can see, we listed the two instance by name, setting for each the Ansible connection driver to `podman`.
We could alternatively set it in `ansible.cfg`.


## Configuration points for HA

To tell the collection we wnat to deploy an HA node pair in active/standby, we need to set some parameters.
Those parameters will be relevant to all amq nodes, so we write them in the group_vars/amq.yml file

```yaml
# enable the ha configuration (default is primary/backup)
activemq_ha_enabled: true
# enable using the shared filesystem (we do not need to set path, because we are mounting at the default location)
activemq_shared_storage: true
# disable firewall configuration (firewalld not available on ubi containers)
activemq_configure_firewalld: false
```

We will let the amq collection use all other defaults.

Now we need to pick which instance will be initially the primary node (and thus which is the backup). In the inventory/host_vars/amq1.yml file:

```yaml
activemq_ha_role: 'primary'
```

And (optionally, since it's default) in inventory/host_vars/amq2.yml:

```yaml
activemq_ha_role: 'backup'
```

## Run installation of activemq

Now that we have our inventory ready with all configuration, we can create a playbook `deploy.yml` and execute the deployment, with the command:

```bash
ansible-playbook -i inventory/ deploy.yml
```

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
  roles:
   - middleware_automation.amq.activemq
```


## Deployment and validation

Hopefully the execution will end successfully, returning the following output at the end:

```
PLAY RECAP *******************************************************************************************************
amq1                       : ok=173  changed=29   unreachable=0    failed=0    skipped=48   rescued=0    ignored=0
amq2                       : ok=162  changed=29   unreachable=0    failed=0    skipped=40   rescued=0    ignored=0
```

We can now inspect if the desired configuration was applied correctly.

```bash
podman exec -ti amq1 tail -n 3 /var/log/activemq/amq-broker/artemis.log
2024-07-30 16:00:25,453 INFO  [org.apache.activemq.artemis] AMQ241001: HTTP Server started at http://0.0.0.0:8161
2024-07-30 16:00:25,455 INFO  [org.apache.activemq.artemis] AMQ241002: Artemis Jolokia REST API available at http://0.0.0.0:8161/console/jolokia
2024-07-30 16:00:25,455 INFO  [org.apache.activemq.artemis] AMQ241004: Artemis Console available at http://0.0.0.0:8161/console
```

amq1 is definitely the active nodes here, let's check amq2 too:


```bash
podman exec -ti amq2 tail -n 3 /var/log/activemq/amq-broker/artemis.log
2024-07-30 16:00:36,801 INFO  [org.apache.activemq.artemis.core.server] AMQ221034: Waiting indefinitely to obtain primary lock
```



## Futher reading

You can find an asciinema recording of this [guide here](https://asciinema.org/a/670215)

More guides are available in asciinema format at this links:

* https://asciinema.org/a/668257
* https://asciinema.org/a/670220
* https://asciinema.org/a/668260
