# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


class Update(AAZCommand):
    """Update an environment in the specified subscription and resource group.
    """

    _aaz_info = {
        "version": "2020-05-15",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.timeseriesinsights/environments/{}", "2020-05-15"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.environment_name = AAZStrArg(
            options=["-n", "--name", "--environment-name"],
            help="The name of the Time Series Insights environment associated with the specified resource group.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Parameters"

        _args_schema = cls._args_schema
        _args_schema.gen1 = AAZObjectArg(
            options=["--gen1"],
            arg_group="Parameters",
        )
        _args_schema.gen2 = AAZObjectArg(
            options=["--gen2"],
            arg_group="Parameters",
        )
        _args_schema.sku = AAZObjectArg(
            options=["--sku"],
            arg_group="Parameters",
            help="The sku determines the type of environment, either Gen1 (S1 or S2) or Gen2 (L1). For Gen1 environments the sku determines the capacity of the environment, the ingress rate, and the billing rate.",
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Parameters",
            help="Key-value pairs of additional properties for the resource.",
            nullable=True,
        )

        gen1 = cls._args_schema.gen1
        gen1.data_retention_time = AAZDurationArg(
            options=["data-retention-time"],
            help="ISO8601 timespan specifying the minimum number of days the environment's events will be available for query.",
        )
        gen1.partition_key_properties = AAZListArg(
            options=["key-properties", "partition-key-properties"],
            help="The list of event properties which will be used to partition data in the environment. Currently, only a single partition key property is supported.",
            nullable=True,
        )
        gen1.storage_limit_exceeded_behavior = AAZStrArg(
            options=["exceeded-behavior", "storage-limit-exceeded-behavior"],
            help="The behavior the Time Series Insights service should take when the environment's capacity has been exceeded. If \"PauseIngress\" is specified, new events will not be read from the event source. If \"PurgeOldData\" is specified, new events will continue to be read and old events will be deleted from the environment. The default behavior is PurgeOldData.",
            nullable=True,
            enum={"PauseIngress": "PauseIngress", "PurgeOldData": "PurgeOldData"},
        )

        partition_key_properties = cls._args_schema.gen1.partition_key_properties
        partition_key_properties.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.gen1.partition_key_properties.Element
        _element.name = AAZStrArg(
            options=["name"],
            nullable=True,
        )
        _element.type = AAZStrArg(
            options=["type"],
            nullable=True,
            enum={"String": "String"},
        )

        gen2 = cls._args_schema.gen2
        gen2.storage_configuration = AAZObjectArg(
            options=["storage-configuration"],
            help="The storage configuration provides the connection details that allows the Time Series Insights service to connect to the customer storage account that is used to store the environment's data.",
        )
        gen2.time_series_id_properties = AAZListArg(
            options=["id-properties", "time-series-id-properties"],
            help="The list of event properties which will be used to define the environment's time series id.",
        )
        gen2.warm_store_configuration = AAZObjectArg(
            options=["warm-store-config", "warm-store-configuration"],
            help="The warm store configuration provides the details to create a warm store cache that will retain a copy of the environment's data available for faster query.",
            nullable=True,
        )

        storage_configuration = cls._args_schema.gen2.storage_configuration
        storage_configuration.account_name = AAZStrArg(
            options=["account-name"],
            help="The name of the storage account that will hold the environment's Gen2 data.",
        )
        storage_configuration.management_key = AAZStrArg(
            options=["management-key"],
            help="The value of the management key that grants the Time Series Insights service write access to the storage account. This property is not shown in environment responses.",
        )

        time_series_id_properties = cls._args_schema.gen2.time_series_id_properties
        time_series_id_properties.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.gen2.time_series_id_properties.Element
        _element.name = AAZStrArg(
            options=["name"],
            nullable=True,
        )
        _element.type = AAZStrArg(
            options=["type"],
            nullable=True,
            enum={"String": "String"},
        )

        warm_store_configuration = cls._args_schema.gen2.warm_store_configuration
        warm_store_configuration.data_retention = AAZDurationArg(
            options=["data-retention"],
            help="ISO8601 timespan specifying the number of days the environment's events will be available for query from the warm store.",
        )

        sku = cls._args_schema.sku
        sku.capacity = AAZIntArg(
            options=["capacity"],
            help="The capacity of the sku. For Gen1 environments, this value can be changed to support scale out of environments after they have been created.",
            fmt=AAZIntArgFormat(
                maximum=10,
                minimum=1,
            ),
        )
        sku.name = AAZStrArg(
            options=["name"],
            help="The name of this SKU.",
            enum={"L1": "L1", "P1": "P1", "S1": "S1", "S2": "S2"},
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg(
            nullable=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.EnvironmentsGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.EnvironmentsCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class EnvironmentsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "environmentName", self.ctx.args.environment_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2020-05-15",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _UpdateHelper._build_schema_environment_resource_read(cls._schema_on_200)

            return cls._schema_on_200

    class EnvironmentsCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.TimeSeriesInsights/environments/{environmentName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "environmentName", self.ctx.args.environment_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2020-05-15",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_environment_resource_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("sku", AAZObjectType, ".sku", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")
            _builder.discriminate_by("kind", "Gen1")
            _builder.discriminate_by("kind", "Gen2")

            sku = _builder.get(".sku")
            if sku is not None:
                sku.set_prop("capacity", AAZIntType, ".capacity", typ_kwargs={"flags": {"required": True}})
                sku.set_prop("name", AAZStrType, ".name", typ_kwargs={"flags": {"required": True}})

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            disc_gen1 = _builder.get("{kind:Gen1}")
            if disc_gen1 is not None:
                disc_gen1.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True, "client_flatten": True}})

            properties = _builder.get("{kind:Gen1}.properties")
            if properties is not None:
                properties.set_prop("dataRetentionTime", AAZStrType, ".gen1.data_retention_time", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("partitionKeyProperties", AAZListType, ".gen1.partition_key_properties")
                properties.set_prop("storageLimitExceededBehavior", AAZStrType, ".gen1.storage_limit_exceeded_behavior")

            partition_key_properties = _builder.get("{kind:Gen1}.properties.partitionKeyProperties")
            if partition_key_properties is not None:
                partition_key_properties.set_elements(AAZObjectType, ".")

            _elements = _builder.get("{kind:Gen1}.properties.partitionKeyProperties[]")
            if _elements is not None:
                _elements.set_prop("name", AAZStrType, ".name")
                _elements.set_prop("type", AAZStrType, ".type")

            disc_gen2 = _builder.get("{kind:Gen2}")
            if disc_gen2 is not None:
                disc_gen2.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True, "client_flatten": True}})

            properties = _builder.get("{kind:Gen2}.properties")
            if properties is not None:
                properties.set_prop("storageConfiguration", AAZObjectType, ".gen2.storage_configuration", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("timeSeriesIdProperties", AAZListType, ".gen2.time_series_id_properties", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("warmStoreConfiguration", AAZObjectType, ".gen2.warm_store_configuration")

            storage_configuration = _builder.get("{kind:Gen2}.properties.storageConfiguration")
            if storage_configuration is not None:
                storage_configuration.set_prop("accountName", AAZStrType, ".account_name", typ_kwargs={"flags": {"required": True}})
                storage_configuration.set_prop("managementKey", AAZStrType, ".management_key", typ_kwargs={"flags": {"required": True}})

            time_series_id_properties = _builder.get("{kind:Gen2}.properties.timeSeriesIdProperties")
            if time_series_id_properties is not None:
                time_series_id_properties.set_elements(AAZObjectType, ".")

            _elements = _builder.get("{kind:Gen2}.properties.timeSeriesIdProperties[]")
            if _elements is not None:
                _elements.set_prop("name", AAZStrType, ".name")
                _elements.set_prop("type", AAZStrType, ".type")

            warm_store_configuration = _builder.get("{kind:Gen2}.properties.warmStoreConfiguration")
            if warm_store_configuration is not None:
                warm_store_configuration.set_prop("dataRetention", AAZStrType, ".data_retention", typ_kwargs={"flags": {"required": True}})

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_environment_resource_read = None

    @classmethod
    def _build_schema_environment_resource_read(cls, _schema):
        if cls._schema_environment_resource_read is not None:
            _schema.id = cls._schema_environment_resource_read.id
            _schema.kind = cls._schema_environment_resource_read.kind
            _schema.location = cls._schema_environment_resource_read.location
            _schema.name = cls._schema_environment_resource_read.name
            _schema.sku = cls._schema_environment_resource_read.sku
            _schema.tags = cls._schema_environment_resource_read.tags
            _schema.type = cls._schema_environment_resource_read.type
            _schema.discriminate_by(
                "kind",
                "Gen1",
                cls._schema_environment_resource_read.discriminate_by(
                    "kind",
                    "Gen1",
                )
            )
            _schema.discriminate_by(
                "kind",
                "Gen2",
                cls._schema_environment_resource_read.discriminate_by(
                    "kind",
                    "Gen2",
                )
            )
            return

        cls._schema_environment_resource_read = _schema_environment_resource_read = AAZObjectType()

        environment_resource_read = _schema_environment_resource_read
        environment_resource_read.id = AAZStrType(
            flags={"read_only": True},
        )
        environment_resource_read.kind = AAZStrType(
            flags={"required": True},
        )
        environment_resource_read.location = AAZStrType(
            flags={"required": True},
        )
        environment_resource_read.name = AAZStrType(
            flags={"read_only": True},
        )
        environment_resource_read.sku = AAZObjectType(
            flags={"required": True},
        )
        environment_resource_read.tags = AAZDictType()
        environment_resource_read.type = AAZStrType(
            flags={"read_only": True},
        )

        sku = _schema_environment_resource_read.sku
        sku.capacity = AAZIntType(
            flags={"required": True},
        )
        sku.name = AAZStrType(
            flags={"required": True},
        )

        tags = _schema_environment_resource_read.tags
        tags.Element = AAZStrType()

        disc_gen1 = _schema_environment_resource_read.discriminate_by("kind", "Gen1")
        disc_gen1.properties = AAZObjectType(
            flags={"required": True, "client_flatten": True},
        )

        properties = _schema_environment_resource_read.discriminate_by("kind", "Gen1").properties
        properties.creation_time = AAZStrType(
            serialized_name="creationTime",
            flags={"read_only": True},
        )
        properties.data_access_fqdn = AAZStrType(
            serialized_name="dataAccessFqdn",
            flags={"read_only": True},
        )
        properties.data_access_id = AAZStrType(
            serialized_name="dataAccessId",
            flags={"read_only": True},
        )
        properties.data_retention_time = AAZStrType(
            serialized_name="dataRetentionTime",
            flags={"required": True},
        )
        properties.partition_key_properties = AAZListType(
            serialized_name="partitionKeyProperties",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.status = AAZObjectType(
            flags={"read_only": True},
        )
        cls._build_schema_environment_status_read(properties.status)
        properties.storage_limit_exceeded_behavior = AAZStrType(
            serialized_name="storageLimitExceededBehavior",
        )

        partition_key_properties = _schema_environment_resource_read.discriminate_by("kind", "Gen1").properties.partition_key_properties
        partition_key_properties.Element = AAZObjectType()
        cls._build_schema_time_series_id_property_read(partition_key_properties.Element)

        disc_gen2 = _schema_environment_resource_read.discriminate_by("kind", "Gen2")
        disc_gen2.properties = AAZObjectType(
            flags={"required": True, "client_flatten": True},
        )

        properties = _schema_environment_resource_read.discriminate_by("kind", "Gen2").properties
        properties.creation_time = AAZStrType(
            serialized_name="creationTime",
            flags={"read_only": True},
        )
        properties.data_access_fqdn = AAZStrType(
            serialized_name="dataAccessFqdn",
            flags={"read_only": True},
        )
        properties.data_access_id = AAZStrType(
            serialized_name="dataAccessId",
            flags={"read_only": True},
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.status = AAZObjectType(
            flags={"read_only": True},
        )
        cls._build_schema_environment_status_read(properties.status)
        properties.storage_configuration = AAZObjectType(
            serialized_name="storageConfiguration",
            flags={"required": True},
        )
        properties.time_series_id_properties = AAZListType(
            serialized_name="timeSeriesIdProperties",
            flags={"required": True},
        )
        properties.warm_store_configuration = AAZObjectType(
            serialized_name="warmStoreConfiguration",
        )

        storage_configuration = _schema_environment_resource_read.discriminate_by("kind", "Gen2").properties.storage_configuration
        storage_configuration.account_name = AAZStrType(
            serialized_name="accountName",
            flags={"required": True},
        )

        time_series_id_properties = _schema_environment_resource_read.discriminate_by("kind", "Gen2").properties.time_series_id_properties
        time_series_id_properties.Element = AAZObjectType()
        cls._build_schema_time_series_id_property_read(time_series_id_properties.Element)

        warm_store_configuration = _schema_environment_resource_read.discriminate_by("kind", "Gen2").properties.warm_store_configuration
        warm_store_configuration.data_retention = AAZStrType(
            serialized_name="dataRetention",
            flags={"required": True},
        )

        _schema.id = cls._schema_environment_resource_read.id
        _schema.kind = cls._schema_environment_resource_read.kind
        _schema.location = cls._schema_environment_resource_read.location
        _schema.name = cls._schema_environment_resource_read.name
        _schema.sku = cls._schema_environment_resource_read.sku
        _schema.tags = cls._schema_environment_resource_read.tags
        _schema.type = cls._schema_environment_resource_read.type
        _schema.discriminate_by(
                "kind",
                "Gen1",
                cls._schema_environment_resource_read.discriminate_by(
                    "kind",
                    "Gen1",
                )
            )
        _schema.discriminate_by(
                "kind",
                "Gen2",
                cls._schema_environment_resource_read.discriminate_by(
                    "kind",
                    "Gen2",
                )
            )

    _schema_environment_status_read = None

    @classmethod
    def _build_schema_environment_status_read(cls, _schema):
        if cls._schema_environment_status_read is not None:
            _schema.ingress = cls._schema_environment_status_read.ingress
            _schema.warm_storage = cls._schema_environment_status_read.warm_storage
            return

        cls._schema_environment_status_read = _schema_environment_status_read = AAZObjectType(
            flags={"read_only": True}
        )

        environment_status_read = _schema_environment_status_read
        environment_status_read.ingress = AAZObjectType(
            flags={"read_only": True},
        )
        environment_status_read.warm_storage = AAZObjectType(
            serialized_name="warmStorage",
            flags={"read_only": True},
        )

        ingress = _schema_environment_status_read.ingress
        ingress.state = AAZStrType()
        ingress.state_details = AAZObjectType(
            serialized_name="stateDetails",
            flags={"read_only": True},
        )

        state_details = _schema_environment_status_read.ingress.state_details
        state_details.code = AAZStrType()
        state_details.message = AAZStrType()

        warm_storage = _schema_environment_status_read.warm_storage
        warm_storage.properties_usage = AAZObjectType(
            serialized_name="propertiesUsage",
            flags={"client_flatten": True, "read_only": True},
        )

        properties_usage = _schema_environment_status_read.warm_storage.properties_usage
        properties_usage.state = AAZStrType()
        properties_usage.state_details = AAZObjectType(
            serialized_name="stateDetails",
            flags={"client_flatten": True, "read_only": True},
        )

        state_details = _schema_environment_status_read.warm_storage.properties_usage.state_details
        state_details.current_count = AAZIntType(
            serialized_name="currentCount",
        )
        state_details.max_count = AAZIntType(
            serialized_name="maxCount",
        )

        _schema.ingress = cls._schema_environment_status_read.ingress
        _schema.warm_storage = cls._schema_environment_status_read.warm_storage

    _schema_time_series_id_property_read = None

    @classmethod
    def _build_schema_time_series_id_property_read(cls, _schema):
        if cls._schema_time_series_id_property_read is not None:
            _schema.name = cls._schema_time_series_id_property_read.name
            _schema.type = cls._schema_time_series_id_property_read.type
            return

        cls._schema_time_series_id_property_read = _schema_time_series_id_property_read = AAZObjectType()

        time_series_id_property_read = _schema_time_series_id_property_read
        time_series_id_property_read.name = AAZStrType()
        time_series_id_property_read.type = AAZStrType()

        _schema.name = cls._schema_time_series_id_property_read.name
        _schema.type = cls._schema_time_series_id_property_read.type


__all__ = ["Update"]