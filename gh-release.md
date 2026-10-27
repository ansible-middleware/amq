v2.4.0
======

Minor Changes
-------------

- AMW-620 amq collection spelling and grammar checking for PRs #279
- Add support for ignore-scheme in jolokia-access.xml #276
- Replace deprecated _collections_compat import #280
- Replace deprecated top-level fact variables with ansible_fact #281

Bugfixes
--------

- AMW-592 AMW Github Actions are failing because of latest molecule #274
- AMW-594 Upstream release is failing due to recent rules change #273
- Fix LDAP passwordCodec using wrong variable in login.config.j2 #284
- Update JAVA_ARGS in artemis.profile from role variables #287
