activemq
==========

Installs and configures [Apache ActiveMQ Artemis](https://activemq.apache.org/components/artemis/) services.


Dependencies
------------

The role depends on the `redhat_csp_download` role of [middleware_automation.redhat_csp_download](https://github.com/ansible-middleware/redhat-csp-download) collection.
To install, from the collection root directory, run:

    ansible-galaxy collections install -r requirements.yml


Versions
--------

| AMQ VERSION | Release Date      | Artemis Version | Notes           |
|:------------|:------------------|:----------------|:----------------|
| `AMQ 7.10`  | 2021.Q4           | `2.20.0`        |[Release Notes](https://access.redhat.com/documentation/en-us/red_hat_amq_broker/7.10/html/release_notes_for_red_hat_amq_broker_7.10/index)|
| `AMQ 7.9`   | 2021.Q3           | `2.18.0`        |[Release Notes](https://access.redhat.com/documentation/en-us/red_hat_amq/2021.q3/html-single/release_notes_for_red_hat_amq_broker_7.9/index)|
| `AMQ 7.8`   | 2020.Q4           | `2.16.0`        |[Release Notes](https://access.redhat.com/documentation/en-us/red_hat_amq/2020.q4/html-single/release_notes_for_red_hat_amq_broker_7.8/index)|


<!--start argument_specs-->
Role Defaults
-------------

* Install options

| Variable | Description | Default |
|:---------|:------------|:--------|
|`activemq_version`| Apache Artemis version | `2.18.0` |
|`activemq_archive`| Apache Artemis install archive filename | `apache-artemis-{{ activemq_version }}-bin.zip` |
|`activemq_download_url`| Apache Artemis download URL | `https://archive.apache.org/dist/activemq/activemq-artemis/{{ activemq_version }}/{{ activemq_archive }}` |
|`activemq_installdir`| Apache Artemis Installation path | `{{ activemq_dest }}/apache-artemis-{{ activemq_version }}` |
|`activemq_dest`| Root installation directory | `/opt/amq` |
|`activemq_offline_install`| Perform an offline installation | `False` |
|`activemq_local_archive_repository`| Path local to controller for offline/download of install archives | `{{ lookup('env', 'PWD') }}` |


* Service configuration

| Variable | Description | Default |
|:---------|:------------|:--------|
|`activemq_service_user`| POSIX user running the service | `amq-broker` |
|`activemq_service_group`| POSIX group running the service | `amq-broker` |
|`activemq_service_pidfile`| PID file for service | `data/artemis.pid` |
|`activemq_service_name`| systemd service unit name | `activemq` |


* Common configuration

| Variable | Description | Default |
|:---------|:------------|:--------|
|`activemq_instance_name`| Name of broker instance to deploy | `amq-broker` |
|`activemq_instance_username`| Username for accessing the broker instance | `amq-broker` |
|`activemq_instance_password`| Password for accessing the broker instance | `amq-broker` |
|`activemq_instance_anonymous`| Whether to allow anonymous logins to the instance | `False` |
|`activemq_configure_firewalld`| Whether to install and configure firewalld | `False` |
|`activemq_bind_address`| Service bind address | `0.0.0.0` |
|`activemq_host`| Service hostname | `localhost` |
|`activemq_http_port`| Service http port serving console and REST api | `8161` |
|`activemq_jolokia_url`| URL for jolokia REST api | `http://{{ activemq_host }}:{{ activemq_http_port }}/console/jolokia` |
|`activemq_console_url`| URL for console service | `http://{{ activemq_host }}:{{ activemq_http_port }}/console/` |
|`activemq_jvm_package`| RPM package to install for the service | `java-11-openjdk-headless` |
|`activemq_java_opts`| Additional JVM options for the service | `-Xms512M -Xmx2G [...]` |
|`activemq_port`| Main port for the broker instance | `61616` |
|`activemq_port_hornetq`| hornetq port for the broker instance | `5445` |
|`activemq_port_amqp`| AMQP port for the broker instance | `5672` |
|`activemq_port_mqtt`| MQTT port for the broker instance | `1883` |
|`activemq_port_stomp`| STOMP port for the broker instance | `61613` |
|`activemq_ports_offset_enabled`| Whether to enable port offset | `False` |
|`activemq_ports_offset`| Port offset for all default ports | `0` |
|`activemq_shared_storage`| Use shared filesystem directory for storage | `False` |
|`activemq_shared_storage_path`| Absolute path of shared directory | `{{ activemq_dest }}/{{ activemq_instance_name }}/data/shared` |
|`activemq_disable_destination_autocreate`| Disable automatic creation of destination | `True` |
|`activemq_queues`| Queue names comma separated | `queue.in,queue.out` |


* Acceptors / connectors

| Variable | Description | Default |
|:---------|:------------|:--------|
|`activemq_acceptors`| Acceptors configuration; list of `{ name(str), bind_address(str), bind_port(int), parameters(dict) }` | Generate same configuration as `artemis create` |
|`activemq_connectors`| Connectors configuration; list of `{ name(str), address(str), port(int), parameters(dict) }` | Generate same configuration as `artemis create` |

Sample acceptor:

```
  - name: amqp
    bind_address: {{ activemq_host }}
    bind_port: {{ activemq_port_amqp }}
    parameters:
      tcpSendBufferSize: 1048576
      tcpReceiveBufferSize: 1048576
      protocols: AMQP
      useEpoll: true
      amqpMinLargeMessageSize: 102400
      amqpCredits: 1000
      amqpLowCredits: 300
      amqpDuplicateDetection: true
```

Sample connector with TLS:

```
  - name: amqp
    address: 172.168.10.43
    port: 61616
    parameters:
      tcpSendBufferSize: 1048576
      tcpReceiveBufferSize: 1048576
      protocols: CORE
      useEpoll: true
      sslEnabled: True
      keyStorePath: "{{ activemq_tls_keystore_dest }}"
      keyStorePassword: "{{ activemq_tls_keystore_pasword }}"
      trustStorePath: "{{ activemq_tls_truststore_dest }}"
      trustStorePassword: "{{ activemq_tls_truststore_password }}"
      verifyHost: False
```


* Clustering

| Variable | Description | Default |
|:---------|:------------|:--------|
|`activemq_ha_enabled`| Whether to enable clustering | `False` |
|`activemq_cluster_user`| Cluster username | `amq-cluster-user` |
|`activemq_cluster_pass`| Cluster user password | `amq-cluster-pass` |
|`activemq_cluster_maxhops`| Cluster max hops | `1` |
|`activemq_cluster_lb_policy`| Policy for cluster load balancing | `ON_DEMAND` |
|`activemq_replicate`| Enables replication | `False` |
|`activemq_replicated`| Designate instance as replicated node | `False` |
|`activemq_cluster_discovery` | Cluster discovery: [`jgroups` (shared file ping), `multicast` (UDP), `static` (node list)] | `static` |


* TLS/SSL protocol

| Variable | Description | Default |
|:---------|:------------|:--------|
|`activemq_tls_enabled`| Whether to enable TLS | `False` |
|`activemq_tls_keystore_dest`| Path for installation of truststore | `{{ activemq_dest }}/{{ activemq_instance_name }}/etc/identity.ks` |
|`activemq_tls_mutual_authentication`| Whether to enable TLS mutual auth, requires TLS enabled | `False` |
|`activemq_tls_truststore_dest`| Path for installation of truststore | `{{ activemq_dest }}/{{ activemq_instance_name }}/etc/trust.ks` |

See _Role Variables_ below for additional TLS/SSL settings.


* Logging

| Variable | Description | Default |
|:---------|:------------|:--------|
|`activemq_enable_audit`| Whether to enable audit file logging | `False` |
|`activemq_logger_level`| Root logging level | `INFO` |
|`activemq_logger_core_server_level`| Logging level for org.apache.activemq.artemis.core.server | `INFO` |
|`activemq_logger_journal_level`| Logging level for org.apache.activemq.artemis.journal | `INFO` |
|`activemq_logger_utils_level`| Logging level for org.apache.activemq.artemis.utils | `INFO` |
|`activemq_logger_utils_critical_level`| Logging level for org.apache.activemq.artemis.utils.critical | `INFO` |
|`activemq_logger_jms_level`| Logging level for org.apache.activemq.artemis.jms | `INFO` |
|`activemq_logger_integration_bootstrap_level`| Logging level for org.apache.activemq.artemis.integration.bootstrap | `INFO` |
|`activemq_logger_jetty_level`| Logging level for org.eclipse.jetty | `WARN` |
|`activemq_logger_curator_level`| Logging level for org.apache.curator | `WARN` |
|`activemq_logger_zookeeper_level`| Logging level for org.apache.zookeeper | `ERROR` |


* Other options

| Variable | Description | Default |
|:---------|:------------|:--------|
|`activemq_nio_enabled`| Enable Native IO using libaio | `False` |
|`activemq_disable_amqp_protocol`| Whether to disable AMQP protocol | `False` |
|`activemq_disable_hornetq_protocol`| Whether to disable HORNETQ protocol | `False` |
|`activemq_disable_mqtt_protocol`| Whether to disable MQTT protocol | `False` |
|`activemq_disable_stomp_protocol`| Whether to disable STOMP protocol | `False` |
|`activemq_jmx_exporter_port` | Port for prometheus JMX exporter to listen | `18080` |
|`activemq_jmx_exporter_config_path`| JMX exporter configuration path |`{{ activemq_dest }}/{{ activemq_instance_name }}/etc/jmx_exporter.yml` |
|`activemq_jmx_exporter_enabled`| Enable install and configuration of prometheus-jmx-exporter | `False` |
|`activemq_prometheus_enabled`| Enable install and configuration of prometheus metrics plugin | `False` |
|`activemq_name`| Human readable service name | `Apache ActiveMQ` |
|`activemq_db_enabled`| Whether to enable JDBC persistence | `False` |
|`activemq_config_dir`| Broker instance configuration directory | `conf` |
|`activemq_config_xml`| Broker instance configuration file | `amq-broker.xml` |
|`activemq_config_override_template`| TODO document argument | `TODO` |


* User / Role configuration

| Variable | Description | Default |
|:---------|:------------|:--------|
|`activemq_users`| List of users the create with role; user is not created if password empty. List of (user,password,role) dicts | `{{ activemq_instance_username }}/{{ activemq_instance_password }}/amq` |
|`activemq_roles`| List of roles to create. List of (role,permissions) dicts where permissions is a list of amq broker permissions | `amq` |
|`activemq_hawtio_role`| Artemis role for hawtio console access | `amq` |
|`activemq_management_access_default`| Management console access methods for roles in `activemq_hawtio_role` | `[ 'list*', 'get*', 'is*', 'set*', 'browse*', 'count*', '*' ]` |
|`activemq_management_access_domains`| Management console access methods per domain for roles in `activemq_hawtio_role` | `java.lang`, `org.apache.artemis.activemq` |
|`activemq_cors_allow_origin`| CORS allow origin setting for jolokia | `*://0.0.0.0*` |
|`activemq_cors_strict_checking`| Whether to enforce strict checking for CORS | `True` |

Sample user/role configuration with one admin, a consumer and a producer:

```
    activemq_hawtio_role: admin
    activemq_users:
      - user: amq
        password: amqbrokerpass
        roles: [ admin ]
      - user: other
        password: amqotherpass
        roles: [ consumer, producer ]
    activemq_roles:
      - name: admin
        permissions: [ createNonDurableQueue, deleteNonDurableQueue, createDurableQueue, deleteDurableQueue, createAddress, deleteAddress, consume, browse, send, manage ]
      - name: consumer
        match: topics.#
        permissions: [ consume, browse ]
      - name: producer
        match: topics.#
        permissions: [ send, browse ]
```


Role Variables
--------------

| Variable | Description | Required |
|:---------|:------------|:---------|
|`activemq_java_home`| `JAVA_HOME` of installed JRE, leave empty for using specified `activemq_jvm_package` path | `no` |
|`activemq_tls_keystore_path`| Keystore path for TLS connections | when `activemq_tls_enabled` is `True` |
|`activemq_tls_keystore_password`| Keystore password for TLS connections | when `activemq_tls_enabled` is `True` |
|`activemq_tls_truststore_path`| Truststore to use for TLS mutual authentication | when `activemq_tls_mutual_authentication` is `True` |
|`activemq_tls_truststore_password`| Password for truststore | when `activemq_tls_mutual_authentication` is `True` |

<!--end argument_specs-->


Example Playbook
----------------
```
---
- hosts: all
  collections:
    - middleware_automation.amq
  roles:
    - activemq
```
