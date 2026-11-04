---
title: Readme Information for Oracle Database 11g Release 2 (11.2.0.4)
book: Readme
doc_id: E41331-17
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/readmes.112/e41331/chapter11204.htm
tags:
  - oracle
  - 11g
  - readme
---

## 2 Readme Information for Oracle Database 11g Release 2 (11.2.0.4)

Note:

If you are on Oracle Database 11g release 2 (11.2.0.4), then this is the Readme section that you need to read.

This section of the Readme contains the following sub-sections:

Section 2.1, "Compatibility, Upgrading, Downgrading, and Installation"

Section 2.2, "Features Not Available or Restricted in 11.2.0.4"

Section 2.3, "Deprecated and Desupported Features for Oracle Database"

Section 2.4, "Default Behavior Changes"

Section 2.5, "Database Security"

Section 2.6, "Java and Web Services"

Section 2.7, "Media Management Software"

Section 2.8, "Oracle Application Express"

Section 2.9, "Oracle Automatic Storage Management (Oracle ASM)"

Section 2.10, "Oracle Grid Infrastructure for a Cluster"

Section 2.11, "Oracle Multimedia"

Section 2.12, "Oracle ODBC Driver"

Section 2.13, "Oracle Real Application Clusters"

Section 2.14, "Oracle Spatial"

Section 2.15, "Oracle SQL Developer"

Section 2.16, "Oracle Text"

Section 2.17, "Oracle XML DB"

Section 2.18, "Oracle Warehouse Builder"

Section 2.19, "Pro\*C"

Section 2.20, "Pro\*COBOL"

Section 2.21, "SQL\*Plus"

Section 2.22, "Open Bugs"

## 2.1 Compatibility, Upgrading, Downgrading, and Installation

For late-breaking updates and best practices about preupgrade, post-upgrade, compatibility, and interoperability discussions, see Note 785351.1 on My Oracle Support (at `https://support.oracle.com`) that links to the "Upgrade Companion" web site for Oracle Database 11g release 2 (11.2).

Caution:

After installation is complete, do not manually remove or run `cron` jobs that remove `/tmp/.oracle` or `/var/tmp/.oracle` directories or their files while Oracle software is running. If you remove these files, then Oracle software can encounter intermittent hangs. Oracle Grid Infrastructure for a cluster and Oracle Restart installations fail with the following error:
```
CRS-0184: Cannot communicate with the CRS daemon.
```

### 2.1.1 Upgrading to Release 11.2.0.4 Generates Suboptimal Plans for CHAR or NCHAR Data Type Columns

After upgrading to Oracle Database 11g release 2 (11.2.0.4), the optimizer generates suboptimal plans for `CHAR` or `NCHAR` data type columns that have histogram statistics and when the `OPTIMIZER_FEATURES_ENABLE` parameter is set to a value of `11.2.0.4` (which is the default value in Oracle Database 11g release 2 (11.2.0.4)).

One workaround for this issue is to apply the patch for bug 18255105. For `CHAR` or `NCHAR` data type columns that have histogram statistics, this patch marks them as stale. This patch also helps if you are using automatic statistics gathering or if you are using manual statistics gathering (with either the `GATHER AUTO` or `GATHER STALE` option) to gather statistics on the problematic tables.

Another workaround is to find the tables that have `CHAR` or `NCHAR` data type columns that have histogram statistics (using the `DBA_TAB_COL_STATISTICS` view) and execute the `GATHER_TABLE_STATS` procedure on them. Instead of using the `GATHER_TABLE_STATS` procedure on the production system, gather statistics on a test system, export the statistics to a user statistics table, and then import the statistics into the production system. This workaround eliminates the need for the patch for bug 18255105.

When you collect statistics, set the `NO_INVALIDATE` parameter to `FALSE` so that the existing cursors (with suboptimal plans) are not shared when SQL statements are executed again.

Gathering statistics for tables that have all of the following scenarios can also cause suboptimal plans:

- The tables have `CHAR` or `NCHAR` data type columns.
- The `OPTIMIZER_FEATURES_ENABLE` parameter is set to a value of `11.2.0.4`.
- The tables have histograms.
- Later, you change the `OPTIMIZER_FEATURES_ENABLE` parameter value to less than `11.2.0.4` (for example, you downgraded Oracle Database and set the `OPTIMIZER_FEATURES_ENABLE` parameter to a smaller value).

In this scenario, you need to regather the statistics for those tables after changing the `OPTIMIZER_FEATURES_ENABLE` parameter.

### 2.1.2 Downgrading Release 11.2.0.4 to 11.2.0.2 Results in an Error When You Run catdwgrd.sql

When downgrading from release 11.2.0.4 to 11.2.0.2, the following error is raised when you run `@catdwgrd.sql` (reference Bug 11811073):

```
ORA-20000: Upgrade from version 11.2.0.2.0 cannot be downgraded to version
```

Apply patch 11811073 for release 11.2.0.2 which provides an updated version of `catrelod.sql`. Applying this patch must be done prior to executing `@catdwgrd.sql` in the 11.2.0.2 environment.

### 2.1.3 Downgrading a Database Having Database Control Configured

Consider the following when downgrading the database while having Database Control configured (reference Bug 9922349):

1. If you are upgrading from 11.2.0.1 to 11.2.0.4 and then plan to downgrade to 11.2.0.1, you need to apply the 11.2.0.1 PSU2 bundle patch in order to downgrade Database Control as part of the database downgrade.
	Without this patch, the `emdwgrd` utility would fail with `IMPORT` (`impdp`) errors when restoring Database Control data.
2. When running `emdwgrd` on 11.2.0.1 Oracle RAC databases, you may need to pass an additional parameter, `-serviceAlias`, if you do not have system identifier (SID) aliases defined in `tnsnames.ora`. This is also needed for single instance if SID and database names are different. For example:
	```
	emdwgrd -save [-cluster] -sid SID [-serviceAlias tns_alias] -path save_directory 
	emdwgrd -restore -tempTablespace TEMP [-cluster] -sid SID [-serviceAlias tns_alias] -path save_directory
	```
3. In the case of in-place downgrade from 11.2.0.4 to 11.2.0.1 using the same Oracle home, you do not need to run `emca -restore` before running `emdwngrd -restore`.

### 2.1.4 Performing -force Upgrade Results in an Incorrect Grid Home Node List in Inventory

When a node crash occurs during an upgrade, a `-force` upgrade can be performed to upgrade a partial cluster minus the unavailable node (reference Bug 12933798).

After performing a `-force` upgrade, the node list of the Grid home in inventory is not in sync with the actual Oracle Grid Infrastructure deployment. The node list still contains the unavailable node. Because the node list in inventory is incorrect, the next upgrade or node addition, and any other Oracle Grid Infrastructure deployment, fails.

After performing a `-force` upgrade, manually invoke the following command as a CRS user:

```
$GRID_HOME/oui/bin/runInstaller -updateNodeList "CLUSTER_NODES={comma_separated_alive_node_list}" ORACLE_HOME=$GRID_HOME CRS=true
```

### 2.1.5 ora.ons Status May Show UNKNOWN

After upgrading from release 11.2.0.3 to 11.2.0.4, you may see `ora.ons` status showing `UNKNOWN` with the explanation being `CHECK TIMED OUT` (reference Bug 12861771).

The workaround is to kill the Oracle Notification Services (ONS) process and run `srvctl start nodeapps`.

### 2.1.6 Purge the Database Recycle Bin Before Upgrading

If the following error is seen during the upgrade process, this may indicate that the recycle bin was not purged:

```
ORA-00600: internal error code, arguments: [15239]
```

Prior to upgrade, empty the database recycle bin by running the following command:

```
SQL> PURGE DBA_RECYCLEBIN
```

### 2.1.7 Downgrade to Release 11.1.0.6

If you anticipate downgrading back to release 11.1.0.6, then apply the patch for Bug 7634119. This action avoids the following `DBMS_XS_DATA_SECURITY_EVENTS` error:

```
PLS-00306: wrong number or types of arguments in call
to 'INVALIDATE_DSD_CACHE' DBMS_XS_DATA_SECURITY_EVENTS
PL/SQL: Statement ignored
```

Apply this patch prior to running `catrelod.sql`.

### 2.1.8 Upgrading a Database With Oracle Data Mining (ODM)

If you upgrade a database with the Data Mining option from 11.2.0.1 to 11.2.0.4, make sure that the `DMSYS` schema does not exist in your 11.2.0.1 database. If it does, you should drop the `DMSYS` schema and its associated objects from the database as follows:

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

### 2.1.9 catrelod.sql Fails if the Time Zone File Version Used by the Database Does Not Exist in Oracle Home

The following error is returned when `catrelod.sql` is run as part of the downgrade process if you previously installed a recent version of the time zone file and used the `DBMS_DST` PL/SQL package to upgrade `TIMESTAMP WITH TIME ZONE` data to that version (reference Bug 9803834):

```
ORA-00600: internal error code, arguments: [qcisSetPlsqlCtx:tzi init], 
 [], [], [], [], [], [], [], [], [], [], []
```

See Step 2 of 'Downgrade the Database' in Chapter 6 of the [Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/downgrade.htm#UPGRD12556) for more details.

If you previously installed a recent version of the time zone file and used the `DBMS_DST` PL/SQL package to upgrade `TIMESTAMP WITH TIME ZONE` data to that version, then you must install the same version of the time zone file in the release to which you are downgrading. For example, the latest time zone files that are supplied with Oracle Database 11g release 2 (11.2) are version 14. If, after the database upgrade, you had used `DBMS_DST` to upgrade the `TIMESTAMP WITH TIME ZONE` data to version 14, then install the version 14 time zone file in the release to which you are downgrading. This ensures that your `TIMESTAMP WITH TIME ZONE` data is not logically corrupted during retrieval. To find which version your database is using, query `V$TIMEZONE_FILE`.

Also see the [Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/toc.htm) for more information on installing time zone files.

### 2.1.10 Oracle ASM Rolling Upgrade

Oracle Automatic Storage Management (Oracle ASM) rolling upgrade check does not allow rolling upgrade to be done from 11.1.0.6 to any later release (reference Bug 6872001). The following message is reported in the alert log:

```
Rolling upgrade from 11.1.0.6 (instance instance-number) to 11.x.x.x is not supported
```

`ORA-15156` is signalled by LMON which will then terminate the instance.

When trying to upgrade Oracle ASM from 11.1.0.6 to a later release of Oracle ASM, apply the patch for this bug to 11.1.0.6 instances before rolling upgrade starts. This patch can be applied to 11.1.0.6 instances in a rolling fashion.

### 2.1.11 Oracle ACFS Registry May Be in an Inconsistent State After Installing or Upgrading to 11.2.0.3.0 or After An Oracle Clusterware Restart

If Oracle ASM is not used as the voting disk and quorum disk, the Oracle Automatic Storage Management Cluster File System (Oracle ACFS) registry resource will report OFFLINE after an install (reference Bug 9876173 and Bug 9864447). This occurs because the Oracle ACFS registry requires that Oracle ASM be used in order to provide Oracle ASM Dynamic Volume Manager (Oracle ADVM) volumes.

### 2.1.12 Multiple Interconnects and Oracle ACFS

If you have Oracle ACFS file systems on Oracle Grid Infrastructure for a cluster 11g release 2 (11.2.0.1), you upgrade Oracle Grid Infrastructure to 11g release 2 (11.2.0.2), 11g release 2 (11.2.0.3), or 11g release 2 (11.2.0.4) and you take advantage of Redundant Interconnect Usage and add one or more additional private interfaces to the private network, then you must restart the Oracle ASM instance on each upgraded cluster member node (reference Bug 9969133).

### 2.1.13 INVALID Materialized View

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

### 2.1.14 Tablespace and Fast Recovery Area Sizing

Note:

Fast Recovery was previously known as Flash Recovery.

The Oracle Database 11g Pre-Upgrade Information Utility (`utlu112i.sql`) estimates the additional space that is required in the `SYSTEM` tablespace and in any tablespaces associated with the components that are in the database (for example, `SYSAUX`, `DRSYS`) (reference Bug 13067061). For a manual upgrade, be sure to run this utility on your existing database prior to upgrading.

The tablespace size estimates may be too small, especially if Oracle XML DB is installed in your database. However, to avoid potential space problems during either a manual upgrade or an upgrade using the Database Upgrade Assistant (DBUA), you can set one data file for each tablespace to `AUTOEXTEND ON MAXSIZE UNLIMITED` for the duration of the upgrade.

If you are using file systems for data file storage, then be sure there is adequate space in the file systems for tablespace growth during the upgrade.

If you are using a Fast Recovery Area, then check that the size available is sufficient for the redo generated during the upgrade. If the size is inadequate, then an `ORA-19815` error will be written to the alert log, and the upgrade will stop until additional space is made available.

### 2.1.15 Deinstallation Restrictions

The following sections describe deinstallation and deconfiguration restrictions. See Section 2.22.2, "Deinstallation Tool Known Bugs" for additional information.

#### 2.1.15.1 Deinstall Upgraded 11.2 Oracle RAC and Oracle Grid Infrastructure for a Cluster Homes

After you deconfigure and deinstall an upgraded Oracle Database 11g release 2 (11.2) Oracle RAC home and to deconfigure and deinstall an 11.2 Oracle Grid Infrastructure for a cluster home, you must detach any pre-11.2 Oracle RAC software homes from the central Inventory (reference Bug 8666509).

Detach the pre-11.2 Oracle RAC homes from the central inventory with the following command:

```
ORACLE_HOME/oui/bin/runInstaller -detachHome ORACLE_HOME_NAME=pre-11.2_ORACLE_HOME_NAME ORACLE_HOME=pre-11.2_ORACLE_HOME
```

### 2.1.16 Upgrading Oracle Database Express Edition to Oracle Database 11g

You cannot upgrade Oracle Database Express Edition 10g to Oracle Database 11g. Instead, use Oracle Data Pump (reference Bug 28137959).

In Oracle Database Upgrade Guide, 11g release 2 (11.2), part number E23633-11, the topic "About Upgrading from Oracle Database Express Edition to Oracle Database" says that you can upgrade Oracle Database 10g Express Edition (Oracle Database XE) to Oracle Database 11g. This information is incorrect. You cannot upgrade Oracle Database 10g XE to Oracle Database Standard or Enterprise Editions. Instead, you can use Oracle Data Pump to export data from Oracle Database XE to a later Oracle Database release.

See Also:

[Oracle Database Utilities](https://docs.oracle.com/cd/E11882_01/server.112/e22490/dp_export.htm#SUTIL200)

## 2.2 Features Not Available or Restricted in 11.2.0.4

The following is a list of components that are not available or are restricted in Oracle Database 11g release 2 (11.2.0.4):

- Certain Oracle Text functionality based on third-party technologies, including `AUTO_LEXER` and `CTX_ENTITY`, have been disabled in 11.2.0.4 (reference Bug 12618046). For `BASIC_LEXER`, the usage of the `INDEX_STEMS` attribute values that depend on third-party technologies, is also affected. If this impacts an existing application, contact Oracle Support Services for guidance.
- You cannot use the `rootcrs.pl` script to delete nodes in Oracle Clusterware 11g release 2 (11.2.0.1) or 11g release 2 (11.2.0.2) (reference Bug 13712508).
- Oracle Database release 11.2.0.1, 11.2.0.2, or 11.2.0.3 upgrade to Oracle Clusterware release 11.2.0.4 is not supported if the 11.2.0.1, 11.2.0.2, or 11.2.0.3 release of Oracle Grid Infrastructure for a cluster is installed in a non-shared Oracle home and the 11.2.0.4 release of Oracle Grid Infrastructure for a cluster is installed in a shared Oracle home (reference Bug 10074804). The original and upgraded releases of Oracle Clusterware should both be installed in either a shared or non-shared Oracle home.
- All Oracle Grid Infrastructure patch set upgrades must be out-of-place upgrades, in which case you install the patch set into a new Oracle Grid home (reference Bug 10210246). In-place patch set upgrades are not supported.

## 2.3 Deprecated and Desupported Features for Oracle Database

Oracle Database 11g release 2 (11.2) introduces behavior changes for your database in addition to new features. Changes in behavior include deprecated and desupported initialization parameters, options, syntax, and the deprecation and desupport of features and components. For more information, see the [Oracle Database Upgrade Guide.](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=UPGRD60000)

## 2.4 Default Behavior Changes

This section describes some of the differences in behavior between Oracle Database 11g release 2 (11.2) and previous releases. The majority of the information about upgrading and downgrading is already included in the [Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/toc.htm).

### 2.4.1 Audits of SYS User SQL Statements Using the DBMS\_SYS\_SQL PL/SQL Package

If the `AUDIT_SYS_OPERATIONS` initialization parameter is set to `TRUE`, then Oracle Database audits user SQL statements that have been executed with `SYS` authorizations using the `DBMS_SYS_SQL` PL/SQL package.

### 2.4.2 Configure and Use SSL Certificates to Setup Authentication

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

### 2.4.3 Use of the Append Hint Runs Out of Memory When Loading Many Partitions

Use of direct-path `INSERT` to load a large number of partitions can exceed memory limits, especially when data compression is specified (reference Bug 6749894). Starting in 11.2, the number of partitions loaded at the same time will be limited, based on the `PGA_AGGREGATE_TARGET` initialization parameter, to preserve memory. Rows that are not stored in the partitions that are currently being loaded are saved in the temporary tablespace. After all rows are loaded for the current set of partitions, other partitions are loaded from rows that are saved in the temporary tablespace.

This behavior helps prevent the direct-path `INSERT` from terminating because of insufficient memory.

### 2.4.4 Use Bloom Filter for Serial Queries on Oracle Exadata

Bloom filter can be used for serial queries on Oracle Exadata to push its evaluation into the storage cells. In previous 11.2 releases, bloom filter was used for serial queries in very limited scenarios. In this 11.2.0.4 release, Oracle allows bloom filter in more scenarios on Oracle Exadata only. This improves performance of the affected queries since, even though the query runs in serial on the server nodes, the pushed bloom filter to the storage cells runs in parallel.

### 2.4.5 FILE\_ACCESS\_ROLE Default Behavior Change

The default behavior of the CTX system parameter `FILE_ACCESS_ROLE` has changed (reference Bug 8360111). Customers with existing Oracle Text indexes that use the file or URL datastore must take action to continue to use the indexes without error. The changes are as follows:

- If `FILE_ACCESS_ROLE` is null (the default), then access is not allowed. By default, users who were previously able to create indexes of this type will not be able to create these indexes after the change.
- `FILE_ACCESS_ROLE` is now checked for index synchronization and document service operations. By default, users will not be able to synchronize indexes of this type or use document service calls such as `ctx_doc.highlight` who were allowed to prior to this change.
- Only SYS will be allowed to modify `FILE_ACCESS_ROLE`. Calling `ctx_adm.set_parameter (FILE_ACESS_ROLE,` `role_name``)` as a user other than SYS will now raise the new error:
	```
	DRG-10764: only SYS can modify FILE_ACCESS_ROLE
	```
- Users can set `FILE_ACCESS_ROLE` to `PUBLIC` to explicitly disable this check (which was the previous default behavior).

### 2.4.6 Non-Uniform Memory Access Optimizations and Support Disabled in 11.2

With Oracle Database 11g release 2 (11.2), non-uniform memory access support is disabled by default. This restriction applies to all platforms and operating systems (reference Bug 8450932).

Non-uniform memory access optimizations and support in the Oracle Database are only available for specific combinations of Oracle version, operating systems, and platforms. Work with Oracle Support Services and your hardware vendor to enable non-uniform memory access support.

## 2.5 Database Security

Note the following changes in Database Security.

### 2.5.1 Improving Native Network Encryption Security

Oracle provides a patch that will strengthen native network encryption security for both Oracle Database servers and clients.

#### 2.5.1.1 About Improving Native Network Encryption Security

The Oracle patch will update encryption and checksumming algorithms and deprecate weak encryption and checksumming algorithms.

This patch, which you can download from My Oracle Support note [2118136.2](https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=2118136.2), strengthens the connection between servers and clients, fixing a vulnerability in native network encryption and checksumming algorithms. It adds two parameters that make it easy to disable older, less secure encryption and checksumming algorithms. Oracle strongly recommends that you apply this patch to your Oracle Database server and clients.

This patch applies to Oracle Database releases 11.2 and later. You can apply this patch in the following environments: standalone, primary-standby, Oracle Real Application Clusters (Oracle RAC), and environments that use database links.

The supported algorithms that have been improved are as follows:

- Encryption algorithms: AES128, AES192 and AES256
- Checksumming algorithms: SHA1, SHA256, SHA384, and SHA512

Weak algorithms that are deprecated and should not be used after you apply the patch are as follows:

- Encryption algorithms: DES, DES40, 3DES112, 3DES168, RC4\_40, RC4\_56, RC4\_128, and RC4\_256
- Checksumming algorithm: MD5

The general procedure that you will follow is to first replace references to desupported algorithms in your Oracle Database environment with supported algorithms, patch the server, patch the client, and finally, set `sqlnet.ora` parameters to re-enable a proper connection between the server and clients.

The patch affects the following areas including, but not limited to, the following:

- `oracle.net.ano.AnoServices` interface constants settings used for Java Database Connectivity (JDBC) thin drivers
- `CONNECTION_PROPERTY_THIN_NET_CHECKSUM_TYPE` thin JDBC network parameter settings
- `SQLNET.ENCRYPTION_TYPES_SERVER` and `SQLNET.ENCRYPTION_TYPES_CLIENT` parameter settings
- Secure Sockets Layer (SSL) `SSL_CIPHER_SUITE` parameter settings
- SecureFiles LOB encrypted columns
- Database Resident Connection Pooling (DRCP) configurations
- Encryption settings used for the configuration of Oracle Call Interface (Oracle OCI), `ODP.NET`

See Also:

- Oracle Database JDBC Developer's Guide
- Oracle Database Advanced Security Administrator's Guide, section titled "Configuring Encryption and Integrity Parameters Using Oracle Net Manager"

#### 2.5.1.2 Applying Security Improvement Updates to Native Network Encryption

In addition to applying a patch to the Oracle Database server and client, you must set the server and client `sqlnet.ora` parameters.

Ensure that you perform the following steps in the order shown:

1. Back up the servers and clients to which you will install the patch.
2. Log in to My Oracle Support and then download patch described in My Oracle Support note [2118136.2](https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=2118136.2).
	My Oracle Support is located at the following URL:
	```
	https://support.oracle.com
	```
3. Patch the server.
	Follow the instructions in My Oracle Support note [2118136.2](https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=2118136.2) to apply the patch to the server. You will apply the same patch to the client in a later step.
4. Patch the clients.
	Determine which clients you need to patch.
	Follow the instructions in My Oracle Support note [2118136.2](https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=2118136.2) to apply the patch to each client.
5. In each client `sqlnet.ora` file, remove all deprecated algorithms if they are defined.
	You can bypass this step if the following parameters are not defined or have no algorithms listed:
	- `SQLNET.ENCRYPTION_TYPES_CLIENT`
		- `SQLNET.CRYPTO_CHECKSUM_TYPES_CLIENT`
6. In the server `sqlnet.ora` file, remove all deprecated algorithms if they are defined.
	You can bypass this step if the following parameters are not defined or have no algorithms listed.
	- `SQLNET.ENCRYPTION_TYPES_SERVER`
		- `SQLNET.CRYPTO_CHECKSUM_TYPES_SERVER`
7. For maximum security on the server, set the following `sqlnet.ora` parameters:
	- `SQLNET.ENCRYPTION_SERVER = REQUIRED`
		- `SQLNET.ENCRYPTION_TYPES_SERVER = (AES256)`
		- `SQLNET.CRYPTO_CHECKSUM_SERVER = REQUIRED`
		- `SQLNET.CRYPTO_CHECKSUM_TYPES_SERVER = (SHA512)`
		- `SQLNET.ALLOW_WEAK_CRYPTO_CLIENTS = FALSE`
8. For maximum security on the client, set the following sqlnet.ora parameters:
	- `SQLNET.ENCRYPTION_CLIENT = REQUIRED`
		- `SQLNET.ENCRYPTION_TYPES_CLIENT = (AES256)`
		- `SQLNET.CRYPTO_CHECKSUM_CLIENT = REQUIRED`
		- `SQLNET.CRYPTO_CHECKSUM_TYPES_CLIENT = (SHA512)`
		- `SQLNET.ALLOW_WEAK_CRYPTO = FALSE`
9. In each client `sqlnet.ora` file, after you have removed all the deprecated algorithms from the server and the clients per steps 5 and 6, set the parameter `SQLNET.ALLOW_WEAK_CRYPTO = FALSE` so that the clients can be prevented from communicating with unpatched servers.
	If the `SQLNET.ALLOW_WEAK_CRYPTO` parameter is set to `FALSE`, then a client attempting to use a weak algorithm will produce an `ORA-12269: client uses weak encryption/crypto-checksumming version` error at the server. A client connecting to a server (or proxy) that is using weak algorithms will receive an `ORA-12268: server uses weak encryption/crypto-checksumming version` error.
10. In the server `sqlnet.ora` file, after you have updated all the clients with `SQLNET.ALLOW_WEAK_CRYPTO = FALSE` per step 9, set the parameter `SQLNET.ALLOW_WEAK_CRYPTO_CLIENTS = FALSE`. This parameter prevents a patched server from communicating with unpatched clients.
	If the `SQLNET.ALLOW_WEAK_CRYPTO` parameter is set to `FALSE`, then a client attempting to use a weak algorithm will produce an `ORA-12269: client uses weak encryption/crypto-checksumming version` error at the server. A client connecting to a server (or proxy) that is using weak algorithms will receive an `ORA-12268: server uses weak encryption/crypto-checksumming version` error.
	If you use the database links, then the first database server acts as a client and connects to the second server. Therefore, ensure that all servers are fully patched and unsupported algorithms are removed before you set `SQLNET.ALLOW_WEAK_CRYPTO` to `FALSE`.

#### 2.5.1.3 Choosing Between Native Network Encryption and Transport Layer Security

Oracle offers two ways to encrypt data over the network, native network encryption and Transport Layer Security (TLS).

There are advantages and disadvantages to both methods.

##### 2.5.1.3.1 Native Network Encryption

There are advantages and disadvantages for native network encryption:

- Advantages
	- It is configured with parameters in the `sqlnet.ora` configuration file.
		- In most cases, no client configuration changes are required.
		- No certificates are required.
		- Clients that do not support native network encryption can fall back to unencrypted connections while incompatibility is mitigated.
- Disadvantages
	- It uses a non-standard, Oracle proprietary implementation.
		- It provides no non-repudiation of the server connection (that is, no protection against a third-party attack).

##### 2.5.1.3.2 Transport Layer Security

There are advantages and disadvantages for Transport Layer Security:

- Advantages
	- It is an industry standard for encrypting data in motion.
		- It provides non-repudiation for server connections to prevent third-party attacks.
		- It can be used for database user authentication.
- Disadvantages
	- It requires client and server changes.
		- Certificates are required for the server and are optional for the client. However, the client must have the trusted root certificate for the certificate authority that issued the server's certificate.
		- Certificates eventually expire.

## 2.6 Java and Web Services

Note the following items when working with Java.

### 2.6.1 Oracle JVM

Oracle Database 11g Release 2 (11.2) includes a fully functional Java Virtual Machine (JVM), as well as the Java class libraries for Sun's Java Development Kit (JDK) 6.0. When combined with Oracle's JDBC and SQLJ, release 11.2.0.4 provides an enterprise class platform, Oracle JVM, for developing and deploying server-based Java applications. Refer to the Oracle JVM Readme file located at:

```
ORACLE_HOME/relnotes/readmes/README_javavm.txt
```

## 2.7 Media Management Software

For environments that consist of a single server, Oracle offers Oracle Secure Backup Express to back up your Oracle Database and other critical Oracle infrastructure to tape. Oracle Secure Backup is fully integrated with Recovery Manager (RMAN) to provide data protection services. For larger environments, Oracle Secure Backup is available as a separately licensable product to back up many database servers and file systems to tape. Oracle Secure Backup release 10.4 is shipping with this Oracle Database 11g release 2 (11.2.0.4). For more information on Oracle Secure Backup, refer to

`http://www.oracle.com/goto/osb/`

### 2.7.1 Globalization Restrictions Within Oracle Secure Backup

The following globalization restrictions apply to Oracle Secure Backup:

- The Oracle Secure Backup Web Tool and command line interface are available in English only, and are not globalized. All messages and documentation are in English.
- Oracle Secure Backup does not support file names or RMAN backup names that are encoded in character sets that do not support null byte termination, such as Unicode UTF-16. Note that this restriction affects file names, not backup contents. Oracle Secure Backup can back up Oracle databases in any character set.

## 2.8 Oracle Application Express

To learn more about Oracle Application Express, refer to the [Oracle Application Express Release Notes](https://docs.oracle.com/cd/E11882_01/relnotes.112/e11944/toc.htm) and the [Oracle Application Express Installation Guide.](https://docs.oracle.com/cd/E11882_01/install.112/e12196/toc.htm)

## 2.9 Oracle Automatic Storage Management (Oracle ASM)

The following sections describe information pertinent to Oracle Automatic Storage Management (Oracle ASM).

### 2.9.1 Oracle Homes on Oracle ACFS Supported Starting With Release 11.2

Placing Oracle homes on Oracle ACFS is supported starting with Oracle Database 11g release 2 (11.2) (reference Bug 10144982). Oracle ACFS can result in unexpected and inconsistent behavior if you attempt to place Oracle homes on Oracle ACFS on database versions prior to 11.2.

### 2.9.2 Storing Oracle RAC Database-Related Files on an Oracle ACFS File System

Starting with Oracle Automatic Storage Management 11g release 2 (11.2.0.3), Oracle ACFS supports RMAN backups (`BACKUPSET` file type), archive logs (`ARCHIVELOG` file type), and Data Pump dumpsets (`DUMPSET` file type). Note that Oracle ACFS snapshots are not supported with these files.

In addition, starting with Oracle Automatic Storage Management 11g release 2 (11.2.0.3), Oracle ACFS supports transient files in the flash recovery area (such as, archived redo logs, flashback logs, and RMAN backups (data file and control file)). Note that Oracle ACFS snapshots are not supported with these files. Permanent files, such as online redo logs and copies of the current control files, are not supported.

## 2.10 Oracle Grid Infrastructure for a Cluster

Note the following items when working with Oracle Clusterware and Oracle Automatic Storage Management (Oracle ASM), which are installed with an Oracle Grid Infrastructure for a cluster installation.

### 2.10.1 Oracle ACFS and Oracle Clusterware Stack Shut Down

When attempting to shut down Oracle Clusterware, the Oracle Clusterware stack may report that it did not successfully stop on selected nodes (reference Bug 8651848). If the database home is on Oracle ACFS, then you may receive the following error:

```
CRS-5014: Agent orarootagent.bin timed out starting process acfsmount for action
```

This error can be ignored.

Alternatively, the Oracle Clusterware stack may report that it did not successfully stop on selected nodes due to the inability to shut down the Oracle ACFS resources. If this occurs, take the following steps:

- Ensure that all file system activity to Oracle ACFS mount points is quiesced by shutting down programs or processes and retry the shutdown.
- If the `ora.registry.acfs` resource check function times out, or the resource exhibits a state of `UNKNOWN` or `INTERMEDIATE`, then this may indicate an inability to access the Oracle Cluster Registry (OCR). The most common cause of this is a network failure. The commands `acfsutil registry` and `ocrcheck` may give you a better indicator of the specific error. Clear this error and attempt to stop Oracle Clusterware again.

## 2.11 Oracle Multimedia

The Oracle Multimedia Readme file located at:

```
ORACLE_HOME/ord/im/admin/README.txt
```

## 2.12 Oracle ODBC Driver

The Oracle ODBC Driver Readme file is located at:

```
ORACLE_HOME/odbc/html/ODBCRelnotesUS.htm
```

## 2.13 Oracle Real Application Clusters

Note the following items when working with Oracle RAC.

### 2.13.1 Moving root Owned Binaries That Need setuid to Local Nodes From NFS

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

## 2.14 Oracle Spatial

The Oracle Spatial readme file supplements the information in the following manuals: [Oracle Spatial Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e11830/toc.htm), [Oracle Spatial Topology and Network Data Models Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e11831/toc.htm), and [Oracle Spatial GeoRaster Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e11827/toc.htm). The Oracle Spatial readme file is located at:

```
ORACLE_HOME/md/doc/README.txt
```

## 2.15 Oracle SQL Developer

The Oracle SQL Developer readme file is located at:

```
ORACLE_HOME/sqldeveloper/readme.html
```

## 2.16 Oracle Text

Note the following items when working with Oracle Text. You should also check entries for the [Oracle Text Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/text.112/e24435/toc.htm) in the Documentation Addendum.

### 2.16.1 Change to Supported Features

Certain Oracle Text functionality based on third-party technologies, including `AUTO_LEXER` and `CTX_ENTITY`, have been disabled in release 11.2.0.4 (reference Bug 12618046). For `BASIC_LEXER`, the usage of the `INDEX_STEMS` attribute values that depend on third-party technologies, is also affected. If this impacts an existing application, contact Oracle Support Services for guidance.

### 2.16.2 Oracle Text Supplied Knowledge Bases

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

## 2.17 Oracle XML DB

Consider the following when working with Oracle XML DB.

### 2.17.1 VARRAY Storage Default Change

In Oracle Database 11g release 1 (11.1), the default value for `xdb:storeVarrayAsTable` changed from `FALSE` to `TRUE` for XMLType object-relational storage. This default applied to the default table, but not when creating XMLType object-relational tables and columns after the schema registration (reference Bug 6858659). In Oracle Database 11g release 2 (11.2), all `VARRAY` data elements are created as tables by default. This provides a significant performance increase at query time. In addition, note the following:

- Tables created prior to 11.2 are not affected by this. The upgrade process retains storage parameters. This only affects tables created in 11.2 or later.
- You can retain the pre-11.2 default of `VARRAY` storage as LOBs if you have small `VARRAY` data elements and you read and or write the full `VARRAY` all at once. You have two options to revert to the pre-11.2 behavior:
	- Re-register the schema with `xdb:storeVarrayAsTable=FALSE`. This affects the default and non-default tables.
		- Or, when creating the table (for non default tables), you can use the `STORE ALL VARRAYS AS LOBS` clause to override the default for all `VARRAY` data elements in the XMLType. This clause can only be used during table creation. It will return an error if used in the `table_props` at schema registration time.
- For schemas registered prior to 11.2 (when the default storage for `VARRAY` data elements was `LOB`), you can use `STORE ALL VARRAYS AS TABLES` clause to override the default for all `VARRAY` data elements in the XMLType.

### 2.17.2 Change in Semantics of xdb:defaultTable Annotation

There is a change in behavior in the semantics of `xdb:defaultTable` annotation while registering Oracle XML DB schemas in 11.2 as compared to 11.1 (reference Bug 7646934). If you specify `xdb:defaultTable="MY_TAB"` without specifying `xdb:sqlInline="false"`, Oracle XML DB creates the table as requested and implicitly marks it as an out-of-line table. This behavior is different from 11.1 where the `defaultTable` annotation was ignored when the `sqlInline` setting was missing.

## 2.18 Oracle Warehouse Builder

For additional information about Oracle Warehouse Builder (OWB) in Oracle Database 11g release 2 (11.2), refer to the [Oracle Warehouse Builder Release Notes.](https://docs.oracle.com/cd/E11882_01/relnotes.112/e24470/toc.htm)

## 2.19 Pro\*C

The Pro\*C readme file is located at:

```
ORACLE_HOME/precomp/doc/proc2/readme.doc
```

## 2.20 Pro\*COBOL

The Pro\*COBOL readme file is located at:

```
ORACLE_HOME/precomp/doc/procob2/readme.doc
```

## 2.21 SQL\*Plus

For additional information regarding SQL\*Plus, see the SQL\*Plus Release Notes.

## 2.22 Open Bugs

This section lists known bugs for release 11.2.0.4. A supplemental list of bugs may be found as part of the release documentation specific for your platform.

### 2.22.1 Database Configuration Assistant (DBCA) Known Bugs

Bug 16929299

Depending on the number of server instances running on a host and its utilization of memory resources, the Database Configuration Assistant (DBCA) may run into out-of-memory issues, and may fail with the following error:

```
java.lang.OutOfMemoryError
```

Workaround: Increase the Java heap size for DBCA from 128 MB to 256 MB. For example:

```
JRE_OPTIONS="${JRE_OPTIONS} -DSET_LAF=${SET_LAF} 
-Dsun.java2d.font.DisableAlgorithmicStyles=true 
-Dice.pilots.html4.ignoreNonGenericFo    nts=true  -DDISPLAY=${DISPLAY} 
-DJDBC_PROTOCOL=thin -mx256m"
```

Bug 16832579

If a 10.2.0.4 database is coexisting in an 11.2.0.x Oracle Grid Infrastructure environment and the owners of the 11.2 and 10.2 Oracle homes are different, 10.2.0.4 Database Configuration Assistant (DBCA) will not be able to parse Grid home listeners due to a permission issue.

Workaround: Provide write permissions to the `Gridhome/network/admin` directory on all nodes during configuration of the database from the 10.2.0.4 Oracle home.

### 2.22.2 Deinstallation Tool Known Bugs

Bug 12762927

When using the deinstallation tool to deinstall a shared Oracle RAC home, some of the files or directories may not get deleted.

Workaround: To remove the `ORACLE_HOME`, run the `rm -rf $ORACLE_HOME` command after the deinstallation tool exits.

Bug 9925724

If `Grid_home` is created directly under a root-owned directory, the deinstallation tool cannot remove the top-level home directory. An empty Oracle home directory remains at the end of the deinstallation.

Workaround: Run `rmdir` `ORACLE_HOME` using the root user on all nodes.

Bug 8666509

A deinstallation of Oracle Clusterware should ask you to detach any pre-11.2 Oracle RAC homes from the Oracle inventory.

Workaround: After you deconfigure and deinstall an upgraded 11.2 Oracle RAC home and want to continue with deconfiguration and deinstallation of the Oracle Grid Infrastructure for a cluster home, first detach any pre-11.2 Oracle RAC software homes from the central Inventory.

Bug 8644344

When running the deinstallation tool to deinstall the database, you will be prompted to expand the Oracle home and to select a component. If you select the top level component, `Oracle Database Server`, and do not select the Oracle home, OUI does not show the message to run the deinstall utility and proceeds with the deinstallation of the database.

Workaround: Run the deinstallation tool to deinstall the Oracle home.

Bug 8635356

If you are running the deinstall tool from `ORACLE_HOME` that is installed on shared NFS storage, then you will see errors related to `.nfs` files during `ORACLE_HOME` clean up.

Workaround: To remove the `ORACLE_HOME`, run the `rm -rf` `ORACLE_HOME` command after the deinstall tool exits. Alternatively, you can use the standalone `deinstall.zip` and specify the location of the `ORACLE_HOME`.

### 2.22.3 Oracle Automatic Storage Management (Oracle ASM) Known Bugs

Bug 12881572

During an upgrade of Oracle ASM release 10.1.0.5 to Single-Instance High Availability (SIHA) release 11.2.0.4, the `rootupgrade.sh` script returns the following error:

```
<ORACLE_HOME>/bin/crsctl query crs activeversion ... failed rc=4 with message: Unexpected parameter: crs
```

Workaround: This error can be ignored.

Bug 12332603

Oracle Automatic Storage Management (Oracle ASM) loses the rolling migration state if Cluster Ready Services (CRS) shuts down on all nodes. If this occurs, one of the Oracle ASM versions will fail with either the `ORA-15153` or `ORA-15163` error message.

Workaround: Consider the following scenario of 4 nodes (`node1`, `node2`, `node3`, and `node4`) that are at release 11.2.0.3 and being upgraded to release 11.2.0.4:

- `node1` and `node2` are upgraded to 11.2.0.4 and running.
- `node3` and `node 4` are still at 11.2.0.3 and running.
- Now consider that there is an outage where all CRS stacks are down which leaves the cluster in a heterogeneous state (that is, two nodes at 11.2.0.3 and two nodes at 11.2.0.4).

To proceed with the upgrade, run one of the following steps (depending on the node that was started as the first node):

- If `node3` or `node4` was started as the first node (for example, as an 11.2.0.3 node), you need to run the `ALTER SYSTEM START ROLLING MIGRATION TO '11.2.0.4'` command on the Oracle ASM instance on `node3` or `node4` before you can bring up an 11.2.0.4 node.
- If `node1` or `node2` was started as the first node, you need to the `ALTER SYSTEM START ROLLING MIGRATION TO '11.2.0.3'` command on the Oracle ASM instance on `node1` or `node2` before you can bring up any 11.2.0.3 node.

Continue the upgrade procedure as already documented from this point forward. Note that before executing one of the above steps to bring the Oracle ASM cluster back into rolling migration, you cannot start two nodes of different versions in the cluster. If you do so, one of the Oracle ASM versions will fail with either the `ORA-15153` or `ORA-15163` error message.

Bug 9413827

An 11.2.0.1 Oracle Clusterware rolling upgrade to 11.2.0.4 fails when Oracle Cluster Registry (OCR) is on Oracle ASM.

Workaround: Apply the patch for bug 9413827 on 11.2.0.1 Oracle Grid Infrastructure for a cluster home before performing the upgrade.

Bug 9276692

Cannot permanently stop the Oracle ASM instance.

Workaround: If the Oracle ASM instance is disabled using SRVCTL, you must unregister Oracle ACFS-related resources to avoid restarting the Oracle ASM instance. Do this by executing the following command as root:

```
acfsroot disable
```

### 2.22.4 Oracle ASM Dynamic Volume Manager (Oracle ADVM) Known Bugs

Bug 9683229

Oracle ADVM does not support mounting ext3 file systems over Oracle ADVM with the mount barrier option enabled. The mount barrier option is enabled by default on SLES11.

Workaround: Mount ext3 file system with `-o barrier=1`. For example:

```
mount -o barrier=0 /dev/asm/myvol-131 /mnt
```

### 2.22.5 Oracle Automatic Storage Management Cluster File System (Oracle ACFS) Known Bugs

Bug 19668256

The deinstall tool deletes the Oracle ACFS mount point when Oracle base is inside the Oracle ACFS mount point.

Workaround: Choose a location for Oracle base that is outside the Oracle ACFS mount point.

Bug 16988224

After a rolling upgrade with Oracle Automatic Storage Management Cluster File System (Oracle ACFS) replication configured, it is possible that not all replication daemons are running in the cluster. This can be verified by running the following command:

```
crsctl stat res -w "TYPE = ora.acfsrepltransport.type"
```

If the transport daemon is not running on the nodes where the replicated Oracle ACFS file system is mounted, then the file system must be unmounted and remounted on all nodes after the upgrade is complete. Run the same command again to verify that the daemon is running.

Workaround: None.

Bug 15944411

On the fifth attempt to resize an Oracle ACFS file system, the following error is returned:

```
ACFS-03008: The Volume Could Not Be Resized At the 5th attempt
```

Workaround: Set the `compatible.advm` attribute to 11.2.0.4. Setting the `compatible.advm` attribute to 11.2.0.4 enables support for unlimited resizes to Oracle ACFS file systems.

Bug 12690672

In releases prior to 11.2.0.4, it is possible to put the database home on an Oracle Automatic Storage Management Cluster File System (Oracle ACFS). If the database home is on an Oracle ACFS file system, the database will have a hard start and stop dependency on the corresponding Oracle ACFS file system.

After upgrading Oracle Grid Infrastructure or Oracle RAC to release 11.2.0.4, the dependency between the database and the Oracle ACFS file system, which stored the previous version's database home, is not deleted.

If using a different Oracle ACFS file system than was used to store the previous version's database home, the database fails to start.

Workaround: After a database upgrade, if using a different Oracle ACFS file system for the database home, Oracle recommends that you review the list of Oracle ACFS file systems that you are using for the database, and update the database dependencies on the file systems using the `srvctl modify database -d` `db_unique_name` `-j` `acfs_path_list` command (instead of the `srvctl modify` `filesystem` `-j` `filesystem-list` command).

Bug 10104766

An `ls` command of a very large shared Oracle ACFS directory can hang, even if the files have been removed from the directory.

Workaround: Set the `compatible.advm` attribute to 11.2.0.4.

After upgrading the `compatible.advm` attribute, the performance improvements will be available on any newly created directories. If desired, files created prior to the change to the `compatible.advm` attribute can be copied into the newly created directories.

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

### 2.22.6 Oracle Clusterware Known Bugs

Bug 17279427

If the `JAVA_HOME` environment variable is set in the user environment when `root.sh` or `rootupgrade.sh` runs as part of the clusterware install, then Oracle Trace File Analyzer (TFA) will fail to install. The following message is returned:

```
You should not use any other parameters with -crshome will be seen in the root script log file.
```

Workaround: This issue can be avoided by ensuring `JAVA_HOME` is not set prior to running the root scripts for clusterware installation or upgrade or customers can download the latest TFA from My Oracle Support Note 1513912.1 (at `https://support.oracle.com`).

Bug 17227707

The Oracle Trace File Analyzer (TFA) uses a date and time stamp when naming collection directories and files. In some non-English language environments, the use of the operating system `date` command may return unexpected characters which are then used to name the directory and files.

Workaround: This issue can be avoided by either exporting the environment variable `LC_ALL=C` before calling `tfactl diagcollect` or by downloading the latest TFA from My Oracle Support Note 1513912.1 (at `https://support.oracle.com`).

Bug 17181902

Service resources for pre-11.2 releases may be `OFFLINE` after Oracle Grid Infrastructure is upgraded to release 11.2.0.4.

Workaround: Use the following command to manually start the `OFFLINE` service resources:

```
$ORACLE_HOME/bin/srvctl start service -d <dbname> -s <srvname> -i <instname>
```

Bug 17027888

Cluster Ready Services Daemon (CRSD) on a non-PE master node may hang and stop processing Oracle Cluster Registry (OCR) requests if the OCR master failed while it was sending a message to it.

Workaround: Restart the CRSD process.

Bug 16914379

Upgrading the Oracle Grid Infrastructure from Oracle Database 11g release 2 (11.2.0.4) to Oracle Database 12c release 1 (12.1) fails due to Oracle ACFS or Oracle ADVM resources being unable to stop.

Workaround: Manually stop the resources using SRVCTL or CRSCTL, and retry the upgrade.

Bug 16825359

If an attempt is made to relocate the Cluster Health Monitor (CHM) Repository to a directory that has previously contained it, the following error is returned:

```
CRS-9114-Cluster Health Monitor repository location change failed on one or more nodes. Aborting location change.
```

Workaround: Archive or delete the previous subdirectories (`<hostname>, <hostname>bkp`) and try again.

Bug 16592535

During upgrade of Cluster Ready Services (CRS) from 10.1.0.5 to 11.2.0.4, patch 3841387 is mandatory but the Cluster Verification Utility (CVU) prerequisite check does not enforce the requirement. Consequently, CVU does not issue an error if the patch is not applied.

Workaround: Manually ensure that patch 3841387 is applied to the 10.1.0.5 source home using the `opatch lsinventory` command before proceeding with the upgrade.

Bug 13110641

While installing Oracle RAC software on a cluster configured with Grid Naming Service (GNS), the Prerequisite's page might show a warning status for the GNS Integrity check even when GNS is working fine.

The message appears to be of the following type:

```
PRVF-5217 : An error occurred while trying to look up IP address for 
"<gns-subdomain-extended-name>"
```

Workaround: Run `nslookup` on the fully qualified names that are listed in the error message. If `nslookup` returns an IP address for the name with a non-authoritative answer, then this warning can be ignored. If the name does not resolve to an IP address, then follow the steps mentioned in Action part of the error message.

Bug 13073882

Service resources for pre-11.2 releases may be `OFFLINE` after Oracle Grid Infrastructure is upgraded to release 11.2.0.4.

Workaround: Use the following command to start the `OFFLINE` service resources manually:

```
srvctl start service -d <dbname> -s <srvname> -i <instname>
```

Bug 13033342

After an upgrade from Oracle ASM 10.2.x to Oracle Grid Infrastructure 11.2.x or Oracle ASM 11.2.x in an Oracle RAC environment, you must move the `PFILE` to an `SPFILE` in a disk group before running the add node operation, otherwise the correct initialization parameter file cannot be found.

Workaround: None.

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

In release 11.2.0.3, the default `RETENTION_TIME` size of a Cluster Health Monitor (CHM) repository in number of seconds is 30823 for a 4-node cluster or is (30823\*4) divided by the number of nodes for other clusters. When upgrading from 11.2.0.3 to 11.2.0.4, the `RETENTION_TIME` is 6311 for a 4-node cluster.

Workaround: Oracle recommends changing the `RETENTION_TIME` size from 6311 to 30823 for a 4-node cluster after upgrading from 11.2.0.3 to 11.2.0.4 by using the following `oclumon` command:

```
oclumon manage -repos resize 30823
```

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

Bug 8641798

Note: Also reference Bugs 3841387, 8262786, 8373758, 8406545, and 8441769.

Oracle resources for 10.1, 10.2 and 11.1 Oracle RAC databases may not operate properly after upgrading Oracle Clusterware to 11.2.

Workaround: Apply the patches for any of the bugs listed here to the Oracle Database home.

### 2.22.7 Oracle Database Upgrade Assistant (DBUA) Known Bugs

Bug 12914730

The custom network configuration is not carried forward for Oracle RAC database upgrades to release 11.2.0.4.

Workaround: The custom network configuration needs to be redone by manually copying the settings from the source Oracle home to the target Oracle home.

### 2.22.8 Oracle Database Vault Known Bugs

Bug 8341283

The `ACTION_NAME` entry in the `DVSYS.AUDIT_TRAIL$` table displays `Realm Authorization Audit` for a failed realm enforcement if the audit option is set to audit on success and failure. The `RETURNCODE` will show the correct error code that was triggered.

Workaround: Use the `RETURNCODE` value to determine whether a violation has occurred and the `ACTION_NAME` column to identify whether the audit was generated by a realm enforcement or command rule enforcement.

Bug 7118790

Before Oracle Database 11g release 2 (11.2.0.4), there was no mechanism to control the usage of `ORADEBUG` in the Oracle Database Vault environment.

Workaround: The `DVSYS.DBMS_MACADM.ENABLE_ORADEBUG` and `DVSYS.DBMS_MACADM.DISABLE_ORADEBUG` procedures can be used to restrict the `ORADEBUG` usage.

### 2.22.9 Oracle Database QoS Management Known Bugs

Bug 12792222

This bug applies to recommendations for CPU resources managed by Oracle Database QoS Management. If the number of configured CPUs for all instances on a server is less than the number of physical CPUs for that server, then the nonallocated, or "free", CPUs are not detected by Oracle Database QoS Management and no recommendation is made to increase the number of configured CPUs. Only those "slices" that host databases are considered as donors for the target slice. Adding one of the non-allocated CPUs should be the first-ranked Move CPU action.

Workaround: Make sure the sum of CPU counts configured for each database instance on each server is the same as the number of physical CPUs.

Bug 12767103

If a user creates a performance class with two or more services in its classifier(s) and these services are not all specified to run in the same server pool, the metrics graphs for that performance class on the Enterprise Manager Quality of Service (QoS) Management Performance Class details page are incorrect. The Resource Use Time and Resource Wait Time graphs will only display metrics from one server pool. The other graphs will correctly display metrics for all server pools.

Workaround: This bug will not affect the correct management or recommended actions associated with this type of performance class.

### 2.22.10 Oracle Database Enterprise Edition Known Bugs

Bug 20720667

If you are running with Oracle Direct NFS (dNFS) enabled, then you can use network file system (NFS) protocol devices for backup files or for Oracle Data Pump files. Since these files are not used by the database all of the time, you can run NFS administration changes to unmount the NFS volume and remount it on the same mount point. Without this fix, you may see stale or bad file handle errors because dNFS uses the cached file handles from the system global area (SGA). The `UNMOUNTVOLUME` procedure allows you to clean up the cached file handles in SGA.

The `UNMOUNTVOLUME` procedure cleans up the cached NFS file handles in SGA and should be used when any NFS mount changes are being made using the operating system and when the operating system `UNMOUNT` and `MOUNT` commands are being invoked. The `UNMOUNTVOLUME` procedure is the equivalent of the operating system `UNMOUNT` command for the dNFS client.

Workaround: Restart the database so that the old file handles that are cached in SGA are cleaned up as part of the database restart.

Bug 20511726

Database directory names should not contain error message prefix codes (for example, TNS or ORA) because this causes a problem for Oracle Enterprise Manager.

Workaround: None.

Bug 16386142

The installer copies files to the temporary bootstrap location, usually in `/tmp`, using the `-p` option to preserve permissions on the source files. The source and the target file systems are not mounted with the same ACL options so the copy fails with the following error because the permissions cannot be preserved on the target file system:

```
[INS-30060] Check for group existence failed.
```

Workaround: There are three possible workarounds:

- Mount the source file system and the file system on which the `/tmp` directory resides using the same ACL options.
- Mount the file system on which the source software exists using the `noacl` option.
- Copy the installation software to the `/tmp` directory and retry the installation.

Note:

This issue is also observed when the software (zipfile 1 and 2) is not extracted in the same location or the `OSOPER` group is specified during the installation.

Bug 9859532

Current implementation of node-specific network interfaces requires complete definition of all networks used by Oracle RAC for that node (that is, either node abides by global network configuration or it defines its own node-specific network configuration).

As a corollary, once the first node-specific network interface is defined for a given node, Oracle RAC will not consider any configured global network interfaces that are already configured and may have applied for the same node.

While this is correct, it presents a problem. If the cluster had a working global network configuration, the moment a user updates it (using `oifcfg`) to define a node-specific `public` interface, a global configuration will not be considered for this node, and it will have only one newly-defined `public` interface. Any cluster interconnects that existed in the global network configuration, and may still resolve fine for this node, will not be considered valid. Thus, the node loses cluster interconnects and PCW stack goes down on that node.

Workaround: If the node belongs to a global cluster network configuration, then if there is an intent to make network configuration node-specific, the first defined node-specific interface must be cluster interconnect, so that node never loses interconnect with other cluster nodes. Then, other node-specific interfaces can be defined as necessary.

Bug 8729627

When using 11.1 DBCA to remove a database on a cluster running 11.2 Oracle Clusterware, a `PRKP-1061/CRS-2524` error may be displayed because the database resource is locked.

Workaround: You can ignore the message. Click OK to continue.

### 2.22.11 Oracle Enterprise Manager Database Control Known Bugs

Bug 16706199

The Oracle home value for the Cluster Target is not changed after a Cluster Ready Services (CRS) upgrade for Oracle Enterprise Manager Cloud Control (Cloud Control).

Workaround: Modify the Cluster Target properties in Oracle Enterprise Manager Grid Control or in Oracle Enterprise Manager Cloud Control for the cluster and its related targets as shown in the following steps:

1. Go to the Targets page and click All Targets.
2. Select the target.
3. Select a target menu item, click Target Setup, and click Monitoring Configuration.
4. On the Monitoring Configuration page, set the Oracle Home Path to upgraded Clusterware Oracle Home.

Bug 12793336

When attempting to upgrade Cluster Ready Services (CRS) or Oracle ASM to release 11.2 using the Oracle ASM Configuration Assistant (ASMCA), the upgrade succeeds, but it may fail to update the new clusterware home for cluster targets in existing agent homes due to permission issues. As a result, Oracle Enterprise Manager Grid Control and Database Control cannot monitor the Oracle ASM and CRS targets.

Workaround: Modify `OracleHome` property of Oracle ASM and Cluster targets using the Monitoring Configuration link on ASM and Cluster home pages, respectively.

Bug 9766628

`emctl` commands did not return valid results as expected.

Workaround: The `emctl` command needs to be run from an Oracle Database home. Do not invoke this command from the Oracle Grid Infrastructure for a cluster home.

Bug 8674920

If the installation owners for the Oracle Grid Infrastructure for a cluster and Oracle Database are different, then the owners of Oracle ASM binaries and Oracle Enterprise Manager Agent binaries are also different. When you start Support Workbench, the error message `Error Operation failed - Operation failed` might appear, because the Oracle Enterprise Manager Agent is running as a different user, and Support Workbench does not have permissions for the Oracle ASM target.

Workaround: None.

### 2.22.12 Oracle OLAP Known Bugs

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

### 2.22.13 Oracle Real Application Clusters (Oracle RAC) Known Bugs

Bug 17210454

The Oracle Real Application Clusters (Oracle RAC) Configuration Audit Tool (RACcheck) returns a space availability error even if there is enough space available on the `/tmp` directory when it is being run in a non-English installation.

Workaround: Download the latest RACcheck from My Oracle Support, Note 1268927.1 (at `https://support.oracle.com`) to avoid this issue.

Bug 16233295

When upgrading from 11.2.x.x to 11.2.0.4, if any customized listener configuration is set (such as a remote listener), Database Upgrade Assistant (DBUA) will set it back to the default.

Workaround: Run `ALTER SYSTEM SET REMOTE_LISTENER=` `<user_remote_listener_setting>``, ... SCOPE=BOTH` from SQL\*Plus after the database upgrade.

### 2.22.14 Oracle SQL\*Loader Known Bugs

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

### 2.22.15 Oracle Universal Installer Known Bugs

Bug 17533350

When installing 32-bit Oracle Database Client software on a 64-bit architecture server, the Oracle base cannot be the same as the secured Oracle base of any other 64-bit Oracle Database product software.

When installing 64-bit Oracle Database product software, the Oracle base cannot be same as the secured Oracle base of 32-bit Oracle Database client software.

Workaround: None.

Bug 17085615

During the local node only deinstallation, the following message can be ignored:

The deconfig command below can be run in parallel on all the remote nodes. Run the command on the local node after the execution completes on all the remote nodes.

Workaround: None.

Bug 17008903

When installing 11.2.0.4 Oracle Grid Infrastructure, the Oracle Universal Installer (OUI) does not verify and report if Oracle ASM disks with insufficient permission on remote nodes are selected due to `root.sh` failing on the nodes where the disks reside that have insufficient permission.

Workaround: Ensure that the Oracle ASM disks with the insufficient permission on remote nodes are not selected. The Cluster Verification Utility (CVU) tool can be used to verify that disks on remote nodes have sufficient permission.

Bug 16930240

During an upgrade from 11.2.0.2 or 11.2.0.3 Oracle Grid Infrastructure to 11.2.0.4.0 and when there are more than 1,000 database service resources registered, the upgrade fails because the root script fails on the first node while trying to upgrade the Server Management (SRVM) model.

Workaround: Manually apply the patch for bug 16684285 on 11.2.0.2 or 11.2.0.3 Oracle Grid Infrastructure home before starting the upgrade.

Bug 16842099

If the database is configured using the Oracle Universal Installer (OUI), the VKTM/LMS process runs with the wrong priority.

Workaround: Stop and start the database after the installation is complete.

Bug 13028836

Secure Shell (SSH) setup code is changing the user's home directory permission to 755 only on the current or local node.

Workaround: This is expected behavior because SSH requires this permission to do some SSH-related operations on the local node.

Bug 13012502

Cloning of an Oracle home that was added with Oracle Database Client or Oracle Database Examples software results in a database creation failure.

Workaround: During the clone operation, supply the values for the privileged operating system groups (`OSDBA_GROUP` and `OSOPER_GROUP`) as specified in the [Oracle Database Installation Guide for Linux](https://docs.oracle.com/cd/E11882_01/install.112/e47689/toc.htm).

Bug 12930328

If the central inventory location is different on different nodes of a cluster, `addnode.sh` does not update the inventory correctly on remote nodes of the cluster.

Workaround: Adding nodes to a cluster requires the central inventory location to be the same on all the nodes of the cluster. Please ensure that this is the case prior to running `addnode.sh`.

Bug 12711224

If Oracle Universal Installer (OUI) crashes during a node reboot or crashes while you are executing the rootupgrade script, OUI cannot resume post-upgrade tasks.

Workaround: You have to manually take care of the following tasks and complete the upgrade:

- If you are upgrading from a pre-11.2 to 11.2.0.4 release:
	1. Update inventory
		2. Orace Net Configuration Assistant
		3. Automatic Storage Management Configuration Assitant
		4. Enterprise Manager Configuration Upgrade Utility
		5. Oracle Cluster Verification Utility
- If you are upgrading from a post-11.2 to 11.2.0.4 release:
	1. Update inventory
		2. Enterprise Manager Configuration Upgrade Utility
		3. Oracle Cluster Verification Utility

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

### 2.22.16 Oracle XML Database Known Bugs

Bug 17215306

You may run into the following error:

```
ORA-600 [QMXPTREWRITEFRO1]
```

Workaround: If you use the `XMLTABLE()` query and run into this error, you can request the BLR for this bug fix or use the following command:

```
ALTER SESSION SET EVENTS '19120 TRACE NAME CONTEXT FOREVER, LEVEL 0x10000000'
```

Bug 16069266

Using Transportable Tablespaces (TTS) to export or import tables with Binary XML data is not supported.

Workaround: Use the Oracle Data Pump conventional path to move data.

Bug 12834970

Starting with release 11.2.0.3, the `MOVEXDB_TABLESPACE` and `REBUILDHIERARCHICALINDEX` procedures were moved from the `DBMS_XDB` package to the `DBMS_XDB_ADMIN` package. These procedures are no longer available in the `DBMS_XDB` package.

Workaround: None.

Bug 9586264

In order to fully optimize some `XMLQUERY` or `XMLTABLE` queries, `OPTIMIZER_FEATURE_ENABLE` should be set to 11.1.0.6 or above.

Workaround: None.

### 2.22.17 Vendor and Operating System Known Bugs

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