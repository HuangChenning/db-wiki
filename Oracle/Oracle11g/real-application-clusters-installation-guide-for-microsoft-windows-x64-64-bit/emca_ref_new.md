---
title: Oracle Enterprise Manager Configuration Assistant Reference
book: Real Application Clusters Installation Guide for Microsoft Windows x64 (64-Bit)
doc_id: E48195-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e48195/emca_ref_new.htm
tags:
  - oracle
  - 11g
  - real-application-clusters-installation-guide-for-microsoft-windows-x64-64-bit
---

## G Oracle Enterprise Manager Configuration Assistant Reference

Oracle Enterprise Manager Configuration Assistant (EMCA) provides a command-line interface for configuring Database Control. This appendix contains the following topics:

See Also:

[Section 6.7, "Managing Database Control Using EMCA"](srvpool.md) for more information using EMCA

## G.1 About EMCA

This section contains topics that relate to using the EMCA command-line interface.

### G.1.1 Overview

The primary method for configuring an existing Oracle Database 11g release 2 (11.2) database to be managed with Oracle Enterprise Manager Database Control is to use DBCA, but EMCA can be used if a nongraphical user interface is preferred.

Caution:

During the database configuration using EMCA, the database is unavailable and users cannot connect to the database or perform operations on the database.

### G.1.2 Operational Notes

This section contains information about how to use the EMCA command-line interface.

#### G.1.2.1 Usage Information

Every EMCA command can be used in Oracle RAC environments, and certain commands are applicable only in cluster setups. To perform cluster commands using EMCA, use the `-cluster` flag that is available in almost every EMCA operational mode.

EMCA commands are of the form:

```
emca [operation] [mode] [flags] [parameters]
```

For information about the current cluster configuration, you can run the following command:

```
emca -displayConfig dbcontrol –cluster
```

#### G.1.2.2 EMCA Parameters

Depending upon the parameters you include on the EMCA command line, EMCA prompts you for additional information required to configure Database Control.

Each EMCA command can include optional parameters to specify the additional information required by EMCA. Parameters used with EMCA are of the form \[- `parameterName` `parameterValue`\]. Multiple parameters can be used in combination at the command line. Table G-1 lists the optional parameters that can be used with EMCA.

Note:

You can view a list of the available parameters by entering `emca -help` at the command line.

Table G-1 EMCA Optional Command-Line Parameters

| Parameter | Description |
| --- | --- |
| `-respFile` | The path of an input file that lists parameters for EMCA to use while performing its configuration operation. For more information, see [Section 6.6.2, "Using EMCA in Silent Mode With an Input File."](srvpool.md). |
| `-SID` | Database system identifier. |
| `-PORT` | Port number for the listener servicing the database. |
| `-ORACLE_HOME` | Database Oracle home, as an absolute path. |
| `-LISTENER_OH` | Oracle home from where the listener is running. If the listener is running from an Oracle home other than the one on which the database is running, then the parameter LISTENER\_OH must be specified. |
| `-HOST_USER` | Host computer user name (for automatic backup). |
| `-HOST_USER_PWD` | Host computer user password (for automatic backup). |
| `-BACKUP_SCHEDULE` | Schedule in the form of "HH:MM" (for daily automatic backups). |
| `-EMAIL_ADDRESS` | E-mail address for notifications. |
| `-MAIL_SERVER_NAME` | Outgoing mail server, or Simple Mail Transfer Protocol (SMTP) server, for notifications. |
| `-ASM_OH` | Oracle Automatic Storage Management (Oracle ASM) home. |
| `-ASM_SID` | System identifier for Oracle ASM instance. |
| `-ASM_PORT` | Port number for the listener servicing the Oracle ASM instance. |
| `-ASM_USER_ROLE` | User role for connecting to the Oracle ASM instance. |
| `-ASM_USER_NAME` | User name for connecting to the Oracle ASM instance. |
| `-ASM_USER_PWD` | Password for connecting to the Oracle ASM instance. |
| `-DBSNMP_PWD` | Password for DBSNMP user. |
| `-SYSMAN_PWD` | Password for SYSMAN user. |
| `-SYS_PWD` | Password for SYS user. |
| `-SRC_OH` | Oracle home of the database with Oracle Enterprise Manager configuration to be upgraded or restored. |
| `-DBCONTROL_HTTP_PORT` | The port you use to display the Database Control console in your web browser. For more information, see [Section 6.7.3, "Changing the Ports Used by Database Control."](srvpool.md). |
| `-AGENT_PORT` | The Oracle Management Agent port for Database Control. For more information, see [Section 6.7.3, "Changing the Ports Used by Database Control."](srvpool.md). |
| `-RMI_PORT` | The RMI port for Database Control. For more information, see [Section 6.7.3, "Changing the Ports Used by Database Control."](srvpool.md). |
| `-JMS_PORT` | The JMS port for Database Control. For more information, see [Section 6.7.3, "Changing the Ports Used by Database Control."](srvpool.md). |
| `-CLUSTER_NAME` | Cluster name (for cluster databases). |
| `-DB_UNIQUE_NAME` | Database unique name (for cluster databases). |
| `-SERVICE_NAME` | Database service name (for cluster databases). |
| `-EM_NODE` | Node from which Database Control console is to be run (for cluster databases). For more information, see [Section 6.7.1, "Changing the Database Control Implementation for Your Oracle RAC Database."](srvpool.md). |
| `-EM_NODE_LIST` | Comma-separated list of nodes for agent-only configurations, uploading data to `–EM_NODE`. For more information, see [Section 6.7.1, "Changing the Database Control Implementation for Your Oracle RAC Database."](srvpool.md). |

#### G.1.2.3 Using Tool/Utility Help

To see a list of EMCA options, start EMCA using any of the following commands:

```
emca -h
emca --h
emca -help
emca --help
```

These commands display the Help message for the EMCA utility. These `help` commands also list the command arguments described in Table G-2, and the optional parameters described in Table G-1.

## G.2 EMCA Command Reference

This section describes the commands available with the EMCA utility.

Table G-2 EMCA Commands

| Command | Description |
| --- | --- |
| addInst | Configures Oracle Enterprise Manager for a new cluster instance of a database or Oracle ASM storage. |
| addNode | Configures Oracle Enterprise Manager for a new cluster instance of a database or Oracle ASM storage. |
| config all db | Configures both Database Control and central agent management for a database. |
| config centralAgent | Configures central agent management for a database or an Oracle ASM instance. |
| config dbcontrol db | Configures Database Control for a database. |
| deconfig all db | Deconfigures both Database Control and central agent management for a database. |
| deconfig centralAgent | Deconfigures central agent management for a database or an Oracle ASM instance. |
| deconfig dbcontrol db | Deconfigures Database Control for a database. |
| deleteInst | Deconfigures Oracle Enterprise Manager for a specific instance of a cluster database or Oracle ASM storage. |
| deleteNode | Deconfigures Oracle Enterprise Manager for a node getting deleted. |
| displayConfig dbcontrol | Displays information about the current deployment configuration of Database Control in a cluster environment. |
| reconfig dbcontrol | Reconfigures the Database Control deployment for a cluster database. |
| reconfig ports | Explicitly reassigns Database Control ports. |
| restore | Restores the current release of Oracle Enterprise Manager configuration to an earlier release. |
| upgrade | Upgrades the configuration of an release version of Oracle Enterprise Manager to the current release. |
| version | Prints the release information associated with EMCA. |

### G.2.1 addInst

Use this command to configure Oracle Enterprise Manager for a new cluster instance of a database or Oracle ASM.

#### G.2.1.1 Syntax

There are two forms for this command, depending on whether you are adding an Oracle database instance or an Oracle ASM instance:

```
emca -addInst db [-silent] [parameters]

emca -addInst asm [-silent] [parameters]
```

#### G.2.1.2 Parameters/Options

Table G-3 addInst Options

| Parameter | Description |
| --- | --- |
| `db` | Performs the operation for a database (including cluster databases).  Use this option for databases that use Oracle ASM to store the data files. If a database is using Oracle ASM, then all the EMCA configuration commands (except for `-upgrade` and `-restore`) detect this automatically and apply the changes to both the database and Oracle ASM instances. |
| `asm` | Performs the operation for an Oracle ASM-only instance (including cluster Oracle ASM instances). |
| `-silent` | Performs the operation without prompting for additional information.  If this mode is specified, then all the required parameters must be entered at the command line or specified in an input file using the `–respFile` argument. See [Section 6.6.2, "Using EMCA in Silent Mode With an Input File"](srvpool.md) for more information. |
| `parameters` | See Table G-1, "EMCA Optional Command-Line Parameters". |

### G.2.2 addNode

Use this command to configure Oracle Enterprise Manager for a new cluster instance of a database or Oracle ASM.

For more information, see [Section 6.3, "Understanding EMCA and Enterprise Manager Control with Oracle RAC."](srvpool.md)

#### G.2.2.1 Syntax

```
emca -addNode db [-silent] [parameters]

emca -addNode asm [-silent] [parameters]
```

#### G.2.2.2 Parameters

Table G-4 addNode Options

| Parameter | Description |
| --- | --- |
| `db` | Performs the operation for a database (including cluster databases).  Use this option for databases that use Oracle ASM to store the data files. If a database is using Oracle ASM, then all the EMCA configuration commands (except for `-upgrade` and `-restore`) detect this automatically and apply the changes to both the database and Oracle ASM instances. |
| `asm` | Performs the operation for an Oracle ASM-only instance (including cluster Oracle ASM instances). |
| `-silent` | Performs the operation without prompting for additional information.  If this mode is specified, then all the required parameters must be entered at the command line or specified in an input file using the `–respFile` argument. See [Section 6.6.2, "Using EMCA in Silent Mode With an Input File"](srvpool.md) for more information. |
| `parameters` | See Table G-1, "EMCA Optional Command-Line Parameters". |

#### G.2.2.3 Examples

This command is discussed further in [Section 6.7.2, "Updating Database Control Configuration When Adding and Removing Nodes."](srvpool.md)

### G.2.3 config all db

Use this command to configure both Database Control and Oracle Management Agent for a database. Options include creating (or re-creating) the Database Control repository, configuring automatic backups, and performing these operations on a cluster database.

This operation configures the database so that it can be centrally managed by the Oracle Enterprise Manager 10g Grid Control console. To use this option, you must have previously installed the Oracle Management Service component of Oracle Enterprise Manager on a network host. In addition, the Oracle Management Agent must be installed on the host where you run the database.

#### G.2.3.1 Syntax

```
emca -config all db [-repos (create | recreate)] [-cluster] [-silent] 
     [-backup] [parameters]
```

#### G.2.3.2 Parameters

Table G-5 config all db Options

| Parameter | Description |
| --- | --- |
| `-repos create` | Creates a new Oracle Management Repository. |
| `-repos recreate` | Deletes the current Oracle Management Repository and then re-creates a new one. |
| `-cluster` | Performs the operation for a cluster database or Oracle ASM instance. |
| `-silent` | Performs the operation without prompting for additional information.  If this mode is specified, then all the required parameters must be entered at the command line or specified in an input file using the `–respFile` argument. See [Section 6.6.2, "Using EMCA in Silent Mode With an Input File"](srvpool.md) for more information. |
| `parameters` | See Table G-1, "EMCA Optional Command-Line Parameters". |

### G.2.4 config centralAgent

Use this command to configure the Management Agent for a database or an Oracle ASM instance. Options include performing this operation on a cluster environment.

This operation configures the database so that it can be centrally managed by the Oracle Enterprise Manager 10g Grid Control console. To use this option, you must have previously installed the Oracle Management Service component of Oracle Enterprise Manager on a network host. In addition, the Oracle Management Agent must be installed on the host where you run the database.

#### G.2.4.1 Syntax

```
emca -config centralAgent (db | asm) [-cluster] [-silent] [parameters]
```

#### G.2.4.2 Parameters

Table G-6 config centralAgent Options

| Parameter | Description |
| --- | --- |
| `db` | Performs the operation for a database (including cluster databases).  Use this option for databases that use Oracle ASM to store the data files. If a database is using Oracle ASM, then all the EMCA configuration commands (except for `-upgrade` and `-restore`) detect this automatically and apply the changes to both the database and Oracle ASM instances. |
| `asm` | Performs the operation for an Oracle ASM-only instance (including cluster Oracle ASM instances). |
| `-cluster` | Performs the operation for a cluster database or Oracle ASM instance. |
| `-silent` | Performs the operation without prompting for additional information.  If this mode is specified, then all the required parameters must be entered at the command line or specified in an input file using the `–respFile` argument. See [Section 6.6.2, "Using EMCA in Silent Mode With an Input File."](srvpool.md) for more information. |
| `parameters` | See Table G-1, "EMCA Optional Command-Line Parameters". |

### G.2.5 config dbcontrol db

Use this command to configure Oracle Enterprise Manager Database Control for a database. Options include creating (or re-creating) the Oracle Management Repository, configuring automatic backups, and performing these operations on a cluster database.

#### G.2.5.1 Syntax

```
emca -config dbcontrol db [-repos (create | recreate)] [-cluster] [-silent]
     [-backup] [parameters]
```

#### G.2.5.2 Options

Table G-7 config dbcontrol Options

| Parameter | Description |
| --- | --- |
| `-repos create` | Creates a new Management Repository. |
| `-repos recreate` | Deletes the current Management Repository and then creates a new one. |
| `-cluster` | Performs the operation for a cluster database or Oracle ASM instance. |
| `-silent` | Performs the operation without prompting for additional information.  If this mode is specified, then all the required parameters must be entered at the command line or specified in an input file using the `–respFile` argument. See [Section 6.6.2, "Using EMCA in Silent Mode With an Input File"](srvpool.md) for more information. |
| `-backup` | Configures automatic backup for a database. EMCA prompts for daily automatic backup options. The default Oracle Enterprise Manager settings are used to back up the database files.  If you use this option, then EMCA uses the value of the `db_recovery_file_des` `t` initialization parameter to identify the fast recovery area for the automated backups. If that parameter is not set, then EMCA generates an error. You can modify these settings later using the Maintenance page in Database Control. |
| `parameters` | See Table G-1, "EMCA Optional Command-Line Parameters". |

#### G.2.5.3 Examples

Example 1 Configuring Database Control for a Single Oracle ASM Instance

To configure the Database Control console for single-instance database using Oracle ASM, run the following command to configure the Database Control console and automatically detect the Oracle ASM instance:

```
emca -config dbcontrol db -repos create
```

Example 2 Configuring Automatic Backups of Your Database

Enter the following command to configure Database Control so it performs automatic daily backups of your database:

```
emca -config dbcontrol db -backup
```

### G.2.6 deconfig all db

Deconfigures both Database Control and the Oracle Management Agent for a database. Options include deleting the Oracle Management Repository and performing these operations on a cluster database.

#### G.2.6.1 Syntax

```
emca -deconfig all db [-repos drop] [-cluster] [-silent] [parameters]
```

#### G.2.6.2 Parameters

Table G-8 deconfig all db Options

| Parameter | Description |
| --- | --- |
| `-repos drop` | Deletes the current Management Repository. |
| `-cluster` | Performs the operation for a cluster database or Oracle ASM instance |
| `-silent` | Performs the operation without prompting for additional information.  If this mode is specified, then all the required parameters must be entered at the command line or specified in an input file using the `–respFile` argument. See [Section 6.6.2, "Using EMCA in Silent Mode With an Input File"](srvpool.md) for more information. |
| `parameters` | See Table G-1, "EMCA Optional Command-Line Parameters". |

### G.2.7 deconfig centralAgent

Use this command to deconfigure the Oracle Management Agent for a database or an Oracle ASM instance. Options include performing this operation on a cluster environment.

For example, you might use this command to remove the Management Agent configuration from a database you are planning to delete. In such a scenario, remove the Management Agent configuration before physically deleting the database. This operation does not remove the actual database or its data files.

#### G.2.7.1 Syntax

```
emca -deconfig centralAgent (db | asm) [-cluster] [-silent] [parameters]
```

#### G.2.7.2 Parameters

Table G-9 deconfig centralAgent Options

| Parameter | Description |
| --- | --- |
| `db` | Performs the operation for a database (including cluster databases).  Use this option for databases that use Oracle ASM to store the data files. If a database is using Oracle ASM, then all the EMCA configuration commands (except for `-upgrade` and `-restore`) detect this automatically and apply the changes to both the database and Oracle ASM instances. |
| `asm` | Performs the operation for an Oracle ASM-only instance (including cluster Oracle ASM instances). |
| `-cluster` | Performs the operation for a cluster database or Oracle ASM instance. |
| `-silent` | Performs the operation without prompting for additional information.  If this mode is specified, then all the required parameters must be entered at the command line or specified in an input file using the `–respFile` argument. See [Section 6.6.2, "Using EMCA in Silent Mode With an Input File"](srvpool.md) for more information. |
| `parameters` | See Table G-1, "EMCA Optional Command-Line Parameters". |

#### G.2.7.3 Examples

Example 1 Removing the Management Agent Configuration from a Database Being Deleted

If you are planning to delete the `testdb` database, then you would use a command similar to the following to remove the Management Agent configuration before physically deleting the database:

```
emca -deconfig centralAgent db -ORACLE_HOME C:\app\oracle\10.2\db1
-SID testdb
```

### G.2.8 deconfig dbcontrol db

Use this command to deconfigure Database Control for a database. Options include deleting the Oracle Management Repository and performing these operations on a cluster database.

This operation does not remove the actual database or its data files

#### G.2.8.1 Syntax

```
emca -deconfig dbcontrol db [-repos drop] [-cluster] [-silent] [parameters]
```

#### G.2.8.2 Parameters

Table G-10 deconfig dbcontrol db Options

| Parameter | Description |
| --- | --- |
| `-repos drop` | Deletes the current Management Repository. |
| `-cluster` | Performs the operation for a cluster database or Oracle ASM instance. |
| `-silent` | Performs the operation without prompting for additional information.  If this mode is specified, then all the required parameters must be entered at the command line or specified in an input file using the `–respFile` argument. See [Section 6.6.2, "Using EMCA in Silent Mode With an Input File"](srvpool.md) for more information. |
| `parameters` | See Table G-1, "EMCA Optional Command-Line Parameters". |

#### G.2.8.3 Examples

Example 1 Removing the Database Control Configuration from a Database Being Deleted

If you are planning to delete the `testdb` database, then you would use a command similar to the following to remove the Database Control configuration before physically deleting the database:

```
emca -deconfig dbcontrol db -repos drop -ORACLE_HOME C:\app\oracle\10.2\db1
-SID testdb
```

### G.2.9 deleteInst

Use this command to deconfigure Oracle Enterprise Manager for a specific instance of a cluster database or Oracle ASM.

#### G.2.9.1 Syntax

```
emca -deleteInst (db | asm) [-silent] [parameters]
```

#### G.2.9.2 Parameters

Table G-11 deleteInst Options

| Parameter | Description |
| --- | --- |
| `db` | Performs the operation for a database (including cluster databases).  Use this option for databases that use Oracle ASM to store the data files. If a database is using Oracle ASM, then all the EMCA configuration commands (except for `-upgrade` and `-restore`) detect this automatically and apply the changes to both the database and Oracle ASM instances. |
| `asm` | Performs the operation for an Oracle ASM-only instance (including cluster Oracle ASM instances). |
| `-silent` | Performs the operation without prompting for additional information.  If this mode is specified, then all the required parameters must be entered at the command line or specified in an input file using the `–respFile` argument. See [Section 6.6.2, "Using EMCA in Silent Mode With an Input File"](srvpool.md) for more information. |
| `parameters` | See Table G-1, "EMCA Optional Command-Line Parameters". |

### G.2.10 deleteNode

Use this command to deconfigure Oracle Enterprise Manager for a node being deleted. For more information, see [Section 6.3, "Understanding EMCA and Enterprise Manager Control with Oracle RAC."](srvpool.md).

#### G.2.10.1 Syntax

```
emca -deleteNode (db | asm) [-silent] [parameters]
```

#### G.2.10.2 Parameters

Table G-12 deleteNode Options

| Parameter | Description |
| --- | --- |
| `db` | Performs the operation for a database (including cluster databases).  Use this option for databases that use Oracle ASM to store the data files. If a database is using Oracle ASM, then all the EMCA configuration commands (except for `-upgrade` and `-restore`) detect this automatically and apply the changes to both the database and Oracle ASM instances. |
| `asm` | Performs the operation for an Oracle ASM-only instance (including cluster Oracle ASM instances). |
| `-silent` | Performs the operation without prompting for additional information.  If this mode is specified, then all the required parameters must be entered at the command line or specified in an input file using the `–respFile` argument. See [Section 6.6.2, "Using EMCA in Silent Mode With an Input File"](srvpool.md) for more information. |
| `parameters` | See Table G-1, "EMCA Optional Command-Line Parameters". |

#### G.2.10.3 Examples

This command is discussed further in [Section 6.7.2, "Updating Database Control Configuration When Adding and Removing Nodes."](srvpool.md).

### G.2.11 displayConfig dbcontrol

Use this command to display information about the current deployment configuration of Database Control in a cluster environment. This command must be used with the `-cluster` option.

#### G.2.11.1 Syntax

```
emca -displayConfig dbcontrol -cluster [-silent] [parameters]
```

#### G.2.11.2 Parameters

Table G-13 displayConfig dbcontrol Options

| Parameter | Description |
| --- | --- |
| `-cluster` | Performs the operation for a cluster database or Oracle ASM instance. |
| `-silent` | Performs the operation without prompting for additional information.  If this mode is specified, then all the required parameters must be entered at the command line or specified in an input file using the `–respFile` argument. See [Section 6.6.2, "Using EMCA in Silent Mode With an Input File"](srvpool.md) for more information. |
| `parameters` | See Table G-1, "EMCA Optional Command-Line Parameters". |

### G.2.12 reconfig dbcontrol

Use this command to reconfigure Database Control deployment for a cluster database. This command must be used with the `-cluster` option.

#### G.2.12.1 Syntax

```
emca -reconfig dbcontrol -cluster [-silent] [parameters]
```

#### G.2.12.2 Parameters

Table G-14 reconfig dbcontrol Options

| Parameter | Description |
| --- | --- |
| `-cluster` | Performs the operation for a cluster database or Oracle ASM instance. |
| `-silent` | Performs the operation without prompting for additional information.  If this mode is specified, then all the required parameters must be entered at the command line or specified in an input file using the `–respFile` argument. See [Section 6.6.2, "Using EMCA in Silent Mode With an Input File"](srvpool.md) for more information. |
| `parameters` | See Table G-1, "EMCA Optional Command-Line Parameters". |

#### G.2.12.3 Examples

This command is discussed further in [Section 6.7.1, "Changing the Database Control Implementation for Your Oracle RAC Database."](srvpool.md).

### G.2.13 reconfig ports

Use this command to explicitly reassign Database Control ports. Options include performing this operation on a cluster environment.

#### G.2.13.1 Syntax

```
emca -reconfig ports [-cluster] [parameters]
```

#### G.2.13.2 Parameters

Table G-15 reconfig ports Options

| Parameter | Description |
| --- | --- |
| `-cluster` | Performs the operation for a cluster database or Oracle ASM instance. |
| `parameters` | See Table G-1, "EMCA Optional Command-Line Parameters". |

#### G.2.13.3 Examples

This command is discussed further in [Section 6.7.3, "Changing the Ports Used by Database Control."](srvpool.md).

### G.2.14 restore

Use this command to restore the current release of Oracle Enterprise Manager configuration to an earlier release. This is the inverse of the `-upgrade` command. Executing this command reverses any changes that resulted from an `-upgrade` operation. This operation can be performed for database, Oracle ASM, or database and Oracle ASM instances simultaneously.

#### G.2.14.1 Syntax

```
emca -restore (db | asm | db_asm) [-cluster] [-silent] [parameters]
```

#### G.2.14.2 Parameters

Table G-16 restore Options

| Parameter | Description |
| --- | --- |
| `db` | Performs the operation for a database (including cluster databases). |
| `asm` | Performs the operation for an Oracle ASM-only instance (including cluster Oracle ASM instances). |
| `db_asm` | Performs the restore operation for a database and an Oracle ASM instance.  Restoring an Oracle ASM instance does not require restoring the database instances it services. Therefore, the Oracle Enterprise Manager configuration can be restored separately for a database and its respective Oracle ASM instance. |
| `-cluster` | Performs the operation for a cluster database or Oracle ASM instance. |
| `-silent` | Performs the operation without prompting for additional information.  If this mode is specified, then all the required parameters must be entered at the command line or specified in an input file using the `–respFile` argument. See [Section 6.6.2, "Using EMCA in Silent Mode With an Input File"](srvpool.md) for more information. |
| `parameters` | See Table G-1, "EMCA Optional Command-Line Parameters". |

### G.2.15 upgrade

Use this command to upgrade the configuration of an earlier release of Oracle Enterprise Manager to the current release. This operation can be performed for database, Oracle ASM, or database and Oracle ASM instances simultaneously.

This command does not upgrade the actual database or Oracle ASM instances, nor does it upgrade the Oracle Enterprise Manager software. Instead, it upgrades the configuration files for the specified instance so that they are compatible with the current release of the Oracle Enterprise Manager software. EMCA attempts to upgrade all instances of the specified database or Oracle ASM target on the host, across all Oracle homes (because it is likely that certain target properties, such as listener port or Oracle home, have changed).

#### G.2.15.1 Syntax

```
emca -upgrade (db | asm | db_asm) [-cluster] [-silent] [parameters]
```

#### G.2.15.2 Parameters

Table G-17 upgrade Options

| Parameter | Description |
| --- | --- |
| `db` | Performs the operation for a database (including cluster databases). |
| `asm` | Performs the operation for an Oracle ASM-only instance (including cluster Oracle ASM instances). |
| `db_asm` | Performs the upgrade operation for a database and an Oracle ASM instance.  Upgrading an Oracle ASM instance does not require upgrading the database instances it services. Therefore, the Oracle Enterprise Manager configuration can be upgraded separately for a database and its respective Oracle ASM instance. |
| `-cluster` | Performs the operation for a cluster database or Oracle ASM instance. |
| `-silent` | Performs the operation without prompting for additional information.  If this mode is specified, then all the required parameters must be entered at the command line or specified in an input file using the `–respFile` argument. See [Section 6.6.2, "Using EMCA in Silent Mode With an Input File"](srvpool.md) for more information. |
| `parameters` | See Table G-1, "EMCA Optional Command-Line Parameters". |

### G.2.16 version

Use this command to print the release information associated with EMCA.

#### G.2.16.1 Syntax

```
emca -version
```