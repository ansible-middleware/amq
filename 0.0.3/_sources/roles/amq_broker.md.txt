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
|`amq_broker_db_enabled`| Whether to enable JDBC persistence | `False` |


* Install options

| Variable | Description | Default |
|:---------|:------------|:--------|
|`amq_broker_activemq_version`| Apache Artemis version | `2.18.0` |
|`amq_broker_activemq_archive`| Apache Artemis install archive filename | `apache-artemis-{{ amq_broker_activemq_version }}-bin.zip` |
|`amq_broker_activemq_download_url`| Apache Artemis download URL | `https://archive.apache.org/dist/activemq/activemq-artemis/{{ amq_broker_activemq_version }}/{{ amq_broker_activemq_archive }}` |
|`amq_broker_activemq_installdir`| Apache Artemis Installation path | `{{ amq_broker_dest }}/apache-artemis-{{ amq_broker_activemq_version }}` |
|`amq_broker_enable`| Enable installation of Red Hat AMQ Broker | `{{ True if rhn_username is defined and rhn_password is defined else False }}` |
|`amq_broker_version`| Red Hat AMQ Broker version | `7.9.4` |
|`amq_broker_archive`| Red Hat AMQ Broker install archive filename | `amq-broker-{{ amq_broker_version }}-bin.zip` |
|`amq_broker_installdir`| Red Hat AMQ Broker installation path | `{{ amq_broker_dest }}/amq-broker-{{ amq_broker_version }}` |
|`amq_broker_dest`| Root installation directory | `/opt/amq` |
|`amq_broker_offline_install`| Perform an offline installation | `False` |


* Common configuration

| Variable | Description | Default |
|:---------|:------------|:--------|
|`amq_broker_config_dir`| Broker instance configuration directory | `conf` |
|`amq_broker_config_xml`| Broker instance configuration file | `amq-broker.xml` |
|`amq_broker_config_override_template`| TODO document argument | `TODO` |
|`amq_broker_service_user`| POSIX user running the service | `amq-broker` |
|`amq_broker_service_group`| POSIX group running the service | `amq-broker` |
|`amq_broker_instance_name`| Name of broker instance to deploy | `amq-broker` |
|`amq_broker_instance_username`| Username for accessing the broker instance | `amq-broker` |
|`amq_broker_instance_password`| Password for accessing the broker instance | `amq-broker` |
|`amq_broker_instance_anonymous`| Whether to allow anonymous logins to the instance | `False` |
|`amq_broker_service_pidfile`| PID file for service | `data/artemis.pid` |
|`amq_broker_configure_firewalld`| Whether to install and configure firewalld | `False` |
|`amq_broker_bind_address`| Service bind address | `0.0.0.0` |
|`amq_broker_host`| Service hostname | `localhost` |
|`amq_broker_http_port`| Service http port serving console and REST api | `8161` |
|`amq_broker_jolokia_url`| URL for jolokia REST api | `http://{{ amq_broker_host }}:{{ amq_broker_http_port }}/console/jolokia` |
|`amq_broker_console_url`| URL for console service | `http://{{ amq_broker_host }}:{{ amq_broker_http_port }}/console/` |
|`amq_broker_jvm_package`| RPM package to install for the service | `java-11-openjdk-headless` |
|`amq_broker_java_opts`| Additional JVM options for the service | `-Xms1024m -Xmx2048m` |
|`amq_broker_port`| Main port for the broker instance | `61616` |
|`amq_broker_port_hornetq`| hornetq port for the broker instance | `5445` |
|`amq_broker_port_amqp`| AMQP port for the broker instance | `5672` |
|`amq_broker_port_mqtt`| MQTT port for the broker instance | `1883` |
|`amq_broker_port_stomp`| STOMP port for the broker instance | `61613` |
|`amq_broker_ports_offset_enabled`| Whether to enable port offset | `False` |
|`amq_broker_ports_offset`| Port offset for all default ports | `0` |
|`amq_broker_rhn_baseurl`| Base RHN download URL for Red Hat AMQ Broker | `https://access.redhat.com/jbossnetwork/restricted/softwareDownload.html?softwareId=` |
|`amq_broker_rhn_id`| RHN Product ID for Red Hat AMQ Broker | `{{ amq_broker_rhn_ids[amq_broker_version].id }}` |


* Clustering

| Variable | Description | Default |
|:---------|:------------|:--------|
|`amq_broker_ha_enabled`| Whether to enable clustering | `False` |
|`amq_broker_cluster_user`| Cluster username | `amq-cluster-user` |
|`amq_broker_cluster_pass`| Cluster user password | `amq-cluster-pass` |
|`amq_broker_cluster_maxhops`| Cluster max hops | `1` |
|`amq_broker_cluster_lb_policy`| Policy for cluster load balancing | `ON_DEMAND` |
|`amq_broker_replicate`| Enables replication | `False` |
|`amq_broker_replicated`| Designate instance as replicated node | `False` |
|`amq_broker_cluster_discovery` | Cluster discovery: [`jgroups` (shared file ping), `multicast` (UDP), `static` (node list)] | `static` |


* TLS/SSL protocol

| Variable | Description | Default |
|:---------|:------------|:--------|
|`amq_broker_tls_enabled`| Whether to enable TLS | `False` |
|`amq_broker_tls_keystore_dest`| Path for installation of truststore | `{{ amq_broker_dest }}/{{ amq_broker_instance_name }}/etc/identity.ks` |
|`amq_broker_tls_mutual_authentication`| Whether to enable TLS mutual auth, requires TLS enabled | `False` |
|`amq_broker_tls_truststore_dest`| Path for installation of truststore | `{{ amq_broker_dest }}/{{ amq_broker_instance_name }}/etc/trust.ks` |


* Logging

| Variable | Description | Default |
|:---------|:------------|:--------|
|`amq_broker_enable_audit`| Whether to enable audit file logging | `False` |
|`amq_broker_logger_level`| Root logging level | `INFO` |
|`amq_broker_logger_core_server_level`| Logging level for org.apache.activemq.artemis.core.server | `INFO` |
|`amq_broker_logger_journal_level`| Logging level for org.apache.activemq.artemis.journal | `INFO` |
|`amq_broker_logger_utils_level`| Logging level for org.apache.activemq.artemis.utils | `INFO` |
|`amq_broker_logger_utils_critical_level`| Logging level for org.apache.activemq.artemis.utils.critical | `INFO` |
|`amq_broker_logger_jms_level`| Logging level for org.apache.activemq.artemis.jms | `INFO` |
|`amq_broker_logger_integration_bootstrap_level`| Logging level for org.apache.activemq.artemis.integration.bootstrap | `INFO` |
|`amq_broker_logger_jetty_level`| Logging level for org.eclipse.jetty | `WARN` |
|`amq_broker_logger_curator_level`| Logging level for org.apache.curator | `WARN` |
|`amq_broker_logger_zookeeper_level`| Logging level for org.apache.zookeeper | `ERROR` |


* Other options

| Variable | Description | Default |
|:---------|:------------|:--------|
|`amq_broker_nio_enabled`| Enable Native IO using libaio | `False` |
|`amq_broker_shared_storage`| Use shared filesystem directory for storage | `False` |
|`amq_broker_shared_storage_path`| Path of shared directory relative to activemq home directory | `data/shared` |
|`amq_broker_disable_destination_autocreate`| Disable automatic creation of destination | `True` |
|`amq_broker_queues`| Queue names comma separated | `queue.in,queue.out` |
|`amq_broker_disable_amqp_protocol`| Whether to disable AMQP protocol | `False` |
|`amq_broker_disable_hornetq_protocol`| Whether to disable HORNETQ protocol | `False` |
|`amq_broker_disable_mqtt_protocol`| Whether to disable MQTT protocol | `False` |
|`amq_broker_disable_stomp_protocol`| Whether to disable STOMP protocol | `False` |
|`amq_broker_jmx_exporter_port` | Port for prometheus JMX exporter to listen | `18080` |
|`amq_broker_jmx_exporter_config_path`| JMX exporter configuration path |`{{ amq_broker_dest }}/{{ amq_broker_instance_name }}/etc/jmx_exporter.yml` |
|`amq_broker_jmx_exporter_enabled`| Enable install and configuration of prometheus-jmx-exporter | `False` |
|`amq_broker_prometheus_enabled`| Enable install and configuration of prometheus metrics plugin | `False` |


Role Variables
--------------

| Variable | Description | Required |
|:---------|:------------|:---------|
|`amq_broker_java_home`| JAVA_HOME of installed JRE, leave empty for using specified amq_broker_jvm_package path | `no` |
|`amq_broker_tls_keystore_path`| Keystore path for TLS connections | when `amq_broker_tls_enabled` is `True` |
|`amq_broker_tls_keystore_password`| Keystore password for TLS connections | when `amq_broker_tls_enabled` is `True` |
|`amq_broker_tls_truststore`| Truststore to use for TLS mutual authentication | when `amq_broker_tls_mutual_authentication` is `True` |
|`amq_broker_tls_truststore_password`| Password for truststore | when `amq_broker_tls_mutual_authentication` is `True` |

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