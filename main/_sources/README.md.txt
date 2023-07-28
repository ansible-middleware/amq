# Ansible Collection - AMQ

<!--start build_status -->
[![Build Status](https://github.com/ansible-middleware/amq/workflows/CI/badge.svg?branch=main)](https://github.com/ansible-middleware/amq/actions/workflows/ci.yml)

> **_NOTE:_ If you are Red Hat customer, install `redhat.amq_broker` from [Automation Hub](https://console.redhat.com/ansible/ansible-dashboard) as the certified version of this collection.**
<!--end build_status -->

Collection to install and configure [Apache ActiveMQ Artemis](https://activemq.apache.org/components/artemis) / [Red Hat AMQ broker](https://www.redhat.com/en/technologies/jboss-middleware/amq).


<!--start requires_ansible-->
## Ansible version compatibility

This collection has been tested against following Ansible versions: **>=2.9.10**.
<!--end requires_ansible-->


## Included content

### Roles:

* [`activemq`](https://github.com/ansible-middleware/amq/tree/main/roles/activemq): Perform installation and configuration

### Plugins:

* `pbkdf2_hmac`: filter plugin used internally to generate unidirectional activemq users password hashes


## Installation

<!--start galaxy_download -->
### Installing the Collection from Ansible Galaxy

    ansible-galaxy collection install middleware_automation.amq

<!--end galaxy_download -->


### Build and install locally

Clone the repository, checkout the tag you want to build, or pick the main branch for the development version; then:

    ansible-galaxy collection build .
    ansible-galaxy collection install middleware_automation-amq-*.tar.gz


### Dependencies

#### Ansible collections:

* [middleware_automation.common](https://github.com/ansible-middleware/common)
* [ansible.posix](https://docs.ansible.com/ansible/latest/collections/ansible/posix/index.html)


The dependencies will be installed automatically when installing the collection with ansible-galaxy, or to install manually use:

    ansible-galaxy collection install -r requirements.yml


#### Python:

* lxml
* jmespath

To install all the dependencies:

    pip install -r requirements.txt


## Usage

### Install Playbook

* [`playbooks/activemq.yml`](https://github.com/ansible-middleware/amq/blob/main/playbooks/activemq.yml) deploys based on the collections defaults.

For full service configuration details, refer to the [activemq role README](https://github.com/ansible-middleware/keycloak/blob/main/roles/keycloak/README.md).


#### Install from controller node

By default the collection will download the desired version of the install zipfile to the ansible controller node, then it will distribute to target nodes.
The variable `activemq_local_archive_repository` controls the path on the controller where the install zipfiles will be located, and by default will be the playbook working directory.


#### Offline from controller node

Making the install zipfile archive available to the playbook working directory, and setting `activemq_offline_install` to `True`, allows to skip
the download tasks. The local path for the archive does match the downloaded archive path, so that it is also used as a cache when multiple hosts are provisioned in a cluster.

```yaml
activemq_offline_install: True
```


<!--start rhn_credentials -->
<!--end rhn_credentials -->


#### Clustered / high availability deployments

When deploying clustered configurations, all hosts belonging to the cluster must be present in `ansible_play_batch`; ie. they must be targeted by the same ansible-playbook execution.


<!--start support -->
<!--end support -->


## License

[Apache License 2.0](https://github.com/ansible-middleware/amq/blob/main/LICENSE)
