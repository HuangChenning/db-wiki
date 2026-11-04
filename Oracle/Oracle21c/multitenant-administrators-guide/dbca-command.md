---
title: "Administrator’s Guide"
book: "Multitenant Administrator's Guide"
doc_id: F31734-10
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/multi/dbca-command.html
tags:
  - oracle
  - 21c
  - multitenant-administrators-guide
---

This section lists all the DBCA silent mode commands along with their syntax and parameter description.

- addInstance  
	The `addInstance` command adds a database instance to an administrator-managed Oracle RAC database.
- configureDatabase  
	The `configureDatabase` command configures a database.
- configurePluggableDatabase  
	The `configurePluggableDatabase` command configures a pluggable database (PDB).
- createCloneTemplate  
	The `createCloneTemplate` command creates a clone (seed) database template from an existing database.
- createDatabase  
	The `createDatabase` command creates a database.
- createDuplicateDB  
	The `createDuplicateDB` command creates a duplicate of an Oracle database.
- createPluggableDatabase  
	The `createPluggableDatabase` command creates a pluggable database (PDB) in a multitenant container database (CDB).
- createTemplateFromDB  
	The `createTemplateFromDB` command creates a database template from an existing database.
- createTemplateFromTemplate  
	The `createTemplateFromTemplate` command creates a database template from an existing database template.
- deleteDatabase  
	The `deleteDatabase` command deletes a database.
- deleteInstance  
	The `deleteInstance` command deletes a database instance from an administror-managed Oracle RAC database.
- deletePluggableDatabase  
	The `deletePluggableDatabase` command deletes a PDB.
- deleteTemplate  
	The `deleteTemplate` command deletes a database template.
- executePrereqs  
	The `executePrereqs` command executes the prerequisites checks and reports the results. This command can be used to check the environment before running `dbca` to create a database.
- generateScripts  
	The `generateScripts` command generates scripts, which can be used to create a database.
- relocatePDB  
	The `relocatePDB` command relocates a PDB from a remote CDB to a local CDB.
- unplugDatabase  
	The `unplugDatabase` command unplugs a pluggable database (PDB) from a multitenant container database (CDB).

**Parent topic:** [Database Configuration Assistant Command Reference for Silent Mode](dbca-reference.md)

### addInstance

The `addInstance` command adds a database instance to an administrator-managed Oracle RAC database.

Syntax and Parameters

Use the `dbca -addInstance` command with the following syntax:

```
dbca -addInstance 
   -gdbName global_database_name
   -nodeName database_instance_node_name
   [-updateDirService {true | false}
      -dirServiceUserName directory_service_user_name
      -dirServicePassword directory_service_user_password]
   [-instanceName database_instance_name]
   [-sysDBAUserName SYSDBA_user_name]
   [-sysDBAPassword SYSDBA_user_password]
   [-useWalletForDBCredentials {true | false}
      -dbCredentialsWalletPassword wallet_account_password
      -dbCredentialsWalletLocation wallet_files_directory]
```

Table 19-1 addInstance Parameters

| Parameter | Required/Optional | Description |
| --- | --- | --- |
| `-gdbName` `global_database_name` | Required | Global database name in the form database\_name.domain\_name. |
| `-nodeName` `database_instance_node_name` | Required | Node name of the database instance. |
| `-instanceName` `database_instance_name` | Optional | Database instance name. |
| `-sysDBAUserName` `SYSDBA_user_name` | Optional | User name of the database user having the `SYSDBA` privileges. |
| `-sysDBAPassword` `SYSDBA_user_password` | Optional | Password of the database user having the `SYSDBA` privileges. |
| `-updateDirService`  `{true \| false}` | Optional | Specify `true` to register the database with a directory service, else specify `false`.  When `true` is specified, the following additional parameters are required:  - `-dirServiceUserName`: User name for the directory service. - `—dirServicePassword`: Password for the directory service user. |
| `-useWalletForDBCredentials`  `{true \| false}` | Optional | Specify `true` to use Oracle Wallet for database credentials, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters can be provided:  - `-dbCredentialsWalletPassword`: Password for the Oracle Wallet account. - `-dbCredentialsWalletLocation`: Directory location for the Oracle Wallet files.  Note:  If you are using Oracle Unified Directory (OUD), then the OUD passwords should be stored in the wallet using the following keys:  - `oracle.dbsecurity.walletPassword` - `oracle.dbsecurity.userDNPassword` |

**Parent topic:** DBCA Silent Mode Commands

### configureDatabase

The `configureDatabase` command configures a database.

Syntax and Parameters

Use the `dbca` `-configureDatabase` command with the following syntax:

```
dbca -configureDatabase 
   -sourceDB database_sid
   [-addDBOption database_options]
   [-configureOML4PY
      [-oml4pyConfigTablespace tablespace_for_OML4PY_configuration]
      [-enableOml4pyEmbeddedExecution {true | false}]]
   [-configureOracleR
      -oracleRConfigTablespace tablespace_for_Oracle_R_configuration]
   [-dvConfiguration {true | false}
      -dvUserName Database_Vault_owner_name
      -dvUserPassword Database_Vault_owner_password
      [-dvAccountManagerName Database_Vault_account_manager_name]
      [-dvAccountManagerPassword Database_Vault_account_manager_password]]
   [-moveDatabaseFiles
      -datafileDestination data_files_directory
      -sourceDB database_sid
      [-initParams initialization_parameters_list
        [-initParamsEscapeChar initialization_parameters_escape_character]]
      [-recoveryAreaDestination fast_recovery_area_directory
        [-recoveryAreaSize fast_recovery_area_size]]
      [-useOMF {true | false}]
   [-olsConfiguration {true | false}
      -configureWithOID configure_with_OID_flag]
   [-regenerateDBPassword {true | false}]
   [-registerWithDirService {true | false}
      -dirServiceUserName directory_service_user_name
      [-databaseCN database_common_name]
      [-dirServiceCertificatePath certificate_file_path]
      [-dirServiceUser directory_service_user_name]
      [-dirServicePassword directory_service_password]
      [-ldapDirectoryAccessType ldap_directory_access_type]
      [-useSYSAuthForLDAPAccess use_sys_user_for_ldap_access_flag]
      [-walletPassword wallet_password]]
   [-sysDBAPassword SYSDBA_user_password]
   [-sysDBAUserName SYSDBA_user_name]
   [-unregisterWithDirService {true | false}
      -dirServiceUserName directory_service_user_name
      [-dirServicePassword directory_service_password]
      [-walletPassword wallet_password]]
   [-useWalletForDBCredentials {true | false} 
      -dbCredentialsWalletPassword wallet_account_password
      -dbCredentialsWalletLocation wallet_files_directory]
```

Table 19-2 configureDatabase Parameters

| Parameter | Required/Optional | Description |
| --- | --- | --- |
| `-sourceDB` `database_sid` | Required | The database system identifier (SID) of the database being configured. |
| `-addDBOption`  `database_options` | Optional | Specify one or more of the following Oracle Database options in the form of a comma separated list:  - `JSERVER`: Oracle JServer JAVA Virtual Machine - `ORACLE_TEXT`: Oracle Text - `IMEDIA`: Oracle Locator (fully supported) and Oracle Multimedia (desupported) - `CWMLITE`: Oracle OLAP with Oracle Warehouse Builder (OWB) - `SPATIAL`: Oracle Spatial and Graph - `OMS`: Oracle Management Server - `APEX`: Oracle Application Express - `DV`: Oracle Database Vault  Example:  ``` -addDBOption JSERVER,ORACLE_TEXT,OMS ``` |
| `-configureOML4PY` | Optional | Specify this parameter to configure Oracle Machine Learning for Python in the database.  Additionally, you specify the following parameters: - `-oml4pyConfigTablespace` to configure the tablespace of the `PYQSYS` schema for Oracle Machine Learning for Python. The default tablespace is `SYSAUX`. - `-enableOml4pyEmbeddedExecution` to enable the embedded Python component of Oracle Machine Learning for Python. The default value is `TRUE`. |
| `-configureOracleR` | Optional | Specify this parameter to configure Oracle R in the database.  Additionally, you can specify the `-oracleRConfigTablespace` parameter to assign a tablespace for the Oracle R configuration, such as `SYSAUX` tablespace. |
| `-dvConfiguration`  `{true \| false}` | Optional | Specify `true` to enable and configure Database Vault, or specify `false`. Default is `false`.  When `true` is specified, the following additional Database Vault parameters are required:  - `-dvUserName`: Specify the Database Vault owner username. - `-dvUserPassword`: Specify Database Vault owner password. - `-dvAccountManagerName`: Specify a separate Database Vault account manager. - `-dvAccountManagerPassword`: Specify the Database Vault account manager password. |
| `-moveDatabaseFiles` | Optional | Specify this parameter to move database files from one storage location to another storage location. For example, to move database files from ASM to FS, or from FS to ASM.  Specify the following additional parameters:  - `-datafileDestination`: Destination directory for all the database files - `-sourceDB`: Database system identifier (SID) for a single instance database or database unique name for an Oracle RAC database - `-initParams`: Database initialization parameters in the form of comma separated list of `name=value` pairs 	Additionally, you can specify the `-initParamsEscapeChar` parameter for using a specific escape character between multiple values of an initialization parameter. If an escape character is not specified, backslash (/) is used as the default escape character. - `-recoveryAreaDestination`: Destination directory for the Fast Recovery Area, which is a backup and recovery area. Specify `NONE` to disable Fast Recovery Area. 	Additionally, you can specify the Fast Recovery Area size in megabytes using the parameter `-recoveryAreaSize`. This parameter is optional. - `-useOMF`: Specify `true` to use Oracle-Managed Files (OMF), else specify `false`. |
| `-olsConfiguration`  `{true \| false}` | Optional | Specify `true` to enable and configure Oracle Label Security, else specify `false`. Default is `false`.  When `true` is specified, you can additionally specify the `-configureWithOID` parameter to configure Oracle Label Security with Oracle Internet Directory (OID). This parameter is optional. |
| `-regenerateDBPassword` `{true \| false}` | Optional | Specify `true` to regenerate Oracle Internet Directory (OID) server registration password, else specify `false`. Default is `false`. |
| `-registerWithDirService`  `{true \| false}` | Optional | Specify `true` to register with a Lightweight Directory Access Protocol (LDAP) service, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters are required:  - `-dirServiceUserName`: User name for the LDAP service. - `-dirServicePassword`: Password for the LDAP service. - `-databaseCN`: Database common name. - `-dirServiceCertificatePath`: Directory service certificate file path. - `-dirServiceUser`: Directory service user name. - `-ldapDirectoryAccessType {PASSWORD \| SSL}`: LDAP directory access type. - `-useSYSAuthForLDAPAccess {true \| false}`: Specify whether to use SYS user authentication for LDAP access. - `-walletPassword`: Password for the database wallet. |
| `-sysDBAPassword` `SYSDBA_user_password` | Optional | Password of a user having `SYSDBA` privileges. |
| `-sysDBAUserName` `SYSDBA_user_name` | Optional | User name of a user having `SYSDBA` privileges. |
| `-unregisterWithDirService `  `{true \| false}` | Optional | Specify `true` to unregister with a Lightweight Directory Access Protocol (LDAP) service, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters are required:  - `-dirServiceUserName`: User name for the LDAP service. - `-dirServicePassword`: Password for the LDAP service. - `-walletPassword`: Password for the database wallet. |
| `-useWalletForDBCredentials`  `{true \| false}` | Optional | Specify `true` to use Oracle Wallet for database credentials, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters can be provided:  - `-dbCredentialsWalletLocation`: Directory location for the Oracle Wallet files. - `-dbCredentialsWalletPassword`: Password for the Oracle Wallet account.  Note:  If you are using Oracle Unified Directory (OUD), then the OUD passwords should be stored in the wallet using the following keys:  - `oracle.dbsecurity.walletPassword` - `oracle.dbsecurity.userDNPassword` |

**Parent topic:** DBCA Silent Mode Commands

### configurePluggableDatabase

The `configurePluggableDatabase` command configures a pluggable database (PDB).

Syntax and Parameters

Use the `dbca` `-configurePluggableDatabase` command with the following syntax:

```
dbca -configurePluggableDatabase
   -pdbName pdb_name 
   -sourceDB cdb_sid
   [-configureOML4PY
      [-oml4pyConfigTablespace tablespace_for_OML4PY_configuration]
      [-enableOml4pyEmbeddedExecution {true | false}]]
   [-configureOracleR
      [-oracleRConfigTablespace tablespace_for_Oracle_R_configuration]]
   [-dvConfiguration {true | false}
      -dvUserName Database_Vault_owner_name
      -dvUserPassword Database_Vault_owner_password
      [-dvAccountManagerName Database_Vault_account_manager_name]
      [-dvAccountManagerPassword Database_Vault_account_manager_password]]
   [-lbacsysPassword LBACSYS_user_password]]
   [-olsConfiguration {true | false}
      [-configureWithOID configure_with_OID_flag]]
   [-pdbTimezone {{+|-}hh:mi|time_zone_region}]
   [-registerWithDirService {true | false}
      -dirServiceUserName directory_service_user_name
      [-dirServicePassword directory_service_user_password]
      [-walletPassword wallet_password]
      [-databaseCN database_common_name]
      [-dirServiceCertificatePath certificate_file_path]
      [-dirServiceUser active_directory_account_user_name]]
   [-unregisterWithDirService {true | false}
      -dirServiceUserName directory_service_user_name
      [-dirServicePassword directory_service_user_password]
      [-walletPassword wallet_password]]
   [-useWalletForDBCredentials {true | false}
      -dbCredentialsWalletPassword wallet_account_password
      -dbCredentialsWalletLocation wallet_files_directory]
```

Table 19-3 configurePluggableDatabase Parameters

| Parameter | Required/Optional | Description |
| --- | --- | --- |
| `-pdbName` `pdb_name` | Required | Name of the PDB. |
| `-sourceDB` `cdb_sid` | Required | The database system identifier (SID) of the CDB. |
| `-configureOML4PY` | Optional | Specify this parameter to configure Oracle Machine Learning for Python in the database.  Additionally, you specify the following parameters: - `-oml4pyConfigTablespace` to configure the tablespace of the `PYQSYS` schema for Oracle Machine Learning for Python. The default tablespace is `SYSAUX`. - `-enableOml4pyEmbeddedExecution` to enable the embedded Python component of Oracle Machine Learning for Python. The default value is `TRUE`. |
| `-configureOracleR` | Optional | Specify this parameter to configure Oracle R for the PDB.  Additionally, you can specify the `-oracleRConfigTablespace` parameter to assign a tablespace for the Oracle R configuration, for example, `SYSAUX` tablespace. |
| `-dvConfiguration` `{true \| false}` | Optional | Specify `true` to enable and configure Database Vault for the PDB, else specify `false`. Default is `false`.  When `true` is specified, the following additional Database Vault parameters are required:  - `-dvUserName`: Specify the Database Vault owner user name. - `-dvUserPassword`: Specify Database Vault owner password. - `-dvAccountManagerName`: Specify a separate Database Vault account manager. - `-dvAccountManagerPassword`: Specify the Database Vault account manager password. |
| `-lbacsysPassword` | Optional | Specify the `LBACSYS` user password, if you want to configure OLS with a directory service. |
| `-olsConfiguration` `{true \| false}` | Optional | Specify `true` to enable and configure Oracle Label Security (OLS) for the PDB, else specify `false`. Default is `false`.  When `true` is specified, you can additionally specify the `-configureWithOID` parameter to configure Oracle Label Security (OLS) with Oracle Internet Directory (OID). This parameter is optional. |
| `-pdbTimezone` `{{+\|-}hh:mi\|time_zone_region}` | Optional | Use this parameter to specify the time zone of the PDB.  You can specify the time zone in two ways: - By specifying a displacement from UTC (Coordinated Universal Time—formerly Greenwich Mean Time). The valid range of hh:mi is -12:00 to +14:00. - By specifying a time zone region. To see a listing of valid time zone region names, query the `TZNAME` column of the `V$TIMEZONE_NAMES` dynamic performance view. |
| `-registerWithDirService` `{true \| false}` | Optional | Specify `true` to register the PDB with a Lightweight Directory Access Protocol (LDAP) service, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters can be provided:  - `-dirServiceUserName`: User name for the LDAP service. - `-dirServicePassword`: Password for the LDAP service user. - `-walletPassword`: Password for the database wallet. - `-databaseCN`: Database common name. - `-dirServiceCertificatePath`: Directory service certificate file path. - `-dirServiceUser`: Active Directory account user name. |
| `unregisterWithDirService` `{true \| false}` | Optional | Specify `true` to unregister the PDB with the Lightweight Directory Access Protocol (LDAP) service, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters can be provided:  - `-dirServiceUserName`: User name for the LDAP service. - `-dirServicePassword`: Password for the LDAP service user. - `-walletPassword`: Password for the database wallet. |
| `-useWalletForDBCredentials`  `{true \| false}` | Optional | Specify `true` to use Oracle Wallet for database credentials, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters can be provided:  - `-dbCredentialsWalletPassword`: Password for the Oracle Wallet account. - `-dbCredentialsWalletLocation`: Directory location for the Oracle Wallet files.  Note:  If you are using Oracle Unified Directory (OUD), then the OUD passwords should be stored in the wallet using the following keys:  - `oracle.dbsecurity.walletPassword` - `oracle.dbsecurity.userDNPassword` |

**Parent topic:** DBCA Silent Mode Commands

### createCloneTemplate

The `createCloneTemplate` command creates a clone (seed) database template from an existing database.

Syntax and Parameters

Use the `dbca` `-createCloneTemplate` command with the following syntax:

```
dbca -createCloneTemplate
   -sourceSID source_database_sid | -sourceDB source_database_name
   -templateName new_database_template_name
   [-promptForWalletPassword]
   [-rmanParallelism parallelism_integer_value]
   [-maxBackupSetSizeInMB maximum_backup_set_size_in_MB]
   [-dataFileBackup {true | false}]
   [-datafileJarLocation data_files_backup_directory]
   [-sysDBAUserName SYSDBA_user_name]
   [-sysDBAPassword SYSDBA_user_password]
   [-useWalletForDBCredentials {true | false}
       -dbCredentialsWalletPassword wallet_account_password
       -dbCredentialsWalletLocation wallet_files_directory]
   [-uploadToCloud 
       -opcLibPath OPC_library_path
       -opcConfigFile OPC_configuration_file_name
       [-rmanEncryptionPassword rman_encryption_password ]
   [-compressBackup { true | false } ]
   [-walletPassword database_wallet_password]
```

Table 19-4 createCloneTemplate Parameters

| Parameter | Required/Optional | Description |
| --- | --- | --- |
| `-sourceSID` `source_database_sid`  or  `-sourceDB` `source_database_name` | Required | Specify either the source database system identifier (SID) or the source database name. |
| `-templateName` `new_database_template_name` | Required | Name of the new database template. |
| `-sysDBAUserName` `SYSDBA_user_name` | Optional | User name of a user having the `SYSDBA` privileges. |
| `-sysDBAPassword` `SYSDBA_user_password` | Optional | Password of the user having the `SYSDBA` privileges. |
| `-maxBackupSetSizeInMB` `maximum_backup_set_size_in_MB` | Optional | Maximum backup set size in megabytes. |
| `-rmanParallelism` `parallelism_integer_value` | Optional | Parallelism integer value for RMAN operations. |
| `-datafileJarLocation` `data_files_backup_directory` | Optional | Complete directory path to store data files as a backup in a compressed format. |
| `-dataFileBackup {true \| false}` | Optional | Specify `true` to take the data files backup, else specify `false`. |
| `-useWalletForDBCredentials`  `{true \| false}` | Optional | Specify `true` to use Oracle Wallet for database credentials, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters can be provided:  - `-dbCredentialsWalletPassword`: Password for the Oracle Wallet account. - `-dbCredentialsWalletLocation`: Directory location for the Oracle Wallet files.  Note:  If you are using Oracle Unified Directory (OUD), then the OUD passwords should be stored in the wallet using the following keys:  - `oracle.dbsecurity.walletPassword` - `oracle.dbsecurity.userDNPassword` |
| `-uploadToCloud` | Optional | Creates a clone template and uploads it to Oracle Cloud Infrastructure. The structure and data of the database is stored in the template. DBCA can then use this template to create new databases.  To create a template to Oracle Cloud Infrastructure, you must subscribe to the Oracle Database Backup Cloud Service and install the Oracle Database Cloud Backup Module for OCI. Recovery Manager (RMAN) creates a backup containing the details of the clone template. The backup must be encrypted, so you must provide the RMAN encryption password to encrypt backups.  This option is only supported on Linux.  - `opcLibPath`: Directory in which the Oracle Database Cloud Backup Module for OCI is stored. The backup module is a system backup to tape (SBT) library that is used to integrate on-premise databases with Oracle Cloud Infrastructure. The file name is `libopc.so` on Linux. - `opcConfigFile`: Name, with complete location, of the Oracle Database Cloud Backup Module for OCI configuration file. This file is created when you install the backup module. - `rmanEncryptionPassword`: Password used to encrypt the RMAN backups to Cloud that contian the clone template.  See [Administering Oracle Database Backup Cloud Service](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=CSDBB-GUID-483BAC13-854B-4044-9569-0FAD313AD126) for information about installing and configuring the backup module. |
| `-compressBackup` | Optional | Compresses the backup containing the clone template files. |
| `-walletPassword` | Optional | Password of the TDE wallet that contains the keys used to encrypt backups. Specify this parameter if Transparent Data Encryption (TDE) must be used to encrypt backups. |

**Parent topic:** DBCA Silent Mode Commands

### createDatabase

The `createDatabase` command creates a database.

Syntax and Parameters

Use the `dbca` `-createDatabase` command with the following syntax:

```
dbca -createDatabase
    -gdbName global_database_name 
    -responseFile | (-gdbName,-templateName)
    -responseFile response_file_directory
    -templateName database_template_name
    [-adminManaged]
    [-characterSet database_character_set]
    [-configureTDE {true | false} 
          [-primaryDBTdeWallet value]
          [-sourceTdeWalletPassword value]
          [-tdeWalletRoot tde_wallet_root_init_parameter]
          [-pdbTDEPassword pdb_tde_wallet_password]
          [-tdeWalletModeForPDB pdb_keystore_type]
          [-tdeAlgorithm TDE_algorithm]
          [-tdeWalletLoginType type_of_wallet_login]
          [-sourcePdbTDEPassword source_pdb_TDE_wallet_password]
          [-tdeWalletPassword TDE_wallet_password]]
    [-createAsContainerDatabase {true | false}
        [-numberOfPDBs number_of_pdbs]
        [-pdbName pdb_name]
        [-pdbStorageMAXSizeInMB maximum_storage_size_of_the_pdb]
        [-pdbStorageMAXTempSizeInMB maximum_temporary_storage_size_of_the_pdb]
        [-useLocalUndoForPDBs {true | false}]
        [-pdbAdminPassword pdb_administrator_password]
        [-pdbOptions pdb_options]]
    [-createListener new_database_listener]
    [-customScripts list_of_custom_sql_scripts]
    [-databaseConfigType {SINGLE | RAC | RACONENODE}
            [-RACOneNodeServiceName service_name_for_RAC_One_Node_database]]
    [-databaseType {MULTIPURPOSE | DATA_WAREHOUSING | OLTP}]
    [-datafileDestination data_files_directory]
    [-datafileJarLocation data_files_backup_directory]
    [-dbOptions database_options]
    [-dvConfiguration {true | false}
        -dvUserName Database_Vault_owner_name
        -dvUserPassword Database_Vault_owner_password
        [-dvAccountManagerName Database_Vault_account_manager_name
        -dvAccountManagerPassword Database_Vault_account_manager_password]]
    [-emConfiguration {DBEXPRESS | CENTRAL | BOTH | NONE}
        [-dbsnmpPassword DBSNMP_user_password]
        [-omsHost Oracle_Management_Server_host_name]
        [-omsPort Oracle_Management_Server_port_number]
        [-emUser EM_administrator_user_name]
        [-emPassword EM_administrator_user_password]
        [-emExpressPort EM_Express_port]
        [-emExpressPortAsGlobalPort EM_Express_global_port]]
    [-enableArchive {true | false} 
        [-archiveLogMode {AUTO | MANUAL}]
        [-archiveLogDest archive_log_files_directory]]
    [-encryptPDBTablespaces ALL|tablespace_name:{true | false}]
    [-encryptTablespaces ALL|tablespace_name:{true | false}]
    [-initParams initialization_parameters_list
        [-initParamsEscapeChar initialization_parameters_escape_character]]
    [-listeners listeners_list]
    [-managementPolicy [AUTOMATIC|RANK]]
    [-memoryMgmtType {AUTO | AUTO_SGA | CUSTOM_SGA}]
    [-memoryPercentage | -totalMemory]
    [-memoryPercentage percentage_of_total_memory_to_assign_to_oracle_database]
    [-nationalCharacterSet database_national_character_set]
    [-nodelist database_nodes_list]
    [-olsConfiguration {true | false}
        [-configureWithOID configure_with_OID_flag]]
    [-oracleHomeUserName Oracle_Home_user_name]
    [-oracleHomeUserPassword Oracle_Home_user_password]
    [-policyManaged
        -serverPoolName server_pool_names
        [-pqPoolName pq_pool_name]
        [-createServerPool new_server_pool_name]
            [-pqPoolName new_pq_pool_name]
            [-force]
            [-pqCardinality pq_cardinality_of_the_new_server_pool]
            [-cardinality cardinality_of_the_new_server_pool]]
    [-recoveryAreaDestination recovery_files_directory
        [-recoveryAreaSize fast_recovery_area_size]]
    [-redoLogFileSize maximum_redo_log_file_size]
    [-registerWithDirService {true | false} 
        [-dirServiceUserName directory_service_user_name]
        [-dirServicePassword directory_service_password]
        [-databaseCN database_common_name]
        [-dirServiceCertificatePath certificate_file_path]
        [-dirServiceUser directory_service_user_name]
        [-ldapDirectoryAccessType ldap_directory_access_type]
        [-useSYSAuthForLDAPAccess use_sys_user_for_ldap_access_flag]
        [-walletPassword wallet_password]]
    [-runCVUChecks {true | false}]
    [-sampleSchema {true | false}]
    [-sid database_system_identifier]
    [-storageType {FS | ASM } 
        [-asmsnmpPassword ASMSNMP_password]
        -datafileDestination database_files_directory]
    [-sysPassword SYS_user_password]
    [-systemPassword SYSTEM_user_password]
    [-templateFromCloud 
        -opcLibPath OPC_library_path
        -opcConfigFile OPC_config_file_name
        [-rmanDecryptionPassword rman_decryption_password]]
    [-totalMemory total_memory_to_assign_to_oracle_database_in_MB]
    [-useOMF {true | false}]
    [-useWalletForDBCredentials { true | false}
         -dbCredentialsWalletLocation directory_containing_wallet_files
         [-dbCredentialsWalletPassword password_to_open_wallet]]
    [-variables variables_list]
    [-variablesFile variables_file]
```

Table 19-5 createDatabase Parameters

| Parameter | Required/Optional | Description |
| --- | --- | --- |
| `-gdbName`  `global_database_name` | Required | Global database name in the form database\_name.domain\_name. |
| `-responseFile`  `response_file_directory` | Required | Absolute directory path of the response file. |
| `-templateName`  `database_template_name` | Required | Name of an existing database template in the default location or the complete path to a database template that is not in the default location. |
| `-adminManaged` | Optional | Administrator-managed database. |
| `-characterSet`  `database_character_set` | Optional | Character set of the database. |
| `configureTDE` | Optional | Specify `true` to configure TDE during the database creation. Only software wallets are supported. You can create a wallet for the entire CDB or for a PDB.  - `primaryDBTdeWallet`: This option is not applicable when creating a database. - `sourceTdeWalletPassword`: If the template that is being used is from a database that uses encryption, or if you are duplicating a database, specify the password of the wallet in the source database. - `tdeWalletModeForPDB`: Specify `UNITED` to create a wallet for the entire CDB. Use `ISOLATED` to create a wallet for a PDB. - `tdeAlgorithm`: Algorithm used to encrypt data. Can be one of the following: 3DES168, AES128, AES192, AES256. - `tdeWalletLoginType`: Type of software wallet. `PASSWORD` or `AUTO_LOGIN` or `LOCAL_AUTO_LOGIN`. - `tdeWalletLocation`: Location in which the TDE wallet is stored. - `tdeWalletPassword`: The password used to open the wallet. This parameter is mandatory.  Note: Isolated wallets are supported only in Oracle Cloud or Exadata environments. |
| `-createAsContainerDatabase`  `{true \| false}` | Optional | Specify `true` to create a CDB. Specifying `false` is not supported starting with Oracle Database Release 20.3.  When `true` is specified, the following additional parameters are optional:  - `-numberOfPDBs`: Number of PDBs to create. The default is 0 (zero). - `-pdbName`: Base name of each PDB. A number is appended to each name if `-numberOfPDBs` is greater than 1. This parameter must be specified if `-numberOfPDBs` is greater than 0 (zero). - `-pdbStorageMAXSizeInMB`: Maximum storage size for the PDBs in megabytes. - `-pdbStorageMAXTempSizeInMB`: Maximum temporary storage size for the PDBs in megabytes. - `-useLocalUndoForPDBs {true \| false}`: Specify whether local undo should be used for the PDBs. - `-pdbAdminPassword`: PDB administrator password. - `-pdbOptions`: Specify PDB options as comma separated list in `name:value` format. 	Example: `JSERVER:true`, `DV:false` |
| `-createListener`  `new_database_listener` | Optional | Database listener to register the database in the form listener\_name:port. |
| `-customScripts`  `custom_scripts_list` | Optional | Specify a comma separated list of SQL scripts that needs to be run after the database creation. The scripts are run in the order they are listed. |
| `-databaseConfigType`  `{SINGLE \| RAC \| RACONENODE}` | Optional | Specify one of the following database configuration types:  - `SINGLE`: Single individual database. - `RAC`: Oracle RAC database. - `RACONENODE`: Oracle RAC One Node database. 	For Oracle RAC One Node database, you can specify the service name using the `-RACOneNodeServiceName` parameter. |
| `-databaseType`  `{MULTIPURPOSE \| DATA_WAREHOUSING \|                                     OLTP}` | Optional | Specify `MULTIPURPOSE` if the database is for both OLTP and data warehouse purposes.  Specify `DATA_WAREHOUSING` if the primary purpose of the database is a data warehouse.  Specify `OLTP` if the primary purpose of the database is online transaction processing. |
| `-datafileDestination`  `data_files_directory` | Optional | Complete path to the location of the database data files. |
| `-datafileJarLocation`  `data_files_backup_directory` | Optional | Absolute directory path of the database backup data files stored in a compressed RMAN backup format (files with.dfb extensions). |
| `-dbOptions`  `database_options` | Optional | Specify database options as comma separated list of `name:value` pairs.  Example: `JSERVER:true,DV:false` |
| `-dvConfiguration`  `{true \| false}` | Optional | Specify `true` to enable and configure Database Vault, else specify `false`. Default is `false`.  When `true` is specified, the following additional Database Vault parameters are required:  - `-dvUserName`: Specify Database Vault owner name. - `-dvUserPassword`: Specify Database Vault owner password. - `-dvAccountManagerName`: Specify Database Vault account manager name. - `-dvAccountManagerPassword`: Specify Database Vault account manager password. |
| `-emConfiguration`  `{DBEXPRESS \| CENTRAL \| BOTH \| NONE}` | Optional | Enterprise Manager configuration settings.  Oracle Enterprise Manager Database Express (EM Express) is deprecated, and will be removed in a future Oracle Database release.  When `DBEXPRESS`, `CENTRAL`, or `BOTH` is specified, specify the following additional parameters:  - `-dbsnmpPassword`: DBSNMP user password. - `-omsHost`: Oracle Management Server host name. - `-omsPort`: Oracle Management Server port number. - `-emUser`: User name for Enterprise Manager administrator. - `-emPassword`: Password for Enterprise Manager administrator. - `-emExpressPort`: Enterprise Manager Express port number. - `-emExpressPortAsGlobalPort`: Enterprise Manager Express global port number. |
| `-enableArchive`  `{true \| false}` | Optional | Specify `true` to enable log file archive, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters can be provided:  - `-archiveLogMode {AUTO \| MANUAL}`: Specify either the automatic archive mode or the manual archive mode. Default is automatic archive mode. - `-archiveLogDest`: Directory path for storing the archive log files. |
| `-encryptPDBTablespaces` | Optional | If you have configured TDE using `-configureTDE`, you can use this parameter to encrypt all of some of the tablespaces at the PDB and CDB level.  Specify the following additional parameters: - `ALL`: Encrypt all tablespaces - `tablespace_name`: Comma-separated list of tablespaces with a value of `TRUE` or `FALSE` for each |
| `-encryptTablespaces` | Optional | If you have configured TDE using `-configureTDE`, you can use this parameter to encrypt all or some of the tablespaces at the CDB level.  Specify the following additional parameters: - `ALL`: Encrypt all tablespaces - `tablespace_name`: Comma-separated list of tablespaces with a value of `TRUE` or `FALSE` for each |
| `-initParams`  `initialization_parameters_list` | Optional | A comma-separated list of `name=value` pairs of initialization parameter values for the database.  You can additionally provide the `-initParamsEscapeChar` parameter for using a specific escape character between multiple values of an initialization parameter. If an escape character is not specified, backslash (/) is used as the default escape character. |
| `-listeners`  `listeners_list` | Optional | A comma-separated list of listeners for the database. |
| `-managementPolicy` | Optional | Use this parameter to set the database management policy.  Optionally, specify the management policy type: - `AUTOMATIC` - `RANK`  If `-adminManaged` is selected, `-managementPolicy` defaults to `AUTOMATIC`. |
| `-memoryMgmtType`  `{AUTO \| AUTO_SGA \| CUSTOM_SGA}` | Optional | Specify one of the following memory management types:  - `AUTO`: Automatic memory management for SGA and PGA. - `AUTO_SGA`: Automatic shared memory management for SGA. - `CUSTOM_SGA`: Manual shared memory management for SGA.  Note: If the total physical memory of a database instance is greater than 4 GB, then you cannot specify the Automatic Memory Management option `AUTO` during the database installation and creation. Oracle recommends that you specify the Automatic Shared Memory Management option `AUTO_SGA` in such environments. |
| `-memoryPercentage`  `percentage_of_total_memory_to_assign_to_oracle_database`  or  `-totalMemory`  `total_memory_to_assign_to_oracle_database_in_MB` | Optional | Specify either `-memoryPercentage` or `-totalMemory`.  - `-memoryPercentage` 	The percentage of physical memory that can be used by the database. - `-totalMemory`. 	Total amount of physical memory, in megabytes, that can be used by the database. |
| `-nationalCharacterSet`  `database_national_character_set` | Optional | National character set of the database. |
| `-nodelist`  `database_nodes_list` | Optional | List of database nodes separated by comma. |
| `-olsConfiguration`  `{true \| false}` | Optional | Specify `true` to enable and configure Oracle Label Security (OLS), else specify `false`. Default is `false`.  When `true` is specified, you can additionally specify the `-configureWithOID` parameter, if you want to configure Oracle Label Security (OLS) with Oracle Internet Directory (OID). |
| `-oracleHomeUserName`  `Oracle_Home_user_name`  `-oracleHomeUserPassword`  `Oracle_Home_user_password` | Optional | Oracle Home user name and password. |
| `-policyManaged` | Optional | Policy-managed database.  You can specify the following additional parameters:  - `-serverPoolName`: Specify the single server pool name when creating a new server pool or specify a comma separated list of existing server pools. - `-pqPoolName`: Specify the PQ pool name. - `-createServerPool`: Specify this parameter for creating a new server pool. 	: 	- `-pqPoolName`: Specify the PQ pool name. 		- `-force`: Specify this parameter to create the server pool by force when adequate free servers are not available. 		- `-pqCardinality`: Specify the PQ cardinality of the new server pool. 		- `-cardinality`: Specify the cardinality of the new server pool. |
| `-recoveryAreaDestination`  `fast_recovery_area_directory` | Optional | Destination directory for the Fast Recovery Area, which is a backup and recovery area. Specify `NONE` to disable Fast Recovery Area.  Additionally, you can specify the Fast Recovery Area size in megabytes using the parameter `-recoveryAreaSize`. This parameter is optional. |
| `-redoLogFileSize`  `maximum_size_of_redo_log_file` | Optional | Size of each online redo log in megabytes. |
| `-registerWithDirService `  `{true \| false}` | Optional | Specify `true` to register with a Lightweight Directory Access Protocol (LDAP) service, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters are required:  - `-dirServiceUserName`: Username for the LDAP service. - `-dirServicePassword`: Password for the LDAP service. - `-databaseCN`: Database common name. - `-dirServiceCertificatePath`: Directory path to the certificate file to use when configuring SSL between the database and the directory service. - `-dirServiceUser`: Directory service user name. - `-ldapDirectoryAccessType {PASSWORD \|                                             SSL}`: LDAP directory access type. - `-useSYSAuthForLDAPAccess {true \|                                             false}`: Specify whether to use SYS user authentication for LDAP acces. - `-walletPassword`: Password for the database wallet. |
| `-runCVUChecks`  `{true \| false}` | Optional | Specify `true` to run Cluster Verification Utility checks periodically for Oracle RAC databases, else specify `false`. Default is `false`. |
| `-sampleSchema`  `{true \| false}` | Optional | Specify `true` to include the `HR` sample schema (`EXAMPLE` tablespace) in your database. Oracle guides and educational materials contain examples based on the sample schemas. Oracle strongly recommends that you do not install the sample schemas in a production database.  Specify `false` to create the database without the `HR` sample schema. Default is `false`. |
| `-sid`  `database_system_identifier` | Optional | Database system identifier (SID).  The SID uniquely identifies the instance that runs the database. If it is not specified, then it defaults to the database name. |
| `-storageType`  `{FS \| ASM}` | Optional | Specify the storage type of either `FS` or `ASM`.  - `FS`: File system storage type. 	When `FS` is specified, your database files are managed by the file system of your operating system. You can specify the directory path where the database files are to be stored using a database template or the `-datafileDestination` parameter. Oracle Database can create and manage the actual files. - `ASM`: Oracle Automatic Storage Management (Oracle ASM) storage type. 	When `ASM` is specified, your database files are placed in Oracle ASM disk groups. Oracle Database automatically manages database file placement and naming. 	When `ASM` is specified, you can also specify the ASMSNMP password using the `-asmsnmpPassword` parameter. This parameter is optional. |
| `-sysPassword`  `SYS_user_password` | Optional | `SYS` user password for the new database. |
| `-systemPassword`  `SYSTEM_user_password` | Optional | `SYSTEM` user password for the new database. |
| `-templateFromCloud` | Optional | Creates a database using the clone template that is stored in Oracle Cloud Infrastructure. This option is supported only for Linux.  - `opcLibPath`: Directory in which the Oracle Database Cloud Backup Module for OCI is stored. The backup module is a system backup to tape (SBT) library that is used to integrate an on-premise database with Oracle Cloud Infrastructure. 	You must install the Oracle Database Cloud Backup Module for OCI before running this command. - `opcConfigFile`: Name, with complete location, of the Oracle Database Cloud Backup Module for OCI configuration file. This file is created when you install the backup module. - `rmanDecryptionPassword`: Password that must be used to decrypt the RMAN template file stored in Oracle Cloud Infrastructure. This is the same password that was used when creating an RMAN backup of the template.  See [Administering Oracle Database Backup Cloud Service](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=CSDBB-GUID-483BAC13-854B-4044-9569-0FAD313AD126) for information about installing and configuring the backup module. |
| `-useOMF`  `{true \| false}` | Optional | Specify `true` to use Oracle-Managed Files (OMF), else specify `false`. Default is `false`. |
| `-useWalletForDBCredentials`  `{true \| false}` | Optional | Specify `true` to use Oracle Wallet for database credentials, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters can be provided:  - `-dbCredentialsWalletLocation`: Directory location for the Oracle Wallet files. - `-dbCredentialsWalletPassword`: Password for the Oracle Wallet account.  Note:  If you are using Oracle Unified Directory (OUD), then the OUD passwords should be stored in the wallet using the following keys:  - `oracle.dbsecurity.walletPassword` - `oracle.dbsecurity.userDNPassword` |
| `-variables`  `variables_list` | Optional | A comma-separated list of `name=value` pairs for the variables in the database template. |
| `-variablesFile`  `variables_file` | Optional | Name of the variables file with the complete directory path in the database template. |

See Also:

[Oracle Database Sample Schemas](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=COMSC)

**Parent topic:** DBCA Silent Mode Commands

### createDuplicateDB

The `createDuplicateDB` command creates a duplicate of an Oracle database.

Prerequisites

The following are the prerequisites for using the `createDuplicateDB` command:

- The database to be duplicated is in the archivelog mode.
- If the database to be duplicated is in a remote server, then there must be connectivity from the system where DBCA is running to the remote server.

Syntax and Parameters

Use the `dbca` `-createDuplicateDB` command with the following syntax:

```
dbca -createDuplicateDB 
    -gdbName global_database_name 
    -primaryDBConnectionString easy_db_connection_string
    -sid database_system_identifier
    [-initParams initialization_parameters
        [-initParamsEscapeChar initialization_parameters_escape_character]]
    [-sysPassword SYS_user_password]
    [-policyManaged | -adminManaged]
    [-policyManaged
        -serverPoolName server_pool_names
        [-pqPoolName pq_pool_name]
        [-createServerPool new_server_pool_name
            [-pqPoolName new_pq_pool_name]
            [-force]
            [-pqCardinality pq_cardinality_of_the_new_server_pool]
            [-cardinality cardinality_of_the_new_server_pool]]]
    [-adminManaged]
    [-nodelist database_nodes_list]
    [-datafileDestination data_files_directory]
    [-recoveryAreaDestination recovery_files_directory
        [-recoveryAreaSize fast_recovery_area_size]]
    [-databaseConfigType {SINGLE | RAC | RACONENODE}
        [-RACOneNodeServiceName service_name_for_RAC_One_Node_database]]
    [-useOMF {true | false}]
    [-storageType {FS | ASM} 
        [-asmsnmpPassword ASMSNMP_password]
        -datafileDestination database_files_directory]
    [-createListener new_database_listener]
    [-createAsStandby 
        [-dbUniqueName db_unique_name_for_standby_database]]
    [-customScripts custom_sql_scripts_to_run_after_database_creation]
    [-useWalletForDBCredentials {true | false}
        -dbCredentialsWalletPassword wallet_account_password
        -dbCredentialsWalletLocation wallet_files_directory]
    [-configureTDE <true | false> ]
          [-primaryDBTdeWallet value]
          [-sourceTdeWalletPassword value]
          [-tdeWalletRoot tde_wallet_root_init_parameter]
          [-pdbTDEPassword pdb_tde_wallet_password]
          [-tdeWalletModeForPDB pdb_keystore_type]
          [-tdeAlgorithm TDE_algorithm]
          [-tdeWalletLoginType type_of_wallet_login]
          [-sourcePdbTDEPassword source_pdb_TDE_wallet_password]
          [-tdeWalletPassword TDE_wallet_password]
```

Table 19-6 createDuplicateDB Parameters

| Parameter | Required/Optional | Description |
| --- | --- | --- |
| `-gdbName` `global_database_name` | Required | Global database name of the duplicate database in the form database\_name.domain\_name. |
| `-primaryDBConnectionString` `easy_db_connection_string` | Required | Easy connection string to connect to the database to be duplicated. Easy connection string must be in the following format:  `"host[:port][/service_name][:server][/instance_name]"` |
| `-sid` `database_system_identifier` | Required | Database system identifier (SID) of the duplicate database.  The SID uniquely identifies the instance that runs the database. If it is not specified, then it defaults to the database name. |
| `-initParams`  `initialization_parameters_list` | Optional | A comma-separated list of `name=value` pairs of initialization parameter values for the database.  You can additionally provide the `-initParamsEscapeChar` parameter for using a specific escape character between multiple values of an initialization parameter. If an escape character is not specified, backslash (/) is used as the default escape character. |
| `-sysPassword`  `SYS_user_password` | Optional | `SYS` user password. |
| `-policyManaged` | Optional | Policy-managed database.  Note: You can specify either policy-managed database or administrator-managed database.  You can specify the following additional parameters:  - `-serverPoolName`: Specify the single server pool name when creating a new server pool or specify a comma separated list of existing server pools. - `-pqPoolName`: Specify the PQ pool name. - `-createServerPool`: Specify this parameter for creating a new server pool. 	- `-pqPoolName`: Specify the PQ pool name. 		- `-force`: Specify this parameter to create the server pool by force when adequate free servers are not available. 		- `-pqCardinality`: Specify the PQ cardinality of the new server pool. 		- `-cardinality`: Specify the cardinality of the new server pool. |
| `-adminManaged` | Optional | Administrator-managed database.  Note: You can specify either policy-managed database or administrator-managed database. |
| `-nodelist`  `database_nodes_list` | Optional | For administrator-managed database, specify database nodes separated by comma. |
| `-datafileDestination `  `data_files_directory` | Optional | Complete directory path for database data files. |
| `-recoveryAreaDestination`  `fast_recovery_area_directory` | Optional | Destination directory for the Fast Recovery Area, which is a backup and recovery area. Specify `NONE` to disable Fast Recovery Area.  Additionally, you can specify the Fast Recovery Area size in megabytes using the parameter `-recoveryAreaSize`. This parameter is optional. |
| `-databaseConfigType`  `{SINGLE \| RAC \| RACONENODE}` | Optional | Specify one of the following database configuration types:  - `SINGLE`: Single individual database. - `RAC`: Oracle RAC database. - `RACONENODE`: Oracle RAC One Node database. 	For Oracle RAC One Node database, you can specify the service name using the `-RACOneNodeServiceName` parameter. |
| `-useOMF`  `{true \| false}` | Optional | Specify `true` to use Oracle-Managed Files (OMF), else specify `false`. Default is `false`. |
| `-storageType`  `{FS \| ASM}` | Optional | Specify the storage type of either `FS` or `ASM`.  - `FS`: File system storage type. 	When `FS` is specified, your database files are managed by the file system of your operating system. You can specify the directory path where the database files are to be stored using a database template or the `-datafileDestination` parameter. Oracle Database can create and manage the actual files. - `ASM`: Oracle Automatic Storage Management (Oracle ASM) storage type. 	When `ASM` is specified, your database files are placed in Oracle ASM disk groups. Oracle Database automatically manages database file placement and naming. 	When `ASM` is specified, you can also specify the ASMSNMP password using the `-asmsnmpPassword` parameter. This parameter is optional. |
| `-createListener`  `new_database_listener` | Optional | Database listener to register the database in the form listener\_name:port. |
| `-createAsStandby` | Optional | Specifies that the duplicate database is a standby database for the primary database.  Optionally, use the `-dbUniqueName` parameter to set the unique database name for the standby database. If the `-dbUniqueName` parameter is not specified, then the value of the `DB_NAME` initialization parameter is used. |
| `-customScripts` `custom_sql_scripts_to_run_after_database_creation` | Optional | A comma separated list of SQL scripts that should be run after the duplicate database is created. The scripts are run in the order listed. |
| `-useWalletForDBCredentials`  `{true \| false}` | Optional | Specify `true` to use Oracle Wallet for database credentials, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters can be provided:  - `-dbCredentialsWalletPassword`: Password for the Oracle Wallet account. - `-dbCredentialsWalletLocation`: Directory location for the Oracle Wallet files.  Note:  If you are using Oracle Unified Directory (OUD), then the OUD passwords should be stored in the wallet using the following keys:  - `oracle.dbsecurity.walletPassword` - `oracle.dbsecurity.userDNPassword` |
| `configureTDE` | Optional | Specify true to configure TDE during the database creation. Only software wallets are supported. You can create a wallet for the entire CDB or for a PDB.  - `primaryDBTdeWallet`: This option is not applicable when creating a database. - `sourceTdeWalletPassword`: If the template that is being used is from a database that uses encryption, specify the password of the wallet in the source database. - `tdeWalletModeForPDB`: Specify UNITED to create a wallet for the entire CDB. Use ISOLATED to create a wallet for a PDB. - `tdeAlgorithm`: Algorithm used to encrypt data. Can be one of the following: 3DES168, AES128, AES192, AES256. - `tdeWalletLoginType`: Type of software wallet. PASSWORD or AUTO\_LOGIN or LOCAL\_AUTO\_LOGIN. - `tdeWalletLocation`: Location in which the TDE wallet is stored. - `tdeWalletPassword`: The password used to open the wallet. This parameter is mandatory.  Note: Isolated wallets are supported only in Oracle Cloud or Exadata environments. |

### createPluggableDatabase

The `createPluggableDatabase` command creates a pluggable database (PDB) in a multitenant container database (CDB).

Syntax and Parameters

Use the `dbca` `-createPluggableDatabase` command with the following syntax:

```
dbca -createPluggableDatabase 
   -pdbName name_of_the_pdb_to_create
   -sourceDB cdb_sid
   [-configureTDE {true | false} 
          [-primaryDBTdeWallet value]
          [-sourceTdeWalletPassword value]
          [-tdeWalletRoot tde_wallet_root_init_parameter]
          [-pdbTDEPassword pdb_tde_wallet_password]
          [-tdeWalletModeForPDB pdb_keystore_type]
          [-tdeAlgorithm TDE_algorithm]
          [-tdeWalletLoginType type_of_wallet_login]
          [-sourcePdbTDEPassword source_pdb_TDE_wallet_password]
          [-tdeWalletPassword TDE_wallet_password]]
   [-createAsClone {true | false}]
   [-createFromRemotePDB
      -pdbName name_of_the_local_pdb_to_create
      -sourceDB database_name_of_the_local_pdb
      -remotePDBName name_of_the_remote_pdb
      -remoteDBConnString db_connection_string_of_the_remote_pdb
      -sysDBAUserName name_of_the_sysdba_user
      -sysDBAPassword password_of_the_sysdba_user
      -dbLinkUsername name_of_the_dblink_user_of_the_remote_pdb
      -dbLinkUserPassword password_of_the_dblink_user_of_the_remote_pdb]
   [-createPDBFrom {DEFAULT | FILEARCHIVE | RMANBACKUP | USINGXML | PDB}
      [-pdbArchiveFile pdb_archive_file_name_with_directory_path]
      [-PDBBackUpfile pdb_backup_file_name_with_directory_path]
      [-PDBMetadataFile pdb_metadata_file_name_with_directory_path]
      [-pdbAdminUserName pdb_administrator_name]
      [-pdbAdminPassword pdb_administrator_password]
      [-createNewPDBAdminUser {true | false}]
      [-sourceFileNameConvert method_to_locate_pdb_files]
      [-fileNameConvert names_of_pdb_files]
      [-pdbStorageMAXSizeInMB maximum_storage_size_for_the_pdb_in_MB]
      [-pdbStorageMAXTempSizeInMB maximum_temporary_storage_size_for_the_pdb_in_MB]
      [-workArea directory_to_unzip_PDB_archive_files_for_FILEARCHIVE_option]
      [-copyPDBFiles  {true | false}]
      [-sourcePDB name_of_the_pdb_to_clone]
   [-createUserTableSpace {true | false)]
   [-customScripts custom_sql_scripts_to_run_after_PDB_creation]
   [-dvConfiguration {true | false}
      -dvUserName Database_Vault_owner_name
      -dvUserPassword Database_Vault_owner_password
      [-dvAccountManagerName Database_Vault_account_manager_name]
      [-dvAccountManagerPassword Database_Vault_account_manager_password]]
   [-encryptPDBTablespaces ALL|tablespace_name:{true | false}]
    [-encryptTablespaces ALL|tablespace_name:{true | false}]
   [-lbacsysPassword LBACSYS_user_password]
   [-pdbDatafileDestination pdb_data_files_directory]
   [-pdbStorageMAXSizeInMB maximum_storage_size_for_the_pdb_in_MB]
   [-pdbStorageMAXTempSizeInMB maximum_temporary_storage_size_for_the_pdb_in_MB]
   [-pdbTimezone {{+|-}hh:mi|time_zone_region}]
   [-pdbUseMultipleBackup number_of_pdb_backups_to_create]
   [-registerWithDirService {true | false} 
      -dirServiceUserName directory_service_user_name
      [-dirServicePassword directory_service_user_password]
      [-databaseCN directory_service_database_common_name]
      [-dirServiceCertificatePath certificate_file_directory_path]
      [-dirServiceUser active_directory_account_user_name]
      [-walletPassword wallet_password]]
   [-useMetaDataFileLocation {true | false}]
   [-useWalletForDBCredentials {true | false}
      -dbCredentialsWalletPassword wallet_account_password
      -dbCredentialsWalletLocation wallet_files_directory]
```

Table 19-7 createPluggableDatabase Parameters

| Parameter | Required/Optional | Description |
| --- | --- | --- |
| `-pdbName`  `name_of_the_pdb_to_create` | Required | Name of the new PDB to create.  Note: For Oracle RAC databases, the PDB name must be unique in the cluster. |
| `-sourceDB`  `cdb_sid` | Required | The database system identifier (SID) of the CDB. |
| `configureTDE` | Optional | Specify `true` to configure TDE during the database creation. Only software wallets are supported. You can create a wallet for the entire CDB or for a PDB.  - `primaryDBTdeWallet`: This option is not applicable when creating a database. - `sourceTdeWalletPassword`: If the template that is being used is from a database that uses encryption, or if you are duplicating a database, specify the password of the wallet in the source database. - `tdeWalletModeForPDB`: Specify `UNITED` to create a wallet for the entire CDB. Use `ISOLATED` to create a wallet for a PDB. - `tdeAlgorithm`: Algorithm used to encrypt data. Can be one of the following: 3DES168, AES128, AES192, AES256. - `tdeWalletLoginType`: Type of software wallet. `PASSWORD` or `AUTO_LOGIN` or `LOCAL_AUTO_LOGIN`. - `tdeWalletLocation`: Location in which the TDE wallet is stored. - `tdeWalletPassword`: The password used to open the wallet. This parameter is mandatory.  Note: Isolated wallets are supported only in Oracle Cloud or Exadata environments. |
| `-createAsClone`  `{true \| false}` | Optional | Specify `true` if the files you plan to use to create the new PDB are the same files that were used to create an existing PDB. Specifying `true` ensures that Oracle Database generates unique PDB DBID, GUID, and other identifiers expected for the new PDB.  Specify `false`, the default, if the files you plan to use to create the new PDB are not the same files that were used to create an existing PDB. |
| `-createFromRemotePDB` | Optional | Create a PDB by cloning a remote PDB.  Specify the following parameters:  - `-pdbName`: Name of the local PDB to create. - `-sourceDB`: Database name of the local PDB. - `-remotePDBName`: Name of the remote PDB to clone. - `-remoteDBConnString`: Database connection string of the remote PDB. - `-sysDBAUserName`: Name of the SYSDBA user. - `-sysDBAPassword`: Password of the SYSDBA user. - `-dbLinkUsername`: Name of the database link user of the remote PDB. - `-dbLinkUserPassword`: Password of the database link user of the remote PDB.  Note:  - The database user of the local CDB must have the `CREATE PLUGGABLE DATABASE` privileges in the root container. - The remote CDB must be in the local undo mode. - The remote PDB must be in the archivelog mode. - The database user of the remote PDB to which the database link connects to must have the `CREATE PLUGGABLE                                  DATABASE` and `CREATE SESSION` privileges. |
| `-createPDBFrom`  `{DEFAULT \| FILEARCHIVE \| RMANBACKUP \| USINGXML \| PDB}` | Optional | Specify `DEFAULT` to create the PDB from the CDB's seed. When you specify `DEFAULT`, the following additional parameters are required:  - `-pdbAdminUserName`: The user name of the PDB's local administrator. - `-pdbAdminPassword`: The password for the PDB's local administrator.  Specify `FILEARCHIVE` to create the PDB from an unplugged PDB's files. When you specify `FILEARCHIVE`, the following additional parameters are required:  - `-pdbArchiveFile`: Complete path and name for unplugged PDB's archive file. 	The archive file contains all of the files for the PDB, including its XML metadata file and its data files. Typically, the archive file has a `.gz` extension. - `-createNewPDBAdminUser`: Specify `true` to create a new PDB administrator or `false` to avoid creating a new PDB administrator. - `-workArea`: Specify the directory location where the PDB archive files need to be unzipped.  Specify `RMANBACKUP` to create the PDB from a Recovery Manager (RMAN) backup. When you specify `RMANBACKUP`, the following additional parameters are required:  - `-pdbBackUpfile`: Complete path and name for the PDB backup file. - `-pdbMetadataFile`: Complete path and name for the PDB's XML metadata file.  Specify `USINGXML` to create the PDB from an unplugged PDB's XML metadata file. When you specify `USINGXML`, the following additional parameter is required:  - `-pdbMetadataFile`: Complete path and name for the PDB's XML metadata file.  Specify `PDB` to create a new PDB by cloning an existing PDB. When you specify `PDB`, the following additional parameter is required:  - `-sourcePDB`: Name of an existing PDB to clone.  Specify the following optional parameters, if required:  - `-sourceFileNameConvert`: This parameter specifies how to locate PDB files listed in the PDB XML metadata file. 	See `SOURCE_FILE_NAME_CONVERT` clause of the `CREATE PLUGGABLE DATABASE` statement described in [Oracle Multitenant Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=MULTI-GUID-CD341EDB-8B27-484B-9C55-CF206E2983DD). - `-fileNameConvert`: This parameter specifies the names of the PDB’s files. 	See `FILE_NAME_CONVERT` clause of the `CREATE PLUGGABLE DATABASE` statement described in [Oracle Multitenant Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=MULTI-GUID-39D2F826-7460-4439-B410-29E16C0CA0B1). - `-pdbStorageMAXSizeInMB`: Specify the maximum storage size for the PDB in megabytes. 	See information about PDB storage described in [Oracle Multitenant Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/multi&id=MULTI-GUID-59F42929-7237-4371-8934-921B46DB6F31). - `-pdbStorageMAXTempSizeInMB`: Specify the maximum temporary storage size for the PDB in megabytes. - `-copyPDBFiles {true \| false}`: Specify `true` if the PDB data files need to be copied, else specify `false`. |
| `-createUserTableSpace`  `{true \| false}` | Optional | Specify `true` if a default user tablespace needs to be created in the new PDB. |
| `-customScripts`  `lcustom_sql_scripts_to_run_after_PDB_creation` | Optional | Specify a list of custom SQL scripts to run after the PDB creation. |
| `-dvConfiguration`  `{true \| false}` | Optional | Specify `true` to enable and configure Database Vault, else specify `false`. Default is `false`.  When `true` is specified, the following additional Database Vault parameters are required:  - `-dvUserName`: Specify the Database Vault owner name. - `-dvUserPassword`: Specify Database Vault owner password. - `-dvAccountManagerName`: Specify a separate Database Vault account manager name. - `-dvAccountManagerPassword`: Specify the Database Vault account manager password. |
| `-encryptPDBTablespaces` | Optional | If you have configured TDE using `-configureTDE`, you can use this parameter to encrypt all of some of the tablespaces at the PDB and CDB level.  Specify the following additional parameters: - `ALL`: Encrypt all tablespaces - `tablespace_name`: Comma-separated list of tablespaces with a value of `TRUE` or `FALSE` for each |
| `-encryptTablespaces` | Optional | If you have configured TDE using `-configureTDE`, you can use this parameter to encrypt all or some of the tablespaces at the CDB level.  Specify the following additional parameters: - `ALL`: Encrypt all tablespaces - `tablespace_name`: Comma-separated list of tablespaces with a value of `TRUE` or `FALSE` for each |
| `-lbacsysPassword`  `LBACSYS_user_password` | Optional | Specify the `LBACSYS` user password if you want to configure OLS with a directory service. |
| `-pdbDatafileDestination`  `pdb_data_files_directory` | Optional | Compete directory path to the new PDB data files.  When this parameter is not specified, either Oracle Managed Files or the `PDB_FILE_NAME_CONVERT` initialization parameter specifies how to generate the names and locations of the files. If you use both Oracle Managed Files and the `PDB_FILE_NAME_CONVERT` initialization parameter, then Oracle Managed Files takes precedence.  When this parameter is not specified, Oracle Managed Files is not enabled, and the `PDB_FILE_NAME_CONVERT` initialization parameter is not set, by default a path to a subdirectory with the name of the PDB in the directory for the root's files is used. |
| `-pdbStorageMAXSizeInMB`  `maximum_storage_size_for_the_pdb_in_MB` | Optional | Specify the maximum storage size for the PDB in megabytes. |
| `-pdbStorageMAXTempSizeInMB`  `maximum_temporary_storage_size_for_the_pdb_in_MB` | Optional | Specify the maximum temporary storage size for the PDB in megabytes. |
| `-pdbTimezone` `{{+\|-}hh:mi\|time_zone_region}` | Optional | Use this parameter to specify the time zone of the PDB.  You can specify the time zone in two ways: - By specifying a displacement from UTC (Coordinated Universal Time—formerly Greenwich Mean Time). The valid range of hh:mi is -12:00 to +14:00. - By specifying a time zone region. To see a listing of valid time zone region names, query the `TZNAME` column of the `V$TIMEZONE_NAMES` dynamic performance view. |
| `-pdbUseMultipleBackup`  `number_of_pdb_backups_to_create` | Optional | Specify the number of PDB backups to create. |
| `-registerWithDirService`  `{true \| false}` | Optional | Specify `true` to register the PDB with a Lightweight Directory Access Protocol (LDAP) service, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters are required:  - `-dirServiceUserName`: User name for the LDAP service. - `-dirServicePassword`: Password for the LDAP service. - `-dirServiceUser`: User name for the Active Directory account. - `-dirServiceCertificatePath`: Certificate file path of the directory service. - `-databaseCN`: Common name of the directory service database. - `-walletPassword`: Password for the database wallet. |
| `-useMetaDataFileLocation`  `{true \| false}` | Optional | Specify `true` to use the data file path defined in XML metadata file within a PDB archive when extracting data files.  Specify `false`, the default, to not use the data file path defined in XML metadata file within a PDB archive when extracting data files. |
| `-useWalletForDBCredentials`  `{true \| false}` | Optional | Specify `true` to use Oracle Wallet for database credentials, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters can be provided:  - `-dbCredentialsWalletLocation`: Directory location for the Oracle Wallet files. - `-dbCredentialsWalletPassword`: Password for the Oracle Wallet account.  Note:  If you are using Oracle Unified Directory (OUD), then the OUD passwords should be stored in the wallet using the following keys:  - `oracle.dbsecurity.walletPassword` - `oracle.dbsecurity.userDNPassword` |

**Parent topic:** DBCA Silent Mode Commands

### createTemplateFromDB

The `createTemplateFromDB` command creates a database template from an existing database.

Syntax and Parameters

Use the `dbca -createTemplateFromDB` command with the following syntax:

```
dbca -createTemplateFromDB 
   -sourceDB source_database_sid
   -templateName new_database_template_name
   -sysDBAUserName SYSDBA_user_name
   -sysDBAPassword SYSDBA_user_password
   [-maintainFileLocations {true | false}]
   [-connectionString easy_connect_string]
   [-useWalletForDBCredentials {true | false}
       -dbCredentialsWalletPassword wallet_account_password
       -dbCredentialsWalletLocation wallet_files_directory]
```

Table 19-8 createTemplateFromDB Parameters

| Parameter | Required/Optional | Description |
| --- | --- | --- |
| `-sourceDB` `source_database_sid` | Required | The source database system identifier (SID). |
| `-templateName` `new_database_template_name` | Required | Name of the new database template. |
| `-sysDBAUserName` `SYSDBA_user_name` | Required | User name of a user that has `SYSDBA` privileges. |
| `-sysDBAPassword` `SYSDBA_user_password` | Required | Password of the user that has `SYSDBA` privileges. |
| `-maintainFileLocations` `{true \| false}` | Optional | Specify `true` to use the file locations of the database in the template.  Specify `false`, the default, to use different file locations in the template. The file locations are determined by Oracle Flexible Architecture (OFA). |
| `-connectionString` `easy_connect_string` | Optional | Easy connect string for connecting to a remote database in the following format:  `"host[:port][/service_name][:server][/instance_name]"` |
| `-useWalletForDBCredentials`  `{true \| false}` | Optional | Specify `true` to use Oracle Wallet for database credentials, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters can be provided:  - `-dbCredentialsWalletPassword`: Password for the Oracle Wallet account. - `-dbCredentialsWalletLocation`: Directory location for the Oracle Wallet files.  Note:  If you are using Oracle Unified Directory (OUD), then the OUD passwords should be stored in the wallet using the following keys:  - `oracle.dbsecurity.walletPassword` - `oracle.dbsecurity.userDNPassword` |

**Parent topic:** DBCA Silent Mode Commands

### createTemplateFromTemplate

The `createTemplateFromTemplate` command creates a database template from an existing database template.

Syntax and Parameters

Use the `dbca -createTemplateFromTemplate` command with the following syntax:

```
dbca -createTemplateFromTemplate 
    -sourcetemplateName existing_template_name 
    -templateName new_template_name 
    [-variables variables_list]
    [-characterSet database_character_set]
    [-nationalCharacterSet database_national_character_set]
    [-recoveryAreaDestination fast_recovery_area_directory]
        -recoveryAreaSize fast_recovery_area_size]
    [-datafileDestination data_files_directory]
    [-useOMF {true | false}]
    [-datafileJarLocation database_backup_files_directory]
    [-memoryPercentage percentage_of_total_memory_to_assign_to_oracle_database]
    [-totalMemory total_memory_to_assign_to_oracle_database]
    [-dbOptions database_options]
    [-variablesFile variables_file]
    [-redoLogFileSize redo_log_file_size]
    [-initParams initialization_parameters_list]
        [-initParamsEscapeChar escape_character_for_initialization_parameters]
    [-storageType {FS | ASM} 
        [-asmsnmpPassword ASMSNMP_password]
        -datafileDestination data_files_directory]
    [-enableArchive {true | false} 
         -archiveLogMode {AUTO | MANUAL}
         -archiveLogDest archive_logs_directory
    [-memoryMgmtType {AUTO | AUTO_SGA | CUSTOM_SGA}]
    [-useWalletForDBCredentials {true | false}
         -dbCredentialsWalletPassword wallet_account_password
         -dbCredentialsWalletLocation wallet_files_directory]
```

Table 19-9 createTemplateFromTemplate Parameters

| Parameter | Required/Optional | Description |
| --- | --- | --- |
| `-sourceTemplateName`  `existing_template_name` | Required | Name of an existing database template in the default location or the complete path to a database template that is not in the default location. |
| `-templateName`  `new_template_name` | Required | Name for a new database template. |
| `-variables`  `variables_list` | Optional | A comma-separated list of `name=value` pairs for the variables in the database template. |
| `-characterSet`  `database_character_set` | Optional | Character set of the database. |
| `-nationalCharacterSet`  `database_national_character_set` | Optional | National character set of the database. |
| `-recoveryAreaDestination`  `fast_recovery_area_directory` | Optional | Directory path for the Fast Recovery Area, which is a backup and recovery area. |
| `-datafileDestination`  `data_files_directory` | Optional | Directory path for the data files. |
| `-useOMF`  `{true \| false}` | Optional | Specify `true` to use Oracle-Managed Files (OMF), else specify `false`. |
| `-datafileJarLocation`  `database_backup_files_directory` | Optional | Location of the database offline backup (for clone database creation only).  The data files for the seed database are stored in compressed RMAN backup format in a file with a.dfb extension. |
| `-memoryPercentage`  `percentage_of_total_memory_to_assign_to_oracle_database`  or  `-totalMemory`  `total_memory_to_assign_to_oracle_database` | Optional | Specify either `-memoryPercentage` or `-totalMemory`.  - `-memoryPercentage` 	The percentage of physical memory that can be used by the database. - `-totalMemory` 	The amount of physical memory in megabytes that can be used by the database. |
| `-dbOptions`  `database_options` | Optional | Specify database options as comma separated list of `name:value` pairs.  Example: `JSERVER:true,DV:false` |
| `-variablesFile`  `variables_file` | Optional | File name with complete directory path to the file that contains the variables and their values in the database template. |
| `-redoLogFileSize`  `redo_log_file_size` | Optional | Size of each online redo log file in megabytes. |
| `-initParams`  `initialization_parameters_list` | Optional | A comma-separated list of `name=value` pairs of the database initialization parameters and their values. |
| `-storageType`  `{FS \| ASM}` | Optional | Specify `FS` for file system and `ASM` for Oracle Automatic Storage Management (Oracle ASM) system.  When `FS` is specified, your database files are managed by the file system of your operating system. You specify the directory path where the database files are to be stored using the `-datafileDestination` parameter.  When `ASM` is specified, your database files are placed in the Oracle ASM disk groups. Oracle Database automatically manages database file placement and naming. You also specify the `ASMSNMP` password for ASM monitoring using the `-asmsnmpPassword` parameter. |
| `-enableArchive`  `{true \| false}` | Optional | Specify `true` to enable log file archive. Default is `false`.  When `true` is specified, the following additional parameters can be provided:  - `-archiveLogMode {AUTO \| MANUAL}`: Specify either the automatic archive mode (`AUTO`) or the manual archive mode (`MANUAL`). Default is automatic archive mode (`AUTO`). - `-archiveLogDest`: Directory path for storing the archive log files. |
| `-memoryMgmtType`  `{AUTO \| AUTO_SGA \| CUSTOM_SGA}` | Optional | Specify one of the following memory management types:  - `AUTO`: Automatic memory management for SGA and PGA. - `AUTO_SGA`: Automatic shared memory management for SGA. - `CUSTOM_SGA`: Manual shared memory management for SGA.  Note: If the total physical memory of a database instance is greater than 4 GB, then you cannot specify the Automatic Memory Management option `AUTO` during the database installation and creation. Oracle recommends that you specify the Automatic Shared Memory Management option `AUTO_SGA` in such environments. |
| `-useWalletForDBCredentials`  `{true \| false}` | Optional | Specify `true` to use Oracle Wallet for database credentials, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters can be provided:  - `-dbCredentialsWalletPassword`: Password for the Oracle Wallet account. - `-dbCredentialsWalletLocation`: Directory location for the Oracle Wallet files.  Note:  If you are using Oracle Unified Directory (OUD), then the OUD passwords should be stored in the wallet using the following keys:  - `oracle.dbsecurity.walletPassword` - `oracle.dbsecurity.userDNPassword` |

**Parent topic:** DBCA Silent Mode Commands

### deleteDatabase

The `deleteDatabase` command deletes a database.

Syntax and Parameters

Use the `dbca` `-deleteDatabase` command with the following syntax:

```
dbca -deleteDatabase 
   -sourceDB database_name_or_sid
   [-sysDBAUserName SYSDBA_user_name]
   [-sysDBAPassword SYSDBA_user_password]
   [-forceArchiveLogDeletion]
   [-deRegisterEMCloudControl
     [-omsHost Oracle_Management_Server_host_name
      -omsPort Oracle_Management_Server_port_number
      -emUser EM_administrator_user_name
      -emPassword EM_administrator_password]]
   [-unregisterWithDirService {true | false}
      -dirServiceUserName directory_service_user_name
      [-dirServicePassword directory_service_user_password
      [-walletPassword wallet_password]]
   [-sid database_system_identifier]
   [-useWalletForDBCredentials {true | false}
       -dbCredentialsWalletPassword wallet_account_password
       -dbCredentialsWalletLocation wallet_files_directory]
```

Table 19-10 deleteDatabase Parameters

| Parameter | Required/Optional | Description |
| --- | --- | --- |
| `-sourceDB` `database_name_or_sid` | Required | Database unique name for an Oracle RAC database or database system identifier (SID) for a single instance database. |
| `-sysDBAUserName` `SYSDBA_user_name` | Optional | User name of the user having the `SYSDBA` privileges. |
| `-sysDBAPassword` `SYSDBA_password` | Optional | Password of the user having the `SYSDBA` privileges. |
| `-forceArchiveLogDeletion` | Optional | Specify this parameter to delete the database archive logs. |
| `-deRegisterEMCloudControl` | Optional | Specify this parameter along with the following parameters to unregister the database with Enterprise Manager Cloud Control:  - `-omsHost`: Oracle Management Server host name. - `-omsPort`: Oracle Management Server port number. - `-emUser`: User name for Enterprise Manager administrator. - `-emPassword`: Password for Enterprise Manager administrator. |
| `-unregisterWithDirService {true \| false}` | Optional | Specify this parameter along with the following parameters to unregister the database with the directory service:  - `-dirServiceUserName`: User name for the directory service. - `-dirServicePassword`: Password for the directory service user. - `-walletPassword`: Password for the database wallet. |
| `-sid` `database_system_identifier` | Optional | Database system identifier (SID). |
| `-useWalletForDBCredentials`  `{true \| false}` | Optional | Specify `true` to use Oracle Wallet for database credentials, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters can be provided:  - `-dbCredentialsWalletLocation`: Directory location for the Oracle Wallet files. - `-dbCredentialsWalletPassword`: Password for the Oracle Wallet account.  Note:  If you are using Oracle Unified Directory (OUD), then the OUD passwords should be stored in the wallet using the following keys:  - `oracle.dbsecurity.walletPassword` - `oracle.dbsecurity.userDNPassword` |

**Parent topic:** DBCA Silent Mode Commands

### deleteInstance

The `deleteInstance` command deletes a database instance from an administror-managed Oracle RAC database.

Syntax and Parameters

Use the `dbca` `-deleteInstance` command with the following syntax:

```
dbca -deleteInstance 
   -gdbName global_database_name
   -instanceName database_instance_name
   [-nodeName database_instance_node_name]
   [-updateDirService {true | false}
      -dirServiceUserName directory_service_user_name
      -dirServicePassword directory_service_user_password]
   [-sysDBAUserName SYSDBA_user_name]
   [-sysDBAPassword SYSDBA_user_password]
   [-useWalletForDBCredentials {true | false}
      -dbCredentialsWalletPassword wallet_account_password
      -dbCredentialsWalletLocation wallet_files_directory]
```

Table 19-11 deleteInstance Parameters

| Parameter | Required/Optional | Description |
| --- | --- | --- |
| `-gdbName` `global_database_name` | Required | Global database name in the form database\_name.domain\_name. |
| `-instanceName` `database_instance_name` | Required | Database instance name. |
| `-nodeName` `node_name_of_database_instance` | Optional | Node name of the database instance. |
| `-sysDBAUserName` `SYSDBA_user_name` | Optional | User name of the database user having the `SYSDBA` privileges. |
| `-sysDBAPassword` `SYSDBA_user_password` | Optional | Password of the database user having the `SYSDBA` privileges. |
| `-updateDirService`  `{true \| false}` | Optional | Specify `true` to unregister the database with the directory service, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters are required:  - `-dirServiceUserName`: User name for the directory service. - `—dirServicePassword`: Password for the directory service user. |
| `-useWalletForDBCredentials`  `{true \| false}` | Optional | Specify `true` to use Oracle Wallet for database credentials, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters can be provided:  - `-dbCredentialsWalletPassword`: Password for the Oracle Wallet account. - `-dbCredentialsWalletLocation`: Directory location for the Oracle Wallet files.  Note:  If you are using Oracle Unified Directory (OUD), then the OUD passwords should be stored in the wallet using the following keys:  - `oracle.dbsecurity.walletPassword` - `oracle.dbsecurity.userDNPassword` |

**Parent topic:** DBCA Silent Mode Commands

### deletePluggableDatabase

The `deletePluggableDatabase` command deletes a PDB.

Syntax and Parameters

Use the `dbca -deletePluggableDatabase` command with the following syntax:

```
dbca -deletePluggableDatabase 
   -sourceDB cdb_sid
   -pdbName pdb_name
   [-unregisterWithDirService {true | false} ]
      -dirServiceUserName directory_service_user_name
      [-dirServicePassword directory_service_user_password ]
      [-walletPassword wallet_password]
   [-useWalletForDBCredentials {true | false} ]
       -dbCredentialsWalletPassword wallet_account_password
       [-dbCredentialsWalletLocation wallet_files_directory]
```

Table 19-12 deletePluggableDatabase Parameters

| Parameter | Required/Optional | Description |
| --- | --- | --- |
| `-sourceDB` `cdb_sid` | Required | The database system identifier (SID) of the CDB. |
| `-pdbName` `pdb_name` | Required | Name of the PDB to delete. |
| `-useWalletForDBCredentials`  `{true \| false}` | Optional | Specify `true` to use Oracle Wallet for database credentials, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters must be provided:  - `-dbCredentialsWalletPassword` (Optional): Password for the Oracle Wallet account. If you omit this parameter, DBCA prompts for the password. - `-dbCredentialsWalletLocation`: Directory location for the Oracle Wallet files.  Note:  If you are using Oracle Unified Directory (OUD), then the OUD passwords should be stored in the wallet using the following keys:  - `oracle.dbsecurity.walletPassword` - `oracle.dbsecurity.userDNPassword` |
| `-unregisterWithDirService {true \|                                     false}` | Optional | Specify this parameter along with the following parameters to unregister the database with the directory service:  - `-dirServiceUserName`: User name for the directory service. - `-dirServicePassword`: Password for the directory service user. - `-walletPassword`: Password for the database wallet. |

**Parent topic:** DBCA Silent Mode Commands

### deleteTemplate

The `deleteTemplate` command deletes a database template.

Syntax and Parameters

Use the `dbca -deleteTemplate` command with the following syntax:

```
dbca -deleteTemplate 
   -templateName name_of_an_existing_database_template
   [-useWalletForDBCredentials {true | false}
      -dbCredentialsWalletPassword wallet_account_password
      -dbCredentialsWalletLocation wallet_files_directory]
   [-templateFromCloud 
      -opcLibPath OPC_library_path
      -opcConfigFile OPC_config_file_name
      [-rmanDecryptionPassword rman_decryption_password]]
```

Table 19-13 deleteTemplate Parameters

| Parameter | Required/Optional | Description |
| --- | --- | --- |
| `-templateName`  `name_of_an_existing_database_template` | Required | Name of an existing database template to delete. |
| `-templateFromCloud` | Optional | Indicates that the template is a Cloud template.  - `opcLibPath`: Provide the directory containing the `odbsrmt.py` script for the delete template operation or provide the directory containing `libopc.so`. - `opcConfigFile`: Name, with complete location, of the Oracle Database Cloud Backup Module for OCI configuration file. - `rmanDecryptionPassword`: Password that must be used to decrypt the RMAN template file stored in Oracle Cloud Infrastructure. This is the same password that was used when creating an RMAN backup of the template. |
| `-useWalletForDBCredentials`  `{true \| false}` | Optional | Specify `true` to use Oracle Wallet for database credentials, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters can be provided:  - `-dbCredentialsWalletPassword`: Password for the Oracle Wallet account. - `-dbCredentialsWalletLocation`: Directory location for the Oracle Wallet files.  Note:  If you are using Oracle Unified Directory (OUD), then the OUD passwords should be stored in the wallet using the following keys:  - `oracle.dbsecurity.walletPassword` - `oracle.dbsecurity.userDNPassword` |

**Parent topic:** DBCA Silent Mode Commands

### executePrereqs

The `executePrereqs` command executes the prerequisites checks and reports the results. This command can be used to check the environment before running `dbca` to create a database.

Syntax and Parameters

Use the `dbca -executePrereqs` command with the following syntax:

```
dbca -executePrereqs 
   -databaseConfigType {SINGLE | RAC | RACONENODE}
        [-RACOneNodeServiceName RAC_node_service_name]
   [-nodelist database_nodes_list]
```

Table 19-14 executePrereqs Parameters

| Parameter | Required/Optional | Description |
| --- | --- | --- |
| `-databaseConfigType {SINGLE \| RAC \| RACONENODE}` | Required | Specify one of the following database configuration types:  - `SINGLE`: Single individual database. - `RAC`: Oracle RAC database. - `RACONENODE`: Oracle RAC One Node database. 	For Oracle RAC One Node database, you can specify the service name using the `-RACOneNodeServiceName` parameter. |
| `-nodelist`  `database_nodes_list` | Optional | List of database nodes separated by comma. |

**Parent topic:** DBCA Silent Mode Commands

### generateScripts

The `generateScripts` command generates scripts, which can be used to create a database.

Syntax and Parameters

Use the `dbca` `-generateScripts` command with the following syntax:

```
dbca -generateScripts 
    -templateName database_template_name 
    -gdbName global_database_name 
    [-sid database_system_identifier]
    [-scriptDest sql_scripts_directory]
    [-createAsContainerDatabase {true | false}
        [-numberOfPDBs number_of_pdbs_to_create]
        [-pdbName pdb_name]
        [-pdbStorageMAXSizeInMB maximum_storage_size_of_the_pdb]
        [-pdbStorageMAXTempSizeInMB maximum_temporary_storage_size_of_the_pdb]
        [-useLocalUndoForPDBs {true | false}]
        [-pdbAdminPassword pdb_administrator_password]
        [-pdbOptions pdb_options]
    [-sysPassword SYS_user_password]
    [-systemPassword SYSTEM_user_password]
    [-emConfiguration {DBEXPRESS | CENTRAL | BOTH | NONE}
        [-dbsnmpPassword DBSNMP_user_password]
        [-omsHost EM_Management_Server_host_name]
        [-omsPort EM_Management_Server_port_number]
        [-emUser EM_administrator_name]
        [-emPassword EM_administrator_password]
        [-emExpressPort EM_Express_port]
        [-emExpressPortAsGlobalPort EM_Express_global_port]]
    [-dvConfiguration {true | false}
        -dvUserName Database_Vault_owner_user_name
        -dvUserPassword Database_Vault_owner_user_password
        [-dvAccountManagerName Database_Vault_account_manager_name
        -dvAccountManagerPassword Database_Vault_account_manager_password]]
    [-olsConfiguration {true | false}
        [-configureWithOID configure_with_OID_flag]]
    [-datafileDestination data_files_directory]
    [-redoLogFileSize maximum_redo_log_file_size_in_MB]
    [-recoveryAreaDestination fast_recovery_area_directory
        [-recoveryAreaSize fast_recovery_area_size]]
    [-datafileJarLocation data_files_backup_directory]
    [-responseFile response_file_directory]
    [-storageType {FS | ASM} 
        [-asmsnmpPassword ASMSNMP_password]
        -datafileDestination data_files_directory]
    [-runCVUChecks {true | false}]
    [-nodelist database_nodes_list]
    [-enableArchive {true | false} 
        [-archiveLogMode {AUTO | MANUAL}]
        [-archiveLogDest archive_log_files_directory]]
    [-memoryMgmtType {AUTO | AUTO_SGA | CUSTOM_SGA}]
    [-createListener new_database_listener_to_register_the_database_with]
    [-useOMF {true | false}]
    [-dbOptions database_options]
    [-customScripts custom_sql_scripts_to_run_after_database_creation]
    [-policyManaged | -adminManaged]
    [-policyManaged
        -serverPoolName server_pool_names
        [-pqPoolName pq_pool_name]
        [-createServerPool new_server_pool_name]
            [-pqPoolName new_pq_pool_name]
            [-force]
            [-pqCardinality pq_cardinality_of_the_new_server_pool]
            [-cardinality cardinality_of_the_new_server_pool]]
    [-adminManaged]
    [-databaseConfigType {SINGLE | RAC | RACONENODE}
            [-RACOneNodeServiceName service_name_for_RAC_one_node_database]]
    [-characterSet database_character_set]
    [-nationalCharacterSet database_national_character_set]
    [-registerWithDirService {true | false} 
        [-dirServiceUserName directory_service_user_name]
        [-dirServicePassword directory_service_user_password]
        [-databaseCN database_common_name]
        [-dirServiceCertificatePath certificate_file_path]
        [-dirServiceUser directory_service_user_name]
        [-ldapDirectoryAccessType ldap_directory_access_type]
        [-useSYSAuthForLDAPAccess use_sys_user_for_ldap_access_flag]
        [-walletPassword wallet_password]]
    [-listeners list_of_listeners_to_register_the_database_with]
    [-variablesFile variables_file]
    [-variables variables_list]
    [-initParams initialization_parameters_list
        [-initParamsEscapeChar initialization_parameters_escape_character]]
    [-sampleSchema {true | false}]
    [-memoryPercentage percentage_of_total_memory_to_assign_to_the_database]
    [-totalMemory total_memory_to_assign_to_the_database_in_MB]
    [-databaseType {MULTIPURPOSE | DATA_WAREHOUSING | OLTP}]
    [-useWalletForDBCredentials {true | false}
        -dbCredentialsWalletPassword wallet_account_password
        -dbCredentialsWalletLocation wallet_files_directory]
    [-configureTDE <true | false> ]
          [-primaryDBTdeWallet value]
          [-sourceTdeWalletPassword value]
          [-tdeWalletRoot tde_wallet_root_init_parameter]
          [-pdbTDEPassword pdb_tde_wallet_password]
          [-tdeWalletModeForPDB pdb_keystore_type]
          [-tdeAlgorithm TDE_algorithm]
          [-tdeWalletLoginType type_of_wallet_login]
          [-sourcePdbTDEPassword source_pdb_TDE_wallet_password]
          [-tdeWalletPassword TDE_wallet_password]
```

Table 19-15 generateScripts Parameters

| Parameter | Required/Optional | Description |
| --- | --- | --- |
| `-templateName` `database_template_name` | Required | Name of an existing database template in the default location or the complete path of a template that is not in the default location. |
| `-gdbName` `global_database_name` | Required | Global database name in the form database\_name.domain\_name. |
| `-sid`  `database_system_identifier` | Optional | Database system identifier (SID).  The SID uniquely identifies the instance that runs the database. If it is not specified, then it defaults to the database name. |
| `-scriptDest` `scripts_directory` | Optional | Complete directory path to store the scripts. |
| `-createAsContainerDatabase`  `{true \| false}` | Optional | Specify `true` to create a CDB. Specifying `false` is not supported starting with Oracle Database Release 21c.  When `true` is specified, the following optional parameters can be provided:  - `-numberOfPDBs`: Number of PDBs to create. Default is 0 (zero). - `-pdbName`: Name of each PDB. A number is appended to each PDB name if `-numberOfPDBs` value is greater than 1. This parameter must be specified if `-numberOfPDBs` value is greater than 0 (zero). - `-pdbStorageMAXSizeInMB`: Maximum storage size for a PDB in megabytes. - `-pdbStorageMAXTempSizeInMB`: Maximum temporary storage size for a PDB in megabytes. - `-useLocalUndoForPDBs {true \| false}`: Flag indicating whether local undo should be used for the PDBs. - `-pdbAdminPassword`: PDB administrator password. - `-pdbOptions`: PDB options in the form of comma separated list. Each option must be specified in the `name:value` format. 	Example: `JSERVER:true,DV:false` |
| `-sysPassword`  `SYS_user_password` | Optional | `SYS` user password for the new database. |
| `-systemPassword`  `SYSTEM_user_password` | Optional | `SYSTEM` user password for the new database. |
| `-emConfiguration`  `{DBEXPRESS \| CENTRAL \| BOTH \| NONE}` | Optional | Enterprise Manager configuration settings.  Oracle Enterprise Manager Database Express (EM Express) is deprecated, and will be removed in a future Oracle Database release.  When `DBEXPRESS`, `CENTRAL`, or `BOTH` is specified, specify the following additional parameters:  - `-dbsnmpPassword`: DBSNMP user password. - `-omsHost`: Oracle Management Server host name. - `-omsPort`: Oracle Management Server port number. - `-emUser`: User name for Enterprise Manager administrator. - `-emPassword`: Password for Enterprise Manager administrator. - `-emExpressPort`: Enterprise Manager Express port number. - `-emExpressPortAsGlobalPort`: Enterprise Manager Express global port number. |
| `-dvConfiguration`  `{true \| false}` | Optional | Specify `true` to enable and configure Database Vault, else specify `false`. Default is `false`.  When `true` is specified, the following additional Database Vault parameters are required:  - `-dvUserName`: Database Vault owner name. - `-dvUserPassword`: Database Vault owner password. - `-dvAccountManagerName`: Database Vault account manager name. - `-dvAccountManagerPassword`: Database Vault account manager password. |
| `-olsConfiguration`  `{true \| false}` | Optional | Specify `true` to enable and configure Oracle Label Security (OLS), else specify `false`. Default is `false`.  When `true` is specified, you can additionally specify the `-configureWithOID` parameter to configure Oracle Label Security (OLS) with Oracle Internet Directory (OID). This parameter is optional. |
| `-datafileDestination`  `data_files_directory` | Optional | Complete path to the location of the database's data files. |
| `-redoLogFileSize`  `maximum_size_of_online_redo_log` | Optional | Size of each online redo log file in megabytes. |
| `-recoveryAreaDestination`  `fast_recovery_area_directory` | Optional | Directory for the Fast Recovery Area, which is a backup and recovery area. Specify `NONE` to disable the Fast Recovery Area.  Additionally, you can specify the Fast Recovery Area size in megabytes using the parameter `-recoveryAreaSize`. This parameter is optional. |
| `-datafileJarLocation`  `data_files_backup_directory` | Optional | Directory of the database backup data files in a compressed RMAN backup format (files with.dfb extensions). |
| `-responseFile`  `response_file_directory` | Optional | Directory path of the response file. |
| `-storageType`  `{FS \| ASM}` | Optional | Specify the storage type of either `FS` or `ASM`.  - `FS`: File system storage type. 	When `FS` is specified, your database files are managed by the file system of your operating system. You can specify the directory path where the database files are to be stored using a database template or the `-datafileDestination` parameter. Oracle Database can create and manage the actual files. - `ASM`: Oracle Automatic Storage Management (Oracle ASM) storage type. 	When `ASM` is specified, your database files are placed in Oracle ASM disk groups. Oracle Database automatically manages database file placement and naming. 	When `ASM` is specified, you can also specify the ASMSNMP password using the `-asmsnmpPassword` parameter. This parameter is optional. |
| `-runCVUChecks`  `{true \| false}` | Optional | Specify `true` to run Cluster Verification Utility checks periodically for Oracle RAC databases, else specify `false`. Default is `false`. |
| `-nodelist`  `database_nodes_list` | Optional | List of database nodes separated by comma. |
| `-enableArchive`  `{true \| false}` | Optional | Specify `true` to enable log file archive, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters can be provided:  - `-archiveLogMode {AUTO \| MANUAL}`: Specify either the automatic archive mode or the manual archive mode. Default is automatic archive mode. - `-archiveLogDest`: Directory for storing the archive log files. |
| `-memoryMgmtType`  `{AUTO \| AUTO_SGA \| CUSTOM_SGA}` | Optional | Specify one of the following memory management types:  - `AUTO`: Automatic memory management for SGA and PGA. - `AUTO_SGA`: Automatic shared memory management for SGA. - `CUSTOM_SGA`: Manual shared memory management for SGA.  Note: If the total physical memory of a database instance is greater than 4 GB, then you cannot specify the Automatic Memory Management option `AUTO` during the database installation and creation. Oracle recommends that you specify the Automatic Shared Memory Management option `AUTO_SGA` in such environments. |
| `-createListener`  `new_database_listener` | Optional | Database listener to register the database with in the form listener\_name:port. |
| `-useOMF`  `{true \| false}` | Optional | Specify `true` to use Oracle-Managed Files (OMF), else specify `false`. |
| `-dbOptions`  `database_options` | Optional | Specify database options as a comma separated list of `name:value` pairs.  Example: `JSERVER:true,DV:false` |
| `-customScripts`  `custom_sql_scripts_list` | Optional | Specify a comma separated list of SQL scripts that need to be run after the database creation. The scripts are run in the order they are listed. |
| `-policyManaged` | Optional | Policy-managed database.  You can specify the following additional parameters:  - `-serverPoolName`: Specify the single server pool name when creating a new server pool or specify a comma separated list of existing server pools. - `-pqPoolName`: Specify the PQ pool name. - `-createServerPool`: Specify this parameter for creating a new server pool. 	- `-pqPoolName`: Specify the PQ pool name. 		- `-force`: Specify this parameter to create the server pool by force when adequate free servers are not available. 		- `-pqCardinality`: Specify the PQ cardinality of the new server pool. 		- `-cardinality`: Specify the cardinality of the new server pool. |
| `-adminManaged` | Optional | Administrator-managed database. |
| `-databaseConfigType`  `{SINGLE \| RAC \| RACONENODE}` | Optional | Specify one of the following database configuration types:  - `SINGLE`: Single individual database. - `RAC`: Oracle RAC database. - `RACONENODE`: Oracle RAC One Node database. 	For Oracle RAC One Node database, you can specify the service name using the `-RACOneNodeServiceName` parameter. |
| `-characterSet`  `database_character_set` | Optional | Character set of the database. |
| `-nationalCharacterSet`  `database_national_character_set` | Optional | National character set of the database. |
| `-registerWithDirService `  `{true \| false}` | Optional | Specify `true` to register with a Lightweight Directory Access Protocol (LDAP) service, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters are required:  - `-dirServiceUserName`: User name for the LDAP service. - `-dirServicePassword`: Password for the LDAP service. - `-databaseCN`: Database common name. - `-dirServiceCertificatePath`: Directory service certificate file path. - `-dirServiceUser`: Directory service user name. - `-ldapDirectoryAccessType {PASSWORD \| SSL}`: LDAP directory access type. - `-useSYSAuthForLDAPAccess {true \| false}`: Specify whether to use SYS user authentication for LDAP acces. - `-walletPassword`: Password for the database wallet. |
| `-listeners`  `listeners_list` | Optional | A comma-separated list of listeners for the database. |
| `-variablesFile`  `variables_file` | Optional | Directory path to the file that contains the variables and their values for the database template. |
| `-variables`  `variables_list` | Optional | A comma-separated list of `name=value` pairs of variables for the database template. |
| `-initParams`  `initialization_parameters_list` | Optional | A comma-separated list of `name=value` pairs of initialization parameter values of the database.  You can additionally provide the `-initParamsEscapeChar` parameter for using a specific escape character between multiple values of an initialization parameter. If an escape character is not specified, backslash (/) is used as the default escape character. |
| `-sampleSchema`  `{true \| false}` | Optional | Specify `true` to include the `HR` sample schema (`EXAMPLE` tablespace) in your database, else specify `false`. Default is `false`.  Oracle guides and educational materials contain examples based on the sample schemas. Oracle strongly recommends that you do not install the sample schemas in a production database. |
| `-memoryPercentage`  `percentage_of_total_memory_assigned_to_the_database` | Optional | The percentage of physical memory that can be used by the database. |
| `-totalMemory`  `total_memory_assigned_to_the_database_in_MB` | Optional | Total amount of physical memory, in megabytes, that can be used by the database. |
| `-databaseType`  `{MULTIPURPOSE \| DATA_WAREHOUSING \| OLTP}` | Optional | Specify `MULTIPURPOSE` if the database is for both OLTP and data warehouse purposes.  Specify `DATA_WAREHOUSING` if the primary purpose of the database is a data warehouse.  Specify `OLTP` if the primary purpose of the database is online transaction processing. |
| `-useWalletForDBCredentials`  `{true \| false}` | Optional | Specify `true` to use Oracle Wallet for database credentials, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters can be provided:  - `-dbCredentialsWalletLocation`: Directory location for the Oracle Wallet files. - `-dbCredentialsWalletPassword`: Password for the Oracle Wallet account.  Note:  If you are using Oracle Unified Directory (OUD), then the OUD passwords should be stored in the wallet using the following keys:  - `oracle.dbsecurity.walletPassword` - `oracle.dbsecurity.userDNPassword` |
| `configureTDE` | Optional | Specify true to configure TDE during the database creation. Only software wallets are supported. You can create a wallet for the entire CDB or for a PDB.  - `primaryDBTdeWallet`: This option is not applicable when creating a database. - `sourceTdeWalletPassword`: If the template that is being used is from a database that uses encryption, or if you are duplicating a database, specify the password of the wallet in the source database. - `tdeWalletModeForPDB`: Specify UNITED to create a wallet for the entire CDB. Use ISOLATED to create a wallet for a PDB. - `tdeAlgorithm`: Algorithm used to encrypt data. Can be one of the following: 3DES168, AES128, AES192, AES256. - `tdeWalletLoginType`: Type of software wallet. PASSWORD or AUTO\_LOGIN or LOCAL\_AUTO\_LOGIN. - `tdeWalletLocation`: Location in which the TDE wallet is stored. - `tdeWalletPassword`: The password used to open the wallet. This parameter is mandatory.  Note: Isolated wallets are supported only in Oracle Cloud or Exadata environments. |

**Parent topic:** DBCA Silent Mode Commands

### relocatePDB

The `relocatePDB` command relocates a PDB from a remote CDB to a local CDB.

Prerequisites

The following are the prerequisites for running the `relocatePDB` command:

- The database user in the local PDB must have the `CREATE PLUGGABLE DATABASE` privilege in the local CDB root container.
- The remote CDB must be in the local undo mode.
- The remote and local PDBs must be in the archivelog mode.
- The database user in the remote PDB that the database link connects to must have the `CREATE PLUGGABLE DATABASE`, `SESSION`, and `SYSOPER` privileges.
- The local and remote PDBs must have the same options installed, or the remote PDB must have a subset of the options installed on the local PDB.

Syntax and Parameters

Use the `dbca` `-relocatePDB` command with the following syntax:

```
dbca -relocatePDB 
   -pdbName name_of_the_local_pdb_to_create
   -sourceDB database_name_of_the_local_pdb
   -remotePDBName name_of_the_remote_pdb_to_relocate
   -remoteDBConnString db_connection_string_of_the_remote_pdb
   -sysDBAUserName name_of_the_sysdba_user
   -sysDBAPassword password_of_the_sysdba_user
   -dbLinkUsername name_of_the_dblink_user_of_the_remote_pdb
   -dbLinkUserPassword password_of_the_dblink_user_of_the_remote_pdb
```

Table 19-16 relocatePDB Parameters

| Parameter | Required/Optional | Description |
| --- | --- | --- |
| `-pdbName` `name_of_the_local_pdb_to_create` | Required | Name of the local PDB to create after relocating the remote PDB. |
| `-sourceDB` `database_name_of_the_local_pdb` | Required | Database name of the local PDB. |
| `-remotePDBName` `name_of_the_remote_pdb_to_relocate` | Required | Name of the remote PDB to relocate. |
| `-remoteDBConnString` `db_connection_string_of_the_remote_pdb` | Required | Database connection string of the remote PDB. |
| `-sysDBAUserName` `name_of_the_sysdba_user` | Required | Name of the SYSDBA user. |
| `-sysDBAPassword` `password_of_the_sysdba_user` | Required | Password of the SYSDBA user. |
| `-dbLinkUsername` `name_of_the_dblink_user_of_the_remote_pdb` | Required | Name of the database link user of the remote PDB. |
| `-dbLinkUserPassword` `password_of_the_dblink_user_of_the_remote_pdb` | Required | Password of the database link user of the remote PDB. |

**Parent topic:** DBCA Silent Mode Commands

### unplugDatabase

The `unplugDatabase` command unplugs a pluggable database (PDB) from a multitenant container database (CDB).

Syntax and Parameters

Use the `dbca` `-unplugDatabase` command with the following syntax:

```
dbca -unplugDatabase 
   -sourceDB cdb_sid
   -pdbName pdb_name
   [-unregisterWithDirService {true | false}
      -dirServiceUserName directory_service_user_name
      -dirServicePassword directory_service_user_password
      -walletPassword wallet_password]
   [-archiveType {TAR | RMAN | NONE}
      [-rmanParallelism parallelism_integer_value]
      [-pdbArchiveFile pdb_archive_file_directory]
      [-PDBBackUpfile pdb_backup_file_directory]
      [-PDBMetadataFile pdb_metadata_file_directory]
      [-rmanParallelism parallelism_integer_value]]
   [-useWalletForDBCredentials {true | false}
      -dbCredentialsWalletPassword wallet_account_password
      -dbCredentialsWalletLocation wallet_files_directory]
```

Table 19-17 unplugDatabase Parameters

| Parameter | Required/Optional | Description |
| --- | --- | --- |
| `-sourceDB` `cdb_sid` | Required | The database system identifier (SID) of the CDB. |
| `-pdbName` `pdb_name` | Required | Name of the PDB. |
| `-archiveType` `{TAR \| RMAN \| NONE}` | Optional | Specify `TAR` to store the unplugged PDB files in a tar file.  Specify `RMAN` to store the unplugged PDB files in an RMAN backup.  Specify `NONE` to store the unplugged PDB files without using a tar file or an RMAN backup.  Specify any of the following parameters:  - `-pdbArchiveFile`: Specify absolute file path and name for the PDB Archive file. - `-pdbBackUpfile`: Specify absolute file path and name for the PDB backup file when archive type is `RMAN`. specify comma separated file paths, if there are multiple backups to be taken when creating the PDB. - `-pdbMetadataFile`: Specify absolute file path and name for the PDB metadata file when archive type is `RMAN` or `NONE`. - `-rmanParallelism`: Specify the RMAN parallelism integer value. |
| `-unregisterWithDirService` `{true \| false}` | Optional | Specify `true` to unregister the PDB from the LDAP service, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters are required:  - `-dirServiceUserName`: User name for the LDAP service. - `-dirServicePassword`: Password for the LDAP service user. - `-walletPassword`: Password for the database wallet. |
| `-useWalletForDBCredentials`  `{true \| false}` | Optional | Specify `true` to use Oracle Wallet for database credentials, else specify `false`. Default is `false`.  When `true` is specified, the following additional parameters can be provided:  - `-dbCredentialsWalletPassword`: Password for the Oracle Wallet account. - `-dbCredentialsWalletLocation`: Directory location for the Oracle Wallet files.  Note:  If you are using Oracle Unified Directory (OUD), then the OUD passwords should be stored in the wallet using the following keys:  - `oracle.dbsecurity.walletPassword` - `oracle.dbsecurity.userDNPassword` |

**Parent topic:** DBCA Silent Mode Commands