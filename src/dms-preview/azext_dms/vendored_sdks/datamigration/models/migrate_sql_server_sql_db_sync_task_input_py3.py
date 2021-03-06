# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .sql_migration_task_input_py3 import SqlMigrationTaskInput


class MigrateSqlServerSqlDbSyncTaskInput(SqlMigrationTaskInput):
    """Input for the task that migrates on-prem SQL Server databases to Azure SQL
    Database for online migrations.

    All required parameters must be populated in order to send to Azure.

    :param source_connection_info: Required. Information for connecting to
     source
    :type source_connection_info:
     ~azure.mgmt.datamigration.models.SqlConnectionInfo
    :param target_connection_info: Required. Information for connecting to
     target
    :type target_connection_info:
     ~azure.mgmt.datamigration.models.SqlConnectionInfo
    :param selected_databases: Required. Databases to migrate
    :type selected_databases:
     list[~azure.mgmt.datamigration.models.MigrateSqlServerSqlDbSyncDatabaseInput]
    :param validation_options: Validation options
    :type validation_options:
     ~azure.mgmt.datamigration.models.MigrationValidationOptions
    """

    _validation = {
        'source_connection_info': {'required': True},
        'target_connection_info': {'required': True},
        'selected_databases': {'required': True},
    }

    _attribute_map = {
        'source_connection_info': {'key': 'sourceConnectionInfo', 'type': 'SqlConnectionInfo'},
        'target_connection_info': {'key': 'targetConnectionInfo', 'type': 'SqlConnectionInfo'},
        'selected_databases': {'key': 'selectedDatabases', 'type': '[MigrateSqlServerSqlDbSyncDatabaseInput]'},
        'validation_options': {'key': 'validationOptions', 'type': 'MigrationValidationOptions'},
    }

    def __init__(self, *, source_connection_info, target_connection_info, selected_databases, validation_options=None, **kwargs) -> None:
        super(MigrateSqlServerSqlDbSyncTaskInput, self).__init__(source_connection_info=source_connection_info, target_connection_info=target_connection_info, **kwargs)
        self.selected_databases = selected_databases
        self.validation_options = validation_options
