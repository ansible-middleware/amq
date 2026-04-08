from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.errors import AnsibleFilterError

DOCUMENTATION = '''
  name: create_security_matches
  short_description: Create security settings matches from AMQ broker roles
  version_added: 2.3.6
  description:
    - Processes AMQ broker roles and permissions to create security settings matches.
  positional: _input
  options:
    _input:
      description: List of AMQ broker role dictionaries.
      type: list
      elements: dictionary
      required: true
  notes:
    - Each role dict should have 'name' (required), 'match' (optional, defaults to '#'), and 'permissions' (list).
  author:
    - Martin Cihlar (mcihlar@redhat.com)
'''

EXAMPLES = '''
# Create security settings matches from roles
- name: Create security settings
  ansible.builtin.set_fact:
    security_settings_matches: "{{ activemq_roles | middleware_automation.amq.create_security_matches }}"
'''

RETURN = '''
  _value:
    description: Dictionary mapping match patterns to permissions and roles.
    type: dict
    returned: always
'''


def create_security_matches(amq_broker_roles):
    """
    Build security settings matches from AMQ broker roles.

    Efficiently processes roles and permissions without expensive
    subelements/combine operations.

    Args:
        amq_broker_roles: List of role dicts with 'name', 'match', 'permissions'

    Returns:
        Dict of {match_pattern: {permission: [role_names]}}
    """
    if not isinstance(amq_broker_roles, list):
        raise AnsibleFilterError(
            'create_security_matches requires a list of roles'
        )

    result = {}

    for role in amq_broker_roles:
        role_name = role.get('name')
        if not role_name:
            continue

        match_pattern = role.get('match') or '#'
        permissions = role.get('permissions', [])

        if match_pattern not in result:
            result[match_pattern] = {}

        for permission in permissions:
            if permission not in result[match_pattern]:
                result[match_pattern][permission] = []

            result[match_pattern][permission].append(role_name)

    return result


class FilterModule(object):
    """AMQ security settings filter plugin"""

    def filters(self):
        return {
            'create_security_matches': create_security_matches,
        }
