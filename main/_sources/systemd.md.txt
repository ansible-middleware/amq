# Service configuration with systemd

After the download, installation, and configuration phases of an `activemq` role execution,
additional configuration is performed by the collection to allow the service to be controlled
as a systemd unit.


## Base systemd unit definition

The template used for the systemd unit is:

```
# {{ ansible_managed }}
[Unit]
Description={{ activemq.instance_name }} {{ activemq.name }} Service
After=network.target
{% if activemq_shared_storage and activemq_shared_storage_mounted %}
RequiresMountsFor={{ activemq_shared_storage_path }}
{% endif %}

[Service]
User={{ activemq_service_user }}
Group={{ activemq_service_group }}
Type=forking
EnvironmentFile=-/etc/sysconfig/{{ activemq.instance_name }}
PIDFile={{ activemq.instance_home }}/{{ activemq_service_pidfile }}
ExecStart={{ activemq.instance_home }}/bin/artemis-service start
ExecStop={{ activemq.instance_home }}/bin/artemis-service stop
SuccessExitStatus = 0 143
RestartSec = 120
Restart = on-failure
LimitNOFILE=102642
TimeoutSec=600
{% if activemq_systemd_wait_for_port %}
ExecStartPost=/usr/bin/timeout {{ activemq_systemd_wait_for_timeout }} sh -c 'while ! ss -H -t -l -n sport = :{{ activemq_port }} | grep -q "^LISTEN.*:{{ activemq_port }}"; do sleep 1; done && /bin/sleep {{ activemq_systemd_wait_for_delay }}'
{% endif %}
{% if activemq_systemd_wait_for_log %}
{% if activemq_ha_enabled and (activemq_ha_role == 'slave' or activemq_ha_role == 'backup') %}
ExecStartPost=/usr/bin/timeout {{ activemq_systemd_wait_for_timeout }} sh -c 'tail -n 15 -f {{ activemq.instance_home }}/log/artemis.log | sed "/AMQ221109/ q" && /bin/sleep {{ activemq_systemd_wait_for_delay }}'
{% elif activemq_ha_enabled and (activemq_ha_role == 'master' or activemq_ha_role == 'primary') %}
ExecStartPost=/usr/bin/timeout {{ activemq_systemd_wait_for_timeout }} sh -c 'tail -n 15 -f {{ activemq.instance_home }}/log/artemis.log | sed "/AMQ221001/ q" && /bin/sleep {{ activemq_systemd_wait_for_delay }}'
{% else %}
ExecStartPost=/usr/bin/timeout {{ activemq_systemd_wait_for_timeout }} sh -c 'tail -n 15 -f {{ activemq.instance_home }}/log/artemis.log | sed "/AMQ221034/ q" && /bin/sleep {{ activemq_systemd_wait_for_delay }}'
{% endif %}
{% endif %}

[Install]
WantedBy=multi-user.target
```

The notable configurations are for the paths and user/group that runs the service, in addition to the "wait_for" feature that will be discussed in the
next paragraph.

The `/etc/sysconfig/<instance_name>` is an environment variable definition file, also created and maintained by the collection, which
populates the environment for the service as follows:

```
# {{ ansible_managed }}
JAVA_ARGS='{{ activemq_java_opts }} {{ activemq_logger_opts }} {{ activemq_jmx_opts }} {{ activemq_properties_opts }}'
JAVA_HOME={{ activemq_java_home  | default(activemq_rpm_java_home, true) }}
HAWTIO_ROLE='{{ activemq_hawtio_role }}'
ARTEMIS_INSTANCE_URI='file:{{ activemq.instance_home }}/'
ARTEMIS_INSTANCE_ETC_URI='file:{{ activemq.instance_home }}/etc/'
ARTEMIS_HOME='{{ activemq.home }}'
ARTEMIS_INSTANCE='{{ activemq.instance_home }}'
{% if activemq_shared_storage %}
ARTEMIS_DATA_DIR='{{ activemq_shared_storage_path }}'
{% else %}
ARTEMIS_DATA_DIR='{{ activemq.instance_home }}/data'
{% endif %}
ARTEMIS_ETC_DIR='{{ activemq.instance_home }}/etc'
ARTEMIS_USER={{ activemq_service_user }}
```


## Configuration for HA / clustering

A few parameters are available, that when enabled (by default when ha is enabled), add configurations
to the systemd unit, so that service start/restart commands return only after certain conditions (ie. some port is open / a console log line):


| Variable | Description | Default |
|:---------|:------------|:--------|
|`activemq_systemd_wait_for_port` | Whether or not systemd unit should wait for `activemq_port` before returning | `true` when activemq_ha_enabled is `true` and activemq_shared_storage is `false` |
|`activemq_systemd_wait_for_log` | Whether or not systemd unit should wait for service to be up in logs | `true` when activemq_ha_enabled and activemq_shared_storage are `true` |
|`activemq_systemd_wait_for_timeout`| How long to wait for service to be alive (seconds)  |`60`|
|`activemq_systemd_wait_for_delay`| Activation delay for service systemd unit (seconds)  |`10`|

By default, the wait_for_port is used for replication HA, while wait_for_log for shared store HA, however, they can be individually or both together
used along with any other configuration.


## Running the systemd configuration on itself

The task file `systemd.yml` provided by the collection is also defined as an entrypoint, meaning that you can:

```yaml
- name: Configure systemd unit
  ansible.builtin.include_role:
    - name: activemq
      tasks_from: systemd
```

That allows to configure systemd on existing installation of activemq, requiring a subset of the parameters
needed by the full execution of the `activemq` role.

Here's the list of what you may need to configure to fit your environment, with the default value:

```yaml
activemq_version:
    default: "2.34.0"
    description: "Apache Artemis version"
    type: "str"
activemq_installdir:
    default: "{{ activemq_dest }}/apache-artemis-{{ activemq_version }}"
    description: "Apache Artemis Installation path"
    type: "str"
activemq_dest:
    default: "/opt/activemq"
    description: "Root installation directory"
    type: "str"
activemq_instance_name:
    default: "amq-broker"
    description: "Name of broker instance to deploy"
    type: "str"
activemq_service_user:
    default: "amq-broker"
    description: "POSIX user running the service"
    type: "str"
activemq_service_group:
    default: "amq-broker"
    description: "POSIX group running the service"
    type: "str"
activemq_jvm_package:
    default: "java-17-openjdk-headless"
    description: "RPM package to install for the service"
    type: "str"
activemq_java_home:
    required: false
    description: "JAVA_HOME of installed JRE, leave empty for using specified activemq_jvm_package path"
    type: "str"
activemq_java_opts:
    default: "{{ [ activemq_java_opts_mem, activemq_java_opts_gc, activemq_java_opts_hawtio,
                    '-Djolokia.policyLocation=file:' + activemq_dest + '/' + activemq_instance_name + '/etc/jolokia-access.xml',
                    '-Dlog4j.configurationFile=' + activemq_logger_config_template if activemq_logger_config_template != 'log4j2.properties' and activemq_logger_config_template != 'logging.properties' else '',
                    activemq_java_opts_extra | default('') ] | join(' ') }}"
    description: >
        Arguments for the service JVM; you can override this parameter that will take precedence, or
        otherwise use the activemq_java_opts_* parameters
    type: "str"
activemq_java_opts_extra:
    description: "Arbitrary extra arguments for the JVM"
    default: ""
    type: "str"
activemq_java_opts_mem:
    description: "Memory arguments for the JVM"
    default: "-Xms512M -Xmx2G"
    type: "str"
activemq_java_opts_gc:
    description: "Garbage collection arguments for the JVM"
    default: "-XX:+PrintClassHistogram -XX:+UseG1GC -XX:+UseStringDeduplication"
    type: "str"
activemq_java_opts_hawtio:
    description: "Arbitrary extra arguments for the JVM"
    default: "-Dhawtio.disableProxy=true -Dhawtio.realm=activemq -Dhawtio.offline=true -Dhawtio.rolePrincipalClasses=org.apache.activemq.artemis.spi.core.security.jaas.RolePrincipal"
    type: "str"
activemq_systemd_wait_for_port:
    description: 'Whether systemd unit should wait for activemq port before returning'
    default: "{{ activemq_ha_enabled and not activemq_shared_storage }}"
    type: 'bool'
activemq_systemd_wait_for_log:
    description: 'Whether systemd unit should wait for service to be up in logs'
    default: "{{ activemq_ha_enabled and activemq_shared_storage }}"
    type: 'bool'
activemq_systemd_wait_for_timeout:
    description: "How long to wait for service to be alive (seconds)"
    default: 60
    type: 'int'
activemq_systemd_wait_for_delay:
    description: "Activation delay for service systemd unit"
    default: 10
    type: 'int'
activemq_hawtio_role:
    description: "Artemis role for hawtio console access"
    default: "amq"
    type: "str"
```


## Verify deployment

You can now login on the target instance, and run:

```
[root@instance /]# systemctl status amq-broker
● amq-broker.service - amq-broker Apache ActiveMQ Service
     Loaded: loaded (/etc/systemd/system/amq-broker.service; enabled; preset: disabled)
     Active: active (running) since Thu 2024-08-22 09:02:33 UTC; 3h 33min ago
    Process: 4061 ExecStart=/opt/amq/amq-broker/bin/artemis-service start (code=exited, status=0/SUCCESS)
   Main PID: 4064 (java)
      Tasks: 66 (limit: 30641)
     Memory: 394.2M
        CPU: 41.030s
     CGroup: /system.slice/amq-broker.service
             └─4064 /etc/alternatives/jre_17/bin/java -Xms512M -Xmx2G -XX:+PrintClassHistogram -XX:+UseG1GC -XX:+UseStringDeduplication -Dhawtio.disableProxy=true -Dhawtio.realm=activemq -Dhawtio.offline=true -Dhawtio.rolePrincipalClasses=org.apache.activemq.artemis.spi.core.security.jaas.RolePrincipal -Djolokia.policyLocation=file:/opt/amq/amq-broker/etc/jolokia-access.xml -Dhawtio.role=admin -Djava.security.auth.login.config=/opt/amq/amq-broker/etc/login.config -classpath /opt/amq/apache-artemis-2.34.0/lib/artemis-boot.jar -Dartemis.home=/opt/amq/apache-artemis-2.34.0 -Dartemis.instance=/opt/amq/amq-broker -Djava.library.path=/opt/amq/apache-artemis-2.34.0/bin/lib/linux-x86_64 -Djava.io.tmpdir=/opt/amq/amq-broker/tmp -Ddata.dir=/opt/amq/amq-broker/data -Dartemis.instance.etc=/opt/amq/amq-broker/etc org.apache.activemq.artemis.boot.Artemis run

Aug 22 09:02:32 instance systemd[1]: Starting amq-broker Apache ActiveMQ Service...
Aug 22 09:02:32 instance artemis-service[4061]: Starting artemis-service
Aug 22 09:02:33 instance artemis-service[4061]: artemis-service is now running (4064)
Aug 22 09:02:33 instance systemd[1]: Started amq-broker Apache ActiveMQ Service.
```

The systemd journal also will be available, with:

```
[root@instance /]# journalctl -u amq-broker -n 50
Aug 22 12:37:30 instance systemd[1]: Stopping amq-broker Apache ActiveMQ Service...
Aug 22 12:37:30 instance artemis-service[6072]: Gracefully Stopping artemis-service
Aug 22 12:37:31 instance systemd[1]: amq-broker.service: Deactivated successfully.
Aug 22 12:37:31 instance systemd[1]: Stopped amq-broker Apache ActiveMQ Service.
Aug 22 12:37:31 instance systemd[1]: amq-broker.service: Consumed 42.425s CPU time.
Aug 22 12:37:31 instance systemd[1]: Starting amq-broker Apache ActiveMQ Service...
Aug 22 12:37:31 instance artemis-service[6156]: Starting artemis-service
Aug 22 12:37:32 instance artemis-service[6156]: artemis-service is now running (6159)
Aug 22 12:37:32 instance systemd[1]: Started amq-broker Apache ActiveMQ Service.
```

And eventually, the other systemctl commands: `start`, `stop`, and `restart`.

If configuration for the wait_for conditions was enabled, you'll additionally notice that the commands
do not return immediately, but only after the service is considered healthy (ie. the condition has been met).
