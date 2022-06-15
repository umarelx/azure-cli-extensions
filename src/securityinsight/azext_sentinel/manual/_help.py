# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=too-many-lines

from knack.help_files import helps

helps['sentinel'] = """
    type: group
    short-summary: Manage Microsoft Sentinel.
"""

helps['sentinel automation-rule create'] = """
    type: command
    short-summary: "Create the automation rule."
    parameters:
      - name: --actions
        short-summary: "The actions to execute when the automation rule is triggered."
        long-summary: |
            Usage: --actions order=XX action-type=XX

            action-type: Required. The type of the automation rule action.

            Multiple actions can be specified by using more than one --actions argument.
      - name: --conditions
        short-summary: "The conditions to evaluate to determine if the automation rule should be triggered on a given \
object."
        long-summary: |
            Usage: --conditions condition-type=XX


            Multiple actions can be specified by using more than one --conditions argument.
    examples:
      - name: AutomationRules_CreateOrUpdate
        text: |-
               az sentinel automation-rule create --etag "\\"0300bf09-0000-0000-0000-5c37296e0000\\"" --actions \
action-type="ModifyProperties" order=1 --display-name "High severity incidents \
escalation" --order 1 --conditions condition-type="Property" --conditions condition-type="PropertyChanged" --conditions \
condition-type="PropertyArrayChanged" --is-enabled \
true --triggers-when "Created" --automation-rule-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" --resource-group "myRg" \
--workspace-name "myWorkspace"
"""
