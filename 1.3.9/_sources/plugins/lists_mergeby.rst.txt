
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

.. _ansible_collections.middleware_automation.amq.lists_mergeby_filter:

.. Anchors: short name for ansible.builtin

.. Title

lists_mergeby -- Merge two or more lists of dictionaries by a given attribute
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This filter plugin is part of the `middleware_automation.amq collection <https://galaxy.ansible.com/middleware_automation/amq>`_.

    To install it, use: :code:`ansible-galaxy collection install middleware\_automation.amq`.

    To use it in a playbook, specify: :code:`middleware_automation.amq.lists_mergeby`.

.. version_added

.. rst-class:: ansible-version-added

New in middleware\_automation.amq 2.0.0

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Merge two or more lists by attribute \ :ansopt:`middleware\_automation.amq.lists\_mergeby#filter:index`\ . Optional parameters \ :ansopt:`middleware\_automation.amq.lists\_mergeby#filter:recursive`\  and \ :ansopt:`middleware\_automation.amq.lists\_mergeby#filter:list\_merge`\  control the merging of the lists in values. The function merge\_hash from ansible.utils.vars is used. To learn details on how to use the parameters \ :ansopt:`middleware\_automation.amq.lists\_mergeby#filter:recursive`\  and \ :ansopt:`middleware\_automation.amq.lists\_mergeby#filter:list\_merge`\  see Ansible User's Guide chapter "Using filters to manipulate data" section "Combining hashes/dictionaries".


.. Aliases


.. Requirements





.. Input

Input
-----

This describes the input of the filter, the value before ``| middleware_automation.amq.lists_mergeby``.

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

      .. _ansible_collections.middleware_automation.amq.lists_mergeby_filter__parameter-_input:

      .. rst-class:: ansible-option-title

      **Input**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-_input" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary` / :ansible-option-required:`required`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      A list of dictionaries.


      .. raw:: html

        </div>




.. Positional

Positional parameters
---------------------

This describes positional parameters of the filter. These are the values ``positional1``, ``positional2`` and so on in the following
example: ``input | middleware_automation.amq.lists_mergeby(positional1, positional2, ...)``

.. rst-class:: ansible-option-table

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-another_list"></div>

      .. _ansible_collections.middleware_automation.amq.lists_mergeby_filter__parameter-another_list:

      .. rst-class:: ansible-option-title

      **another_list**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-another_list" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Another list of dictionaries. This parameter can be specified multiple times.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-index"></div>

      .. _ansible_collections.middleware_automation.amq.lists_mergeby_filter__parameter-index:

      .. rst-class:: ansible-option-title

      **index**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-index" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The dictionary key that must be present in every dictionary in every list that is used to merge the lists.


      .. raw:: html

        </div>



.. Options

Keyword parameters
------------------

This describes keyword parameters of the filter. These are the values ``key1=value1``, ``key2=value2`` and so on in the following
example: ``input | middleware_automation.amq.lists_mergeby(key1=value1, key2=value2, ...)``

.. rst-class:: ansible-option-table

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-list_merge"></div>

      .. _ansible_collections.middleware_automation.amq.lists_mergeby_filter__parameter-list_merge:

      .. rst-class:: ansible-option-title

      **list_merge**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-list_merge" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Modifies the behaviour when the dictionaries (hashes) to merge contain arrays/lists.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`"replace"` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`"keep"`
      - :ansible-option-choices-entry:`"append"`
      - :ansible-option-choices-entry:`"prepend"`
      - :ansible-option-choices-entry:`"append\_rp"`
      - :ansible-option-choices-entry:`"prepend\_rp"`


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-recursive"></div>

      .. _ansible_collections.middleware_automation.amq.lists_mergeby_filter__parameter-recursive:

      .. rst-class:: ansible-option-title

      **recursive**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-recursive" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`




      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Should the combine recursively merge nested dictionaries (hashes).

      \ :strong:`Note:`\  It does not depend on the value of the \ :literal:`hash\_behaviour`\  setting in \ :literal:`ansible.cfg`\ .


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry-default:`false` :ansible-option-choices-default-mark:`← (default)`
      - :ansible-option-choices-entry:`true`


      .. raw:: html

        </div>


.. Attributes


.. Notes

Notes
-----

.. note::
   - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
     ``input | middleware_automation.amq.lists_mergeby(positional1, positional2, key1=value1, key2=value2)``

.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Merge two lists
      ansible.builtin.debug:
        msg: >-
          {{ list1 | middleware_automation.amq.lists_mergeby(
                        list2,
                        'index',
                        recursive=True,
                        list_merge='append'
                     ) }}"
      vars:
        list1:
          - index: a
            value: 123
          - index: b
            value: 42
        list2:
          - index: a
            foo: bar
          - index: c
            foo: baz
      # Produces the following list of dictionaries:
      #   {
      #     "index": "a",
      #     "foo": "bar",
      #     "value": 123
      #   },
      #   {
      #     "index": "b",
      #     "value": 42
      #   },
      #   {
      #     "index": "c",
      #     "foo": "baz"
      #   }




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

      .. _ansible_collections.middleware_automation.amq.lists_mergeby_filter__return-_value:

      .. rst-class:: ansible-option-title

      **Return value**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-_value" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The merged list.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success


      .. raw:: html

        </div>



..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Vladimir Botka (@vbotka)


.. hint::
    Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

.. Extra links


.. Parsing errors

