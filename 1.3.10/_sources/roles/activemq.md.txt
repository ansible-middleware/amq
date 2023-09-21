activemq
========

Installs and configures [Apache ActiveMQ Artemis](https://activemq.apache.org/components/artemis/) services.


Dependencies
------------

The role depends on the following collections:

* [middleware_automation.common](https://github.com/ansible-middleware/common)
* [ansible.posix](https://github.com/ansible-collections/ansible.posix)

To install, from the collection root directory, run:

    ansible-galaxy collections install -r requirements.yml


Versions
--------

| AMQ VERSION | Release Date      | Artemis Version | Notes           |
|:------------|:------------------|:----------------|:----------------|
| `AMQ 7.11`  | 2023.Q2           | `2.21.0`        |[Release Notes](https://access.redhat.com/documentation/en-us/red_hat_amq_broker/7.11/html/release_notes_for_red_hat_amq_broker_7.11/index)|
| `AMQ 7.10`  | 2021.Q4           | `2.21.0`        |[Release Notes](https://access.redhat.com/documentation/en-us/red_hat_amq_broker/7.10/html/release_notes_for_red_hat_amq_broker_7.10/index)|
| `AMQ 7.9`   | 2021.Q3           | `2.18.0`        |[Release Notes](https://access.redhat.com/documentation/en-us/red_hat_amq/2021.q3/html-single/release_notes_for_red_hat_amq_broker_7.9/index)|
| `AMQ 7.8`   | 2020.Q4           | `2.16.0`        |[Release Notes](https://access.redhat.com/documentation/en-us/red_hat_amq/2020.q4/html-single/release_notes_for_red_hat_amq_broker_7.8/index)|


<!--start argument_specs-->
Role Defaults
-------------

#### Install options

| Variable | Description | Default |
|:---------|:------------|:--------|
|`activemq_version`| Apache Artemis version | `2.21.0` |
|`activemq_archive`| Apache Artemis install archive filename | `apache-artemis-{{ activemq_version }}-bin.zip` |
|`activemq_download_url`| Apache Artemis download URL | `https://archive.apache.org/dist/activemq/activemq-artemis/{{ activemq_version }}/{{ activemq_archive }}` |
|`activemq_installdir`| Apache Artemis Installation path | `{{ activemq_dest }}/apache-artemis-{{ activemq_version }}` |
|`activemq_dest`| Root installation directory | `/opt/amq` |
|`activemq_offline_install`| Perform an offline installation | `False` |
|`activemq_local_archive_repository`| Path local to controller for offline/download of install archives | `{{ lookup('env', 'PWD') }}` |


#### Service configuration

| Variable | Description | Default |
|:---------|:------------|:--------|
|`activemq_service_user`| POSIX user running the service | `amq-broker` |
|`activemq_service_group`| POSIX group running the service | `amq-broker` |
|`activemq_service_pidfile`| PID file for service | `data/artemis.pid` |
|`activemq_service_name`| systemd service unit name | `activemq` |
|`activemq_service_user_home`| Service user home directory, defaults to artemis installation directory | `{{ activemq_dest }}/apache-artemis-{{ activemq_version }}` |


#### Common configuration

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
|`activemq_shared_storage_mounted`| Whether the systemd unit must require a mounted path (only when using shared storage) | `True` |
|`activemq_disable_destination_autocreate`| Disable automatic creation of destination | `True` |
|`activemq_queues`| Queue names comma separated | `queue.in,queue.out` |
|`activemq_configuration_file_refresh_period`| Periodic refresh of configuration in milliseconds; can be disabled by specifying -1 | `5000` |
|`activemq_password_codec`| Fully qualified class name and its parameters for the Decoder used to decode the masked password. Ignored if activemq_mask_password is false. |`org.apache.activemq.artemis.utils.DefaultSensitiveStringCodec` |
|`activemq_mask_password` | Whether passwords in server configuration need to be masked. | `True` |
|`activemq_additional_libs`| List of jars to install in activemq classpath, read from playbook files lookup paths | `[]` |
|`activemq_mask_password_hashname`| Name of algorithm used for masking password, will be passed to custom codec | `sha1` |
|`activemq_mask_password_iterations`| Number of iterations for masking password, will be passed to custom codec | `1024` |


#### LDAP authN/authZ

| Variable | Description | Default |
|:---------|:------------|:--------|
|`activemq_auth_properties_enabled`| Whether to enable property based JAAS config | `True` |
|`activemq_auth_ldap_enabled` | Whether to enable LDAP based JAAS config" | `False` |
|`activemq_auth_ldap_url` | URL for LDAP server connection" | `ldap://localhost:389` |
|`activemq_auth_ldap_conn_username` | Bind username for LDAP server" | `uid=admin,ou=system` |
|`activemq_auth_ldap_conn_password` | Bind user password for LDAP server" | `password` |
|`activemq_auth_ldap_conn_codec` | Optional password codec class for bind user password" | `{{ activemq_password_codec }}` |
|`activemq_auth_ldap_conn_protocol` | Protocol for LDAP connection" | `s` |
|`activemq_auth_ldap_auth` | Type of LDAP server authentication" | `simple` |
|`activemq_auth_ldap_user_base` | Base for user search | `ou=Users,dc=example,dc=com` |
|`activemq_auth_ldap_user_search` | User attribute | `(uid={0})` |
|`activemq_auth_ldap_user_search_subtree` | Whether to enable subtree user search | `True` |
|`activemq_auth_ldap_role_base` | Base for role search | `ou=Groups,dc=example,dc=com` |
|`activemq_auth_ldap_role_name` | Role attribute | `cn` |
|`activemq_auth_ldap_role_search` | Role search attribute | `(member={0})` |
|`activemq_auth_ldap_role_search_subtree` | Whether to enable subtree role search | `False` |


#### Journal configuration

| Variable | Description | Default |
|:---------|:------------|:--------|
|`activemq_global_max_messages`| Number of messages before all addresses will enter into their Full Policy configured. It works in conjunction with activemq_global_max_size, being whatever value hits its maximum first. | `-1` |
|`activemq_global_max_size` | Size (in bytes) before all addresses will enter into their Full Policy configured upon messages being produced. Supports byte notation like 'K', 'Mb', 'MiB', 'GB', etc. | `'-1'` |
|`activemq_data_directory`| The activemq data directory path | `data/`, or the value of `activemq_shared_storage_path` if activemq_shared_storage is set |
|`activemq_persistence_enabled`| Whether to use the file based journal for persistence | `True` |
|`activemq_persist_id_cache`| Whether to persist cache IDs to the journal | `True` |
|`activemq_id_cache_size`| The duplicate detection circular cache size | `20000` |
|`activemq_journal_type`| Journal type, valid values are [ `ASYNCIO`: libaio, `MAPPED`: mmap files, `NIO`: Plain Java Files  ] | `ASYNCIO` |
|`activemq_paging_directory`| The directory to store paged messages in | `data/paging` |
|`activemq_bindings_directory`| The folder in use for the bindings folder | `data/bindings` |
|`activemq_journal_directory`| The directory to store the journal files in | `data/journal` |
|`activemq_large_messages_directory`| The directory to store large messages | `data/largemessages` |
|`activemq_journal_datasync`| Whether to use msync/fsync on journal operations | `True` |
|`activemq_journal_min_files`| How many journal files to pre-create | `2` |
|`activemq_journal_pool_files`| The upper threshold of the journal file pool, -1 means no Limit | `10` |
|`activemq_journal_device_block_size`| The block size by the device | `4096` |
|`activemq_journal_file_size`| The size (in bytes) of each journal file | `10M` |
|`activemq_journal_buffer_timeout`| The Flush timeout for the journal buffer | `500000` if 'ASYNCIO' else `3333333` |
|`activemq_journal_max_io`| The maximum number of write requests that can be in the ASYNCIO queue at any one time | `4096` if 'ASYNCIO' else `1` |
|`activemq_db_enabled`| Whether to enable JDBC persistence | `False` |
|`activemq_db_jdbc_url`| The full JDBC connection URL for your database server | `jdbc:derby:target/derby/database-store;create=true` |
|`activemq_db_bindings_table`| The name of the table in which bindings data will be persisted | `BINDINGS_TABLE` |
|`activemq_db_message_table`| The name of the table in which bindings data will be persisted | `MESSAGE_TABLE` |
|`activemq_db_large_message_table`| The name of the table in which messages and related data will be persisted | `LARGE_MESSAGES_TABLE` |
|`activemq_db_jdbc_driver_class`| The fully qualified class name of the desired database Driver | `org.apache.derby.jdbc.EmbeddedDriver` |


#### Acceptors / connectors

| Variable | Description | Default |
|:---------|:------------|:--------|
|`activemq_acceptors`| Acceptors configuration; list of `{ name(str), bind_address(str), bind_port(int), parameters(dict) }` | Generate same configuration as `artemis create` |
|`activemq_connectors`| Connectors configuration; list of `{ name(str), address(str), port(int), parameters(dict) }` | Generate same configuration as `artemis create` |

Sample acceptor:

```yaml
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

```yaml
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
      keyStorePassword: "{{ activemq_tls_keystore_password }}"
      trustStorePath: "{{ activemq_tls_truststore_dest }}"
      trustStorePassword: "{{ activemq_tls_truststore_password }}"
      verifyHost: False
```


#### Addresses configuration

| Variable | Description | Default |
|:---------|:------------|:--------|
|`activemq_addresses`| Addresses/queue configuration; list of `{ name, [anycast or multicast], and parameters }` | Generate same configuration as `artemis create` |

Sample addresses:

```yaml
  - name: ExpiryQueue
    anycast:
      - name: ExpiryQueue
  - name: Virtual
    anycast:
      - name: Virtual
        filter: "discard='true'"
        max_consumers: 5
        consumers_before_dispatch: 1
```


#### Address settings

| Variable | Description | Default |
|:---------|:------------|:--------|
|`activemq_address_settings`| Address settings configuration; list of `{ match address string and parameters(dict) }` | "Generate same configuration as `artemis create`" |

Sample address settings:

```yaml
  - match: activemq.management#
    parameters:
      dead_letter_address: DLQ
      expiry_address: ExpiryQueue
      redelivery_delay: 0
      max_size_bytes: -1
      message_counter_history_day_limit: 10
      address_full_policy: PAGE
      auto_create_queues: true
      auto_create_addresses: true
      auto_create_jms_queues: true
      auto_create_jms_topics: true
```

The parameters are snake_cased variants of the artemis configuration schema elements, which are kebab-cased (ie. `dead-letter-address` -> `dead_letter_address`).


#### Diverts configuration

| Variable | Description | Default |
|:---------|:------------|:--------|
|`activemq_diverts`| Diverts configuration; list of `{ name with parameters }` | `[]` |

Sample divert:

```yaml
  - name: SAMPLEDIVERT
    address: FROMQUEUE
    forwarding_address: TOQUEUE
    routing_type: ANYCAST
    filter: "msgType LIKE '%ff%'"
    exclusive: True
```


#### Clustering

| Variable | Description | Default |
|:---------|:------------|:--------|
|`activemq_ha_enabled`| Whether to enable clustering | `False` |
|`activemq_cluster_user`| Cluster username | `amq-cluster-user` |
|`activemq_cluster_pass`| Cluster user password | `amq-cluster-pass` |
|`activemq_cluster_maxhops`| Cluster max hops | `1` |
|`activemq_cluster_lb_policy`| Policy for cluster load balancing | `ON_DEMAND` |
|`activemq_ha_role` | Instance role for high availability | `live-only` |
|`activemq_replicate`| Enables replication | `False` |
|`activemq_replicated`| Designate instance as replicated node | `False` |
|`activemq_cluster_discovery` | Cluster discovery: [`jgroups` (shared file ping), `multicast` (UDP), `static` (node list)] | `static` |
|`activemq_cluster_iface` | The NIC name to be used for cluster IPv4 addresses (ie. 'eth0') | `default_ipv4` |
|`activemq_systemd_wait_for_port` | Whether systemd unit should wait for activemq port before returning | `True` when activemq_ha_enabled is `True` and activemq_shared_storage is `False` |
|`activemq_systemd_wait_for_log` | Whether systemd unit should wait for service to be up in logs | `True` when activemq_ha_enabled and activemq_shared_storage are `True` |
|`activemq_systemd_wait_for_timeout`| How long to wait for service to be alive (seconds) | `60` |
|`activemq_systemd_wait_for_delay`| Activation delay for service systemd unit | `10` |


#### Multi-site fault-tolerance (AMQP broker connections)

| Variable | Description | Default |
|:---------|:------------|:--------|
|`activemq_broker_connections`| AMQP broker connections configuration; list of `{ name(str),uri(str),operations(list of dicts with type key in [mirror,sender,receiver,peer])) }` | `[]` |

Sample of mirroring operation:

```yaml
activemq_broker_connections:
  - uri: 'tcp://<hostname>:<port>'
    name: DC2
    sync: true
    operations:
      - type: mirror
        parameters:
          queue-removal: false
```

Sample for sender-receiver operation:

```yaml
activemq_broker_connections:
  - uri: 'tcp://<hostname>:<port>'
    name: other-server
    operations:
      - type: sender
        parameters:
          address-match: 'queues.#'
      - type: receiver
        parameters:
          address-match: 'remotequeues.#'
```

Notice the local queues for `remotequeues.#` need to be created on this broker.


#### TLS/SSL protocol

| Variable | Description | Default |
|:---------|:------------|:--------|
|`activemq_tls_enabled`| Whether to enable TLS | `False` |
|`activemq_tls_keystore_dest`| Path for installation of truststore | `{{ activemq_dest }}/{{ activemq_instance_name }}/etc/identity.ks` |
|`activemq_tls_mutual_authentication`| Whether to enable TLS mutual auth, requires TLS enabled | `False` |
|`activemq_tls_truststore_dest`| Path for installation of truststore | `{{ activemq_dest }}/{{ activemq_instance_name }}/etc/trust.ks` |

See _Role Variables_ below for additional TLS/SSL settings.


#### Logging

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
|`activemq_logger_rollover_files`| Number of rollover log files | `5`|
|`activemq_logger_audit_rollover_files`| Number of rollover audit log files | `5` |


#### Other options

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
|`activemq_jmx_exporter_package`| The rpm package name providing JMX exporter | `prometheus-jmx-exporter-openjdk11` |
|`activemq_prometheus_enabled`| Enable install and configuration of prometheus metrics plugin | `False` |
|`activemq_name`| Human readable service name | `Apache ActiveMQ` |
|`activemq_config_dir`| Broker instance configuration directory | `conf` |
|`activemq_config_xml`| Broker instance configuration file | `amq-broker.xml` |
|`activemq_config_override_template`| Filename of custom broker xml configuration file to be deployed | `''` |
|`activemq_service_override_template`| Filename of custom systemd unit template to be deployed | `''` |


#### User / Role configuration

| Variable | Description | Default |
|:---------|:------------|:--------|
|`activemq_users`| List of users the create with role; user is not created if password empty. List of (user,password,role) dicts | `{{ activemq_instance_username }}/{{ activemq_instance_password }}/amq` |
|`activemq_roles`| List of roles to create. List of (role,permissions) dicts where permissions is a list of amq broker permissions | `amq` |
|`activemq_hawtio_role`| Artemis role for hawtio console access | `amq` |
|`activemq_management_access_default`| Management console access methods for roles in `activemq_hawtio_role` | `[ 'list*', 'get*', 'is*', 'set*', 'browse*', 'count*', '*' ]` |
|`activemq_management_access_domains`| Management console access methods per domain for roles in `activemq_hawtio_role` | `java.lang`, `org.apache.artemis.activemq` |
|`activemq_cors_allow_origin`| List of CORS allow origin setting for jolokia | `[ *://0.0.0.0* ]` |
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
