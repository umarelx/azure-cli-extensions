# Azure CLI Module Creation Report

## EXTENSION
|CLI Extension|Command Groups|
|---------|------------|
|az sentinel|[groups](#CommandGroups)

## GROUPS
### <a name="CommandGroups">Command groups in `az sentinel` extension </a>
|CLI Command Group|Group Swagger name|Commands|
|---------|------------|--------|
|az sentinel action|Actions|[commands](#CommandsInActions)|
|az sentinel alert-rule|AlertRules|[commands](#CommandsInAlertRules)|
|az sentinel alert-rule template|AlertRuleTemplates|[commands](#CommandsInAlertRuleTemplates)|
|az sentinel analytic-setting|SecurityMLAnalyticsSettings|[commands](#CommandsInSecurityMLAnalyticsSettings)|
|az sentinel automation-rule|AutomationRules|[commands](#CommandsInAutomationRules)|
|az sentinel bookmark|Bookmarks|[commands](#CommandsInBookmarks)|
|az sentinel bookmark relation|BookmarkRelations|[commands](#CommandsInBookmarkRelations)|
|az sentinel data-connector|DataConnectors|[commands](#CommandsInDataConnectors)|
|az sentinel data-connector|DataConnectorsCheckRequirements|[commands](#CommandsInDataConnectorsCheckRequirements)|
|az sentinel domain-whois|DomainWhois|[commands](#CommandsInDomainWhois)|
|az sentinel entity|Entities|[commands](#CommandsInEntities)|
|az sentinel entity|EntitiesGetTimeline|[commands](#CommandsInEntitiesGetTimeline)|
|az sentinel entity query|EntityQueries|[commands](#CommandsInEntityQueries)|
|az sentinel entity relation|EntitiesRelations|[commands](#CommandsInEntitiesRelations)|
|az sentinel entity relation|EntityRelations|[commands](#CommandsInEntityRelations)|
|az sentinel entity template|EntityQueryTemplates|[commands](#CommandsInEntityQueryTemplates)|
|az sentinel incident|Incidents|[commands](#CommandsInIncidents)|
|az sentinel incident comment|IncidentComments|[commands](#CommandsInIncidentComments)|
|az sentinel incident relation|IncidentRelations|[commands](#CommandsInIncidentRelations)|
|az sentinel ip-geodata|IPGeodata|[commands](#CommandsInIPGeodata)|
|az sentinel metadata|Metadata|[commands](#CommandsInMetadata)|
|az sentinel office-consent|OfficeConsents|[commands](#CommandsInOfficeConsents)|
|az sentinel onboarding-state|SentinelOnboardingStates|[commands](#CommandsInSentinelOnboardingStates)|
|az sentinel product-setting|ProductSettings|[commands](#CommandsInProductSettings)|
|az sentinel source-control|SourceControl|[commands](#CommandsInSourceControl)|
|az sentinel source-control|SourceControls|[commands](#CommandsInSourceControls)|
|az sentinel threat-indicator|ThreatIntelligenceIndicator|[commands](#CommandsInThreatIntelligenceIndicator)|
|az sentinel threat-indicator|ThreatIntelligenceIndicators|[commands](#CommandsInThreatIntelligenceIndicators)|
|az sentinel threat-indicator metric|ThreatIntelligenceIndicatorMetrics|[commands](#CommandsInThreatIntelligenceIndicatorMetrics)|
|az sentinel watchlist|Watchlists|[commands](#CommandsInWatchlists)|
|az sentinel watchlist item|WatchlistItems|[commands](#CommandsInWatchlistItems)|

## COMMANDS
### <a name="CommandsInActions">Commands in `az sentinel action` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az sentinel action list](#ActionsListByAlertRule)|ListByAlertRule|[Parameters](#ParametersActionsListByAlertRule)|[Example](#ExamplesActionsListByAlertRule)|
|[az sentinel action show](#ActionsGet)|Get|[Parameters](#ParametersActionsGet)|[Example](#ExamplesActionsGet)|
|[az sentinel action create](#ActionsCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersActionsCreateOrUpdate#Create)|[Example](#ExamplesActionsCreateOrUpdate#Create)|
|[az sentinel action update](#ActionsCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersActionsCreateOrUpdate#Update)|Not Found|
|[az sentinel action delete](#ActionsDelete)|Delete|[Parameters](#ParametersActionsDelete)|[Example](#ExamplesActionsDelete)|

### <a name="CommandsInAlertRules">Commands in `az sentinel alert-rule` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az sentinel alert-rule list](#AlertRulesList)|List|[Parameters](#ParametersAlertRulesList)|[Example](#ExamplesAlertRulesList)|
|[az sentinel alert-rule show](#AlertRulesGet)|Get|[Parameters](#ParametersAlertRulesGet)|[Example](#ExamplesAlertRulesGet)|
|[az sentinel alert-rule create](#AlertRulesCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersAlertRulesCreateOrUpdate#Create)|[Example](#ExamplesAlertRulesCreateOrUpdate#Create)|
|[az sentinel alert-rule update](#AlertRulesCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersAlertRulesCreateOrUpdate#Update)|Not Found|
|[az sentinel alert-rule delete](#AlertRulesDelete)|Delete|[Parameters](#ParametersAlertRulesDelete)|[Example](#ExamplesAlertRulesDelete)|

### <a name="CommandsInAlertRuleTemplates">Commands in `az sentinel alert-rule template` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az sentinel alert-rule template list](#AlertRuleTemplatesList)|List|[Parameters](#ParametersAlertRuleTemplatesList)|[Example](#ExamplesAlertRuleTemplatesList)|
|[az sentinel alert-rule template show](#AlertRuleTemplatesGet)|Get|[Parameters](#ParametersAlertRuleTemplatesGet)|[Example](#ExamplesAlertRuleTemplatesGet)|

### <a name="CommandsInSecurityMLAnalyticsSettings">Commands in `az sentinel analytic-setting` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az sentinel analytic-setting list](#SecurityMLAnalyticsSettingsList)|List|[Parameters](#ParametersSecurityMLAnalyticsSettingsList)|[Example](#ExamplesSecurityMLAnalyticsSettingsList)|
|[az sentinel analytic-setting show](#SecurityMLAnalyticsSettingsGet)|Get|[Parameters](#ParametersSecurityMLAnalyticsSettingsGet)|[Example](#ExamplesSecurityMLAnalyticsSettingsGet)|
|[az sentinel analytic-setting create](#SecurityMLAnalyticsSettingsCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersSecurityMLAnalyticsSettingsCreateOrUpdate#Create)|[Example](#ExamplesSecurityMLAnalyticsSettingsCreateOrUpdate#Create)|
|[az sentinel analytic-setting update](#SecurityMLAnalyticsSettingsCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersSecurityMLAnalyticsSettingsCreateOrUpdate#Update)|Not Found|
|[az sentinel analytic-setting delete](#SecurityMLAnalyticsSettingsDelete)|Delete|[Parameters](#ParametersSecurityMLAnalyticsSettingsDelete)|[Example](#ExamplesSecurityMLAnalyticsSettingsDelete)|

### <a name="CommandsInAutomationRules">Commands in `az sentinel automation-rule` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az sentinel automation-rule list](#AutomationRulesList)|List|[Parameters](#ParametersAutomationRulesList)|[Example](#ExamplesAutomationRulesList)|
|[az sentinel automation-rule show](#AutomationRulesGet)|Get|[Parameters](#ParametersAutomationRulesGet)|[Example](#ExamplesAutomationRulesGet)|
|[az sentinel automation-rule create](#AutomationRulesCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersAutomationRulesCreateOrUpdate#Create)|[Example](#ExamplesAutomationRulesCreateOrUpdate#Create)|
|[az sentinel automation-rule update](#AutomationRulesCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersAutomationRulesCreateOrUpdate#Update)|Not Found|
|[az sentinel automation-rule delete](#AutomationRulesDelete)|Delete|[Parameters](#ParametersAutomationRulesDelete)|[Example](#ExamplesAutomationRulesDelete)|

### <a name="CommandsInBookmarks">Commands in `az sentinel bookmark` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az sentinel bookmark list](#BookmarksList)|List|[Parameters](#ParametersBookmarksList)|[Example](#ExamplesBookmarksList)|
|[az sentinel bookmark show](#BookmarksGet)|Get|[Parameters](#ParametersBookmarksGet)|[Example](#ExamplesBookmarksGet)|
|[az sentinel bookmark create](#BookmarksCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersBookmarksCreateOrUpdate#Create)|[Example](#ExamplesBookmarksCreateOrUpdate#Create)|
|[az sentinel bookmark update](#BookmarksCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersBookmarksCreateOrUpdate#Update)|Not Found|
|[az sentinel bookmark delete](#BookmarksDelete)|Delete|[Parameters](#ParametersBookmarksDelete)|[Example](#ExamplesBookmarksDelete)|
|[az sentinel bookmark expand](#BookmarksExpand)|Expand|[Parameters](#ParametersBookmarksExpand)|[Example](#ExamplesBookmarksExpand)|

### <a name="CommandsInBookmarkRelations">Commands in `az sentinel bookmark relation` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az sentinel bookmark relation list](#BookmarkRelationsList)|List|[Parameters](#ParametersBookmarkRelationsList)|[Example](#ExamplesBookmarkRelationsList)|
|[az sentinel bookmark relation show](#BookmarkRelationsGet)|Get|[Parameters](#ParametersBookmarkRelationsGet)|[Example](#ExamplesBookmarkRelationsGet)|
|[az sentinel bookmark relation create](#BookmarkRelationsCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersBookmarkRelationsCreateOrUpdate#Create)|[Example](#ExamplesBookmarkRelationsCreateOrUpdate#Create)|
|[az sentinel bookmark relation update](#BookmarkRelationsCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersBookmarkRelationsCreateOrUpdate#Update)|Not Found|
|[az sentinel bookmark relation delete](#BookmarkRelationsDelete)|Delete|[Parameters](#ParametersBookmarkRelationsDelete)|[Example](#ExamplesBookmarkRelationsDelete)|

### <a name="CommandsInDataConnectors">Commands in `az sentinel data-connector` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az sentinel data-connector list](#DataConnectorsList)|List|[Parameters](#ParametersDataConnectorsList)|[Example](#ExamplesDataConnectorsList)|
|[az sentinel data-connector show](#DataConnectorsGet)|Get|[Parameters](#ParametersDataConnectorsGet)|[Example](#ExamplesDataConnectorsGet)|
|[az sentinel data-connector create](#DataConnectorsCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersDataConnectorsCreateOrUpdate#Create)|[Example](#ExamplesDataConnectorsCreateOrUpdate#Create)|
|[az sentinel data-connector update](#DataConnectorsCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersDataConnectorsCreateOrUpdate#Update)|Not Found|
|[az sentinel data-connector delete](#DataConnectorsDelete)|Delete|[Parameters](#ParametersDataConnectorsDelete)|[Example](#ExamplesDataConnectorsDelete)|
|[az sentinel data-connector connect](#DataConnectorsConnect)|Connect|[Parameters](#ParametersDataConnectorsConnect)|[Example](#ExamplesDataConnectorsConnect)|
|[az sentinel data-connector disconnect](#DataConnectorsDisconnect)|Disconnect|[Parameters](#ParametersDataConnectorsDisconnect)|[Example](#ExamplesDataConnectorsDisconnect)|

### <a name="CommandsInDataConnectorsCheckRequirements">Commands in `az sentinel data-connector` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az sentinel data-connector check-requirement](#DataConnectorsCheckRequirementsPost)|Post|[Parameters](#ParametersDataConnectorsCheckRequirementsPost)|[Example](#ExamplesDataConnectorsCheckRequirementsPost)|

### <a name="CommandsInDomainWhois">Commands in `az sentinel domain-whois` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az sentinel domain-whois show](#DomainWhoisGet)|Get|[Parameters](#ParametersDomainWhoisGet)|[Example](#ExamplesDomainWhoisGet)|

### <a name="CommandsInEntities">Commands in `az sentinel entity` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az sentinel entity list](#EntitiesList)|List|[Parameters](#ParametersEntitiesList)|[Example](#ExamplesEntitiesList)|
|[az sentinel entity show](#EntitiesGet)|Get|[Parameters](#ParametersEntitiesGet)|[Example](#ExamplesEntitiesGet)|
|[az sentinel entity expand](#EntitiesExpand)|Expand|[Parameters](#ParametersEntitiesExpand)|[Example](#ExamplesEntitiesExpand)|
|[az sentinel entity list-insight](#EntitiesGetInsights)|GetInsights|[Parameters](#ParametersEntitiesGetInsights)|[Example](#ExamplesEntitiesGetInsights)|

### <a name="CommandsInEntitiesGetTimeline">Commands in `az sentinel entity` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az sentinel entity list-timeline](#EntitiesGetTimelinelist)|list|[Parameters](#ParametersEntitiesGetTimelinelist)|[Example](#ExamplesEntitiesGetTimelinelist)|

### <a name="CommandsInEntityQueries">Commands in `az sentinel entity query` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az sentinel entity query list](#EntityQueriesList)|List|[Parameters](#ParametersEntityQueriesList)|[Example](#ExamplesEntityQueriesList)|
|[az sentinel entity query show](#EntityQueriesGet)|Get|[Parameters](#ParametersEntityQueriesGet)|[Example](#ExamplesEntityQueriesGet)|
|[az sentinel entity query create](#EntityQueriesCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersEntityQueriesCreateOrUpdate#Create)|[Example](#ExamplesEntityQueriesCreateOrUpdate#Create)|
|[az sentinel entity query update](#EntityQueriesCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersEntityQueriesCreateOrUpdate#Update)|Not Found|
|[az sentinel entity query delete](#EntityQueriesDelete)|Delete|[Parameters](#ParametersEntityQueriesDelete)|[Example](#ExamplesEntityQueriesDelete)|

### <a name="CommandsInEntitiesRelations">Commands in `az sentinel entity relation` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az sentinel entity relation list](#EntitiesRelationsList)|List|[Parameters](#ParametersEntitiesRelationsList)|[Example](#ExamplesEntitiesRelationsList)|

### <a name="CommandsInEntityRelations">Commands in `az sentinel entity relation` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az sentinel entity relation show](#EntityRelationsGetRelation)|GetRelation|[Parameters](#ParametersEntityRelationsGetRelation)|[Example](#ExamplesEntityRelationsGetRelation)|

### <a name="CommandsInEntityQueryTemplates">Commands in `az sentinel entity template` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az sentinel entity template list](#EntityQueryTemplatesList)|List|[Parameters](#ParametersEntityQueryTemplatesList)|[Example](#ExamplesEntityQueryTemplatesList)|
|[az sentinel entity template show](#EntityQueryTemplatesGet)|Get|[Parameters](#ParametersEntityQueryTemplatesGet)|[Example](#ExamplesEntityQueryTemplatesGet)|

### <a name="CommandsInIncidents">Commands in `az sentinel incident` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az sentinel incident list](#IncidentsList)|List|[Parameters](#ParametersIncidentsList)|[Example](#ExamplesIncidentsList)|
|[az sentinel incident show](#IncidentsGet)|Get|[Parameters](#ParametersIncidentsGet)|[Example](#ExamplesIncidentsGet)|
|[az sentinel incident create](#IncidentsCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersIncidentsCreateOrUpdate#Create)|[Example](#ExamplesIncidentsCreateOrUpdate#Create)|
|[az sentinel incident update](#IncidentsCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersIncidentsCreateOrUpdate#Update)|Not Found|
|[az sentinel incident delete](#IncidentsDelete)|Delete|[Parameters](#ParametersIncidentsDelete)|[Example](#ExamplesIncidentsDelete)|
|[az sentinel incident create-team](#IncidentsCreateTeam)|CreateTeam|[Parameters](#ParametersIncidentsCreateTeam)|[Example](#ExamplesIncidentsCreateTeam)|
|[az sentinel incident list-alert](#IncidentsListAlerts)|ListAlerts|[Parameters](#ParametersIncidentsListAlerts)|[Example](#ExamplesIncidentsListAlerts)|
|[az sentinel incident list-bookmark](#IncidentsListBookmarks)|ListBookmarks|[Parameters](#ParametersIncidentsListBookmarks)|[Example](#ExamplesIncidentsListBookmarks)|
|[az sentinel incident list-entity](#IncidentsListEntities)|ListEntities|[Parameters](#ParametersIncidentsListEntities)|[Example](#ExamplesIncidentsListEntities)|
|[az sentinel incident run-playbook](#IncidentsRunPlaybook)|RunPlaybook|[Parameters](#ParametersIncidentsRunPlaybook)|[Example](#ExamplesIncidentsRunPlaybook)|

### <a name="CommandsInIncidentComments">Commands in `az sentinel incident comment` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az sentinel incident comment list](#IncidentCommentsList)|List|[Parameters](#ParametersIncidentCommentsList)|[Example](#ExamplesIncidentCommentsList)|
|[az sentinel incident comment show](#IncidentCommentsGet)|Get|[Parameters](#ParametersIncidentCommentsGet)|[Example](#ExamplesIncidentCommentsGet)|
|[az sentinel incident comment create](#IncidentCommentsCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersIncidentCommentsCreateOrUpdate#Create)|[Example](#ExamplesIncidentCommentsCreateOrUpdate#Create)|
|[az sentinel incident comment update](#IncidentCommentsCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersIncidentCommentsCreateOrUpdate#Update)|Not Found|
|[az sentinel incident comment delete](#IncidentCommentsDelete)|Delete|[Parameters](#ParametersIncidentCommentsDelete)|[Example](#ExamplesIncidentCommentsDelete)|

### <a name="CommandsInIncidentRelations">Commands in `az sentinel incident relation` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az sentinel incident relation list](#IncidentRelationsList)|List|[Parameters](#ParametersIncidentRelationsList)|[Example](#ExamplesIncidentRelationsList)|
|[az sentinel incident relation show](#IncidentRelationsGet)|Get|[Parameters](#ParametersIncidentRelationsGet)|[Example](#ExamplesIncidentRelationsGet)|
|[az sentinel incident relation create](#IncidentRelationsCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersIncidentRelationsCreateOrUpdate#Create)|[Example](#ExamplesIncidentRelationsCreateOrUpdate#Create)|
|[az sentinel incident relation update](#IncidentRelationsCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersIncidentRelationsCreateOrUpdate#Update)|Not Found|
|[az sentinel incident relation delete](#IncidentRelationsDelete)|Delete|[Parameters](#ParametersIncidentRelationsDelete)|[Example](#ExamplesIncidentRelationsDelete)|

### <a name="CommandsInIPGeodata">Commands in `az sentinel ip-geodata` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az sentinel ip-geodata show](#IPGeodataGet)|Get|[Parameters](#ParametersIPGeodataGet)|[Example](#ExamplesIPGeodataGet)|

### <a name="CommandsInMetadata">Commands in `az sentinel metadata` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az sentinel metadata list](#MetadataList)|List|[Parameters](#ParametersMetadataList)|[Example](#ExamplesMetadataList)|
|[az sentinel metadata show](#MetadataGet)|Get|[Parameters](#ParametersMetadataGet)|[Example](#ExamplesMetadataGet)|
|[az sentinel metadata create](#MetadataCreate)|Create|[Parameters](#ParametersMetadataCreate)|[Example](#ExamplesMetadataCreate)|
|[az sentinel metadata update](#MetadataUpdate)|Update|[Parameters](#ParametersMetadataUpdate)|[Example](#ExamplesMetadataUpdate)|
|[az sentinel metadata delete](#MetadataDelete)|Delete|[Parameters](#ParametersMetadataDelete)|[Example](#ExamplesMetadataDelete)|

### <a name="CommandsInOfficeConsents">Commands in `az sentinel office-consent` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az sentinel office-consent list](#OfficeConsentsList)|List|[Parameters](#ParametersOfficeConsentsList)|[Example](#ExamplesOfficeConsentsList)|
|[az sentinel office-consent show](#OfficeConsentsGet)|Get|[Parameters](#ParametersOfficeConsentsGet)|[Example](#ExamplesOfficeConsentsGet)|
|[az sentinel office-consent delete](#OfficeConsentsDelete)|Delete|[Parameters](#ParametersOfficeConsentsDelete)|[Example](#ExamplesOfficeConsentsDelete)|

### <a name="CommandsInSentinelOnboardingStates">Commands in `az sentinel onboarding-state` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az sentinel onboarding-state list](#SentinelOnboardingStatesList)|List|[Parameters](#ParametersSentinelOnboardingStatesList)|[Example](#ExamplesSentinelOnboardingStatesList)|
|[az sentinel onboarding-state show](#SentinelOnboardingStatesGet)|Get|[Parameters](#ParametersSentinelOnboardingStatesGet)|[Example](#ExamplesSentinelOnboardingStatesGet)|
|[az sentinel onboarding-state create](#SentinelOnboardingStatesCreate)|Create|[Parameters](#ParametersSentinelOnboardingStatesCreate)|[Example](#ExamplesSentinelOnboardingStatesCreate)|
|[az sentinel onboarding-state delete](#SentinelOnboardingStatesDelete)|Delete|[Parameters](#ParametersSentinelOnboardingStatesDelete)|[Example](#ExamplesSentinelOnboardingStatesDelete)|

### <a name="CommandsInProductSettings">Commands in `az sentinel product-setting` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az sentinel product-setting list](#ProductSettingsList)|List|[Parameters](#ParametersProductSettingsList)|[Example](#ExamplesProductSettingsList)|
|[az sentinel product-setting show](#ProductSettingsGet)|Get|[Parameters](#ParametersProductSettingsGet)|[Example](#ExamplesProductSettingsGet)|
|[az sentinel product-setting update](#ProductSettingsUpdate)|Update|[Parameters](#ParametersProductSettingsUpdate)|Not Found|
|[az sentinel product-setting delete](#ProductSettingsDelete)|Delete|[Parameters](#ParametersProductSettingsDelete)|[Example](#ExamplesProductSettingsDelete)|

### <a name="CommandsInSourceControl">Commands in `az sentinel source-control` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az sentinel source-control list-repository](#SourceControllistRepositories)|listRepositories|[Parameters](#ParametersSourceControllistRepositories)|[Example](#ExamplesSourceControllistRepositories)|

### <a name="CommandsInSourceControls">Commands in `az sentinel source-control` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az sentinel source-control list](#SourceControlsList)|List|[Parameters](#ParametersSourceControlsList)|[Example](#ExamplesSourceControlsList)|
|[az sentinel source-control show](#SourceControlsGet)|Get|[Parameters](#ParametersSourceControlsGet)|[Example](#ExamplesSourceControlsGet)|
|[az sentinel source-control create](#SourceControlsCreate)|Create|[Parameters](#ParametersSourceControlsCreate)|[Example](#ExamplesSourceControlsCreate)|
|[az sentinel source-control delete](#SourceControlsDelete)|Delete|[Parameters](#ParametersSourceControlsDelete)|[Example](#ExamplesSourceControlsDelete)|

### <a name="CommandsInThreatIntelligenceIndicator">Commands in `az sentinel threat-indicator` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az sentinel threat-indicator show](#ThreatIntelligenceIndicatorGet)|Get|[Parameters](#ParametersThreatIntelligenceIndicatorGet)|[Example](#ExamplesThreatIntelligenceIndicatorGet)|
|[az sentinel threat-indicator create](#ThreatIntelligenceIndicatorCreateIndicator)|CreateIndicator|[Parameters](#ParametersThreatIntelligenceIndicatorCreateIndicator)|[Example](#ExamplesThreatIntelligenceIndicatorCreateIndicator)|
|[az sentinel threat-indicator update](#ThreatIntelligenceIndicatorCreate)|Create|[Parameters](#ParametersThreatIntelligenceIndicatorCreate)|[Example](#ExamplesThreatIntelligenceIndicatorCreate)|
|[az sentinel threat-indicator delete](#ThreatIntelligenceIndicatorDelete)|Delete|[Parameters](#ParametersThreatIntelligenceIndicatorDelete)|[Example](#ExamplesThreatIntelligenceIndicatorDelete)|
|[az sentinel threat-indicator append-tag](#ThreatIntelligenceIndicatorAppendTags)|AppendTags|[Parameters](#ParametersThreatIntelligenceIndicatorAppendTags)|[Example](#ExamplesThreatIntelligenceIndicatorAppendTags)|
|[az sentinel threat-indicator query](#ThreatIntelligenceIndicatorQueryIndicators)|QueryIndicators|[Parameters](#ParametersThreatIntelligenceIndicatorQueryIndicators)|[Example](#ExamplesThreatIntelligenceIndicatorQueryIndicators)|
|[az sentinel threat-indicator replace-tag](#ThreatIntelligenceIndicatorReplaceTags)|ReplaceTags|[Parameters](#ParametersThreatIntelligenceIndicatorReplaceTags)|[Example](#ExamplesThreatIntelligenceIndicatorReplaceTags)|

### <a name="CommandsInThreatIntelligenceIndicators">Commands in `az sentinel threat-indicator` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az sentinel threat-indicator list](#ThreatIntelligenceIndicatorsList)|List|[Parameters](#ParametersThreatIntelligenceIndicatorsList)|[Example](#ExamplesThreatIntelligenceIndicatorsList)|

### <a name="CommandsInThreatIntelligenceIndicatorMetrics">Commands in `az sentinel threat-indicator metric` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az sentinel threat-indicator metric list](#ThreatIntelligenceIndicatorMetricsList)|List|[Parameters](#ParametersThreatIntelligenceIndicatorMetricsList)|[Example](#ExamplesThreatIntelligenceIndicatorMetricsList)|

### <a name="CommandsInWatchlists">Commands in `az sentinel watchlist` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az sentinel watchlist list](#WatchlistsList)|List|[Parameters](#ParametersWatchlistsList)|[Example](#ExamplesWatchlistsList)|
|[az sentinel watchlist show](#WatchlistsGet)|Get|[Parameters](#ParametersWatchlistsGet)|[Example](#ExamplesWatchlistsGet)|
|[az sentinel watchlist create](#WatchlistsCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersWatchlistsCreateOrUpdate#Create)|[Example](#ExamplesWatchlistsCreateOrUpdate#Create)|
|[az sentinel watchlist update](#WatchlistsCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersWatchlistsCreateOrUpdate#Update)|Not Found|
|[az sentinel watchlist delete](#WatchlistsDelete)|Delete|[Parameters](#ParametersWatchlistsDelete)|[Example](#ExamplesWatchlistsDelete)|

### <a name="CommandsInWatchlistItems">Commands in `az sentinel watchlist item` group</a>
|CLI Command|Operation Swagger name|Parameters|Examples|
|---------|------------|--------|-----------|
|[az sentinel watchlist item list](#WatchlistItemsList)|List|[Parameters](#ParametersWatchlistItemsList)|[Example](#ExamplesWatchlistItemsList)|
|[az sentinel watchlist item show](#WatchlistItemsGet)|Get|[Parameters](#ParametersWatchlistItemsGet)|[Example](#ExamplesWatchlistItemsGet)|
|[az sentinel watchlist item create](#WatchlistItemsCreateOrUpdate#Create)|CreateOrUpdate#Create|[Parameters](#ParametersWatchlistItemsCreateOrUpdate#Create)|[Example](#ExamplesWatchlistItemsCreateOrUpdate#Create)|
|[az sentinel watchlist item update](#WatchlistItemsCreateOrUpdate#Update)|CreateOrUpdate#Update|[Parameters](#ParametersWatchlistItemsCreateOrUpdate#Update)|Not Found|
|[az sentinel watchlist item delete](#WatchlistItemsDelete)|Delete|[Parameters](#ParametersWatchlistItemsDelete)|[Example](#ExamplesWatchlistItemsDelete)|


## COMMAND DETAILS
### group `az sentinel action`
#### <a name="ActionsListByAlertRule">Command `az sentinel action list`</a>

##### <a name="ExamplesActionsListByAlertRule">Example</a>
```
az sentinel action list --resource-group "myRg" --rule-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" --workspace-name \
"myWorkspace"
```
##### <a name="ParametersActionsListByAlertRule">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--rule-id**|string|Alert rule ID|rule_id|ruleId|

#### <a name="ActionsGet">Command `az sentinel action show`</a>

##### <a name="ExamplesActionsGet">Example</a>
```
az sentinel action show --action-id "912bec42-cb66-4c03-ac63-1761b6898c3e" --resource-group "myRg" --rule-id \
"73e01a99-5cd7-4139-a149-9f2736ff2ab5" --workspace-name "myWorkspace"
```
##### <a name="ParametersActionsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--rule-id**|string|Alert rule ID|rule_id|ruleId|
|**--action-id**|string|Action ID|action_id|actionId|

#### <a name="ActionsCreateOrUpdate#Create">Command `az sentinel action create`</a>

##### <a name="ExamplesActionsCreateOrUpdate#Create">Example</a>
```
az sentinel action create --etag "\\"0300bf09-0000-0000-0000-5c37296e0000\\"" --logic-app-resource-id \
"/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.Logic/workflows/MyAlerts" \
--trigger-uri "https://prod-31.northcentralus.logic.azure.com:443/workflows/cd3765391efd48549fd7681ded1d48d7/triggers/m\
anual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=signature" --action-id \
"912bec42-cb66-4c03-ac63-1761b6898c3e" --resource-group "myRg" --rule-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" \
--workspace-name "myWorkspace"
```
##### <a name="ParametersActionsCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--rule-id**|string|Alert rule ID|rule_id|ruleId|
|**--action-id**|string|Action ID|action_id|actionId|
|**--etag**|string|Etag of the azure resource|etag|etag|
|**--logic-app-resource-id**|string|Logic App Resource Id, /subscriptions/{my-subscription}/resourceGroups/{my-resource-group}/providers/Microsoft.Logic/workflows/{my-workflow-id}.|logic_app_resource_id|logicAppResourceId|
|**--trigger-uri**|string|Logic App Callback URL for this specific workflow.|trigger_uri|triggerUri|

#### <a name="ActionsCreateOrUpdate#Update">Command `az sentinel action update`</a>


##### <a name="ParametersActionsCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--rule-id**|string|Alert rule ID|rule_id|ruleId|
|**--action-id**|string|Action ID|action_id|actionId|
|**--etag**|string|Etag of the azure resource|etag|etag|
|**--logic-app-resource-id**|string|Logic App Resource Id, /subscriptions/{my-subscription}/resourceGroups/{my-resource-group}/providers/Microsoft.Logic/workflows/{my-workflow-id}.|logic_app_resource_id|logicAppResourceId|
|**--trigger-uri**|string|Logic App Callback URL for this specific workflow.|trigger_uri|triggerUri|

#### <a name="ActionsDelete">Command `az sentinel action delete`</a>

##### <a name="ExamplesActionsDelete">Example</a>
```
az sentinel action delete --action-id "912bec42-cb66-4c03-ac63-1761b6898c3e" --resource-group "myRg" --rule-id \
"73e01a99-5cd7-4139-a149-9f2736ff2ab5" --workspace-name "myWorkspace"
```
##### <a name="ParametersActionsDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--rule-id**|string|Alert rule ID|rule_id|ruleId|
|**--action-id**|string|Action ID|action_id|actionId|

### group `az sentinel alert-rule`
#### <a name="AlertRulesList">Command `az sentinel alert-rule list`</a>

##### <a name="ExamplesAlertRulesList">Example</a>
```
az sentinel alert-rule list --resource-group "myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersAlertRulesList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|

#### <a name="AlertRulesGet">Command `az sentinel alert-rule show`</a>

##### <a name="ExamplesAlertRulesGet">Example</a>
```
az sentinel alert-rule show --resource-group "myRg" --rule-id "myFirstFusionRule" --workspace-name "myWorkspace"
az sentinel alert-rule show --resource-group "myRg" --rule-id "microsoftSecurityIncidentCreationRuleExample" \
--workspace-name "myWorkspace"
az sentinel alert-rule show --resource-group "myRg" --rule-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" --workspace-name \
"myWorkspace"
az sentinel alert-rule show --resource-group "myRg" --rule-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" --workspace-name \
"myWorkspace"
```
##### <a name="ParametersAlertRulesGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--rule-id**|string|Alert rule ID|rule_id|ruleId|

#### <a name="AlertRulesCreateOrUpdate#Create">Command `az sentinel alert-rule create`</a>

##### <a name="ExamplesAlertRulesCreateOrUpdate#Create">Example</a>
```
az sentinel alert-rule create --alert-rule "{\\"etag\\":\\"3d00c3ca-0000-0100-0000-5d42d5010000\\",\\"kind\\":\\"Fusion\
\\",\\"properties\\":{\\"alertRuleTemplateName\\":\\"f71aba3d-28fb-450b-b192-4e76a83015c8\\",\\"enabled\\":true,\\"sour\
ceSettings\\":[{\\"enabled\\":true,\\"sourceName\\":\\"Anomalies\\",\\"sourceSubTypes\\":null},{\\"enabled\\":true,\\"s\
ourceName\\":\\"Alert providers\\",\\"sourceSubTypes\\":[{\\"enabled\\":true,\\"severityFilters\\":{\\"filters\\":[{\\"\
enabled\\":true,\\"severity\\":\\"High\\"},{\\"enabled\\":true,\\"severity\\":\\"Medium\\"},{\\"enabled\\":true,\\"seve\
rity\\":\\"Low\\"},{\\"enabled\\":true,\\"severity\\":\\"Informational\\"}]},\\"sourceSubTypeName\\":\\"Azure Active \
Directory Identity Protection\\"},{\\"enabled\\":true,\\"severityFilters\\":{\\"filters\\":[{\\"enabled\\":true,\\"seve\
rity\\":\\"High\\"},{\\"enabled\\":true,\\"severity\\":\\"Medium\\"},{\\"enabled\\":true,\\"severity\\":\\"Low\\"},{\\"\
enabled\\":true,\\"severity\\":\\"Informational\\"}]},\\"sourceSubTypeName\\":\\"Azure Defender\\"},{\\"enabled\\":true\
,\\"severityFilters\\":{\\"filters\\":[{\\"enabled\\":true,\\"severity\\":\\"High\\"},{\\"enabled\\":true,\\"severity\\\
":\\"Medium\\"},{\\"enabled\\":true,\\"severity\\":\\"Low\\"},{\\"enabled\\":true,\\"severity\\":\\"Informational\\"}]}\
,\\"sourceSubTypeName\\":\\"Azure Defender for IoT\\"},{\\"enabled\\":true,\\"severityFilter\\":[\\"High\\",\\"Medium\\\
",\\"Low\\",\\"Informational\\"],\\"severityFilters\\":{\\"filters\\":[{\\"enabled\\":true,\\"severity\\":\\"High\\"},{\
\\"enabled\\":true,\\"severity\\":\\"Medium\\"},{\\"enabled\\":true,\\"severity\\":\\"Low\\"},{\\"enabled\\":true,\\"se\
verity\\":\\"Informational\\"}]},\\"sourceSubTypeName\\":\\"Microsoft 365 Defender\\"},{\\"enabled\\":true,\\"severityF\
ilters\\":{\\"filters\\":[{\\"enabled\\":true,\\"severity\\":\\"High\\"},{\\"enabled\\":true,\\"severity\\":\\"Medium\\\
"},{\\"enabled\\":true,\\"severity\\":\\"Low\\"},{\\"enabled\\":true,\\"severity\\":\\"Informational\\"}]},\\"sourceSub\
TypeName\\":\\"Microsoft Cloud App Security\\"},{\\"enabled\\":true,\\"severityFilters\\":{\\"filters\\":[{\\"enabled\\\
":true,\\"severity\\":\\"High\\"},{\\"enabled\\":true,\\"severity\\":\\"Medium\\"},{\\"enabled\\":true,\\"severity\\":\
\\"Low\\"},{\\"enabled\\":true,\\"severity\\":\\"Informational\\"}]},\\"sourceSubTypeName\\":\\"Microsoft Defender for \
Endpoint\\"},{\\"enabled\\":true,\\"severityFilters\\":{\\"filters\\":[{\\"enabled\\":true,\\"severity\\":\\"High\\"},{\
\\"enabled\\":true,\\"severity\\":\\"Medium\\"},{\\"enabled\\":true,\\"severity\\":\\"Low\\"},{\\"enabled\\":true,\\"se\
verity\\":\\"Informational\\"}]},\\"sourceSubTypeName\\":\\"Microsoft Defender for Identity\\"},{\\"enabled\\":true,\\"\
severityFilters\\":{\\"filters\\":[{\\"enabled\\":true,\\"severity\\":\\"High\\"},{\\"enabled\\":true,\\"severity\\":\\\
"Medium\\"},{\\"enabled\\":true,\\"severity\\":\\"Low\\"},{\\"enabled\\":true,\\"severity\\":\\"Informational\\"}]},\\"\
sourceSubTypeName\\":\\"Microsoft Defender for Office 365\\"},{\\"enabled\\":true,\\"severityFilters\\":{\\"filters\\":\
[{\\"enabled\\":true,\\"severity\\":\\"High\\"},{\\"enabled\\":true,\\"severity\\":\\"Medium\\"},{\\"enabled\\":true,\\\
"severity\\":\\"Low\\"},{\\"enabled\\":true,\\"severity\\":\\"Informational\\"}]},\\"sourceSubTypeName\\":\\"Azure \
Sentinel scheduled analytics rules\\"}]},{\\"enabled\\":true,\\"sourceName\\":\\"Raw logs from other \
sources\\",\\"sourceSubTypes\\":[{\\"enabled\\":true,\\"severityFilters\\":{\\"filters\\":null},\\"sourceSubTypeName\\"\
:\\"Palo Alto Networks\\"}]}]}}" --resource-group "myRg" --rule-id "myFirstFusionRule" --workspace-name "myWorkspace"
az sentinel alert-rule create --alert-rule "{\\"etag\\":\\"3d00c3ca-0000-0100-0000-5d42d5010000\\",\\"kind\\":\\"Fusion\
\\",\\"properties\\":{\\"alertRuleTemplateName\\":\\"f71aba3d-28fb-450b-b192-4e76a83015c8\\",\\"enabled\\":true,\\"sour\
ceSettings\\":[{\\"enabled\\":true,\\"sourceName\\":\\"Anomalies\\",\\"sourceSubTypes\\":null},{\\"enabled\\":true,\\"s\
ourceName\\":\\"Alert providers\\",\\"sourceSubTypes\\":[{\\"enabled\\":true,\\"severityFilters\\":{\\"filters\\":[{\\"\
enabled\\":true,\\"severity\\":\\"High\\"},{\\"enabled\\":true,\\"severity\\":\\"Medium\\"},{\\"enabled\\":true,\\"seve\
rity\\":\\"Low\\"},{\\"enabled\\":true,\\"severity\\":\\"Informational\\"}]},\\"sourceSubTypeName\\":\\"Azure Active \
Directory Identity Protection\\"},{\\"enabled\\":true,\\"severityFilters\\":{\\"filters\\":[{\\"enabled\\":true,\\"seve\
rity\\":\\"High\\"},{\\"enabled\\":true,\\"severity\\":\\"Medium\\"},{\\"enabled\\":true,\\"severity\\":\\"Low\\"},{\\"\
enabled\\":true,\\"severity\\":\\"Informational\\"}]},\\"sourceSubTypeName\\":\\"Azure Defender\\"},{\\"enabled\\":true\
,\\"severityFilters\\":{\\"filters\\":[{\\"enabled\\":true,\\"severity\\":\\"High\\"},{\\"enabled\\":true,\\"severity\\\
":\\"Medium\\"},{\\"enabled\\":true,\\"severity\\":\\"Low\\"},{\\"enabled\\":true,\\"severity\\":\\"Informational\\"}]}\
,\\"sourceSubTypeName\\":\\"Azure Defender for IoT\\"},{\\"enabled\\":true,\\"severityFilter\\":[\\"High\\",\\"Medium\\\
",\\"Low\\",\\"Informational\\"],\\"severityFilters\\":{\\"filters\\":[{\\"enabled\\":true,\\"severity\\":\\"High\\"},{\
\\"enabled\\":true,\\"severity\\":\\"Medium\\"},{\\"enabled\\":true,\\"severity\\":\\"Low\\"},{\\"enabled\\":true,\\"se\
verity\\":\\"Informational\\"}]},\\"sourceSubTypeName\\":\\"Microsoft 365 Defender\\"},{\\"enabled\\":true,\\"severityF\
ilters\\":{\\"filters\\":[{\\"enabled\\":true,\\"severity\\":\\"High\\"},{\\"enabled\\":true,\\"severity\\":\\"Medium\\\
"},{\\"enabled\\":true,\\"severity\\":\\"Low\\"},{\\"enabled\\":true,\\"severity\\":\\"Informational\\"}]},\\"sourceSub\
TypeName\\":\\"Microsoft Cloud App Security\\"},{\\"enabled\\":true,\\"severityFilters\\":{\\"filters\\":[{\\"enabled\\\
":true,\\"severity\\":\\"High\\"},{\\"enabled\\":true,\\"severity\\":\\"Medium\\"},{\\"enabled\\":true,\\"severity\\":\
\\"Low\\"},{\\"enabled\\":true,\\"severity\\":\\"Informational\\"}]},\\"sourceSubTypeName\\":\\"Microsoft Defender for \
Endpoint\\"},{\\"enabled\\":true,\\"severityFilters\\":{\\"filters\\":[{\\"enabled\\":true,\\"severity\\":\\"High\\"},{\
\\"enabled\\":true,\\"severity\\":\\"Medium\\"},{\\"enabled\\":true,\\"severity\\":\\"Low\\"},{\\"enabled\\":true,\\"se\
verity\\":\\"Informational\\"}]},\\"sourceSubTypeName\\":\\"Microsoft Defender for Identity\\"},{\\"enabled\\":true,\\"\
severityFilters\\":{\\"filters\\":[{\\"enabled\\":true,\\"severity\\":\\"High\\"},{\\"enabled\\":true,\\"severity\\":\\\
"Medium\\"},{\\"enabled\\":true,\\"severity\\":\\"Low\\"},{\\"enabled\\":true,\\"severity\\":\\"Informational\\"}]},\\"\
sourceSubTypeName\\":\\"Microsoft Defender for Office 365\\"},{\\"enabled\\":true,\\"severityFilters\\":{\\"filters\\":\
[{\\"enabled\\":true,\\"severity\\":\\"High\\"},{\\"enabled\\":true,\\"severity\\":\\"Medium\\"},{\\"enabled\\":true,\\\
"severity\\":\\"Low\\"},{\\"enabled\\":true,\\"severity\\":\\"Informational\\"}]},\\"sourceSubTypeName\\":\\"Azure \
Sentinel scheduled analytics rules\\"}]},{\\"enabled\\":true,\\"sourceName\\":\\"Raw logs from other \
sources\\",\\"sourceSubTypes\\":[{\\"enabled\\":true,\\"severityFilters\\":{\\"filters\\":null},\\"sourceSubTypeName\\"\
:\\"Palo Alto Networks\\"}]}]}}" --resource-group "myRg" --rule-id "myFirstFusionRule" --workspace-name "myWorkspace"
az sentinel alert-rule create --alert-rule "{\\"etag\\":\\"\\\\\\"260097e0-0000-0d00-0000-5d6fa88f0000\\\\\\"\\",\\"kin\
d\\":\\"MicrosoftSecurityIncidentCreation\\",\\"properties\\":{\\"displayName\\":\\"testing \
displayname\\",\\"enabled\\":true,\\"productFilter\\":\\"Microsoft Cloud App Security\\"}}" --resource-group "myRg" \
--rule-id "microsoftSecurityIncidentCreationRuleExample" --workspace-name "myWorkspace"
az sentinel alert-rule create --alert-rule "{\\"etag\\":\\"\\\\\\"0300bf09-0000-0000-0000-5c37296e0000\\\\\\"\\",\\"kin\
d\\":\\"NRT\\",\\"properties\\":{\\"description\\":\\"\\",\\"displayName\\":\\"Rule2\\",\\"enabled\\":true,\\"eventGrou\
pingSettings\\":{\\"aggregationKind\\":\\"AlertPerResult\\"},\\"incidentConfiguration\\":{\\"createIncident\\":true,\\"\
groupingConfiguration\\":{\\"enabled\\":true,\\"groupByEntities\\":[\\"Host\\",\\"Account\\"],\\"lookbackDuration\\":\\\
"PT5H\\",\\"matchingMethod\\":\\"Selected\\",\\"reopenClosedIncident\\":false}},\\"query\\":\\"ProtectionStatus | \
extend HostCustomEntity = Computer | extend IPCustomEntity = ComputerIP_Hidden\\",\\"severity\\":\\"High\\",\\"suppress\
ionDuration\\":\\"PT1H\\",\\"suppressionEnabled\\":false,\\"tactics\\":[\\"Persistence\\",\\"LateralMovement\\"],\\"tec\
hniques\\":[\\"T1037\\",\\"T1021\\"]}}" --resource-group "myRg" --rule-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" \
--workspace-name "myWorkspace"
az sentinel alert-rule create --alert-rule "{\\"etag\\":\\"\\\\\\"0300bf09-0000-0000-0000-5c37296e0000\\\\\\"\\",\\"kin\
d\\":\\"Scheduled\\",\\"properties\\":{\\"description\\":\\"An example for a scheduled rule\\",\\"alertDetailsOverride\
\\":{\\"alertDescriptionFormat\\":\\"Suspicious activity was made by {{ComputerIP}}\\",\\"alertDisplayNameFormat\\":\\"\
Alert from {{Computer}}\\"},\\"customDetails\\":{\\"OperatingSystemName\\":\\"OSName\\",\\"OperatingSystemType\\":\\"OS\
Type\\"},\\"displayName\\":\\"My scheduled rule\\",\\"enabled\\":true,\\"entityMappings\\":[{\\"entityType\\":\\"Host\\\
",\\"fieldMappings\\":[{\\"columnName\\":\\"Computer\\",\\"identifier\\":\\"FullName\\"}]},{\\"entityType\\":\\"IP\\",\
\\"fieldMappings\\":[{\\"columnName\\":\\"ComputerIP\\",\\"identifier\\":\\"Address\\"}]}],\\"eventGroupingSettings\\":\
{\\"aggregationKind\\":\\"AlertPerResult\\"},\\"incidentConfiguration\\":{\\"createIncident\\":true,\\"groupingConfigur\
ation\\":{\\"enabled\\":true,\\"groupByAlertDetails\\":[\\"DisplayName\\"],\\"groupByCustomDetails\\":[\\"OperatingSyst\
emType\\",\\"OperatingSystemName\\"],\\"groupByEntities\\":[\\"Host\\"],\\"lookbackDuration\\":\\"PT5H\\",\\"matchingMe\
thod\\":\\"Selected\\",\\"reopenClosedIncident\\":false}},\\"query\\":\\"Heartbeat\\",\\"queryFrequency\\":\\"PT1H\\",\
\\"queryPeriod\\":\\"P2DT1H30M\\",\\"severity\\":\\"High\\",\\"suppressionDuration\\":\\"PT1H\\",\\"suppressionEnabled\
\\":false,\\"tactics\\":[\\"Persistence\\",\\"LateralMovement\\"],\\"techniques\\":[\\"T1037\\",\\"T1021\\"],\\"trigger\
Operator\\":\\"GreaterThan\\",\\"triggerThreshold\\":0}}" --resource-group "myRg" --rule-id \
"73e01a99-5cd7-4139-a149-9f2736ff2ab5" --workspace-name "myWorkspace"
```
##### <a name="ParametersAlertRulesCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--rule-id**|string|Alert rule ID|rule_id|ruleId|
|**--alert-rule**|object|The alert rule|alert_rule|alertRule|

#### <a name="AlertRulesCreateOrUpdate#Update">Command `az sentinel alert-rule update`</a>


##### <a name="ParametersAlertRulesCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--rule-id**|string|Alert rule ID|rule_id|ruleId|
|**--alert-rule**|object|The alert rule|alert_rule|alertRule|

#### <a name="AlertRulesDelete">Command `az sentinel alert-rule delete`</a>

##### <a name="ExamplesAlertRulesDelete">Example</a>
```
az sentinel alert-rule delete --resource-group "myRg" --rule-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" \
--workspace-name "myWorkspace"
```
##### <a name="ParametersAlertRulesDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--rule-id**|string|Alert rule ID|rule_id|ruleId|

### group `az sentinel alert-rule template`
#### <a name="AlertRuleTemplatesList">Command `az sentinel alert-rule template list`</a>

##### <a name="ExamplesAlertRuleTemplatesList">Example</a>
```
az sentinel alert-rule template list --resource-group "myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersAlertRuleTemplatesList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|

#### <a name="AlertRuleTemplatesGet">Command `az sentinel alert-rule template show`</a>

##### <a name="ExamplesAlertRuleTemplatesGet">Example</a>
```
az sentinel alert-rule template show --alert-rule-template-id "65360bb0-8986-4ade-a89d-af3cf44d28aa" --resource-group \
"myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersAlertRuleTemplatesGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--alert-rule-template-id**|string|Alert rule template ID|alert_rule_template_id|alertRuleTemplateId|

### group `az sentinel analytic-setting`
#### <a name="SecurityMLAnalyticsSettingsList">Command `az sentinel analytic-setting list`</a>

##### <a name="ExamplesSecurityMLAnalyticsSettingsList">Example</a>
```
az sentinel analytic-setting list --resource-group "myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersSecurityMLAnalyticsSettingsList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|

#### <a name="SecurityMLAnalyticsSettingsGet">Command `az sentinel analytic-setting show`</a>

##### <a name="ExamplesSecurityMLAnalyticsSettingsGet">Example</a>
```
az sentinel analytic-setting show --resource-group "myRg" --settings-resource-name "myFirstAnomalySettings" \
--workspace-name "myWorkspace"
```
##### <a name="ParametersSecurityMLAnalyticsSettingsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--settings-resource-name**|string|Security ML Analytics Settings resource name|settings_resource_name|settingsResourceName|

#### <a name="SecurityMLAnalyticsSettingsCreateOrUpdate#Create">Command `az sentinel analytic-setting create`</a>

##### <a name="ExamplesSecurityMLAnalyticsSettingsCreateOrUpdate#Create">Example</a>
```
az sentinel analytic-setting create --resource-group "myRg" --settings "{\\"etag\\":\\"\\\\\\"260090e2-0000-0d00-0000-5\
d6fb8670000\\\\\\"\\",\\"kind\\":\\"Anomaly\\",\\"properties\\":{\\"description\\":\\"When account logs from a source \
region that has rarely been logged in from during the last 14 days, an anomaly is triggered.\\",\\"anomalySettingsVersi\
on\\":0,\\"anomalyVersion\\":\\"1.0.5\\",\\"customizableObservations\\":{\\"multiSelectObservations\\":null,\\"prioriti\
zeExcludeObservations\\":null,\\"singleSelectObservations\\":[{\\"name\\":\\"Device vendor\\",\\"description\\":\\"Sele\
ct device vendor of network connection logs from CommonSecurityLog\\",\\"rerun\\":\\"RerunAlways\\",\\"sequenceNumber\\\
":1,\\"supportedValues\\":[\\"Palo Alto Networks\\",\\"Fortinet\\",\\"Check Point\\"],\\"supportedValuesKql\\":null,\\"\
value\\":[\\"Palo Alto Networks\\"],\\"valuesKql\\":null}],\\"singleValueObservations\\":null,\\"thresholdObservations\
\\":[{\\"name\\":\\"Daily data transfer threshold in MB\\",\\"description\\":\\"Suppress anomalies when daily data \
transfered (in MB) per hour is less than the chosen value\\",\\"maximum\\":\\"100\\",\\"minimum\\":\\"1\\",\\"rerun\\":\
\\"RerunAlways\\",\\"sequenceNumber\\":1,\\"value\\":\\"25\\"},{\\"name\\":\\"Number of standard \
deviations\\",\\"description\\":\\"Triggers anomalies when number of standard deviations is greater than the chosen \
value\\",\\"maximum\\":\\"10\\",\\"minimum\\":\\"2\\",\\"rerun\\":\\"RerunAlways\\",\\"sequenceNumber\\":2,\\"value\\":\
\\"3\\"}]},\\"displayName\\":\\"Login from unusual region\\",\\"enabled\\":true,\\"frequency\\":\\"PT1H\\",\\"isDefault\
Settings\\":true,\\"requiredDataConnectors\\":[{\\"connectorId\\":\\"AWS\\",\\"dataTypes\\":[\\"AWSCloudTrail\\"]}],\\"\
settingsDefinitionId\\":\\"f209187f-1d17-4431-94af-c141bf5f23db\\",\\"settingsStatus\\":\\"Production\\",\\"tactics\\":\
[\\"Exfiltration\\",\\"CommandAndControl\\"],\\"techniques\\":[\\"T1037\\",\\"T1021\\"]}}" --settings-resource-name \
"f209187f-1d17-4431-94af-c141bf5f23db" --workspace-name "myWorkspace"
```
##### <a name="ParametersSecurityMLAnalyticsSettingsCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--settings-resource-name**|string|Security ML Analytics Settings resource name|settings_resource_name|settingsResourceName|
|**--security-ml-analytics-setting**|object|The security ML Analytics setting|security_ml_analytics_setting|securityMLAnalyticsSetting|

#### <a name="SecurityMLAnalyticsSettingsCreateOrUpdate#Update">Command `az sentinel analytic-setting update`</a>


##### <a name="ParametersSecurityMLAnalyticsSettingsCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--settings-resource-name**|string|Security ML Analytics Settings resource name|settings_resource_name|settingsResourceName|
|**--security-ml-analytics-setting**|object|The security ML Analytics setting|security_ml_analytics_setting|securityMLAnalyticsSetting|

#### <a name="SecurityMLAnalyticsSettingsDelete">Command `az sentinel analytic-setting delete`</a>

##### <a name="ExamplesSecurityMLAnalyticsSettingsDelete">Example</a>
```
az sentinel analytic-setting delete --resource-group "myRg" --settings-resource-name "f209187f-1d17-4431-94af-c141bf5f2\
3db" --workspace-name "myWorkspace"
```
##### <a name="ParametersSecurityMLAnalyticsSettingsDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--settings-resource-name**|string|Security ML Analytics Settings resource name|settings_resource_name|settingsResourceName|

### group `az sentinel automation-rule`
#### <a name="AutomationRulesList">Command `az sentinel automation-rule list`</a>

##### <a name="ExamplesAutomationRulesList">Example</a>
```
az sentinel automation-rule list --resource-group "myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersAutomationRulesList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|

#### <a name="AutomationRulesGet">Command `az sentinel automation-rule show`</a>

##### <a name="ExamplesAutomationRulesGet">Example</a>
```
az sentinel automation-rule show --automation-rule-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" --resource-group "myRg" \
--workspace-name "myWorkspace"
```
##### <a name="ParametersAutomationRulesGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--automation-rule-id**|string|Automation rule ID|automation_rule_id|automationRuleId|

#### <a name="AutomationRulesCreateOrUpdate#Create">Command `az sentinel automation-rule create`</a>

##### <a name="ExamplesAutomationRulesCreateOrUpdate#Create">Example</a>
```
az sentinel automation-rule create --etag "\\"0300bf09-0000-0000-0000-5c37296e0000\\"" --actions \
actionConfiguration={"severity":"High"} action-type="ModifyProperties" order=1 --display-name "High severity incidents \
escalation" --order 1 --conditions conditionProperties={"operator":"Contains","propertyName":"IncidentRelatedAnalyticRu\
leIds","propertyValues":["/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.O\
perationalInsights/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/alertRules/fab3d2d4-747f-46a7-8ef0-9c0be\
8112bf7","/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalInsigh\
ts/workspaces/myWorkspace/providers/Microsoft.SecurityInsights/alertRules/8deb8303-e94d-46ff-96e0-5fd94b33df1a"]} \
condition-type="Property" --conditions conditionProperties={"changeType":"ChangedFrom","operator":"Equals","propertyNam\
e":"IncidentStatus","propertyValues":["Closed"]} condition-type="PropertyChanged" --conditions \
conditionProperties={"arrayType":"Alerts","changeType":"Added"} condition-type="PropertyArrayChanged" --is-enabled \
true --triggers-when "Created" --automation-rule-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" --resource-group "myRg" \
--workspace-name "myWorkspace"
```
##### <a name="ParametersAutomationRulesCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--automation-rule-id**|string|Automation rule ID|automation_rule_id|automationRuleId|
|**--etag**|string|Etag of the azure resource|etag|etag|
|**--display-name**|string|The display name of the automation rule.|display_name|displayName|
|**--order**|integer|The order of execution of the automation rule.|order|order|
|**--actions**|array|The actions to execute when the automation rule is triggered.|actions|actions|
|**--is-enabled**|boolean|Determines whether the automation rule is enabled or disabled.|is_enabled|isEnabled|
|**--triggers-when**|choice||triggers_when|triggersWhen|
|**--expiration-time-utc**|date-time|Determines when the automation rule should automatically expire and be disabled.|expiration_time_utc|expirationTimeUtc|
|**--conditions**|array|The conditions to evaluate to determine if the automation rule should be triggered on a given object.|conditions|conditions|

#### <a name="AutomationRulesCreateOrUpdate#Update">Command `az sentinel automation-rule update`</a>


##### <a name="ParametersAutomationRulesCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--automation-rule-id**|string|Automation rule ID|automation_rule_id|automationRuleId|
|**--etag**|string|Etag of the azure resource|etag|etag|
|**--display-name**|string|The display name of the automation rule.|display_name|displayName|
|**--order**|integer|The order of execution of the automation rule.|order|order|
|**--actions**|array|The actions to execute when the automation rule is triggered.|actions|actions|
|**--is-enabled**|boolean|Determines whether the automation rule is enabled or disabled.|is_enabled|isEnabled|
|**--triggers-when**|choice||triggers_when|triggersWhen|
|**--expiration-time-utc**|date-time|Determines when the automation rule should automatically expire and be disabled.|expiration_time_utc|expirationTimeUtc|
|**--conditions**|array|The conditions to evaluate to determine if the automation rule should be triggered on a given object.|conditions|conditions|

#### <a name="AutomationRulesDelete">Command `az sentinel automation-rule delete`</a>

##### <a name="ExamplesAutomationRulesDelete">Example</a>
```
az sentinel automation-rule delete --automation-rule-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" --resource-group "myRg" \
--workspace-name "myWorkspace"
```
##### <a name="ParametersAutomationRulesDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--automation-rule-id**|string|Automation rule ID|automation_rule_id|automationRuleId|

### group `az sentinel bookmark`
#### <a name="BookmarksList">Command `az sentinel bookmark list`</a>

##### <a name="ExamplesBookmarksList">Example</a>
```
az sentinel bookmark list --resource-group "myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersBookmarksList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|

#### <a name="BookmarksGet">Command `az sentinel bookmark show`</a>

##### <a name="ExamplesBookmarksGet">Example</a>
```
az sentinel bookmark show --bookmark-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" --resource-group "myRg" \
--workspace-name "myWorkspace"
```
##### <a name="ParametersBookmarksGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--bookmark-id**|string|Bookmark ID|bookmark_id|bookmarkId|

#### <a name="BookmarksCreateOrUpdate#Create">Command `az sentinel bookmark create`</a>

##### <a name="ExamplesBookmarksCreateOrUpdate#Create">Example</a>
```
az sentinel bookmark create --etag "\\"0300bf09-0000-0000-0000-5c37296e0000\\"" --created "2021-09-01T13:15:30Z" \
--user-info-object-id "2046feea-040d-4a46-9e2b-91c2941bfa70" --display-name "My bookmark" --entity-mappings \
"[{\\"entityType\\":\\"Account\\",\\"fieldMappings\\":[{\\"identifier\\":\\"Fullname\\",\\"value\\":\\"johndoe@microsof\
t.com\\"}]}]" --labels "Tag1" "Tag2" --notes "Found a suspicious activity" --query-content "SecurityEvent | where \
TimeGenerated > ago(1d) and TimeGenerated < ago(2d)" --query-result "Security Event query result" --tactics \
"Execution" --techniques "T1609" --updated "2021-09-01T13:15:30Z" --object-id "2046feea-040d-4a46-9e2b-91c2941bfa70" \
--bookmark-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" --resource-group "myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersBookmarksCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--bookmark-id**|string|Bookmark ID|bookmark_id|bookmarkId|
|**--etag**|string|Etag of the azure resource|etag|etag|
|**--created**|date-time|The time the bookmark was created|created|created|
|**--display-name**|string|The display name of the bookmark|display_name|displayName|
|**--labels**|array|List of labels relevant to this bookmark|labels|labels|
|**--notes**|string|The notes of the bookmark|notes|notes|
|**--query-content**|string|The query of the bookmark.|query_content|query|
|**--query-result**|string|The query result of the bookmark.|query_result|queryResult|
|**--updated**|date-time|The last time the bookmark was updated|updated|updated|
|**--event-time**|date-time|The bookmark event time|event_time|eventTime|
|**--query-start-time**|date-time|The start time for the query|query_start_time|queryStartTime|
|**--query-end-time**|date-time|The end time for the query|query_end_time|queryEndTime|
|**--incident-info**|object|Describes an incident that relates to bookmark|incident_info|incidentInfo|
|**--entity-mappings**|array|Describes the entity mappings of the bookmark|entity_mappings|entityMappings|
|**--tactics**|array|A list of relevant mitre attacks|tactics|tactics|
|**--techniques**|array|A list of relevant mitre techniques|techniques|techniques|
|**--object-id**|uuid|The object id of the user.|object_id|objectId|
|**--user-info-object-id**|uuid|The object id of the user.|user_info_object_id|objectId|

#### <a name="BookmarksCreateOrUpdate#Update">Command `az sentinel bookmark update`</a>


##### <a name="ParametersBookmarksCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--bookmark-id**|string|Bookmark ID|bookmark_id|bookmarkId|
|**--etag**|string|Etag of the azure resource|etag|etag|
|**--created**|date-time|The time the bookmark was created|created|created|
|**--display-name**|string|The display name of the bookmark|display_name|displayName|
|**--labels**|array|List of labels relevant to this bookmark|labels|labels|
|**--notes**|string|The notes of the bookmark|notes|notes|
|**--query-content**|string|The query of the bookmark.|query_content|query|
|**--query-result**|string|The query result of the bookmark.|query_result|queryResult|
|**--updated**|date-time|The last time the bookmark was updated|updated|updated|
|**--event-time**|date-time|The bookmark event time|event_time|eventTime|
|**--query-start-time**|date-time|The start time for the query|query_start_time|queryStartTime|
|**--query-end-time**|date-time|The end time for the query|query_end_time|queryEndTime|
|**--incident-info**|object|Describes an incident that relates to bookmark|incident_info|incidentInfo|
|**--entity-mappings**|array|Describes the entity mappings of the bookmark|entity_mappings|entityMappings|
|**--tactics**|array|A list of relevant mitre attacks|tactics|tactics|
|**--techniques**|array|A list of relevant mitre techniques|techniques|techniques|
|**--object-id**|uuid|The object id of the user.|object_id|objectId|
|**--user-info-object-id**|uuid|The object id of the user.|user_info_object_id|objectId|

#### <a name="BookmarksDelete">Command `az sentinel bookmark delete`</a>

##### <a name="ExamplesBookmarksDelete">Example</a>
```
az sentinel bookmark delete --bookmark-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" --resource-group "myRg" \
--workspace-name "myWorkspace"
```
##### <a name="ParametersBookmarksDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--bookmark-id**|string|Bookmark ID|bookmark_id|bookmarkId|

#### <a name="BookmarksExpand">Command `az sentinel bookmark expand`</a>

##### <a name="ExamplesBookmarksExpand">Example</a>
```
az sentinel bookmark expand --bookmark-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" --end-time "2020-01-24T17:21:00.000Z" \
--expansion-id "27f76e63-c41b-480f-bb18-12ad2e011d49" --start-time "2019-12-25T17:21:00.000Z" --resource-group "myRg" \
--workspace-name "myWorkspace"
```
##### <a name="ParametersBookmarksExpand">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--bookmark-id**|string|Bookmark ID|bookmark_id|bookmarkId|
|**--end-time**|date-time|The end date filter, so the only expansion results returned are before this date.|end_time|endTime|
|**--expansion-id**|uuid|The Id of the expansion to perform.|expansion_id|expansionId|
|**--start-time**|date-time|The start date filter, so the only expansion results returned are after this date.|start_time|startTime|

### group `az sentinel bookmark relation`
#### <a name="BookmarkRelationsList">Command `az sentinel bookmark relation list`</a>

##### <a name="ExamplesBookmarkRelationsList">Example</a>
```
az sentinel bookmark relation list --bookmark-id "2216d0e1-91e3-4902-89fd-d2df8c535096" --resource-group "myRg" \
--workspace-name "myWorkspace"
```
##### <a name="ParametersBookmarkRelationsList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--bookmark-id**|string|Bookmark ID|bookmark_id|bookmarkId|
|**--filter**|string|Filters the results, based on a Boolean condition. Optional.|filter|$filter|
|**--orderby**|string|Sorts the results. Optional.|orderby|$orderby|
|**--top**|integer|Returns only the first n results. Optional.|top|$top|
|**--skip-token**|string|Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. Optional.|skip_token|$skipToken|

#### <a name="BookmarkRelationsGet">Command `az sentinel bookmark relation show`</a>

##### <a name="ExamplesBookmarkRelationsGet">Example</a>
```
az sentinel bookmark relation show --bookmark-id "2216d0e1-91e3-4902-89fd-d2df8c535096" --relation-name \
"4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014" --resource-group "myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersBookmarkRelationsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--bookmark-id**|string|Bookmark ID|bookmark_id|bookmarkId|
|**--relation-name**|string|Relation Name|relation_name|relationName|

#### <a name="BookmarkRelationsCreateOrUpdate#Create">Command `az sentinel bookmark relation create`</a>

##### <a name="ExamplesBookmarkRelationsCreateOrUpdate#Create">Example</a>
```
az sentinel bookmark relation create --bookmark-id "2216d0e1-91e3-4902-89fd-d2df8c535096" --related-resource-id \
"/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalInsights/worksp\
aces/myWorkspace/providers/Microsoft.SecurityInsights/incidents/afbd324f-6c48-459c-8710-8d1e1cd03812" --relation-name \
"4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014" --resource-group "myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersBookmarkRelationsCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--bookmark-id**|string|Bookmark ID|bookmark_id|bookmarkId|
|**--relation-name**|string|Relation Name|relation_name|relationName|
|**--etag**|string|Etag of the azure resource|etag|etag|
|**--related-resource-id**|string|The resource ID of the related resource|related_resource_id|relatedResourceId|

#### <a name="BookmarkRelationsCreateOrUpdate#Update">Command `az sentinel bookmark relation update`</a>


##### <a name="ParametersBookmarkRelationsCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--bookmark-id**|string|Bookmark ID|bookmark_id|bookmarkId|
|**--relation-name**|string|Relation Name|relation_name|relationName|
|**--etag**|string|Etag of the azure resource|etag|etag|
|**--related-resource-id**|string|The resource ID of the related resource|related_resource_id|relatedResourceId|

#### <a name="BookmarkRelationsDelete">Command `az sentinel bookmark relation delete`</a>

##### <a name="ExamplesBookmarkRelationsDelete">Example</a>
```
az sentinel bookmark relation delete --bookmark-id "2216d0e1-91e3-4902-89fd-d2df8c535096" --relation-name \
"4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014" --resource-group "myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersBookmarkRelationsDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--bookmark-id**|string|Bookmark ID|bookmark_id|bookmarkId|
|**--relation-name**|string|Relation Name|relation_name|relationName|

### group `az sentinel data-connector`
#### <a name="DataConnectorsList">Command `az sentinel data-connector list`</a>

##### <a name="ExamplesDataConnectorsList">Example</a>
```
az sentinel data-connector list --resource-group "myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersDataConnectorsList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|

#### <a name="DataConnectorsGet">Command `az sentinel data-connector show`</a>

##### <a name="ExamplesDataConnectorsGet">Example</a>
```
az sentinel data-connector show --data-connector-id "316ec55e-7138-4d63-ab18-90c8a60fd1c8" --resource-group "myRg" \
--workspace-name "myWorkspace"
az sentinel data-connector show --data-connector-id "763f9fa1-c2d3-4fa2-93e9-bccd4899aa12" --resource-group "myRg" \
--workspace-name "myWorkspace"
az sentinel data-connector show --data-connector-id "c2541efb-c9a6-47fe-9501-87d1017d1512" --resource-group "myRg" \
--workspace-name "myWorkspace"
az sentinel data-connector show --data-connector-id "316ec55e-7138-4d63-ab18-90c8a60fd1c8" --resource-group "myRg" \
--workspace-name "myWorkspace"
az sentinel data-connector show --data-connector-id "d2e5dc7a-f3a2-429d-954b-939fa8c2932e" --resource-group "myRg" \
--workspace-name "myWorkspace"
az sentinel data-connector show --data-connector-id "b96d014d-b5c2-4a01-9aba-a8058f629d42" --resource-group "myRg" \
--workspace-name "myWorkspace"
az sentinel data-connector show --data-connector-id "06b3ccb8-1384-4bcc-aec7-852f6d57161b" --resource-group "myRg" \
--workspace-name "myWorkspace"
az sentinel data-connector show --data-connector-id "c345bf40-8509-4ed2-b947-50cb773aaf04" --resource-group "myRg" \
--workspace-name "myWorkspace"
az sentinel data-connector show --data-connector-id "c345bf40-8509-4ed2-b947-50cb773aaf04" --resource-group "myRg" \
--workspace-name "myWorkspace"
az sentinel data-connector show --data-connector-id "c39bb458-02a7-4b3f-b0c8-71a1d2692652" --resource-group "myRg" \
--workspace-name "myWorkspace"
az sentinel data-connector show --data-connector-id "c345bf40-8509-4ed2-b947-50cb773aaf04" --resource-group "myRg" \
--workspace-name "myWorkspace"
az sentinel data-connector show --data-connector-id "f0cd27d2-5f03-4c06-ba31-d2dc82dcb51d" --resource-group "myRg" \
--workspace-name "myWorkspace"
az sentinel data-connector show --data-connector-id "07e42cb3-e658-4e90-801c-efa0f29d3d44" --resource-group "myRg" \
--workspace-name "myWorkspace"
az sentinel data-connector show --data-connector-id "afef3743-0c88-469c-84ff-ca2e87dc1e48" --resource-group "myRg" \
--workspace-name "myWorkspace"
az sentinel data-connector show --data-connector-id "c345bf40-8509-4ed2-b947-50cb773aaf04" --resource-group "myRg" \
--workspace-name "myWorkspace"
az sentinel data-connector show --data-connector-id "3d3e955e-33eb-401d-89a7-251c81ddd660" --resource-group "myRg" \
--workspace-name "myWorkspace"
az sentinel data-connector show --data-connector-id "3d3e955e-33eb-401d-89a7-251c81ddd660" --resource-group "myRg" \
--workspace-name "myWorkspace"
az sentinel data-connector show --data-connector-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" --resource-group "myRg" \
--workspace-name "myWorkspace"
az sentinel data-connector show --data-connector-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" --resource-group "myRg" \
--workspace-name "myWorkspace"
az sentinel data-connector show --data-connector-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" --resource-group "myRg" \
--workspace-name "myWorkspace"
```
##### <a name="ParametersDataConnectorsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--data-connector-id**|string|Connector ID|data_connector_id|dataConnectorId|

#### <a name="DataConnectorsCreateOrUpdate#Create">Command `az sentinel data-connector create`</a>

##### <a name="ExamplesDataConnectorsCreateOrUpdate#Create">Example</a>
```
az sentinel data-connector create --data-connector "{\\"kind\\":\\"APIPolling\\",\\"properties\\":{\\"connectorUiConfig\
\\":{\\"availability\\":{\\"isPreview\\":true,\\"status\\":1},\\"connectivityCriteria\\":[{\\"type\\":\\"SentinelKindsV\
2\\",\\"value\\":[]}],\\"dataTypes\\":[{\\"name\\":\\"{{graphQueriesTableName}}\\",\\"lastDataReceivedQuery\\":\\"{{gra\
phQueriesTableName}}\\\\n            | summarize Time = max(TimeGenerated)\\\\n            | where \
isnotempty(Time)\\"}],\\"descriptionMarkdown\\":\\"The GitHub audit log connector provides the capability to ingest \
GitHub logs into Azure Sentinel. By connecting GitHub audit logs into Azure Sentinel, you can view this data in \
workbooks, use it to create custom alerts, and improve your investigation process.\\",\\"graphQueries\\":[{\\"baseQuery\
\\":\\"{{graphQueriesTableName}}\\",\\"legend\\":\\"GitHub audit log events\\",\\"metricName\\":\\"Total events \
received\\"}],\\"graphQueriesTableName\\":\\"GitHubAuditLogPolling_CL\\",\\"instructionSteps\\":[{\\"description\\":\\"\
Enable GitHub audit Logs. \\\\n Follow [this](https://docs.github.com/en/github/authenticating-to-github/keeping-your-a\
ccount-and-data-secure/creating-a-personal-access-token) to create or find your personal \
key\\",\\"instructions\\":[{\\"type\\":\\"APIKey\\",\\"parameters\\":{\\"enable\\":\\"true\\",\\"userRequestPlaceHolder\
sInput\\":[{\\"displayText\\":\\"Organization Name\\",\\"placeHolderName\\":\\"{{placeHolder1}}\\",\\"placeHolderValue\
\\":\\"\\",\\"requestObjectKey\\":\\"apiEndpoint\\"}]}}],\\"title\\":\\"Connect GitHub Enterprise Audit Log to Azure \
Sentinel\\"}],\\"permissions\\":{\\"customs\\":[{\\"name\\":\\"GitHub API personal token \
Key\\",\\"description\\":\\"You need access to GitHub personal token, the key should have \'admin:org\' \
scope\\"}],\\"resourceProvider\\":[{\\"permissionsDisplayText\\":\\"read and write permissions are \
required.\\",\\"provider\\":\\"Microsoft.OperationalInsights/workspaces\\",\\"providerDisplayName\\":\\"Workspace\\",\\\
"requiredPermissions\\":{\\"delete\\":true,\\"read\\":true,\\"write\\":true},\\"scope\\":\\"Workspace\\"}]},\\"publishe\
r\\":\\"GitHub\\",\\"sampleQueries\\":[{\\"description\\":\\"All logs\\",\\"query\\":\\"{{graphQueriesTableName}}\\\\n \
| take 10 <change>\\"}],\\"title\\":\\"GitHub Enterprise Audit Log\\"},\\"pollingConfig\\":{\\"auth\\":{\\"apiKeyIdenti\
fier\\":\\"token\\",\\"apiKeyName\\":\\"Authorization\\",\\"authType\\":\\"APIKey\\"},\\"paging\\":{\\"pageSizeParaName\
\\":\\"per_page\\",\\"pagingType\\":\\"LinkHeader\\"},\\"response\\":{\\"eventsJsonPaths\\":[\\"$\\"]},\\"request\\":{\
\\"apiEndpoint\\":\\"https://api.github.com/organizations/{{placeHolder1}}/audit-log\\",\\"headers\\":{\\"Accept\\":\\"\
application/json\\",\\"User-Agent\\":\\"Scuba\\"},\\"httpMethod\\":\\"Get\\",\\"queryParameters\\":{\\"phrase\\":\\"cre\
ated:{_QueryWindowStartTime}..{_QueryWindowEndTime}\\"},\\"queryTimeFormat\\":\\"yyyy-MM-ddTHH:mm:ssZ\\",\\"queryWindow\
InMin\\":15,\\"rateLimitQps\\":50,\\"retryCount\\":2,\\"timeoutInSeconds\\":60}}}}" --data-connector-id \
"316ec55e-7138-4d63-ab18-90c8a60fd1c8" --resource-group "myRg" --workspace-name "myWorkspace"
az sentinel data-connector create --data-connector "{\\"etag\\":\\"\\\\\\"0300bf09-0000-0000-0000-5c37296e0000\\\\\\"\\\
",\\"kind\\":\\"Dynamics365\\",\\"properties\\":{\\"dataTypes\\":{\\"dynamics365CdsActivities\\":{\\"state\\":\\"Enable\
d\\"}},\\"tenantId\\":\\"2070ecc9-b4d5-4ae4-adaa-936fa1954fa8\\"}}" --data-connector-id "c2541efb-c9a6-47fe-9501-87d101\
7d1512" --resource-group "myRg" --workspace-name "myWorkspace"
az sentinel data-connector create --data-connector "{\\"kind\\":\\"GenericUI\\",\\"properties\\":{\\"connectorUiConfig\
\\":{\\"availability\\":{\\"isPreview\\":true,\\"status\\":1},\\"connectivityCriteria\\":[{\\"type\\":\\"IsConnectedQue\
ry\\",\\"value\\":[\\"{{graphQueriesTableName}}\\\\n            | summarize LastLogReceived = max(TimeGenerated)\\\\n  \
          | project IsConnected = LastLogReceived > ago(30d)\\"]}],\\"dataTypes\\":[{\\"name\\":\\"{{graphQueriesTableN\
ame}}\\",\\"lastDataReceivedQuery\\":\\"{{graphQueriesTableName}}\\\\n            | summarize Time = \
max(TimeGenerated)\\\\n            | where isnotempty(Time)\\"}],\\"descriptionMarkdown\\":\\"The [Qualys \
Vulnerability Management (VM)](https://www.qualys.com/apps/vulnerability-management/) data connector provides the \
capability to ingest vulnerability host detection data into Azure Sentinel through the Qualys API. The connector \
provides visibility into host detection data from vulerability scans. This connector provides Azure Sentinel the \
capability to view dashboards, create custom alerts, and improve investigation \\",\\"graphQueries\\":[{\\"baseQuery\\"\
:\\"{{graphQueriesTableName}}\\",\\"legend\\":\\"{{graphQueriesTableName}}\\",\\"metricName\\":\\"Total data \
received\\"}],\\"graphQueriesTableName\\":\\"QualysHostDetection_CL\\",\\"instructionSteps\\":[{\\"description\\":\\">*\
*NOTE:** This connector uses Azure Functions to connect to Qualys VM to pull its logs into Azure Sentinel. This might \
result in additional data ingestion costs. Check the [Azure Functions pricing page](https://azure.microsoft.com/pricing\
/details/functions/) for details.\\",\\"title\\":\\"\\"},{\\"description\\":\\">**(Optional Step)** Securely store \
workspace and API authorization key(s) or token(s) in Azure Key Vault. Azure Key Vault provides a secure mechanism to \
store and retrieve key values. [Follow these instructions](https://docs.microsoft.com/azure/app-service/app-service-key\
-vault-references) to use Azure Key Vault with an Azure Function App.\\",\\"title\\":\\"\\"},{\\"description\\":\\"**ST\
EP 1 - Configuration steps for the Qualys VM API**\\\\n\\\\n1. Log into the Qualys Vulnerability Management console \
with an administrator account, select the **Users** tab and the **Users** subtab. \\\\n2. Click on the **New** \
drop-down menu and select **Users..**\\\\n3. Create a username and password for the API account. \\\\n4. In the **User \
Roles** tab, ensure the account role is set to **Manager** and access is allowed to **GUI** and **API**\\\\n4. Log out \
of the administrator account and log into the console with the new API credentials for validation, then log out of the \
API account. \\\\n5. Log back into the console using an administrator account and modify the API accounts User Roles, \
removing access to **GUI**. \\\\n6. Save all changes.\\",\\"title\\":\\"\\"},{\\"description\\":\\"**STEP 2 - Choose \
ONE from the following two deployment options to deploy the connector and the associated Azure \
Function**\\\\n\\\\n>**IMPORTANT:** Before deploying the Qualys VM connector, have the Workspace ID and Workspace \
Primary Key (can be copied from the following), as well as the Qualys VM API Authorization Key(s), readily \
available.\\",\\"instructions\\":[{\\"type\\":\\"CopyableLabel\\",\\"parameters\\":{\\"fillWith\\":[\\"WorkspaceId\\"],\
\\"label\\":\\"Workspace ID\\"}},{\\"type\\":\\"CopyableLabel\\",\\"parameters\\":{\\"fillWith\\":[\\"PrimaryKey\\"],\\\
"label\\":\\"Primary Key\\"}}],\\"title\\":\\"\\"},{\\"description\\":\\"Use this method for automated deployment of \
the Qualys VM connector using an ARM Tempate.\\\\n\\\\n1. Click the **Deploy to Azure** button below. \
\\\\n\\\\n\\\\t[![Deploy To Azure](https://aka.ms/deploytoazurebutton)](https://aka.ms/sentinelqualysvmazuredeploy)\\\\\
n2. Select the preferred **Subscription**, **Resource Group** and **Location**. \\\\n3. Enter the **Workspace ID**, \
**Workspace Key**, **API Username**, **API Password** , update the **URI**, and any additional URI **Filter \
Parameters** (each filter should be separated by an \\\\\\"&\\\\\\" symbol, no spaces.) \\\\n> - Enter the URI that \
corresponds to your region. The complete list of API Server URLs can be [found here](https://www.qualys.com/docs/qualys\
-api-vmpc-user-guide.pdf#G4.735348) -- There is no need to add a time suffix to the URI, the Function App will \
dynamically append the Time Value to the URI in the proper format. \\\\n - The default **Time Interval** is set to \
pull the last five (5) minutes of data. If the time interval needs to be modified, it is recommended to change the \
Function App Timer Trigger accordingly (in the function.json file, post deployment) to prevent overlapping data \
ingestion. \\\\n> - Note: If using Azure Key Vault secrets for any of the values above, use \
the`@Microsoft.KeyVault(SecretUri={Security Identifier})`schema in place of the string values. Refer to [Key Vault \
references documentation](https://docs.microsoft.com/azure/app-service/app-service-key-vault-references) for further \
details. \\\\n4. Mark the checkbox labeled **I agree to the terms and conditions stated above**. \\\\n5. Click \
**Purchase** to deploy.\\",\\"title\\":\\"Option 1 - Azure Resource Manager (ARM) Template\\"},{\\"description\\":\\"Us\
e the following step-by-step instructions to deploy the Quayls VM connector manually with Azure \
Functions.\\",\\"title\\":\\"Option 2 - Manual Deployment of Azure Functions\\"},{\\"description\\":\\"**1. Create a \
Function App**\\\\n\\\\n1.  From the Azure Portal, navigate to [Function App](https://portal.azure.com/#blade/HubsExten\
sion/BrowseResource/resourceType/Microsoft.Web%2Fsites/kind/functionapp), and select **+ Add**.\\\\n2. In the \
**Basics** tab, ensure Runtime stack is set to **Powershell Core**. \\\\n3. In the **Hosting** tab, ensure the \
**Consumption (Serverless)** plan type is selected.\\\\n4. Make other preferrable configuration changes, if needed, \
then click **Create**.\\",\\"title\\":\\"\\"},{\\"description\\":\\"**2. Import Function App Code**\\\\n\\\\n1. In the \
newly created Function App, select **Functions** on the left pane and click **+ New Function**.\\\\n2. Select **Timer \
Trigger**.\\\\n3. Enter a unique Function **Name** and leave the default cron schedule of every 5 minutes, then click \
**Create**.\\\\n5. Click on **Code + Test** on the left pane. \\\\n6. Copy the [Function App \
Code](https://aka.ms/sentinelqualysvmazurefunctioncode) and paste into the Function App `run.ps1` editor.\\\\n7. Click \
**Save**.\\",\\"title\\":\\"\\"},{\\"description\\":\\"**3. Configure the Function App**\\\\n\\\\n1. In the Function \
App, select the Function App Name and select **Configuration**.\\\\n2. In the **Application settings** tab, select **+ \
New application setting**.\\\\n3. Add each of the following seven (7) application settings individually, with their \
respective string values (case-sensitive): \\\\n\\\\t\\\\tapiUsername\\\\n\\\\t\\\\tapiPassword\\\\n\\\\t\\\\tworkspace\
ID\\\\n\\\\t\\\\tworkspaceKey\\\\n\\\\t\\\\turi\\\\n\\\\t\\\\tfilterParameters\\\\n\\\\t\\\\ttimeInterval\\\\n> - \
Enter the URI that corresponds to your region. The complete list of API Server URLs can be [found \
here](https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf#G4.735348). The `uri` value must follow the following \
schema: `https://<API Server>/api/2.0/fo/asset/host/vm/detection/?action=list&vm_processed_after=` -- There is no need \
to add a time suffix to the URI, the Function App will dynamically append the Time Value to the URI in the proper \
format.\\\\n> - Add any additional filter parameters, for the `filterParameters` variable, that need to be appended to \
the URI. Each parameter should be seperated by an \\\\\\"&\\\\\\" symbol and should not include any spaces.\\\\n> - \
Set the `timeInterval` (in minutes) to the value of `5` to correspond to the Timer Trigger of every `5` minutes. If \
the time interval needs to be modified, it is recommended to change the Function App Timer Trigger accordingly to \
prevent overlapping data ingestion.\\\\n> - Note: If using Azure Key Vault, use the`@Microsoft.KeyVault(SecretUri={Secu\
rity Identifier})`schema in place of the string values. Refer to [Key Vault references documentation](https://docs.micr\
osoft.com/azure/app-service/app-service-key-vault-references) for further details.\\\\n4. Once all application \
settings have been entered, click **Save**.\\",\\"title\\":\\"\\"},{\\"description\\":\\"**4. Configure the \
host.json**.\\\\n\\\\nDue to the potentially large amount of Qualys host detection data being ingested, it can cause \
the execution time to surpass the default Function App timeout of five (5) minutes. Increase the default timeout \
duration to the maximum of ten (10) minutes, under the Consumption Plan, to allow more time for the Function App to \
execute.\\\\n\\\\n1. In the Function App, select the Function App Name and select the **App Service Editor** \
blade.\\\\n2. Click **Go** to open the editor, then select the **host.json** file under the **wwwroot** \
directory.\\\\n3. Add the line `\\\\\\"functionTimeout\\\\\\": \\\\\\"00:10:00\\\\\\",` above the `managedDependancy` \
line \\\\n4. Ensure **SAVED** appears on the top right corner of the editor, then exit the editor.\\\\n\\\\n> NOTE: If \
a longer timeout duration is required, consider upgrading to an [App Service Plan](https://docs.microsoft.com/azure/azu\
re-functions/functions-scale#timeout)\\",\\"title\\":\\"\\"}],\\"permissions\\":{\\"customs\\":[{\\"name\\":\\"Microsof\
t.Web/sites permissions\\",\\"description\\":\\"Read and write permissions to Azure Functions to create a Function App \
is required. [See the documentation to learn more about Azure Functions](https://docs.microsoft.com/azure/azure-functio\
ns/).\\"},{\\"name\\":\\"Qualys API Key\\",\\"description\\":\\"A Qualys VM API username and password is required. \
[See the documentation to learn more about Qualys VM API](https://www.qualys.com/docs/qualys-api-vmpc-user-guide.pdf).\
\\"}],\\"resourceProvider\\":[{\\"permissionsDisplayText\\":\\"read and write permissions on the workspace are \
required.\\",\\"provider\\":\\"Microsoft.OperationalInsights/workspaces\\",\\"providerDisplayName\\":\\"Workspace\\",\\\
"requiredPermissions\\":{\\"delete\\":true,\\"read\\":true,\\"write\\":true},\\"scope\\":\\"Workspace\\"},{\\"permissio\
nsDisplayText\\":\\"read permissions to shared keys for the workspace are required. [See the documentation to learn \
more about workspace keys](https://docs.microsoft.com/azure/azure-monitor/platform/agent-windows#obtain-workspace-id-an\
d-key).\\",\\"provider\\":\\"Microsoft.OperationalInsights/workspaces/sharedKeys\\",\\"providerDisplayName\\":\\"Keys\\\
",\\"requiredPermissions\\":{\\"action\\":true},\\"scope\\":\\"Workspace\\"}]},\\"publisher\\":\\"Qualys\\",\\"sampleQu\
eries\\":[{\\"description\\":\\"Top 10 Vulerabilities detected\\",\\"query\\":\\"{{graphQueriesTableName}}\\\\n | \
mv-expand todynamic(Detections_s)\\\\n | extend Vulnerability = tostring(Detections_s.Results)\\\\n | summarize \
count() by Vulnerability\\\\n | top 10 by count_\\"}],\\"title\\":\\"Qualys Vulnerability Management (CCP DEMO)\\"}}}" \
--data-connector-id "316ec55e-7138-4d63-ab18-90c8a60fd1c8" --resource-group "myRg" --workspace-name "myWorkspace"
az sentinel data-connector create --data-connector "{\\"etag\\":\\"d12423f6-a60b-4ca5-88c0-feb1a182d0f0\\",\\"kind\\":\
\\"ThreatIntelligenceTaxii\\",\\"properties\\":{\\"collectionId\\":\\"135\\",\\"dataTypes\\":{\\"taxiiClient\\":{\\"sta\
te\\":\\"Enabled\\"}},\\"friendlyName\\":\\"testTaxii\\",\\"password\\":\\"--\\",\\"pollingFrequency\\":\\"OnceADay\\",\
\\"taxiiLookbackPeriod\\":\\"2020-01-01T13:00:30.123Z\\",\\"taxiiServer\\":\\"https://limo.anomali.com/api/v1/taxii2/fe\
eds\\",\\"tenantId\\":\\"06b3ccb8-1384-4bcc-aec7-852f6d57161b\\",\\"userName\\":\\"--\\",\\"workspaceId\\":\\"dd124572-\
4962-4495-9bd2-9dade12314b4\\"}}" --data-connector-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" --resource-group "myRg" \
--workspace-name "myWorkspace"
az sentinel data-connector create --data-connector "{\\"etag\\":\\"\\\\\\"0300bf09-0000-0000-0000-5c37296e0000\\\\\\"\\\
",\\"kind\\":\\"OfficePowerBI\\",\\"properties\\":{\\"dataTypes\\":{\\"logs\\":{\\"state\\":\\"Enabled\\"}},\\"tenantId\
\\":\\"2070ecc9-b4d5-4ae4-adaa-936fa1954fa8\\"}}" --data-connector-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" \
--resource-group "myRg" --workspace-name "myWorkspace"
az sentinel data-connector create --data-connector "{\\"etag\\":\\"\\\\\\"0300bf09-0000-0000-0000-5c37296e0000\\\\\\"\\\
",\\"kind\\":\\"Office365Project\\",\\"properties\\":{\\"dataTypes\\":{\\"logs\\":{\\"state\\":\\"Enabled\\"}},\\"tenan\
tId\\":\\"2070ecc9-b4d5-4ae4-adaa-936fa1954fa8\\"}}" --data-connector-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" \
--resource-group "myRg" --workspace-name "myWorkspace"
az sentinel data-connector create --data-connector "{\\"etag\\":\\"\\\\\\"0300bf09-0000-0000-0000-5c37296e0000\\\\\\"\\\
",\\"kind\\":\\"Office365\\",\\"properties\\":{\\"dataTypes\\":{\\"exchange\\":{\\"state\\":\\"Enabled\\"},\\"sharePoin\
t\\":{\\"state\\":\\"Enabled\\"},\\"teams\\":{\\"state\\":\\"Enabled\\"}},\\"tenantId\\":\\"2070ecc9-b4d5-4ae4-adaa-936\
fa1954fa8\\"}}" --data-connector-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" --resource-group "myRg" --workspace-name \
"myWorkspace"
az sentinel data-connector create --data-connector "{\\"kind\\":\\"ThreatIntelligence\\",\\"properties\\":{\\"dataTypes\
\\":{\\"indicators\\":{\\"state\\":\\"Enabled\\"}},\\"tenantId\\":\\"06b3ccb8-1384-4bcc-aec7-852f6d57161b\\",\\"tipLook\
backPeriod\\":\\"2020-01-01T13:00:30.123Z\\"}}" --data-connector-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" \
--resource-group "myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersDataConnectorsCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--data-connector-id**|string|Connector ID|data_connector_id|dataConnectorId|
|**--data-connector**|object|The data connector|data_connector|dataConnector|

#### <a name="DataConnectorsCreateOrUpdate#Update">Command `az sentinel data-connector update`</a>


##### <a name="ParametersDataConnectorsCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--data-connector-id**|string|Connector ID|data_connector_id|dataConnectorId|
|**--data-connector**|object|The data connector|data_connector|dataConnector|

#### <a name="DataConnectorsDelete">Command `az sentinel data-connector delete`</a>

##### <a name="ExamplesDataConnectorsDelete">Example</a>
```
az sentinel data-connector delete --data-connector-id "316ec55e-7138-4d63-ab18-90c8a60fd1c8" --resource-group "myRg" \
--workspace-name "myWorkspace"
az sentinel data-connector delete --data-connector-id "316ec55e-7138-4d63-ab18-90c8a60fd1c8" --resource-group "myRg" \
--workspace-name "myWorkspace"
az sentinel data-connector delete --data-connector-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" --resource-group "myRg" \
--workspace-name "myWorkspace"
az sentinel data-connector delete --data-connector-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" --resource-group "myRg" \
--workspace-name "myWorkspace"
az sentinel data-connector delete --data-connector-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" --resource-group "myRg" \
--workspace-name "myWorkspace"
```
##### <a name="ParametersDataConnectorsDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--data-connector-id**|string|Connector ID|data_connector_id|dataConnectorId|

#### <a name="DataConnectorsConnect">Command `az sentinel data-connector connect`</a>

##### <a name="ExamplesDataConnectorsConnect">Example</a>
```
az sentinel data-connector connect --api-key "123456789" --endpoint "https://test.eastus.ingest.monitor.azure.com" \
--rule-immutable-id "dcr-34adsj9o7d6f9de204478b9cgb43b631" --kind "APIKey" --output-stream "Custom-MyTableRawData" \
--input-values "[{\\"displayText\\":\\"Organization Name\\",\\"placeHolderName\\":\\"{{placeHolder1}}\\",\\"placeHolder\
Value\\":\\"somePlaceHolderValue\\",\\"requestObjectKey\\":\\"apiEndpoint\\"}]" --data-connector-id \
"316ec55e-7138-4d63-ab18-90c8a60fd1c8" --resource-group "myRg" --workspace-name "myWorkspace"
az sentinel data-connector connect --api-key "123456789" --kind "APIKey" --input-values "[{\\"displayText\\":\\"Organiz\
ation Name\\",\\"placeHolderName\\":\\"{{placeHolder1}}\\",\\"placeHolderValue\\":\\"somePlaceHolderValue\\",\\"request\
ObjectKey\\":\\"apiEndpoint\\"}]" --data-connector-id "316ec55e-7138-4d63-ab18-90c8a60fd1c8" --resource-group "myRg" \
--workspace-name "myWorkspace"
```
##### <a name="ParametersDataConnectorsConnect">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--data-connector-id**|string|Connector ID|data_connector_id|dataConnectorId|
|**--kind**|choice|The authentication kind used to poll the data|kind|kind|
|**--api-key**|string|The API key of the audit server.|api_key|apiKey|
|**--data-collection-endpoint**|string|Used in v2 logs connector. Represents the data collection ingestion endpoint in log analytics.|data_collection_endpoint|dataCollectionEndpoint|
|**--data-collection-rule-immutable-id**|string|Used in v2 logs connector. The data collection rule immutable id, the rule defines the transformation and data destination.|data_collection_rule_immutable_id|dataCollectionRuleImmutableId|
|**--output-stream**|string|Used in v2 logs connector. The stream we are sending the data to, this is the name of the streamDeclarations defined in the DCR.|output_stream|outputStream|
|**--client-secret**|string|The client secret of the OAuth 2.0 application.|client_secret|clientSecret|
|**--client-id**|string|The client id of the OAuth 2.0 application.|client_id|clientId|
|**--authorization-code**|string|The authorization code used in OAuth 2.0 code flow to issue a token.|authorization_code|authorizationCode|
|**--user-name**|string|The user name in the audit log server.|user_name|userName|
|**--password**|string|The user password in the audit log server.|password|password|
|**--request-config-user-input-values**|array||request_config_user_input_values|requestConfigUserInputValues|

#### <a name="DataConnectorsDisconnect">Command `az sentinel data-connector disconnect`</a>

##### <a name="ExamplesDataConnectorsDisconnect">Example</a>
```
az sentinel data-connector disconnect --data-connector-id "316ec55e-7138-4d63-ab18-90c8a60fd1c8" --resource-group \
"myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersDataConnectorsDisconnect">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--data-connector-id**|string|Connector ID|data_connector_id|dataConnectorId|

### group `az sentinel data-connector`
#### <a name="DataConnectorsCheckRequirementsPost">Command `az sentinel data-connector check-requirement`</a>

##### <a name="ExamplesDataConnectorsCheckRequirementsPost">Example</a>
```
az sentinel data-connector check-requirement --aad-check-requirements tenant-id="2070ecc9-b4d5-4ae4-adaa-936fa1954fa8" \
--resource-group "myRg" --workspace-name "myWorkspace"
az sentinel data-connector check-requirement --aad-check-requirements tenant-id="2070ecc9-b4d5-4ae4-adaa-936fa1954fa8" \
--resource-group "myRg" --workspace-name "myWorkspace"
az sentinel data-connector check-requirement --aad-check-requirements tenant-id="2070ecc9-b4d5-4ae4-adaa-936fa1954fa8" \
--resource-group "myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersDataConnectorsCheckRequirementsPost">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--aad-check-requirements**|object|Represents AAD (Azure Active Directory) requirements check request.|aad_check_requirements|AADCheckRequirements|
|**--aatp-check-requirements**|object|Represents AATP (Azure Advanced Threat Protection) requirements check request.|aatp_check_requirements|AATPCheckRequirements|
|**--asc-check-requirements**|object|Represents ASC (Azure Security Center) requirements check request.|asc_check_requirements|ASCCheckRequirements|
|**--aws-cloud-trail-check-requirements**|object|Amazon Web Services CloudTrail requirements check request.|aws_cloud_trail_check_requirements|AwsCloudTrailCheckRequirements|
|**--aws-s3-check-requirements**|object|Amazon Web Services S3 requirements check request.|aws_s3_check_requirements|AwsS3CheckRequirements|
|**--dynamics365-check-requirements**|object|Represents Dynamics365 requirements check request.|dynamics365_check_requirements|Dynamics365CheckRequirements|
|**--mcas-check-requirements**|object|Represents MCAS (Microsoft Cloud App Security) requirements check request.|mcas_check_requirements|MCASCheckRequirements|
|**--mdatp-check-requirements**|object|Represents MDATP (Microsoft Defender Advanced Threat Protection) requirements check request.|mdatp_check_requirements|MDATPCheckRequirements|
|**--msti-check-requirements**|object|Represents Microsoft Threat Intelligence requirements check request.|msti_check_requirements|MSTICheckRequirements|
|**--mtp-check-requirements**|object|Represents MTP (Microsoft Threat Protection) requirements check request.|mtp_check_requirements|MtpCheckRequirements|
|**--office-atp-check-requirements**|object|Represents OfficeATP (Office 365 Advanced Threat Protection) requirements check request.|office_atp_check_requirements|OfficeATPCheckRequirements|
|**--office-irm-check-requirements**|object|Represents OfficeIRM (Microsoft Insider Risk Management) requirements check request.|office_irm_check_requirements|OfficeIRMCheckRequirements|
|**--office365-project-check-requirements**|object|Represents Office365 Project requirements check request.|office365_project_check_requirements|Office365ProjectCheckRequirements|
|**--office-power-bi-check-requirements**|object|Represents Office PowerBI requirements check request.|office_power_bi_check_requirements|OfficePowerBICheckRequirements|
|**--ti-check-requirements**|object|Threat Intelligence Platforms data connector check requirements|ti_check_requirements|TICheckRequirements|
|**--ti-taxii-check-requirements**|object|Threat Intelligence TAXII data connector check requirements|ti_taxii_check_requirements|TiTaxiiCheckRequirements|
|**--io-t-check-requirements**|object|Represents IoT requirements check request.|io_t_check_requirements|IoTCheckRequirements|

### group `az sentinel domain-whois`
#### <a name="DomainWhoisGet">Command `az sentinel domain-whois show`</a>

##### <a name="ExamplesDomainWhoisGet">Example</a>
```
az sentinel domain-whois show --domain "microsoft.com" --resource-group "myRg"
```
##### <a name="ParametersDomainWhoisGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--domain**|string|Domain name to be enriched|domain|domain|

### group `az sentinel entity`
#### <a name="EntitiesList">Command `az sentinel entity list`</a>

##### <a name="ExamplesEntitiesList">Example</a>
```
az sentinel entity list --resource-group "myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersEntitiesList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|

#### <a name="EntitiesGet">Command `az sentinel entity show`</a>

##### <a name="ExamplesEntitiesGet">Example</a>
```
az sentinel entity show --entity-id "e1d3d618-e11f-478b-98e3-bb381539a8e1" --resource-group "myRg" --workspace-name \
"myWorkspace"
az sentinel entity show --entity-id "f4e74920-f2c0-4412-a45f-66d94fdf01f8" --resource-group "myRg" --workspace-name \
"myWorkspace"
az sentinel entity show --entity-id "af378b21-b4aa-4fe7-bc70-13f8621a322f" --resource-group "myRg" --workspace-name \
"myWorkspace"
az sentinel entity show --entity-id "ea359fa6-c1e5-f878-e105-6344f3e399a1" --resource-group "myRg" --workspace-name \
"myWorkspace"
az sentinel entity show --entity-id "e1d3d618-e11f-478b-98e3-bb381539a8e1" --resource-group "myRg" --workspace-name \
"myWorkspace"
az sentinel entity show --entity-id "e1d3d618-e11f-478b-98e3-bb381539a8e1" --resource-group "myRg" --workspace-name \
"myWorkspace"
az sentinel entity show --entity-id "e1d3d618-e11f-478b-98e3-bb381539a8e1" --resource-group "myRg" --workspace-name \
"myWorkspace"
az sentinel entity show --entity-id "e1d3d618-e11f-478b-98e3-bb381539a8e1" --resource-group "myRg" --workspace-name \
"myWorkspace"
az sentinel entity show --entity-id "af378b21-b4aa-4fe7-bc70-13f8621a322f" --resource-group "myRg" --workspace-name \
"myWorkspace"
az sentinel entity show --entity-id "7264685c-038c-42c6-948c-38e14ef1fb98" --resource-group "myRg" --workspace-name \
"myWorkspace"
az sentinel entity show --entity-id "e1d3d618-e11f-478b-98e3-bb381539a8e1" --resource-group "myRg" --workspace-name \
"myWorkspace"
az sentinel entity show --entity-id "dc44bd11-b348-4d76-ad29-37bf7aa41356" --resource-group "myRg" --workspace-name \
"myWorkspace"
az sentinel entity show --entity-id "4aa486e0-6f85-41af-99ea-7acdce7be6c8" --resource-group "myRg" --workspace-name \
"myWorkspace"
az sentinel entity show --entity-id "e1d3d618-e11f-478b-98e3-bb381539a8e1" --resource-group "myRg" --workspace-name \
"myWorkspace"
az sentinel entity show --entity-id "e1d3d618-e11f-478b-98e3-bb381539a8e1" --resource-group "myRg" --workspace-name \
"myWorkspace"
az sentinel entity show --entity-id "e1d3d618-e11f-478b-98e3-bb381539a8e1" --resource-group "myRg" --workspace-name \
"myWorkspace"
az sentinel entity show --entity-id "e1d3d618-e11f-478b-98e3-bb381539a8e1" --resource-group "myRg" --workspace-name \
"myWorkspace"
az sentinel entity show --entity-id "e1d3d618-e11f-478b-98e3-bb381539a8e1" --resource-group "myRg" --workspace-name \
"myWorkspace"
az sentinel entity show --entity-id "e1d3d618-e11f-478b-98e3-bb381539a8e1" --resource-group "myRg" --workspace-name \
"myWorkspace"
az sentinel entity show --entity-id "e1d3d618-e11f-478b-98e3-bb381539a8e1" --resource-group "myRg" --workspace-name \
"myWorkspace"
```
##### <a name="ParametersEntitiesGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--entity-id**|string|entity ID|entity_id|entityId|

#### <a name="EntitiesExpand">Command `az sentinel entity expand`</a>

##### <a name="ExamplesEntitiesExpand">Example</a>
```
az sentinel entity expand --entity-id "e1d3d618-e11f-478b-98e3-bb381539a8e1" --end-time "2019-05-26T00:00:00.000Z" \
--expansion-id "a77992f3-25e9-4d01-99a4-5ff606cc410a" --start-time "2019-04-25T00:00:00.000Z" --resource-group "myRg" \
--workspace-name "myWorkspace"
```
##### <a name="ParametersEntitiesExpand">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--entity-id**|string|entity ID|entity_id|entityId|
|**--end-time**|date-time|The end date filter, so the only expansion results returned are before this date.|end_time|endTime|
|**--expansion-id**|uuid|The Id of the expansion to perform.|expansion_id|expansionId|
|**--start-time**|date-time|The start date filter, so the only expansion results returned are after this date.|start_time|startTime|

#### <a name="EntitiesGetInsights">Command `az sentinel entity list-insight`</a>

##### <a name="ExamplesEntitiesGetInsights">Example</a>
```
az sentinel entity list-insight --entity-id "e1d3d618-e11f-478b-98e3-bb381539a8e1" --is-extended false --end-time \
"2021-10-01T00:00:00.000Z" --insight-query-ids "cae8d0aa-aa45-4d53-8d88-17dd64ffd4e4" --start-time \
"2021-09-01T00:00:00.000Z" --resource-group "myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersEntitiesGetInsights">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--entity-id**|string|entity ID|entity_id|entityId|
|**--start-time**|date-time|The start timeline date, so the results returned are after this date.|start_time|startTime|
|**--end-time**|date-time|The end timeline date, so the results returned are before this date.|end_time|endTime|
|**--add-default-extended-time-range**|boolean|Indicates if query time range should be extended with default time range of the query. Default value is false|add_default_extended_time_range|addDefaultExtendedTimeRange|
|**--insight-query-ids**|array|List of Insights Query Id. If empty, default value is all insights of this entity|insight_query_ids|insightQueryIds|

### group `az sentinel entity`
#### <a name="EntitiesGetTimelinelist">Command `az sentinel entity list-timeline`</a>

##### <a name="ExamplesEntitiesGetTimelinelist">Example</a>
```
az sentinel entity list-timeline --entity-id "e1d3d618-e11f-478b-98e3-bb381539a8e1" --end-time \
"2021-10-01T00:00:00.000Z" --number-of-bucket 4 --start-time "2021-09-01T00:00:00.000Z" --resource-group "myRg" \
--workspace-name "myWorkspace"
```
##### <a name="ParametersEntitiesGetTimelinelist">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--entity-id**|string|entity ID|entity_id|entityId|
|**--start-time**|date-time|The start timeline date, so the results returned are after this date.|start_time|startTime|
|**--end-time**|date-time|The end timeline date, so the results returned are before this date.|end_time|endTime|
|**--kinds**|array|Array of timeline Item kinds.|kinds|kinds|
|**--number-of-bucket**|integer|The number of bucket for timeline queries aggregation.|number_of_bucket|numberOfBucket|

### group `az sentinel entity query`
#### <a name="EntityQueriesList">Command `az sentinel entity query list`</a>

##### <a name="ExamplesEntityQueriesList">Example</a>
```
az sentinel entity query list --kind "Expansion" --resource-group "myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersEntityQueriesList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--kind**|choice|The entity query kind we want to fetch|kind|kind|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|

#### <a name="EntityQueriesGet">Command `az sentinel entity query show`</a>

##### <a name="ExamplesEntityQueriesGet">Example</a>
```
az sentinel entity query show --entity-query-id "07da3cc8-c8ad-4710-a44e-334cdcb7882b" --resource-group "myRg" \
--workspace-name "myWorkspace"
az sentinel entity query show --entity-query-id "07da3cc8-c8ad-4710-a44e-334cdcb7882b" --resource-group "myRg" \
--workspace-name "myWorkspace"
```
##### <a name="ParametersEntityQueriesGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--entity-query-id**|string|entity query ID|entity_query_id|entityQueryId|

#### <a name="EntityQueriesCreateOrUpdate#Create">Command `az sentinel entity query create`</a>

##### <a name="ExamplesEntityQueriesCreateOrUpdate#Create">Example</a>
```
az sentinel entity query create --entity-query "{\\"etag\\":\\"\\\\\\"0300bf09-0000-0000-0000-5c37296e0000\\\\\\"\\",\\\
"kind\\":\\"Activity\\",\\"properties\\":{\\"description\\":\\"Account deleted on host\\",\\"content\\":\\"On \
\'{{Computer}}\' the account \'{{TargetAccount}}\' was deleted by \'{{AddedBy}}\'\\",\\"enabled\\":true,\\"entitiesFilt\
er\\":{\\"Host_OsFamily\\":[\\"Windows\\"]},\\"inputEntityType\\":\\"Host\\",\\"queryDefinitions\\":{\\"query\\":\\"let\
 GetAccountActions = (v_Host_Name:string, v_Host_NTDomain:string, v_Host_DnsDomain:string, v_Host_AzureID:string, \
v_Host_OMSAgentID:string){\\\\nSecurityEvent\\\\n| where EventID in (4725, 4726, 4767, 4720, 4722, 4723, 4724)\\\\n// \
parsing for Host to handle variety of conventions coming from data\\\\n| extend Host_HostName = case(\\\\nComputer has \
\'@\', tostring(split(Computer, \'@\')[0]),\\\\nComputer has \'\\\\\\\\\\\\\\\\\', tostring(split(Computer, \
\'\\\\\\\\\\\\\\\\\')[1]),\\\\nComputer has \'.\', tostring(split(Computer, \'.\')[0]),\\\\nComputer\\\\n)\\\\n| \
extend Host_NTDomain = case(\\\\nComputer has \'\\\\\\\\\\\\\\\\\', tostring(split(Computer, \
\'\\\\\\\\\\\\\\\\\')[0]), \\\\nComputer has \'.\', tostring(split(Computer, \'.\')[-2]), \\\\nComputer\\\\n)\\\\n| \
extend Host_DnsDomain = case(\\\\nComputer has \'\\\\\\\\\\\\\\\\\', tostring(split(Computer, \
\'\\\\\\\\\\\\\\\\\')[0]), \\\\nComputer has \'.\', strcat_array(array_slice(split(Computer,\'.\'),-2,-1),\'.\'), \
\\\\nComputer\\\\n)\\\\n| where (Host_HostName =~ v_Host_Name and Host_NTDomain =~ v_Host_NTDomain) \\\\nor \
(Host_HostName =~ v_Host_Name and Host_DnsDomain =~ v_Host_DnsDomain) \\\\nor v_Host_AzureID =~ _ResourceId \\\\nor \
v_Host_OMSAgentID == SourceComputerId\\\\n| project TimeGenerated, EventID, Activity, Computer, TargetAccount, \
TargetUserName, TargetDomainName, TargetSid, SubjectUserName, SubjectUserSid, _ResourceId, SourceComputerId\\\\n| \
extend AddedBy = SubjectUserName\\\\n// Future support for Activities\\\\n| extend timestamp = TimeGenerated, \
HostCustomEntity = Computer, AccountCustomEntity = TargetAccount\\\\n};\\\\nGetAccountActions(\'{{Host_HostName}}\', \
\'{{Host_NTDomain}}\', \'{{Host_DnsDomain}}\', \'{{Host_AzureID}}\', \'{{Host_OMSAgentID}}\')\\\\n \\\\n| where \
EventID == 4726 \\"},\\"requiredInputFieldsSets\\":[[\\"Host_HostName\\",\\"Host_NTDomain\\"],[\\"Host_HostName\\",\\"H\
ost_DnsDomain\\"],[\\"Host_AzureID\\"],[\\"Host_OMSAgentID\\"]],\\"templateName\\":null,\\"title\\":\\"An account was \
deleted on this host\\"}}" --entity-query-id "07da3cc8-c8ad-4710-a44e-334cdcb7882b" --resource-group "myRg" \
--workspace-name "myWorkspace"
```
##### <a name="ParametersEntityQueriesCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--entity-query-id**|string|entity query ID|entity_query_id|entityQueryId|
|**--entity-query**|object|The entity query we want to create or update|entity_query|entityQuery|

#### <a name="EntityQueriesCreateOrUpdate#Update">Command `az sentinel entity query update`</a>


##### <a name="ParametersEntityQueriesCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--entity-query-id**|string|entity query ID|entity_query_id|entityQueryId|
|**--entity-query**|object|The entity query we want to create or update|entity_query|entityQuery|

#### <a name="EntityQueriesDelete">Command `az sentinel entity query delete`</a>

##### <a name="ExamplesEntityQueriesDelete">Example</a>
```
az sentinel entity query delete --entity-query-id "07da3cc8-c8ad-4710-a44e-334cdcb7882b" --resource-group "myRg" \
--workspace-name "myWorkspace"
```
##### <a name="ParametersEntityQueriesDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--entity-query-id**|string|entity query ID|entity_query_id|entityQueryId|

### group `az sentinel entity relation`
#### <a name="EntitiesRelationsList">Command `az sentinel entity relation list`</a>

##### <a name="ExamplesEntitiesRelationsList">Example</a>
```
az sentinel entity relation list --entity-id "afbd324f-6c48-459c-8710-8d1e1cd03812" --resource-group "myRg" \
--workspace-name "myWorkspace"
```
##### <a name="ParametersEntitiesRelationsList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--entity-id**|string|entity ID|entity_id|entityId|
|**--filter**|string|Filters the results, based on a Boolean condition. Optional.|filter|$filter|
|**--orderby**|string|Sorts the results. Optional.|orderby|$orderby|
|**--top**|integer|Returns only the first n results. Optional.|top|$top|
|**--skip-token**|string|Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. Optional.|skip_token|$skipToken|

### group `az sentinel entity relation`
#### <a name="EntityRelationsGetRelation">Command `az sentinel entity relation show`</a>

##### <a name="ExamplesEntityRelationsGetRelation">Example</a>
```
az sentinel entity relation show --entity-id "afbd324f-6c48-459c-8710-8d1e1cd03812" --relation-name \
"4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014" --resource-group "myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersEntityRelationsGetRelation">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--entity-id**|string|entity ID|entity_id|entityId|
|**--relation-name**|string|Relation Name|relation_name|relationName|

### group `az sentinel entity template`
#### <a name="EntityQueryTemplatesList">Command `az sentinel entity template list`</a>

##### <a name="ExamplesEntityQueryTemplatesList">Example</a>
```
az sentinel entity template list --resource-group "myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersEntityQueryTemplatesList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|

#### <a name="EntityQueryTemplatesGet">Command `az sentinel entity template show`</a>

##### <a name="ExamplesEntityQueryTemplatesGet">Example</a>
```
az sentinel entity template show --template-id "07da3cc8-c8ad-4710-a44e-334cdcb7882b" --resource-group "myRg" \
--workspace-name "myWorkspace"
```
##### <a name="ParametersEntityQueryTemplatesGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--entity-query-template-id**|string|entity query template ID|entity_query_template_id|entityQueryTemplateId|

### group `az sentinel incident`
#### <a name="IncidentsList">Command `az sentinel incident list`</a>

##### <a name="ExamplesIncidentsList">Example</a>
```
az sentinel incident list --orderby "properties/createdTimeUtc desc" --top 1 --resource-group "myRg" --workspace-name \
"myWorkspace"
```
##### <a name="ParametersIncidentsList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--filter**|string|Filters the results, based on a Boolean condition. Optional.|filter|$filter|
|**--orderby**|string|Sorts the results. Optional.|orderby|$orderby|
|**--top**|integer|Returns only the first n results. Optional.|top|$top|
|**--skip-token**|string|Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. Optional.|skip_token|$skipToken|

#### <a name="IncidentsGet">Command `az sentinel incident show`</a>

##### <a name="ExamplesIncidentsGet">Example</a>
```
az sentinel incident show --incident-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" --resource-group "myRg" \
--workspace-name "myWorkspace"
```
##### <a name="ParametersIncidentsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--incident-id**|string|Incident ID|incident_id|incidentId|

#### <a name="IncidentsCreateOrUpdate#Create">Command `az sentinel incident create`</a>

##### <a name="ExamplesIncidentsCreateOrUpdate#Create">Example</a>
```
az sentinel incident create --etag "\\"0300bf09-0000-0000-0000-5c37296e0000\\"" --description "This is a demo \
incident" --classification "FalsePositive" --classification-comment "Not a malicious activity" --classification-reason \
"IncorrectAlertLogic" --first-activity-time-utc "2019-01-01T13:00:30Z" --last-activity-time-utc "2019-01-01T13:05:30Z" \
--owner object-id="2046feea-040d-4a46-9e2b-91c2941bfa70" --severity "High" --status "Closed" --title "My incident" \
--incident-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" --resource-group "myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersIncidentsCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--incident-id**|string|Incident ID|incident_id|incidentId|
|**--etag**|string|Etag of the azure resource|etag|etag|
|**--classification**|choice|The reason the incident was closed|classification|classification|
|**--classification-comment**|string|Describes the reason the incident was closed|classification_comment|classificationComment|
|**--classification-reason**|choice|The classification reason the incident was closed with|classification_reason|classificationReason|
|**--description**|string|The description of the incident|description|description|
|**--first-activity-time-utc**|date-time|The time of the first activity in the incident|first_activity_time_utc|firstActivityTimeUtc|
|**--labels**|array|List of labels relevant to this incident|labels|labels|
|**--provider-name**|string|The name of the source provider that generated the incident|provider_name|providerName|
|**--provider-incident-id**|string|The incident ID assigned by the incident provider|provider_incident_id|providerIncidentId|
|**--last-activity-time-utc**|date-time|The time of the last activity in the incident|last_activity_time_utc|lastActivityTimeUtc|
|**--owner**|object|Describes a user that the incident is assigned to|owner|owner|
|**--severity**|choice|The severity of the incident|severity|severity|
|**--status**|choice|The status of the incident|status|status|
|**--title**|string|The title of the incident|title|title|

#### <a name="IncidentsCreateOrUpdate#Update">Command `az sentinel incident update`</a>


##### <a name="ParametersIncidentsCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--incident-id**|string|Incident ID|incident_id|incidentId|
|**--etag**|string|Etag of the azure resource|etag|etag|
|**--classification**|choice|The reason the incident was closed|classification|classification|
|**--classification-comment**|string|Describes the reason the incident was closed|classification_comment|classificationComment|
|**--classification-reason**|choice|The classification reason the incident was closed with|classification_reason|classificationReason|
|**--description**|string|The description of the incident|description|description|
|**--first-activity-time-utc**|date-time|The time of the first activity in the incident|first_activity_time_utc|firstActivityTimeUtc|
|**--labels**|array|List of labels relevant to this incident|labels|labels|
|**--provider-name**|string|The name of the source provider that generated the incident|provider_name|providerName|
|**--provider-incident-id**|string|The incident ID assigned by the incident provider|provider_incident_id|providerIncidentId|
|**--last-activity-time-utc**|date-time|The time of the last activity in the incident|last_activity_time_utc|lastActivityTimeUtc|
|**--owner**|object|Describes a user that the incident is assigned to|owner|owner|
|**--severity**|choice|The severity of the incident|severity|severity|
|**--status**|choice|The status of the incident|status|status|
|**--title**|string|The title of the incident|title|title|

#### <a name="IncidentsDelete">Command `az sentinel incident delete`</a>

##### <a name="ExamplesIncidentsDelete">Example</a>
```
az sentinel incident delete --incident-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" --resource-group "myRg" \
--workspace-name "myWorkspace"
```
##### <a name="ParametersIncidentsDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--incident-id**|string|Incident ID|incident_id|incidentId|

#### <a name="IncidentsCreateTeam">Command `az sentinel incident create-team`</a>

##### <a name="ExamplesIncidentsCreateTeam">Example</a>
```
az sentinel incident create-team --incident-id "69a30280-6a4c-4aa7-9af0-5d63f335d600" --resource-group \
"ambawolvese5resourcegroup" --team-description "Team description" --team-name "Team name" --workspace-name \
"AmbaE5WestCentralUS"
```
##### <a name="ParametersIncidentsCreateTeam">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--incident-id**|string|Incident ID|incident_id|incidentId|
|**--team-name**|string|The name of the team|team_name|teamName|
|**--team-description**|string|The description of the team|team_description|teamDescription|
|**--member-ids**|array|List of member IDs to add to the team|member_ids|memberIds|
|**--group-ids**|array|List of group IDs to add their members to the team|group_ids|groupIds|

#### <a name="IncidentsListAlerts">Command `az sentinel incident list-alert`</a>

##### <a name="ExamplesIncidentsListAlerts">Example</a>
```
az sentinel incident list-alert --incident-id "afbd324f-6c48-459c-8710-8d1e1cd03812" --resource-group "myRg" \
--workspace-name "myWorkspace"
```
##### <a name="ParametersIncidentsListAlerts">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--incident-id**|string|Incident ID|incident_id|incidentId|

#### <a name="IncidentsListBookmarks">Command `az sentinel incident list-bookmark`</a>

##### <a name="ExamplesIncidentsListBookmarks">Example</a>
```
az sentinel incident list-bookmark --incident-id "afbd324f-6c48-459c-8710-8d1e1cd03812" --resource-group "myRg" \
--workspace-name "myWorkspace"
```
##### <a name="ParametersIncidentsListBookmarks">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--incident-id**|string|Incident ID|incident_id|incidentId|

#### <a name="IncidentsListEntities">Command `az sentinel incident list-entity`</a>

##### <a name="ExamplesIncidentsListEntities">Example</a>
```
az sentinel incident list-entity --incident-id "afbd324f-6c48-459c-8710-8d1e1cd03812" --resource-group "myRg" \
--workspace-name "myWorkspace"
```
##### <a name="ParametersIncidentsListEntities">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--incident-id**|string|Incident ID|incident_id|incidentId|

#### <a name="IncidentsRunPlaybook">Command `az sentinel incident run-playbook`</a>

##### <a name="ExamplesIncidentsRunPlaybook">Example</a>
```
az sentinel incident run-playbook --incident-identifier "73e01a99-5cd7-4139-a149-9f2736ff2ar4" \
--logic-apps-resource-id "/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.L\
ogic/workflows/my-playbook-name" --tenant-id "qwere6b2-9ac0-4464-9919-dccaee2e4ddd" --resource-group "myRg" \
--workspace-name "myWorkspace"
```
##### <a name="ParametersIncidentsRunPlaybook">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--incident-identifier**|string||incident_identifier|incidentIdentifier|
|**--tenant-id**|uuid||tenant_id|tenantId|
|**--logic-apps-resource-id**|string||logic_apps_resource_id|logicAppsResourceId|

### group `az sentinel incident comment`
#### <a name="IncidentCommentsList">Command `az sentinel incident comment list`</a>

##### <a name="ExamplesIncidentCommentsList">Example</a>
```
az sentinel incident comment list --incident-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" --resource-group "myRg" \
--workspace-name "myWorkspace"
```
##### <a name="ParametersIncidentCommentsList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--incident-id**|string|Incident ID|incident_id|incidentId|
|**--filter**|string|Filters the results, based on a Boolean condition. Optional.|filter|$filter|
|**--orderby**|string|Sorts the results. Optional.|orderby|$orderby|
|**--top**|integer|Returns only the first n results. Optional.|top|$top|
|**--skip-token**|string|Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. Optional.|skip_token|$skipToken|

#### <a name="IncidentCommentsGet">Command `az sentinel incident comment show`</a>

##### <a name="ExamplesIncidentCommentsGet">Example</a>
```
az sentinel incident comment show --incident-comment-id "4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014" --incident-id \
"73e01a99-5cd7-4139-a149-9f2736ff2ab5" --resource-group "myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersIncidentCommentsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--incident-id**|string|Incident ID|incident_id|incidentId|
|**--incident-comment-id**|string|Incident comment ID|incident_comment_id|incidentCommentId|

#### <a name="IncidentCommentsCreateOrUpdate#Create">Command `az sentinel incident comment create`</a>

##### <a name="ExamplesIncidentCommentsCreateOrUpdate#Create">Example</a>
```
az sentinel incident comment create --message "Some message" --incident-comment-id "4bb36b7b-26ff-4d1c-9cbe-0d8ab3da001\
4" --incident-id "73e01a99-5cd7-4139-a149-9f2736ff2ab5" --resource-group "myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersIncidentCommentsCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--incident-id**|string|Incident ID|incident_id|incidentId|
|**--incident-comment-id**|string|Incident comment ID|incident_comment_id|incidentCommentId|
|**--etag**|string|Etag of the azure resource|etag|etag|
|**--message**|string|The comment message|message|message|

#### <a name="IncidentCommentsCreateOrUpdate#Update">Command `az sentinel incident comment update`</a>


##### <a name="ParametersIncidentCommentsCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--incident-id**|string|Incident ID|incident_id|incidentId|
|**--incident-comment-id**|string|Incident comment ID|incident_comment_id|incidentCommentId|
|**--etag**|string|Etag of the azure resource|etag|etag|
|**--message**|string|The comment message|message|message|

#### <a name="IncidentCommentsDelete">Command `az sentinel incident comment delete`</a>

##### <a name="ExamplesIncidentCommentsDelete">Example</a>
```
az sentinel incident comment delete --incident-comment-id "4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014" --incident-id \
"73e01a99-5cd7-4139-a149-9f2736ff2ab5" --resource-group "myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersIncidentCommentsDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--incident-id**|string|Incident ID|incident_id|incidentId|
|**--incident-comment-id**|string|Incident comment ID|incident_comment_id|incidentCommentId|

### group `az sentinel incident relation`
#### <a name="IncidentRelationsList">Command `az sentinel incident relation list`</a>

##### <a name="ExamplesIncidentRelationsList">Example</a>
```
az sentinel incident relation list --incident-id "afbd324f-6c48-459c-8710-8d1e1cd03812" --resource-group "myRg" \
--workspace-name "myWorkspace"
```
##### <a name="ParametersIncidentRelationsList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--incident-id**|string|Incident ID|incident_id|incidentId|
|**--filter**|string|Filters the results, based on a Boolean condition. Optional.|filter|$filter|
|**--orderby**|string|Sorts the results. Optional.|orderby|$orderby|
|**--top**|integer|Returns only the first n results. Optional.|top|$top|
|**--skip-token**|string|Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. Optional.|skip_token|$skipToken|

#### <a name="IncidentRelationsGet">Command `az sentinel incident relation show`</a>

##### <a name="ExamplesIncidentRelationsGet">Example</a>
```
az sentinel incident relation show --incident-id "afbd324f-6c48-459c-8710-8d1e1cd03812" --relation-name \
"4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014" --resource-group "myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersIncidentRelationsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--incident-id**|string|Incident ID|incident_id|incidentId|
|**--relation-name**|string|Relation Name|relation_name|relationName|

#### <a name="IncidentRelationsCreateOrUpdate#Create">Command `az sentinel incident relation create`</a>

##### <a name="ExamplesIncidentRelationsCreateOrUpdate#Create">Example</a>
```
az sentinel incident relation create --incident-id "afbd324f-6c48-459c-8710-8d1e1cd03812" --related-resource-id \
"/subscriptions/d0cfe6b2-9ac0-4464-9919-dccaee2e48c0/resourceGroups/myRg/providers/Microsoft.OperationalIinsights/works\
paces/myWorkspace/providers/Microsoft.SecurityInsights/bookmarks/2216d0e1-91e3-4902-89fd-d2df8c535096" --relation-name \
"4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014" --resource-group "myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersIncidentRelationsCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--incident-id**|string|Incident ID|incident_id|incidentId|
|**--relation-name**|string|Relation Name|relation_name|relationName|
|**--etag**|string|Etag of the azure resource|etag|etag|
|**--related-resource-id**|string|The resource ID of the related resource|related_resource_id|relatedResourceId|

#### <a name="IncidentRelationsCreateOrUpdate#Update">Command `az sentinel incident relation update`</a>


##### <a name="ParametersIncidentRelationsCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--incident-id**|string|Incident ID|incident_id|incidentId|
|**--relation-name**|string|Relation Name|relation_name|relationName|
|**--etag**|string|Etag of the azure resource|etag|etag|
|**--related-resource-id**|string|The resource ID of the related resource|related_resource_id|relatedResourceId|

#### <a name="IncidentRelationsDelete">Command `az sentinel incident relation delete`</a>

##### <a name="ExamplesIncidentRelationsDelete">Example</a>
```
az sentinel incident relation delete --incident-id "afbd324f-6c48-459c-8710-8d1e1cd03812" --relation-name \
"4bb36b7b-26ff-4d1c-9cbe-0d8ab3da0014" --resource-group "myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersIncidentRelationsDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--incident-id**|string|Incident ID|incident_id|incidentId|
|**--relation-name**|string|Relation Name|relation_name|relationName|

### group `az sentinel ip-geodata`
#### <a name="IPGeodataGet">Command `az sentinel ip-geodata show`</a>

##### <a name="ExamplesIPGeodataGet">Example</a>
```
az sentinel ip-geodata show --ip-address "1.2.3.4" --resource-group "myRg"
```
##### <a name="ParametersIPGeodataGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--ip-address**|string|IP address (v4 or v6) to be enriched|ip_address|ipAddress|

### group `az sentinel metadata`
#### <a name="MetadataList">Command `az sentinel metadata list`</a>

##### <a name="ExamplesMetadataList">Example</a>
```
az sentinel metadata list --resource-group "myRg" --workspace-name "myWorkspace"
az sentinel metadata list --resource-group "myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersMetadataList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--filter**|string|Filters the results, based on a Boolean condition. Optional.|filter|$filter|
|**--orderby**|string|Sorts the results. Optional.|orderby|$orderby|
|**--top**|integer|Returns only the first n results. Optional.|top|$top|
|**--skip**|integer|Used to skip n elements in the OData query (offset). Returns a nextLink to the next page of results if there are any left.|skip|$skip|

#### <a name="MetadataGet">Command `az sentinel metadata show`</a>

##### <a name="ExamplesMetadataGet">Example</a>
```
az sentinel metadata show --name "metadataName" --resource-group "myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersMetadataGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--metadata-name**|string|The Metadata name.|metadata_name|metadataName|

#### <a name="MetadataCreate">Command `az sentinel metadata create`</a>

##### <a name="ExamplesMetadataCreate">Example</a>
```
az sentinel metadata create --author name="User Name" email="email@microsoft.com" --categories domains="Application" \
domains="Security – Insider Threat" verticals="Healthcare" --content-id "c00ee137-7475-47c8-9cce-ec6f0f1bedd0" \
--content-schema-version "2.0" --custom-version "1.0" --dependencies "{\\"criteria\\":[{\\"criteria\\":[{\\"name\\":\\"\
Microsoft Defender for Endpoint\\",\\"contentId\\":\\"045d06d0-ee72-4794-aba4-cf5646e4c756\\",\\"kind\\":\\"DataConnect\
or\\"},{\\"contentId\\":\\"dbfcb2cc-d782-40ef-8d94-fe7af58a6f2d\\",\\"kind\\":\\"DataConnector\\"},{\\"contentId\\":\\"\
de4dca9b-eb37-47d6-a56f-b8b06b261593\\",\\"kind\\":\\"DataConnector\\",\\"version\\":\\"2.0\\"}],\\"operator\\":\\"OR\\\
"},{\\"contentId\\":\\"31ee11cc-9989-4de8-b176-5e0ef5c4dbab\\",\\"kind\\":\\"Playbook\\",\\"version\\":\\"1.0\\"},{\\"c\
ontentId\\":\\"21ba424a-9438-4444-953a-7059539a7a1b\\",\\"kind\\":\\"Parser\\"}],\\"operator\\":\\"AND\\"}" \
--first-publish-date "2021-05-18" --kind "AnalyticsRule" --last-publish-date "2021-05-18" --parent-id \
"/subscriptions/2e1dc338-d04d-4443-b721-037eff4fdcac/resourceGroups/myRg/providers/Microsoft.OperationalInsights/worksp\
aces/myWorkspace/providers/Microsoft.SecurityInsights/alertRules/ruleName" --preview-images "firstImage.png" \
"secondImage.jpeg" --preview-images-dark "firstImageDark.png" "secondImageDark.jpeg" --providers "Amazon" "Microsoft" \
--source name="Contoso Solution 1.0" kind="Solution" source-id="b688a130-76f4-4a07-bf57-762222a3cadf" --support \
name="Microsoft" email="support@microsoft.com" link="https://support.microsoft.com/" tier="Partner" --tactics \
"reconnaissance" "commandandcontrol" --techniques "T1548" "T1548.001" --version "1.0.0.0" --name "metadataName" \
--resource-group "myRg" --workspace-name "myWorkspace"
az sentinel metadata create --content-id "c00ee137-7475-47c8-9cce-ec6f0f1bedd0" --kind "AnalyticsRule" --parent-id \
"/subscriptions/2e1dc338-d04d-4443-b721-037eff4fdcac/resourceGroups/myRg/providers/Microsoft.OperationalInsights/worksp\
aces/myWorkspace/providers/Microsoft.SecurityInsights/alertRules/ruleName" --name "metadataName" --resource-group \
"myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersMetadataCreate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--metadata-name**|string|The Metadata name.|metadata_name|metadataName|
|**--etag**|string|Etag of the azure resource|etag|etag|
|**--content-id**|string|Static ID for the content.  Used to identify dependencies and content from solutions or community.  Hard-coded/static for out of the box content and solutions. Dynamic for user-created.  This is the resource name|content_id|contentId|
|**--parent-id**|string|Full parent resource ID of the content item the metadata is for.  This is the full resource ID including the scope (subscription and resource group)|parent_id|parentId|
|**--version**|string|Version of the content.  Default and recommended format is numeric (e.g. 1, 1.0, 1.0.0, 1.0.0.0), following ARM template best practices.  Can also be any string, but then we cannot guarantee any version checks|version|version|
|**--kind**|choice|The kind of content the metadata is for.|kind|kind|
|**--source**|object|Source of the content.  This is where/how it was created.|source|source|
|**--author**|object|The creator of the content item.|author|author|
|**--support**|object|Support information for the metadata - type, name, contact information|support|support|
|**--dependencies**|object|Dependencies for the content item, what other content items it requires to work.  Can describe more complex dependencies using a recursive/nested structure. For a single dependency an id/kind/version can be supplied or operator/criteria for complex formats.|dependencies|dependencies|
|**--categories**|object|Categories for the solution content item|categories|categories|
|**--providers**|array|Providers for the solution content item|providers|providers|
|**--first-publish-date**|date|first publish date solution content item|first_publish_date|firstPublishDate|
|**--last-publish-date**|date|last publish date for the solution content item|last_publish_date|lastPublishDate|
|**--custom-version**|string|The custom version of the content. A optional free text|custom_version|customVersion|
|**--content-schema-version**|string|Schema version of the content. Can be used to distinguish between different flow based on the schema version|content_schema_version|contentSchemaVersion|
|**--icon**|string|the icon identifier. this id can later be fetched from the solution template|icon|icon|
|**--threat-analysis-tactics**|array|the tactics the resource covers|threat_analysis_tactics|threatAnalysisTactics|
|**--threat-analysis-techniques**|array|the techniques the resource covers, these have to be aligned with the tactics being used|threat_analysis_techniques|threatAnalysisTechniques|
|**--preview-images**|array|preview image file names. These will be taken from the solution artifacts|preview_images|previewImages|
|**--preview-images-dark**|array|preview image file names. These will be taken from the solution artifacts. used for dark theme support|preview_images_dark|previewImagesDark|

#### <a name="MetadataUpdate">Command `az sentinel metadata update`</a>

##### <a name="ExamplesMetadataUpdate">Example</a>
```
az sentinel metadata update --name "metadataName" --author name="User Name" email="email@microsoft.com" \
--resource-group "myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersMetadataUpdate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--metadata-name**|string|The Metadata name.|metadata_name|metadataName|
|**--etag**|string|Etag of the azure resource|etag|etag|
|**--content-id**|string|Static ID for the content.  Used to identify dependencies and content from solutions or community.  Hard-coded/static for out of the box content and solutions. Dynamic for user-created.  This is the resource name|content_id|contentId|
|**--parent-id**|string|Full parent resource ID of the content item the metadata is for.  This is the full resource ID including the scope (subscription and resource group)|parent_id|parentId|
|**--version**|string|Version of the content.  Default and recommended format is numeric (e.g. 1, 1.0, 1.0.0, 1.0.0.0), following ARM template best practices.  Can also be any string, but then we cannot guarantee any version checks|version|version|
|**--kind**|choice|The kind of content the metadata is for.|kind|kind|
|**--source**|object|Source of the content.  This is where/how it was created.|source|source|
|**--author**|object|The creator of the content item.|author|author|
|**--support**|object|Support information for the metadata - type, name, contact information|support|support|
|**--dependencies**|object|Dependencies for the content item, what other content items it requires to work.  Can describe more complex dependencies using a recursive/nested structure. For a single dependency an id/kind/version can be supplied or operator/criteria for complex formats.|dependencies|dependencies|
|**--categories**|object|Categories for the solution content item|categories|categories|
|**--providers**|array|Providers for the solution content item|providers|providers|
|**--first-publish-date**|date|first publish date solution content item|first_publish_date|firstPublishDate|
|**--last-publish-date**|date|last publish date for the solution content item|last_publish_date|lastPublishDate|
|**--custom-version**|string|The custom version of the content. A optional free text|custom_version|customVersion|
|**--content-schema-version**|string|Schema version of the content. Can be used to distinguish between different flow based on the schema version|content_schema_version|contentSchemaVersion|
|**--icon**|string|the icon identifier. this id can later be fetched from the solution template|icon|icon|
|**--threat-analysis-tactics**|array|the tactics the resource covers|threat_analysis_tactics|threatAnalysisTactics|
|**--threat-analysis-techniques**|array|the techniques the resource covers, these have to be aligned with the tactics being used|threat_analysis_techniques|threatAnalysisTechniques|
|**--preview-images**|array|preview image file names. These will be taken from the solution artifacts|preview_images|previewImages|
|**--preview-images-dark**|array|preview image file names. These will be taken from the solution artifacts. used for dark theme support|preview_images_dark|previewImagesDark|

#### <a name="MetadataDelete">Command `az sentinel metadata delete`</a>

##### <a name="ExamplesMetadataDelete">Example</a>
```
az sentinel metadata delete --name "metadataName" --resource-group "myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersMetadataDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--metadata-name**|string|The Metadata name.|metadata_name|metadataName|

### group `az sentinel office-consent`
#### <a name="OfficeConsentsList">Command `az sentinel office-consent list`</a>

##### <a name="ExamplesOfficeConsentsList">Example</a>
```
az sentinel office-consent list --resource-group "myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersOfficeConsentsList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|

#### <a name="OfficeConsentsGet">Command `az sentinel office-consent show`</a>

##### <a name="ExamplesOfficeConsentsGet">Example</a>
```
az sentinel office-consent show --consent-id "04e5fd05-ff86-4b97-b8d2-1c20933cb46c" --resource-group "myRg" \
--workspace-name "myWorkspace"
```
##### <a name="ParametersOfficeConsentsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--consent-id**|string|consent ID|consent_id|consentId|

#### <a name="OfficeConsentsDelete">Command `az sentinel office-consent delete`</a>

##### <a name="ExamplesOfficeConsentsDelete">Example</a>
```
az sentinel office-consent delete --consent-id "04e5fd05-ff86-4b97-b8d2-1c20933cb46c" --resource-group "myRg" \
--workspace-name "myWorkspace"
```
##### <a name="ParametersOfficeConsentsDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--consent-id**|string|consent ID|consent_id|consentId|

### group `az sentinel onboarding-state`
#### <a name="SentinelOnboardingStatesList">Command `az sentinel onboarding-state list`</a>

##### <a name="ExamplesSentinelOnboardingStatesList">Example</a>
```
az sentinel onboarding-state list --resource-group "myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersSentinelOnboardingStatesList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|

#### <a name="SentinelOnboardingStatesGet">Command `az sentinel onboarding-state show`</a>

##### <a name="ExamplesSentinelOnboardingStatesGet">Example</a>
```
az sentinel onboarding-state show --resource-group "myRg" --name "default" --workspace-name "myWorkspace"
```
##### <a name="ParametersSentinelOnboardingStatesGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--sentinel-onboarding-state-name**|string|The Sentinel onboarding state name. Supports - default|sentinel_onboarding_state_name|sentinelOnboardingStateName|

#### <a name="SentinelOnboardingStatesCreate">Command `az sentinel onboarding-state create`</a>

##### <a name="ExamplesSentinelOnboardingStatesCreate">Example</a>
```
az sentinel onboarding-state create --resource-group "myRg" --name "default" --customer-managed-key false \
--workspace-name "myWorkspace"
```
##### <a name="ParametersSentinelOnboardingStatesCreate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--sentinel-onboarding-state-name**|string|The Sentinel onboarding state name. Supports - default|sentinel_onboarding_state_name|sentinelOnboardingStateName|
|**--etag**|string|Etag of the azure resource|etag|etag|
|**--customer-managed-key**|boolean|Flag that indicates the status of the CMK setting|customer_managed_key|customerManagedKey|

#### <a name="SentinelOnboardingStatesDelete">Command `az sentinel onboarding-state delete`</a>

##### <a name="ExamplesSentinelOnboardingStatesDelete">Example</a>
```
az sentinel onboarding-state delete --resource-group "myRg" --name "default" --workspace-name "myWorkspace"
```
##### <a name="ParametersSentinelOnboardingStatesDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--sentinel-onboarding-state-name**|string|The Sentinel onboarding state name. Supports - default|sentinel_onboarding_state_name|sentinelOnboardingStateName|

### group `az sentinel product-setting`
#### <a name="ProductSettingsList">Command `az sentinel product-setting list`</a>

##### <a name="ExamplesProductSettingsList">Example</a>
```
az sentinel product-setting list --resource-group "myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersProductSettingsList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|

#### <a name="ProductSettingsGet">Command `az sentinel product-setting show`</a>

##### <a name="ExamplesProductSettingsGet">Example</a>
```
az sentinel product-setting show --resource-group "myRg" --settings-name "EyesOn" --workspace-name "myWorkspace"
```
##### <a name="ParametersProductSettingsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--settings-name**|string|The setting name. Supports - Anomalies, EyesOn, EntityAnalytics, Ueba|settings_name|settingsName|

#### <a name="ProductSettingsUpdate">Command `az sentinel product-setting update`</a>


##### <a name="ParametersProductSettingsUpdate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--settings-name**|string|The setting name. Supports - Anomalies, EyesOn, EntityAnalytics, Ueba|settings_name|settingsName|
|**--anomalies**|object|Settings with single toggle.|anomalies|Anomalies|
|**--eyes-on**|object|Settings with single toggle.|eyes_on|EyesOn|
|**--entity-analytics**|object|Settings with single toggle.|entity_analytics|EntityAnalytics|
|**--ueba**|object|Settings with single toggle.|ueba|Ueba|

#### <a name="ProductSettingsDelete">Command `az sentinel product-setting delete`</a>

##### <a name="ExamplesProductSettingsDelete">Example</a>
```
az sentinel product-setting delete --resource-group "myRg" --settings-name "EyesOn" --workspace-name "myWorkspace"
```
##### <a name="ParametersProductSettingsDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--settings-name**|string|The setting name. Supports - Anomalies, EyesOn, EntityAnalytics, Ueba|settings_name|settingsName|

### group `az sentinel source-control`
#### <a name="SourceControllistRepositories">Command `az sentinel source-control list-repository`</a>

##### <a name="ExamplesSourceControllistRepositories">Example</a>
```
az sentinel source-control list-repository --repo-type "Github" --resource-group "myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersSourceControllistRepositories">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--repo-type**|choice|The repo type.|repo_type|repoType|

### group `az sentinel source-control`
#### <a name="SourceControlsList">Command `az sentinel source-control list`</a>

##### <a name="ExamplesSourceControlsList">Example</a>
```
az sentinel source-control list --resource-group "myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersSourceControlsList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|

#### <a name="SourceControlsGet">Command `az sentinel source-control show`</a>

##### <a name="ExamplesSourceControlsGet">Example</a>
```
az sentinel source-control show --resource-group "myRg" --source-control-id "789e0c1f-4a3d-43ad-809c-e713b677b04a" \
--workspace-name "myWorkspace"
```
##### <a name="ParametersSourceControlsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--source-control-id**|string|Source control Id|source_control_id|sourceControlId|

#### <a name="SourceControlsCreate">Command `az sentinel source-control create`</a>

##### <a name="ExamplesSourceControlsCreate">Example</a>
```
az sentinel source-control create --resource-group "myRg" --etag "\\"0300bf09-0000-0000-0000-5c37296e0000\\"" \
--description "This is a source control" --content-types "AnalyticRules" "Workbook" --display-name "My Source Control" \
--repo-type "Github" --branch "master" --display-url "https://github.com/user/repo" --path-mapping \
path="path/to/rules" content-type="AnalyticRules" --path-mapping path="path/to/workbooks" content-type="Workbook" \
--url "https://github.com/user/repo" --source-control-id "789e0c1f-4a3d-43ad-809c-e713b677b04a" --workspace-name \
"myWorkspace"
```
##### <a name="ParametersSourceControlsCreate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--source-control-id**|string|Source control Id|source_control_id|sourceControlId|
|**--etag**|string|Etag of the azure resource|etag|etag|
|**--id-properties-id**|string|The id (a Guid) of the source control|id_properties_id|id|
|**--version**|choice|The version number associated with the source control|version|version|
|**--display-name**|string|The display name of the source control|display_name|displayName|
|**--description**|string|A description of the source control|description|description|
|**--repo-type**|choice|The repository type of the source control|repo_type|repoType|
|**--content-types**|array|Array of source control content types.|content_types|contentTypes|
|**--deployment-fetch-status**|choice|Status while fetching the last deployment.|deployment_fetch_status|deploymentFetchStatus|
|**--deployment**|object|Deployment information.|deployment|deployment|
|**--message**|string|Additional details about the deployment that can be shown to the user.|message|message|
|**--webhook**|object|The webhook object created for the source-control.|webhook|webhook|
|**--azure-dev-ops-resource-info**|object|Resources created in Azure DevOps for this source-control.|azure_dev_ops_resource_info|azureDevOpsResourceInfo|
|**--app-installation-id**|string|GitHub application installation id.|app_installation_id|appInstallationId|
|**--url**|string|Url of repository.|url|url|
|**--branch**|string|Branch name of repository.|branch|branch|
|**--display-url**|string|Display url of repository.|display_url|displayUrl|
|**--deployment-logs-url**|string|Url to access repository action logs.|deployment_logs_url|deploymentLogsUrl|
|**--path-mapping**|array|Dictionary of source control content type and path mapping.|path_mapping|pathMapping|

#### <a name="SourceControlsDelete">Command `az sentinel source-control delete`</a>

##### <a name="ExamplesSourceControlsDelete">Example</a>
```
az sentinel source-control delete --resource-group "myRg" --source-control-id "789e0c1f-4a3d-43ad-809c-e713b677b04a" \
--workspace-name "myWorkspace"
```
##### <a name="ParametersSourceControlsDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--source-control-id**|string|Source control Id|source_control_id|sourceControlId|

### group `az sentinel threat-indicator`
#### <a name="ThreatIntelligenceIndicatorGet">Command `az sentinel threat-indicator show`</a>

##### <a name="ExamplesThreatIntelligenceIndicatorGet">Example</a>
```
az sentinel threat-indicator show --name "e16ef847-962e-d7b6-9c8b-a33e4bd30e47" --resource-group "myRg" \
--workspace-name "myWorkspace"
```
##### <a name="ParametersThreatIntelligenceIndicatorGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--name**|string|Threat intelligence indicator name field.|name|name|

#### <a name="ThreatIntelligenceIndicatorCreateIndicator">Command `az sentinel threat-indicator create`</a>

##### <a name="ExamplesThreatIntelligenceIndicatorCreateIndicator">Example</a>
```
az sentinel threat-indicator create --description "debugging indicators" --confidence 78 --created-by-ref \
"contoso@contoso.com" --display-name "new schema" --external-references "[]" --modified "" --pattern "[url:value = \
\'https://www.contoso.com\']" --pattern-type "url" --revoked false --source "Azure Sentinel" \
--threat-intelligence-tags "new schema" --threat-types "compromised" --valid-from "2021-09-15T17:44:00.114052Z" \
--valid-until "" --resource-group "myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersThreatIntelligenceIndicatorCreateIndicator">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--etag**|string|Etag of the azure resource|etag|etag|
|**--threat-intelligence-tags**|array|List of tags|threat_intelligence_tags|threatIntelligenceTags|
|**--last-updated-time-utc**|string|Last updated time in UTC|last_updated_time_utc|lastUpdatedTimeUtc|
|**--source**|string|Source of a threat intelligence entity|source|source|
|**--display-name**|string|Display name of a threat intelligence entity|display_name|displayName|
|**--description**|string|Description of a threat intelligence entity|description|description|
|**--indicator-types**|array|Indicator types of threat intelligence entities|indicator_types|indicatorTypes|
|**--pattern**|string|Pattern of a threat intelligence entity|pattern|pattern|
|**--pattern-type**|string|Pattern type of a threat intelligence entity|pattern_type|patternType|
|**--pattern-version**|string|Pattern version of a threat intelligence entity|pattern_version|patternVersion|
|**--kill-chain-phases**|array|Kill chain phases|kill_chain_phases|killChainPhases|
|**--parsed-pattern**|array|Parsed patterns|parsed_pattern|parsedPattern|
|**--external-id**|string|External ID of threat intelligence entity|external_id|externalId|
|**--created-by-ref**|string|Created by reference of threat intelligence entity|created_by_ref|createdByRef|
|**--defanged**|boolean|Is threat intelligence entity defanged|defanged|defanged|
|**--external-last-updated-time-utc**|string|External last updated time in UTC|external_last_updated_time_utc|externalLastUpdatedTimeUtc|
|**--external-references**|array|External References|external_references|externalReferences|
|**--granular-markings**|array|Granular Markings|granular_markings|granularMarkings|
|**--labels**|array|Labels  of threat intelligence entity|labels|labels|
|**--revoked**|boolean|Is threat intelligence entity revoked|revoked|revoked|
|**--confidence**|integer|Confidence of threat intelligence entity|confidence|confidence|
|**--object-marking-refs**|array|Threat intelligence entity object marking references|object_marking_refs|objectMarkingRefs|
|**--language**|string|Language of threat intelligence entity|language|language|
|**--threat-types**|array|Threat types|threat_types|threatTypes|
|**--valid-from**|string|Valid from|valid_from|validFrom|
|**--valid-until**|string|Valid until|valid_until|validUntil|
|**--created**|string|Created by|created|created|
|**--modified**|string|Modified by|modified|modified|
|**--extensions**|dictionary|Extensions map|extensions|extensions|

#### <a name="ThreatIntelligenceIndicatorCreate">Command `az sentinel threat-indicator update`</a>

##### <a name="ExamplesThreatIntelligenceIndicatorCreate">Example</a>
```
az sentinel threat-indicator update --name "d9cd6f0b-96b9-3984-17cd-a779d1e15a93" --description "debugging indicators" \
--confidence 78 --created-by-ref "contoso@contoso.com" --display-name "new schema" --external-references "[]" \
--modified "" --pattern "[url:value = \'https://www.contoso.com\']" --pattern-type "url" --revoked false --source \
"Azure Sentinel" --threat-intelligence-tags "new schema" --threat-types "compromised" --valid-from \
"2020-04-15T17:44:00.114052Z" --valid-until "" --resource-group "myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersThreatIntelligenceIndicatorCreate">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--name**|string|Threat intelligence indicator name field.|name|name|
|**--etag**|string|Etag of the azure resource|etag|etag|
|**--threat-intelligence-tags**|array|List of tags|threat_intelligence_tags|threatIntelligenceTags|
|**--last-updated-time-utc**|string|Last updated time in UTC|last_updated_time_utc|lastUpdatedTimeUtc|
|**--source**|string|Source of a threat intelligence entity|source|source|
|**--display-name**|string|Display name of a threat intelligence entity|display_name|displayName|
|**--description**|string|Description of a threat intelligence entity|description|description|
|**--indicator-types**|array|Indicator types of threat intelligence entities|indicator_types|indicatorTypes|
|**--pattern**|string|Pattern of a threat intelligence entity|pattern|pattern|
|**--pattern-type**|string|Pattern type of a threat intelligence entity|pattern_type|patternType|
|**--pattern-version**|string|Pattern version of a threat intelligence entity|pattern_version|patternVersion|
|**--kill-chain-phases**|array|Kill chain phases|kill_chain_phases|killChainPhases|
|**--parsed-pattern**|array|Parsed patterns|parsed_pattern|parsedPattern|
|**--external-id**|string|External ID of threat intelligence entity|external_id|externalId|
|**--created-by-ref**|string|Created by reference of threat intelligence entity|created_by_ref|createdByRef|
|**--defanged**|boolean|Is threat intelligence entity defanged|defanged|defanged|
|**--external-last-updated-time-utc**|string|External last updated time in UTC|external_last_updated_time_utc|externalLastUpdatedTimeUtc|
|**--external-references**|array|External References|external_references|externalReferences|
|**--granular-markings**|array|Granular Markings|granular_markings|granularMarkings|
|**--labels**|array|Labels  of threat intelligence entity|labels|labels|
|**--revoked**|boolean|Is threat intelligence entity revoked|revoked|revoked|
|**--confidence**|integer|Confidence of threat intelligence entity|confidence|confidence|
|**--object-marking-refs**|array|Threat intelligence entity object marking references|object_marking_refs|objectMarkingRefs|
|**--language**|string|Language of threat intelligence entity|language|language|
|**--threat-types**|array|Threat types|threat_types|threatTypes|
|**--valid-from**|string|Valid from|valid_from|validFrom|
|**--valid-until**|string|Valid until|valid_until|validUntil|
|**--created**|string|Created by|created|created|
|**--modified**|string|Modified by|modified|modified|
|**--extensions**|dictionary|Extensions map|extensions|extensions|

#### <a name="ThreatIntelligenceIndicatorDelete">Command `az sentinel threat-indicator delete`</a>

##### <a name="ExamplesThreatIntelligenceIndicatorDelete">Example</a>
```
az sentinel threat-indicator delete --name "d9cd6f0b-96b9-3984-17cd-a779d1e15a93" --resource-group "myRg" \
--workspace-name "myWorkspace"
```
##### <a name="ParametersThreatIntelligenceIndicatorDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--name**|string|Threat intelligence indicator name field.|name|name|

#### <a name="ThreatIntelligenceIndicatorAppendTags">Command `az sentinel threat-indicator append-tag`</a>

##### <a name="ExamplesThreatIntelligenceIndicatorAppendTags">Example</a>
```
az sentinel threat-indicator append-tag --name "d9cd6f0b-96b9-3984-17cd-a779d1e15a93" --threat-intelligence-tags \
"tag1" "tag2" --resource-group "myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersThreatIntelligenceIndicatorAppendTags">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--name**|string|Threat intelligence indicator name field.|name|name|
|**--threat-intelligence-tags**|array|List of tags to be appended.|threat_intelligence_tags|threatIntelligenceTags|

#### <a name="ThreatIntelligenceIndicatorQueryIndicators">Command `az sentinel threat-indicator query`</a>

##### <a name="ExamplesThreatIntelligenceIndicatorQueryIndicators">Example</a>
```
az sentinel threat-indicator query --max-confidence 80 --max-valid-until "2021-04-25T17:44:00.114052Z" \
--min-confidence 25 --min-valid-until "2021-04-05T17:44:00.114052Z" --page-size 100 --sort-by \
item-key="lastUpdatedTimeUtc" sort-order="descending" --sources "Azure Sentinel" --resource-group "myRg" \
--workspace-name "myWorkspace"
```
##### <a name="ParametersThreatIntelligenceIndicatorQueryIndicators">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--page-size**|integer|Page size|page_size|pageSize|
|**--min-confidence**|integer|Minimum confidence.|min_confidence|minConfidence|
|**--max-confidence**|integer|Maximum confidence.|max_confidence|maxConfidence|
|**--min-valid-until**|string|Start time for ValidUntil filter.|min_valid_until|minValidUntil|
|**--max-valid-until**|string|End time for ValidUntil filter.|max_valid_until|maxValidUntil|
|**--include-disabled**|boolean|Parameter to include/exclude disabled indicators.|include_disabled|includeDisabled|
|**--sort-by**|array|Columns to sort by and sorting order|sort_by|sortBy|
|**--sources**|array|Sources of threat intelligence indicators|sources|sources|
|**--pattern-types**|array|Pattern types|pattern_types|patternTypes|
|**--threat-types**|array|Threat types of threat intelligence indicators|threat_types|threatTypes|
|**--ids**|array|Ids of threat intelligence indicators|ids|ids|
|**--keywords**|array|Keywords for searching threat intelligence indicators|keywords|keywords|
|**--skip-token**|string|Skip token.|skip_token|skipToken|

#### <a name="ThreatIntelligenceIndicatorReplaceTags">Command `az sentinel threat-indicator replace-tag`</a>

##### <a name="ExamplesThreatIntelligenceIndicatorReplaceTags">Example</a>
```
az sentinel threat-indicator replace-tag --name "d9cd6f0b-96b9-3984-17cd-a779d1e15a93" --etag \
"\\"0000262c-0000-0800-0000-5e9767060000\\"" --threat-intelligence-tags "patching tags" --resource-group "myRg" \
--workspace-name "myWorkspace"
```
##### <a name="ParametersThreatIntelligenceIndicatorReplaceTags">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--name**|string|Threat intelligence indicator name field.|name|name|
|**--etag**|string|Etag of the azure resource|etag|etag|
|**--threat-intelligence-tags**|array|List of tags|threat_intelligence_tags|threatIntelligenceTags|
|**--last-updated-time-utc**|string|Last updated time in UTC|last_updated_time_utc|lastUpdatedTimeUtc|
|**--source**|string|Source of a threat intelligence entity|source|source|
|**--display-name**|string|Display name of a threat intelligence entity|display_name|displayName|
|**--description**|string|Description of a threat intelligence entity|description|description|
|**--indicator-types**|array|Indicator types of threat intelligence entities|indicator_types|indicatorTypes|
|**--pattern**|string|Pattern of a threat intelligence entity|pattern|pattern|
|**--pattern-type**|string|Pattern type of a threat intelligence entity|pattern_type|patternType|
|**--pattern-version**|string|Pattern version of a threat intelligence entity|pattern_version|patternVersion|
|**--kill-chain-phases**|array|Kill chain phases|kill_chain_phases|killChainPhases|
|**--parsed-pattern**|array|Parsed patterns|parsed_pattern|parsedPattern|
|**--external-id**|string|External ID of threat intelligence entity|external_id|externalId|
|**--created-by-ref**|string|Created by reference of threat intelligence entity|created_by_ref|createdByRef|
|**--defanged**|boolean|Is threat intelligence entity defanged|defanged|defanged|
|**--external-last-updated-time-utc**|string|External last updated time in UTC|external_last_updated_time_utc|externalLastUpdatedTimeUtc|
|**--external-references**|array|External References|external_references|externalReferences|
|**--granular-markings**|array|Granular Markings|granular_markings|granularMarkings|
|**--labels**|array|Labels  of threat intelligence entity|labels|labels|
|**--revoked**|boolean|Is threat intelligence entity revoked|revoked|revoked|
|**--confidence**|integer|Confidence of threat intelligence entity|confidence|confidence|
|**--object-marking-refs**|array|Threat intelligence entity object marking references|object_marking_refs|objectMarkingRefs|
|**--language**|string|Language of threat intelligence entity|language|language|
|**--threat-types**|array|Threat types|threat_types|threatTypes|
|**--valid-from**|string|Valid from|valid_from|validFrom|
|**--valid-until**|string|Valid until|valid_until|validUntil|
|**--created**|string|Created by|created|created|
|**--modified**|string|Modified by|modified|modified|
|**--extensions**|dictionary|Extensions map|extensions|extensions|

### group `az sentinel threat-indicator`
#### <a name="ThreatIntelligenceIndicatorsList">Command `az sentinel threat-indicator list`</a>

##### <a name="ExamplesThreatIntelligenceIndicatorsList">Example</a>
```
az sentinel threat-indicator list --resource-group "myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersThreatIntelligenceIndicatorsList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--filter**|string|Filters the results, based on a Boolean condition. Optional.|filter|$filter|
|**--orderby**|string|Sorts the results. Optional.|orderby|$orderby|
|**--top**|integer|Returns only the first n results. Optional.|top|$top|
|**--skip-token**|string|Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. Optional.|skip_token|$skipToken|

### group `az sentinel threat-indicator metric`
#### <a name="ThreatIntelligenceIndicatorMetricsList">Command `az sentinel threat-indicator metric list`</a>

##### <a name="ExamplesThreatIntelligenceIndicatorMetricsList">Example</a>
```
az sentinel threat-indicator metric list --resource-group "myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersThreatIntelligenceIndicatorMetricsList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|

### group `az sentinel watchlist`
#### <a name="WatchlistsList">Command `az sentinel watchlist list`</a>

##### <a name="ExamplesWatchlistsList">Example</a>
```
az sentinel watchlist list --resource-group "myRg" --workspace-name "myWorkspace"
```
##### <a name="ParametersWatchlistsList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--skip-token**|string|Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. Optional.|skip_token|$skipToken|

#### <a name="WatchlistsGet">Command `az sentinel watchlist show`</a>

##### <a name="ExamplesWatchlistsGet">Example</a>
```
az sentinel watchlist show --resource-group "myRg" --watchlist-alias "highValueAsset" --workspace-name "myWorkspace"
```
##### <a name="ParametersWatchlistsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--watchlist-alias**|string|Watchlist Alias|watchlist_alias|watchlistAlias|

#### <a name="WatchlistsCreateOrUpdate#Create">Command `az sentinel watchlist create`</a>

##### <a name="ExamplesWatchlistsCreateOrUpdate#Create">Example</a>
```
az sentinel watchlist create --resource-group "myRg" --etag "\\"0300bf09-0000-0000-0000-5c37296e0000\\"" --description \
"Watchlist from CSV content" --content-type "text/csv" --display-name "High Value Assets Watchlist" --items-search-key \
"header1" --skip-num 1 --provider "Microsoft" --raw-content "This line will be skipped\\nheader1,header2\\nvalue1,value\
2" --source "watchlist.csv" --source-type "Local file" --watchlist-alias "highValueAsset" --workspace-name \
"myWorkspace"
az sentinel watchlist create --resource-group "myRg" --etag "\\"0300bf09-0000-0000-0000-5c37296e0000\\"" --description \
"Watchlist from CSV content" --display-name "High Value Assets Watchlist" --items-search-key "header1" --provider \
"Microsoft" --source "watchlist.csv" --source-type "Local file" --watchlist-alias "highValueAsset" --workspace-name \
"myWorkspace"
```
##### <a name="ParametersWatchlistsCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--watchlist-alias**|string|Watchlist Alias|watchlist_alias|watchlistAlias|
|**--etag**|string|Etag of the azure resource|etag|etag|
|**--watchlist-id**|string|The id (a Guid) of the watchlist|watchlist_id|watchlistId|
|**--display-name**|string|The display name of the watchlist|display_name|displayName|
|**--provider**|string|The provider of the watchlist|provider|provider|
|**--source**|string|The filename of the watchlist, called 'source'|source|source|
|**--source-type**|choice|The sourceType of the watchlist|source_type|sourceType|
|**--created**|date-time|The time the watchlist was created|created|created|
|**--updated**|date-time|The last time the watchlist was updated|updated|updated|
|**--description**|string|A description of the watchlist|description|description|
|**--watchlist-type**|string|The type of the watchlist|watchlist_type|watchlistType|
|**--watchlist-properties-watchlist-alias**|string|The alias of the watchlist|watchlist_properties_watchlist_alias|watchlistAlias|
|**--is-deleted**|boolean|A flag that indicates if the watchlist is deleted or not|is_deleted|isDeleted|
|**--labels**|array|List of labels relevant to this watchlist|labels|labels|
|**--default-duration**|duration|The default duration of a watchlist (in ISO 8601 duration format)|default_duration|defaultDuration|
|**--tenant-id**|string|The tenantId where the watchlist belongs to|tenant_id|tenantId|
|**--number-of-lines-to-skip**|integer|The number of lines in a csv/tsv content to skip before the header|number_of_lines_to_skip|numberOfLinesToSkip|
|**--raw-content**|string|The raw content that represents to watchlist items to create. In case of csv/tsv content type, it's the content of the file that will parsed by the endpoint|raw_content|rawContent|
|**--items-search-key**|string|The search key is used to optimize query performance when using watchlists for joins with other data. For example, enable a column with IP addresses to be the designated SearchKey field, then use this field as the key field when joining to other event data by IP address.|items_search_key|itemsSearchKey|
|**--content-type**|string|The content type of the raw content. Example : text/csv or text/tsv |content_type|contentType|
|**--upload-status**|string|The status of the Watchlist upload : New, InProgress or Complete. Pls note : When a Watchlist upload status is equal to InProgress, the Watchlist cannot be deleted|upload_status|uploadStatus|
|**--object-id**|uuid|The object id of the user.|object_id|objectId|
|**--user-info-object-id**|uuid|The object id of the user.|user_info_object_id|objectId|

#### <a name="WatchlistsCreateOrUpdate#Update">Command `az sentinel watchlist update`</a>


##### <a name="ParametersWatchlistsCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--watchlist-alias**|string|Watchlist Alias|watchlist_alias|watchlistAlias|
|**--etag**|string|Etag of the azure resource|etag|etag|
|**--watchlist-id**|string|The id (a Guid) of the watchlist|watchlist_id|watchlistId|
|**--display-name**|string|The display name of the watchlist|display_name|displayName|
|**--provider**|string|The provider of the watchlist|provider|provider|
|**--source**|string|The filename of the watchlist, called 'source'|source|source|
|**--source-type**|choice|The sourceType of the watchlist|source_type|sourceType|
|**--created**|date-time|The time the watchlist was created|created|created|
|**--updated**|date-time|The last time the watchlist was updated|updated|updated|
|**--description**|string|A description of the watchlist|description|description|
|**--watchlist-type**|string|The type of the watchlist|watchlist_type|watchlistType|
|**--watchlist-properties-watchlist-alias**|string|The alias of the watchlist|watchlist_properties_watchlist_alias|watchlistAlias|
|**--is-deleted**|boolean|A flag that indicates if the watchlist is deleted or not|is_deleted|isDeleted|
|**--labels**|array|List of labels relevant to this watchlist|labels|labels|
|**--default-duration**|duration|The default duration of a watchlist (in ISO 8601 duration format)|default_duration|defaultDuration|
|**--tenant-id**|string|The tenantId where the watchlist belongs to|tenant_id|tenantId|
|**--number-of-lines-to-skip**|integer|The number of lines in a csv/tsv content to skip before the header|number_of_lines_to_skip|numberOfLinesToSkip|
|**--raw-content**|string|The raw content that represents to watchlist items to create. In case of csv/tsv content type, it's the content of the file that will parsed by the endpoint|raw_content|rawContent|
|**--items-search-key**|string|The search key is used to optimize query performance when using watchlists for joins with other data. For example, enable a column with IP addresses to be the designated SearchKey field, then use this field as the key field when joining to other event data by IP address.|items_search_key|itemsSearchKey|
|**--content-type**|string|The content type of the raw content. Example : text/csv or text/tsv |content_type|contentType|
|**--upload-status**|string|The status of the Watchlist upload : New, InProgress or Complete. Pls note : When a Watchlist upload status is equal to InProgress, the Watchlist cannot be deleted|upload_status|uploadStatus|
|**--object-id**|uuid|The object id of the user.|object_id|objectId|
|**--user-info-object-id**|uuid|The object id of the user.|user_info_object_id|objectId|

#### <a name="WatchlistsDelete">Command `az sentinel watchlist delete`</a>

##### <a name="ExamplesWatchlistsDelete">Example</a>
```
az sentinel watchlist delete --resource-group "myRg" --watchlist-alias "highValueAsset" --workspace-name "myWorkspace"
```
##### <a name="ParametersWatchlistsDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--watchlist-alias**|string|Watchlist Alias|watchlist_alias|watchlistAlias|

### group `az sentinel watchlist item`
#### <a name="WatchlistItemsList">Command `az sentinel watchlist item list`</a>

##### <a name="ExamplesWatchlistItemsList">Example</a>
```
az sentinel watchlist item list --resource-group "myRg" --watchlist-alias "highValueAsset" --workspace-name \
"myWorkspace"
```
##### <a name="ParametersWatchlistItemsList">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--skip-token**|string|Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. Optional.|skip_token|$skipToken|
|**--watchlist-alias**|string|Watchlist Alias|watchlist_alias|watchlistAlias|

#### <a name="WatchlistItemsGet">Command `az sentinel watchlist item show`</a>

##### <a name="ExamplesWatchlistItemsGet">Example</a>
```
az sentinel watchlist item show --resource-group "myRg" --watchlist-alias "highValueAsset" --watchlist-item-id \
"3f8901fe-63d9-4875-9ad5-9fb3b8105797" --workspace-name "myWorkspace"
```
##### <a name="ParametersWatchlistItemsGet">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--watchlist-alias**|string|Watchlist Alias|watchlist_alias|watchlistAlias|
|**--watchlist-item-id**|string|Watchlist Item Id (GUID)|watchlist_item_id|watchlistItemId|

#### <a name="WatchlistItemsCreateOrUpdate#Create">Command `az sentinel watchlist item create`</a>

##### <a name="ExamplesWatchlistItemsCreateOrUpdate#Create">Example</a>
```
az sentinel watchlist item create --resource-group "myRg" --watchlist-alias "highValueAsset" --etag \
"0300bf09-0000-0000-0000-5c37296e0000" --items-key-value "{\\"Business tier\\":\\"10.0.2.0/24\\",\\"Data \
tier\\":\\"10.0.2.0/24\\",\\"Gateway subnet\\":\\"10.0.255.224/27\\",\\"Private DMZ in\\":\\"10.0.0.0/27\\",\\"Public \
DMZ out\\":\\"10.0.0.96/27\\",\\"Web Tier\\":\\"10.0.1.0/24\\"}" --watchlist-item-id "82ba292c-dc97-4dfc-969d-d4dd9e666\
842" --workspace-name "myWorkspace"
```
##### <a name="ParametersWatchlistItemsCreateOrUpdate#Create">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--watchlist-alias**|string|Watchlist Alias|watchlist_alias|watchlistAlias|
|**--watchlist-item-id**|string|Watchlist Item Id (GUID)|watchlist_item_id|watchlistItemId|
|**--etag**|string|Etag of the azure resource|etag|etag|
|**--watchlist-item-type**|string|The type of the watchlist item|watchlist_item_type|watchlistItemType|
|**--watchlist-item-properties-watchlist-item-id-watchlist-item-id**|string|The id (a Guid) of the watchlist item|watchlist_item_properties_watchlist_item_id_watchlist_item_id|watchlistItemId|
|**--tenant-id**|string|The tenantId to which the watchlist item belongs to|tenant_id|tenantId|
|**--is-deleted**|boolean|A flag that indicates if the watchlist item is deleted or not|is_deleted|isDeleted|
|**--created**|date-time|The time the watchlist item was created|created|created|
|**--updated**|date-time|The last time the watchlist item was updated|updated|updated|
|**--items-key-value**|dictionary|key-value pairs for a watchlist item|items_key_value|itemsKeyValue|
|**--entity-mapping**|dictionary|key-value pairs for a watchlist item entity mapping|entity_mapping|entityMapping|
|**--object-id**|uuid|The object id of the user.|object_id|objectId|
|**--user-info-object-id**|uuid|The object id of the user.|user_info_object_id|objectId|

#### <a name="WatchlistItemsCreateOrUpdate#Update">Command `az sentinel watchlist item update`</a>


##### <a name="ParametersWatchlistItemsCreateOrUpdate#Update">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--watchlist-alias**|string|Watchlist Alias|watchlist_alias|watchlistAlias|
|**--watchlist-item-id**|string|Watchlist Item Id (GUID)|watchlist_item_id|watchlistItemId|
|**--etag**|string|Etag of the azure resource|etag|etag|
|**--watchlist-item-type**|string|The type of the watchlist item|watchlist_item_type|watchlistItemType|
|**--watchlist-item-properties-watchlist-item-id-watchlist-item-id**|string|The id (a Guid) of the watchlist item|watchlist_item_properties_watchlist_item_id_watchlist_item_id|watchlistItemId|
|**--tenant-id**|string|The tenantId to which the watchlist item belongs to|tenant_id|tenantId|
|**--is-deleted**|boolean|A flag that indicates if the watchlist item is deleted or not|is_deleted|isDeleted|
|**--created**|date-time|The time the watchlist item was created|created|created|
|**--updated**|date-time|The last time the watchlist item was updated|updated|updated|
|**--items-key-value**|dictionary|key-value pairs for a watchlist item|items_key_value|itemsKeyValue|
|**--entity-mapping**|dictionary|key-value pairs for a watchlist item entity mapping|entity_mapping|entityMapping|
|**--object-id**|uuid|The object id of the user.|object_id|objectId|
|**--user-info-object-id**|uuid|The object id of the user.|user_info_object_id|objectId|

#### <a name="WatchlistItemsDelete">Command `az sentinel watchlist item delete`</a>

##### <a name="ExamplesWatchlistItemsDelete">Example</a>
```
az sentinel watchlist item delete --resource-group "myRg" --watchlist-alias "highValueAsset" --watchlist-item-id \
"4008512e-1d30-48b2-9ee2-d3612ed9d3ea" --workspace-name "myWorkspace"
```
##### <a name="ParametersWatchlistItemsDelete">Parameters</a> 
|Option|Type|Description|Path (SDK)|Swagger name|
|------|----|-----------|----------|------------|
|**--resource-group-name**|string|The name of the resource group. The name is case insensitive.|resource_group_name|resourceGroupName|
|**--workspace-name**|string|The name of the workspace.|workspace_name|workspaceName|
|**--watchlist-alias**|string|Watchlist Alias|watchlist_alias|watchlistAlias|
|**--watchlist-item-id**|string|Watchlist Item Id (GUID)|watchlist_item_id|watchlistItemId|
