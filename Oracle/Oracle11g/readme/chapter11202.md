---
title: Readme Information for Oracle Database 11g Release 2 (11.2.0.2)
book: Readme
doc_id: E41331-17
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/readmes.112/e41331/chapter11202.htm
tags:
  - oracle
  - 11g
  - readme
---

## 4 Readme Information for Oracle Database 11g Release 2 (11.2.0.2)

Note:

If you are on Oracle Database 11g release 2 (11.2.0.2), this is the Readme section that you need to read.

This section of the Readme contains the following sub-sections:

Section 4.1, "Nomenclature Changes"

Section 4.2, "Compatibility, Upgrading, Downgrading, and Installation"

Section 4.3, "Features Not Available or Restricted in 11.2.0.2"

Section 4.4, "Default Behavior Changes"

Section 4.5, "Oracle Automatic Storage Management (Oracle ASM)"

Section 4.6, "Oracle Enterprise Manager Database Control"

Section 4.7, "Database Security"

Section 4.8, "Encryption and Integrity"

Section 4.9, "Java and Web Services"

Section 4.10, "Media Management Software"

Section 4.11, "Oracle Application Express"

Section 4.12, "Oracle Client Applications"

Section 4.13, "Oracle Configuration Manager"

Section 4.14, "Oracle Data Mining"

Section 4.15, "Oracle Internet Directory"

Section 4.16, "Oracle Multimedia"

Section 4.17, "Oracle Net Services"

Section 4.18, "Oracle Real Application Clusters"

Section 4.19, "Oracle Grid Infrastructure for a Cluster"

Section 4.20, "Oracle ODBC Driver"

Section 4.21, "Oracle OLAP"

Section 4.22, "Oracle Spatial"

Section 4.23, "Oracle SQL Developer"

Section 4.24, "Oracle Text"

Section 4.25, "Oracle Ultra Search"

Section 4.26, "Oracle Warehouse Builder"

Section 4.27, "Oracle Workflow"

Section 4.28, "Oracle XML DB"

Section 4.29, "PL/SQL"

Section 4.30, "Pro\*C"

Section 4.31, "Pro\*COBOL"

Section 4.32, "SQLJ"

Section 4.33, "SQL\*Plus"

Section 4.34, "Summary Management"

Section 4.35, "Oracle Streams"

Section 4.36, "Open Bugs"

## 4.1 Nomenclature Changes

Note the following nomenclature changes:

- Flash Recovery Area has been renamed to Fast Recovery Area.
- The name Oracle interMedia was changed to Oracle Multimedia in Oracle Database 11g release 1 (11.1). The feature remains the same, only the name has changed.

## 4.2 Compatibility, Upgrading, Downgrading, and Installation

For late-breaking updates and best practices about preupgrade, post-upgrade, compatibility, and interoperability discussions, see Note 785351.1 on My Oracle Support (at `https://support.oracle.com`) that links to the "Upgrade Companion" web site for Oracle Database 11g release 2 (11.2).

Caution:

After installation is complete, do not manually remove or run `cron` jobs that remove `/tmp/.oracle` or `/var/tmp/.oracle` directories or their files while Oracle software is running. If you remove these files, then Oracle software can encounter intermittent hangs. Oracle Grid Infrastructure for a cluster and Oracle Restart installations fail with the following error:
```
CRS-0184: Cannot communicate with the CRS daemon.
```

### 4.2.1 Multiple Interconnects and Oracle ACFS

If you have Oracle ACFS file systems on Oracle Grid Infrastructure for a cluster 11g release 2 (11.2.0.1), you upgrade Oracle Grid Infrastructure to 11g release 2 (11.2.0.2), and you take advantage of Redundant Interconnect Usage and add one or more additional private interfaces to the private network, then you must restart the Oracle ASM instance on each upgraded cluster member node (reference Bug 9969133).

### 4.2.2 Deinstallation Restrictions

The following sections describe deinstallation and deconfiguration restrictions. See Section 4.36.2, "Deinstallation Tool Known Bugs" for additional information.

#### 4.2.2.1 Deinstall Upgraded 11.2 Oracle RAC and Oracle Grid Infrastructure for a Cluster Homes

in 11201, 11202, 11203

After you deconfigure and deinstall an upgraded Oracle Database 11g release 2 (11.2) Oracle RAC home and to deconfigure and deinstall an 11.2 Oracle Grid Infrastructure for a cluster home, you must detach any pre-11.2 Oracle RAC software homes from the central Inventory (reference Bug 8666509).

Detach the pre-11.2 Oracle RAC homes from the central inventory with the following command:

```
ORACLE_HOME/oui/bin/runInstaller -detachHome ORACLE_HOME_NAME=pre-11.2_ORACLE_HOME_NAME ORACLE_HOME=pre-11.2_ORACLE_HOME
```

#### 4.2.2.2 Error When Running Deinstallation from an Existing Oracle Home With the -home Option

If you try to run the `deinstall` tool from the product home with the `-home` option, then the deinstallation fails with the following error message:

```
$ ./deinstall -home /scratch/user_dir/oracle/product/11.2.0/dbhome_1
Error: invalid argument -home.
Since the tool is run from inside an Oracle Home it will deinstall the home
the tool is installed in. You cannot specify another home.
```

Because the `deinstall` tool is run from within an Oracle home, the `deinstall` tool cannot be run with the `-home` option. The `deinstall` tool can only be run as `./deinstall` from within an Oracle home.

### 4.2.3 Time Zone File Version

Oracle Database 11g release 2 (11.2) ships with time zone file versions 1 through 14. If your older database is using a time zone file version greater than 14, then you must obtain the corresponding time zone file patch for 11.2 prior to upgrading your database.

You can use `SELECT VERSION FROM V$TIMEZONE_FILE` to identify the time zone file version when upgrading your Oracle Database 10g or 11g databases. The Pre-Upgrade Information Tool (`utlu112i.sql` and its counterpart used by the Database Upgrade Assistant) provides a warning if the time zone file version is not version 11. The warning recommends running the `DBMS_DST` package to upgrade the database time zone version to the latest and to update `TIMESTAMP WITH TIME ZONE` data as well. The Pre-Upgrade Information Tool also populates three new database properties (`DST_PRIMARY_TT_VERSION`, `DST_SECONDARY_TT_VERSION`, and `DST_UPGRADE_STATE`) in `sys.database_properties` that are pertinent to the time zone version and its upgrade. `DST_PRIMARY_TT_VERSION` property records the actual time zone version in use. The other two database properties will be used when you upgrade your time zone version using `DBMS_DST` package.

Note that, in release 11.2.0.2, you have the option to retain your current time zone version after migrating to 11.2. For example, whether your application uses any `TIMESTAMP WITH TIME ZONE` type, you do not need to run the `DBMS_DST` package to upgrade your time zone version to the latest one available.

### 4.2.4 Oracle ASM Rolling Upgrade

Oracle Automatic Storage Management (Oracle ASM) rolling upgrade check does not allow rolling upgrade to be done from 11.1.0.6 to any later release (reference Bug 6872001). The following message is reported in the alert log:

```
Rolling upgrade from 11.1.0.6 (instance instance-number) to 11.x.x.x is not supported
```

`ORA-15156` is signalled by LMON which will then terminate the instance.

When trying to upgrade Oracle ASM from 11.1.0.6 to a later release of Oracle ASM, apply the patch for this bug to 11.1.0.6 instances before rolling upgrade starts. This patch can be applied to 11.1.0.6 instances in a rolling fashion.

### 4.2.5 UTC Time Zone Error When Upgrading From 9.2 to 11.2

When running upgrade scripts from Oracle9i Database release 2 (9.2) to Oracle Database 11g release 2 (11.2), you may encounter the following error:

```
ORA-27465: invalid value UTC for attribute DEFAULT_TIMEZONE
```

This error occurs because the default time zone file for release 9.2 does not have the coordinated universal time (UTC) zone. This message is produced by Oracle Scheduler that, by default, selects the UTC time zone and checks it against the default time zone file of release 9.2. This error message is expected and you can ignore it.

### 4.2.6 Tablespace and Fast Recovery Area Sizing

Note:

Fast Recovery was previously known as Flash Recovery.

The Oracle Database 11g Pre-Upgrade Information Utility (`utlu112i.sql`) estimates the additional space that is required in the `SYSTEM` tablespace and in any tablespaces associated with the components that are in the database (for example, `SYSAUX`, `DRSYS`) (reference Bug 13067061). For a manual upgrade, be sure to run this utility on your existing database prior to upgrading.

The tablespace size estimates may be too small, especially if Oracle XML DB is installed in your database. However, to avoid potential space problems during either a manual upgrade or an upgrade using the Database Upgrade Assistant (DBUA), you can set one data file for each tablespace to `AUTOEXTEND ON MAXSIZE UNLIMITED` for the duration of the upgrade.

If you are using file systems for data file storage, then be sure there is adequate space in the file systems for tablespace growth during the upgrade.

If you are using a Fast Recovery Area, then check that the size available is sufficient for the redo generated during the upgrade. If the size is inadequate, then an `ORA-19815` error will be written to the alert log, and the upgrade will stop until additional space is made available.

### 4.2.7 Memory Target for Oracle Database Instances

Running Database Configuration Assistant (DBCA) defaults to this Automatic Memory Management option. In the case of upgrade or manual database creation, `MEMORY_TARGET` can be specified in the initialization parameter file.

### 4.2.8 Upgrading a Database With Oracle Data Mining (ODM)

If you upgrade a database with the Data Mining option from 11.2.0.1 to 11.2.0.2, make sure that the `DMSYS` schema does not exist in your 11.2.0.1 database. If it does, you should drop the `DMSYS` schema and its associated objects from the database as follows:

```
SQL> CONNECT / AS SYSDBA;
SQL> DROP USER DMSYS CASCADE;
SQL> DELETE FROM SYS.EXPPKGACT$ WHERE SCHEMA = 'DMSYS';
SQL> SELECT COUNT(*) FROM DBA_SYNONYMS WHERE TABLE_OWNER = 'DMSYS';
```

If the above SQL returns non-zero rows, create and run a SQL script as shown in the following example:

```
SQL> SET HEAD OFF
SQL> SPOOL dir_path/DROP_DMSYS_SYNONYMS.SQL
SQL> SELECT 'Drop public synonym ' ||'"'||SYNONYM_NAME||'";' FROM DBA_SYNONYMS WHERE TABLE_OWNER = 'DMSYS'; 
SQL> SPOOL OFF
SQL> @dir_path/DROP_DMSYS_SYNONYMS.SQL
SQL> EXIT;
```

If you upgrade a database from 10g to 11.2, all Data Mining metadata objects are migrated from `DMSYS` to `SYS`. After the upgrade, when you determine that there is no need to perform a downgrade, set the initialization parameter `COMPATIBLE` to 11.2 and drop the `DMSYS` schema and its associated objects as described above.

### 4.2.9 Compatibility with Oracle9i Database Release 2

Connecting the Oracle Database 11g release 2 (11.2) client or server to Oracle9i Database release (9.2.0.4 and above) is supported. Similarly, connecting Oracle9i client (release 9.2.0.4 and above) to Oracle Database 11g release 2 (11.2) is supported.

### 4.2.10 Enabling Automated Backups

While installing Oracle Database, the Specify Backup and Recovery Options screen may appear truncated if your system does not have the required fonts installed. If your system has only fixed-width fonts, then you may not be able to fully specify the required information in the Backup Job Credentials area of the screen. To work around this issue, do not select Enable Automated Backups on this screen. After the installation is complete, use Oracle Enterprise Manager 11g Database Control to enable automated backups.

### 4.2.11 Upgrading a Database With SQL Access Advisor Tasks

Due to internal structural changes to the SQL Access Advisor repository, a database upgrade resets all of the existing SQL Access Advisor tasks to their initial state. This action effectively deletes all of the recommendation information for tasks that have been successfully completed prior to the upgrade.

After upgrading, the recommendation information can be restored by reexecuting the existing SQL Access Advisor tasks.

### 4.2.12 Downgrade to Release 11.1.0.6

If you anticipate downgrading back to release 11.1.0.6, then apply the patch for Bug 7634119. This action avoids the following `DBMS_XS_DATA_SECURITY_EVENTS` error:

```
PLS-00306: wrong number or types of arguments in call
to 'INVALIDATE_DSD_CACHE' DBMS_XS_DATA_SECURITY_EVENTS
PL/SQL: Statement ignored
```

Apply this patch prior to running `catrelod.sql`.

### 4.2.13 Rolling Upgrade for Oracle Clusterware

In Oracle Database 11g release 2 (11.2), there is a new prerequisite check during the rolling Oracle Clusterware upgrade cycle. On failure of this prerequisite check, the [Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/toc.htm) documents the following:

When upgrading Oracle Clusterware from Oracle Clusterware 10g release 2 (10.2) to Oracle Clusterware 11g release 2 (11.2), you must first apply the patchset version 10.2.0.3.0 or later to your existing Oracle Clusterware before it can be upgraded.

Follow the rolling upgrade procedure in Appendix F.5.1 of the [Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=CWGEN).

Apart from this proposed solution, there is an alternative. You can upgrade all of the nodes of the cluster simultaneously in a non-rolling manner. Choosing this solution voids the 10.2.0.3.0 patchset requirement.

### 4.2.14 Upgrading With Objects in the Recycle Bin

The recycle bin must be empty during an upgrade to avoid possible `ORA-00600` deadlock errors, as well as to minimize the time required to perform the upgrade (reference Bug 8632581).

To avoid this deadlock, use the `PURGE DBA_RECYCLEBIN` statement to remove items and their associated objects from the recycle bin and release their storage space prior to upgrading your database.

### 4.2.15 Oracle ACFS Registry May Be in an Inconsistent State After Installing or Upgrading to 11.2.0.2.0 or After An Oracle Clusterware Restart

The `ora.acfs.registry` resource may be in an inconsistent state after installing or upgrading to 11.2.0.2.0 or after an Oracle Clusterware restart (reference Bug 9876173 and Bug 9864447):

- After completing a new 11.2.0.2.0 installation, if the voting disk or the Oracle Cluster Registry (OCR) or both are on Oracle ASM, then `ora.registry.acfs` will have the following values:
	```
	./crsctl status resource ora.registry.acfs 
	 NAME=ora.registry.acfs 
	 TYPE=ora.registry.acfs.type 
	 TARGET=ONLINE, ONLINE 
	 STATE=ONLINE, ONLINE
	```
	(Note that `ora.asm` will be in `STATE ONLINE`, `TARGET ONLINE`.)
	However, if the voting disk or the Oracle Cluster Registry (OCR) or both are not on Oracle ASM, then `ora.registry.acfs` will have the following values:
	```
	./crsctl status resource ora.registry.acfs 
	 NAME=ora.registry.acfs 
	 TYPE=ora.registry.acfs.type 
	 TARGET=ONLINE , ONLINE 
	 STATE=OFFLINE, OFFLINE
	```
	(Note that `ora.asm` will be in `STATE OFFLINE`, `TARGET OFFLINE`.)
- After completing an upgrade from 11.2.0.1.0 to 11.2.0.2.0, `TARGET` and `STATE` for `ora.registry.acfs` will be set to the value they were in 11.2.0.1.0, prior to upgrading to 11.2.0.2.0.
- At any time, if Oracle Clusterware is restarted, `ora.registry.acfs` will have the following values:
	```
	./crsctl status resource ora.registry.acfs 
	 NAME=ora.registry.acfs 
	 TYPE=ora.registry.acfs.type 
	 TARGET=ONLINE , ONLINE 
	 STATE=ONLINE, ONLINE
	```
	(Note that `ora.asm` will be in `STATE ONLINE`, `TARGET ONLINE`.)

It is not necessary to take any action, however, if desired, to disable Oracle ACFS, enter the command `acfsroot unregister`, which will remove the `ora.registry` (and `ora.drivers`) resources completely.

### 4.2.16 Oracle ACFS File Systems Must be Manually Dismounted Prior to Upgrade, Deinstallation, or Direct Shutdown of Oracle Clusterware or Oracle ASM

Oracle ACFS file systems must be manually dismounted prior to upgrade, deinstallation, or direct shutdown of Oracle Clusterware or Oracle ASM. Also, manually dismount non-Oracle ACFS file systems which are running over Oracle ASM Dynamic Volume Manager (Oracle ADVM). This is also recommended when rebooting the system (reference Bug 8594128, Bug 9547527, and Bug 9777741).

When doing an upgrade, deinstallation, or direct shutdown of Oracle Clusterware or Oracle ASM, to ensure that Oracle Clusterware (or Oracle ASM) comes down cleanly, you must dismount all Oracle ACFS file systems manually prior to Oracle Cluserware shutdown. Use the `lsof` and `fuser` commands (Linux and UNIX) or the `handle` and `wmic` commands (Windows) to identify processes which are active on the Oracle ACFS file systems. To ensure that these processes are no longer active, dismount all Oracle ACFS file systems and issue Oracle Clusterware shutdown. Otherwise errors may be issued during Oracle Clusterware shutdown relating to activity on Oracle ACFS file systems which will stop the successful shutdown of Oracle Clusterware.

### 4.2.17 Data Pump Export Operations Do Not Work if the DMSYS Schema is Not Removed as Part of the Upgrade to 11.2.0.2

Data Pump Export operations do not work if the `DMSYS` schema is not removed as part of the upgrade to 11.2.0.2 (reference Bug 10007411). The reported error is similar to the following:

```
Processing object type SCHEMA_EXPORT/TABLE/TABLE_DATA 
ORA-39126: Worker unexpected fatal error in 
KUPW$WORKER.GET_TABLE_DATA_OBJECTS [] 
ORA-31642: the following SQL statement fails: 
BEGIN "DMSYS"."DBMS_DM_MODEL_EXP".SCHEMA_CALLOUT(:1,0,1,'10.01.00.05.00'); 
END; 
ORA-06512: at "SYS.DBMS_SYS_ERROR", line 86 
ORA-06512: at "SYS.DBMS_METADATA", line 1245 
ORA-04063: package body "DMSYS.DBMS_DM_MODEL_EXP" has errors 
ORA-06508: PL/SQL: could not find program unit being called:   
"DMSYS.DBMS_DM_MODEL_EXP"
```

The pre-upgrade checks for 11.2.0.2 report the action that should be taken before the upgrade:

```
The DMSYS schema exists in the database. Prior to performing an upgrade Oracle recommends that the DMSYS schema, and its associated objects be removed from the database. Refer to the Oracle Data Mining Administration Guide for the instructions on how to perform this task.
```

Until this step is taken, Data Pump Export will not work.

### 4.2.18 catrelod.sql Fails if the Time Zone File Version Used by the Database Does Not Exist in Oracle Home

The following error is returned when `catrelod.sql` is run as part of the downgrade process if you previously installed a recent version of the time zone file and used the `DBMS_DST` PL/SQL package to upgrade `TIMESTAMP WITH TIME ZONE` data to that version (reference Bug 9803834):

```
ORA-00600: internal error code, arguments: [qcisSetPlsqlCtx:tzi init], 
 [], [], [], [], [], [], [], [], [], [], []
```

See Step 2 of 'Downgrade the Database' in Chapter 6 of the [Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/downgrade.htm#UPGRD12556) for more details.

If you previously installed a recent version of the time zone file and used the `DBMS_DST` PL/SQL package to upgrade `TIMESTAMP WITH TIME ZONE` data to that version, then you must install the same version of the time zone file in the release to which you are downgrading. For example, the latest time zone files that are supplied with Oracle Database 11g release 2 (11.2) are version 14. If, after the database upgrade, you had used `DBMS_DST` to upgrade the `TIMESTAMP WITH TIME ZONE` data to version 14, then install the version 14 time zone file in the release to which you are downgrading. This ensures that your `TIMESTAMP WITH TIME ZONE` data is not logically corrupted during retrieval. To find which version your database is using, query `V$TIMEZONE_FILE`.

Also see the [Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/toc.htm) for more information on installing time zone files.

### 4.2.19 Error Downgrading from 11.2.0.2 to 10.2.0.5

During 10.2.0.5 downgrade from 11.2.0.2, `catrelod.sql` fails with the following internal error (reference Bug 9975586):

```
ORA-00600: internal error code, arguments: [17069]
```

To workaround this problem, add the following to the initialization parameter file:

```
event='logon trace name kra_options level 7'
```

If using `spfile`, issue the following command:

```
alter system set event='logon trace name kra_options level 7' scope=spfile;
```

Restart the instance and continue running the downgrade script. After downgrade, remove the event from the initialization parameter file.

### 4.2.20 Downgrading a Database Having Database Control Configured

Consider the following when downgrading the database while having Database Control configured (reference Bug 9922349):

1. If you are upgrading from 11.2.0.1 to 11.2.0.2 and then plan to downgrade to 11.2.0.1, you need to apply the following patches in order to downgrade Database Control as part of the database downgrade:
	- 11.2.0.1 PSU2 bundle
		- One-off patch for Bug 8795792
		- One-off patch for Bug 10013976
	Without these patches, the `emdwgrd` utility would fail with `IMPORT` (`impdp`) errors when restoring Database Control data.
2. When running `emdwgrd` on 11.2.0.1 Oracle RAC databases, you may need to pass an additional parameter, `-serviceAlias`, if you do not have system identifier (SID) aliases defined in `tnsnames.ora`. This is also needed for single instance if SID and database names are different. For example:
	```
	emdwgrd -save [-cluster] -sid SID [-serviceAlias tns_alias] -path save_directory 
	emdwgrd -restore -tempTablespace TEMP [-cluster] -sid SID [-serviceAlias tns_alias] -path save_directory
	```
3. In the case of in-place downgrade from 11.2.0.2 to 11.2.0.1 using the same Oracle home, you do not need to run `emca -restore` before running `emdwngrd -restore`.

## 4.3 Features Not Available or Restricted in 11.2.0.2

The following is a list of components that are not available or are restricted in Oracle Database 11g release 2 (11.2.0.2):

- Patching from Database Control is deprecated and no longer available.
- Oracle Database release 11.2.0.1 upgrade to 11.2.0.2 clusterware is not supported if the 11.2.0.1 Oracle Grid Infrastructure for a cluster is installed in a non-shared Oracle home and 11.2.0.2 Oracle Grid Infrastructure for a cluster is installed in a shared Oracle home (reference Bug 10074804). Both 11.2.0.1 and 11.2.0.2 should be installed in either a shared or non-shared Oracle home.
- All Oracle Grid Infrastructure patch set upgrades must be out-of-place upgrades, in which case you install the patch set into a new Oracle Grid home (reference Bug 10210246). In-place patch set upgrades are not supported.
- Database Smart Flash Cache is supported on Solaris and Oracle Linux only.
- Using Internet Protocol Version 6 (IPv6) is not supported with the following:
	- Oracle RAC and Oracle Clusterware
		- Oracle Fail Safe
- Oracle Ultra Search has been desupported and is not shipping with Oracle Database 11g Release 2 (11.2).
- Downgrading from Oracle Database 11g release 2 (11.2) to release 10.2.0.3 or release 10.2.0.4 is not supported with Oracle Database Vault.
- Oracle Automatic Storage Management Cluster File System (Oracle ACFS) resources are not supported for Oracle Restart configurations on all platforms. Oracle ACFS drivers must be manually unloaded and loaded; Oracle ACFS file systems must be manually unmounted and mounted (after the Oracle ASM instance is running); Oracle ACFS database home file systems can be placed into the Oracle ACFS mount registry to be mounted along with other registered Oracle ACFS file systems.
- Oracle ACFS Replication is not supported in Oracle Restart.
- Refer to Section 4.10.1 for globalization restrictions within Oracle Secure Backup.
- Refer to Section 4.14 for features that are no longer available in Oracle Data Mining.
- Security-Enhanced Linux (SELinux) is not supported on Oracle Automatic Storage Management Cluster File System (Oracle ACFS) file systems.

The following sections discuss additional restrictions.

### 4.3.1 Database Object Names

Oracle does not recommend using quoted identifiers for database object names. These quoted identifiers are accepted by SQL\*Plus, but they may not be valid when using other tools that manage database objects.

## 4.4 Default Behavior Changes

This section describes some of the differences in behavior between Oracle Database 11g release 2 (11.2) and previous releases. The majority of the information about upgrading and downgrading is already included in the [Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/toc.htm).

### 4.4.1 Direct Insert Behavior Change

Direct insert requires memory for every partition loaded. The memory usage is even greater if the partitions are compressed. In previous releases, a direct insert would continue to allocate memory as rows were encountered for previously untouched partitions until all of the partitions were loaded or until it ran out of memory. In this case, the insert fails.

Starting in Oracle Database 11g release 2 (11.2), direct insert limits the memory that is allocated. If direct insert reaches the limit and it acquires rows for partitions that have not been loaded during the insert, then direct load stores those rows in the temporary tablespace. Once all rows have been passed in, direct load will load the rows it stored in the temporary tablespace.

### 4.4.2 Audit Default Behavior Changes

Default Audit behavior changes include:

- Audit filename is now prefixed with the instance name and ends with a sequence number. For example:
	```
	instanceName_ora_pid_seqNumber.aud / instanceName_ora_pid_seqNumber.xml
	```
- An existing audit file is never appended to. If an audit file already exists, the sequence number is incremented and written to `instanceName_ora_pid_seqNumber+1``.aud`.
- There is a preconfigured threshold for audit file growth. The audit file associated with an active session remains open until one of the following limits is reached:
	- After the audit record is written, the audit file size becomes 10 megabytes or more.
		- After the audit record is written, the audit file age becomes 5 days or more.
	Once one of these thresholds is reached, a new audit file with an incremented sequence number is opened for further audit records.
- There are no updates to `AUD$` anymore.
	- All logoff (action# 101) audit records are written separately.
		- If an event is audited `BY SESSION`, then every occurrence of the event becomes a new audit record in `AUD$`.

### 4.4.3 FILE\_ACCESS\_ROLE Default Behavior Change

The default behavior of the CTX system parameter `FILE_ACCESS_ROLE` has changed (reference Bug 8360111). Customers with existing Oracle Text indexes that use the file or URL datastore must take action to continue to use the indexes without error. The changes are as follows:

- If `FILE_ACCESS_ROLE` is null (the default), then access is not allowed. By default, users who were previously able to create indexes of this type will not be able to create these indexes after the change.
- `FILE_ACCESS_ROLE` is now checked for index synchronization and document service operations. By default, users will not be able to synchronize indexes of this type or use document service calls such as `ctx_doc.highlight` who were allowed to prior to this change.
- Only SYS will be allowed to modify `FILE_ACCESS_ROLE`. Calling `ctx_adm.set_parameter (FILE_ACESS_ROLE,` `role_name``)` as a user other than SYS will now raise the new error:
	```
	DRG-10764: only SYS can modify FILE_ACCESS_ROLE
	```
- Users can set `FILE_ACCESS_ROLE` to `PUBLIC` to explicitly disable this check (which was the previous default behavior).

### 4.4.4 Support for Raw Devices

Oracle Universal Installer (OUI) and Database Configuration Assistant (DBCA) do not support raw devices (or block devices on Linux). However, command-line utilities such as SQL\*Plus and CRSCTL do support raw or block devices.

### 4.4.5 Oracle Clusterware and Oracle ASM Installed Into Oracle Grid Infrastructure for a Cluster Home

Oracle Clusterware and Oracle Automatic Storage Management (Oracle ASM) are installed into a single Oracle home called the `Grid_home`. This installation is referred to as the Oracle Grid Infrastructure for a cluster installation.

When upgrading, you must upgrade both Oracle Clusterware and Oracle ASM at the same time.

### 4.4.6 Deprecated Parameters in the Oracle ASM Instance

The following initialization parameters are deprecated in the Oracle ASM instance:

- `CLUSTER_DATABASE` parameter
	If the `INSTANCE_TYPE` is Oracle ASM and the Oracle RAC option is turned on, then you do not have to specify the `CLUSTER_DATABASE` parameter. In this case, the `CLUSTER_DATABASE` parameter defaults to `TRUE`.
- `COMPATIBLE` parameter
	Do not set the `COMPATIBLE` parameter in an Oracle ASM instance. To advance the disk group compatibility, change the  
	`COMPATIBLE.[RDBMS|ASM|ADVM]` attributes of the disk group.

### 4.4.7 Fixed Views

All parameter views (for example, `V$PARAMETER`) in the Oracle ASM instance only report parameters that are relevant to the Oracle ASM instance.

### 4.4.8 Offset for CLOB and NCLOB APIs

Starting with Oracle Database 10g release 1 (10.1), APIs that write to a `CLOB` or `NCLOB` cause error `ORA-22831` when the offset specified for the beginning of the write is not on a character boundary of the existing `LOB` data.

`LOB` APIs use UCS2 codepoint semantics for the amount and offset parameters on `CLOBs` or `NCLOBs` when the database default or national character set is multibyte. The specified offset is not on a character boundary if it points to the low (second) surrogate of a surrogate pair. In such situations, error `ORA-22831` occurs and the data is not written. Thus, this prevents the corruption of the character in the target `LOB`.

Contact Oracle Support Services to configure the database so that it does not return `ORA-22831`.

### 4.4.9 Use of the Append Hint Runs Out of Memory When Loading Many Partitions

Use of direct-path `INSERT` to load a large number of partitions can exceed memory limits, especially when data compression is specified (reference Bug 6749894). Starting in 11.2, the number of partitions loaded at the same time will be limited, based on the `PGA_AGGREGATE_TARGET` initialization parameter, to preserve memory. Rows that are not stored in the partitions that are currently being loaded are saved in the temporary tablespace. After all rows are loaded for the current set of partitions, other partitions are loaded from rows that are saved in the temporary tablespace.

This behavior helps prevent the direct-path `INSERT` from terminating because of insufficient memory.

### 4.4.10 Non-Uniform Memory Access Optimizations and Support Disabled in 11.2

With Oracle Database 11g release 2 (11.2), non-uniform memory access support is disabled by default. This restriction applies to all platforms and operating systems (reference Bug 8450932).

Non-uniform memory access optimizations and support in the Oracle Database are only available for specific combinations of Oracle version, operating systems, and platforms. Work with Oracle Support Services and your hardware vendor to enable non-uniform memory access support.

### 4.4.11 View Changes for Advanced Compression

The `COMPRESS_FOR` column in various table views, such as `user_tables` and `dba_tables`, returns different values in 11.2 as compared to 11.1. The new values returned from a `COMPRESS_FOR` column are `BASIC` or `OLTP`. In 11.1, the value was `DIRECT LOAD ONLY` and `FOR ALL OPERATIONS`, respectively.

## 4.5 Oracle Automatic Storage Management (Oracle ASM)

The following sections describe information pertinent to Oracle Automatic Storage Management (Oracle ASM) in Oracle Database 11g release 2 (11.2).

### 4.5.1 Oracle Database Data Files and Oracle ACFS

Oracle ACFS is the preferred file manager for non-database files. It is optimized for general purpose files. Oracle ACFS does not support any file that can be directly stored in Oracle ASM.

### 4.5.2 Oracle Homes on Oracle ACFS Supported Starting With Release 11.2

Placing Oracle homes on Oracle ACFS is supported starting with Oracle Database release 11.2 (reference Bug 10144982). Oracle ACFS can result in unexpected and inconsistent behavior if you attempt to place Oracle homes on Oracle ACFS on database versions prior to 11.2.

## 4.6 Oracle Enterprise Manager Database Control

The following sections describe information for Database Control in Oracle Database 11g Release 2 (11.2).

### 4.6.1 Reorganize Objects

The following applies to Reorganize Objects:

- The database can be adversely affected if metadata changes occur between the time the reorganization script is generated and the time it is completed.
- The database can be adversely affected if an offline reorganization is attempted while DDL is in progress against the tables being reorganized.
- Before using the Reorganize Objects wizard or the Make Tablespace Locally Managed wizard in Oracle Enterprise Manager, Oracle recommends that you back up your database.

### 4.6.2 Editing Multiple Objects

Oracle Enterprise Manager only supports having one browser window open for editing an object. For example, Oracle Enterprise Manager only supports editing one tablespace at a time.

Note:

If a window is read-only, then you may have multiple browser windows open.

### 4.6.3 Large Number of Database Objects May Require Increase in Heap Size

Oracle Enterprise Manager Database Control is configured with 192 MB (32-Bit)/384 MB (64-Bit) of heap memory. However, certain Oracle Enterprise Manager Database Control functionality (for example, Change Manager) may require higher memory settings if the database contains a large number of objects.

Memory settings can be increased using the following `emctl` command:

```
emctl config dbconsole -heap_size MemorySizeValue M
```

Oracle Enterprise Manager Database Control must be restarted for the new settings to take effect.

## 4.7 Database Security

Note the following changes in Database Security.

### 4.7.1 Configure and Use SSL Certificates to Setup Authentication

Note:

This affects the security in the connection between the Oracle Clusterware and the mid-tier or JDBC client.

JDBC or Oracle Universal Connection Pool's (UCP) Oracle RAC features like Fast Connection Failover (FCF) subscribe to notifications from the Oracle Notification Service (ONS) running on the Oracle RAC nodes. The connections between the ONS server in the database tier and the notification client in the mid-tier are usually not authenticated. It is possible to configure and use SSL certificates to setup the authentication but the steps are not clearly documented.

The workaround is as follows:

1. Create an Oracle Wallet to store the SSL certificate using the `orapki` interface:
	1. `cd $ORA_CRS_HOME/opmn/conf`
		2. `mkdir sslwallet`
		3. `orapki wallet create -wallet sslwallet -auto_login`
		When prompted, provide `ONS_Wallet` as the password.
		4. `orapki wallet add -wallet sslwallet -dn "CN=ons_test,C=US" -keysize 1024 -self_signed -validity 9999 -pwd ONS_Wallet`
		5. `orapki wallet export -wallet sslwallet -dn "CN=ons_test,C=US" -cert sslwallet/cert.txt -pwd ONS_Wallet`
		6. Copy the wallet created in Step c to all other cluster nodes at the same location.
2. Stop the ONS server on all nodes in the cluster:
	```
	srvctl stop nodeapps
	```
3. Update the ONS configuration file on all nodes in the database tier to specify the location of the wallet created in Step 1:
	1. Open the file `ORA_CRS_HOME` `/opmn/conf/ons.config`
		2. Add the `walletfile` parameter to the `ons.config` file:
		`walletfile=` `ORA_CRS_HOME` `/opmn/conf/sslwallet`
		3. Restart the ONS servers with the `srvctl`:
		```
		srvctl start nodeapps
		```
4. If you are running a client-side ONS daemon on the mid-tier, there are two possible configurations:
	- ONS started from OPMN (like in OracleAS 10.1.3.x) which uses `opmn.xml` for its configuration.
		- ONS started standalone (like using `onsctl`), which uses `ons.config` for its configuration.
	For case (1), refer to the OPMN Administrator's Guide for the Oracle Application Server release. This involves modifying the `opmn.xml` file to specify the wallet location.
	For case (2), refer to the section titled Configuration of ONS in Appendix B of the [Oracle Database JDBC Developer's Guide](https://docs.oracle.com/cd/E11882_01/java.112/e16548/toc.htm). The client-side ONS daemon can potentially run of different machines. Copy the wallet created in Step 1 to those client-side machines and specify the path on that client-side machine in the `ons.config` file or in the `opmn.xml` file.
5. If you are running remote ONS configuration without a client-side ONS daemon, refer to the "Remote ONS Subscription" subsection of the "Configuring ONS for Fast Connection Failover" subsection of the "Using Fast Connection Failover" section of the "Fast Connection Failover" chapter in the [Oracle Database JDBC Developer's Guide](https://docs.oracle.com/cd/E11882_01/java.112/e16548/toc.htm). Copy the wallet created in Step 1 to those client-side machines and specify the path on that client-side machine in the `ons.config` file or in the `opmn.xml` file.
	Alternatively, you can specify the following string as the `setONSConfiguration` argument:
	```
	propertiesfile=location_of_a_Java_properties_file
	```
	The Java properties file should contain one or more of the ONS Java properties listed below, but at least the `oracle.ons.nodes` property. The values for these Java properties would be similar to those specified in the "Remote ONS Subscription" subsection previously noted in this step:
	```
	oracle.ons.nodes
	oracle.ons.walletfile
	oracle.ons.walletpassword
	```

## 4.8 Encryption and Integrity

Note the following changes in the areas of encryption and integrity.

### 4.8.1 Encrypted Tablespaces

- You cannot encrypt an existing tablespace with an `ALTER TABLESPACE` statement. However, you can use Data Pump or SQL statements such as `CREATE TABLE AS SELECT` or `ALTER TABLE MOVE` to move existing table data into an encrypted tablespace.
- When recovering a database with encrypted tablespaces (for example, after a `SHUTDOWN ABORT` or a catastrophic error that brings down the database instance), you must open the wallet after database mount and before database open so the recovery process can decrypt data blocks and redo.
- The master encryption key for Transparent Data Encryption (TDE) tablespace encryption can leverage Hardware Security Modules (HSM) for full key management (for example, create, store, rotate, and retire). In 11.1.0.7, it was only possible to create and store the TDE tablespace encryption master key in HSM, not rotate. Master key for the TDE tablespace encryption can also be migrated from Oracle Wallet to HSM.

## 4.9 Java and Web Services

Note the following items when working with Java.

### 4.9.1 Oracle JVM

Oracle Database 11g Release 2 (11.2) includes a fully functional Java Virtual Machine (JVM), as well as the Java class libraries for Sun's Java Development Kit (JDK) 5.0. When combined with Oracle's JDBC and SQLJ, release 11.2.0.2 provides an enterprise class platform, Oracle JVM, for developing and deploying server-based Java applications. Refer to the Oracle JVM Readme file located at:

```
ORACLE_HOME/relnotes/readmes/README_javavm.txt
```

### 4.9.2 Announcing Oracle Universal Connection Pool (UCP) and Deprecation of JDBC Implicit Connection Cache in Favor of UCP

Starting with Oracle Database 11g release 1 (11.1.0.7), Oracle has released the new Universal Connection Pool for JDBC. For more details, see the Oracle Universal Connection Pool for JDBC Developer's Guide at the following Web page:

`http://www.oracle.com/technology/tech/java/sqlj_jdbc/UCP_dev_guide.pdf`

Consequently, Oracle is deprecating the existing JDBC connection pool (that is, Implicit Connection Cache) that was introduced in Oracle Database 10g release 1 (10.1). Your applications will continue to work until formal desupport in a future release at which time a desupport notice will be posted.

Oracle encourages you to plan to adopt UCP for new applications and plan to change existing applications as indicated in Transitioning to Oracle Universal Connection Pool (UCP) at the following Web page:

`http://www.oracle.com/technology/tech/java/sqlj_jdbc/pdf/ucp_transition_guide.pdf`

UCP download and code samples are located at the following Web page:

`http://www.oracle.com/technology/software/tech/java/sqlj_jdbc/htdocs/ucp.html`

### 4.9.3 JDBC

The Oracle JDBC product supports the latest Java/JDBC standards. For more details, refer to the JDBC Readme file located at:

```
ORACLE_HOME/relnotes/readmes/README_jdbc.txt
```

### 4.9.4 Web Services

As an alternative to Oracle Net, Oracle Database Web services provides nonconnected access to the database through standard Web services mechanisms. These include XML, SOAP, and WSDL, and can turn the database into a Web services provider. Similarly, the database itself can act as a Web service consumer and run external Web services. Important features of Web services include:

- A JAX-RPC based SOAP Client library supports invocation of external Web services from within the database, and applies the power of SQL to the results.
- Web Services Call-In: Deploying a JPublisher-generated Java class against Oracle Application Server 10g enables you to run database operations such as Java and PL/SQL procedures and packages, SQL queries, and DML operations.
- Web Services Call-Out: Deploying a JPublisher-generated Web services client from a WSDL and its PL/SQL wrapper supports invocation of external Web services from within the database.

## 4.10 Media Management Software

For environments that consist of a single server, Oracle offers Oracle Secure Backup Express to back up your Oracle Database and other critical Oracle infrastructure to tape. Oracle Secure Backup is fully integrated with Recovery Manager (RMAN) to provide data protection services. For larger environments, Oracle Secure Backup is available as a separately licensable product to back up many database servers and file systems to tape. Oracle Secure Backup release 10.4 is shipping with this Oracle Database 11g release 2 (11.2.0.2). For more information on Oracle Secure Backup, refer to

`http://www.oracle.com/goto/osb/`

### 4.10.1 Globalization Restrictions Within Oracle Secure Backup

The following globalization restrictions apply to Oracle Secure Backup:

- The Oracle Secure Backup Web Tool and command line interface are available in English only, and are not globalized. All messages and documentation are in English.
- Oracle Secure Backup does not support file names or RMAN backup names that are encoded in character sets that do not support null byte termination, such as Unicode UTF-16. Note that this restriction affects file names, not backup contents. Oracle Secure Backup can back up Oracle databases in any character set.

## 4.11 Oracle Application Express

Note the following items when working with Oracle Application Express.

To learn more about Oracle Application Express, refer to the [Oracle Application Express Release Notes](https://docs.oracle.com/cd/E11882_01/relnotes.112/e11944/toc.htm) and the [Oracle Application Express Installation Guide.](https://docs.oracle.com/cd/E11882_01/install.112/e12196/toc.htm)

### 4.11.1 Checking for the Most Current Release

Oracle Application Express is released more frequently than Oracle Database. To view additional information about the most current release, refer to:

```
http://www.oracle.com/technetwork/developer-tools/apex/overview/index.html
```

### 4.11.2 Configuring Oracle HTTP Server

When configuring Oracle HTTP Server for Oracle Application Express in a new installation, the database user `APEX_PUBLIC_USER` must be an unlocked account. To unlock the account for database user `APEX_PUBLIC_USER`, complete the following:

1. Start SQL\*Plus and connect as `SYS` to the database where Oracle Application Express is installed. For example:
	```
	$ ORACLE_HOME/bin/sqlplus
	SQL> CONNECT SYS as SYSDBA
	Enter password: SYS_password
	```
2. Run the following command:
	```
	SQL> ALTER USER APEX_PUBLIC_USER ACCOUNT UNLOCK
	```

### 4.11.3 Database Compatible Parameter and Enabling Network Services

To run the examples in the Oracle Application Express Post-Installation tasks in the section titled "Enabling Network Services in Oracle Database 11g" in the [Oracle Database Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST), the `COMPATIBLE` initialization parameter of the database must be set to at least 11.1.0.0.0. By default, an Oracle Database 11g database will already have the parameter set properly, but a database upgraded to 11g from a prior version may not.

Refer to the section titled "Creating and Configuring an Oracle Database" in the [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for information about changing database initialization parameters.

## 4.12 Oracle Client Applications

Oracle Client 11g contains advanced features for diagnosing issues, including the ability to dump diagnostic information when important errors are detected. By default, these dumps are restricted to a small subset of available information to ensure that application data is not dumped. However, in many installations, secure locations for dump files may be configured, ensuring the privacy of such logs. In such cases, it is recommended that you turn on full dumps; this can greatly speed the resolution of issues. Enable full dumps by adding the following line to the `sqlnet.ora` file that is used by your Oracle client installation:

```
DIAG_RESTRICTED=false
```

To verify that diagnosability features are working correctly, take the following steps:

1. Upgrade your application to use Oracle Database 11g client libraries.
2. Start your application.
3. Check the file `sqlnet.log` in your application's `TNS_ADMIN` directory for error messages indicating that diagnosability could not be started (normally this is due to invalid directory names or permissions).

Refer to the [Oracle Call Interface Programmer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e10646/toc.htm) for details.

## 4.13 Oracle Configuration Manager

Note the following for Oracle Configuration Manager.

### 4.13.1 cron Configuration Issue

If you are denied access to `cron`, then the configuration of Oracle Configuration Manager fails with the following error:

```
ORACLE_HOME/ccr/bin/setupCCR
** Installing base package **
Deploying core - Version 10.2.5.0.0
Error encountered in package deployment.
```

After the installation is complete, set the environment variable `CCR_DISABLE_CRON_ENTRY` to `TRUE` and try the configuration of Oracle Configuration Manager again using the following command:

```
ORACLE_HOME/ccr/bin/setupCCR
```

## 4.14 Oracle Data Mining

Oracle Data Mining scoring functions in Oracle Database 11g release 2 (11.2) are also available in Oracle Exadata Storage Server Software. Scoring capabilities in the storage layer permit very large data sets to be mined quickly, thus further increasing the competitive advantage already gained from Oracle in-database analytics. For information about Oracle Exadata Storage Server Software, see `http://www.oracle.com/technology/products/bi/db/exadata/index.html`.

The Data Mining Option, as an embedded feature of the database, is automatically installed with the Oracle Enterprise Edition Database. When installing the database with the Data Mining Option, choose the Data Warehouse configuration type for the most appropriate default initialization parameters.

In Oracle Database 11g, Data Mining models are implemented as data dictionary objects in the `SYS` schema. The `DMSYS` schema no longer exists.

Data Mining users must have the `CREATE MINING MODEL` privilege to create mining models in their own schema. Additional privileges are required for other data mining activities, as described in the [Oracle Data Mining Administrator's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e16807/security.htm#DMADM004).

New data dictionary views for Oracle Data Mining were introduced in Oracle Database 11g release 1 (11.1):

- `USER/ALL/DBA_MINING_MODELS`
- `USER/ALL/DBA_MINING_MODEL_ATTRIBUTES`
- `USER/ALL/DBA_MINING_MODEL_SETTINGS`

Demo programs that illustrate the Data Mining APIs (PL/SQL and Java) are installed with Oracle Database Examples. Instructions are in the [Oracle Data Mining Administrator's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e16807/sampleprogs.htm#DMADM009).

The Oracle Data Mining Scoring Engine Option, a separately installed database option in Oracle Database 10g, is not available in Oracle Database 11g. All functionality of the Data Mining Scoring Engine Option is offered in the Data Mining Option.

The Basic Local Alignment Search Tool (BLAST), previously supported by Oracle Data Mining, is not available in Oracle 11g.

## 4.15 Oracle Internet Directory

The Oracle Internet Directory product ships only with Oracle Application Server, not the Oracle Database 11g release 1 (11.1) product set. The following information is included because Oracle Network functionality may use Oracle Internet Directory. Many of the administrative activities for Oracle Internet Directory have been consolidated into a single tool, Oracle Internet Directory Configuration Assistant (OIDCA). OIDCA should be used with Enterprise User Security and Network Names features under these conditions:

1. Enterprise User Security
	- Enterprise User Security only works with Identity Management Realms in release 11.2.0.2. You must convert Oracle Contexts used in prior releases to Identity Management Realms using the OIDCA tool.
		- Use OIDCA when creating or updating the `ldap.ora` configuration file for discovering the Oracle Internet Directory server in the environment. When created with OIDCA, `ldap.ora` is located in the `ORACLE_HOME` `/ldap/admin` directory on Linux and UNIX operating systems and in the `ORACLE_HOME` `\ldap\admin` directory on Windows operating systems.
2. Network Names
	- Use OIDCA when creating, upgrading, and deleting Oracle Contexts.
		- Use OIDCA when converting an Oracle Context from an earlier release to an Identity Management Realm.
		- Use OIDCA when setting up the `ldap.ora` configuration file for discovering the Oracle Internet Directory server in the environment.

Note the following items when working with Oracle Internet Directory.

### 4.15.1 Using the Oracle Internet Directory Configuration Assistant

The Oracle Internet Directory Configuration Assistant (OIDCA) enables you to create, upgrade, and delete an Oracle Context, configure the file `ldap.ora`, and convert an Oracle Context to an Identity Management Realm.

The OIDCA syntax is:

```
oidca oidhost=host 
      nonsslport=port |
      sslport=SSL Port
      dn=binddn 
      pwd=bindpwd 
      propfile=properties file
```

To see the usage of OIDCA, enter `oidca -help` at the command prompt.

### 4.15.2 Creating an Oracle Context

The following syntax is used to create an Oracle Context in OIDCA; the parameters are described in the subsequent table.

```
oidca oidhost=host
      nonsslport=port
      sslport=SSL Port
      dn=binddn
      pwd=bindpwd
      mode=CREATECTX 
      contextdn=OracleContext DN
```

| Parameters | Description |
| --- | --- |
| `oidhost` | OID server host; if not specified, default is `localhost` |
| `nonsslport` | OID server port; if not specified, default is `389` |
| `sslport` | OID SSL port; if not specified, default is `636` |
| `dn` | OID user, such as `cn=orcladmin` |
| `pwd` | OID user password |
| `mode` | Mode of the OIDCA; set to `CREATECTX` |
| `contextdn` | DN under which `OracleContext` must be created, such as `dc=acme`, `dc=com` |

Note the following points:

- The `contextdn` must exist for this operation to be successful.
- This valid DN should not exist in OID: `"cn=oraclecontext,dc=acme, dc=com"`.
- This valid DN must exist in OID: `"dc=acme,dc=com"`.
- The parameters `mode` and `contextdn` can also be passed as a properties file.
- Specify the parameter `nonsslport=port` if you want to perform the operation using non-SSL mode.
- Specify the parameter `sslport=sslport` if you want to perform the operation using SSL mode.
- Either the `nonsslport` or the `sslport` parameter must be specified, but not both.

Functionality

1. The OIDCA verifies that `contextdn` has a valid DN syntax and that the entry exists in Oracle Internet Directory. Note that the OIDCA cannot create a root `OracleContext` explicitly. If there is no root Oracle Context, then OIDCA exits with an error.
2. If DN exists, then OIDCA verifies that the Oracle Context already exists.
	- If the Oracle Context already exists and is up-to-date, then OIDCA exits with the message `Oracle Context already exists and is up to date`.
		- If the Oracle Context already exists, but it is an older version, then OIDCA exits with the message `Oracle Context already exists and is of an older version`.
		- If the Oracle Context does not exist, then OIDCA creates the Oracle Context under this DN.

### 4.15.3 Upgrading an Oracle Context

To upgrade an `OracleContext` instance, use the following syntax; the parameters are listed in the subsequent table.

```
oidca oidhost=host
      nonsslport=port 
      sslport=SSL Port 
      dn=binddn
      pwd=bindpwd
      mode=UPGRADECTX
      contextdn=OracleContext DN
```

| Parameters | Description |
| --- | --- |
| `oidhost` | OID server host; if not specified, default is `localhost` |
| `nonsslport` | OID server port; if not specified, default is `389` |
| `sslport` | OID SSL port; if not specified, default is `636` |
| `dn` | OID user, such as `cn=orcladmin` |
| `pwd` | OID user password |
| `mode` | Mode of the OIDCA; always set to `UPGRADECTX` |
| `contextdn` | DN under which `OracleContext` must be created, such as `dc=acme`, `dc=com` |

Note the following points:

- The `contextdn` must contain an `OracleContext` for this operation to be successful.
- The DNs `"cn=oraclecontext`,`dc=acme,dc=com"` and `"dc=acme,dc=com"` are both valid.
- The parameters `mode` and `contextdn` can also be passed as a properties file.
- Specify the parameter `nonsslport=port` if you want to perform the operation using a non-SSL mode.
- Specify the parameter `sslport=sslport` if you want to perform the operation using SSL mode.
- Either the `nonsslport` or the `sslport` parameter must be specified, but not both.

Functionality

1. OIDCA verifies that the `contextdn` has valid DN syntax and that `OracleContext` exists in Oracle Internet Directory. OIDCA cannot upgrade a root `OracleContext` explicitly. If there is no root `OracleContext`, then OIDCA sends an error message.
2. If `OracleContext` exists under `contextdn`,
	- The OIDCA checks if the `OracleContext` belongs to a realm, in which case it exits with the appropriate message. Note that `OracleContext` instances that belong to a realm cannot be upgraded.
		- The OIDCA verifies that the `OracleContext` is up-to-date, then exits with the message `Oracle Context already exists and is up to date`.
		- If the `OracleContext` is not up-to-date, then the OIDCA upgrades the `OracleContext` under this DN.

### 4.15.4 Deleting an Oracle Context

To delete an `OracleContext`, use the following syntax; the parameters are listed in the subsequent table.

```
oidca oidhost=host
      nonsslport=port
      sslport=SSL Port
      dn=binddn
      pwd=bindpwd
      mode=DELETECTX
      contextdn=OracleContext DN
```

| Parameters | Description |
| --- | --- |
| `oidhost` | OID server host; if not specified, default is `localhost` |
| `nonsslport` | OID server port; if not specified, default is `389` |
| `sslport` | OID SSL port; if not specified, default is `636` |
| `dn` | OID user, such as `cn=orcladmin` |
| `pwd` | OID user password |
| `mode` | Mode of the OIDCA; always set to `DELETECTX` |
| `contextdn` | DN under which OracleContext must be created, such as `dc=acme`, `dc=com` |

Note the following points:

- The `contextdn` must contain an `OracleContext` for this operation to be successful.
- The DNs `"cn=oraclecontext,` `dc=acme,dc=com"` and `"dc=acme,dc=com"` are both valid.
- The parameters `mode` and `contextdn` can also be passed as a properties file.
- Specify the parameter `nonsslport=port` if you want to perform the operation using a non-SSL mode.
- Specify the parameter `sslport=sslport` if you want to perform the operation using SSL mode.
- Either the `nonsslport` or the `sslport` parameter must be specified, but not both.

Functionality

1. OIDCA verifies that the `contextdn` has valid DN syntax and that `OracleContext` exists in Oracle Internet Directory.
2. If `OracleContext` exists under `contextdn`,
	- The OIDCA checks if the `OracleContext` belongs to a realm, in which case it exits with the appropriate message. Note that `OracleContext` instances that belong to a realm cannot be deleted.
		- If `OracleContext` does not belong to a realm, then OIDCA deletes it.

### 4.15.5 Configuring the File ldap.ora

To configure the file `ldap.ora`, use the following syntax; the parameters are listed in the subsequent table.

```
oidca oidhost=host
      nonsslport=port
      sslport=SSL Port
      adminctx=Administrative context
      mode=LDAPORA  
      dirtype=OID or AD
      -update
```

| Parameters | Description |
| --- | --- |
| `oidhost` | OID server host; if not specified, default is `localhost`. |
| `nonsslport` | OID server port; determined using discovery APIs. |
| `sslport` | OID SSL port; determined using discovery APIs. |
| `mode` | Mode of the OIDCA; always set to `LDAPORA`. |
| `dirtype` | Directory type; possible values are `OID` and `AD`; mandatory attribute. |
| `adminctx` | Default administrative context, such as `dc=acme,dc=com`. If not specified, then determined using discovery. |
| `-update` | If this flag is specified, then overwrite existing `ldap.ora`; if not, then create `ldap.ora` only if it does not already exist. |

Note the following points:

- Either the non-SSL or the SSL port must be specified. The other port is discovered.
- The parameters `mode`, `dirtype`, and `adminctx` can also be passed in within a properties file.

Functionality

1. Using the Discovery API, the OIDCA determines all the parameters not specified on the command line.
2. The OIDCA checks for the `ldap.ora` location using Discovery APIs.
	- If `ldap.ora` exists and the `-update` parameter is not specified, then exit with message `ldap.ora exists`.
		- If `ldap.ora` exists and the `-update` parameter is not specified, then update the existing `ldap.ora` using Discovery API.
		- If `ldap.ora` does not exist, then create a new `ldap.ora` file in a location in the following order:
		```
		LDAP_ADMIN
		ORACLE_HOME/ldap/admin
		```

### 4.15.6 Converting an Oracle Context to an Identity Management Realm

Oracle Database 10g entries must be stored in Oracle Internet Directory release 9.0.4 server. An Identity Management Realm release 9.0.4 is also required for Enterprise User Security, a feature of the Oracle Database 10g.

To convert an existing `OracleContext` to an Identity Management Realm, use the following syntax. The parameters are listed in the subsequent table. Note that the root of the `OracleContext` object is not converted.

```
oidca oidhost=host
      nonsslport=port
      sslport=SSL Port
      dn=binddn
      pwd=bindpwd
      mode=CTXTOIMR
      contextdn=OracleContext DN
```

| Parameters | Description |
| --- | --- |
| `oidhost` | OID server host; default is `localhost` |
| `nonsslport` | OID server port; default is `389` |
| `sslport` | OID SSL port; default is `636` |
| `dn` | OID user, such as `cn=orcladmin` |
| `pwd` | OID user password |
| `mode` | Mode of the OIDCA; always set to `CTXTOIMR` |
| `contextdn` | DN under which `OracleContext` must be created, such as `dc=acme`, `dc=com` |

Note the following points:

- The `OracleContext` must exist under the specified `contextdn`.
- The DNs `"cn=oraclecontext`, `dc=acme,dc=com"` and `"dc=acme, dc=com"` are both valid.
- The parameters `mode` and `contextdn` can also be passed in a properties file.
- Specify the parameter `nonsslport=port` if you want to perform the operation using a non-SSL mode.
- Specify the parameter `sslport=sslport` if you want to perform the operation using SSL mode.
- Either the `nonsslport` or the `sslport` parameter must be specified, but not both.

Functionality

1. The OIDCA checks if `contextdn` has valid DN syntax, and if it contains a valid `OracleContext`.
2. If `OracleContext` exists under `contextdn,`
	- The OIDCA checks if the `OracleContext` belongs to a realm. If it does, then it exits with an appropriate error message.
		- If `OracleContext` does not belong to a realm, then OIDCA upgrades it to the latest version, and converts it to a realm.

Note also:

- If the nickname attribute is not `cn`, then configure it as a user configuration attribute using the Oracle Internet Directory Self-Service Console.
- If you want to use the Oracle Internet Directory Self-Service Console to manage the users and groups in the converted realm, then you must set up the administrative privileges appropriately. For details, refer to the [Oracle Fusion Middleware Administrator's Guide for Oracle Internet Directory](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=OIDAG).

## 4.16 Oracle Multimedia

The name Oracle interMedia was changed to Oracle Multimedia in Oracle Database 11g release 1 (11.1). The feature remains the same, only the name has changed. References to Oracle interMedia were replaced with Oracle Multimedia, however some references to Oracle interMedia or interMedia may still appear in graphical user interfaces, code examples, and related documents in the Oracle Database documentation library for 11g release 2 (11.2).

For additional information, refer to the Oracle Multimedia Readme file located at:

```
ORACLE_HOME/ord/im/admin/README.txt
```

## 4.17 Oracle Net Services

Oracle Database provides limited support for Internet Protocol Version 6 (IPv6) addressing and connectivity. For details, see [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm).

## 4.18 Oracle Real Application Clusters

Note the following items when working with Oracle RAC.

### 4.18.1 Moving root Owned Binaries that need setuid to Local Nodes from NFS

If you install an Oracle RAC database into a shared Oracle home on an NFS device, then you must copy the ORADISM binary (`oradism`) into a local directory on each node (reference Bug 7210614).

To move `oradism`, take the following steps:

1. Copy the `ORACLE_HOME` `/bin/oradism` binary to an identical directory path on all cluster nodes. The path (for example, `/u01/local/bin` in the example in Step 2) must be local and not NFS. For example:
	```
	cp -a ORACLE_HOME/bin/oradism /u01/local/bin
	```
2. Run the following commands, as the root user, to set ownership and permissions of the `oradism` executable:
	```
	$ chown root /u01/local/bin/oradism
	$ chmod 4750 /u01/local/bin/oradism
	```
3. Create a symbolic link from the NFS shared home to the local `oradism` directory path. This needs to be done from one node only. Each node can then reference its own `oradism` using the `symlink` from the shared Oracle home. For example:
	```
	$ cd /nfs/app/oracle/product/11.2.0/db_1/bin
	$ rm -f oradism
	$ ln -s /u01/local/bin/oradism oradism
	```
4. If the Oracle home is an Oracle Database home directory, then repeat steps 1-3 for other binaries such as `extjob`, `jssu`, `nmb`, `nmhs` and `nmo`. You do not need to perform this step if the Oracle home is an Oracle Grid Infrastructure home directory.

### 4.18.2 Creating Server Pools

Caution:

By default, any named user may create a server pool. To restrict the operating system users that have this privilege, Oracle strongly recommends that you add specific users to the CRS Administrators list.

See also [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/admin.htm#CWADD91105) for more information about adding users to the CRS Administrators list.

Create an initial, user-defined server pool immediately after the Oracle Grid Infrastructure for a cluster installation if you plan to use a policy-managed Oracle RAC database. As the Grid software owner, use the following SRVCTL command located in the path `Grid_home` `/bin`:

```
srvctl add srvpool -g srvpool_name -u max
```

### 4.18.3 Using the Same Cluster for Administrator-Managed and Policy-Managed Databases

If you are creating an administrator-managed database on a cluster that already hosts policy-managed databases, then you must carefully select the nodes for the administrator-managed database (reference Bug 10027250). This is because the nodes that you select for an administrator-managed database that are in policy-managed server pools will be moved into the Generic server pool as part of this process. If you select nodes that already run other policy-managed database instances, then DBCA prompts you with a message that lists the instances and services that will be shut down when DBCA creates the administrator-managed database. If you select the `Yes` button on the dialog box when DBCA asks " `Do you want to continue?`," then your policy-managed database instances and services will be shut down as a result of the administrator-managed database creation process.

Note: This is also true if you use the `srvctl add instance` command, which gives a similar error message indicating that the databases would be shut down. If you also use the force option (`-f`) with the `srvctl add instance` command, then this is the same as choosing `Yes` on the DBCA dialog. Doing this shuts down any policy-managed databases that are running on the node before moving the node into the Generic server pool.

### 4.18.4 Adding a Node in a Cluster

When adding a node in a cluster running a policy-managed database, Oracle Clusterware tries to start the new instance before the cloning procedure completes. The following steps should be used to add the node:

1. Run `addNode` for the Oracle Grid Infrastructure for a cluster to add the new node. Do not run the root scripts when prompted; you will run them later.
2. Install the Oracle RAC database software using a software-only installation. Ensure Oracle is linked with the Oracle RAC option.
3. Complete the root script actions for the Database home.
4. Complete the root scripts action for the Oracle Clusterware home and then finish the installation.

## 4.19 Oracle Grid Infrastructure for a Cluster

Note the following items when working with Oracle Clusterware and Oracle Automatic Storage Management (Oracle ASM), which are installed with an Oracle Grid Infrastructure for a cluster installation.

### 4.19.1 In-Place Patch Set Upgrades Are Not Supported

All Oracle Grid Infrastructure patch set upgrades must be out-of-place upgrades, in which case you install the patch set into a new Oracle Grid home (reference Bug 10210246). In-place patch set upgrades are not supported.

### 4.19.2 Changing Host Names

Avoid changing host names after you complete the Oracle Grid Infrastructure for a cluster installation. Nodes with changed host names must be deleted from the cluster and added back with the new name.

### 4.19.3 Oracle ACFS and Oracle Clusterware Stack Shut Down

When attempting to shut down Oracle Clusterware, the Oracle Clusterware stack may report that it did not successfully stop on selected nodes (reference Bug 8651848). If the database home is on Oracle ACFS, then you may receive the following error:

```
CRS-5014: Agent orarootagent.bin timed out starting process acfsmount for action
```

This error can be ignored.

Alternatively, the Oracle Clusterware stack may report that it did not successfully stop on selected nodes due to the inability to shut down the Oracle ACFS resources. If this occurs, take the following steps:

- Ensure that all file system activity to Oracle ACFS mount points is quiesced by shutting down programs or processes and retry the shutdown.
- If the `ora.registry.acfs` resource check function times out, or the resource exhibits a state of `UNKNOWN` or `INTERMEDIATE`, then this may indicate an inability to access the Oracle Cluster Registry (OCR). The most common cause of this is a network failure. The commands `acfsutil registry` and `ocrcheck` may give you a better indicator of the specific error. Clear this error and attempt to stop Oracle Clusterware again.

## 4.20 Oracle ODBC Driver

The Oracle ODBC Driver Readme file is located at:

```
ORACLE_HOME/odbc/html/ODBCRelnotesUS.htm
```

## 4.21 Oracle OLAP

Consider the following when working with Oracle OLAP:

1. SQL Aggregation Management is a group of PL/SQL subprograms in `DBMS_CUBE` that support the rapid deployment of cube materialized views from existing relational materialized views. Cube materialized views are cubes that have been enhanced to use the automatic refresh and query rewrite features of Oracle Database. A single cube materialized view can replace many of the relational materialized views of summaries on a fact table, providing uniform response time to all summary data.
	In the process of creating the cube materialized views, `DBMS_CUBE` also creates a fully functional analytic workspace including a cube and the cube dimensions. The cube stores the data for a cube materialized view, instead of the table that stores the data for a relational materialized view. A cube can also support a wide range of analytic functions that enhance the database with information-rich content.
2. Enhanced logging capabilities are provided through the new PL/SQL package `DBMS_CUBE_LOG` that offers four different logs. Both Analytic Workspace Manager users and database administrators can view the progress of an analytic workspace build in `CUBE_BUILD_LOG`, find load errors in `CUBE_REJECTED_RECORDS`, check the validity of dimension hierarchies in `CUBE_DIMENSION_COMPILE`, and follow OLAP engine events in `CUBE_OPERATIONS_LOG`.
3. The OLAP Option, as an embedded feature of the database, is automatically installed with the Oracle Enterprise Edition Database. When installing the database with the OLAP Option, choose the Data Warehouse configuration type for the most appropriate default initialization parameters.
4. Analytic Workspace Manager 11.2.0 should be used when running Oracle Database 11g release 2 (11.2) in either Oracle Database 10g or Oracle Database 11g compatibility modes. An Oracle Database 10g format analytic workspace may be created by choosing the Oracle Database 10g cube type when creating a new analytic workspace.
5. OLAP 10g clients connecting to 10g style analytic workspaces in an Oracle Database 11g release 2 (11.2) database instance should upgrade their Java to version 1.5, as well as upgrade their OLAP API version to 11.2.0.
6. Oracle Business Intelligence Beans 10g and Oracle Discoverer for OLAP 10g can be used with 10g format analytic workspaces in Oracle Database 11g. They cannot be used with 11g format analytic workspaces. To upgrade the OLAP API client JARs, include these new JARs in the Java class search list before the Intelligence Beans or Discoverer JAR files or both.
7. The OLAPSYS schema and the CWM metadata contained within the schema are deprecated in Oracle Database 11g release 2 (11.2). The OLAP API can still query relational tables (ROLAP mode) using data dictionary metadata. For more information, refer to My Oracle Support, Note 445311.1 (at `https://support.oracle.com`).

## 4.22 Oracle Spatial

The Oracle Spatial readme file supplements the information in the following manuals: [Oracle Spatial Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e11830/toc.htm), [Oracle Spatial Topology and Network Data Models Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e11831/toc.htm), and [Oracle Spatial GeoRaster Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e11827/toc.htm). The Oracle Spatial readme file is located at:

```
ORACLE_HOME/md/doc/README.txt
```

## 4.23 Oracle SQL Developer

The Oracle SQL Developer readme file is located at:

```
ORACLE_HOME/sqldeveloper/readme.html
```

## 4.24 Oracle Text

Note the following items when working with Oracle Text. You should also check entries for the [Oracle Text Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/text.112/e24435/toc.htm) in the Documentation Addendum.

### 4.24.1 Query Compatible Syntax Values

Chapter 6, titled "CTX\_CLS Package", in the [Oracle Text Reference](https://docs.oracle.com/cd/E11882_01/text.112/e24436/toc.htm) states under the section titled "Query Compatible Syntax" that the `doc_id` column is a number. This is correct; however, the values stored in this column must be in the range `0-4294967295`. The values must be stored in an unsigned 32-bit value. This range also pertains to `catid`, `catdocid`, and `rescatid`.

### 4.24.2 Oracle Text Supplied Knowledge Bases

An Oracle Text knowledge base is a hierarchical tree of concepts used for theme indexing, `ABOUT` queries, and deriving themes for document services. The following Oracle Text services require that a knowledge base be installed:

- Index creation using a `BASIC_LEXER` preference where `INDEX_THEMES=YES`
- `SYNC` ing of an index where `INDEX_THEMES=YES`
- `CTX_DOC.THEME` s
- `CTX_DOC.POLICY_THEME` s
- `CTX_DOC.GIST`
- `CTX_DOC.POLICY_GIST`
- `CTX_QUERY.HFEEDBACK`
- `CTX_QUERY.EXPLAIN`, if using `ABOUT` or `THEMES` with `TRANSFORM`
- `CTX_DOC.SNIPPET` (if using the `ABOUT` operator)
- `CTX_DOC.POLICY_SNIPPET` (if using the `ABOUT` operator)
- `CONTAINS` queries that use `ABOUT` or `THEMES` with `TRANSFORM`
- The Knowledge Base Extension Compiler, `ctxkbtc`
- Clustering and classification services, if themes are specified

If you plan to use any of these Oracle Text features, then you should install the supplied knowledge bases, English and French, from the Oracle Database Examples media, available for download on OTN.

Note that you can extend the supplied knowledge bases, or create your own knowledge bases, possibly in languages other than English and French. For more information about creating and extending knowledge bases, refer to the [Oracle Text Reference](https://docs.oracle.com/cd/E11882_01/text.112/e24436/toc.htm).

For information about how to install products from the Oracle Database Examples media, refer to the [Oracle Database Examples Installation Guide](https://docs.oracle.com/cd/E11882_01/install.112/e24501/toc.htm) that is specific to your platform.

Supplied Knowledge Bases and Upgrades

Because the supplied knowledge bases are contained on the Oracle Database Examples media, they are not immediately available after an upgrade to Oracle Database 11g release 1 (11.1). Oracle Text features that depend on the supplied knowledge bases available before the upgrade will not function after the upgrade, so you must install the supplied knowledge bases from the Oracle Database Examples media.

After an upgrade, you must regenerate all user extensions to the supplied knowledge bases. These changes affect all databases installed in the given `ORACLE_HOME`.

For more information on upgrading Oracle Text and supplied knowledge bases, refer to the [Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/toc.htm), Chapter 4, "After Upgrading a Database", section "Upgrading Oracle Text". The [Oracle Text Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/text.112/e24435/toc.htm) contains both general instructions for upgrading from previous releases of Oracle Text and information on supplied knowledge bases.

### 4.24.3 Document Filtering Support

Starting with version 11.1.0.7, Oracle Text uses Oracle Outside In HTML Export for document filtering instead of filtering technology licensed from Autonomy, Inc. With the migration to Oracle Outside In HTML Export, several document formats are no longer supported. Refer to Appendix B of the [Oracle Text Reference](https://docs.oracle.com/cd/E11882_01/text.112/e24436/toc.htm) for a complete list of filter-supported document formats as well as for a list of formats that are no longer supported in 11.1.0.7.

## 4.25 Oracle Ultra Search

Oracle Ultra Search has been desupported and is not shipping with Oracle Database 11g Release 2 (11.2). In March of 2006, Oracle launched Oracle Secure Enterprise Search (SES). Oracle SES is a faster and more secure product built on the technologies originally developed for Ultra Search. Customers using Ultra Search are strongly recommended to migrate to Oracle SES.

See Also:

The Oracle Secure Enterprise Search page on the Oracle Technology Network at:

`http://www.oracle.com/technology/products/oses/index.html`

## 4.26 Oracle Warehouse Builder

For additional information about Oracle Warehouse Builder (OWB) in Oracle Database 11g release 2 (11.2), refer to the [Oracle Warehouse Builder Release Notes.](https://docs.oracle.com/cd/E11882_01/relnotes.112/e24470/toc.htm)

## 4.27 Oracle Workflow

Oracle Workflow is not shipping with Oracle Database 11g Release 2 (11.2).

## 4.28 Oracle XML DB

The following features are not supported with Oracle XML DB:

- Flashback Archive
- Editioning Views
- Exadata Hybrid Columnar Compression (EHCC)
- SecureFiles LOB Encryption
- Oracle Label Security (OLS) with a hybrid structured and unstructured XMLIndex on the same XML document.

### 4.28.1 Change in Semantics of xdb:defaultTable Annotation

There is a change in behavior in the semantics of `xdb:defaultTable` annotation while registering Oracle XML DB schemas in 11.2 as compared to 11.1 (reference Bug 7646934). If you specify `xdb:defaultTable="MY_TAB"` without specifying `xdb:sqlInline="false"`, Oracle XML DB creates the table as requested and implicitly marks it as an out-of-line table. This behavior is different from 11.1 where the `defaultTable` annotation was ignored when the `sqlInline` setting was missing.

### 4.28.2 VARRAY Storage Default Change

In Oracle Database 11g release 1 (11.1), the default value for `xdb:storeVarrayAsTable` changed from `FALSE` to `TRUE` for XMLType object-relational storage. This default applied to the default table, but not when creating XMLType object-relational tables and columns after the schema registration (reference Bug 6858659). In Oracle Database 11g Release 2 (11.2), all `VARRAY` data elements are created as tables by default. This provides a significant performance increase at query time. In addition, note the following:

- Tables created prior to 11.2 are not affected by this. The upgrade process retains storage parameters. This only affects tables created in 11.2 or later.
- You can retain the pre-11.2 default of `VARRAY` storage as LOBs if you have small `VARRAY` data elements and you read and or write the full `VARRAY` all at once. You have two options to revert to the pre-11.2 behavior:
	- Re-register the schema with `xdb:storeVarrayAsTable=FALSE`. This affects the default and non-default tables.
		- Or, when creating the table (for non default tables), you can use the `STORE ALL VARRAYS AS LOBS` clause to override the default for all `VARRAY` data elements in the XMLType. This clause can only be used during table creation. It will return an error if used in the `table_props` at schema registration time.
- For schemas registered prior to 11.2 (when the default storage for `VARRAY` data elements was `LOB`), you can use `STORE ALL VARRAYS AS TABLES` clause to override the default for all `VARRAY` data elements in the XMLType.

## 4.29 PL/SQL

Note the following when working with PL/SQL.

### 4.29.1 Secure Database By Default Changes

The `PUBLIC EXECUTE` privilege for the `DBMS_RANDOM` PL/SQL package will be deprecated in future Oracle Database releases (reference Bug 7591837). Users who need to run this PL/SQL package should be given explicit `EXECUTE` privileges.

### 4.29.2 DBMS\_SCHEDULER PL/SQL Package

Consider the following when working with the `DBMS_SCHEDULER` PL/SQL package.

#### 4.29.2.1 Event-Based Jobs

The Oracle Scheduler supports event-based jobs. These are jobs that are started when a message is enqueued into a database queue. When the database queue used for this purpose is a secure queue, the `QUEUE_SPEC` attribute of event-based jobs and schedules is a pair of the form `queue_name, agent_name`. The reason an agent has to be specified is to help the scheduler determine which messages the user can see. In the case of nonsecure queues, if the user has dequeue privileges on a queue, then he or she can dequeue any agent that is subscribed to the queue. This means that he or she can see all of the messages in the queue. In the case of secure queues, the user has to be granted privileges to not only the queue but to agents as well.

In addition to granting dequeue privileges, the queue owner has to make a call to `dbms_aqadm.enable_db_access()` to enable the user to dequeue as a specific agent. The agent could be subscribed to the queue using a rule that filters messages that the user should not see.

The scheduler always subscribes to every queue (secure or otherwise) using its own agent `SCHEDULER$_EVENT_AGENT`. Because the scheduler runs as user `SYS`, it can see all the messages in the queue. In the case of secure queues, however, this should not be done because the purpose of secure queues is to enable the queue owner to provide some type of limited access to the queue by users. Therefore, the scheduler requires an agent name in the `QUEUE_SPEC` attribute. This agent name is used solely for the purpose of determining which messages the user can see. The scheduler does not dequeue messages as this agent. When the scheduler receives a notification that a message has arrived in a secure queue, it performs the following checks for each event-based job that depends on the queue.

1. It checks to determine if the job owner has dequeue privileges on the queue.
2. It checks to see if the agent name provided in the queue spec can be used by the job owner.
3. It checks to see if the agent is currently subscribed to the queue.
4. It checks if the incoming message is visible to the agent.

If all of these checks succeed, then the scheduler launches the event-based job. Regardless of whether the checks pass, the message is dequeued using the agent `SCHEDULER$_EVENT_AGENT`.

When providing an agent for the `QUEUE_SPEC` attribute, the user can provide an existing agent name or have a new one created for this purpose. In either case, it is the user's or queue owner's responsibility to ensure that the agent dequeues its messages.

#### 4.29.2.2 Remote Jobs

The Oracle Scheduler supports running jobs on remote hosts and transferring files to or from remote hosts. To achieve this goal, it is first necessary to go through the setup described in the "Enabling and Disabling Remote External Jobs" section of Chapter 28 of the [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm). This feature also requires that Oracle XML DB HTTP Server be enabled on the database.

To check whether Oracle XML DB HTTP Server is enabled, you can use the following command:

```
SQL> SELECT DBMS_XDB.GETHTTPPORT() FROM DUAL;
```

If this statement returns `0`, then you need to enable Oracle XML DB HTTP Server on a non-zero port by logging in as `SYS` and issuing the following commands:

```
SQL> EXEC DBMS_XDB.SETHTTPPORT (port);
SQL> COMMIT;
```

Substitute `port` with Oracle XML DB HTTP Server port you wish to use.

### 4.29.3 DBMS\_SQL Package

In Oracle Database 11g release 1 (11.1), Oracle introduces a number of enhancements to `DBMS_SQL` to improve the security of the package:

- Prevent guessing of open cursor numbers
	A new error, `ORA-29471`, will be raised when any `DBMS_SQL` subprogram is called with a cursor number that does not denote an open cursor. When the error is raised, an alert is issued to the alert log and `DBMS_SQL` becomes inoperable for the life of the session.
	If the actual value for the cursor number in a call to `IS_OPEN` does denote a cursor that is currently open in the session, then the return value is `TRUE`. If the actual is null, then the return value is `FALSE`. Otherwise, you get the `ORA-29471` error.
	Note that the `DBMS_SQL.OPEN_CURSOR` function is the only `DBMS_SQL` subprogram that has no formal parameter for the cursor number. Rather, it returns a cursor number. Therefore, it is not within the scope of the rules.
- Prevent inappropriate use of a cursor
	Cursors are now better protected from security breaches that subvert known, existing cursors.
	Checks are always made when binding and executing. Optionally, checks may be performed for every single `DBMS_SQL` subprogram call. The check is:
	- `current_user` is the same on calling the subprogram in question as it was on calling the most recent parse.
		- The enabled roles on calling the subprogram must be a superset of the enabled roles on calling the most recent parse.
	As is always the case, for definer's right subprograms, roles are irrelevant.
	If either check fails, then `ORA-29470` is raised.
	The mechanism for defining when checks are performed is a new overload for the `OPEN_CURSOR` subprogram which takes a formal parameter, `security_level`, with allowed values `NULL`, `1` and `2`.
	When `security_level = 1` (or is `NULL`), the checks are made only when binding and executing. When `security_level = 2`, the checks are always made.
	This security regime is stricter than in 10.2 and previous releases. As a consequence, users of `DBMS_SQL` may encounter runtime errors on upgrade. While the regime makes for more secure applications, users may want to relax the security checks temporarily as they migrate to 11.1. If so, consult with Oracle Support Services on steps to relax the security checks.

### 4.29.4 UTL\_FILE Package

The `UTL_FILE` package no longer opens a file if that file is a symbolic link. This new restriction closes a known security hole in the `UTL_FILE` package.

If this security restriction poses an undue burden during migration, then contact Oracle Support Services for assistance.

### 4.29.5 Interoperability Between Releases

Interoperability between an 11.1 database or Forms client and a 10.1 or 10.2 database requires a minimum patchset level of 10.1.0.5 (for 10.1) or 10.2.0.2 (for 10.2).

An attempt to reference a 10.1 or 10.2 PL/SQL unit or view under the following circumstances fails with a `PLS-801[55916]` error unless the 10.1 or 10.2 environment has been patched to the correct level:

- A PL/SQL unit, anonymous block, trigger, call statement, or SQL statement on an 11.1 database runs a PL/SQL unit on a 10.1 or 10.2 database across a database link.
- A PL/SQL unit, anonymous block, trigger, or call statement on an 11.1 database references a view on a 10.1 or 10.2 database across a database link and the view directly or indirectly references a PL/SQL function or an object type.
- An 11.1 Forms client runs a PL/SQL unit in a 10.1 or 10.2 database using RPC.

To avoid the `PLS-801[55916]` error, a minimum patchset level of 10.1.0.5 (for 10.1) or 10.2.0.2 (for 10.2) is required.

There is no interoperability problem between 10.1 and 10.2 environments.

## 4.30 Pro\*C

The Pro\*C readme file is located at:

```
ORACLE_HOME/precomp/doc/proc2/readme.doc
```

## 4.31 Pro\*COBOL

The Pro\*COBOL readme file is located at:

```
ORACLE_HOME/precomp/doc/procob2/readme.doc
```

## 4.32 SQLJ

SQLJ in Oracle Database 11g release 2 (11.2) is supported with JDK 5.0 and JDK 6.0.

## 4.33 SQL\*Plus

The SQL\*Plus readme file is located at:

```
ORACLE_HOME/sqlplus/doc/README.htm
```

## 4.34 Summary Management

Note the following items when working with Summary Management.

### 4.34.1 Query Rewrite

The following items apply to Query Rewrite.

#### 4.34.1.1 Fine Grained Auditing (FGA)

If Fine Grained Auditing (FGA) is enabled on a table in the query, then Query Rewrite will not occur for this query.

#### 4.34.1.2 Use of PARTITION Clause

Query rewrite does not occur for queries that use the `PARTITION` clause in the `FROM` clause to access table partitions. In order for query rewrite to rewrite such queries, the `PARTITION` clauses must first be converted into equivalent selection predicates and added to the `WHERE` clause.

### 4.34.2 NLS Parameters

When using or refreshing certain materialized views, you must ensure that your NLS parameters are the same as when you created the materialized view. Materialized views that fall under this restriction contain the following constructs:

1. Expressions that may return different values, depending on NLS parameter settings
	It is recommended to write such expressions in the NLS-independent way. For example:
	```
	(date > DATE '2003-01-02')
	```
	Or:
	```
	(rate <= 2.150)
	```
2. Equijoins where one side of the join is character data
	The result of this equijoin depends on collation which can change on a session basis, giving an incorrect result in the case of query rewrite or an inconsistent materialized view after a refresh operation.
3. Expressions that generate internal conversion to character data in the select list of a materialized view, or inside an aggregate of a materialized aggregate view
	This restriction does not apply to expressions that involve only numeric data; for example, `a+b` where `a` and `b` are numeric values.

## 4.35 Oracle Streams

Note the following when working with Oracle Streams.

### 4.35.1 Oracle Streams Apply Handler Modifications Necessary for Handling New Error Messages That Replace ORA-1403 Errors

Customized DML and error handlers for Oracle Streams require modification to catch the additional Oracle errors `ORA-26786` and `ORA-26787` in place of the `ORA-01403 No data found` message. An `ORA-26787` error is raised if the row to be updated or deleted does not exist in the target table. An ORA-26786 error is raised when the row exists in the target table, but the values of some columns do not match those of the LCR.

### 4.35.2 Oracle Streams Advanced Queuing

Subscription names for Advanced Queuing notification will become canonical. Thus, registrations for `scott.queue1:sub` and `SCOTT.QUEUE1:SUB` are for the same entity and are represented in canonical form as `"SCOTT"."QUEUE1":"SUB"`.

### 4.35.3 UTL\_SPADV Load Privileges

An additional privilege is required to load the `UTL_SPADV` package into the Oracle Streams administrator schema. The Oracle Streams administrator schema must have `EXECUTE` privilege on `DBMS_LOCK` in order to load this package.

## 4.36 Open Bugs

This section lists known bugs for release 11.2.0.2. A supplemental list of bugs may be found as part of the release documentation specific for your platform.

### 4.36.1 Oracle Automatic Storage Management (Oracle ASM) Known Bugs

Bug 9655918

Increase in Oracle ASM disk group size for Oracle ACFS Database Home may be required.

Workaround: When creating a Database Home on Oracle ACFS, the ASMCA tool will default to a minimum of 6 GB for the Oracle ACFS Database Home. However, depending on the status and configuration of the disk group, additional storage may be required. Therefore, the recommendation is to use a minimum of 10 GB for the disk group to avoid any such issues, as reported by these messages:

```
ORA-15032: not all alterations performed 
ORA-15041: diskgroup "dg_name" space exhausted
```

Bug 9413827

An 11.2.0.1 Oracle Clusterware rolling upgrade to 11.2.0.2 fails when Oracle Cluster Registry (OCR) is on Oracle ASM.

Workaround: Apply the patch for bug 9413827 on 11.2.0.1 Oracle Grid Infrastructure for a cluster home before performing the upgrade.

Bug 9276692

Cannot permanently stop the Oracle ASM instance.

Workaround: If the Oracle ASM instance is disabled using SRVCTL, you must unregister Oracle ACFS-related resources to avoid restarting the Oracle ASM instance. Do this by executing the following command as root:

```
acfsroot unregister
```

### 4.36.2 Deinstallation Tool Known Bugs

Bug 9925724

If `Grid_home` is created directly under a root-owned directory, the deinstallation tool cannot remove the top-level home directory. An empty Oracle home directory remains at the end of the deinstallation.

Workaround: Run `rmdir` `ORACLE_HOME` using the root user on all nodes.

Bug 9924588

The deinstallation tool is not deleting the old Grid home after upgrading to a new release.

Workaround: After upgrading from previous releases, if you want to deinstall the previous release Oracle Grid Infrastructure Grid home, then you must first change the permission and ownership of the previous release Grid home. Log in as root, and change the permission and ownership of the previous release Grid home using the following command syntax, where `oldGH` is the previous release Grid home, `jsmith` is the Oracle Grid Infrastructure installation owner, and `oldGHParent` is the parent directory of the previous release Grid home:

```
#chmod -R 755 oldGH 
#chown -R jsmith oldGH 
#chown jsmith oldGHParent
```

As the installation user, use the 11.2.0.2 standalone deinstallation tool to remove `oldGH`.

Bug 9871334

If the deinstallation tool is launched from Oracle home, it fails to delete the `ORACLE_HOME` `/deinstall` directory. This issue is not seen with the standalone deinstallation tool. An empty `ORACLE_HOME` `/deinstall` directory remains at the end of deinstallation.

Workaround: Manually delete empty directory `ORACLE_HOME` `/deinstall` and `ORACLE_HOME` at the end of the deinstallation.

Bug 9406768

The 11.2 deinstallation utility is removing all the homes under Oracle base if these homes are not using the same central inventory and the deinstallation utility finds this home is the only one registered in inventory.

Workaround: While installing 11.2 products:

- Oracle does not recommend using multiple central inventories. Avoid this if possible.
- If for some reason a different central inventory is required, use a different Oracle base directory for each central inventory.

Bug 8644344

When running the deinstallation tool to deinstall the database, you will be prompted to expand the Oracle home and to select a component. If you select the top level component, `Oracle Database Server`, and do not select the Oracle home, OUI does not show the message to run the deinstall utility and proceeds with the deinstallation of the database.

Workaround: Run the deinstallation tool to deinstall the Oracle home.

Bug 8635356

If you are running the deinstall tool from `ORACLE_HOME` that is installed on shared NFS storage, then you will see errors related to `.nfs` files during `ORACLE_HOME` clean up.

Workaround: To remove the `ORACLE_HOME`, run the `rm -rf` `ORACLE_HOME` command after the deinstall tool exits. Alternatively, you can use the standalone `deinstall.zip` and specify the location of the `ORACLE_HOME`.

### 4.36.3 Oracle ACFS Known Bugs

Bug 10019796

When `acfsutil encr info` command is run on a file or a directory on which encryption has never been enabled, the command produces no output. Furthermore, when `acfsutil encr info` is run on a directory with the recursive (`-r`) option and encryption has never been enabled on that directory, the command produces no output for the directory or any files contained in that directory.

Workaround: When `acfsutil encr info` is run on an individual file or directory and the command produces no output, it implies that encryption is not enabled on that file or directory.

When `acfsutil encr info` is run on a directory with the recursive (`-r`) option and the command produces no output for the specified directory or one of its subdirectories, it implies that encryption is not enabled on that directory. To see the encryption status of files in that directory, run `acfsutil encr info` on each file individually.

Bug 10069735

In a cluster with a password-protected key store, when an Oracle ACFS file system using encryption is mounted through the Oracle ACFS mount registry, the administrator is not prompted to enter the key store password. Although the process of mounting the file system succeeds, not all information required for Oracle ACFS encryption to work correctly is made available to the file system. In this case, encryption is not operational on this file system and any encrypted files in the file system are not available for read or write.

Workaround: In a cluster with a password-protected key store, do not use the Oracle ACFS mount registry for mounting any file systems that are using encryption. If some file systems are already mounted through the Oracle ACFS mount registry, unmount them and remove any such file systems from the mount registry to avoid possible unavailability of encrypted data in the future. Then, remount these file systems without using the Oracle ACFS mount registry, providing the correct password when requested.

Bug 9975343

In some situations when `acfsutil encr set` or `acfsutil sec prepare` commands are run from multiple nodes in succession, the `.Security` directory in the mount point may be created incorrectly.

If this happens, two entries will be shown for.`Security` when listing the contents of the mount point, and the `acfsutil sec prepare` command will fail to add the logging and backup directories to their respective system realms if this command was the last to be run.

Workaround: If `acfsutil encr set` or `acfsutil sec prepare` commands are to be performed in succession, executing the commands from the same node will avoid the problem.

The problem can also be avoided by listing the contents of the `.Security` directory before running the second command.

However, if the problem is encountered, it can be resolved by first removing both security and encryption from the file system using `acfsutil encr set -u` and `acfsutil sec prepare -u` and then removing the `.Security` directory. The removal of the `.Security` directory will have to be performed twice.

Once security and encryption have been removed from the file system and the `.Security` directory has been deleted, the `acfsutil sec prepare` or `acfsutil encr set` commands may be run again on the file system.

Bug 9958114

If the standby file system is initialized for replication, but the primary file system is not, `repl terminate` of the standby will loop forever.

Workaround: Use `acfsutil repl terminate standby immediate` to terminate the standby under these conditions.

Bug 9947559

After a certain number of retries, the `acfsrepl_transport` daemon attempts to failover to another node if it cannot communicate with the remote site. If there is no other node for the daemon to failover to, or after a certain number of failover attempts, Oracle Clusterware stops trying to failover and the transport daemon will not be running. Not running the transport daemon causes replication to stall and eventually the file systems can run out of space.

Workaround: Run `acfsutil repl bg start` `mnpt` after the communication problem is corrected.

Bug 9940090

Unable to communicate with remote site if the disk group is forced dismounted. The root cause of this issue is that the service name associated with the file system is not being unregistered when the disk group is forced dismounted.

Workaround: Unmount the file system whose disk group was forced dismounted. This will unregister the service, thereby allowing the remote site to choose another node with the disk group and file system mounted for communication.

Bug 9896821

The following are alert log messages pointing to trace files that do not indicate an actual problem:

```
ORA-19505: failed to identify file 
"/scratch/primary/.ACFS/repl/ready/receipt.transport.cord242.12786023 69" 
ORA-27037: unable to obtain file status 
Linux-x86_64 Error: 2: No such file or directory
```

Workaround: None.

Bug 8644639

When creating an Oracle ACFS mount point and adding it to the registry, the mount point is not mounted automatically if the following conditions are met:

1. The mount point directory was previously registered with the Oracle ACFS Registry.
2. The mount point directory had been previously mounted.
3. The mount point had then been unmounted and removed from the Oracle ACFS Registry.
4. The `ora.registry.acfs` resource has not been restarted since the mount point was deleted from the registry.

Workaround: Remove the mount point directory from the file `/tmp/``.usm_state_file`.

### 4.36.4 Oracle ASM Dynamic Volume Manager (Oracle ADVM) Known Bugs

Bug 9683229

Oracle ADVM does not support mounting ext3 file systems over Oracle ADVM with the mount barrier option enabled. The mount barrier option is enabled by default on SLES10.

Workaround: Mount ext3 file system with `-o barrier=1`. For example:

```
mount -o barrier=0 /dev/asm/myvol-131 /mnt
```

### 4.36.5 Oracle Application Express Known Bugs

Refer to "Open Bugs and Known Issues" in [Oracle Application Express Release Notes](https://docs.oracle.com/cd/E11882_01/relnotes.112/e11944/toc.htm).

### 4.36.6 Oracle Clusterware Known Bugs

Bug 10062301

After a non-rolling clusterware upgrade from 11.2.0.1 to 11.2.0.2, the `CLUSTER_NAME` parameter is not set in the `clusterware_home _path` `/crs/install/crsconfig_params`. This affects the `addNode` scenario after the upgrade.

Workaround: Run the following:

1. Run `clusterware_home_path` `/bin/olsnodes -c` to get the cluster name.
2. Edit the `clusterware_home_path` `/crs/install/crsconfig_params` and update the `CLUSTER_NAME` entry as `CLUSTER_NAME=` `clustername_acquired_in_step1`.

Bug 10055232

The `root.sh` scripts fails after downgrading from 11.2.0.2 to 11.2.0.1.

Workaround:

Downgrade using the following steps when Oracle Cluster Registry (OCR) and voting disk are not on Oracle ASM:

1. Stop Oracle Clusterware running from the 11.2.0.2 home and verify that it is stopped. For example:
	```
	11.2.0.2_Home/bin/crsctl stop crs
	11.2.0.2_Home/bin/crsctl check crs
	```
2. Copy the OLR backup file and verify that the `olrconfig_loc` and the `crs_home` properties in the `olr.loc` file point to the 11.2.0.1.0 home. For example:
	```
	cd location_of_olr_loc
	cp olr.loc.bkp olr.loc
	```
	Note that `location_of_olr_loc` is platform-specific. Refer to the platform-specific documentation for the location of `olr.loc` on your system.
3. On the last node to downgrade, format OCR with the 11.2.0.1.0 snapshot. For example:
	```
	ocrconfig -import 11202_crshome/cdata/ocr11.2.0.1.0
	```
4. Remove one or more voting files. The voting file is located at the location given by the user while installing 11.2.0.1 prior to the upgrade to 11.2.0.2. Usually, it is located at the same place as OCR. For example:
	```
	rm vote_file
	```
5. Start the stack in exclusive mode. For example:
	```
	11.2.0.1_Home/bin/crsctl start crs -excl
	```
6. Add the voting file or files. For example:
	```
	crsctl add css votedisk voting_file
	```
7. Stop the stack running in exclusive mode and verify it stopped. For example:
	```
	11.2.0.1_Home/bin/crsctl stop crs -f
	11.2.0.1_Home/bin/crsctl check crs
	```
8. On all nodes, start the Oracle Clusterware from the 11.2.0.1 home. For example:
	```
	11.2.0.1_Home/bin/crsctl start crs
	```

Downgrade using the following steps when Oracle Cluster Registry (OCR) and voting disk are on Oracle ASM:

1. If the `compatible.asm` attribute for the OCR disk group is set to 11.2.0.2, then you must migrate the OCR to a disk group with `compatible.asm` set to 11.2.0.1 using the `ocrconfig -add` and `ocrconfig -delete` commands before starting the downgrade procedure.
2. Stop Oracle Clusterware from running from the 11.2.0.2 home and verify that it is stopped. For example:
	```
	11.2.0.2_Home/bin/crsctl stop crs
	11.2.0.2_Home/bin/crsctl check crs
	```
3. Copy the OLR backup file and verify that the olrconfig\_loc and the `crs_home` properties in the `olr.loc` file point to the 11.2.0.1.0 home. For example:
	```
	cd location_of_olr_loc
	cp olr.loc.bkp olr.loc
	```
	Note that `location_of_olr_loc` is platform-specific. Refer to the platform-specific documentation for the location of `olr.loc` on your system.
4. On the last node to downgrade, start the 11.2.0.2.0 Oracle Clusterware stack in exclusive mode. For example:
	```
	11.2.0.2_Home/bin/crsctl start crs -excl -nocrs
	```
5. Delete the voting disk from the Oracle ASM disk group. For example:
	```
	11.2.0.2_Home/bin/crsctl delete css votedisk <diskgroup>
	```
6. Stop Oracle Clusterware running in exclusive mode from the 11.2.0.2 home and verify it is stopped. For example:
	```
	11.2.0.2_Home/bin/crsctl stop crs -f
	11.2.0.2_Home/bin/crsctl check crs
	```
7. On the last node to downgrade, start the 11.2.0.1.0 Oracle Clusterware stack in exclusive mode. For example:
	```
	11.2.0.1_Home/bin/crsctl start crs -excl
	```
8. Stop the Oracle Clusterware daemon. For example:
	```
	11.2.0.1_Home/bin/crsctl stop resource ora.crsd -init -f
	```
9. On the last node to downgrade, format OCR with 11.2.0.1.0 snapshot. For example:
	```
	11.2.0.1_Home/bin/ocrconfig -import 11202_crshome/cdata/ocr11.2.0.1.0
	```
10. Verify the integrity of OCR. For example:
	```
	11.2.0.1_Home/bin/ocrcheck
	```
11. Stop the stack running in exclusive mode and verify it is stopped. For example:
	```
	11.2.0.1_Home/bin/crsctl stop crs -f
	11.2.0.1_Home/bin/crsctl check crs
	```
12. On all nodes, start Oracle Clusterware from the 11.2.0.1 home. For example:
	```
	11.2.0.1_Home/bin/crsctl start crs
	```
13. Verify the OCR integrity from all nodes. For example:
	```
	11.2.0.1_Home/bin/cluvfy comp ocr -n all -verbose
	```

Bug 10044507

While verifying `udev` attributes during installation, upgrade or manual execution of `cluvfy`, an error may be reported even though the expected `udev` attributes are defined correctly in the appropriate `udev` rules file. For example:

```
PRVF-5184 : Check of following Udev attributes of "<node>:<path>" failed: 
"[Permissions: Found='0600' Expected='0660']"
```

This error is due to the expectation that `udev` attributes for the device are expected to be in a specific order in the `udev` rules file.

Workaround: When specifying the device information in the `udev` rules file, make sure that the `OWNER`, `GROUP` and `MODE` are specified in this order before any other characteristics are specified. For example, if you want to include the `ACTION` characteristic on the `udev` line, you should specify the following:

```
KERNEL=="<device>",  OWNER="oracle", GROUP="dba", MODE="660", ACTION=="add|change"
```

And, do not specify the following:

```
KERNEL=="<device>", ACTION=="add|change", OWNER="oracle", GROUP="dba", MODE="660"
```

Bug 10043601

During Oracle Grid Infrastructure for a cluster installation, when a file created by `dd` on NFS is used as Oracle ASM disks, the prerequisite check for Oracle ASM devices reports an error (with `PRVF-5150`) that the given disk is not a valid path.

Workaround: This error can be ignored.

Bug 10041397

During Oracle Grid Infrastructure for a cluster installation on Oracle Virtual Machine (Oracle VM), when virtual shared disks are used as Oracle ASM devices, the prerequisite check for Oracle ASM devices gives a warning that these devices are not shared. For example:

```
PRVF-5149 : WARNING: Storage "/dev/xvde1" is not shared on all nodes
```

Workaround: This warning can be ignored.

Bug 10033106

When running `addNode.sh` with the `-silent` flag to add a new node to Oracle Clusterware, if there are any failures during `cluvfy stage -pre nodeadd`, no error messages will be displayed. The `addNode` operation will be terminated and the new node will not be added.

Workaround: Run `cluvfy stage -pre nodeadd` command from an existing node of the cluster. Look at the errors reported and fix them. If you want to ignore the errors and continue with the `addNode` operation, set the environment variable `IGNORE_PREADDNODE_CHECKS` to `Y` and retry the addNode operation.

Bug 10032601

During Oracle Grid Infrastructure for a cluster installation or during invocation of the `cluvfy stage -pre crsinst` command, the prerequisite check for user existence reports an error if the numerical value of the user ID exceeds 6 digits. This is applicable to both the local and NIS users.

Workaround: The reported user existence validation error can be ignored.

Bug 10025999

If the Oracle High Availability Services Daemon (OHASD) crashes and restarts while the Oracle Clusterware stack is already running, subsequent Cluster Verification Utility (CVU) checks may produce the following informational messages:

```
INFO: PRVF-9656 : The CTSS command to query time offset and reference failed on node nodename with error message "" 
INFO: Query of CTSS for time offset failed
```

Workaround: These informational messages can be ignored.

Bug 9978765

Oracle Grid Infrastructure for a cluster cannot be upgraded to Oracle Grid Infrastructure 11g release 2 Patchset 2 from Oracle Clusterware releases 10gR1, 10gR2 and 11gR1 when there are multiple private network interfaces configured in the previous release. This can be verified by running the OIFCFG `getif` command prior to upgrading, and inspecting the number of interfaces marked `cluster_interconnect`.

Workaround: Run the steps in the following procedure to upgrade Oracle Grid Infrastructure for a cluster. This example assumes a 2-node (`A` and `B`) cluster:

1. Shut down all database instances and Oracle ASM running on nodes `A` and `B` in the 10gR1, 10gR2 or 11gR1 cluster.
2. On node `A`, identify the private network interface used by Oracle Clusterware using the OLSNODES `-p` command. Delete the rest of the private network interfaces marked `cluster_interconnect` using OIFCFG `delif -global` `if_name` command.
3. Start up all database instances and Oracle ASM running on nodes `A` and `B` in the 10gR1, 10gR2 or 11gR1 cluster.
4. Proceed upgrading the Oracle Grid Infrastructure for the cluster 11g release 2 (11.2).
5. Verify that the Oracle Grid Infrastructure for a cluster upgrade is complete using `crsctl query crs activeversion` command. Add the private network interfaces which were removed in Step 2 using `oifcfg setif -global` `if_name``:cluster_interconnect` command.

Bug 9974223

Oracle Grid Infrastructure for a cluster needs multicast communication on 230.0.1.0 addresses working properly between the cluster nodes.

When first attempting to start an 11.2.0.2 cluster node, either during a fresh install or after an upgrade attempt, it is possible that the node will be unable to join the cluster. The Oracle Cluster Synchronization Services (OCSSD) will report a failure to join the existing cluster members.

This will be noted as an inability for the CSS to connect to the other active members of the cluster.

The problem occurs because the clusterware in 11.2.0.2 uses multicast messages to initiate communications on the 230.0.1.0 address. If multicast on these addresses is not enabled for the private interfaces, then the clusterware will be unable to connect to it's peer nodes.

Workaround: Contact your network IT department and have them validate that multicast communications are working across all nodes of the cluster on the private interconnect. In particular, ensure that multicast communications on the 230.0.1.0 addresses are working properly between the cluster nodes.

Bug 9951257

If Oracle Cluster Registry (OCR) is on a disk group and that disk group cannot be automatically mounted, it prevents, Cluster Ready Services Daemon (CRSD) from starting (also reference Bug 9799693).

Workaround: You must recover the OCR disk group manually. Determine the reason the disk group has failed to mount, correct the problem and mount the disk group. See also message `CRS-5019` for recovery options.

Bug 9948549

If the agent terminates while starting a database or Oracle ASM instance, it is possible that the instance startup will not complete.

Workaround: Stop and restart the instance using `srvctl` or `sqlplus`.

Bug 9877357

The Oracle Enterprise Manager configuration fails during DBCA if a policy-managed database's name contains `'_'` or more than 8 characters.

Workaround: Choose a database name accordingly.

Bug 8974576

`REMOTE_LISTENER` parameter was not changed after a `SRVCTL ADD SCAN_LISTENER` or `SRVCTL REMOVE SCAN_LISTENER` command.

In a future release, Oracle Clusterware may start managing `REMOTE_LISTENER` as part of a project to support multiple public networks each with their own `SCAN`. But in release 11.2, because of the need to include node VIPs in the `REMOTE_LISTENER` parameter of pre-11.2 databases that are upgraded, Oracle Clusterware does not have all the data needed to keep `REMOTE_LISTENER` properly updated. This is, instead, implemented by DBCA and DBUA, or by manual means.

Workaround: To manually change the REMOTE\_LISTENER parameter, run the following:

```
SQL> ALTER SYSTEM SET REMOTE_LISTENER='t2000-cluster0-scan.t2000-18.oraclecorp.com' sid='*' scope=memory; 

System altered. 
 
SQL> ALTER SYSTEM REGISTER;
 
SQL> SHOW PARAMETER LISTENER;
 
NAME                                 TYPE        VALUE 
------------------------------------ ----------- ------------------------------ 
remote_listener                      string      t2000-cluster0-scan.t2000-18.o
```

Bug 8737732

If you upgrade a previous Oracle Clusterware release to Oracle Grid Infrastructure for a cluster 11g release 2 (11.2.0.2), Cluster Verification Utility (CVU) may fail if the Oracle Grid Infrastructure for a cluster installation owner does not have correct permissions or ownership of the raw devices on which the Oracle Cluster Registry and voting disk files are placed.

Workaround: Check CVU output in the installation log file, and change permissions or ownership of raw devices to the settings specified in the log file. Click Retry to run the configuration tool again.

Bug 8733944

Due to a problem in Oracle Clusterware starting with release 11.1.0.7, with the patches required for Oracle Exadata support or 11.1.0.7 CRS bundle Patch 1, in some cases the CSS daemon may fail when the clusterware is brought down on another node, either due to a shutdown command or a failure.

The symptom is an `ASSERT` in the CSSD log indicating that a maximum value has been exceeded. For example:

```
Group ID of xxxx exceeds max value for global groups
```

Workaround: Oracle recommends that customers running with the Oracle Exadata support patches or 11.1.0.7 CRS Bundle Patch 1 apply the patch for this bug to avoid this problem.

This problem may also be seen during an upgrade from 11.1.0.7 with patches as indicated above. To eliminate the potential of an 11.1.0.7 node failing during upgrade, the patch for this bug may be applied to the 11.1.0.7 nodes prior to upgrade.

When upgrading, it is recommended that the upgrade be completed on all nodes without restarting any non-upgraded nodes during the upgrade. If an 11.1.0.7 node does fail while performing the upgrade, it should be upgraded as opposed to restarted.

Bug 8668083

In Oracle Restart environments, the following commands cannot perform a verification and return an error message if the user equivalence does not exist for the local node:

```
cluvfy stage -pre hacfg
cluvfy stage [-pre | -post] cfs
cluvfy stage [-pre | -post] acfscfg
cluvfy comp admprv
cluvfy stage -pre dbcfg
cluvfy stage -pre dbinst
```

Workaround: Configure SSH in Oracle Restart.

Contact Oracle Support Services to obtain the patches for these bugs and apply the patches to the Oracle Database home.

Bug 8666509

A deinstallation of Oracle Clusterware should ask you to detach any pre-11.2 Oracle RAC homes from the Oracle inventory.

Workaround: After you deconfigure and deinstall an upgraded 11.2 Oracle RAC home and want to continue with deconfiguration and deinstallation of the Oracle Grid Infrastructure for a cluster home, first detach any pre-11.2 Oracle RAC software homes from the central Inventory.

Bug 8657184

If two network interfaces are configured as public network interfaces in the cluster, the failure of one public interface on a node does not result in automatic VIP failover to the other public interface.

Workaround: If multiple public networks interfaces are present, then use interface bonding for high availability. At the Oracle Clusterware installer "Specify Network Interface Usage" screen, choose only one (bonded) interface as public. When configuring public networks with `srvctl` `add` `nodeapps` or `srvctl` `add` `vip`, specify only a single network interface name in the `-A` or `-S` argument.

Bug 8288940

Creating pre-11.2 Oracle RAC database in 11.2 Oracle Grid Infrastructure for a cluster environment using DBCA may fail with following messages. When using a cluster file system as storage, you see the following message:

```
ORA-00119: invalid specification for system parameter REMOTE_LISTENER
```

When using Oracle ASM as storage, you see the following message:

```
DBCA could not startup the ASM instance configured on this node
```

Workaround: Apply the patch for this bug in pre-11.2 database home. This patch is needed for 10.2.0.4, 11.1.0.6 and 11.1.0.7 database releases. No patch is needed for release 10.2.0.5.

Bug 3841387, 8262786, 8373758, 8406545, 8441769

Oracle resources for 10.1, 10.2 and 11.1 Oracle RAC databases may not operate properly after upgrading Oracle Clusterware to 11.2.

Workaround: Apply the patches for Bugs 3841387, 8262786, 8373758, 8406545, and 8441769 to the Oracle Database home.

### 4.36.7 Oracle Data Pump Known Bugs

Bug 10013976

When a database level, schema level, or queue table database export log generated from an 11.2 database is imported into an 11.2 database, `ORA-1403` errors may be raised during an Oracle Streams Advanced Queuing (AQ) procedural import action. Import completes successfully with errors.

Workaround: None. The `ORA-1403` errors in the import log are not fatal. Import of database objects including AQ queues completes successfully.

### 4.36.8 Oracle Database Vault Known Bugs

Bug 10225918

The stated issue can be reproduced when Database Configuration Assistant (DBCA) attempts to configure Database Vault while the local listener is not properly configured. Since this failure leads to partially populated metadata, some Database Vault features may not function as expected.

Workaround: The following steps explain a workaround to this issue:

1. Remove Database Vault completely using `rdbms/admin/dvremove.sql`.
2. Make sure that local listener (`LISTENER`) is configured properly.
3. Retry Database Vault installation and configuration using DBCA.

Optionally, you can manually run the failed DVCA operations (for example, `dvca -action addlanguages` and `catmacpost.sql`) to recover from the failure by following the steps previously mentioned. Make sure that local listener (`LISTENER`) is configured properly before running the steps.

Bug 8686258

Database Vault policy cannot be managed in Oracle Enterprise Manager Database Control because the following message is displayed in Database Vault Administration page:

```
"OPERATOR TARGET" privilege does not exist.
"You must have OPERATOR TARGET privilege to perform this operation."
```

Workaround: To manage Database Vault policy using Oracle Enterprise Manager, the Database Vault administrator must have the EM Administrator privilege. If you do not want to grant the EM Administrator privilege to the Database Vault administrator, then use the Database Vault Administrator page directly. For additional information, see [Oracle Database Vault Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23090/dba.htm#DVADM70290).

Bug 8474817

If a user is granted Database Vault scheduler job authorization by `DBMS_MACADM.AUTHORIZE_SCHEDULER_USER` API, dropping this user does not remove the user from the list of authorized users.

Workaround: Invoke the `DBMS_MACADM.UNAUTHORIZE_SCHEDULER_USER` API call to remove the user's authorization manually.

Bug 8341283

The `ACTION_NAME` entry in the `DVSYS.AUDIT_TRAIL$` table displays `Realm Authorization Audit` for a failed realm enforcement if the audit option is set to audit on success and failure. The `RETURNCODE` will show the correct error code that was triggered.

Workaround: Use the `RETURNCODE` value to determine whether a violation has occurred and the `ACTION_NAME` column to identify whether the audit was generated by a realm enforcement or command rule enforcement.

Bug 8247647

Dropping a user does not automatically remove the user from the list of authorized users for Oracle Data Pump.

Workaround: Invoke the `DBMS_MACADM.UNAUTHORIZE_DATAPUMP_USER` API call to manually remove the user's authorization for Oracle Data Pump.

Bug 7033772

Database Vault Administrator (DVA) does not work after an Enterprise Manager DBControl upgrade.

Workaround: Manually redeploy DVA after DBControl has been upgraded. You can follow the steps described in Appendix C, Section "Deploying Database Vault Administrator to the Database Console OC4J Container" of the [Oracle Database Vault Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23090/dvca.htm#DVADM71067).

### 4.36.9 Oracle Database Enterprise Edition Known Bugs

Bug 10107649

Creating a draft service request (SR) might fail when uploading a correlated package.

Workaround: Upload the correlated package to an existing SR (normally the same SR as the main package).

Bug 9951827

Transportable tablespace import does not handle timestamp with timezone version change.

If a transportable dumpfile produced in release 11.2.0.2 contains tables with timestamp with timezone columns and the version of the timezone table on the target database is different than that from the source database, the import is be prevented from running.

If a dumpfile produced prior to release 11.2.0.2 had a different timezone table version than that of the target, then the import is be prevented from running.

Workaround: Make sure the timezone tables for the import and export databases are the same.

Bug 9859532

Current implementation of node-specific network interfaces requires complete definition of all networks used by Oracle RAC for that node (that is, either node abides by global network configuration or it defines its own node-specific network configuration).

As a corollary, once the first node-specific network interface is defined for a given node, Oracle RAC will not consider any configured global network interfaces that are already configured and may have applied for the same node.

While this is correct, it presents a problem. If the cluster had a working global network configuration, the moment a user updates it (using `oifcfg`) to define a node-specific `public` interface, a global configuration will not be considered for this node, and it will have only one newly-defined `public` interface. Any cluster interconnects that existed in the global network configuration, and may still resolve fine for this node, will not be considered valid. Thus, the node loses cluster interconnects and PCW stack goes down on that node.

Workaround: If the node belongs to a global cluster network configuration, then if there is an intent to make network configuration node-specific, the first defined node-specific interface must be cluster interconnect, so that node never loses interconnect with other cluster nodes. Then, other node-specific interfaces can be defined as necessary.

Bug 9181675

The `asmgidwrap` script needs to be called if you are creating a database manually on Oracle ASM to avoid a permission error.

Workaround: For a role-separated installation (that is, there is a different user and group for grid and RDBMS), use DBCA to create the database that automatically calls `asmgidwrap` script while creating a database on Oracle ASM. If you choose to create a database manually, the script needs to be called explicitly so the proper group can be set to avoid a permission error.

Bug 8729627

When using 11.1 DBCA to remove a database on a cluster running 11.2 Oracle Clusterware, a `PRKP-1061/CRS-2524` error may be displayed because the database resource is locked.

Workaround: You can ignore the message. Click OK to continue.

Bug 8679182

When configuring a database on a cluster that has multiple public subnets defined for its VIPs (for example, using a command similar to `srvctl add vip -k 2 -A ...`), the database agent automatically sets `LOCAL_LISTENER` to the listener on the default network. This may duplicate a listener set in `LISTENER_NETWORKS`.

Workaround: Do not specify listeners in `LISTENER_NETWORKS` that are on the default public subnet.

Bug 8671032

In Oracle Enterprise Manager, the "TIP" obtained from the "Run Analysis" on the Automatic Undo Management page is not correct. For example, the Recommended Undo Tablespace Size should be three times the Minimum Size, to allow for workload fluctuations, but Oracle Enterprise Manager shows different values.

Workaround: The "TIP" should read as follows:

```
Oracle advises that you configure the undo tablespace to be three times the Recommended Undo Tablespace Size to allow for workload fluctuations
```

Bug 8304261

If compression attributes are specified at the table level and in the sub-partition template, newly created interval partitions do not use the compression attributes defined in the sub-partition template, but use the table level compression instead.

Workaround: Redefine compression attributes in sub-partitions.

### 4.36.10 Oracle Enterprise Manager Database Control Known Bugs

Bug 10162200

Clone Database offers an option to configure Database Control during the clone process. If that option is specified when creating an Oracle ASM-based clone database, Database Control is not configured.

Workaround: Manually run Oracle Enterprise Manager Configuration Assistant (EMCA) to setup Database Control.

Bug 9766628

`emctl` commands did not return valid results as expected.

Workaround: The `emctl` command needs to be run from an Oracle Database home. Do not invoke this command from the Oracle Grid Infrastructure for a cluster home.

Bug 8674920

If the installation owners for the Oracle Grid Infrastructure for a cluster and Oracle Database are different, then the owners of Oracle ASM binaries and Oracle Enterprise Manager Agent binaries are also different. When you start Support Workbench, the error message `Error Operation failed - Operation failed` might appear, because the Oracle Enterprise Manager Agent is running as a different user, and Support Workbench does not have permissions for the Oracle ASM target.

Workaround: None.

Bug 8350597

If Database Control is running in an IPv6 environment, then you cannot use it to monitor Exadata cells and you should not add Exadata cells as targets.

Workaround: None.

### 4.36.11 Oracle Database QoS Management Known Bugs

Bug 10019209

This bug applies to platforms that support the Cluster Health Monitor (CHM). If an Oracle Clusterware-managed database service is in a stopped but not disabled state, it will be started by Oracle Database QoS Management if the server hosting that service is not detected to be in a memory overcommitted state. If memory is overcommitted, then all enabled services will be stopped even if they were manually started. The desired behavior is to only start services on the transition from a memory overcommitted state (red) to a normal state (green). If a service is manually started when the server is in the red state, that service should not be shut down.

Workaround: Stop and disable services that you want to remain in the stopped state or disable QoS Management from the Oracle Enterprise Manager Console.

Bug 10019186

The Oracle Database QoS Management feature that protects servers from overcommitting memory is only available on platforms that also support Cluster Health Monitor (CHM).

Workaround: None.

### 4.36.12 Oracle OLAP Known Bugs

Bug 9917299

If the database is installed using the seed provided in the installation kit, and the OLAP option is not selected, then either at the end of the installation or some time later, the OLAP Analytic Workspace and OLAP API components will be reported as invalid.

This will not affect the running of the instance in any way, other than the error messages.

Workaround: Do one of the following as a workaround:

- Ignore the error.
- Enable OLAP (or the offending option).
- Create and use your own seed database that does not include OLAP.

Bug 9545221

Importing an materialized view-enabled cube or cube dimension whose source table is not part of the target schema fails with an `Object not found` error.

Workaround: Disable materialized views for the failing object prior to the import, then reenable them when the source tables are present.

### 4.36.13 Oracle SQL\*Loader Known Bugs

Bug 9301862

When external table code reads very large files on disks served by NFS, the I/O performance of the read can slow down over time. This is caused by NFS caching blocks from the file in memory as it is read. Since these blocks are not re-read, the time spent maintaining the cache slows down the I/O operations.

Workaround: The current behavior (of not using the `O_DIRECT` flags) remains the default. You can enable the use of the `O_DIRECT` flag in the following ways:

- Enable fix control for this bug and set it to `ON` with the following command:
	```
	ALTER SESSION SET "_fix_control"='9301862:ON';
	```
	When fix control is enabled, the external table code looks at the `FILESYSTEMIO_OPTIONS` configuration parameter and if it is set to either `DIRECTIO` or `SETALL`, then the `ORACLE_LOADER` access driver will specify the `O_DIRECT` flag when opening data files for reading. If the `FILESYSTEMIO_OPTIONS` parameter is not set or if it is set to other values, then the access driver will not attempt to use `O_DIRECT` unless you choose the following option.
- Use the new `IO_OPTIONS` clause in the access driver to specify direct I/O. The clause is part of the larger `RECORDS` clause. The syntax is:
	```
	IO_OPTIONS (DIRECTIO | NODIRECTIO)
	```
	If `DIRECTIO` is specified, then the access driver uses `O_DIRECT` flag when opening the file. If `NODIRECTIO` is specified, then the access driver does not use the `O_DIRECT` flag. Note that the action specified by `IO_OPTIONS` is performed regardless of the setting of `_fix_control` for this bug.
	Note that the first option is a way to enable the use of `O_DIRECT` for all external tables while the second option allows `DIRECTIO` to be used or not used for specific external tables.

### 4.36.14 Oracle Streams Known Bugs

Bug 10115681

When the client application detaches from an inbound server while transmitting a transaction with more than 1000 logical change records (LCRs), the coordinator process aborts because it receives an invalid dequeue low-watermark from the reader server.

Workaround: Avoid detaching from the inbound server in the middle of a large transaction. Wait until the `COMMIT` LCR for the large transaction is sent and then detach.

### 4.36.15 Oracle Universal Installer Known Bugs

Bug 10253337

`addnode.sh` fails if `DISPLAY` is not set.

Workaround: Run the `addnode.sh` command with `-silent` flag.

Bug 10096522

Running the `configToolAllCommands` configuration step after the silent installation of Oracle Grid Infrastructure software or database software may fail if the installer session was restarted while choosing to apply software updates.

Workaround: Change the value for `JRE_LOCATION` property in `ORACLE_HOME` `/oui/bin/runconfig.sh` to `ORACLE_HOME` `/jdk/jre`, and then run `configToolAllCommands` again.

Bug 10053840

`clone` or `addNode` operations may fail if the installer session was restarted while choosing to apply software updates in source Oracle home.

Workaround: Change the value for `JRE_LOCATION` property in `ORACLE_HOME` `/oui/oraparam.ini` to `../../jdk/jre`.

Bug 10053090

During the prerequisite checks step of installation, the OUI may display an error with text `-1`, and the prerequisite page result shows `No results`.

Workaround: Rerun the prerequisites by clicking on the `Check Again` button.

Bug 8729326

When upgrading to 11.2 Clusterware, the Installer invokes ASMCA in silent mode to upgrade Oracle ASM into Oracle Grid Infrastructure for a cluster home. Oracle ASM upgrade is handled in rolling fashion when upgrading from 11.1.0.7. Prior versions of Oracle ASM instances are upgraded in non-rolling fashion and Oracle ASM-based databases are bounced without any prior warning.

Workaround: You can plan your database outage to be the point where you acknowledge the Installer prompt after executing `root.sh` on all nodes. At this point, CRS is upgraded in rolling fashion and the Installer will be calling ASMCA to upgrade Oracle ASM, which will bounce databases as part of Oracle ASM upgrade.

Bug 8666656

The Oracle Universal Installer (OUI) `runInstaller` script that resides in the Oracle home (`ORACLE_HOME` `/oui/bin/runInstaller`) cannot be used to install the 11.2.0.1 releases of Oracle Database, Oracle Grid Infrastructure for a cluster, and Oracle Database Client.

Workaround: Use Oracle Universal Installer on the respective 11.2.0.1.0 product media to install each product.

Bug 8638708

If you select the database configuration Desktop Class in Oracle Universal Installer (OUI), listener and database control are configured with `'localhost'` as the host name. The Oracle Enterprise Manager Database Control `start` and `stop` operations using `emctl` may fail.

Workaround: For Database Control start and stop operations that use `emctl` in that home, set the `ORACLE_HOSTNAME` environment variable to `'localhost'`.

Bug 8407818

After adding a new node to a shared Oracle database home using `addNode.sh`, the `/etc/oratab` on the newly added node gets an entry of the source database name that exists on the source node from where `addNode.sh` was run. The `/etc/oratab` file on the new node is supposed to get the database entry after the database instance is added for the new node using DBCA.

Workaround: Before invoking DBCA from the source node to add a new database instance for the new node, open the `/etc/oratab` file on the new node using an editor and remove the entry made for the source database name.

### 4.36.16 Vendor and Operating System Known Bugs

Bug 8256753

A connect using `SCAN` and `EZCONNECT` on one client machine can be requested to use a specific `SCAN` listener. Therefore, load balancing by round-robin DNS is not possible.

Workaround: Connect to a database using the following configuration specifying `LOAD_BALANCE=on` in `tnsnames.ora`:

```
ORCL = 
   (DESCRIPTION = 
     (LOAD_BALANCE=on) 
     (ADDRESS = (PROTOCOL = TCP)(HOST = stscan1)(PORT = 1521)) 
     (CONNECT_DATA = 
       (SERVER = DEDICATED) 
       (SERVICE_NAME = srv.world) 
     ) 
   )
```

### 4.36.17 Oracle Wallet Manager Known Bugs

Bug 9880435

Oracle Wallet Manager fails to upload wallet to Directory service when the wallet password and the directory user password are different.

Workaround: Use the same password for the wallet and the directory user.

### 4.36.18 Oracle Warehouse Builder Known Bugs

Refer to "Open Bugs and Known Issues" in [Oracle Warehouse Builder Release Notes](https://docs.oracle.com/cd/E11882_01/relnotes.112/e24470/toc.htm).

Bug 10010873

Oracle Warehouse Builder (OWB) 11.2.0.1 Design Center client is not compatible with OWB 11.2.0.2 server-side components. Using OWB 11.2.0.1 Design Center to connect to an 11.2.0.2 OWB repository can cause unpredictable behavior, possibly including repository corruption.

Workaround: To avoid these conflicts, configure OWB 11.2.0.1 to check the version of the target repository at connection time.

Edit `OWB_CLIENT_HOME/owb/bin/admin/Preference.properties` on each client installation, and update the `OverrideRuntimeVersionCheck` and `OverrideRepositoryVersionCheck` preferences as follows:

```
OverrideRuntimeVersionCheck=false
OverrideRepositoryVersionCheck=false
```

This change to `Preference.properties` should be applied to the 11.2.0.1 Design Center installation on every client host.

To use OWB Design Center with 11.2.0.2 databases, use the OWB 11.2.0.2 Linux 32-bit Design Center until the OWB 11.2.0.2 Windows 32-bit Design Center is available.

If you cannot use OWB 11.2.0.2 Linux 32-bit Design Center client in your environment, contact Oracle Support Services for further assistance.

### 4.36.19 Oracle XML Database Known Bugs

Bug 10018899

Because operator arguments are not checked for tracking changes to database objects, an existing result cache cannot be invalidated when one of those objects is updated.

The `xmlexists` operator is affected by this problem as well as any operator that accepts a database object as an argument.

Workaround: Disable or flush the result cache for queries that involve such operators.

Bug 9586264

In order to fully optimize some `XMLQUERY` or `XMLTABLE` queries, `OPTIMIZER_FEATURE_ENABLE` should be set to 11.1.0.6 or above.

Workaround: None.