---
title: Readme Information for Oracle Database 11g Release 2 (11.2.0.3)
book: Readme
doc_id: E41331-17
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/readmes.112/e41331/chapter11203.htm
tags:
  - oracle
  - 11g
  - readme
---

## 3 Readme Information for Oracle Database 11g Release 2 (11.2.0.3)

Note:

If you are on Oracle Database 11g release 2 (11.2.0.3), this is the Readme section that you need to read.

This section of the Readme contains the following sub-sections:

Section 3.1, "Compatibility, Upgrading, Downgrading, and Installation"

Section 3.2, "Features Not Available or Restricted in 11.2.0.3"

Section 3.3, "Default Behavior Changes"

Section 3.4, "Database Security"

Section 3.5, "Oracle Automatic Storage Management (Oracle ASM)"

Section 3.6, "Java and Web Services"

Section 3.7, "Media Management Software"

Section 3.8, "Oracle Application Express"

Section 3.9, "Oracle Data Mining"

Section 3.10, "Oracle Database Vault"

Section 3.11, "Oracle Grid Infrastructure for a Cluster"

Section 3.12, "Oracle Multimedia"

Section 3.13, "Oracle Net Listener"

Section 3.14, "Oracle ODBC Driver"

Section 3.15, "Oracle Real Application Clusters"

Section 3.16, "Oracle Spatial"

Section 3.17, "Oracle SQL Developer"

Section 3.18, "Oracle Text"

Section 3.19, "Oracle Warehouse Builder"

Section 3.20, "Oracle XML DB"

Section 3.21, "Pro\*C"

Section 3.22, "Pro\*COBOL"

Section 3.23, "SQL\*Plus"

Section 3.24, "Open Bugs"

## 3.1 Compatibility, Upgrading, Downgrading, and Installation

For late-breaking updates and best practices about preupgrade, post-upgrade, compatibility, and interoperability discussions, see Note 785351.1 on My Oracle Support (at `https://support.oracle.com`) that links to the "Upgrade Companion" web site for Oracle Database 11g release 2 (11.2).

Caution:

After installation is complete, do not manually remove or run `cron` jobs that remove `/tmp/.oracle` or `/var/tmp/.oracle` directories or their files while Oracle software is running. If you remove these files, then Oracle software can encounter intermittent hangs. Oracle Grid Infrastructure for a cluster and Oracle Restart installations fail with the following error:
```
CRS-0184: Cannot communicate with the CRS daemon.
```

### 3.1.1 Downgrading Release 11.2.0.3 to 11.2.0.2 Results in an Error When You Run catdwgrd.sql

When downgrading from release 11.2.0.3 to 11.2.0.2, the following error is raised when you run `@catdwgrd.sql` (reference Bug 11811073):

```
ORA-20000: Upgrade from version 11.2.0.2.0 cannot be downgraded to version
```

Apply patch 11811073 for release 11.2.0.2 which provides an updated version of `catrelod.sql`. Applying this patch must be done prior to executing `@catdwgrd.sql` in the 11.2.0.2 environment.

### 3.1.2 Downgrade to Release 11.1.0.6

If you anticipate downgrading back to release 11.1.0.6, then apply the patch for Bug 7634119. This action avoids the following `DBMS_XS_DATA_SECURITY_EVENTS` error:

```
PLS-00306: wrong number or types of arguments in call
to 'INVALIDATE_DSD_CACHE' DBMS_XS_DATA_SECURITY_EVENTS
PL/SQL: Statement ignored
```

Apply this patch prior to running `catrelod.sql`.

### 3.1.3 Invalid Objects Seen After Downgrading from 11.2.0.3 to 11.2 or 10.2

After downgrading from 11.2.0.3 to 11.1 or 10.2, the following invalid object may be seen:

```
CTX_FILTER_CACHE_STATISTICS (synonym)
CTX_FILTER_CACHE_STATISTICS (view)
```

In the higher release of Oracle, after running `@catdwgrd.sql` and before running `@catrelod.sql`, issue the following two commands:

```
SQL> drop public synonym ctx_filter_cache_statistics;
SQL> drop view ctx_filter_cache_statistics;
```

### 3.1.4 Performing -force Upgrade Results in an Incorrect Grid Home Node List in Inventory

When a node crash occurs during an upgrade, a `-force` upgrade can be performed to upgrade a partial cluster minus the unavailable node (reference Bug 12933798).

After performing a `-force` upgrade, the node list of the Grid home in inventory is not in sync with the actual Oracle Grid Infrastructure deployment. The node list still contains the unavailable node. Because the node list in inventory is incorrect, the next upgrade or node addition, and any other Oracle Grid Infrastructure deployment, fails.

After performing a `-force` upgrade, manually invoke the following command as a CRS user:

```
$GRID_HOME/oui/bin/runInstaller -updateNodeList "CLUSTER_NODES={comma_separated_alive_node_list}" ORACLE_HOME=$GRID_HOME CRS=true
```

### 3.1.5 Tablespace and Fast Recovery Area Sizing

Note:

Fast Recovery was previously known as Flash Recovery.

The Oracle Database 11g Pre-Upgrade Information Utility (`utlu112i.sql`) estimates the additional space that is required in the `SYSTEM` tablespace and in any tablespaces associated with the components that are in the database (for example, `SYSAUX`, `DRSYS`) (reference Bug 13067061). For a manual upgrade, be sure to run this utility on your existing database prior to upgrading.

The tablespace size estimates may be too small, especially if Oracle XML DB is installed in your database. However, to avoid potential space problems during either a manual upgrade or an upgrade using the Database Upgrade Assistant (DBUA), you can set one data file for each tablespace to `AUTOEXTEND ON MAXSIZE UNLIMITED` for the duration of the upgrade.

If you are using file systems for data file storage, then be sure there is adequate space in the file systems for tablespace growth during the upgrade.

If you are using a Fast Recovery Area, then check that the size available is sufficient for the redo generated during the upgrade. If the size is inadequate, then an `ORA-19815` error will be written to the alert log, and the upgrade will stop until additional space is made available.

### 3.1.6 Downgrading a Database Having Database Control Configured

Consider the following when downgrading the database while having Database Control configured (reference Bug 9922349):

1. If you are upgrading from 11.2.0.1 to 11.2.0.3 and then plan to downgrade to 11.2.0.1, you need to apply the following patches in order to downgrade Database Control as part of the database downgrade:
	- 11.2.0.1 PSU2 bundle
		- One-off patch for Bug 8795792
	Without these patches, the `emdwgrd` utility would fail with `IMPORT` (`impdp`) errors when restoring Database Control data.
2. When running `emdwgrd` on 11.2.0.1 Oracle RAC databases, you may need to pass an additional parameter, `-serviceAlias`, if you do not have system identifier (SID) aliases defined in `tnsnames.ora`. This is also needed for single instance if SID and database names are different. For example:
	```
	emdwgrd -save [-cluster] -sid SID [-serviceAlias tns_alias] -path save_directory 
	emdwgrd -restore -tempTablespace TEMP [-cluster] -sid SID [-serviceAlias tns_alias] -path save_directory
	```
3. In the case of in-place downgrade from 11.2.0.3 to 11.2.0.1 using the same Oracle home, you do not need to run `emca -restore` before running `emdwngrd -restore`.

### 3.1.7 DBUA Fails When Upgrading a Single Node Oracle RAC Database

When upgrading a single node Oracle RAC database with the `AUDIT_FILE_DEST` initialization parameter set to a location under `ORACLE_HOME`, DBUA returns an error message similar to `Cannot create dump dir` (reference Bug 12957138). If you see this error, take the following steps:

1. Exit DBUA.
2. Change the `AUDIT_FILE_DEST` initialization parameter file to point to `ORACLE_BASE/admin/adump`.
3. Restart the database.
4. Retry the upgrade using DBUA.

### 3.1.8 Deinstallation Restrictions

The following sections describe deinstallation and deconfiguration restrictions. See Section 3.24.3, "Deinstallation Tool Known Bugs" for additional information.

#### 3.1.8.1 Deinstall Upgraded 11.2 Oracle RAC and Oracle Grid Infrastructure for a Cluster Homes

After you deconfigure and deinstall an upgraded Oracle Database 11g release 2 (11.2) Oracle RAC home and to deconfigure and deinstall an 11.2 Oracle Grid Infrastructure for a cluster home, you must detach any pre-11.2 Oracle RAC software homes from the central Inventory (reference Bug 8666509).

Detach the pre-11.2 Oracle RAC homes from the central inventory with the following command:

```
ORACLE_HOME/oui/bin/runInstaller -detachHome ORACLE_HOME_NAME=pre-11.2_ORACLE_HOME_NAME ORACLE_HOME=pre-11.2_ORACLE_HOME
```

### 3.1.9 Multiple Interconnects and Oracle ACFS

If you have Oracle ACFS file systems on Oracle Grid Infrastructure for a cluster 11g release 2 (11.2.0.1), you upgrade Oracle Grid Infrastructure to 11g release 2 (11.2.0.2) or 11g release 2 (11.2.0.3), and you take advantage of Redundant Interconnect Usage and add one or more additional private interfaces to the private network, then you must restart the Oracle ASM instance on each upgraded cluster member node (reference Bug 9969133).

### 3.1.10 Oracle ASM Rolling Upgrade

Oracle Automatic Storage Management (Oracle ASM) rolling upgrade check does not allow rolling upgrade to be done from 11.1.0.6 to any later release (reference Bug 6872001). The following message is reported in the alert log:

```
Rolling upgrade from 11.1.0.6 (instance instance-number) to 11.x.x.x is not supported
```

`ORA-15156` is signalled by LMON which will then terminate the instance.

When trying to upgrade Oracle ASM from 11.1.0.6 to a later release of Oracle ASM, apply the patch for this bug to 11.1.0.6 instances before rolling upgrade starts. This patch can be applied to 11.1.0.6 instances in a rolling fashion.

### 3.1.11 The ora.acfs.registry Resource May Be in an Inconsistent State After an Upgrade to 11.2.0.3.0 from a Previous Release

`TARGET` and `STATE` for `ora.registry.acfs` will be set to either `ONLINE` if the Oracle Automatic Storage Management Cluster File System (Oracle ACFS) registry resource existed in the previous release, or set to `OFFLINE` if the Oracle ACFS registry resource did not exist in the previous release (reference Bug 12812838 and Bug 9878976).

To disable Oracle ACFS, enter the command `acfsroot disable` which will set `ora.registry` to `STATE OFFLINE`, `TARGET OFFLINE` after a CRS stack restart.

### 3.1.12 Oracle ACFS Registry May Be in an Inconsistent State After Installing or Upgrading to 11.2.0.3.0 or After An Oracle Clusterware Restart

If Oracle ASM is not used as the voting disk and quorum disk, the Oracle Automatic Storage Management Cluster File System (Oracle ACFS) registry resource will report OFFLINE after an install (reference Bug 9876173 and Bug 9864447). This occurs because the Oracle ACFS registry requires that Oracle ASM be used in order to provide Oracle ASM Dynamic Volume Manager (Oracle ADVM) volumes.

### 3.1.13 Upgrading a Database With Oracle Data Mining (ODM)

If you upgrade a database with the Data Mining option from 11.2.0.1 to 11.2.0.3, make sure that the `DMSYS` schema does not exist in your 11.2.0.1 database. If it does, you should drop the `DMSYS` schema and its associated objects from the database as follows:

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

### 3.1.14 Oracle ACFS File Systems Must be Manually Dismounted Prior to Upgrade, Deinstallation, or Direct Shutdown of Oracle Clusterware or Oracle ASM

Oracle ACFS file systems must be unmounted, on any given node, prior to upgrade, deinstallation, or direct shutdown of Oracle Clusterware or Oracle ASM on that node (reference Bug 8594128 and Bug 12726434). Use `srvctl stop filesystem` and `umount` on UNIX or `srvctl stop filesystem` and `acfsdismount` on Windows.

When upgrading, all Oracle ACFS file systems must be stopped before beginning the upgrade. For UNIX, this can happen on a node-by-node basis before beginning the upgrade on each node. For Windows, Oracle ACFS file systems must be unmounted across the cluster due to the unattended nature of the rolling upgrade on Windows.

Use the `lsof` and `fuser` commands (Linux and UNIX) or the `handle` and `wmic` commands (Windows) to identify processes which are active on the Oracle ACFS file systems. To ensure that these processes are no longer active, dismount all Oracle ACFS file systems and issue Oracle Clusterware shutdown. Otherwise errors may be issued during Oracle Clusterware shutdown relating to activity on Oracle ACFS file systems which will stop the successful shutdown of Oracle Clusterware.

### 3.1.15 catrelod.sql Fails if the Time Zone File Version Used by the Database Does Not Exist in Oracle Home

The following error is returned when `catrelod.sql` is run as part of the downgrade process if you previously installed a recent version of the time zone file and used the `DBMS_DST` PL/SQL package to upgrade `TIMESTAMP WITH TIME ZONE` data to that version (reference Bug 9803834):

```
ORA-00600: internal error code, arguments: [qcisSetPlsqlCtx:tzi init], 
 [], [], [], [], [], [], [], [], [], [], []
```

See Step 2 of 'Downgrade the Database' in Chapter 6 of the [Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/downgrade.htm#UPGRD12556) for more details.

If you previously installed a recent version of the time zone file and used the `DBMS_DST` PL/SQL package to upgrade `TIMESTAMP WITH TIME ZONE` data to that version, then you must install the same version of the time zone file in the release to which you are downgrading. For example, the latest time zone files that are supplied with Oracle Database 11g release 2 (11.2) are version 14. If, after the database upgrade, you had used `DBMS_DST` to upgrade the `TIMESTAMP WITH TIME ZONE` data to version 14, then install the version 14 time zone file in the release to which you are downgrading. This ensures that your `TIMESTAMP WITH TIME ZONE` data is not logically corrupted during retrieval. To find which version your database is using, query `V$TIMEZONE_FILE`.

Also see the [Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/toc.htm) for more information on installing time zone files.

### 3.1.16 Data Pump Export Operations Do Not Work if the DMSYS Schema is Not Removed as Part of the Upgrade to 11.2.0.3

Data Pump Export operations do not work if the `DMSYS` schema is not removed as part of the upgrade to release 11.2.0.3 (reference Bug 10007411). The reported error is similar to the following:

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

The pre-upgrade checks for 11.2.0.3 report the action that should be taken before the upgrade:

```
The DMSYS schema exists in the database. Prior to performing an upgrade Oracle recommends that the DMSYS schema, and its associated objects be removed from the database. Refer to the Oracle Data Mining Administration Guide for the instructions on how to perform this task.
```

Until this step is taken, Data Pump Export will not work.

### 3.1.17 Upgrading With Objects in the Recycle Bin

The recycle bin must be empty during an upgrade to avoid possible `ORA-00600` deadlock errors, as well as to minimize the time required to perform the upgrade (reference Bug 8632581).

To avoid this deadlock, use the `PURGE DBA_RECYCLEBIN` statement to remove items and their associated objects from the recycle bin and release their storage space prior to upgrading your database.

### 3.1.18 INVALID Materialized View

A materialized view has a status of `INVALID` after both `@catupgrd.sql` and `@utlrp.sql` have been run (reference Bug 12530178). You can see this using the following command:

```
SELECT object_name, object_id, owner FROM all_objects WHERE 
object_type='MATERIALIZED VIEW' and status='INVALID'; 

OBJECT_NAME                     OBJECT_ID   OWNER 
------------------------------ ----------- ------- 

FWEEK_PSCAT_SALES_MV                51062   SH
```

If, after running both `@catupgrd.sql` to upgrade the database and `@utlrp.sql` to recompile invalid objects, there still exists an invalid materialized view, then issue the following SQL statement:

```
ALTER MATERIALIZED VIEW sh.FWEEK_PSCAT_SALES_MV COMPILE;
```

### 3.1.19 rootupgrade.sh Script Might Fail

During an upgrade from release 11.2.0.2 to 11.2.0.3, if the `rootupgrade.sh` script exits while the CRS stack is shutting down, re-running the `rootupgrade.sh` script might fail (reference Bug 12721330).

Manually start the old CRS stack and then re-run the `rootupgrade.sh` script.

### 3.1.20 ora.ons Status May Show UNKNOWN

After upgrading from release 11.2.0.2 to 11.2.0.3, you may see `ora.ons` status showing `UNKNOWN` with the explanation being `CHECK TIMED OUT` (reference Bug 12861771).

The workaround is to kill the Oracle Notification Services (ONS) process and run `srvctl start nodeapps`.

### 3.1.21 PRVF-10037 Error During Installation of Oracle Grid Infrastructure 11.2.0.3 Software

During storage verification when performing an 11.2.0.3 install or upgrade of Grid Infrastructure, the following error message may be displayed:

```
PRVF-10037 : Failed to retrieve storage type for "<devicepath>" on node "<node>"
Could not get the type of storage
```

This issue could be the result of the CVUQDISK package not being installed or an incorrect version of the CVUQDISK package being installed. Please ensure that the correct package (typically `cvuqdisk-1.0.9-1.rpm`) is installed and if it is not, install this version of the package and run the install or upgrade again (reference bug 12881575).

Perform the following procedure to install the CVUQDISK package:

1. Login as the `root` user.
2. Copy the package, `cvuqdisk-1.0.9-1.rpm`, to a local directory. You can find this package in the rpm subdirectory of the top-most directory in the Oracle Grid Infrastructure installation media. For example, you can find `cvuqdisk-1.0.9-1.rpm` in the directory `/` `mountpoint` `/clusterware/rpm/` where `mountpoint` is the mounting point for the disk on which the Oracle Grid Infrastructure installation media is located.
3. Set the environment variable `CVUQDISK_GRP` to the operating system group that should own the CVUQDISK package binaries. It is recommended that you set this group to the installation group. If `CVUQDISK_GRP` is not set, then by default the `oinstall` group is used for the group that owns the CVUQDISK package binaries.
4. Determine whether previous versions of the CVUQDISK package are installed by running the command `rpm -q cvuqdisk`. If you find previous versions of the CVUQDISK package, then remove them by running the following command, where `previous_version` is the identifier of the previous CVUQDISK version:
	```
	rpm -e cvuqdisk previous_version
	```
5. Install the latest CVUQDISK package by running the following command:
	```
	rpm -iv cvuqdisk-1.0.9-1.rpm
	```

## 3.2 Features Not Available or Restricted in 11.2.0.3

The following is a list of components that are not available or are restricted in Oracle Database 11g release 2 (11.2.0.3):

- Starting with Oracle Database 11g release 2 (11.2.0.3), the Data Mining Java API is deprecated. For information about the Data Mining Java API, see Chapter 7 of [Oracle Data Mining Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e12218/java_api.htm#DMPRG009). See Section 3.9.5, "Data Mining Features Not Available or Deprecated with Oracle Database 11g" for information about other deprecated features of Oracle Data Mining.
- Security-Enhanced Linux (SELinux) is not supported on Oracle Automatic Storage Management Cluster File System (Oracle ACFS) file systems (reference Bug 12754448). (SELinux was also not supported on Oracle ACFS in release 11.2.0.1 and release 11.2.0.2.)
- Certain Oracle Text functionality based on third-party technologies, including `AUTO_LEXER` and `CTX_ENTITY`, have been disabled in release 11.2.0.3 (reference Bug 12618046). For `BASIC_LEXER`, the usage of the `INDEX_STEMS` attribute values that depend on third-party technologies, is also affected. If this impacts an existing application, contact Oracle Support Services for guidance.
- Oracle Data Mining now supports a new release of Oracle Data Miner. The earlier release, Oracle Data Miner Classic, is still available for download on OTN, but it is no longer under active development. For information about the new release, Oracle Data Miner 11g release 2 (11.2), go to `http://www.oracle.com/technetwork/database/options/odm/index.html`.
- All Oracle Grid Infrastructure patch set upgrades must be out-of-place upgrades, in which case you install the patch set into a new Oracle Grid home (reference Bug 10210246). In-place patch set upgrades are not supported.
- Oracle Database release 11.2.0.1 or 11.2.0.2 upgrade to Oracle Clusterware release 11.2.0.3 is not supported if the 11.2.0.1 or 11.2.0.2 release of Oracle Grid Infrastructure for a cluster is installed in a non-shared Oracle home and the 11.2.0.3 release of Oracle Grid Infrastructure for a cluster is installed in a shared Oracle home (reference Bug 10074804). The original and upgraded releases of Oracle Clusterware should both be installed in either a shared or non-shared Oracle home.
- Using Internet Protocol Version 6 (IPv6) is not supported with the following:
	- Oracle RAC and Oracle Clusterware
		- Oracle Fail Safe

## 3.3 Default Behavior Changes

This section describes some of the differences in behavior between Oracle Database 11g release 2 (11.2) and previous releases. The majority of the information about upgrading and downgrading is already included in the [Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/toc.htm).

### 3.3.1 Non-Uniform Memory Access Optimizations and Support Disabled in 11.2

With Oracle Database 11g release 2 (11.2), non-uniform memory access support is disabled by default. This restriction applies to all platforms and operating systems (reference Bug 8450932).

Non-uniform memory access optimizations and support in the Oracle Database are only available for specific combinations of Oracle version, operating systems, and platforms. Work with Oracle Support Services and your hardware vendor to enable non-uniform memory access support.

### 3.3.2 FILE\_ACCESS\_ROLE Default Behavior Change

The default behavior of the CTX system parameter `FILE_ACCESS_ROLE` has changed (reference Bug 8360111). Customers with existing Oracle Text indexes that use the file or URL datastore must take action to continue to use the indexes without error. The changes are as follows:

- If `FILE_ACCESS_ROLE` is null (the default), then access is not allowed. By default, users who were previously able to create indexes of this type will not be able to create these indexes after the change.
- `FILE_ACCESS_ROLE` is now checked for index synchronization and document service operations. By default, users will not be able to synchronize indexes of this type or use document service calls such as `ctx_doc.highlight` who were allowed to prior to this change.
- Only SYS will be allowed to modify `FILE_ACCESS_ROLE`. Calling `ctx_adm.set_parameter (FILE_ACESS_ROLE,` `role_name``)` as a user other than SYS will now raise the new error:
	```
	DRG-10764: only SYS can modify FILE_ACCESS_ROLE
	```
- Users can set `FILE_ACCESS_ROLE` to `PUBLIC` to explicitly disable this check (which was the previous default behavior).

### 3.3.3 Use of the Append Hint Runs Out of Memory When Loading Many Partitions

Use of direct-path `INSERT` to load a large number of partitions can exceed memory limits, especially when data compression is specified (reference Bug 6749894). Starting in 11.2, the number of partitions loaded at the same time will be limited, based on the `PGA_AGGREGATE_TARGET` initialization parameter, to preserve memory. Rows that are not stored in the partitions that are currently being loaded are saved in the temporary tablespace. After all rows are loaded for the current set of partitions, other partitions are loaded from rows that are saved in the temporary tablespace.

This behavior helps prevent the direct-path `INSERT` from terminating because of insufficient memory.

## 3.4 Database Security

Note the following changes in Database Security.

### 3.4.1 Configure and Use SSL Certificates to Setup Authentication

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

### 3.4.2 Protection Against Password-Guessing Attacks

Starting in 11.2.0.3, the database authentication protocol has been strenghtened against certain types of password-guessing attacks. In order to force the use of this more secure behavior, both the database client and the database server must be upgraded to release 11.2.0.3 or later and the server's `SQLNET.ORA` configuration file `SQLNET.ALLOWED_LOGON_VERSION` parameter should be set to a value of `12` to force the new protocol behavior.

If the SQLNET.ALLOWED\_LOGON\_VERSION initialization parameter is set to 12 on the server without upgrading all clients to release 11.2.0.3 or later, password authentication will fail with an `ORA-28040: No matching authentication protocol` error because older clients do not support this new protocol behavior.

If the SQLNET.ALLOWED\_LOGON\_VERSION initialization parameter is set to 12 on the server without upgrading the server to release 11.2.0.3, password authentication will fail with an `ORA-28040: No matching authentication protocol` error because older server software does not support this new protocol behavior.

## 3.5 Oracle Automatic Storage Management (Oracle ASM)

The following sections describe information pertinent to Oracle Automatic Storage Management (Oracle ASM).

### 3.5.1 Oracle Database Data Files and Oracle ACFS

Oracle Automatic Storage Management Cluster File System (Oracle ACFS) is the preferred file manager for non-database files. It is optimized for general purpose files. Oracle ACFS does not support any file type that can be directly stored in Oracle ASM. However, starting with Oracle Automatic Storage Management 11g release 2 (11.2.0.3), Oracle ACFS supports, without snapshots, RMAN backups, archive logs, and Data Pump dumpsets.

### 3.5.2 Oracle Homes on Oracle ACFS Supported Starting With Release 11.2

Placing Oracle homes on Oracle ACFS is supported starting with Oracle Database release 11.2 (reference Bug 10144982). Oracle ACFS can result in unexpected and inconsistent behavior if you attempt to place Oracle homes on Oracle ACFS on database versions prior to 11.2.

## 3.6 Java and Web Services

Note the following items when working with Java.

### 3.6.1 Restricted Access to com.sun.imageio.\* Packages

Access is restricted to `com.sun.imageio.*` packages for applications that need to use these routines (reference Bug 12583785). If you need to use this package and you encounter a permission error, the SQL statement needed to grant the permission is displayed. Run the statement.

## 3.7 Media Management Software

For environments that consist of a single server, Oracle offers Oracle Secure Backup Express to back up your Oracle Database and other critical Oracle infrastructure to tape. Oracle Secure Backup is fully integrated with Recovery Manager (RMAN) to provide data protection services. For larger environments, Oracle Secure Backup is available as a separately licensable product to back up many database servers and file systems to tape. Oracle Secure Backup release 10.4 is shipping with this Oracle Database 11g release 2 (11.2.0.3). For more information on Oracle Secure Backup, refer to

`http://www.oracle.com/goto/osb/`

### 3.7.1 Globalization Restrictions Within Oracle Secure Backup

The following globalization restrictions apply to Oracle Secure Backup:

- The Oracle Secure Backup Web Tool and command line interface are available in English only, and are not globalized. All messages and documentation are in English.
- Oracle Secure Backup does not support file names or RMAN backup names that are encoded in character sets that do not support null byte termination, such as Unicode UTF-16. Note that this restriction affects file names, not backup contents. Oracle Secure Backup can back up Oracle databases in any character set.

## 3.8 Oracle Application Express

To learn more about Oracle Application Express, refer to the [Oracle Application Express Release Notes](https://docs.oracle.com/cd/E11882_01/relnotes.112/e11944/toc.htm) and the [Oracle Application Express Installation Guide.](https://docs.oracle.com/cd/E11882_01/install.112/e12196/toc.htm)

## 3.9 Oracle Data Mining

Note the following items when working with Oracle Data Mining.

### 3.9.1 Scoring Capabilities in Oracle Exadata Storage Server Layer

Oracle Data Mining scoring functions in Oracle Database 11g release 2 (11.2) are also available in Oracle Exadata Storage Server Software. Scoring capabilities in the storage layer permit very large data sets to be mined quickly, thus further increasing the competitive advantage already gained from Oracle in-database analytics. For information about Oracle Exadata Storage Server Software, see `http://www.oracle.com/technology/products/bi/db/exadata/index.html`.

### 3.9.2 Installation of Oracle Data Mining

The Data Mining Option, as an embedded feature of the database, is automatically installed with the Oracle Enterprise Edition Database. When installing the database with the Data Mining Option, choose the Data Warehouse configuration type for the most appropriate default initialization parameters.

### 3.9.3 Oracle Data Mining Models

In Oracle Database 11g, Data Mining models are implemented as data dictionary objects in the `SYS` schema. The `DMSYS` schema no longer exists.

Data Mining users must have the `CREATE MINING MODEL` privilege to create mining models in their own schema. Additional privileges are required for other data mining activities, as described in the [Oracle Data Mining Administrator's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e16807/security.htm#DMADM004).

New data dictionary views for Oracle Data Mining were introduced in Oracle Database 11g release 1 (11.1):

- `USER/ALL/DBA_MINING_MODELS`
- `USER/ALL/DBA_MINING_MODEL_ATTRIBUTES`
- `USER/ALL/DBA_MINING_MODEL_SETTINGS`

### 3.9.4 Demo Programs for the Data Mining APIs

Demo programs that illustrate the Data Mining APIs (PL/SQL and Java) are installed with Oracle Database Examples. Instructions are in the [Oracle Data Mining Administrator's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e16807/sampleprogs.htm#DMADM009).

### 3.9.5 Data Mining Features Not Available or Deprecated with Oracle Database 11g

- The Oracle Data Mining Scoring Engine Option, a separately installed database option in Oracle Database 10g, is not available in Oracle Database 11g. However, all functionality of the Data Mining Scoring Engine Option is offered in the Data Mining Option of Oracle Database 11g.
- The Basic Local Alignment Search Tool (BLAST), previously supported by Oracle Data Mining, is not available in Oracle 11g.
- Starting with release 11.2.0.3 of Oracle Database, the Data Mining Java API is deprecated. For information about the Data Mining Java API, see Chapter 7 of [Oracle Data Mining Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/datamine.112/e12218/java_api.htm#DMPRG009).
- Oracle Data Mining now supports a new release of Oracle Data Miner. The earlier release, Oracle Data Miner Classic, is still available for download on Oracle Technology Network (OTN), but it is no longer under active development. For information about the new release, Oracle Data Miner 11g release 2 (11.2), go to `http://www.oracle.com/technetwork/database/options/odm/index.html`.

## 3.10 Oracle Database Vault

Note the following items when working with Oracle Database Vault.

### 3.10.1 New Language for Oracle Database Vault

To add a new language for Oracle Database Vault, connect as a user and specify the `DV_ADMIN` or `DV_OWNER` role. Run the following command:

```
DVSYS.DBMS_MACADM.ADD_NLS_DATA("<language
>");
```

Where `<language>` is one of the following:

  
`ENGLISH`  
`GERMAN`  
`SPANISH`  
`FRENCH`  
`ITALIAN`  
`JAPANESE`  
`KOREAN`  
`BRAZILIAN PORTUGUESE`  
`SIMPLIFIED CHINESE`  
`TRADITIONAL CHINESE`

## 3.11 Oracle Grid Infrastructure for a Cluster

Note the following items when working with Oracle Clusterware and Oracle Automatic Storage Management (Oracle ASM), which are installed with an Oracle Grid Infrastructure for a cluster installation.

### 3.11.1 Oracle ACFS and Oracle Clusterware Stack Shut Down

When attempting to shut down Oracle Clusterware, the Oracle Clusterware stack may report that it did not successfully stop on selected nodes (reference Bug 8651848). If the database home is on Oracle ACFS, then you may receive the following error:

```
CRS-5014: Agent orarootagent.bin timed out starting process acfsmount for action
```

This error can be ignored.

Alternatively, the Oracle Clusterware stack may report that it did not successfully stop on selected nodes due to the inability to shut down the Oracle ACFS resources. If this occurs, take the following steps:

- Ensure that all file system activity to Oracle ACFS mount points is quiesced by shutting down programs or processes and retry the shutdown.
- If the `ora.registry.acfs` resource check function times out, or the resource exhibits a state of `UNKNOWN` or `INTERMEDIATE`, then this may indicate an inability to access the Oracle Cluster Registry (OCR). The most common cause of this is a network failure. The commands `acfsutil registry` and `ocrcheck` may give you a better indicator of the specific error. Clear this error and attempt to stop Oracle Clusterware again.

### 3.11.2 In-Place Patch Set Upgrades Are Not Supported

All Oracle Grid Infrastructure patch set upgrades must be out-of-place upgrades, in which case you install the patch set into a new Oracle Grid home (reference Bug 10210246). In-place patch set upgrades are not supported.

## 3.12 Oracle Multimedia

The name Oracle interMedia was changed to Oracle Multimedia in Oracle Database 11g release 1 (11.1). The feature remains the same, only the name has changed. References to Oracle interMedia were replaced with Oracle Multimedia, however some references to Oracle interMedia or interMedia may still appear in graphical user interfaces, code examples, and related documents in the Oracle Database documentation library for 11g release 2 (11.2).

For additional information, refer to the Oracle Multimedia Readme file located at:

```
ORACLE_HOME/ord/im/admin/README.txt
```

## 3.13 Oracle Net Listener

Note the following items when working with Oracle Net Listener.

### 3.13.1 Deprecation of SNMP Support in Oracle Net Listener

Oracle is deprecating SNMP support in Oracle Net Listener in Oracle Database 11g release 2 (11.2). Oracle recommends not using SNMP in new implementations.

See Also:

Doc ID 1341834.1 at `https://support.oracle.com`

## 3.14 Oracle ODBC Driver

The Oracle ODBC Driver Readme file is located at:

```
ORACLE_HOME/odbc/html/ODBCRelnotesUS.htm
```

## 3.15 Oracle Real Application Clusters

Note the following items when working with Oracle RAC.

### 3.15.1 Using the Same Cluster for Administrator-Managed and Policy-Managed Databases

If you are creating an administrator-managed database on a cluster that already hosts policy-managed databases, then you must carefully select the nodes for the administrator-managed database (reference Bug 10027250). This is because the nodes that you select for an administrator-managed database that are in policy-managed server pools will be moved into the Generic server pool as part of this process. If you select nodes that already run other policy-managed database instances, then DBCA prompts you with a message that lists the instances and services that will be shut down when DBCA creates the administrator-managed database. If you select the `Yes` button on the dialog box when DBCA asks " `Do you want to continue?`," then your policy-managed database instances and services will be shut down as a result of the administrator-managed database creation process.

Note: This is also true if you use the `srvctl add instance` command, which gives a similar error message indicating that the databases would be shut down. If you also use the force option (`-f`) with the `srvctl add instance` command, then this is the same as choosing `Yes` on the DBCA dialog. Doing this shuts down any policy-managed databases that are running on the node before moving the node into the Generic server pool.

### 3.15.2 Moving root Owned Binaries that need setuid to Local Nodes from NFS

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

## 3.16 Oracle Spatial

The Oracle Spatial readme file supplements the information in the following manuals: [Oracle Spatial Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e11830/toc.htm), [Oracle Spatial Topology and Network Data Models Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e11831/toc.htm), and [Oracle Spatial GeoRaster Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e11827/toc.htm). The Oracle Spatial readme file is located at:

```
ORACLE_HOME/md/doc/README.txt
```

## 3.17 Oracle SQL Developer

The Oracle SQL Developer readme file is located at:

```
ORACLE_HOME/sqldeveloper/readme.html
```

## 3.18 Oracle Text

Note the following items when working with Oracle Text. You should also check entries for the [Oracle Text Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/text.112/e24435/toc.htm) in the Documentation Addendum.

### 3.18.1 Change to Supported Features

Certain Oracle Text functionality based on third-party technologies, including `AUTO_LEXER` and `CTX_ENTITY`, have been disabled in release 11.2.0.3 (reference Bug 12618046). For `BASIC_LEXER`, the usage of the `INDEX_STEMS` attribute values that depend on third-party technologies, is also affected. If this impacts an existing application, contact Oracle Support Services for guidance.

### 3.18.2 Oracle Text Supplied Knowledge Bases

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

## 3.19 Oracle Warehouse Builder

For additional information about Oracle Warehouse Builder (OWB) in Oracle Database 11g release 2 (11.2), refer to the [Oracle Warehouse Builder Release Notes.](https://docs.oracle.com/cd/E11882_01/relnotes.112/e24470/toc.htm)

## 3.20 Oracle XML DB

The following features are not supported with Oracle XML DB:

- Flashback Archive
- Editioning Views
- SecureFiles LOB Encryption
- Oracle Label Security (OLS) with a hybrid structured and unstructured XMLIndex on the same XML document.

### 3.20.1 Change in Semantics of xdb:defaultTable Annotation

There is a change in behavior in the semantics of `xdb:defaultTable` annotation while registering Oracle XML DB schemas in 11.2 as compared to 11.1 (reference Bug 7646934). If you specify `xdb:defaultTable="MY_TAB"` without specifying `xdb:sqlInline="false"`, Oracle XML DB creates the table as requested and implicitly marks it as an out-of-line table. This behavior is different from 11.1 where the `defaultTable` annotation was ignored when the `sqlInline` setting was missing.

### 3.20.2 Additional SSL\_CIPHER\_SUITE Settings for HTTPS Configuration

Starting in release 11.2.0.3, configuring HTTPS with Oracle XML DB requires that you first set up `SSL_CIPHER_SUITES` to include `SSL_DH_anon` (reference Bug 8403366). The parameter can be set to any one of the following values:

```
SSL_DH_anon_WITH_3DES_EDE_CBC_SHA
SSL_DH_anon_WITH_RC4_128_MD5
SSL_DH_anon_WITH_DES_CBC_SHA
```

See the section titled "Configuring Secure Sockets Layer Authentication" in [Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm) 11g release 2 (11.2) for more details.

This has to be followed by the normal HTTPS configuration steps for Oracle XML DB documented in the section titled "Accessing the Repository using Protocols" in the [Oracle XML DB Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e23094/toc.htm) 11g release 2 (11.2).

### 3.20.3 VARRAY Storage Default Change

In Oracle Database 11g release 1 (11.1), the default value for `xdb:storeVarrayAsTable` changed from `FALSE` to `TRUE` for XMLType object-relational storage. This default applied to the default table, but not when creating XMLType object-relational tables and columns after the schema registration (reference Bug 6858659). In Oracle Database 11g release 2 (11.2), all `VARRAY` data elements are created as tables by default. This provides a significant performance increase at query time. In addition, note the following:

- Tables created prior to 11.2 are not affected by this. The upgrade process retains storage parameters. This only affects tables created in 11.2 or later.
- You can retain the pre-11.2 default of `VARRAY` storage as LOBs if you have small `VARRAY` data elements and you read and or write the full `VARRAY` all at once. You have two options to revert to the pre-11.2 behavior:
	- Re-register the schema with `xdb:storeVarrayAsTable=FALSE`. This affects the default and non-default tables.
		- Or, when creating the table (for non default tables), you can use the `STORE ALL VARRAYS AS LOBS` clause to override the default for all `VARRAY` data elements in the XMLType. This clause can only be used during table creation. It will return an error if used in the `table_props` at schema registration time.
- For schemas registered prior to 11.2 (when the default storage for `VARRAY` data elements was `LOB`), you can use `STORE ALL VARRAYS AS TABLES` clause to override the default for all `VARRAY` data elements in the XMLType.

## 3.21 Pro\*C

The Pro\*C readme file is located at:

```
ORACLE_HOME/precomp/doc/proc2/readme.doc
```

## 3.22 Pro\*COBOL

The Pro\*COBOL readme file is located at:

```
ORACLE_HOME/precomp/doc/procob2/readme.doc
```

## 3.23 SQL\*Plus

The SQL\*Plus readme file is located at:

```
ORACLE_HOME/sqlplus/doc/README.htm
```

## 3.24 Open Bugs

This section lists known bugs for release 11.2.0.3. A supplemental list of bugs may be found as part of the release documentation specific for your platform.

### 3.24.1 Oracle Automatic Storage Management (Oracle ASM) Known Bugs

Bug 12930646

Even if Oracle ASM is not configured, it is started after upgrading to Oracle Database release 11.2.0.3.

Workaround: Use the following CRSCTL and SRVCTL commands to stop `ora.registry.acfs` and the Oracle ASM resource after upgrading to 11.2.0.3:

```
crsctl stop res ora.registry.acfs srvctl stop asm
```

Bug 12881572

During an upgrade of Oracle ASM release 10.1.0.5 to Single-Instance High Availability (SIHA) release 11.2.0.3.0, the `rootupgrade.sh` script returns the following error:

```
<ORACLE_HOME>/bin/crsctl query crs activeversion ... failed rc=4 with message: Unexpected parameter: crs
```

Workaround: This error can be ignored.

Bug 12837037

If you try to put the `DIAGNOSTIC_DEST` initialization parameter on Oracle ACFS by modifying the `DIAGNOSTIC_DEST` parameter in DBCA's "All initialization Parameters" page, DBCA creates the database successfully, but does not add the Oracle ACFS resource dependency for the database.

Workaround: After creating the database successfully, manually add the Oracle ACFS dependency using the following command:

```
srvctl modify database -d db_unique_name -j acfs_path_list
```

Bug 12539000

A synchronization problem in the Interprocess Communication (IPC) state of some Oracle processes causes a fatal error during rolling migration. The following error is seen in the alert log:

```
processes are not on active shared page
```

Workaround: None.

Bug 12332603

Oracle Automatic Storage Management (Oracle ASM) loses the rolling migration state if Cluster Ready Services (CRS) shuts down on all nodes. If this occurs, one of the Oracle ASM versions will fail with either the `ORA-15153` or `ORA-15163` error message.

Workaround: Consider the following scenario of 4 nodes (`node1`, `node2`, `node3`, and `node4`) that are at release 11.2.0.2 and being upgraded to release 11.2.0.3:

- `node1` and `node2` are upgraded to 11.2.0.3 and running.
- `node3` and `node 4` are still at 11.2.0.2 and running.
- Now consider that there is an outage where all CRS stacks are down which leaves the cluster in a heterogeneous state (that is, two nodes at 11.2.0.2 and two nodes at 11.2.0.3).

To proceed with the upgrade, run one of the following steps (depending on the node that was started as the first node):

- If `node3` or `node4` was started as the first node (for example, as an 11.2.0.2 node), you need to run the `ALTER SYSTEM START ROLLING MIGRATION TO '11.2.0.3'` command on the Oracle ASM instance on `node3` or `node4` before you can bring up an 11.2.0.3 node.
- If `node1` or `node2` was started as the first node, you need to run the `ALTER SYSTEM START ROLLING MIGRATION TO '11.2.0.2'` command on the Oracle ASM instance on `node1` or `node2` before you can bring up any 11.2.0.2 node.

Continue the upgrade procedure as already documented from this point forward. Note that before executing one of the above steps to bring the Oracle ASM cluster back into rolling migration, you cannot start two nodes of different versions in the cluster. If you do so, one of the Oracle ASM versions will fail with either the `ORA-15153` or `ORA-15163` error message.

Bug 9413827

An 11.2.0.1 Oracle Clusterware rolling upgrade to 11.2.0.3 fails when Oracle Cluster Registry (OCR) is on Oracle ASM.

Workaround: Apply the patch for bug 9413827 on 11.2.0.1 Oracle Grid Infrastructure for a cluster home before performing the upgrade.

Bug 9276692

Cannot permanently stop the Oracle ASM instance.

Workaround: If the Oracle ASM instance is disabled using SRVCTL, you must unregister Oracle ACFS-related resources to avoid restarting the Oracle ASM instance. Do this by executing the following command as root:

```
acfsroot disable
```

### 3.24.2 Oracle ASM Dynamic Volume Manager (Oracle ADVM) Known Bugs

Bug 9683229

Oracle ADVM does not support mounting ext3 file systems over Oracle ADVM with the mount barrier option enabled. The mount barrier option is enabled by default on SLES11.

Workaround: Mount ext3 file system with `-o barrier=1`. For example:

```
mount -o barrier=0 /dev/asm/myvol-131 /mnt
```

### 3.24.3 Deinstallation Tool Known Bugs

Bug 12769015

After upgrading from 11.2.0.1 or 11.2.0.2 to 11.2.0.3, deinstallation of the Oracle home in the previous version may result in the deletion of the old Oracle base that was associated with it. This may also result in the deletion of data files, audit files, etc., that are stored under the old Oracle base.

Workaround: Before deinstalling the Oracle home in the previous version, edit the `orabase_cleanup.lst` file found in the `<Oracle Home>/utl` directory and remove the `oradata` and `admin` entries. Then, deinstall the Oracle home using the 11.2.0.3 deinstallation tool.

Bug 12762927

When using the deinstallation tool to deinstall a shared Oracle RAC home, some of the files or directories may not get deleted.

Workaround: To remove the `ORACLE_HOME`, run the `rm -rf $ORACLE_HOME` command after the deinstallation tool exits.

Bug 9925724

If `Grid_home` is created directly under a root-owned directory, the deinstallation tool cannot remove the top-level home directory. An empty Oracle home directory remains at the end of the deinstallation.

Workaround: Run `rmdir` `ORACLE_HOME` using the root user on all nodes.

Bug 9406768

The 11.2 deinstallation utility is removing all the homes under Oracle base if these homes are not using the same central inventory and the deinstallation utility finds this home is the only one registered in inventory.

Workaround: While installing 11.2 products:

- Oracle does not recommend using multiple central inventories. Avoid this if possible.
- If for some reason a different central inventory is required, use a different Oracle base directory for each central inventory.

Bug 8666509

A deinstallation of Oracle Clusterware should ask you to detach any pre-11.2 Oracle RAC homes from the Oracle inventory.

Workaround: After you deconfigure and deinstall an upgraded 11.2 Oracle RAC home and want to continue with deconfiguration and deinstallation of the Oracle Grid Infrastructure for a cluster home, first detach any pre-11.2 Oracle RAC software homes from the central Inventory.

Bug 8644344

When running the deinstallation tool to deinstall the database, you will be prompted to expand the Oracle home and to select a component. If you select the top level component, `Oracle Database Server`, and do not select the Oracle home, OUI does not show the message to run the deinstall utility and proceeds with the deinstallation of the database.

Workaround: Run the deinstallation tool to deinstall the Oracle home.

Bug 8635356

If you are running the deinstall tool from `ORACLE_HOME` that is installed on shared NFS storage, then you will see errors related to `.nfs` files during `ORACLE_HOME` clean up.

Workaround: To remove the `ORACLE_HOME`, run the `rm -rf` `ORACLE_HOME` command after the deinstall tool exits. Alternatively, you can use the standalone `deinstall.zip` and specify the location of the `ORACLE_HOME`.

### 3.24.4 Oracle ACFS Known Bugs

Bug 13354082

If the following message appears in the Oracle ASM trace logs, the replication standby database may have stopped making progress after recovery from an Oracle ASM instance failure:

`ORA-19505: failed to identify file   "<mount_point>\.ACFS\repl\ready\rlog.node#.cord#"`

Workaround: If the dot-version of the unidentifiable file is present in the replication-ready directory, it can be safely removed using the following command to prompt NFT to resend the file from the primary database which allows replication to progress on the standby database:

```
rm <mount point>\.ACFS\repl\ready\.rlog.node#.cord#
```

Bug 12842804

After executing the following sequence of commands, file system security will be left in an incomplete state:

```
acfsutil sec prepare -m <mount-path> -u
acfsutil snap create -w <snap-name> <mount-path>
acfsutil sec prepare -m <mount-path>
```

Specifically, the problem is executing the `sec prepare` command after `sec prepare -u` and `snap create` commands.

Workaround: Contact Oracle Support Services to help restore the security status of the file system.

Bug 12827493

During execution of the `acfsutil sec save` command, the XML file that is generated has a timestamp formatted in accordance to NLS language settings. For instance, a Japanese environment will have a timestamp in Japanese characters in the format `Dy DD-MON-YYYY HH24:MI:SS`, where `Dy` is the day of the week (for example, `Mon`, `Tue`, `Wed`, and so on) and `MON` is the month of the year (for example, `JAN`, `FEB`, and so on).

The XSD validation fails because unknown characters (apart from English characters) are observed in the XML file. Consequently, the `acfsutil sec load` command fails. The problem is also seen with the automatically generated XML file `secbackup.xml` during `acfsutil sec` commands.

Workaround: Change the date to English in the XML file. Contact Oracle Support Services to fix the `secbackup.xml` file before performing a `acfsutil sec load` command.

Bug 12704678

When upgrading from release 11.2.0.2 to 11.2.0.3, entries in the Oracle ACFS registry do not automatically have the proper dependencies set for the Oracle ACFS registry resource.

Workaround: To ensure that proper dependencies are set, delete each Oracle ACFS registry entry and reenter it using `acfsutil registry`. This can be done while the file systems are mounted.

Bug 12690672

In releases prior to 11.2.0.3, it is possible to put the database home on an Oracle Automatic Storage Management Cluster File System (Oracle ACFS). If the database home is on an Oracle ACFS file system, the database will have a hard start and stop dependency on the corresponding Oracle ACFS file system.

After upgrading Oracle Grid Infrastructure or Oracle RAC to release 11.2.0.3, the dependency between the database and the Oracle ACFS file system, which stored the previous version's database home, is not deleted.

If using a different Oracle ACFS file system than was used to store the previous version's database home, the database fails to start.

Workaround: After a database upgrade, if using a different Oracle ACFS file system for the database home, Oracle recommends that you review the list of Oracle ACFS file systems that you are using for the database, and update the database dependencies on the file systems using the `srvctl modify database -d` `db_unique_name` `-j` `acfs_path_list` command (instead of the `srvctl modify` `filesystem` `-j` `filesystem-list` command).

Bug 10069735

In a cluster with a password-protected key store, when an Oracle ACFS file system using encryption is mounted through the Oracle ACFS mount registry, the administrator is not prompted to enter the key store password. Although the process of mounting the file system succeeds, not all information required for Oracle ACFS encryption to work correctly is made available to the file system. In this case, encryption is not operational on this file system and any encrypted files in the file system are not available for read or write.

Workaround: In a cluster with a password-protected key store, do not use the Oracle ACFS mount registry for mounting any file systems that are using encryption. If some file systems are already mounted through the Oracle ACFS mount registry, unmount them and remove any such file systems from the mount registry to avoid possible unavailability of encrypted data in the future. Then, remount these file systems without using the Oracle ACFS mount registry, providing the correct password when requested.

Bug 8644639

When creating an Oracle ACFS mount point and adding it to the registry, the mount point is not mounted automatically if the following conditions are met:

1. The mount point directory was previously registered with the Oracle ACFS Registry.
2. The mount point directory had been previously mounted.
3. The mount point had then been unmounted and removed from the Oracle ACFS Registry.
4. The `ora.registry.acfs` resource has not been restarted since the mount point was deleted from the registry.

Workaround: Remove the mount point directory from the file `/tmp/``.usm_state_file`.

### 3.24.5 Oracle Clusterware Known Bugs

Bug 14296767

After Oracle Clusterware is upgraded to release 11.2.0.3.3 by running the `rootupgrade.sh` script, the following crashes can be seen:

- Cluster Ready Services Daemon (CRSD) while trying to backup the Oracle Cluster Registry (OCR).
- The OCRCONFIG utility while doing a manual backup (`ocrconfig -manualbackup`).

Workaround: To work around this problem, the following needs to be run as an Oracle Grid Infrastructure installation user after `rootupgrade.sh` completes successfully:

1. Get the value of the `CLUSTER_NAME` parameter from the following file:
	```
	OH/crs/install/crsconfig_params in <cluster_name>
	```
2. Get the value of the `ORA_DBA_GROUP` parameter from the following file:
	```
	OH/crs/install/crsconfig_params in <grid_user_grp>
	```
3. Issue the `mkdir OH/cdata/<cluster_name>` command.
4. Issue the `chgrp <grid_user_group> OH/cdata/<cluster_name>` command.
5. Issue the `chmod 775 OH/cdata/<cluster_name>` command.

Bug 13110641

While installing Oracle RAC software on a cluster configured with Grid Naming Service (GNS), the Prerequisite's page might show a warning status for the GNS Integrity check even when GNS is working fine.

The message appears to be of the following type:

```
PRVF-5217 : An error occurred while trying to look up IP address for 
"<gns-subdomain-extended-name>"
```

Workaround: Run `nslookup` on the fully qualified names that are listed in the error message. If `nslookup` returns an IP address for the name with a non-authoritative answer, then this warning can be ignored. If the name does not resolve to an IP address, then follow the steps mentioned in Action part of the error message.

Bug 13090686

The database service fails to move to other nodes when the public network connectivity is lost on the node.

Workaround: Manually relocate the service (for example, `srvctl relocate service`) to the node which has public network connectivity.

Bug 13031236

While upgrading from 11.2.0.x to 11.2.0.3, the `rootupgrade.sh` execution on the last node fails during Oracle ASM end rolling migration.

Workaround: Take the following steps:

1. Issue `crsctl stat resource ora.asm` and ensure that the `STATE` is `ONLINE`.
2. Rerun the `rootupgrade.sh` script to complete the upgrade.

Bug 12974884

If the Cluster Health Monitor (CHM) repository retention time or size is decreased, CHM will fail to delete the records which may cause replica loggerd to keep restarting and the synchronization between the master loggerd and replica loggerd to fail.

Workaround: After using the `oclumon manage -repos` command to decrease the Cluster Health Monitor repository size, the Cluster Health Monitor repository location must be changed using the `oclumon manage -repos reploc` `<new_location>` command.

Bug 12900070

If you are preparing to upgrade Oracle Clusterware, and you use the Cluster Verification Utility (CVU) command `runcluvfy.sh stage -pre crsinst -upgrade`, then you may encounter the following error:

```
Unable to retrieve nodelist from Oracle Clusterware
```

The cause of this error is that `olsnodes` cannot return a list of nodes when Oracle Clusterware is down.

Workaround: Run the `cluvfy.sh stage crsinst -upgrade` command using the `-n` flag, and provide a comma-delimited list of cluster member nodes. For example:

```
runcluvfy.sh stage -pre crsinst -upgrade -n node1, node2, node3
```

Bug 12769576

In release 11.2.0.3, the default `RETENTION_TIME` size of a Cluster Health Monitor (CHM) repository in number of seconds is 30823 for a 4-node cluster or is (30823\*4) divided by the number of nodes for other clusters. When upgrading from 11.2.0.2 to 11.2.0.3, the `RETENTION_TIME` is 6311 for a 4-node cluster.

Workaround: Oracle recommends changing the `RETENTION_TIME` size from 6311 to 30823 for a 4-node cluster after upgrading from 11.2.0.2 to 11.2.0.3 by using the following `oclumon` command:

```
oclumon manage -repos resize 30823
```

Bug 12710059

When upgrading Oracle Grid Infrastructure to 11.2.0.3 with Oracle Cluster Registry (OCR) and voting disk files on Network File Storage (NFS), if the network card (for example, eth0) that the cluster nodes use to connect to the NFS server goes down, then the `rootupgrade.sh` scriptwill fail to upgrade the Oracle stack.

Workaround: Restore the network interface and make sure that the old Oracle clusterware stack is up and actively running prior to running the `rootupgrade.sh` script.

Bug 12380213

An error exception occurs when installing an 11.2.0.2 database with data files on 11.2.0.3 Oracle Restart.

Workaround: To install release 11.2.0.2 database against 11.2.0.3 Oracle Restart, you need to invoke 11.2.0.2 `runInstaller` with `-ignorePrereq` and then complete the 11.2.0.2 database installation.

Bug 9948549

If the agent terminates while starting a database or Oracle ASM instance, it is possible that the instance startup will not complete.

Workaround: Stop and restart the instance using `srvctl` or `sqlplus`.

Bug 8733944

Due to a problem in Oracle Clusterware starting with release 11.1.0.7, with the patches required for Oracle Exadata support or 11.1.0.7 CRS bundle Patch 1, in some cases the CSS daemon may fail when the clusterware is brought down on another node, either due to a shutdown command or a failure.

The symptom is an `ASSERT` in the CSSD log indicating that a maximum value has been exceeded. For example:

```
Group ID of xxxx exceeds max value for global groups
```

Workaround: Oracle recommends that customers running with the Oracle Exadata support patches or 11.1.0.7 CRS Bundle Patch 1 apply the patch for this bug to avoid this problem.

This problem may also be seen during an upgrade from 11.1.0.7 with patches as indicated above. To eliminate the potential of an 11.1.0.7 node failing during upgrade, the patch for this bug may be applied to the 11.1.0.7 nodes prior to upgrade.

When upgrading, it is recommended that the upgrade be completed on all nodes without restarting any non-upgraded nodes during the upgrade. If an 11.1.0.7 node does fail while performing the upgrade, it should be upgraded as opposed to restarted.

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

### 3.24.6 Oracle Data Pump Known Bugs

Bug 12866600

Database links imported from an 11.2.0.3 database into a version prior to 11.2.0.3 (including 11.2.0.2) will not be usable in the import database. Any attempt to use a database link will cause the following ORA-600 error:

```
ORA-00600 [kzdlk_zt2 err], [18446744073709551601]
```

Workaround: The database links that are imported need to be re-created before they can be used.

### 3.24.7 Oracle Database Enterprise Edition Known Bugs

Bug 13087066

The following error may be returned when a very large double value is passed to a stored procedure that inserts this value into a table and this stored procedure was stored in the database by modada (SQL\*Module compiler for ADA) with the store=y option.

```
ORA-03137: TTC protocol internal error : [3149]
```

Workaround: None.

Bug 9951827

Transportable tablespace import does not handle timestamp with timezone version change.

If a transportable dumpfile produced in release 11.2.0.3 contains tables with timestamp with timezone columns and the version of the timezone table on the target database is different than that from the source database, the import is be prevented from running.

If a dumpfile produced prior to release 11.2.0.3 had a different timezone table version than that of the target, then the import is be prevented from running.

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

### 3.24.8 Oracle Enterprise Manager Grid Control Known Bugs

Bug 12793336

When attempting to upgrade Cluster Ready Services (CRS) or Oracle ASM to release 11.2 using the Oracle ASM Configuration Assistant (ASMCA), the upgrade succeeds, but it may fail to update the new clusterware home for cluster targets in existing agent homes due to permission issues. As a result, Oracle Enterprise Manager Grid Control and Database Control cannot monitor the Oracle ASM and CRS targets.

Workaround: Modify the `OracleHome` property of Oracle ASM and Cluster targets using the Monitoring Configuration link on the ASM and Cluster home pages, respectively.

Bug 12725253

Database upgrade from release 10.2.0.1 to 11.2.0.3 could run into error `ORA-01722 (Invalid number)` when running in locales that do not use the period (.) as the decimal separator.

Workaround: Run the upgrade in a locale that uses the period (.) as the decimal separator. After the upgrade, switch to your preferred locale.

### 3.24.9 Oracle Database QoS Management Known Bugs

Bug 12767103

If a user creates a performance class with two or more services in its classifier(s) and these services are not all specified to run in the same server pool, the metrics graphs for that performance class on the Enterprise Manager Quality of Service (QoS) Management Performance Class details page are incorrect. The Resource Use Time and Resource Wait Time graphs will only display metrics from one server pool. The other graphs will correctly display metrics for all server pools.

Workaround: This bug will not affect the correct management or recommended actions associated with this type of performance class.

Bug 12792222

This bug applies to recommendations for CPU resources managed by Oracle Database QoS Management. If the number of configured CPUs for all instances on a server is less than the number of physical CPUs for that server, then the nonallocated, or "free", CPUs are not detected by Oracle Database QoS Management and no recommendation is made to increase the number of configured CPUs. Only those "slices" that host databases are considered as donors for the target slice. Adding one of the non-allocated CPUs should be the first-ranked Move CPU action.

Workaround: Make sure the sum of CPU counts configured for each database instance on each server is the same as the number of physical CPUs.

Bug 10019209

This bug applies to platforms that support the Cluster Health Monitor (CHM). If an Oracle Clusterware-managed database service is in a stopped but not disabled state, it will be started by Oracle Database QoS Management if the server hosting that service is not detected to be in a memory overcommitted state. If memory is overcommitted, then all enabled services will be stopped even if they were manually started. The desired behavior is to only start services on the transition from a memory overcommitted state (red) to a normal state (green). If a service is manually started when the server is in the red state, that service should not be shut down.

Workaround: Stop and disable services that you want to remain in the stopped state or disable QoS Management from the Oracle Enterprise Manager Console.

### 3.24.10 Oracle Database Vault Known Bugs

Bug 7033772

Database Vault Administrator (DVA) does not work after an Enterprise Manager DBControl upgrade.

Workaround: Manually redeploy DVA after DBControl has been upgraded. You can follow the steps described in Appendix C, Section "Deploying Database Vault Administrator to the Database Console OC4J Container" of the [Oracle Database Vault Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23090/dvca.htm#DVADM71067).

Bug 8686258

Database Vault policy cannot be managed in Oracle Enterprise Manager Database Control because the following message is displayed in Database Vault Administration page:

```
"OPERATOR TARGET" privilege does not exist.
"You must have OPERATOR TARGET privilege to perform this operation."
```

Workaround: To manage Database Vault policy using Oracle Enterprise Manager, the Database Vault administrator must have the EM Administrator privilege. If you do not want to grant the EM Administrator privilege to the Database Vault administrator, then use the Database Vault Administrator page directly. For additional information, see [Oracle Database Vault Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23090/dba.htm#DVADM70290).

Bug 8341283

The `ACTION_NAME` entry in the `DVSYS.AUDIT_TRAIL$` table displays `Realm Authorization Audit` for a failed realm enforcement if the audit option is set to audit on success and failure. The `RETURNCODE` will show the correct error code that was triggered.

Workaround: Use the `RETURNCODE` value to determine whether a violation has occurred and the `ACTION_NAME` column to identify whether the audit was generated by a realm enforcement or command rule enforcement.

### 3.24.11 Oracle Enterprise Manager Database Control Known Bugs

Bug 9766628

`emctl` commands did not return valid results as expected.

Workaround: The `emctl` command needs to be run from an Oracle Database home. Do not invoke this command from the Oracle Grid Infrastructure for a cluster home.

Bug 8674920

If the installation owners for the Oracle Grid Infrastructure for a cluster and Oracle Database are different, then the owners of Oracle ASM binaries and Oracle Enterprise Manager Agent binaries are also different. When you start Support Workbench, the error message `Error Operation failed - Operation failed` might appear, because the Oracle Enterprise Manager Agent is running as a different user, and Support Workbench does not have permissions for the Oracle ASM target.

Workaround: None.

Bug 8350597

If Database Control is running in an IPv6 environment, then you cannot use it to monitor Exadata cells and you should not add Exadata cells as targets.

Workaround: None.

### 3.24.12 Oracle OLAP Known Bugs

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

### 3.24.13 Oracle Real Application Clusters Known Bugs

Bug 10369108

After converting from an administrator-managed database to a policy-managed database, you may need to update the database password file.

Workaround: To update the database password file, run the following steps:

1. Copy the existing password file `orapw$ORACLE_SID` to `orapw<db_unique_name>` on the node where the administrator-managed database was running.
2. Copy this file, `orapw<db_unique_name>`, to the same location on every cluster node.

### 3.24.14 Oracle SQL\*Loader Known Bugs

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

### 3.24.15 Oracle Universal Installer Known Bugs

You should also review Section 3.1, "Compatibility, Upgrading, Downgrading, and Installation" for other issues related to installation and upgrades.

Bug 13362360

Secure Shell (SSH) setup is not yet certified for Protocol 2 only mode.

Workaround: Ensure that the SSH configuration file is configured to process both Protocol 2 and Protocol 1.

Bug 13028836

Secure Shell (SSH) setup code is changing the user's home directory permission to 755 only on the current or local node.

Workaround: This is expected behavior because SSH requires this permission to do some SSH-related operations on the local node.

Bug 13012502

Cloning of an Oracle home that was added with Oracle Database Client or Oracle Database Examples software results in a database creation failure.

Workaround: During the clone operation, supply the values for the privileged operating system groups (`OSDBA_GROUP` and `OSOPER_GROUP`) as specified in the [Oracle Database Installation Guide for Linux](https://docs.oracle.com/cd/E11882_01/install.112/e47689/toc.htm).

Bug 12930328

If the central inventory location is different on different nodes of a cluster, `addnode.sh` does not update the inventory correctly on remote nodes of the cluster.

Workaround: Adding nodes to a cluster requires the central inventory location to be the same on all the nodes of the cluster. Please ensure that this is the case prior to running `addnode.sh`.

Bug 12887720

A file system supporting Access Control Lists (ACL) should not be used for staging Oracle software as this may cause an error when copying the files from the staging area to a temporary directory which does not support Access Control Lists. ACL permissions cannot be preserved while copying the files and this causes the copy to fail.

Workaround: None.

Bug 12719356

After installing Oracle RAC, you might see the following error message in the installation log files:

```
OiiolLogger.addFileHandler:Error while adding file handler - Logs/remoteInterfaces<time>.log
```

Workaround: None. This error message can be ignored.

Bug 12711224

If Oracle Universal Installer (OUI) crashes during a node reboot or crashes while you are executing the rootupgrade script, OUI cannot resume post-upgrade tasks.

Workaround: You have to manually take care of the following tasks and complete the upgrade:

- If you are upgrading from a pre-11.2 to 11.2.0.3 release:
	1. Update inventory
		2. Orace Net Configuration Assistant
		3. Automatic Storage Management Configuration Assitant
		4. Enterprise Manager Configuration Upgrade Utility
		5. Oracle Cluster Verification Utility
- If you are upgrading from a post-11.2 to 11.2.0.3 release:
	1. Update inventory
		2. Enterprise Manager Configuration Upgrade Utility
		3. Oracle Cluster Verification Utility

Bug 12635143

The following issues exist because of a default path mismatch in the properties file:

- The Secure Shell (SSH) setup process returns a success message even if it is not able to copy the required authentication files to the remote boxes. This happens only when some binaries (for example, SCP and SSH) used for the SSH setup process are not present in the specified default location (for example, in platform specific files such as `ssPaths_sol.properties`).
- Some of the default locations mentioned for binaries in platform-specific properties files are not correct.

Workaround: Take the following steps to correct either of the issues previously mentioned:

1. Copy the properties files in the installation shiphome path `/Disk1/stage/properties` to a location on the server.
2. Depending on the source of the path error, open the file `ssPaths_<` `platform` `>.properties` and modify the values in the file to point to the correct path location on your server.
3. Call the following where `<unzipped_resource_directory_path>` is the path of the local location of the properties file (not including the filename):
	```
	./runInstaller -J-Doracle.sysman.prov.PathsPropertiesLoc=<unzipped_resource_directory_path>
	```

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

### 3.24.16 Oracle Wallet Manager Known Bugs

Bug 9880435

Oracle Wallet Manager fails to upload wallet to Directory service when the wallet password and the directory user password are different.

Workaround: Use the same password for the wallet and the directory user.

### 3.24.17 Oracle XML Database Known Bugs

Bug 16069266

Using Transportable Tablespaces (TTS) to export or import tables with Binary XML data is not supported.

Workaround: Use the Oracle Data Pump conventional path to move data.

Bug 12836913

When using `oracle.xdb.XMLType` proprietary constructors in a Java stored procedure with JDK6, the error `Invalid version of the XMLType` could be returned.

Workaround: Either do not use Java stored procedures. Or, use JDK5 instead of JDK6.

Bug 12834970

Starting with release 11.2.0.3, the `MOVEXDB_TABLESPACE` and `REBUILDHIERARCHICALINDEX` procedures were moved from the `DBMS_XDB` package to the `DBMS_XDB_ADMIN` package. These procedures are no longer available in the `DBMS_XDB` package anymore.

Workaround: None.

Bug 9586264

In order to fully optimize some `XMLQUERY` or `XMLTABLE` queries, `OPTIMIZER_FEATURE_ENABLE` should be set to 11.1.0.6 or above.

Workaround: None.

### 3.24.18 Vendor and Operating System Known Bugs

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