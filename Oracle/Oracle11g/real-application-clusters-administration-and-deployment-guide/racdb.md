---
title: Oracle RAC Database (RACDB) Plug-in
book: Real Application Clusters Administration and Deployment Guide
doc_id: E41960-04
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/rac.112/e41960/racdb.htm
tags:
  - oracle
  - 11g
  - real-application-clusters-administration-and-deployment-guide
---

## C Oracle RAC Database (RACDB) Plug-in

The Oracle Real Application Clusters (Oracle RAC) RACDB introspection plug-in examines Oracle Clusterware and Oracle RAC Database components and captures their metadata.

This appendix includes the following Oracle RAC Database introspection plug-in information:

Versions Supported

This plug-in supports Oracle Database 11g release 2 (11.2).

Oracle RAC Database Introspection Parameters

Table C-1 lists the introspection parameters for the Oracle RAC Database introspection plug-in:

Table C-1 Oracle RAC Database Plug-in Introspection Parameters

| Parameter | Description |
| --- | --- |
| ``` asmHome ``` | This parameter is required if Oracle Automatic Storage Management is used as the storage type and it is installed in a separate Oracle home. |
| ``` crsHome ``` | The `ORACLE_HOME` of the Oracle Clusterware to be introspected. |
| ``` dbHome ``` | The `ORACLE_HOME` of the Oracle Database to be introspected. |
| ``` globalDbName ``` | The global database name of the Oracle Database to be introspected. |
| ``` shutdownDBOK ``` | This flag that must be passed to approve the database reboot. |
| ``` sysDBAUserName ``` | Database account with SYSDBA privileges. This parameter is required only if operating system authentication is disabled for the current database. |

Oracle RAC Database Introspection Password Parameters

Table C-2 lists the introspection password parameters for the Oracle RAC Database plug-in. When performing introspection using the `abctl` tool, a prompt is shown to enter values for these parameters. Oracle Virtual Assembly Builder Studio provides password fields for these parameters.

Table C-2 Oracle RAC Database Plug-in Introspection Parameters (Prompted During Introspection)

| Parameter | Description |
| --- | --- |
| ``` rootPassword ``` | The `rootPassword` parameter is required only if you want to change the permissions of the `ORACLE_HOME` files to make capturing of file sets possible. |
| ``` sysDBAPassword ``` | Password for the `sysDBAUserName` user. This parameter is required only if operating system authentication is disabled for the current database. |

Reference System Prerequisites

The Oracle Clusterware stack must be running during introspection.

Requirements

The following requirements apply to Oracle RAC Database:

The base system image operating system version must match the version of the reference system.

Resulting Artifact Type

A single appliance.

Wiring

For an Oracle RAC Database 11g release 2 (11.2), a single input is created on the Oracle RAC Database appliance.

For an Oracle RAC Database prior to 11g release 2 (11.2), inputs are created on the Oracle RAC Database appliance for each listener or port directive found in the configuration.

Wiring Properties

For an Oracle RAC Database 11g release 2 (11.2), the input endpoint has two editable properties— `scan-name` and `global-db-name` —and two non-editable properties— `protocol` and `port` —which indicate what sort of output can be connected to the input.

For an Oracle RAC Database prior to 11g release 2 (11.2), the input endpoint has a editable property— `global-db-name` —and two non-editable properties— `protocol` and `port`.

Oracle Database Appliance Properties

Assemblies with an Oracle Database appliance have user properties (Table C-3) and system properties (Table C-4).

Table C-3 Oracle RAC Database User Properties

| Name | Type | Req'd | Default | Description |
| --- | --- | --- | --- | --- |
| ``` asm-password ``` | String | false | none | Password for SYSASM account. |
| ``` cluster-name ``` | String | false | new\_cluster | Name for cluster (only applies to Oracle Database prior to 11g release 2 (11.2)). |
| ``` db-account-password ``` | Password | true | none | The password for database accounts SYS, SYSTEM, SYSMAN, and DBSNMP. |

Table C-4 Oracle RAC Database System Properties

| Name | Type | Req'd | Default | Description |
| --- | --- | --- | --- | --- |
| ``` CRS_BASE ``` | String | false | none | The Oracle Clusterware base path. |
| ``` CRS_HOME ``` | String | false | none | The Oracle Clusterware home path. |
| ``` CRS_OWNER ``` | String | false | grid | The name of the operating system user who will be the owner of the Oracle Clusterware home. |
| ``` CRS_GROUP ``` | String | false | oinstall | The name of the operating system user group of the owner of the Oracle Clusterware home. |
| ``` CRS_ORACLE_GROUPS ``` | String | false | oinstall | The OSDBA, OSOPER, and OSASM groups. |
| ``` VOTING_DISKS_LOCATIONS ``` | String | false | none | Locations of voting disks (only for file system storage type for Oracle Clusterware files). |
| ``` VOTING_DISKS_REDUNDANCY ``` | String | false | none | Voting disks redundancy (only for file system storage type for Oracle Clusterware files). |
| ``` OCR_DISKS_LOCATIONS ``` | String | false | none | Locations of Oracle Cluster Registry disks (only for file system storage type for Oracle Clusterware files). |
| ``` OCR_DISKS_REDUNDANCY ``` | String | false | none | Oracle Cluster Registry disks redundancy (only for file system storage type for Oracle Clusterware files). |
| ``` SCAN_PORT ``` | String | false | 1521 | Port for SCAN listener. |
| ``` CRS_STORAGE_TYPE ``` | String | false | none | Storage type for Oracle Clusterware files as per reference system. |
| ``` CRS_VERSION ``` | String | false | none | Version of Oracle Clusterware software on reference system. |
| ``` CRS_ASM_DISK_GROUP_NAME ``` | String | false | OVMOCRVD | Name of the Oracle ASM disk group storing Oracle Clusterware files. |
| ``` CRS_ASM_DISCOVERY_STRING ``` | String | false | ``` /dev/raw/ovmocrvd* ``` | Path to discover all data Oracle ASM disks. |
| ``` CRS_ASM_DISK_GROUP_REDUNDANCY ``` | String | false | NORMAL | Oracle ASM disk group level of redundancy. |
| ``` CRS_ASM_DISKS ``` | String | false | ``` /dev/raw/ovmocrvd0, /dev/raw/ovmocrvd1, /dev/raw/ovmocrvd2 ``` | Paths of the disks that belong to Oracle ASM disk group storing Oracle Clusterware files. |
| ``` ASM_BASE ``` | String | false | none | Oracle ASM ORACLE\_BASE path. |
| ``` ASM_HOME ``` | String | false | none | Oracle ASM ORACLE\_HOME path. |
| ``` ASM_OWNER ``` | String | false | grid | The operating system user who owns the Oracle ASM ORACLE\_HOME. |
| ``` DATA_ASM_DISCOVERY_STRING ``` | String | false | ``` /dev/raw/asm* ``` | Path to discover all data Oracle ASM disks. |
| ``` DATA_ASM_DISK_GROUP_NAME ``` | String | false | none | Name of the data Oracle ASM disk group. |
| ``` DATA_ASM_DISK_GROUP_REDUNDANCY ``` | String | false | none | Data Oracle ASM disk group level of redundancy. |
| ``` DATA_ASM_DISKS ``` | String | false | none | Paths of the disks that belong to data Oracle ASM disk group. |
| ``` RECOVERY_ASM_DISCOVERY_STRING ``` | String | false | ``` /dev/raw/asm* ``` | Path to discover all recovery Oracle ASM disks. |
| ``` RECOVERY_ASM_DISK_GROUP_NAME ``` | String | false | none | Name of the recovery Oracle ASM disk group. |
| ``` RECOVERY_ASM_DISK_GROUP_REDUNDANCY ``` | String | false | none | Recovery Oracle ASM disk group level of redundancy. |
| ``` RECOVERY_ASM_DISKS ``` | String | false | none | Paths of the disks that belong to the recovery Oracle ASM disk group. |
| ``` RECOVERY_STORAGE_TYPE ``` | String | false | none | Storage type for database recovery. |
| ``` DATA_STORAGE_TYPE ``` | String | false | none | Storage type for database as per reference system. |
| ``` RECOVERY_STORAGE_TYPE ``` | String | false | none | Storage type for database recovery files as per reference system. |
| ``` DB_USING_ASM ``` | String | false | none | Set to true if either the database or recovery files are stored on Oracle ASM as per reference system. |
| ``` DB_VERSION ``` | String | false | none | Version of Oracle Database software on reference system. |

Extensions of the Plug-in

None.

Supported Template Types

The supported template type is Oracle Enterprise Linux.