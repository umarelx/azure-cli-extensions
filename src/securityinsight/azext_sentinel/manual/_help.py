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
            Usage: --actions order=XX action-type=XX severity=XX

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
action-type="ModifyProperties" order=1 severity=High --display-name "High severity incidents \
escalation" --order 1 --is-enabled \
true --triggers-when "Created" --automation-rule-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" --resource-group "myRg" \
--workspace-name "myWorkspace"
"""

helps['sentinel data-connector check-requirement'] = """
    type: command
    short-summary: "Get requirements state for a data connector type."
    parameters:
      - name: --aad
        short-summary: "Represents AAD (Azure Active Directory) requirements check request."
        long-summary: |
            Usage: --aad tenant-id=XX kind=XX

            tenant-id: The tenant id to connect to, and get the data from.
            kind: Required. Describes the kind of connector to be checked.
      - name: --aatp
        short-summary: "Represents AATP (Azure Advanced Threat Protection) requirements check request."
        long-summary: |
            Usage: --aatp tenant-id=XX kind=XX

            tenant-id: The tenant id to connect to, and get the data from.
            kind: Required. Describes the kind of connector to be checked.
      - name: --asc
        short-summary: "Represents ASC (Azure Security Center) requirements check request."
        long-summary: |
            Usage: --asc subscription-id=XX kind=XX

            subscription-id: The subscription id to connect to, and get the data from.
            kind: Required. Describes the kind of connector to be checked.
      - name: --aws-cloud-trail
        short-summary: "Amazon Web Services CloudTrail requirements check request."
        long-summary: |
            Usage: --aws-cloud-trail kind=XX

            kind: Required. Describes the kind of connector to be checked.
      - name: --aws-s3
        short-summary: "Amazon Web Services S3 requirements check request."
        long-summary: |
            Usage: --aws-s3 kind=XX

            kind: Required. Describes the kind of connector to be checked.
      - name: --dynamics-365
        short-summary: "Represents Dynamics365 requirements check request."
        long-summary: |
            Usage: --dynamics-365 tenant-id=XX kind=XX

            tenant-id: The tenant id to connect to, and get the data from.
            kind: Required. Describes the kind of connector to be checked.
      - name: --mcas
        short-summary: "Represents MCAS (Microsoft Cloud App Security) requirements check request."
        long-summary: |
            Usage: --mcas tenant-id=XX kind=XX

            tenant-id: The tenant id to connect to, and get the data from.
            kind: Required. Describes the kind of connector to be checked.
      - name: --mdatp
        short-summary: "Represents MDATP (Microsoft Defender Advanced Threat Protection) requirements check request."
        long-summary: |
            Usage: --mdatp tenant-id=XX kind=XX

            tenant-id: The tenant id to connect to, and get the data from.
            kind: Required. Describes the kind of connector to be checked.
      - name: --msti
        short-summary: "Represents Microsoft Threat Intelligence requirements check request."
        long-summary: |
            Usage: --msti tenant-id=XX kind=XX

            tenant-id: The tenant id to connect to, and get the data from.
            kind: Required. Describes the kind of connector to be checked.
      - name: --mtp
        short-summary: "Represents MTP (Microsoft Threat Protection) requirements check request."
        long-summary: |
            Usage: --mtp tenant-id=XX kind=XX

            tenant-id: The tenant id to connect to, and get the data from.
            kind: Required. Describes the kind of connector to be checked.
      - name: --office-atp
        short-summary: "Represents OfficeATP (Office 365 Advanced Threat Protection) requirements check request."
        long-summary: |
            Usage: --office-atp tenant-id=XX kind=XX

            tenant-id: The tenant id to connect to, and get the data from.
            kind: Required. Describes the kind of connector to be checked.
      - name: --office-irm
        short-summary: "Represents OfficeIRM (Microsoft Insider Risk Management) requirements check request."
        long-summary: |
            Usage: --office-irm tenant-id=XX kind=XX

            tenant-id: The tenant id to connect to, and get the data from.
            kind: Required. Describes the kind of connector to be checked.
      - name: --office-365-project
        short-summary: "Represents Office365 Project requirements check request."
        long-summary: |
            Usage: --office-365-project tenant-id=XX kind=XX

            tenant-id: The tenant id to connect to, and get the data from.
            kind: Required. Describes the kind of connector to be checked.
      - name: --office-power-bi
        short-summary: "Represents Office PowerBI requirements check request."
        long-summary: |
            Usage: --office-power-bi tenant-id=XX kind=XX

            tenant-id: The tenant id to connect to, and get the data from.
            kind: Required. Describes the kind of connector to be checked.
      - name: --ti
        short-summary: "Threat Intelligence Platforms data connector check requirements"
        long-summary: |
            Usage: --ti tenant-id=XX kind=XX

            tenant-id: The tenant id to connect to, and get the data from.
            kind: Required. Describes the kind of connector to be checked.
      - name: --ti-taxii
        short-summary: "Threat Intelligence TAXII data connector check requirements"
        long-summary: |
            Usage: --ti-taxii tenant-id=XX kind=XX

            tenant-id: The tenant id to connect to, and get the data from.
            kind: Required. Describes the kind of connector to be checked.
      - name: --iot
        short-summary: "Represents IoT requirements check request."
        long-summary: |
            Usage: --iot subscription-id=XX kind=XX

            subscription-id: The subscription id to connect to, and get the data from.
            kind: Required. Describes the kind of connector to be checked.
    examples:
      - name: Check requirements for AAD - no authorization.
        text: |-
               az sentinel data-connector check-requirement --aad tenant-id="2070ecc9-b4d5-4ae4-adaa\
-936fa1954fa8" --resource-group "myRg" --workspace-name "myWorkspace"
      - name: Check requirements for AAD - no license.
        text: |-
               az sentinel data-connector check-requirement --aad tenant-id="2070ecc9-b4d5-4ae4-adaa\
-936fa1954fa8" --resource-group "myRg" --workspace-name "myWorkspace"
      - name: Check requirements for AAD.
        text: |-
               az sentinel data-connector check-requirement --aad tenant-id="2070ecc9-b4d5-4ae4-adaa\
-936fa1954fa8" --resource-group "myRg" --workspace-name "myWorkspace"
"""
