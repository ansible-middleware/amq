#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2024, Red Hat Inc.
# Copyright (c) 2024, Guido Grazioli <ggraziol@redhat.com>
# Apache License, Version 2.0 (see LICENSE or https://www.apache.org/licenses/LICENSE-2.0)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: activemq_facts
short_description: Return activemq configuration as fact data
description:
  - Return artemis activemq configuration and runtime information from the jolokia endpoint as fact data.
version_added: "2.1.0"
requirements: ["A running instance of activemq with the jolokia port open"]
extends_documentation_fragment:
  -  action_common_attributes
  -  action_common_attributes.facts
attributes:
    check_mode:
        support: full
    diff_mode:
        support: none
    facts:
        support: full
    platform:
        platforms: all
options:
    base_url:
        description:
            - URL to the activemq instance.
        type: str
        required: false
        default: http://localhost:8161
        aliases:
          - url
    broker_name:
        description:
            - Name of the broker instance
        type: str
        required: false
        default: 'amq-broker'
        aliases:
          - broker
    auth_username:
        description:
            - Username to authenticate for API access with.
        type: str
        required: true
        aliases:
          - username
    auth_password:
        description:
            - Password to authenticate for API access with.
        type: str
        required: true
        aliases:
          - password
    validate_certs:
        description:
            - Verify TLS certificates when using https.
        type: bool
        default: true
    web_origin:
        description:
            - The value to use in the Origin header for the http request
        type: str
        required: false
        default: http://0.0.0.0
    connection_timeout:
        description:
            - Controls the HTTP connections timeout period in seconds to jolokia API.
        type: int
        default: 10
    continue_on_error:
        description:
            - Stop execution or continue in case of connection error
        type: bool
        default: false
author:
  - Guido Grazioli (@guidograzioli)
'''

EXAMPLES = r'''
- name: Populate activemq facts
  middleware_automation.amq.activemq_facts:

- name: Print activemq service facts
  ansible.builtin.debug:
    var: ansible_facts.activemq
'''

RETURN = r'''
ansible_facts:
  description: Facts to add to ansible_facts about the activemq service
  returned: always
  type: complex
  contains:
    activemq:
      description: The factual representation of an activemq instance configuration.
      returned: always
      type: dict
'''

import json
import traceback

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import open_url, basic_auth_header
from ansible.module_utils.six.moves.urllib.error import HTTPError
from ansible.module_utils.common.text.converters import to_native


URL_JOLOKIA_INFO = "{url}/console/jolokia/read/org.apache.activemq.artemis:broker=!%22{broker}!%22"


class JolokiaService(object):

    def __init__(self, module):
        self.module = module
        self.baseurl = self.module.params.get('base_url')
        self.broker = self.module.params.get('broker_name')
        self.validate_certs = self.module.params.get('validate_certs')
        self.web_origin = self.module.params.get('web_origin')
        self.connection_timeout = self.module.params.get('connection_timeout')
        self.auth_username = self.module.params.get('auth_username')
        self.auth_password = self.module.params.get('auth_password')
        self.continue_on_error = self.module.params.get('continue_on_error')

    def gather_facts(self):
        """ Obtain configuration from jolokia API

        :return: dict of real, representation or None if none matching exist
        """

        jolokia_url = URL_JOLOKIA_INFO.format(url=self.baseurl, broker=self.broker)

        if not self.baseurl.lower().startswith(('http', 'https')):
            raise ValueError("base url '%s' should either start with 'http' or 'https'." % self.baseurl)

        restheaders = {}
        restheaders["Authorization"] = basic_auth_header(self.auth_username, self.auth_password)
        restheaders["Origin"] = self.web_origin

        try:
            value = json.loads(to_native(open_url(jolokia_url, method='GET',
                                                  headers=restheaders,
                                                  timeout=self.connection_timeout,
                                                  validate_certs=self.validate_certs).read()))

            if not value or "value" not in value:
                if self.continue_on_error:
                    self.module.exit_json(changed=False, skipped=True, msg="Ignoring failure to find info. Check configuration.")
                else:
                    self.module.fail_json(msg="Failed to find info. Check configuration (credentials, url, cors, ...)")

            return value["value"]

        except HTTPError as e:
            if e.code == 404:
                self.module.fail_json(msg='HTTP 404 error, check your jolokia configuration: %s' % (str(e)),
                                      exception=traceback.format_exc())
            else:
                self.module.fail_json(msg='HTTP error calling jolokia api: %s' % (str(e)),
                                      exception=traceback.format_exc())
        except ValueError as e:
            self.module.fail_json(msg='API returned incorrect JSON: %s' % (str(e)),
                                  exception=traceback.format_exc())
        except Exception as e:
            self.module.fail_json(msg='General error calling jolokia api %s' % (str(e)),
                                  exception=traceback.format_exc())


def amq_argument_spec():
    """
    Returns argument_spec of options

    :return: argument_spec dict
    """
    return dict(
        base_url=dict(type='str', aliases=['url'], required=False, default="http://localhost:8161", no_log=False),
        broker_name=dict(type='str', aliases=['broker'], required=False, default="amq-broker"),
        auth_username=dict(type='str', aliases=['username'], required=True),
        auth_password=dict(type='str', aliases=['password'], required=True, no_log=True),
        validate_certs=dict(type='bool', default=True),
        web_origin=dict(type='str', required=False, default="http://0.0.0.0", no_log=False),
        connection_timeout=dict(type='int', default=10),
        continue_on_error=dict(type='bool', default=False)
    )


def main():
    module = AnsibleModule(argument_spec=amq_argument_spec(), supports_check_mode=True,
                           required_together=([['auth_username', 'auth_password']]))
    mod = JolokiaService(module)
    svc = mod.gather_facts()
    results = dict(ansible_facts=dict(activemq=svc))
    module.exit_json(**results)


if __name__ == '__main__':
    main()
