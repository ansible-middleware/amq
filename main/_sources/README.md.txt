# Ansible Collection - AMQ

[![Build Status](https://github.com/ansible-middleware/amq/workflows/CI/badge.svg?branch=main)](https://github.com/ansible-middleware/amq/actions/workflows/ci.yml)

## About

Collection to install and configure [Apache ActiveMQ Artemis](https://activemq.apache.org/components/artemis) or [Red Hat AMQ broker](https://www.redhat.com/en/technologies/jboss-middleware/amq).

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

### Download from galaxy

    ansible-galaxy collection install middleware_automation.amq


### Build and install locally

Clone the repository, checkout the tag you want to build, or pick the main branch for the development version; then:

    ansible-galaxy collection build .
    ansible-galaxy collection install middleware_automation-amq-*.tar.gz


### Dependencies

#### Ansible collections:

* [middleware_automation.redhat_csp_download](https://github.com/ansible-middleware/redhat-csp-download)
* [ansible.posix](https://docs.ansible.com/ansible/latest/collections/ansible/posix/index.html)


To install all the dependencies via galaxy:

    ansible-galaxy collection install -r requirements.yml

#### Python:

* no extra python dependencies are currently required


## Support

The amq collection is a Beta release and for [Technical Preview](https://access.redhat.com/support/offerings/techpreview). If you have any issues or questions related to collection, please don't hesitate to contact us on <Ansible-middleware-core@redhat.com> or open an issue on <https://github.com/ansible-middleware/amq/issues>

## License

[GNU General Public License v2.0](https://github.com/ansible-middleware/amq/blob/main/LICENSE)
