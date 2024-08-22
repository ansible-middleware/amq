# LDAP authentication

## Base authentication

The following new parameters allows to configure a secondary (sufficient) or primary (required) LDAP authentication endpoint.

| Variable | Description | Default |
|:---------|:------------|:--------|
|`activemq_auth_properties_enabled`| Whether to enable property based JAAS config | `True` |
|`activemq_auth_ldap_enabled` | Whether to enable LDAP based JAAS config | `False` |
|`activemq_auth_ldap_url` | URL for LDAP server connection | `ldap://localhost:389` |
|`activemq_auth_ldap_conn_username` | Bind username for LDAP server | `uid=admin,ou=system` |
|`activemq_auth_ldap_conn_password` | Bind user password for LDAP server | `password` |
|`activemq_auth_ldap_conn_codec` | Optional password codec class for bind user password | `{{ activemq_password_codec }}` |
|`activemq_auth_ldap_conn_protocol` | Protocol for LDAP connection | `s` |
|`activemq_auth_ldap_auth` | Type of LDAP server authentication | `simple` |
|`activemq_auth_ldap_user_base` | Base for user search | `ou=Users,dc=example,dc=com` |
|`activemq_auth_ldap_user_search` | User attribute | `(uid={0})` |
|`activemq_auth_ldap_user_search_subtree` | Whether to enable subtree user search | `True` |
|`activemq_auth_ldap_role_base` | Base for role search | `ou=Groups,dc=example,dc=com` |
|`activemq_auth_ldap_role_name` | Role attribute | `cn` |
|`activemq_auth_ldap_role_search` | Role search attribute | `(member={0})` |
|`activemq_auth_ldap_role_search_subtree` | Whether to enable subtree role search | `False` |
|`activemq_auth_ldap_referral` | Specify how to handle referrals; valid values: ignore, follow, throw | `ignore` |

## Configuration example

The following example shows how to connect to a test LDAP service publivly available:

```yaml
    activemq_hawtio_role: Scientists
    activemq_auth_ldap_enabled: True
    activemq_auth_ldap_url: ldap://ldap.forumsys.com:389
    activemq_auth_ldap_conn_username: uid=tesla,dc=example,dc=com
    activemq_auth_ldap_conn_password: password
    activemq_auth_ldap_user_base: dc=example,dc=com
    activemq_auth_ldap_user_search: '(uid={0})'
    activemq_auth_ldap_role_base: dc=example,dc=com
    activemq_auth_ldap_role_name: cn
    activemq_auth_ldap_role_search: '(uniqueMember={0})'
    activemq_auth_ldap_role_search_subtree: True
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
      - name: Scientists
        permissions: [ createNonDurableQueue, deleteNonDurableQueue, createDurableQueue, deleteDurableQueue, createAddress, deleteAddress, consume, browse, send, manage ]
```

It will authenticate and authorized LDAP users in the "Scientists" group; in addition to `amq` and `other` defined in property files.


## Custom jaas login.config file

It is possible to use the following parameter to use a custom template, to be made available in playbooks file lookup paths, instead of the configuration
described above (which will in this case be ignored, unless the same parameters are used for the custom template).


| Variable | Description | Default |
|:---------|:------------|:--------|
|`activemq_auth_template` | Location of JAAS login.config template; by default use template provided with role | `login.config.j2` |
