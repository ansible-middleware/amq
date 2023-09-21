
.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. role:: ansible-attribute-support-label
.. role:: ansible-attribute-support-property
.. role:: ansible-attribute-support-full
.. role:: ansible-attribute-support-partial
.. role:: ansible-attribute-support-none
.. role:: ansible-attribute-support-na
.. role:: ansible-option-type
.. role:: ansible-option-elements
.. role:: ansible-option-required
.. role:: ansible-option-versionadded
.. role:: ansible-option-aliases
.. role:: ansible-option-choices
.. role:: ansible-option-choices-default-mark
.. role:: ansible-option-default-bold
.. role:: ansible-option-configuration
.. role:: ansible-option-returned-bold
.. role:: ansible-option-sample-bold

.. Anchors

.. _ansible_collections.middleware_automation.amq.pbkdf2_hmac_filter:

.. Anchors: short name for ansible.builtin

.. Title

pbkdf2_hmac -- Generate a salted PBKDF2\_HMAC password hash
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This filter plugin is part of the `middleware_automation.amq collection <https://galaxy.ansible.com/middleware_automation/amq>`_.

    To install it, use: :code:`ansible-galaxy collection install middleware\_automation.amq`.

    To use it in a playbook, specify: :code:`middleware_automation.amq.pbkdf2_hmac`.

.. version_added

.. rst-class:: ansible-version-added

New in middleware\_automation.amq 1.1.0

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Generate a salted one-way PBKDF2 HMAC\_password hash


.. Aliases


.. Requirements





.. Input

Input
-----

This describes the input of the filter, the value before ``| middleware_automation.amq.pbkdf2_hmac``.

.. rst-class:: ansible-option-table

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-_input"></div>

      .. _ansible_collections.middleware_automation.amq.pbkdf2_hmac_filter__parameter-_input:

      .. rst-class:: ansible-option-title

      **Input**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-_input" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      the unencrypted input password


      .. raw:: html

        </div>




.. Options

Keyword parameters
------------------

This describes keyword parameters of the filter. These are the values ``key1=value1``, ``key2=value2`` and so on in the following
example: ``input | middleware_automation.amq.pbkdf2_hmac(key1=value1, key2=value2, ...)``

.. rst-class:: ansible-option-table

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-hashname"></div>

      .. _ansible_collections.middleware_automation.amq.pbkdf2_hmac_filter__parameter-hashname:

      .. rst-class:: ansible-option-title

      **hashname**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-hashname" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      the hash name, among ['sha1', 'sha224', 'sha256', 'sha384', 'sha512']


      .. rst-class:: ansible-option-line

      :ansible-option-default-bold:`Default:` :ansible-option-default:`"sha1"`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-hexsalt"></div>

      .. _ansible_collections.middleware_automation.amq.pbkdf2_hmac_filter__parameter-hexsalt:

      .. rst-class:: ansible-option-title

      **hexsalt**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-hexsalt" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      salt for password hashing, in uppercase hexstring format


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-iterations"></div>

      .. _ansible_collections.middleware_automation.amq.pbkdf2_hmac_filter__parameter-iterations:

      .. rst-class:: ansible-option-title

      **iterations**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-iterations" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      number of iterations, default 1024


      .. raw:: html

        </div>


.. Attributes


.. Notes


.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    # generate pbkdf2_hmac hash in hex format for 'password' with given salt
    - name: Generate salted PBKDF2_HMAC password hash
      ansible.builtin.debug:
        msg: >-
          {{ 'password' | pbkdf2_hmac(hexsalt='7BD6712B68F9BD60B51D77EBD851A21F63E61F2B52301E7CA38DD1602CA662EB' }}

    # generate pbkdf2_hmac hash in hex format for 'password' using 20000 iterations of sha256
    - name: Generate salted PBKDF2_HMAC password hash
      ansible.builtin.debug:
        msg: >-
          {{ 'password' | pbkdf2_hmac(hashname='sha256', iterations=20000, hexsalt='7BD6712B68F9BD60B51D77EBD851A21F63E61F2B52301E7CA38DD1602CA662EB' }}




.. Facts


.. Return values

Return Value
------------

.. rst-class:: ansible-option-table

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1

  * - Key
    - Description

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-_value"></div>

      .. _ansible_collections.middleware_automation.amq.pbkdf2_hmac_filter__return-_value:

      .. rst-class:: ansible-option-title

      **Return value**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-_value" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      the uppercase hexstring representation of the hashed password


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success


      .. raw:: html

        </div>



..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Guido Grazioli 


.. hint::
    Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

.. Extra links


.. Parsing errors

