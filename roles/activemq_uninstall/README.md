activemq_uninstall
==================

Uninstalls an activemq service that was installed by the activemq role.


Dependencies
------------

The role depends on the following collections:

* [middleware_automation.common](https://github.com/ansible-middleware/common)
* [ansible.posix](https://github.com/ansible-collections/ansible.posix)

To install, from the collection root directory, run:

    ansible-galaxy collections install -r requirements.yml


<!--start argument_specs-->
Role Defaults
-------------

#### Parameters specific to uninstall role

| Variable | Description | Default |
|:---------|:------------|:--------|
|`activemq_uninstall_skip_user`| Whether to skip user/group account deletion | `false` |
|`activemq_uninstall_skip_zipfile`| Whether to skip installation zipfile deletion | `false` |
|`activemq_uninstall_skip_artemis`| Whether to skip artemis directory deletion | `false` |


#### Parameters as used with activemq role

| Variable | Description | Default |
|:---------|:------------|:--------|
|`activemq_version`| Apache Artemis version | `2.34.0` |
|`activemq_archive`| Apache Artemis install archive filename | `apache-artemis-{{ activemq_version }}-bin.zip` |
|`activemq_installdir`| Apache Artemis Installation path | `{{ activemq_dest }}/apache-artemis-{{ activemq_version }}` |
|`activemq_dest`| Root installation directory | `/opt/amq` |
|`activemq_service_user`| POSIX user running the service | `amq-broker` |
|`activemq_service_group`| POSIX group running the service | `amq-broker` |
|`activemq_service_name`| systemd service unit name | `activemq` |
|`activemq_service_user_home`| Service user home directory, defaults to artemis installation directory | `{{ activemq_dest }}/apache-artemis-{{ activemq_version }}` |
|`activemq_instance_name`| Name of broker instance to deploy | `amq-broker` |
|`activemq_configure_firewalld`| Whether to install and configure firewalld | `False` |
|`activemq_shared_storage`| Use shared filesystem directory for storage | `False` |
|`activemq_shared_storage_path`| Absolute path of shared directory | `{{ activemq_dest }}/{{ activemq_instance_name }}/data/shared` |
|`activemq_shared_storage_mounted`| Whether the systemd unit must require a mounted path (only when using shared storage) | `True` |


Example Playbook
----------------
```
---
- hosts: all
  roles:
    - middleware_automation.amq.activemq_uninstall
```
