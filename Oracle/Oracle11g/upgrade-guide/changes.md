---
title: Behavior Changes After Upgrading Oracle Database
book: Upgrade Guide
doc_id: E23633-11
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e23633/changes.htm
tags:
  - oracle
  - 11g
  - upgrade-guide
---

## A Behavior Changes After Upgrading Oracle Database

Important changes in behavior exist between Oracle9i Release 2 (9.2), Oracle Database 10g Release 1 (10.1), Oracle Database 10g Release 2 (10.2), Oracle Database 11g Release 1 (11.1), and Oracle Database 11g Release 2 (11.2). This appendix focuses on behavior changes that require a database administrator (also referred to as a DBA) to make an informed decision to minimize the risks that may be introduced by the changes. This appendix does not describe all changed behavior or new features in the new Oracle Database 11g release.

This appendix includes the following topics:

See Also:

- [Oracle Database New Features Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41360/toc.htm) for a complete list of all new features introduced in Oracle Database 11g release
- The "What's New in Oracle Database Reference" section of [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm) for a list of new initialization parameters, new static data dictionary views, and new dynamic performance views in Oracle Database 11g release

Note:

Some of the initialization parameters listed in this appendix are operating system-specific. See your operating system-specific Oracle documentation for more information about these initialization parameters.

## Compatibility and Interoperability Issues in Oracle Database 11g Release 2 (11.2)

The topics in this section describe compatibility and interoperability issues introduced in Oracle Database 11g Release 2 (11.2) and actions you can take to prevent problems resulting from these changes.

- Deprecation of Oracle Enterprise Manager Database Control
- Deprecation of SNMP Support in Oracle Net Listener
- Changes to PL/SQL Procedures
- Deprecated XML DB Constructs
- Cursor\_sharing=similar Obsolete in Oracle Database
- Planned Desupport of Change Data Capture
- Initialization Parameters Deprecated in Oracle Database 11g Release 2 (11.2)
- Initialization Parameters Obsolete in Oracle Database 11g Release 2 (11.2)
- Static Data Dictionary Views Deprecated in Oracle Database 11g Release 2 (11.2)
- Dynamic Performance Views Deprecated in Oracle Database 11g Release 2 (11.2)
- Deprecated Features in Oracle Database 11g Release 2 (11.2)
- Changes to LOG\_ARCHIVE\_DEST\_n Parameters
- Deprecation of -checkpasswd for QOSCTL Quality of Service (QoS) Command
- Desupport of -cleanupOBase Flag of the Deinstallation Tool
- Desupport of the DES, RC4, and MD5 Algorithms

### Deprecation of Oracle Enterprise Manager Database Control

Oracle Enterprise Manager Database Control is deprecated in Oracle Database 11g Release 2 (11.2), and will be desupported in the next major release of Oracle Database. Oracle will fully support Oracle Enterprise Manager Database Control for the life of Oracle Database 11g Release 2 (11.2), including for all patch sets, and through the end of Extended Support.

### Deprecation of SNMP Support in Oracle Net Listener

Oracle is deprecating SNMP support in Oracle Net Listener in Oracle Database 11g Release 2 (11.2). Oracle recommends not using SNMP in new implementations.

See Also:

Doc ID 1341834.1 at `https://support.oracle.com`

### Changes to PL/SQL Procedures

The following PL/SQL procedures have been moved from package `DBMS_XDB` to package `DBMS_XDB_ADMIN` in release 11.2.0.3:

- `moveXDB_tablespace`
- `rebuildHierarchicalIndex`

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm)

### JOB\_QUEUE\_PROCESSES Parameter and Scheduling Jobs

Starting with Oracle Database 11g Release 2 (11.2), setting `JOB_QUEUE_PROCESSES` to `0` causes both `DBMS_SCHEDULER` and `DBMS_JOB` jobs to not run. Previously, setting `JOB_QUEUE_PROCESSES` to `0` caused `DBMS_JOB` jobs to not run, but `DBMS_SCHEDULER` jobs were unaffected and would still run. The default value is `1000`.

Note that Oracle Database overrides the job queue setting to disable scheduler jobs during upgrade mode. Therefore, there is no need to change this setting when upgrading Oracle Database.

See Also:

[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm) for more information on this parameter

### Deprecated XML DB Constructs

The following XML DB constructs have been deprecated in release 11.2.0.3:

- PL/SQL procedure `DBMS_XDB_ADMIN.createRepositoryXMLIndex`
- PL/SQL procedure `DBMS_XDB_ADMIN.XMLIndexAddPath`
- PL/SQL procedure `DBMS_XDB_ADMIN.XMLIndexRemovePath`
- PL/SQL procedure `DBMS_XDB_ADMIN.dropRepositoryXMLIndex`
- XML schema annotation (attribute) `csx:encodingType`
- XMLIndex index on CLOB portions of hybrid `XMLType storage`

See Also:

[Oracle XML DB Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e23094/toc.htm)

### Cursor\_sharing=similar Obsolete in Oracle Database

The `cursor_sharing=similar` parameter is deprecated in Oracle Database release 11.2.0.3. Use adaptive cursor sharing instead.

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/optimops.htm#PFGRF95174) for information about adaptive cursor sharing

### Planned Desupport of Change Data Capture

Oracle Change Data Capture will not be supported in a future release of Oracle Database and will be replaced with Oracle GoldenGate. Therefore, Oracle strongly recommends that you use Oracle GoldenGate for new applications.

For Oracle Database 11g Release 2 (11.2), Change Data Capture continues to function as in earlier releases. If you are currently using Change Data Capture, then you will be able to continue to do so for the foreseeable future. However, Change Data Capture will not be further enhanced.

See Also:

`http://www.oracle.com/technetwork/middleware/goldengate/overview/index.html` on Oracle Technology Network for more information about Oracle GoldenGate

### Initialization Parameters Deprecated in Oracle Database 11g Release 2 (11.2)

A deprecated parameter behaves the same way as a regular parameter, except that a warning message is displayed at instance startup if a deprecated parameter is specified in the parameter file. In addition, all deprecated parameters are logged to the alert log at instance startup.

To get a list of all initialization parameters that are specified as deprecated for the current database, issue the following SQL statement:

```
SQL> SELECT name FROM v$parameter
         WHERE isdeprecated = 'TRUE';
```

The following initialization parameters were deprecated in Oracle Database 11g Release 2 (11.2):

  
`ACTIVE_INSTANCE_COUNT`  
`PARALLEL_IO_CAP_ENABLED`

### Initialization Parameters Obsolete in Oracle Database 11g Release 2 (11.2)

The following initialization parameters were made obsolete in Oracle Database 11g Release 2 (11.2).

Note:

An attempt to start a database using one or more obsolete initialization parameters will succeed, but a warning is returned and recorded in the alert log.  
`DRS_START`  
`GC_FILES_TO_LOCKS`  
`MAX_COMMIT_PROPAGATION_DELAY`  
`PLSQL_NATIVE_LIBRARY_DIR`  
`PLSQL_NATIVE_LIBRARY_SUBDIR_COUNT`  
`SQL_VERSION`

### Static Data Dictionary Views Deprecated in Oracle Database 11g Release 2 (11.2)

These static data dictionary views were deprecated in Oracle Database 11g Release 2 (11.2):

  
`ALL_STREAMS_STMTS` (replaced by `DBA_STREAMS_STMTS`)  
`ALL_STREAMS_STMT_HANDLERS` (replaced by `DBA_STREAMS_STMT_HANDLERS`)  
`DBA_COMPARISON_SCAN_SUMMARY` (replaced by `DBA_COMPARISON_SCAN`)  
`USER_COMPARISON_SCAN_SUMMARY` (replaced by `USER_COMPARISON_SCAN`)

### Dynamic Performance Views Deprecated in Oracle Database 11g Release 2 (11.2)

These dynamic performance views were deprecated in Oracle Database 11g Release 2 (11.2).

  
`V$FLASH_RECOVERY_AREA_USAGE` (replaced by `V$RECOVERY_AREA_USAGE`)

### Deprecated Features in Oracle Database 11g Release 2 (11.2)

These Oracle Database features have been deprecated in Oracle Database 11g Release 2 (11.2). They are supported in this release for backward compatibility. However, Oracle recommends that you migrate away from these deprecated features.

Dictionary-managed Tablespaces

Oracle recommends that you create locally managed tablespaces. Locally managed tablespaces are much more efficiently managed than dictionary-managed tablespaces.

MAX\_JOB\_SLAVE\_PROCESSES

`MAX_JOB_SLAVE_PROCESSES` has been deprecated. Use `JOB_QUEUE_PROCESSES` instead.

### Changes to LOG\_ARCHIVE\_DEST\_n Parameters

Starting with Oracle Database 11g Release 2 (11.2), the number of supported destinations in the `LOG_ARCHIVE_DEST_` `n` and the `LOG_ARCHIVE_DEST_STATE_` `n` parameters have been increased from 10 to 31. Destinations `LOG_ARCHIVE_DEST_11` through `LOG_ARCHIVE_DEST_31` do not support the `SYNC`, `ARCH`, `LOCATION`, `MANDATORY`, `ALTERNATE`, or `DEPENDENCY` attributes, and cannot be specified as the target of the `ALTERNATE` or `DEPENDENCY` attributes.

`LOG_ARCHIVE_DEST_11` through `LOG_ARCHIVE_DEST_31` can only be used when the `COMPATIBLE` initialization parameter is set to `11.2.0` or higher.

### Deprecation of -checkpasswd for QOSCTL Quality of Service (QoS) Command

The syntax `qosctl -checkpasswd username password` has been deprecated in this release. See [Oracle Database Quality of Service Management User's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e24611/apqos_admin.htm#APQOS303) for information about QOSCTL syntax and commands.

### Desupport of -cleanupOBase Flag of the Deinstallation Tool

The `-cleanupOBase` flag of the deinstallation tool is desupported with Oracle Database 11g Release 2 (11.2). There is no replacement for this flag.

### Desupport of the DES, RC4, and MD5 Algorithms

The DES, RC4, and MD5 algorithms are desupported in Oracle Database 11g Release 2 (11.2).

## Compatibility and Interoperability Issues in Oracle Database 11g Release 1 (11.1)

The following sections describe compatibility and interoperability issues introduced in Oracle Database 11g Release 1 (11.1) and actions you can take to prevent problems resulting from these issues.

- Initialization Parameters Deprecated in Oracle Database 11g Release 1 (11.1)
- Initialization Parameters Obsolete in Oracle Database 11g Release 1 (11.1)
- Static Data Dictionary Views with Dropped Columns in Oracle Database 11g Release 1 (11.1)
- Deprecated Features in Oracle Database 11g Release 1 (11.1)
- Automatic Maintenance Tasks Management
- New SYSASM Privilege and OSASM Group for ASM Administration
- ASM Disk Group Compatibility
- COMPUTE STATISTICS and ESTIMATE STATISTICS Clauses
- Oracle Data Mining Models and the DMSYS Schema Objects
- Oracle Data Mining Scoring Engine
- SQL Plan Management and Control of SQL Plan Baselines
- Binary XML Support for Oracle XML Database
- PL/SQL Native Compilation and Access Control for Network Utility Packages
- PL/SQL Control Parameters
- Change in WebDAV ACL Evaluation Rules in Oracle XML DB
- Summary Management and SQL Access Advisor
- Standard Edition Starter Database
- Core Dump Location
- New Default Value for UNDO\_MANAGEMENT
- LOG\_ARCHIVE\_DEST\_n Parameters
- SHARED\_POOL\_SIZE Parameter
- JOB\_QUEUE\_PROCESSES Parameter and Scheduling Jobs
- Automatic Diagnostic Repository

### Initialization Parameters Deprecated in Oracle Database 11g Release 1 (11.1)

The following initialization parameters were deprecated in Oracle Database 11g Release 1 (11.1).

To get a list of all deprecated initialization parameters, issue the following SQL statement:

```
SQL> SELECT name FROM v$parameter
         WHERE isdeprecated = 'TRUE';
```

A deprecated parameter behaves the same way as a regular parameter, except that a warning message is displayed at instance startup if a deprecated parameter is specified in the parameter file. In addition, all deprecated parameters are logged to the alert log at instance startup.

  
`BACKGROUND_DUMP_DEST` (replaced by `DIAGNOSTIC_DEST`)  
`COMMIT_WRITE`  
`CURSOR_SPACE_FOR_TIME`  
`INSTANCE_GROUPS`  
`LOG_ARCHIVE_LOCAL_FIRST`  
`PLSQL_DEBUG` (replaced by `PLSQL_OPTIMIZE_LEVEL`)  
`PLSQL_V2_COMPATIBILITY`  
`REMOTE_OS_AUTHENT`  
`RESOURCE_MANAGER_CPU_ALLOCATION`  
`STANDBY_ARCHIVE_DEST`  
`TRANSACTION_LAG` attribute (of the `CQ_NOTIFICATION$_REG_INFO` object)  
`USER_DUMP_DEST` (replaced by `DIAGNOSTIC_DEST`)

### Initialization Parameters Obsolete in Oracle Database 11g Release 1 (11.1)

These initialization parameters were made obsolete in Oracle Database 11g Release 1 (11.1).

  
`DDL_WAIT_FOR_LOCKS`  
`LOGMNR_MAX_PERSISTENT_SESSIONS`  
`PLSQL_COMPILER_FLAGS`

Note:

An attempt to start a database using one or more obsolete initialization parameters will succeed, but a warning is returned and recorded in the alert log.

### Static Data Dictionary Views with Dropped Columns in Oracle Database 11g Release 1 (11.1)

These static data dictionary view columns were dropped in Oracle Database 11g Release 1 (11.1):

| Static Data Dictionary View | Dropped Columns |
| --- | --- |
| `V$DATAFILE` | `PLUGGED_IN` |

### Deprecated Features in Oracle Database 11g Release 1 (11.1)

This section lists Oracle Database features deprecated in Oracle Database 11g Release 1 (11.1). They are supported in this release for backward compatibility. However, Oracle recommends that you migrate away from these deprecated features.

- Oracle Ultra Search
- Java Development Kit (JDK) 1.4
	Oracle recommends that you use JDK 5.0; but JDK 1.5 is also fully supported.
- CTXXPATH index
	Oracle recommends that you use XMLIndex instead.

See Also:

[Oracle XML DB Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e23094/xdb_indexing.htm#ADXDB0500)

### Automatic Maintenance Tasks Management

Automatic Maintenance Tasks Management, a new database component in Oracle Database 11g Release 1 (11.1), schedules all automatic maintenance tasks in an expanded set of maintenance windows. Automatic Maintenance Tasks Management enables you to exercise finer control over maintenance task scheduling for tasks such as optimizer statistics gathering, Segment Advisor, and Automatic SQL Tuning Advisor.

Automatic Maintenance Tasks Management uses all existing maintenance windows (for example, windows that are current members of the `MAINTENANCE_WINDOW_GROUP`. Existing resource plans associated with the maintenance windows are used. However, `AUTOTASK_CONSUMER_GROUP` is replaced in the resource plans by the AutoTask Resource Subplan.

If you disable either Optimizer Statistics Gathering or Segment Advisor jobs in 10g, then the corresponding Automatic Maintenance Tasks Management feature is disabled after upgrading to Oracle Database 11g Release 1 (11.1).

The following list shows the default settings for maintenance tasks:

- Online backup is disabled
- Optimizer Statistics Gathering is on
- Segment Advisor is on
- Automatic SQL Tuning is on

All other Automatic Maintenance Tasks Management clients are enabled by default.

Although Automatic Maintenance Tasks Management is automatically enabled when upgrading to Oracle Database 11g Release 1 (11.1), AutoTask online backup is not enabled automatically. You must configure online backup manually, if desired, after upgrading the database. If you perform a database downgrade, then Automatic Maintenance Tasks Management reverts to the default behavior for that release.

See Also:

The [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/tasks.htm#ADMIN0235) for complete information about the Automatic Maintenance Tasks Management feature

### New SYSASM Privilege and OSASM Group for ASM Administration

Oracle Database 11g Release 1 (11.1) introduces a new `SYSASM` privilege that is specifically intended for performing ASM administration tasks. Using the `SYSASM` privilege instead of the `SYSDBA` privilege provides a clearer division of responsibility between ASM administration and database administration.

Warning messages will appear in the ASM `alert.log` if `SYSDBA` performs disk group maintenance (`CREATE` `DISKGROUP`, `MOUNT` / `DISMOUNT`, `ADD` / `DROP` `DISK`, `ONLINE` / `OFFLINE` `DISK`, `DROP` `DISKGROUP`). These tasks are deprecated for `SYSDBA`; they should be performed by `SYSASM`.

`OSASM` is a new operating system (OS) group that is used exclusively for ASM. Members of the `OSASM` group can connect `AS` `SYSASM` using OS authentication and have full access to ASM.

This feature is described in more detail in ["About Upgrading System Authentication for Oracle ASM Instances"](upgrade.md).

See Also:

[Oracle Database Storage Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asminst.htm#OSTMG02600) for more information about accessing ASM instances

### ASM Disk Group Compatibility

Starting with Oracle Database 11g Release 1 (11.1), you can advance the Oracle Database and the ASM disk group compatibility settings across software versions. Using the new compatibility attributes, `compatible.rdbms` and `compatible.asm`, you can specify the minimum software version required to use the disk group for the database and the disk group for ASM, respectively.

This feature enables heterogeneous environments with disk groups from Oracle Database 10g Release 1 (10.1), Oracle Database 10g Release 2 (10.2), and Oracle Database 11g Release 1 (11.1). By default, both attributes are set to 10.1. You must advance these attributes to take advantage of the new features.

See Also:

[Oracle Database Storage Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmdiskgrps.htm#OSTMG10040) for more information on ASM disk group compatibility

### COMPUTE STATISTICS and ESTIMATE STATISTICS Clauses

In earlier releases, the `ANALYZE...COMPUTE STATISTICS` and `ANALYZE...ESTIMATE STATISTICS` clauses could be used to start or stop the collection of statistics on an index. These clauses have been made obsolete. Oracle Database 11g Release 1 (11.1) automatically collects statistics during index creation and rebuild. These clauses are no longer supported.

### Oracle Data Mining Models and the DMSYS Schema Objects

During the upgrade to Oracle Database 11g Release 1 (11.1), `DMSYS` schema objects along with user models residing in user schemas are upgraded from any previous release without major constraints. Upon completion of the upgrade, the mining metadata is migrated into the `SYS` schema while the user models continue functioning with the new metadata. Oracle recommends that you drop the `DMSYS` schema after setting the `COMPATIBLE` initialization parameter to 11.0.0. In addition, the DBA will need to grant the new `CREATE MINING MODEL` privilege so that existing users can continue to build mining models.

Data mining models residing in a user schema are automatically upgraded as part of the model upgrade, which is an integral part of the Oracle Database upgrade process. Data mining model Export and Import utilities can also be used as a means of upgrading data mining models from one release to another.

During the database downgrade process, the data mining component is downgraded to a previous release. The downgrade process reloads `DMSYS` objects such as packages, types, and table objects as well as downgrading model objects residing in user schemas (if any). Objects that were created as a part of the database upgrade are removed from the `SYS` schema during the downgrade procedure. The process is transparent and does not require any user intervention.

After upgrading (and dropping the `DMSYS` schema after setting the `COMPATIBLE` initialization parameter to 11.0.0), importing models that were exported from Oracle Database 10g Release 1 (10.1) might have some complications due to their reference to the now nonexistent `DMSYS` schema. To handle this case, Oracle provides scripts to sufficiently (and minimally) mimic the `DMSYS` interface present in the Oracle Database 10g Release 1 (10.1) database so that the Import process can proceed. This is not a common occurrence because models become stale over time and users typically want to rebuild their models rather than import older ones.

Note that Data Mining is not protected by the `COMPATIBLE` initialization parameter. If `COMPATIBLE` is set at `10.1.0` or `10.2.0` while the database has been upgraded to Oracle Database 11g Release 1 (11.1), then all new and existing Data Mining features and functions should work. If you have built new mining models that are only available in Oracle Database 11g Release 1 (11.1), and subsequently decide to downgrade the database to Oracle Database 10g Release 2 (10.2), you will be required to drop the new mining models before downgrading.

### Oracle Data Mining Scoring Engine

Starting with Oracle Database 11g Release 1 (11.1), the Oracle Data Mining Scoring Engine can no longer be installed.

See Also:

[Oracle Data Mining Administrator's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e16807/upgrade_odm.htm#DMADM001)

### SQL Plan Management and Control of SQL Plan Baselines

The use of stored outlines is deprecated in Oracle Database 11g Release 1 (11.1). Instead, you should use the SQL plan management feature that enables the optimizer to maintain a history of execution plans for a SQL statement. Using the execution plan history, the optimizer is able to detect a new plan representing a plan change for a SQL statement. When the optimizer detects a new plan, it stores the new plan and marks it for performance evaluation and uses the old (currently known good) plan. The optimizer uses the new plan only after its performance is verified to be better than that of the old plan. A SQL plan baseline consists of a set of known good plans for a SQL statement.

Migration of SQL Profiles

SQL Profiles are SQL management objects that were introduced in Oracle Database 10g Release 1 (10.1). These objects resided in a section of the dictionary that was defined in `SYSTEM` tablespace. The dictionary tables storing the SQL profiles are restructured to accommodate the storage of SQL plan baselines, which are also SQL management objects. Further, these dictionary tables are now defined in the `SYSAUX` tablespace.

When you upgrade from Oracle Database 10g Release 1 (10.1) to Oracle Database 11g Release 1 (11.1), the database upgrade script moves existing SQL profiles from the `SYSTEM` tablespace to the `SYSAUX` tablespace. Thus, if an Oracle Database 11g Release 1 (11.1) database instance is up but the `SYSAUX` tablespace is offline, then the optimizer is not able to access SQL Management objects, which can affect the performance on some of the SQL workload. In contrast, in Oracle Database 10g Release 1 (10.1), because SQL profiles were stored in `SYSTEM` tablespace, the unavailability of SQL profiles did not exist. Note that starting with Oracle Database 11g Release 1 (11.1), taking the `SYSAUX` tablespace offline can have potential SQL performance consequences.

Backward Compatibility

In Oracle Database 11g Release 1 (11.1):

- If a stored outline for a SQL statement is active for the user session (for example, the stored outline category matches with the user session category), then the statement is compiled using the stored outline.
- If a private outline is available for a SQL statement, then the statement is compiled using the private outline.

If a stored outline is available for a SQL statement, then the SQL Plan Management feature is not used. However, if another user session uses the same SQL statement but without an active stored outline, then the SQL plan management feature is used.

See Also:

- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm) for more information about SQL Plan Management
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_spm.htm#ARPLS150) for more information about the `DBMS_SPM` package

### Binary XML Support for Oracle XML Database

The binary XML storage option that is new in Oracle Database 11g Release 1 (11.1) is available when the `COMPATIBLE` initialization parameter is set to `11.0.0` or higher. When you create a table or column with this storage option, the minimum compatibility requirement is checked. This also applies when storing binary XML documents directly in the XML DB repository.

#### When Upgrading to Oracle Database 11g Release 1 (11.1)

When the database is upgraded to Oracle Database 11g Release 1 (11.1), none of the existing user XMLType tables and instances is modified in any fashion. Existing tables can be altered and new tables can be subsequently created using the new storage format after the upgrade is completed. The XDB tables `XDB$CONFIG` and `XDB$ACL` and the corresponding XML schemas are migrated to binary XML storage when a database is upgraded to Oracle Database 11g Release 1 (11.1).

### PL/SQL Native Compilation and Access Control for Network Utility Packages

Oracle introduced compatibility and interoperability changes in PL/SQL for Oracle Database 11g Release 1 (11.1).

- PL/SQL Native Compilation
- Access Control for Network Utility Packages

#### PL/SQL Native Compilation

Starting with Oracle Database 11g, PL/SQL Native Compilation does not need a C compiler. Therefore, if you presently use a C compiler only to support PL/SQL Native Compilation, you can remove it from the machine where your database is installed (and from each node in an Oracle RAC configuration).

Moreover, the output of PL/SQL Native Compilation is no longer materialized on the file system. There, the Oracle Database 10g initialization parameters `PLSQL_Native_Library_Dir` and `PLSQL_Native_Library_Subdir_Count` have no significance in Oracle Database 11g. The directories that they denoted, and the contents of these directories, can be safely deleted on completion of the upgrade process.

Further, the `SPNC_COMMANDS` file (in the `ORACLE_HOME` `/plsql` directory) is no longer needed.

Only one initialization parameter, `PLSQL_Code_Type`, remains for controlling PL/SQL Native Compilation. The DBA, therefore, no longer needs to have any interest in PL/SQL Native Compilation.

#### Access Control for Network Utility Packages

The default behavior for access control to network utility packages has been changed to disallow network operations to all nonprivileged users. This default behavior is different from, and is incompatible with, previous versions of Oracle Database.

For database users upgrading to Oracle Database 11g Release 1 (11.1), applications that depend on the PL/SQL network utility packages compile without any issues. However, at runtime the applications might receive exceptions when attempting to perform privileged network operations. Although you can restore the compatibility by using a wildcard to grant those privileges to perform any network operations to `PUBLIC`, Oracle strongly advises that database administrators carefully review each situation on an individual basis and grant privileges only as needed.

Note:

Oracle XML DB is required to properly maintain the access control lists. If Oracle XML DB is not already installed on the system, then you must install it during the upgrade procedure.

See Also:

["Configuring Fine-Grained Access to External Network Services After Upgrading Oracle Database"](afterup.md)

### PL/SQL Control Parameters

The behavior of some Oracle parameters that control the behavior of PL/SQL have changed as of Oracle Database 11g Release 1 (11.1).

- If PL/SQL debug code generation mode is selected by any parameter setup, then native code generation is turned off.
- Debug code generation is on if the `PLSQL_OPTIMIZE_LEVEL` `<=` `1`.
- `PLSQL_DEBUG` is deprecated.
	You should use `PLSQL_OPTIMIZE_LEVEL` instead. A deprecation warning is issued if `PLSQL_DEBUG` is used.
- If `PLSQL_OPTIMIZE_LEVEL` `<=` `1`, then native code generation is turned off.
- `PLSQL_COMPILER_FLAGS` is obsolete. It has no effect any longer and draws an error message that an illegal option is being set.
- `PLSQL_V2_COMPATIBILITY` is deprecated.

### Change in WebDAV ACL Evaluation Rules in Oracle XML DB

Oracle XML DB uses a security mechanism that is based on access-control lists (ACLs) to restrict access to any Oracle XML DB resource. An ACL is a list of access-control entries (ACEs) that determine which users, roles, and groups have access to a given resource.

There have been changes to the treatment of WebDAV ACL entries. Before Oracle Database 11g Release 1 (11.1), a < `deny` > entry always trumped any < `allow` > entry in a given ACL. Starting with Oracle Database 11g Release 1 (11.1), ACE order is irrelevant. The default behavior is determined only by the first < `allow` > or < `deny` > entry that is encountered. That is, the first entry determines the behavior for that principal and additional ACEs for that principal have no effect.

This change in the default behavior is different from, and is incompatible with, previous versions of Oracle Database. When upgrading to Oracle Database 11g Release 1 (11.1), you can get the same behavior as in previous releases by manually reordering the ACLs (if necessary). That is, if there are any ACLs that have `<allow>` followed somewhere by `<deny>`, then you should (manually) reorder the ACLs so that the `<deny>` entry occurs first.

See Also:

[Oracle XML DB Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e23094/xdb21sec.htm#ADXDB2400) for more information about the ACL evaluation rules

### Summary Management and SQL Access Advisor

Starting with Oracle Database 10g Release 2 (10.2), the `DBMS_OLAP` package, which is the Summary Advisor in Summary Management, is being deprecated and has been replaced by the SQL Access Advisor.

### SQL Access Advisor Tasks

Due to internal structural changes to the SQL Access Advisor repository, a database upgrade resets all existing SQL Access Advisor tasks to their initial state. This effectively deletes all recommendation information for tasks that have successfully completed before the upgrade.

After upgrade, the recommendation information can be restored by re-executing the existing SQL Access Advisor tasks.

### Standard Edition Starter Database

When the Standard Edition (SE) starter database is upgraded, the following components cannot be upgraded by the SE server because they require options that are not installed in the Standard Edition:

- OLAP Catalog
- OLAP Analytic Workspace
- Oracle OLAP API

After the upgrade, these components have a `STATUS` value of `'OPTION OFF'` in the `DBA_REGISTRY` view, and there will be some invalid objects in the associated component schemas. The Database Upgrade Assistant (DBUA) shows unsuccessful upgrades for these components.

### Core Dump Location

On UNIX systems, when an application program crashes due to an unhandled signal, such as a segmentation fault, a core dump file is usually generated. The system default file name for this file is `core`, and it is located in the directory in which the application is currently running.

Starting with Oracle Database 11g Release 1 (11.1), applications using the Oracle Call Interface (OCI) can create a subdirectory named core\_process\_id, where process\_id is the UNIX ID of the process that crashed. The `core` file is then placed in that subdirectory instead of the location where the application is running.

In sqlnet.ora, setting `DIAG_SIGHANDLER_ENABLED = TRUE` also puts the generated `core` file in the directory named core\_process\_id.

### New Default Value for UNDO\_MANAGEMENT

Starting with Oracle Database 11g Release 1 (11.1), the default value of the `UNDO_MANAGEMENT` parameter is `AUTO` so that automatic undo management is enabled by default. You must set the parameter to `MANUAL` to turn off automatic undo management, if required.

The `UNDO_MANAGEMENT` and `ROLLBACK_SEGMENTS` initialization parameters have changed from basic initialization parameters to non-basic initialization parameters. Most databases should be required to have only basic parameters set to run properly and efficiently.

See Also:

`UNDO_MANAGEMENT` in [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams264.htm#REFRN10224)

### LOG\_ARCHIVE\_DEST\_n Parameters

Starting with Oracle Database 11g Release 1 (11.1), the `LOG_ARCHIVE_DEST_` `n` parameter can be used to specify a local archiving destination on a database instance running Oracle Standard Edition. Previously, this parameter could only be specified on a database instance running Oracle Enterprise Edition.

### SHARED\_POOL\_SIZE Parameter

Migration utilities for this release recommend new values for `SHARED_POOL_SIZE` based on the value of internal SGA overheads in the pre-upgrade environment, which you can determine by running the following query before upgrading to Oracle Database 11g Release 1 (11.1):

```
SQL> SELECT SUM(BYTES) FROM v$sgastat WHERE pool = 'shared pool';
```

In Oracle Database 11g Release 1 (11.1), the exact value of internal SGA overhead, or Startup overhead in Shared Pool, is listed in the new `v$sgainfo` view.

In manual SGA mode, values of `SHARED_POOL_SIZE` that are too small to accommodate the internal SGA overhead result in an ORA-00371 error during startup. This generated error message includes a suggested value for the `SHARED_POOL_SIZE` parameter. If you are using automatic shared memory management, the size of the shared pool is tuned automatically, and the ORA-00371 error is never generated.

The amount of shared pool memory allocated by Oracle Database releases before Oracle Database 10g Release 1 (10.1) was equal to the sum of the value of the `SHARED_POOL_SIZE` initialization parameter and the internal SGA overhead computed during instance startup. This overhead was based on the values of several other initialization parameters.

For example, if the `SHARED_POOL_SIZE` parameter is 64 megabytes and the internal SGA overhead is 12 megabytes, then the real size of shared pool in the SGA would be 76 megabytes, although the value of the `SHARED_POOL_SIZE` parameter would still be displayed as megabytes.

Starting with Oracle Database 10g Release 1 (10.1), the size of internal SGA overhead is included in the value of the `SHARED_POOL_SIZE` parameter. The shared pool memory allocated at startup is exactly the value of `SHARED_POOL_SIZE`. Therefore, this parameter must be set such that it includes both the internal SGA overhead and the desired effective value of the shared pool size.

Assuming that the internal SGA overhead remains unchanged, the effective available value of shared pool after startup would be 12 megabytes less than the value of the `SHARED_POOL_SIZE` parameter, or 52 megabytes. To maintain 64 megabytes for the effective value of shared pool memory, set the parameter to 76 megabytes.

### JOB\_QUEUE\_PROCESSES Parameter New Default Setting

Beginning with Oracle Database 11g Release 1 (11.1), the `JOB_QUEUE_PROCESSES` parameter is changed from a basic to a non-basic initialization parameter. Most databases must only have basic parameters set to run properly and efficiently. The default value is also changed from `0` to `1000`.

Note that Oracle Database overrides the job queue setting to disable scheduler jobs during upgrade mode. Therefore, there is no need to change this setting when upgrading Oracle Database.

See Also:

[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm) for more information on this parameter

### Automatic Diagnostic Repository

The locations of alert logs and trace files are no longer set by the initialization parameters `BACKGROUND_DUMP_DEST` and `USER_DUMP_DEST`. They are now kept in the Automatic Diagnostic Repository (ADR), whose location is set the by the initialization parameter `DIAGNOSTIC_DEST`.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/diag.htm#ADMIN11260) for more information on the management of diagnostic information

## Compatibility and Interoperability Issues in Oracle Database 10g Release 2 (10.2)

The following sections describe compatibility and interoperability issues introduced in Oracle Database 10g Release 2 (10.2). If you are upgrading to Oracle Database 11g Release 1 (11.1) from a release earlier than Oracle Database 10g Release 2 (10.2), then see the following sections for information about actions you can take to prevent problems resulting from these issues:

- Initialization Parameters Deprecated in Oracle Database 10g Release 2 (10.2)
- Initialization Parameters Obsolete in Oracle Database 10g Release 2 (10.2)
- Static Data Dictionary Views with Dropped Columns in Oracle Database 10g Release 2 (10.2)
- SQL
- CONNECT Role
- Time Zone Files
- New Limit for FAILED\_LOGIN\_ATTEMPTS

### Initialization Parameters Deprecated in Oracle Database 10g Release 2 (10.2)

The following initialization parameters were deprecated in Oracle Database 10g Release 2 (10.2). To get a list of all deprecated initialization parameters, issue the following SQL statement:

```
SQL> SELECT name FROM v$parameter
         WHERE isdeprecated = 'TRUE';
```

A deprecated parameter behaves the same way as a regular parameter, except that a warning message is displayed at instance startup if a deprecated parameter is specified in the parameter file. In addition, all deprecated parameters are logged to the alert log at instance startup:

  
`LOGMNR_MAX_PERSISTENT_SESSIONS`  
`MAX_COMMIT_PROPAGATION_DELAY`  
`REMOTE_ARCHIVE_ENABLE`  
`SERIAL_REUSE`  
`SQL_TRACE`

### Initialization Parameters Obsolete in Oracle Database 10g Release 2 (10.2)

The following initialization parameters were made obsolete in Oracle Database 10g Release 2 (10.2).

Note:

An attempt to start a database using one or more obsolete initialization parameters will succeed, but a warning is returned and recorded in the alert log.  
`ENQUEUE_RESOURCES`

### Static Data Dictionary Views with Dropped Columns in Oracle Database 10g Release 2 (10.2)

The following static data dictionary view columns were dropped in Oracle Database 10g Release 2 (10.2):

| Static Data Dictionary View | Dropped Columns |
| --- | --- |
| `DBA_HIST_SQLBIND` | `CHILD_NUMBER` |

### SQL

The behavior of date formats has changed when used with XML functions. The XML Schema standard specifies that dates and timestamps in XML data be in standard formats. Before Oracle Database 10g Release 2 (10.2), dates and timestamps in XML data did not follow this standard; rather, the format of dates and timestamps in generated XML was determined by the database format.

As of Oracle Database 10g Release 2 (10.2), the XML generation functions in Oracle XML DB produce dates and timestamps according to the XML schema standard.

See Also:

[Oracle XML DB Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e23094/toc.htm) for more information

### CONNECT Role

After upgrading from a release earlier than Oracle Database 10g Release 2 (10.2), the `CONNECT` role has only the `CREATE SESSION` privilege; the other privileges granted to the `CONNECT` role in earlier releases are revoked during the upgrade. For further information about this, see ["Updating the CONNECT Role from Earlier Releases"](upgrade.md).

### Time Zone Files

The time zone files that are supplied with Oracle Database 10g Release 2 (10.2) have been updated from version 4 to version 8 to reflect changes in transition rules for some time zone regions. The changes might affect existing data of `TIMESTAMP WITH TIME ZONE` data type. For further information about this, see ["About Warnings for TIMESTAMP WITH TIME ZONE Data Type"](upgrade.md).

### New Limit for FAILED\_LOGIN\_ATTEMPTS

As of Oracle Database 10g Release 2 (10.2), the limit for `FAILED_LOGIN_ATTEMPTS` for the `DEFAULT` profile is 10. Before Oracle Database 10g Release 2 (10.2), the default was `UNLIMITED`.

## Compatibility and Interoperability Issues in Oracle Database 10g Release 1 (10.1)

The following sections describe compatibility and interoperability issues introduced in Oracle Database 10g Release 1 (10.1). If you are upgrading to Oracle Database 11g Release 1 (11.1) from a release earlier than Oracle Database 10g Release 1 (10.1), then see the following sections for information about actions you can take to prevent problems resulting from these issues:

- Initialization Parameters Deprecated in Oracle Database 10g Release 1 (10.1)
- Initialization Parameters Obsolete in Oracle Database 10g Release 1 (10.1)
- Static Data Dictionary Views Deprecated in Oracle Database 10g Release 1 (10.1)
- Static Data Dictionary Views Obsolete in Oracle Database 10g Release 1 (10.1)
- Dynamic Performance Views Deprecated in Oracle Database 10g Release 1 (10.1)
- Dynamic Performance Views Obsolete in Oracle Database 10g Release 1 (10.1)
- SQL Optimizer
- SQL Changes
- Invalid Synonyms After an Upgrade
- Manageability
- Transaction and Space
- Recovery and Data Guard
- RMAN
- CREATE DATABASE
- Oracle Real Application Clusters
- Materialized Views
- Change Data Capture
- Change in the Default Archival Processing to Remote Archive Destinations
- Limitations on NCHAR Data Types
- PL/SQL Native Compilation
- Evaluation of Numeric Literals
- Change in Behavior for SESSION\_CACHED\_CURSORS
- New Default Value for DB\_BLOCK\_SIZE
- OPTIMIZER\_MAX\_PERMUTATIONS and OPTIMIZER\_FEATURES\_ENABLE
- Change in Behavior for LOG\_ARCHIVE\_FORMAT
- New Default Value for PGA\_AGGREGATE\_TARGET
- Change in Behavior for SHARED\_POOL\_SIZE
- Shared Server Parameters

### Initialization Parameters Deprecated in Oracle Database 10g Release 1 (10.1)

The following initialization parameters were deprecated in Oracle Database 10g Release 1 (10.1) To get a list of all deprecated initialization parameters, issue the following SQL statement:

```
SQL> SELECT name FROM v$parameter
         WHERE isdeprecated = 'TRUE';
```

A deprecated parameter behaves the same way as a regular parameter, except that a warning message is displayed at instance startup if a deprecated parameter is specified in the parameter file. In addition, all deprecated parameters are logged to the alert log at instance startup:

  
`BUFFER_POOL_KEEP` (replaced by `DB_KEEP_CACHE_SIZE`)  
`BUFFER_POOL_RECYCLE` (replaced by `DB_RECYCLE_CACHE_SIZE`)  
`GLOBAL_CONTEXT_POOL_SIZE`  
`LOCK_NAME_SPACE`  
`LOG_ARCHIVE_START`  
`MAX_ENABLED_ROLES`  
`PARALLEL_AUTOMATIC_TUNING`  
`PLSQL_COMPILER_FLAGS` (replaced by `PLSQL_CODE_TYPE` and `PLSQL_DEBUG`)  
`SQL_VERSION`

### Initialization Parameters Obsolete in Oracle Database 10g Release 1 (10.1)

The following initialization parameters were made obsolete in Oracle Database 10g Release 1 (10.1).

Note:

An attempt to start a database using one or more obsolete initialization parameters will succeed, but a warning is returned and recorded in the alert log.  
`DBLINK_ENCRYPT_LOGIN`  
`HASH_JOIN_ENABLED`  
`LOG_PARALLELISM`  
`MAX_ROLLBACK_SEGMENTS`  
`MTS_CIRCUITS`  
`MTS_DISPATCHERS`  
`MTS_LISTENER_ADDRESS`  
`MTS_MAX_DISPATCHERS`  
`MTS_MAX_SERVERS`  
`MTS_MULTIPLE_LISTENERS`  
`MTS_SERVERS`  
`MTS_SERVICE`  
`MTS_SESSIONS`  
`OPTIMIZER_MAX_PERMUTATIONS`  
`ORACLE_TRACE_COLLECTION_NAME`  
`ORACLE_TRACE_COLLECTION_PATH`  
`ORACLE_TRACE_COLLECTION_SIZE`  
`ORACLE_TRACE_ENABLE`  
`ORACLE_TRACE_FACILITY_NAME`  
`ORACLE_TRACE_FACILITY_PATH`  
`PARTITION_VIEW_ENABLED`  
`PLSQL_NATIVE_C_COMPILER`  
`PLSQL_NATIVE_LINKER`  
`PLSQL_NATIVE_MAKE_FILE_NAME`  
`PLSQL_NATIVE_MAKE_UTILITY`  
`ROW_LOCKING`  
`SERIALIZABLE`  
`TRANSACTION_AUDITING`  
`UNDO_SUPPRESS_ERRORS`

### Static Data Dictionary Views Deprecated in Oracle Database 10g Release 1 (10.1)

The following static data dictionary views were deprecated in Oracle Database 10g Release 1 (10.1).

  
`ALL_STORED_SETTINGS` (replaced by `ALL_PLSQL_OBJECT_SETTINGS`)  
`DBA_STORED_SETTINGS` (replaced by `DBA_PLSQL_OBJECT_SETTINGS`)  
`USER_STORED_SETTINGS` (replaced by `USER_PLSQL_OBJECT_SETTINGS`)

### Static Data Dictionary Views Obsolete in Oracle Database 10g Release 1 (10.1)

The following static data dictionary views were made obsolete in Oracle Database 10g Release 1 (10.1).

| ALL\_ Views | DBA\_ Views | USER\_ Views |
| --- | --- | --- |
| `ALL_SOURCE_TAB_COLUMNS` | `DBA_SOURCE_TAB_COLUMNS` | `USER_SOURCE_TAB_COLUMNS` |

### Dynamic Performance Views Deprecated in Oracle Database 10g Release 1 (10.1)

The following dynamic performance views were deprecated in Oracle Database 10g Release 1 (10.1):

  
`GV$CACHE`  
`GV$CACHE_TRANSFER`  
`GV$CLASS_CACHE_TRANSFER` (replaced by `GV$INSTANCE_CACHE_TRANSFER`)  
`GV$FALSE_PING`  
`GV$FILE_CACHE_TRANSFER` (replaced by `GV$INSTANCE_CACHE_TRANSFER`)  
`GV$GC_ELEMENTS_WITH_COLLISIONS`  
`GV$LOCK_ACTIVITY`  
`GV$TEMP_CACHE_TRANSFER` (replaced by `GV$INSTANCE_CACHE_TRANSFER`)  
`V$CACHE`  
`V$CACHE_LOCK`  
`V$CACHE_TRANSFER`  
`V$CLASS_CACHE_TRANSFER` (replaced by `V$INSTANCE_CACHE_TRANSFER`)  
`V$FALSE_PING`  
`V$FILE_CACHE_TRANSFER` (replaced by `V$INSTANCE_CACHE_TRANSFER`)  
`V$GC_ELEMENTS_WITH_COLLISIONS`  
`V$LOCK_ACTIVITY`  
`V$TEMP_CACHE_TRANSFER` (replaced by `V$INSTANCE_CACHE_TRANSFER`)

### Dynamic Performance Views Obsolete in Oracle Database 10g Release 1 (10.1)

The following dynamic performance views were made obsolete in Oracle Database 10g Release 1 (10.1):

| GV$ Views | V$ Views |
| --- | --- |
| `GV$COMPATIBILITY` | `V$COMPATIBILITY` |
| `GV$COMPATSEG` | `V$COMPATSEG` |
| `GV$MLS_PARAMETERS` | `V$MLS_PARAMETERS` |
| `GV$MTS` | `V$MTS` |

### SQL Optimizer

This section describes compatibility and interoperability issues relating to the SQL Optimizer in Oracle Database 10g Release 1 (10.1).

#### Rule-Based Optimizer Desupported

Starting with Oracle Database 10g Release 1 (10.1), the cost-based optimizer (CBO) is now enabled by default. The rule-based optimizer is no longer supported in Oracle Database 10g Release 1 (10.1). As a result, `rule` and `choose` are no longer supported as `OPTIMIZER_MODE` initialization parameter values and a warning is displayed in the alert log if `OPTIMIZER_MODE` is set to either of these values.

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/optimops.htm#PFGRF001) for more information about the cost-based optimizer

#### Optimizer Statistics

Collection of optimizer statistics is now automatically performed by default for all schemas (including `SYS`), for pre-existing databases upgraded from a release earlier than Oracle Database 10g Release 1 (10.1), and for newly created databases. Gathering optimizer statistics on stale objects is scheduled by default to occur daily during the maintenance window.

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/stats.htm#PFGRF003) for more information about optimizer statistics

#### COMPUTE STATISTICS Clause of CREATE INDEX

In earlier releases, the `COMPUTE STATISTICS` clause of `CREATE INDEX` could be used to start or stop the collection of statistics on an index. This clause has been deprecated. Oracle Database 10g Release 1 (10.1) and later releases automatically collect statistics during index creation and rebuild. This clause is supported for backward compatibility and does not cause errors.

#### SKIP\_UNUSABLE\_INDEXES

In earlier releases, `SKIP_UNUSABLE_INDEXES` was a session parameter only. In Oracle Database 10g Release 1 (10.1) and later releases, it is an initialization parameter and defaults to `true`. The `true` setting disables error reporting of indexes and index partitions marked `UNUSABLE`. This setting allows all operations (inserts, deletes, updates, and selects) on tables with unusable indexes or index partitions.

See Also:

`SKIP_UNUSABLE_INDEXES` in [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams243.htm#REFRN10240)

### SQL Changes

Starting with Oracle Database 10g Release 1 (10.1), CLOB <-> NCLOB implicit conversion in SQL and PL/SQL is allowed.

Starting with Oracle Database 10g Release 1 (10.1), name resolution for synonyms has changed. If the base object of a synonym does not exist, then the SQL compiler now tries looking up `PUBLIC.base_object`.

Starting with Oracle Database 10g Release 1 (10.1), VPD policies are attached to synonyms rather than the base objects.

### Invalid Synonyms After an Upgrade

Starting with Oracle Database 10g Release 1 (10.1), if a synonym (public or private) is pointing to an object that does not exist or is invalid, then the synonym is invalid after the upgrade.

### Manageability

Database performance statistics are now automatically collected by the Automatic Workload Repository (AWR) database component for databases upgraded from a release earlier than Oracle Database 10g Release 1 (10.1) and for newly created databases. This data is stored in the `SYSAUX` tablespace, and is used by the database for automatic generation of performance recommendations.

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/autostat.htm#PFGRF02601)

If you currently use Statspack for performance data gathering, then refer to the Statspack README `(spdoc.txt`, located in the ORACLE\_HOME/rdbms/admin directory) for directions on using Statspack in Oracle Database 10g Release 1 (10.1) and later releases to avoid conflict with the AWR.

### Transaction and Space

Starting with Oracle Database 10g Release 1 (10.1), dropped objects are now moved to the recycle bin where the space is only reused when it is needed. This allows an object to be undropped using the `FLASHBACK DROP` feature.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/tables.htm#ADMIN01511)

Starting with Oracle Database 10g Release 1 (10.1), automatic tuning of undo retention is enabled by default. The `UNDO_SUPPRESS_ERRORS` initialization parameter has been deprecated. Errors generated when executing rollback segment operations while in automatic undo management mode are always suppressed.

Starting with Oracle Database 10g Release 1 (10.1), the default `AUTOEXTEND NEXT` size is larger for Oracle managed files (OMF).

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm)

### Recovery and Data Guard

Starting with Oracle Database 10g Release 1 (10.1), the `LOG_ARCHIVE_START` initialization parameter has been deprecated. Archiving is now automatically started when the database is placed in `ARCHIVELOG` mode.

Starting with Oracle Database 10g Release 1 (10.1), the `LOG_PARALLELISM` initialization parameter has been deprecated. Log file parallelism is now automatically enabled.

Starting with Oracle Database 10g Release 1 (10.1), the default value for the `RECOVERY_PARALLELISM` initialization parameter now defaults to allow parallel recovery.

Starting with Oracle Database 10g Release 1 (10.1), the default value for the parallel clause in the `ALTER DATABASE RECOVER DATABASE` statement has changed to `PARALLEL`.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm)

Starting with Oracle Database 10g Release 1 (10.1), the default buffer size for the `ASYNC` attribute of the `LOG_ARCHIVE_DEST_` `n` initialization parameter has increased from 2,048 blocks to 61,440 blocks.

Starting with Oracle Database 10g Release 1 (10.1), the default values of the parameters `MAX_SGA` and `MAX_SERVERS` as set by the `DBMS_LOGSTDBY.APPLY_SET()` procedure have changed.

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_lsbydb.htm#ARPLS363)

Starting with Oracle Database 10g Release 1 (10.1), the default values for the Data Guard broker properties `ApplyParallel`, `AsyncBlocks`, and `LogXptMode` have changed.

See Also:

[Oracle Data Guard Broker](https://docs.oracle.com/cd/E11882_01/server.112/e40771/dbpropref.htm#DGBKR805)

Starting with Oracle Database 10g Release 1 (10.1), the default behavior of the `STARTUP` SQL\*Plus command and the `ALTER DATABASE MOUNT` and `ALTER DATABASE OPEN` SQL statements have changed for physical standby databases. The commands now automatically detect that the database is a physical standby and thus the `STANDBY DATABASE` and `READ ONLY` options are made default.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm)

### RMAN

Starting with Oracle Database 10g Release 1 (10.1), RMAN now creates an empty file when restoring a file from backup and no backup of the file exists. RMAN backup of archived logs now automatically backs up logs that were created before the last resetlogs. Such logs were previously ignored.

Starting with Oracle Database 10g Release 1 (10.1), RMAN now continues to run the remaining portions of a backup or restore job when it encounters an error. RMAN now tries to restore from an alternate backup if it finds the targeted backup is corrupt.

### CREATE DATABASE

In Oracle Database 10g Release 1 (10.1) and later releases, a `SYSAUX` tablespace is always created at database creation time or whenever a database is upgraded. The `SYSAUX` tablespace serves as an auxiliary tablespace to the `SYSTEM` tablespace. Because `SYSAUX` is the default tablespace for many Oracle features and products that previously required their own tablespaces, it reduces the number of tablespaces that a DBA must maintain.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/create.htm#ADMIN00203) for more information about the `SYSAUX` tablespace

Starting with Oracle Database 10g Release 1 (10.1), the minimum and default log file sizes have increased. The minimum size is now 4 MB. The default size is 50 MB, unless using Oracle managed files (OMF) in which case the default is 100 MB.

### Oracle Real Application Clusters

In Oracle Database 10g Release 1 (10.1), there is an automated high availability (HA) framework for Oracle Real Application Clusters. The framework provides detection, recovery, restart, and notification services.

See Also:

[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/toc.htm) for more information

### Materialized Views

Starting with Oracle Database 10g Release 1 (10.1), some privilege name changes have been made. The new names appear in all data dictionary views, but both the old and new names are accepted by the `GRANT` and `REVOKE` SQL statements.

- `CREATE SNAPSHOT` changed to `CREATE MATERIALIZED VIEW`
- `CREATE ANY SNAPSHOT` changed to `CREATE ANY MATERIALIZED VIEW`
- `ALTER ANY SNAPSHOT` changed to `ALTER ANY MATERIALIZED VIEW`
- `DROP ANY SNAPSHOT` changed to `DROP ANY MATERIALIZED VIEW`

### Change Data Capture

Starting with Oracle Database 10g Release 1 (10.1), the interfaces in `DBMS_CDC_SUBSCRIBE` and `DBMS_CDC_PUBLISH` now take a subscription name parameter instead of a subscription handle.

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm)

Starting with Oracle Database 10g Release 1 (10.1), subscriber views are now managed automatically. There is no longer any requirement to call the `DBMS_CDC_SUBSCRIBE` and `DBMS_CDC_PUBLISH` interfaces `PREPARE_SUBSCRIBER_VIEW()` and `DROP_SUBSCRIBER_VIEW()`.

Starting with Oracle Database 10g Release 1 (10.1), the computation of synchronous Change Data Capture's `RSID$` column has been changed to facilitate joining a subscriber view to itself in order to show both old and new values in the same row. The `RSID$` values for the `UO` and `UN` rows associated with the same update operation are now the same. To revert to the Oracle9i behavior where `UN` `RSID$` value is `UO` `RSID$` value + `1` for the same update operation, set event `10983` to level `4`.

### Change in the Default Archival Processing to Remote Archive Destinations

Starting with Oracle Database 10g Release 1 (10.1), the default archival processing to remote destinations has changed so that archiver processes on the primary database completely and successfully archive the local online redo log files before transmitting the redo data to remote standby destinations. This default behavior is equivalent to setting the `LOG_ARCHIVE_LOCAL_FIRST` initialization parameter to `true`, which is also new in Oracle Database 10g Release 1 (10.1) and later releases. Note that this new default archival processing is relevant only when log transport services are defined to use archiver processes (ARCn), not the log writer process (LGWR), when the archiver processes are writing to remote destinations, and when the remote standby destination is not a mandatory destination.

Before Oracle Database 10g Release 1 (10.1), the default behavior was to transmit redo data to the standby destination at the same time the online redo log file was being archived to the local online redo log files. You can achieve this behavior by setting the `LOG_ARCHIVE_LOCAL_FIRST` initialization parameter to `false`. This archival processing is also relevant only when log transport services are defined to use archiver processes (ARCn), not the log writer process (LGWR), when the archiver processes are writing to remote destinations, and when the remote standby destination is not a mandatory destination.

The benefit of the new default behavior is that local archiving, and hence, processing on the primary database, are not affected by archival to non-mandatory, remote destinations. Because local archiving is now disassociated with remote archiving, sites that might have policies to delete archived redo log files on the primary database immediately after backing them up must make sure that the standby destinations have received the corresponding redo data before deleting the archived redo log files on the primary database. You can query the `V$ARCHIVED_LOG` view to verify that the redo data has been received on standby destinations.

Note:

Any value specified for the `LOG_ARCHIVE_LOCAL_FIRST` initialization parameter is ignored for mandatory destinations (configured with the `MANDATORY` attribute of the `LOG_ARCHIVE_DEST_` `n` initialization parameters).

See Also:

[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/log_transport.htm#SBYDB00400) for complete information about setting up archival to remote destinations

### Limitations on NCHAR Data Types

Starting with Oracle9i, the `NCHAR` data types such as `NCHAR`, `NVARCHAR2`, and `NCLOB`, are limited to the Unicode character set encoding, `UTF8` and `AL16UTF16`.

### PL/SQL Native Compilation

Starting with Oracle Database 10g Release 1 (10.1), the configuration of initialization parameters and the command setup for native compilation has been simplified. The important parameters now are `PLSQL_NATIVE_LIBRARY_DIR` and `PLSQL_NATIVE_LIBRARY_SUBDIR_COUNT`. The parameters related to the compiler, linker, and make utility have been made obsolete. Native compilation is turned on and off by a separate initialization parameter, `PLSQL_CODE_TYPE`, rather than being one of several options in the `PLSQL_COMPILER_FLAGS` parameter, which is now deprecated. The `spnc_commands` file, located in the ORACLE\_HOME/plsql directory, contains the commands and options for compiling and linking, rather than a makefile.

See Also:

- [Oracle Database PL/SQL Language Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e25519/tuning.htm#LNPLS01209) for further information about compiling PL/SQL code for native execution
- "PL/SQL Native Compilation (NCOMP) In Oracle Database 10g Rel 1" on the Oracle Technology Network (OTN):
	```
	http://www.oracle.com/technetwork/database/features/plsql/index.html
	```

### Evaluation of Numeric Literals

Evaluation of numeric literals has changed such that at least one of the constants in a numeric computation with literals must be a decimal specified to the 10th place. This is because releases after Oracle Database 10g Release 1 (10.1) use `INTEGER` arithmetic (approximately 9 significant digits) for some expressions whereas Oracle9i Release 2 (9.2) used `NUMBER` arithmetic (approximately 38 significant digits).

Therefore, if you are dealing with results of greater than 9 significant digits, then one of the literals should be in decimal format to prevent numeric overflow errors. For example, in Oracle Database 10g Release 1 (10.1), the computation of `v1` in the following example causes a numeric overflow error:

```
DECLARE
  v1 NUMBER(38);
BEGIN
  v1 := 256*256*256*256;
  DBMS_OUTPUT.PUT_LINE(v1);
END;
/
```

The solution to the error is to specify one of the numeric literals as a decimal (256.0), as follows:

```
DECLARE
  v1 NUMBER(38);
BEGIN
  v1 := 256*256*256*256.0;
  DBMS_OUTPUT.PUT_LINE(v1);
END;
/
```

See Also:

- The "What's New in SQL\*Plus" section in the [SQL\*Plus User's Guide and Reference](https://docs.oracle.com/cd/E11882_01/server.112/e16604/toc.htm) to learn about new features in SQL\*Plus
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/toc.htm) for more information about upgrading SQL scripts

### Change in Behavior for SESSION\_CACHED\_CURSORS

Starting with Oracle Database 10g Release 1 (10.1), the number of cached cursors is determined by the `SESSION_CACHED_CURSORS` initialization parameter. In previous Oracle Database releases, the number of SQL cursors cached by PL/SQL was determined by the `OPEN_CURSORS` initialization parameter.

See Also:

`SESSION_CACHED_CURSORS` in [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams232.htm#REFRN10195)

### New Default Value for DB\_BLOCK\_SIZE

Starting with Oracle Database 10g Release 1 (10.1), the default value of `DB_BLOCK_SIZE` is operating system specific, but is typically 8 KB (8192 bytes). In previous Oracle Database releases, the default value was 2 KB (2048 bytes). If `DB_BLOCK_SIZE` is not specified in the parameter file when upgrading from Oracle9i Release 2 (9.2), then you receive an error when attempting to start up your database. Add the following to your parameter file:

```
DB_BLOCK_SIZE = 2048
```

If `DB_BLOCK_SIZE` is specified in the parameter file, then Oracle Database uses this value instead of the default value of 8 KB.

### OPTIMIZER\_MAX\_PERMUTATIONS and OPTIMIZER\_FEATURES\_ENABLE

Starting with Oracle Database 10g, the `OPTIMIZER_MAX_PERMUTATIONS` initialization parameter has been made obsolete. If you are upgrading from Oracle9i and have `OPTIMIZER_FEATURES_ENABLE` set to `8.1.7` or earlier and `OPTIMIZER_MAX_PERMUTATIONS` explicitly set to `2000` in the parameter file, then the release 8.1.7 default of `80000` is used when you start up the Oracle Database 11g Release 1 (11.1) database.

Setting `OPTIMIZER_FEATURES_ENABLE` to `9.0.0` or higher sets the default to `2000`

### Change in Behavior for LOG\_ARCHIVE\_FORMAT

Starting with Oracle Database 10g Release 1 (10.1), if the `COMPATIBLE` initialization parameter is set to `10.0.0` or higher, then archive log file names must contain each of the elements `%s` (sequence), `%t` (thread), and `%r` (resetlogs ID) to ensure that all archive log file names are unique. If the `LOG_ARCHIVE_FORMAT` initialization parameter is set in the parameter file, then make sure the parameter value contains the `%s`, `%t`, and `%r` elements.

### New Default Value for PGA\_AGGREGATE\_TARGET

Starting with Oracle Database 10g Release 1 (10.1), Automatic PGA Memory Management is now enabled by default (unless `PGA_AGGREGATE_TARGET` is explicitly set to `0` or `WORKAREA_SIZE_POLICY` is explicitly set to `MANUAL`). `PGA_AGGREGATE_TARGET` defaults to 20% of the size of the SGA, unless explicitly set. Oracle recommends tuning the value of `PGA_AGGREGATE_TARGET` after upgrading.

See Also:

[Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/memory.htm#PFGRF01401)

### Change in Behavior for SHARED\_POOL\_SIZE

In previous releases, the amount of shared pool memory that was allocated was equal to the value of the `SHARED_POOL_SIZE` initialization parameter plus the amount of internal SGA overhead computed during instance startup. Starting with Oracle Database 10g Release 1 (10.1), the value of `SHARED_POOL_SIZE` must now also accommodate this shared pool overhead.

Since Oracle Database release 9.2, the shared pool can be partitioned into multiple parts. The partitions are called shared pool subpools and there can be up to seven subpools. Although there is no standard recommendation, you should configure the shared pool memory in a way that generates larger subpools than the default size. For example, 256M and 500M seem to work better as subpool sizes for Oracle Database releases 9i and 10g, respectively. Having adequate sizes allocated for shared pool subpools can avoid raising ORA-4031 errors.

### Shared Server Parameters

Starting with Oracle Database 10g Release 1 (10.1), the recommended way to turn on shared server mode is to set `SHARED_SERVERS` to a value greater than `0`. This can be done at startup or dynamically after the instance is started. If shared server mode is turned off by setting `SHARED_SERVERS` to `0`, then this only affects new clients (that is, no new clients can connect in shared mode; clients that are already connected in shared mode continue to be serviced by shared servers).

In previous releases, the recommended way to turn on shared server mode was to set `DISPATCHERS`. If `SHARED_SERVERS` was changed to `0` and shared server clients were still connected, then client requests would hang.

Before Oracle Database 10g Release 1 (10.1), the following shared server parameters could not be changed dynamically:

- `MAX_SHARED_SERVERS`
- `MAX_DISPATCHERS`
- `SHARED_SERVER_SESSIONS`
- `CIRCUITS`

Starting with Oracle Database 10g Release 1 (10.1), these shared server parameters are dynamically modifiable.

#### New Default Value for DISPATCHERS

Starting with Oracle Database 10g Release 1 (10.1), the default for `DISPATCHERS` is `'(PROTOCOL=TCP)'`. `DISPATCHERS` is given this default value if it is not set or if it is set to `''` and `SHARED_SERVERS` is set to `1` or higher.

In previous releases, there was no default value for `DISPATCHERS`.

#### New Default Value for SHARED\_SERVERS

Starting with Oracle Database 10g Release 1 (10.1), if `DISPATCHERS` is set such that the total number of dispatchers is equal to 0, then `SHARED_SERVERS` defaults to `0`. If `DISPATCHERS` is set such that the total number of dispatchers is greater than 0, then `SHARED_SERVERS` defaults to `1` as in previous releases.

In previous releases, if `DISPATCHERS` was set such that the number of dispatchers is equal to 0, then `SHARED_SERVERS` defaulted to `1`.

#### New Default Value for MAX\_SHARED\_SERVERS

Starting with Oracle Database 10g Release 1 (10.1), there is no preset default for `MAX_SHARED_SERVERS`. The maximum number of shared servers varies depending on the number of free process slots. If `MAX_SHARED_SERVERS` is not set or is set to a value greater than or equal to `PROCESSES`, then PMON does not spawn any more shared servers if the number of free process slots is either 2 (if `PROCESSES` is less than `24`) or is less than 1 / 8, unless the existing servers are involved in a deadlock situation. If the existing servers are involved in a deadlock situation, then no matter the transaction load, a new server is spawned if there is a free process slot.

In previous releases, the default for `MAX_SHARED_SERVERS` is `20`, or 2 \* `SHARED_SERVERS`, whichever is greater, subject to the condition that `MAX_SHARED_SERVERS` does not exceed `PROCESSES`.

Starting with Oracle Database 10g Release 1 (10.1), `SHARED_SERVERS` can be set higher than `MAX_SHARED_SERVERS`, in which case the number of servers remains constant at the level set for `SHARED_SERVERS`. This is to allow the range `SHARED_SERVERS` - `MAX_SHARED_SERVERS` to be changed without having to change these parameters in a specific order.

In previous releases, `SHARED_SERVERS` cannot be set higher than `MAX_SHARED_SERVERS`.

#### New Default Value for SHARED\_SERVER\_SESSIONS

Starting with Oracle Database 10g Release 1 (10.1), there is no preset default for `SHARED_SERVER_SESSIONS`. That is, if `SHARED_SERVER_SESSIONS` is not specified, then shared server sessions can be created as needed and as permitted by the session limit.

In previous releases, the default for `SHARED_SERVER_SESSIONS` was the maximum number of virtual circuits (`CIRCUITS`), or the maximum number of database sessions (`SESSIONS`) - `5`, whichever is smaller.

#### New Default Value for CIRCUITS

Starting with Oracle Database 10g Release 1 (10.1), there is no preset default for `CIRCUITS`. That is, if `CIRCUITS` is not specified, then circuits can be created as needed and as permitted by dispatcher constraints and system resources.

In previous releases, the default for `CIRCUITS` was the maximum number of database sessions (`SESSIONS`) if shared server mode was enabled, `0` otherwise.

#### New Default Value for MAX\_DISPATCHERS

Starting with Oracle Database 10g Release 1 (10.1), there is no preset default for `MAX_DISPATCHERS`. `MAX_DISPATCHERS` no longer limits the number of dispatchers; the user can increase the number of dispatchers with the `DISPATCHERS` parameter as long as there are free process slots and system resources.

In previous releases, the default for `MAX_DISPATCHERS` was `5`, or the total number of dispatchers specified with the `DISPATCHERS` parameter, whichever was greater.