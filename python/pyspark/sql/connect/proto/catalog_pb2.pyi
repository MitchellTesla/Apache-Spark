#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file

Licensed to the Apache Software Foundation (ASF) under one or more
contributor license agreements.  See the NOTICE file distributed with
this work for additional information regarding copyright ownership.
The ASF licenses this file to You under the Apache License, Version 2.0
(the "License"); you may not use this file except in compliance with
the License.  You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import pyspark.sql.connect.proto.types_pb2
import sys
import typing

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Catalog(google.protobuf.message.Message):
    """Catalog messages are marked as unstable."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CURRENT_DATABASE_FIELD_NUMBER: builtins.int
    SET_CURRENT_DATABASE_FIELD_NUMBER: builtins.int
    LIST_DATABASES_FIELD_NUMBER: builtins.int
    LIST_TABLES_FIELD_NUMBER: builtins.int
    LIST_FUNCTIONS_FIELD_NUMBER: builtins.int
    LIST_COLUMNS_FIELD_NUMBER: builtins.int
    GET_DATABASE_FIELD_NUMBER: builtins.int
    GET_TABLE_FIELD_NUMBER: builtins.int
    GET_FUNCTION_FIELD_NUMBER: builtins.int
    DATABASE_EXISTS_FIELD_NUMBER: builtins.int
    TABLE_EXISTS_FIELD_NUMBER: builtins.int
    FUNCTION_EXISTS_FIELD_NUMBER: builtins.int
    CREATE_EXTERNAL_TABLE_FIELD_NUMBER: builtins.int
    CREATE_TABLE_FIELD_NUMBER: builtins.int
    DROP_TEMP_VIEW_FIELD_NUMBER: builtins.int
    DROP_GLOBAL_TEMP_VIEW_FIELD_NUMBER: builtins.int
    RECOVER_PARTITIONS_FIELD_NUMBER: builtins.int
    CLEAR_CACHE_FIELD_NUMBER: builtins.int
    REFRESH_TABLE_FIELD_NUMBER: builtins.int
    REFRESH_BY_PATH_FIELD_NUMBER: builtins.int
    CURRENT_CATALOG_FIELD_NUMBER: builtins.int
    SET_CURRENT_CATALOG_FIELD_NUMBER: builtins.int
    LIST_CATALOGS_FIELD_NUMBER: builtins.int
    @property
    def current_database(self) -> global___CurrentDatabase: ...
    @property
    def set_current_database(self) -> global___SetCurrentDatabase: ...
    @property
    def list_databases(self) -> global___ListDatabases: ...
    @property
    def list_tables(self) -> global___ListTables: ...
    @property
    def list_functions(self) -> global___ListFunctions: ...
    @property
    def list_columns(self) -> global___ListColumns: ...
    @property
    def get_database(self) -> global___GetDatabase: ...
    @property
    def get_table(self) -> global___GetTable: ...
    @property
    def get_function(self) -> global___GetFunction: ...
    @property
    def database_exists(self) -> global___DatabaseExists: ...
    @property
    def table_exists(self) -> global___TableExists: ...
    @property
    def function_exists(self) -> global___FunctionExists: ...
    @property
    def create_external_table(self) -> global___CreateExternalTable: ...
    @property
    def create_table(self) -> global___CreateTable: ...
    @property
    def drop_temp_view(self) -> global___DropTempView: ...
    @property
    def drop_global_temp_view(self) -> global___DropGlobalTempView: ...
    @property
    def recover_partitions(self) -> global___RecoverPartitions: ...
    @property
    def clear_cache(self) -> global___ClearCache:
        """TODO(SPARK-41612): Support Catalog.isCached
        IsCached is_cached = 18;
        TODO(SPARK-41600): Support Catalog.cacheTable
        CacheTable cache_table = 19;
        TODO(SPARK-41623): Support Catalog.uncacheTable
        UncacheTable uncache_table = 20;
        """
    @property
    def refresh_table(self) -> global___RefreshTable: ...
    @property
    def refresh_by_path(self) -> global___RefreshByPath: ...
    @property
    def current_catalog(self) -> global___CurrentCatalog: ...
    @property
    def set_current_catalog(self) -> global___SetCurrentCatalog: ...
    @property
    def list_catalogs(self) -> global___ListCatalogs: ...
    def __init__(
        self,
        *,
        current_database: global___CurrentDatabase | None = ...,
        set_current_database: global___SetCurrentDatabase | None = ...,
        list_databases: global___ListDatabases | None = ...,
        list_tables: global___ListTables | None = ...,
        list_functions: global___ListFunctions | None = ...,
        list_columns: global___ListColumns | None = ...,
        get_database: global___GetDatabase | None = ...,
        get_table: global___GetTable | None = ...,
        get_function: global___GetFunction | None = ...,
        database_exists: global___DatabaseExists | None = ...,
        table_exists: global___TableExists | None = ...,
        function_exists: global___FunctionExists | None = ...,
        create_external_table: global___CreateExternalTable | None = ...,
        create_table: global___CreateTable | None = ...,
        drop_temp_view: global___DropTempView | None = ...,
        drop_global_temp_view: global___DropGlobalTempView | None = ...,
        recover_partitions: global___RecoverPartitions | None = ...,
        clear_cache: global___ClearCache | None = ...,
        refresh_table: global___RefreshTable | None = ...,
        refresh_by_path: global___RefreshByPath | None = ...,
        current_catalog: global___CurrentCatalog | None = ...,
        set_current_catalog: global___SetCurrentCatalog | None = ...,
        list_catalogs: global___ListCatalogs | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "cat_type",
            b"cat_type",
            "clear_cache",
            b"clear_cache",
            "create_external_table",
            b"create_external_table",
            "create_table",
            b"create_table",
            "current_catalog",
            b"current_catalog",
            "current_database",
            b"current_database",
            "database_exists",
            b"database_exists",
            "drop_global_temp_view",
            b"drop_global_temp_view",
            "drop_temp_view",
            b"drop_temp_view",
            "function_exists",
            b"function_exists",
            "get_database",
            b"get_database",
            "get_function",
            b"get_function",
            "get_table",
            b"get_table",
            "list_catalogs",
            b"list_catalogs",
            "list_columns",
            b"list_columns",
            "list_databases",
            b"list_databases",
            "list_functions",
            b"list_functions",
            "list_tables",
            b"list_tables",
            "recover_partitions",
            b"recover_partitions",
            "refresh_by_path",
            b"refresh_by_path",
            "refresh_table",
            b"refresh_table",
            "set_current_catalog",
            b"set_current_catalog",
            "set_current_database",
            b"set_current_database",
            "table_exists",
            b"table_exists",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "cat_type",
            b"cat_type",
            "clear_cache",
            b"clear_cache",
            "create_external_table",
            b"create_external_table",
            "create_table",
            b"create_table",
            "current_catalog",
            b"current_catalog",
            "current_database",
            b"current_database",
            "database_exists",
            b"database_exists",
            "drop_global_temp_view",
            b"drop_global_temp_view",
            "drop_temp_view",
            b"drop_temp_view",
            "function_exists",
            b"function_exists",
            "get_database",
            b"get_database",
            "get_function",
            b"get_function",
            "get_table",
            b"get_table",
            "list_catalogs",
            b"list_catalogs",
            "list_columns",
            b"list_columns",
            "list_databases",
            b"list_databases",
            "list_functions",
            b"list_functions",
            "list_tables",
            b"list_tables",
            "recover_partitions",
            b"recover_partitions",
            "refresh_by_path",
            b"refresh_by_path",
            "refresh_table",
            b"refresh_table",
            "set_current_catalog",
            b"set_current_catalog",
            "set_current_database",
            b"set_current_database",
            "table_exists",
            b"table_exists",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["cat_type", b"cat_type"]
    ) -> typing_extensions.Literal[
        "current_database",
        "set_current_database",
        "list_databases",
        "list_tables",
        "list_functions",
        "list_columns",
        "get_database",
        "get_table",
        "get_function",
        "database_exists",
        "table_exists",
        "function_exists",
        "create_external_table",
        "create_table",
        "drop_temp_view",
        "drop_global_temp_view",
        "recover_partitions",
        "clear_cache",
        "refresh_table",
        "refresh_by_path",
        "current_catalog",
        "set_current_catalog",
        "list_catalogs",
    ] | None: ...

global___Catalog = Catalog

class CurrentDatabase(google.protobuf.message.Message):
    """See `spark.catalog.currentDatabase`"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___CurrentDatabase = CurrentDatabase

class SetCurrentDatabase(google.protobuf.message.Message):
    """See `spark.catalog.setCurrentDatabase`"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DB_NAME_FIELD_NUMBER: builtins.int
    db_name: builtins.str
    """(Required)"""
    def __init__(
        self,
        *,
        db_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["db_name", b"db_name"]) -> None: ...

global___SetCurrentDatabase = SetCurrentDatabase

class ListDatabases(google.protobuf.message.Message):
    """See `spark.catalog.listDatabases`"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ListDatabases = ListDatabases

class ListTables(google.protobuf.message.Message):
    """See `spark.catalog.listTables`"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DB_NAME_FIELD_NUMBER: builtins.int
    db_name: builtins.str
    """(Optional)"""
    def __init__(
        self,
        *,
        db_name: builtins.str | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["_db_name", b"_db_name", "db_name", b"db_name"]
    ) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["_db_name", b"_db_name", "db_name", b"db_name"]
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["_db_name", b"_db_name"]
    ) -> typing_extensions.Literal["db_name"] | None: ...

global___ListTables = ListTables

class ListFunctions(google.protobuf.message.Message):
    """See `spark.catalog.listFunctions`"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DB_NAME_FIELD_NUMBER: builtins.int
    db_name: builtins.str
    """(Optional)"""
    def __init__(
        self,
        *,
        db_name: builtins.str | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["_db_name", b"_db_name", "db_name", b"db_name"]
    ) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["_db_name", b"_db_name", "db_name", b"db_name"]
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["_db_name", b"_db_name"]
    ) -> typing_extensions.Literal["db_name"] | None: ...

global___ListFunctions = ListFunctions

class ListColumns(google.protobuf.message.Message):
    """See `spark.catalog.listColumns`"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TABLE_NAME_FIELD_NUMBER: builtins.int
    DB_NAME_FIELD_NUMBER: builtins.int
    table_name: builtins.str
    """(Required)"""
    db_name: builtins.str
    """(Optional)"""
    def __init__(
        self,
        *,
        table_name: builtins.str = ...,
        db_name: builtins.str | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["_db_name", b"_db_name", "db_name", b"db_name"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "_db_name", b"_db_name", "db_name", b"db_name", "table_name", b"table_name"
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["_db_name", b"_db_name"]
    ) -> typing_extensions.Literal["db_name"] | None: ...

global___ListColumns = ListColumns

class GetDatabase(google.protobuf.message.Message):
    """See `spark.catalog.getDatabase`"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DB_NAME_FIELD_NUMBER: builtins.int
    db_name: builtins.str
    """(Required)"""
    def __init__(
        self,
        *,
        db_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["db_name", b"db_name"]) -> None: ...

global___GetDatabase = GetDatabase

class GetTable(google.protobuf.message.Message):
    """See `spark.catalog.getTable`"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TABLE_NAME_FIELD_NUMBER: builtins.int
    DB_NAME_FIELD_NUMBER: builtins.int
    table_name: builtins.str
    """(Required)"""
    db_name: builtins.str
    """(Optional)"""
    def __init__(
        self,
        *,
        table_name: builtins.str = ...,
        db_name: builtins.str | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["_db_name", b"_db_name", "db_name", b"db_name"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "_db_name", b"_db_name", "db_name", b"db_name", "table_name", b"table_name"
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["_db_name", b"_db_name"]
    ) -> typing_extensions.Literal["db_name"] | None: ...

global___GetTable = GetTable

class GetFunction(google.protobuf.message.Message):
    """See `spark.catalog.getFunction`"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FUNCTION_NAME_FIELD_NUMBER: builtins.int
    DB_NAME_FIELD_NUMBER: builtins.int
    function_name: builtins.str
    """(Required)"""
    db_name: builtins.str
    """(Optional)"""
    def __init__(
        self,
        *,
        function_name: builtins.str = ...,
        db_name: builtins.str | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["_db_name", b"_db_name", "db_name", b"db_name"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "_db_name", b"_db_name", "db_name", b"db_name", "function_name", b"function_name"
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["_db_name", b"_db_name"]
    ) -> typing_extensions.Literal["db_name"] | None: ...

global___GetFunction = GetFunction

class DatabaseExists(google.protobuf.message.Message):
    """See `spark.catalog.databaseExists`"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DB_NAME_FIELD_NUMBER: builtins.int
    db_name: builtins.str
    """(Required)"""
    def __init__(
        self,
        *,
        db_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["db_name", b"db_name"]) -> None: ...

global___DatabaseExists = DatabaseExists

class TableExists(google.protobuf.message.Message):
    """See `spark.catalog.tableExists`"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TABLE_NAME_FIELD_NUMBER: builtins.int
    DB_NAME_FIELD_NUMBER: builtins.int
    table_name: builtins.str
    """(Required)"""
    db_name: builtins.str
    """(Optional)"""
    def __init__(
        self,
        *,
        table_name: builtins.str = ...,
        db_name: builtins.str | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["_db_name", b"_db_name", "db_name", b"db_name"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "_db_name", b"_db_name", "db_name", b"db_name", "table_name", b"table_name"
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["_db_name", b"_db_name"]
    ) -> typing_extensions.Literal["db_name"] | None: ...

global___TableExists = TableExists

class FunctionExists(google.protobuf.message.Message):
    """See `spark.catalog.functionExists`"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FUNCTION_NAME_FIELD_NUMBER: builtins.int
    DB_NAME_FIELD_NUMBER: builtins.int
    function_name: builtins.str
    """(Required)"""
    db_name: builtins.str
    """(Optional)"""
    def __init__(
        self,
        *,
        function_name: builtins.str = ...,
        db_name: builtins.str | None = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["_db_name", b"_db_name", "db_name", b"db_name"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "_db_name", b"_db_name", "db_name", b"db_name", "function_name", b"function_name"
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["_db_name", b"_db_name"]
    ) -> typing_extensions.Literal["db_name"] | None: ...

global___FunctionExists = FunctionExists

class CreateExternalTable(google.protobuf.message.Message):
    """See `spark.catalog.createExternalTable`"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class OptionsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(
            self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]
        ) -> None: ...

    TABLE_NAME_FIELD_NUMBER: builtins.int
    PATH_FIELD_NUMBER: builtins.int
    SOURCE_FIELD_NUMBER: builtins.int
    SCHEMA_FIELD_NUMBER: builtins.int
    OPTIONS_FIELD_NUMBER: builtins.int
    table_name: builtins.str
    """(Required)"""
    path: builtins.str
    """(Optional)"""
    source: builtins.str
    """(Optional)"""
    @property
    def schema(self) -> pyspark.sql.connect.proto.types_pb2.DataType:
        """(Optional)"""
    @property
    def options(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Options could be empty for valid data source format.
        The map key is case insensitive.
        """
    def __init__(
        self,
        *,
        table_name: builtins.str = ...,
        path: builtins.str | None = ...,
        source: builtins.str | None = ...,
        schema: pyspark.sql.connect.proto.types_pb2.DataType | None = ...,
        options: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "_path",
            b"_path",
            "_schema",
            b"_schema",
            "_source",
            b"_source",
            "path",
            b"path",
            "schema",
            b"schema",
            "source",
            b"source",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "_path",
            b"_path",
            "_schema",
            b"_schema",
            "_source",
            b"_source",
            "options",
            b"options",
            "path",
            b"path",
            "schema",
            b"schema",
            "source",
            b"source",
            "table_name",
            b"table_name",
        ],
    ) -> None: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["_path", b"_path"]
    ) -> typing_extensions.Literal["path"] | None: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["_schema", b"_schema"]
    ) -> typing_extensions.Literal["schema"] | None: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["_source", b"_source"]
    ) -> typing_extensions.Literal["source"] | None: ...

global___CreateExternalTable = CreateExternalTable

class CreateTable(google.protobuf.message.Message):
    """See `spark.catalog.createTable`"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class OptionsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(
            self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]
        ) -> None: ...

    TABLE_NAME_FIELD_NUMBER: builtins.int
    PATH_FIELD_NUMBER: builtins.int
    SOURCE_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    SCHEMA_FIELD_NUMBER: builtins.int
    OPTIONS_FIELD_NUMBER: builtins.int
    table_name: builtins.str
    """(Required)"""
    path: builtins.str
    """(Optional)"""
    source: builtins.str
    """(Optional)"""
    description: builtins.str
    """(Optional)"""
    @property
    def schema(self) -> pyspark.sql.connect.proto.types_pb2.DataType:
        """(Optional)"""
    @property
    def options(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Options could be empty for valid data source format.
        The map key is case insensitive.
        """
    def __init__(
        self,
        *,
        table_name: builtins.str = ...,
        path: builtins.str | None = ...,
        source: builtins.str | None = ...,
        description: builtins.str | None = ...,
        schema: pyspark.sql.connect.proto.types_pb2.DataType | None = ...,
        options: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "_description",
            b"_description",
            "_path",
            b"_path",
            "_schema",
            b"_schema",
            "_source",
            b"_source",
            "description",
            b"description",
            "path",
            b"path",
            "schema",
            b"schema",
            "source",
            b"source",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "_description",
            b"_description",
            "_path",
            b"_path",
            "_schema",
            b"_schema",
            "_source",
            b"_source",
            "description",
            b"description",
            "options",
            b"options",
            "path",
            b"path",
            "schema",
            b"schema",
            "source",
            b"source",
            "table_name",
            b"table_name",
        ],
    ) -> None: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["_description", b"_description"]
    ) -> typing_extensions.Literal["description"] | None: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["_path", b"_path"]
    ) -> typing_extensions.Literal["path"] | None: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["_schema", b"_schema"]
    ) -> typing_extensions.Literal["schema"] | None: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["_source", b"_source"]
    ) -> typing_extensions.Literal["source"] | None: ...

global___CreateTable = CreateTable

class DropTempView(google.protobuf.message.Message):
    """See `spark.catalog.dropTempView`"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VIEW_NAME_FIELD_NUMBER: builtins.int
    view_name: builtins.str
    """(Required)"""
    def __init__(
        self,
        *,
        view_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["view_name", b"view_name"]
    ) -> None: ...

global___DropTempView = DropTempView

class DropGlobalTempView(google.protobuf.message.Message):
    """See `spark.catalog.dropGlobalTempView`"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VIEW_NAME_FIELD_NUMBER: builtins.int
    view_name: builtins.str
    """(Required)"""
    def __init__(
        self,
        *,
        view_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["view_name", b"view_name"]
    ) -> None: ...

global___DropGlobalTempView = DropGlobalTempView

class RecoverPartitions(google.protobuf.message.Message):
    """See `spark.catalog.recoverPartitions`"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TABLE_NAME_FIELD_NUMBER: builtins.int
    table_name: builtins.str
    """(Required)"""
    def __init__(
        self,
        *,
        table_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["table_name", b"table_name"]
    ) -> None: ...

global___RecoverPartitions = RecoverPartitions

class ClearCache(google.protobuf.message.Message):
    """TODO(SPARK-41612): Support Catalog.isCached
    // See `spark.catalog.isCached`
    message IsCached {
     // (Required)
     string table_name = 1;
    }

    TODO(SPARK-41600): Support Catalog.cacheTable
    // See `spark.catalog.cacheTable`
    message CacheTable {
     // (Required)
     string table_name = 1;
    }

    TODO(SPARK-41623): Support Catalog.uncacheTable
    // See `spark.catalog.uncacheTable`
    message UncacheTable {
     // (Required)
     string table_name = 1;
    }

    See `spark.catalog.clearCache`
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ClearCache = ClearCache

class RefreshTable(google.protobuf.message.Message):
    """See `spark.catalog.refreshTable`"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TABLE_NAME_FIELD_NUMBER: builtins.int
    table_name: builtins.str
    """(Required)"""
    def __init__(
        self,
        *,
        table_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["table_name", b"table_name"]
    ) -> None: ...

global___RefreshTable = RefreshTable

class RefreshByPath(google.protobuf.message.Message):
    """See `spark.catalog.refreshByPath`"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PATH_FIELD_NUMBER: builtins.int
    path: builtins.str
    """(Required)"""
    def __init__(
        self,
        *,
        path: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["path", b"path"]) -> None: ...

global___RefreshByPath = RefreshByPath

class CurrentCatalog(google.protobuf.message.Message):
    """See `spark.catalog.currentCatalog`"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___CurrentCatalog = CurrentCatalog

class SetCurrentCatalog(google.protobuf.message.Message):
    """See `spark.catalog.setCurrentCatalog`"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CATALOG_NAME_FIELD_NUMBER: builtins.int
    catalog_name: builtins.str
    """(Required)"""
    def __init__(
        self,
        *,
        catalog_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["catalog_name", b"catalog_name"]
    ) -> None: ...

global___SetCurrentCatalog = SetCurrentCatalog

class ListCatalogs(google.protobuf.message.Message):
    """See `spark.catalog.listCatalogs`"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ListCatalogs = ListCatalogs
