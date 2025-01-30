========================================
middleware\_automation.amq Release Notes
========================================

.. contents:: Topics

v2.2.8
======

Bugfixes
--------

- Add missing index to log4j2 filePattern `#202 <https://github.com/ansible-middleware/amq/pull/202>`_

v2.2.7
======

Bugfixes
--------

- Fix password masking JAVA_HOME and undefined variable error `#198 <https://github.com/ansible-middleware/amq/pull/198>`_

v2.2.6
======

Minor Changes
-------------

- Add parameter ``activemq_logger_filepath`` to configure logfile path `#187 <https://github.com/ansible-middleware/amq/pull/187>`_
- Add role expansion parameters for ldap/AD configuration `#193 <https://github.com/ansible-middleware/amq/pull/193>`_

Bugfixes
--------

- Force ``activemq_configuration_file_refresh_period`` integer type in handler `#191 <https://github.com/ansible-middleware/amq/pull/191>`_
- Improve execution time for masked passwords `#194 <https://github.com/ansible-middleware/amq/pull/194>`_

v2.2.5
======

Bugfixes
--------

- Fix invalid ``broker-connections`` when boolean options are used `#179 <https://github.com/ansible-middleware/amq/pull/179>`_
- Update default for ``activemq_systemd_wait_for_log_ha_string`` `#186 <https://github.com/ansible-middleware/amq/pull/186>`_

v2.2.4
======

Bugfixes
--------

- Fix broker.xml connector and connector-ref when using federation `#178 <https://github.com/ansible-middleware/amq/pull/178>`_
- New parameter to configure clustering without HA `#175 <https://github.com/ansible-middleware/amq/pull/175>`_

v2.2.3
======

Bugfixes
--------

- Check broadcast/discovery groups absent with ``provided`` discovery `#174 <https://github.com/ansible-middleware/amq/pull/174>`_

v2.2.2
======

Minor Changes
-------------

- New parameter value to explicitly list ``cluster-connections`` `#168 <https://github.com/ansible-middleware/amq/pull/168>`_
- Parameters for ``activemq_addresses`` as a dictionary `#171 <https://github.com/ansible-middleware/amq/pull/171>`_

Bugfixes
--------

- Prevent some configs to generate non-unique ``connector-ref`` in ``cluster-connections`` `#170 <https://github.com/ansible-middleware/amq/pull/170>`_

v2.2.1
======

Minor Changes
-------------

- Add ``web_origin`` parameter to ``activemq_facts`` module `#167 <https://github.com/ansible-middleware/amq/pull/167>`_
- Add critical analyzer configuration `#162 <https://github.com/ansible-middleware/amq/pull/162>`_
- Add more journal configs `#161 <https://github.com/ansible-middleware/amq/pull/161>`_
- New ``activemq_console_bind_url`` parameter `#164 <https://github.com/ansible-middleware/amq/pull/164>`_
- New ``activemq_systemd_expand_environment`` parameter `#165 <https://github.com/ansible-middleware/amq/pull/165>`_

Bugfixes
--------

- Fix condition for transferring key/trust store `#163 <https://github.com/ansible-middleware/amq/pull/163>`_
- Fix scenarios where duplicate XInclude can be present `#166 <https://github.com/ansible-middleware/amq/pull/166>`_

v2.2.0
======

Major Changes
-------------

- Broker modular configuration with XInclude `#159 <https://github.com/ansible-middleware/amq/pull/159>`_
- New activemq_uninstall role `#150 <https://github.com/ansible-middleware/amq/pull/150>`_

Minor Changes
-------------

- Add additional ha-policy parameters `#155 <https://github.com/ansible-middleware/amq/pull/155>`_
- Add network check parameters `#152 <https://github.com/ansible-middleware/amq/pull/152>`_
- Add wait_for configuration `#156 <https://github.com/ansible-middleware/amq/pull/156>`_
- Allow to configure message counters `#153 <https://github.com/ansible-middleware/amq/pull/153>`_
- Broker plugins support `#160 <https://github.com/ansible-middleware/amq/pull/160>`_
- Define systemd entrypoint `#151 <https://github.com/ansible-middleware/amq/pull/151>`_

Bugfixes
--------

- Allow mixing masked and unmasked passwords `#149 <https://github.com/ansible-middleware/amq/pull/149>`_
- Use bind_address instead of hostname for console binding `#158 <https://github.com/ansible-middleware/amq/pull/158>`_

v2.1.1
======

Minor Changes
-------------

- Add fact gathering module for amq `#145 <https://github.com/ansible-middleware/amq/pull/145>`_
- Add ha with replication policy `#147 <https://github.com/ansible-middleware/amq/pull/147>`_
- Allow to configure broker properties with properties file `#143 <https://github.com/ansible-middleware/amq/pull/143>`_

Bugfixes
--------

- Update jolokia access when bind host and port are changed `#146 <https://github.com/ansible-middleware/amq/pull/146>`_

v2.1.0
======

Major Changes
-------------

- Update default jdk11 to jdk17 `#132 <https://github.com/ansible-middleware/amq/pull/132>`_

Minor Changes
-------------

- Add config for in-vm acceptors/connectors `#135 <https://github.com/ansible-middleware/amq/pull/135>`_
- Federated addressing `#137 <https://github.com/ansible-middleware/amq/pull/137>`_
- Update to artemis 2.34.0 / amq_broker 7.12 `#136 <https://github.com/ansible-middleware/amq/pull/136>`_

v2.0.2
======

Minor Changes
-------------

- Set minimum ansible-core version to >=2.15 `#127 <https://github.com/ansible-middleware/amq/pull/127>`_

Bugfixes
--------

- Artemis command to create broker instance uses correct JAVA_HOME `#125 <https://github.com/ansible-middleware/amq/pull/125>`_
- Fix ``broker-connections`` templating error, add missing parameters `#133 <https://github.com/ansible-middleware/amq/pull/133>`_
- Fix configuration of multicast addresses/queues `#131 <https://github.com/ansible-middleware/amq/pull/131>`_
- Improve validations for offline installs `#124 <https://github.com/ansible-middleware/amq/pull/124>`_

v2.0.1
======

Minor Changes
-------------

- Parameter ``activemq_logger_config_template`` allows relative paths `#116 <https://github.com/ansible-middleware/amq/pull/116>`_
- Update activemq default to 2.32 / amq_broker to 7.11.6 `#118 <https://github.com/ansible-middleware/amq/pull/118>`_

Bugfixes
--------

- ``activemq_config_override_template`` allows to use custom broker.xml templates `#117 <https://github.com/ansible-middleware/amq/pull/117>`_

v2.0.0
======

Minor Changes
-------------

- Add referrer to ldap plugin, allow custom login.config `#110 <https://github.com/ansible-middleware/amq/pull/110>`_
- Update activemq default version to 2.28 `#111 <https://github.com/ansible-middleware/amq/pull/111>`_

Breaking Changes / Porting Guide
--------------------------------

- Set Ansible required version to >= 2.14 `#108 <https://github.com/ansible-middleware/amq/pull/108>`_

New Plugins
-----------

Filter
~~~~~~

- middleware_automation.amq.lists_mergeby - Merge two or more lists of dictionaries by a given attribute

v1.3.10
=======

Minor Changes
-------------

- Add LDAP plugin configuration to JAAS login.config `#96 <https://github.com/ansible-middleware/amq/pull/96>`_
- Add custom codec configurations for masked passwords `#95 <https://github.com/ansible-middleware/amq/pull/95>`_

Bugfixes
--------

- Ignore unwanted output from ``artemis mask`` command `#98 <https://github.com/ansible-middleware/amq/pull/98>`_

v1.3.9
======

Minor Changes
-------------

- Add parameters for ``global-max-size`` and ``global-max-messages`` `#92 <https://github.com/ansible-middleware/amq/pull/92>`_
- Add parameters to configure log4j2 rolling strategy `#94 <https://github.com/ansible-middleware/amq/pull/94>`_
- Default version for activemq updated to 2.21 `#93 <https://github.com/ansible-middleware/amq/pull/93>`_

v1.3.8
======

Minor Changes
-------------

- Update to connectors config (add parameter for NIC name selection) `#84 <https://github.com/ansible-middleware/amq/pull/84>`_

Bugfixes
--------

- Fix incorrectly defined default for ``amq_broker_logger_config_template`` `#86 <https://github.com/ansible-middleware/amq/pull/86>`_

v1.3.7
======

Minor Changes
-------------

- Allow to set arbitrary service user home_dir `#83 <https://github.com/ansible-middleware/amq/pull/83>`_

Bugfixes
--------

- Default java_home path uses alternatives `#82 <https://github.com/ansible-middleware/amq/pull/82>`_

v1.3.6
======

Minor Changes
-------------

- Set systemd unit to run with ``activemq_system_user`` user `#78 <https://github.com/ansible-middleware/amq/pull/78>`_

Bugfixes
--------

- Update logging facade config (by activemq version) `#76 <https://github.com/ansible-middleware/amq/pull/76>`_

v1.3.5
======

Bugfixes
--------

- Update package name for prometheus plugin class `#74 <https://github.com/ansible-middleware/amq/pull/74>`_

v1.3.4
======

Minor Changes
-------------

- Provide AMQP broker-connections configuration `#70 <https://github.com/ansible-middleware/amq/pull/70>`_
- Use middleware_automation.common xml plugin `#72 <https://github.com/ansible-middleware/amq/pull/72>`_

Bugfixes
--------

- Handle case when install zipfile root is not expected `#73 <https://github.com/ansible-middleware/amq/pull/73>`_

v1.3.3
======

Bugfixes
--------

- Restore wait_for_log string in live-only ha `#68 <https://github.com/ansible-middleware/amq/pull/68>`_

v1.3.2
======

Minor Changes
-------------

- Provide ha-policy implementation `#66 <https://github.com/ansible-middleware/amq/pull/66>`_

v1.3.1
======

Bugfixes
--------

- Avoid generating duplicated security-settings match elements `#65 <https://github.com/ansible-middleware/amq/pull/65>`_

v1.3.0
======

Major Changes
-------------

- Configuration pre-install validation against schema `#58 <https://github.com/ansible-middleware/amq/pull/58>`_

Minor Changes
-------------

- Remove dependency on community.general collection `#59 <https://github.com/ansible-middleware/amq/pull/59>`_
- Switch middleware_automation.redhat_csp_download for middleware_automation.common `#60 <https://github.com/ansible-middleware/amq/pull/60>`_

v1.2.0
======

Major Changes
-------------

- Type for ``activemq_cors_allow_origin`` changed from string to list of strings `#53 <https://github.com/ansible-middleware/amq/pull/53>`_

Minor Changes
-------------

- Add address/queue configuration `#51 <https://github.com/ansible-middleware/amq/pull/51>`_
- Add configuration parameters for journal `#43 <https://github.com/ansible-middleware/amq/pull/43>`_
- Add configuration variables for address settings `#49 <https://github.com/ansible-middleware/amq/pull/49>`_
- Add diverts configuration `#52 <https://github.com/ansible-middleware/amq/pull/52>`_
- Don't trigger restarts when config auto-refresh is enabled `#54 <https://github.com/ansible-middleware/amq/pull/54>`_
- New flags make systemd unit wait for activemq ports or logs `#50 <https://github.com/ansible-middleware/amq/pull/50>`_

Bugfixes
--------

- Add ``activemq_data_directory`` variable `#57 <https://github.com/ansible-middleware/amq/pull/57>`_
- Fix templating error when acceptors or connectors have a single parameter `#47 <https://github.com/ansible-middleware/amq/pull/47>`_
- Hide secrets from playbook output `#45 <https://github.com/ansible-middleware/amq/pull/45>`_

v1.1.1
======

Bugfixes
--------

- Add systemd RequiresMountsFor and unit custom template `#36 <https://github.com/ansible-middleware/amq/pull/36>`_
- Stop using ansible.builtin.command module arguments incompatible with ansible 2.14

v1.1.0
======

Major Changes
-------------

- Allow for listing roles for users. Specify security setting match address `#19 <https://github.com/ansible-middleware/amq/pull/19>`_
- Make variable ``activemq_shared_storage_path`` represent an absolute path `#21 <https://github.com/ansible-middleware/amq/pull/21>`_

Minor Changes
-------------

- Arbitrary acceptors configuration via ``activemq_acceptors`` variable `#30 <https://github.com/ansible-middleware/amq/pull/30>`_
- Arbitrary connectors configuration via ``activemq_connectors`` variable `#31 <https://github.com/ansible-middleware/amq/pull/31>`_
- Configuration for management role access `#29 <https://github.com/ansible-middleware/amq/pull/29>`_
- Variable to config controller download/offline directory `#18 <https://github.com/ansible-middleware/amq/pull/18>`_

Breaking Changes / Porting Guide
--------------------------------

- Rename role ``amq_broker`` to ``activemq`` `#26 <https://github.com/ansible-middleware/amq/pull/26>`_
- Rename variables prefix to ``activemq_`` `#11 <https://github.com/ansible-middleware/amq/pull/11>`_

Bugfixes
--------

- Add ``become_user`` to artemis commands `#17 <https://github.com/ansible-middleware/amq/pull/17>`_
- Correctly set etc path and allow cors config for jolokia `#24 <https://github.com/ansible-middleware/amq/pull/24>`_
- Implement idempotent user password hashes `#25 <https://github.com/ansible-middleware/amq/pull/25>`_
- Update ``activemq_java_opts`` to be same as activemq defaults `#20 <https://github.com/ansible-middleware/amq/pull/20>`_

v1.0.0
======

Minor Changes
-------------

- Configuration for users and roles `#7 <https://github.com/ansible-middleware/amq/pull/7>`_
- Perform artemis post-upgrade operations on existing instances `#8 <https://github.com/ansible-middleware/amq/pull/8>`_

v0.0.3
======

Minor Changes
-------------

- Add prometheus metrics export plugin `#6 <https://github.com/ansible-middleware/amq/pull/6>`_
- Add vars and template for logging configuration `#4 <https://github.com/ansible-middleware/amq/pull/4>`_
- Add vars for prometheus_jmx_exporter setup `#5 <https://github.com/ansible-middleware/amq/pull/5>`_

v0.0.2
======

Major Changes
-------------

- amq_broker: configuration of static cluster `#3 <https://github.com/ansible-middleware/amq/pull/3>`_

v0.0.1
======

Minor Changes
-------------

- Import artemis create configuration tasks `#1 <https://github.com/ansible-middleware/amq/pull/1>`_
