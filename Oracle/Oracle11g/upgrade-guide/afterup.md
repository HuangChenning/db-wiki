---
title: Post-Upgrade Tasks for Oracle Database
book: Upgrade Guide
doc_id: E23633-11
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e23633/afterup.htm
tags:
  - oracle
  - 11g
  - upgrade-guide
---

## 4 Post-Upgrade Tasks for Oracle Database

After performing the procedures for upgrading Oracle Database, you must complete required tasks and consider recommendations for the new release.

The chapter contains the following topics:

## How to Show the Current State of the Oracle Data Dictionary

You can collect upgrade and migration diagnostic information about the current state of the data dictionary by running the `dbupgdiag.sql` script. The script can be run in SQL\*Plus both before the upgrade on the source database and after the upgrade on the upgraded database as SYS user.

See Also:

Note 556610.1 Script to Collect DB Upgrade/Migrate Diagnostic Information (dbupgdiag.sql) on My Oracle Support at at `http://support.oracle.com`

To show the current state of the dictionary, execute a SQL query similar to the following example:

```
SQL> spool /tmp/regInvalid.out
SQL> set echo on
-- query registry
SQL> set lines 80 pages 100
SQL> select substr(comp_id,1,15) comp_id,substr(comp_name,1,30)
      comp_name,substr(version,1,10) version,status
from dba_registry order by modified;
```

To query invalid objects, execute a SQL query similar to:

```
SQL> select substr(owner,1,12) owner,substr(object_name,1,30) object,substr(object_type,1,30) type, status
from dba_objects where status <> 'VALID'order by owner, type;
SQL> spool off
SQL> set echo off
```

## About OPatch Commands After Upgrading Oracle Database

After you upgrade Oracle Database, you must run OPatch commands from the new Oracle home. For example, run the `lsinventory` command from the new Oracle home in order to list an accurate and complete inventory of what is currently installed on the system.

See Also:

"Appendix A" in [Oracle OPatch User's Guide for Windows and UNIX](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=OPTCH) for OPatch syntax and commands

## Required Tasks to Complete After Upgrading Oracle Database

After you upgrade Oracle Database, regardless of whether you perform the upgrade manually, or upgrade automatically by using Database Upgrade Assistant (DBUA), you must complete any required tasks that are specified for your environment. You must also consider important information about your environment. The following topics contain the required procedures and information:

- Setting Environment Variables on Linux and UNIX Systems After Manual Upgrades
- Upgrading the Recovery Catalog After Upgrading Oracle Database
- Upgrading the Time Zone File Version After Upgrading Oracle Database
- Upgrading Statistics Tables Created by the DBMS\_STATS Package After Upgrading Oracle Database
- Upgrading Externally Authenticated SSL Users After Upgrading Oracle Database
- Installing Oracle Text Supplied Knowledge Bases After Upgrading Oracle Database
- Updating Your Oracle Application Express Configuration After Upgrading Oracle Database
- Configuring Fine-Grained Access to External Network Services After Upgrading Oracle Database
- Enabling Oracle Database Vault and Revoking the DV\_PATCH\_ADMIN Role After Upgrading Oracle Database

### Setting Environment Variables on Linux and UNIX Systems After Manual Upgrades

If your operating system is Linux or UNIX, and if you performed a manual upgrade of Oracle Database, then you must ensure that certain environment variables point to the directories of the new Oracle Database release. Note that DBUA automatically makes necessary changes to environment variables. Additionally, if you are upgrading a cluster database, then perform these checks on all nodes on which the cluster database has instances configured.

Confirm that the following environment variables point to the directories of the new Oracle home:

- `ORACLE_HOME`
- `PATH`

See Also:

- [Oracle Database Administrator's Guide for procedures](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm)
- Your operating system-specific Oracle Database installation documents for information about setting other important environment variables on your operating system

### Setting oratab and Scripts to Point to the New Oracle Home After Upgrading Oracle Database

After you upgrade Oracle Database to the new release, you must ensure that your `oratab` file and any client scripts that set the value of `ORACLE_HOME` point to the new Oracle home that is created for the new Oracle Database 11g release. Although DBUA automatically points `oratab` to the new Oracle home, client scripts must be checked no matter which method you use to upgrade.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm)

### Upgrading the Recovery Catalog After Upgrading Oracle Database

For complete information about upgrading the recovery catalog and the `UPGRADE CATALOG` command, see [Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/rcmcatdb.htm#BRADV188) for the topic that describes the procedures.

### Upgrading the Time Zone File Version After Upgrading Oracle Database

If the Pre-Upgrade Information Tool instructed you to upgrade the time zone files after completing the database upgrade, then use the `DBMS_DST` PL/SQL package to upgrade the time zone file.

Oracle Database supplies multiple versions of time zone files, and there are two types of file associated with each one: a large file, which contains all the time zones defined in the database, and a small file, which contains only the most commonly used time zones. The large versions are designated as `timezlrg_` `version_number``.dat`, while the small versions are designated as `timezone_` `version_number``.dat`. The files are located in the `oracore/zoneinfo` subdirectory under the Oracle Database home directory.

See Also:

- Note ID 977512.1 "Updating the RDBMS DST version in 11gR2 (11.2.0.1 and up) using `DBMS_DST` " on My Oracle Support at `https://support.oracle.com`
- ["About Warnings for TIMESTAMP WITH TIME ZONE Data Type"](upgrade.md)
- [Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/ch4datetime.htm#NLSPG261) and follow the procedure in "Steps to Upgrade Time Zone File and Timestamp with Time Zone Data"

### Upgrading Statistics Tables Created by the DBMS\_STATS Package After Upgrading Oracle Database

If you created statistics tables using the `DBMS_STATS.CREATE_STAT_TABLE` procedure, then upgrade these tables by running the following procedure:

```
EXECUTE DBMS_STATS.UPGRADE_STAT_TABLE('scott', 'stat_table');
```

In the example, `SCOTT` is the owner of the statistics table and `STAT_TABLE` is the name of the statistics table. Perform this procedure for each statistics table.

### Upgrading Externally Authenticated SSL Users After Upgrading Oracle Database

If you are upgrading from Oracle9i Release 2 (9.2) or Oracle Database 10g Release 1 (10.1), and you are using externally authenticated SSL users, then you must run the SSL external users conversion (`extusrupgrade`) script to upgrade those users. The script has the following syntax:

```
ORACLE_HOME/rdbms/bin/extusrupgrade --dbconnectstring 
<hostname:port_no:sid> --dbuser <db admin> --dbuserpassword 
<password> -a
```

Note:

If you are upgrading from Oracle Database 10g Release 2 (10.2) or higher, then you are not required to run this command.

See Also:

for more information on the `extusrupgrade` script

### Installing Oracle Text Supplied Knowledge Bases After Upgrading Oracle Database

The Oracle Text supplied knowledge bases are part of the companion Oracle Database 11g release products and are not immediately available after an upgrade to the new Oracle Database 11g release. Any Oracle Text features dependent on the supplied knowledge bases which were available before the upgrade do not function after the upgrade. To re-enable such features, you must install the Oracle Text supplied knowledge bases from the installation media.

After an upgrade, all user extensions to the Oracle Text supplied knowledge bases must be regenerated. These changes affect all databases installed in the given Oracle home.

See Also:

- [Oracle Text Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/text.112/e24435/cthes.htm#CCAPP0900) for information about Oracle Text-supplied knowledge bases
- The postinstallation tasks section of your platform-specific [Oracle Database Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for companion products

### Updating Your Oracle Application Express Configuration After Upgrading Oracle Database

If your database originally included Application Express Version 3.2 or higher, then there is no additional configuration necessary after upgrading to the new Oracle Database 11g release.

If your database was not an Oracle Express Edition (XE) database, but contained an earlier version of Application Express (HTML DB), then the latest version is automatically installed during the upgrade. You must complete a series of postinstallation steps to configure Application Express for use with the new Oracle Database 11g release.

See Also:

[Oracle Application Express Installation Guide](https://docs.oracle.com/cd/E11882_01/install.112/e12196/db_install.htm#HTMIG203) for postinstallation tasks for Application Express

If your database is an Oracle Express Edition (XE) database, then it contains an earlier version of Application Express, which is tailored for the XE environment. Review the OTN document describing the differences between Oracle XE and Oracle Application Express at the following URL:

`http://www.oracle.com/technetwork/developer-tools/apex/overview/index.html`

The database administration features available with the XE edition of Application Express are not available in version 3.2, but Oracle Enterprise Manager Database Control can, optionally, be installed to provide a graphical interface for database administration.

### Configuring Fine-Grained Access to External Network Services After Upgrading Oracle Database

Oracle Database 11g includes fine-grained access control to the `UTL_TCP`, `UTL_SMTP`, `UTL_MAIL`, `UTL_HTTP`, or `UTL_INADDR` packages using Oracle XML DB. If you have applications that use these packages, then you must install Oracle XML DB if it is not installed. You must also configure network access control lists (ACLs) in the database before these packages can work as they did in earlier releases.

The following example first looks for any ACL currently assigned to `host_name`. If one is found, then the example grants `user_name` the `CONNECT` privilege in the ACL, only if that user does not have this privilege. If no ACL exists for `host_name`, then the example creates a new ACL called `ACL_name`, grants the `CONNECT` privilege to `user_name`, and assigns the ACL to `host_name`.

```
DECLARE
  acl_path  VARCHAR2(4000);
BEGIN
  SELECT acl INTO acl_path FROM dba_network_acls
   WHERE host = 'host_name' AND lower_port IS NULL AND upper_port IS NULL;
IF DBMS_NETWORK_ACL_ADMIN.CHECK_PRIVILEGE(acl_path, 
                                         'user_name','connect') IS NULL THEN
    DBMS_NETWORK_ACL_ADMIN.ADD_PRIVILEGE(acl_path,
                                         'user_name', TRUE, 'connect');
END IF;
EXCEPTION
  WHEN no_data_found THEN
    DBMS_NETWORK_ACL_ADMIN.CREATE_ACL('ACL_name.xml',
      'ACL description', 'user_name', TRUE, 'connect');
    DBMS_NETWORK_ACL_ADMIN.ASSIGN_ACL('ACL_name.xml','host_name');
END;
COMMIT;
```

Note:

The transaction must be committed for the changes to take effect.

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/authorization.htm#DBSEG40012) for more complicated situations, such as connecting some users to host A and other users to host B

### Enabling Oracle Database Vault and Revoking the DV\_PATCH\_ADMIN Role After Upgrading Oracle Database

If you use Oracle Database Vault, then you were instructed to disable it before upgrading your database. You must now:

- Enable Database Vault.
- Revoke the Database Vault `DV_PATCH_ADMIN` role for the `SYS` account.

See Also:

- ["About Upgrading Databases That Use Oracle Database Vault"](upgrade.md)
- The appendix about "Disabling and Enabling Oracle Database Vault" in [Oracle Database Vault Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23090/dvdisabl.htm#DVADM012)
- The section about "Manually Deploying Oracle Database Vault Administrator" in [Oracle Database Vault Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23090/dvca.htm#DVADM30032)
- The appendix about "Post-installation Oracle Database Vault Procedures" in [Oracle Database Vault Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23090/getting_started.htm#DVADM30031)

## Recommended Tasks to Complete After Upgrading Oracle Database

Performing the following tasks is recommended, but not required, after you have upgraded your database. These tasks are recommended regardless of whether you performed the upgrade manually or by using DBUA:

- Recommended Tasks to Perform After All Database Upgrades
- Recommended Tasks After Upgrading an Oracle Database 10g Release 1 (10.1) Database
- Recommended Tasks After Upgrading an Oracle Express Edition Database
- Recommended Tasks After Upgrading an Oracle RAC Database

### Recommended Tasks to Perform After All Database Upgrades

Performing the following tasks is recommended, but not required, after you have upgraded your database.

- Back Up the Database
- Reset Passwords to Enforce Case-Sensitivity
- Understand Changes with Oracle Grid Infrastructure
- Understand Oracle ASM and Oracle Grid Infrastructure Installation and Upgrade
- Add New Features as Appropriate
- Develop New Administrative Procedures as Needed
- Set Threshold Values for Tablespace Alerts
- Migrate From Rollback Segments to Automatic Undo Mode
- Configure Oracle Data Guard Broker
- Migrate Tables from the LONG Data Type to the LOB Data Type
- Test the Upgraded Production Database

#### Back Up the Database

Make sure you perform a full backup of the production database.

See Also:

[Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/toc.htm) for details about backing up a database

#### Reset Passwords to Enforce Case-Sensitivity

Starting with Oracle Database 11g Release 1 (11.1), you can enforce case sensitivity for passwords. For example, the password `hPP5620qr` fails if it is entered as `hpp5620QR` or `hPp5620Qr`. In previous releases, passwords were not case sensitive.

To take advantage of enforced case-sensitive passwords, you must reset the passwords of existing users during the database upgrade procedure. For new database instances, there are no additional tasks or management requirements. For upgraded databases, each user password must be reset with an `ALTER` `USER` statement.

Alternatively, you can change the default to make the password verifier case insensitive. For regular users, set the initialization parameter `sec_case_sensitive_logon` to `false`:

```
sql> alter system set sec_case_sensitive_logon=false;
```

For `sysdba` and `sysoper` users, you can generate a new `orapw` file using the new command line switch `ignorecase`.

Note:

If the default Oracle Database release 11g security settings are in place, then passwords must be at least eight characters, and passwords such as `welcome` and `oracle` are not allowed. See [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/guidelines.htm#DBSEG10005) for more information.

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/authentication.htm#DBSEG3225)

#### Understand Changes with Oracle Grid Infrastructure

Oracle Clusterware 11g release 2 and Oracle ASM 11g release 2 are both part of an Oracle Grid Infrastructure installation.

If Oracle Grid Infrastructure is installed for a single server, then it is deployed as an Oracle Restart installation with Oracle ASM. If Oracle Grid Infrastructure is installed for a cluster, then it is deployed as an Oracle Clusterware installation with Oracle ASM.

Oracle Restart enhances the availability of Oracle Database in a single-instance environment. If you install Oracle Restart, and there is a temporary failure of any part of the Oracle Database software stack, including the database, listener, and Oracle ASM instance, Oracle Restart automatically restarts the failed component. In addition, Oracle Restart starts all these components when the database host computer is restarted. The components are started in the proper order, taking into consideration the dependencies among components.

Oracle Clusterware is portable cluster software that allows clustering of single servers so that they cooperate as a single system. Oracle Clusterware also provides the required infrastructure for Oracle RAC. In addition, Oracle Clusterware enables the protection of any Oracle application or any other application within a cluster. In any case Oracle Clusterware is the intelligence in those systems that ensures required cooperation between the cluster nodes.

#### Understand Oracle ASM and Oracle Grid Infrastructure Installation and Upgrade

In earlier releases, Oracle ASM was installed as part of the Oracle Database installation. With Oracle Database 11g release 2 (11.2), Oracle ASM is installed when you install the grid infrastructure components and shares an Oracle home with Oracle Clusterware when installed in a cluster such as with Oracle RAC or with Oracle Restart on a standalone server.

If you have an existing Oracle ASM instance, you can either upgrade it during the installation of Oracle Grid Infrastructure, or you can upgrade it after the installation. However, be aware that several Oracle ASM features are disabled until you upgrade Oracle ASM, and Oracle Clusterware management of Oracle ASM does not function correctly until Oracle ASM is upgraded, because Oracle Clusterware only manages Oracle ASM when it is running in the grid infrastructure home. For this reason, Oracle recommends that if you do not upgrade Oracle ASM at the same time as you upgrade Oracle Clusterware, then you should upgrade Oracle ASM immediately afterward.

You can upgrade an Oracle ASM instance using Oracle ASM Configuration Assistant (ASMCA).

See Also:

- "Required Tasks After Oracle Grid Infrastructure Upgrades"
- "Preparing to Upgrade Oracle ASM"
- "Upgrading Oracle ASM"
- "Recommended Tasks After Oracle ASM Upgrades"
- "Tasks to Complete Only After Manually Upgrading Oracle Database"

In earlier releases, you could use Database Upgrade Assistant (DBUA) to upgrade either an Oracle Database, or Oracle ASM. That is no longer the case. You can only use DBUA to upgrade an Oracle Database instance. Use Oracle ASM Configuration Assistant (ASMCA) to upgrade Oracle ASM.

#### Add New Features as Appropriate

[Oracle Database New Features Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41360/toc.htm) describes many of the new features available in the new Oracle Database 11g release. Determine which of these new features can benefit the database and applications; then, develop a plan for using these features.

It is not necessary to make any immediate changes to begin using your new Oracle Database software. You might prefer to introduce these enhancements into your database and corresponding applications gradually.

[Chapter 5, "Upgrading Applications After Upgrading Oracle Database"](app.md) describes ways to enhance your applications so that you can take advantage of the features of the new Oracle Database 11g release. However, before you implement new features, test your applications and successfully run them with the upgraded database.

#### Develop New Administrative Procedures as Needed

After familiarizing yourself with the features of the new Oracle Database 11g release, review your database administration scripts and procedures to determine whether any changes are necessary.

Coordinate your changes to the database with the changes that are necessary for each application. For example, by enabling integrity constraints in the database, you might be able to remove some data checking from your applications.

#### Set Threshold Values for Tablespace Alerts

An upgraded Oracle Database 11g Release 1 (11.1) database has the Tablespace Alerts disabled (the thresholds are set to null). Tablespaces in the database that are candidates for monitoring must be identified and the appropriate threshold values set.

The default threshold values (for a newly created Oracle Database 11g Release 1 (11.1) database) are:

- 85% full warning
- 97% full critical

#### Migrate From Rollback Segments to Automatic Undo Mode

This section describes the steps to migrate the database that is being upgraded from using rollback segments (manual undo management) to automatic undo management.

Starting with Oracle Database 11g Release 1 (11.1), automatic undo management is the default undo space management mode. The `UNDO_MANAGEMENT` initialization parameter specifies which undo space management mode the system should use, as follows:

- If `UNDO_MANAGEMENT` = `AUTO` (or if `UNDO_MANAGEMENT` is not set), then the database instance starts in automatic undo management mode.
	A null `UNDO_MANAGEMENT` initialization parameter defaults to automatic undo management mode in Oracle Database 11g Release 1 (11.1), but it defaults to manual undo management mode in earlier releases. You must therefore use caution when upgrading a previous release to Oracle Database 11g.
- If `UNDO_MANAGEMENT` = `MANUAL`, then undo space is allocated externally as rollback segments.

If you are currently using rollback segments to manage undo space, then Oracle recommends that you migrate your Oracle Database 11g Release 1 (11.1) database to automatic undo management. This change requires that you first create an undo tablespace before opening a newly upgraded database to use automatic undo management. The required size of undo tablespace depends upon the system workload and Flashback requirements.

To migrate to automatic undo management, perform the following steps:

1. Set `UNDO_MANAGEMENT=MANUAL`.
2. Start the instance again and run through a standard business cycle to obtain a representative workload. Doing this to assess the workload and compute the size of the undo tablespace required for automatic undo management.
3. After the standard business cycle completes, run the following function to collect the undo tablespace size and help with the sizing of the undo tablespace (DBA privileges are required to run this function):
	```
	DECLARE
	   utbsiz_in_MB NUMBER;
	BEGIN
	   utbsiz_in_MB := DBMS_UNDO_ADV.RBU_MIGRATION;
	end;
	/
	```
	This function runs a PL/SQL procedure that provides information on how to size your new undo tablespace based on the configuration and usage of the rollback segments in your system. The function returns the sizing information directly.
4. Create an undo tablespace of the required size and turn on the automatic undo management by setting `UNDO_MANAGEMENT=AUTO` or by removing the parameter.
5. For Oracle RAC configurations, repeat these steps on all instances.

#### Configure Oracle Data Guard Broker

The Data Guard broker property `LocalListenerAddress` has been deprecated as of release 11.2.0.1 due to changes with broker communication and the redo transport setting.

The broker property `InitialConnectIdentifier` has been changed to `DGConnectIdentifier`. The value of `DGConnectIdentifier` is used for all Data Guard network traffic, all of the time. If you are upgrading an Oracle Database release 10g configuration, which requires you to first upgrade to Oracle Database 11g Release 1 (11.1), the value that exists for `InitialConnectIdentifier` is retained as the new value for `DGConnectIdentifier` for the database. When upgrading an Oracle RAC database, the database administrator must ensure that the value for the `InitialConnectIdentifier` property reaches all instances.

#### Migrate Tables from the LONG Data Type to the LOB Data Type

`LOB` data types (`BFILE`, `BLOB`, `CLOB`, and `NCLOB`) can provide many advantages over `LONG` data types. See [Oracle Database Concepts](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=CNCPT012) for information about the differences between `LONG` and `LOB` data types.

In Oracle9i Release 1 (9.0.1) and later, you can use the `ALTER TABLE` statement to change the data type of a `LONG` column to `CLOB` and that of a `LONG RAW` column to `BLOB`.

In the following example, the `LONG` column named `long_col` in table `long_tab` is changed to data type `CLOB`:

```
SQL> ALTER TABLE Long_tab MODIFY ( long_col CLOB );
```

After using this method to change `LONG` columns to LOBs, all the existing constraints and triggers on the table are still usable. However, all the indexes, including Domain indexes and Functional indexes, on all columns of the table become unusable and must be rebuilt using an `ALTER INDEX...REBUILD` statement. Also, the Domain indexes on the `LONG` column must be dropped before changing the `LONG` column to a LOB.

See Also:

[Oracle Database SecureFiles and Large Objects Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e18294/toc.htm) for information about modifying applications to use LOB data

#### Test the Upgraded Production Database

If you upgraded a test database to the new Oracle Database 11g release and then tested it, then you can now repeat those tests on the production database that you upgraded to the new Oracle Database 11g release. Compare the results, noting anomalies. Repeat the test upgrade as many times as necessary.

Test the newly upgraded production database with existing applications to verify that they operate properly with a new Oracle database. You also might test enhanced functions by adding available Oracle Database features. However, first ensure that the applications operate in the same manner as they did before the upgrade.

See Also:

[Chapter 5, "Upgrading Applications After Upgrading Oracle Database"](app.md) for more information on using applications with Oracle Database

### Recommended Tasks After Upgrading an Oracle Database 10g Release 1 (10.1) Database

Performing the following tasks is recommended, but not required, after you have upgraded from Oracle Database 10g Release 1 (10.1) or Oracle Database 10g Release 2 (10.2).

- Upgrade Change Data Capture
- Configure Secure HTTP
- Provide Anonymous Access to XML DB Repository Data Through HTTP

#### Upgrade Change Data Capture

Starting with Oracle Database 10g Release 2 (10.2), Asynchronous Change Data Capture (CDC) no longer requires the same operating system for source and target databases. This feature enables a heterogeneous CDC setup with different operating systems and Oracle Database releases, enabling asynchronous CDC to leverage any existing Oracle9i Release 2 (9.2) system as a source.

See Also:

[Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/cdc.htm#DWHSG016) for complete information on upgrading an Oracle9i Release 2 (9.2) or Oracle Database 10g Release 1 (10.1) database to the new Oracle Database 11g release with Change Data Capture, and supported configurations for the Distributed HotLog mode of Change Data Capture

#### Configure Secure HTTP

To configure HTTPS access to Oracle XML DB, follow the steps in this section to provide correct configuration information.

When a database is upgraded to Oracle Database 10g Release 2 (10.2) or later, the XML schema for the Oracle XML DB configuration file is automatically upgraded so that the Oracle XML DB configuration file (located at `/xdbconfig.xml` in the repository) can have two additional elements, `http2-port` and `http2-protocol`. These elements are not added to the Oracle XML DB configuration file by default during an upgrade. If you need support for HTTPS, then you must edit the configuration file to add these two new elements (see the XML schema for their exact locations), and to set the value of `http2-protocol` to `tcps`. The value of `http2-port` should be different from the value of `http-port`.

In addition to specifying the parameters `http2-port` and `http2-protocol` in the Oracle XML DB configuration file, you must configure the database and the listener to enable Oracle XML DB to use HTTPS. Additionally, if the steps in the following procedure were not performed before the upgrade, then you must perform them after the upgrade.

To enable Oracle XML DB to use HTTPS

1. Enable the HTTP listener and the database to use SSL
2. Enable launching of a TCPS dispatcher

For more information on how to do this, see [Oracle XML DB Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e23094/xdb22pro.htm#ADXDB2530).

Note:

If Oracle XML DB is not installed on the system, then you must install it during the upgrade procedure. Oracle XML DB is required to properly maintain the access control lists (ACLs).

#### Provide Anonymous Access to XML DB Repository Data Through HTTP

If anonymous access to XML DB repository data through HTTP is not required, then you are not required to perform this step. If anonymous access to XML DB repository data through HTTP is required, then you must provide correct configuration information, as described in this section. The administrator must carefully consider whether anonymous access is to be allowed, given the inherent security risks.

When a database is upgraded to Oracle Database 10g Release 2 (10.2) or later, the XML schema for the Oracle XML DB configuration file (located at `/xdbconfig.xml` in the repository) is automatically upgraded so that it can have an additional element, `allow-repository-anonymous-access`. This element is of Boolean type which means it can have a value of `true` or `false`. You can use this element to disallow unauthenticated access to your Oracle XML DB Repository data through HTTP even if you unlock the `ANONYMOUS` user account. The `allow-repository-anonymous-access` element is not added to the Oracle XML DB configuration file by default during an upgrade, but when this element is missing, it is interpreted as `false`.

Therefore, anonymous access to XML DB repository data through HTTP is disabled when you upgrade to Oracle Database 10g Release 2 (10.2) or later. If you want to have anonymous access to XML DB repository data through HTTP, then you must change the configuration file to set this new element to `true`, in addition to unlocking the `ANONYMOUS` user account.

Caution:

There is an inherent security risk associated with allowing unauthenticated access to the repository.

See Also:

[Oracle XML DB Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e23094/xdb22pro.htm#ADXDB2500) for more information about the `allow-repository-anonymous-access` element and configuring Oracle XML DB

## Tasks to Complete Only After Manually Upgrading Oracle Database

If you are performing a manual upgrade of Oracle Database rather than using DBUA, then you must perform additional tasks after your database is upgraded.

- Change Passwords for Oracle Supplied Accounts
- Create Password File with ORAPWD
- Migrate Your Initialization Parameter File to a Server Parameter File
- Upgrade Oracle Text
- Upgrade the Oracle Clusterware Configuration
- Adjust the Initialization Parameter File for the New Release
- Configure Enterprise Manager
- Set CLUSTER\_DATABASE Initialization Parameter For Oracle RAC

### Change Passwords for Oracle Supplied Accounts

Depending on the release from which you upgraded, there might be new Oracle supplied accounts. Oracle recommends that you lock all Oracle supplied accounts except for `SYS` and `SYSTEM`, and expire their passwords, thus requiring new passwords to be specified when the accounts are unlocked.

Note:

If the default Oracle Database 11g security settings are in place, then passwords must be at least eight characters, and passwords such as `welcome` and `oracle` are not allowed. See [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/guidelines.htm#DBSEG10005) for more information.

You can view the status of all accounts by issuing the following SQL statement:

```
SQL> SELECT username, account_status
         FROM dba_users
         ORDER BY username;
```

To lock and expire passwords, issue the following SQL statement:

```
SQL> ALTER USER username PASSWORD EXPIRE ACCOUNT LOCK;
```

### Create Password File with ORAPWD

If the `REMOTE_LOGIN_PASSWORDFILE` initialization parameter is set to either `exclusive` or `shared`, create a password file with `ORAPWD`.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/dba.htm#ADMIN11059) for more information about creating password files

### Migrate Your Initialization Parameter File to a Server Parameter File

If you are currently using a traditional initialization parameter file, then perform the following steps to migrate to a server parameter file:

1. If the initialization parameter file is located on a client computer, then transfer the file from the client computer to the server computer.
	Note:
	If you are using Oracle RAC, then you must combine all of your instance-specific initialization parameter files into a single initialization parameter file. Instructions for doing this, and other actions unique to using a server parameter file for cluster databases, are discussed in:
	- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/toc.htm)
	- The [Oracle Real Application Clusters Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=RIGEN) for your operating system
2. Create a server parameter file using the `CREATE SPFILE` statement. This statement reads the initialization parameter file to create a server parameter file. You are not required to start the database to issue a `CREATE SPFILE` statement.
3. Start up the instance using the newly-created server parameter file.

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/create.htm#ADMIN00202) for more information about creating server parameter files
- [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_6016.htm#SQLRF01315) for information about the `CREATE SPFILE` statement

### Upgrade Oracle Text

After an upgrade to the new Oracle Database 11g release, copy the following files from the previous Oracle home to the new Oracle home:

- Stemming user-dictionary files
- User-modified `KOREAN_MORPH_LEXER` dictionary files
- `USER_FILTER` executables

These files affect all databases installed in the given Oracle home.

You can obtain a list of these files by doing the following:

1. Looking at `$ORACLE_HOME/ctx/admin/ctxf102.txt`
2. Executing `$ORACLE_HOME/ctx/admin/ctxf102.sql` as database user `SYS`, `SYSTEM`, or `CTXSYS`

If your Oracle Text index uses `KOREAN_LEXER` which was deprecated in Oracle 9i and desupported in Oracle Database 10g Release 2 (10.2), see Note 300172.1 on My Oracle Support for further information on manual migration from `KOREAN_LEXER` to `KOREAN_MORPH_LEXER`.

See Also:

- [Oracle Text Reference](https://docs.oracle.com/cd/E11882_01/text.112/e24436/cdatadic.htm#CCREF1901) for more information about these files
- [Oracle Text Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/text.112/e24435/cmigrt.htm#CCAPP2001) for information about upgrading your applications from previous releases of Oracle Text
- My Oracle Support at `https://support.oracle.com`

### Upgrade the Oracle Clusterware Configuration

If you are using Oracle Clusterware, then you must upgrade the Oracle Clusterware keys for the database.

Run `srvctl` for release 11.2.0.3 to upgrade the database. For example:

```
%11.2.0.3_ORACLE_HOME/bin/srvctl upgrade database -d <name> -o 11.2.0.3_ORACLE_HOME
```

Caution:

By default, any named user may create a server pool. To restrict the operating system users that have this privilege, Oracle strongly recommends that you add specific users to the CRS Administrators list.

See Also: [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/admin.htm#CWADD91105) for more information about adding users to the CRS Administrators list

### Adjust the Initialization Parameter File for the New Release

Each release of Oracle Database introduces new initialization parameters, deprecates some initialization parameters, and makes some initialization parameters obsolete. You must adjust the parameter file to account for these changes and to take advantage of new initialization parameters that might be beneficial to your system. Additionally, when you perform a manual upgrade without using DBUA, the `tnsnames.ora` file is not automatically populated with new configuration information and settings. Therefore, you may need to manually update `tnsnames.ora` and adjust `local_listener` and `remote_listener` parameter references if these need to be resolved.

See Also:

- The "What's New in Oracle Database Reference" section of [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/toc.htm) for a list of the new initialization parameters in the new Oracle Database 11g release, and for information about each parameter
- [Appendix A, "Behavior Changes After Upgrading Oracle Database"](changes.md) for lists of obsolete and deprecated initialization parameters in the new Oracle Database 11g release

#### Setting the COMPATIBLE Initialization Parameter

The `COMPATIBLE` initialization parameter controls the compatibility level of your database. When you are certain that you no longer need the ability to downgrade your database to its original release, set the `COMPATIBLE` initialization parameter based on the compatibility level you want for your new database.

Complete the following steps to set the `COMPATIBLE` initialization parameter to a higher value:

1. Perform a backup of your database before you raise the `COMPATIBLE` initialization parameter (optional).
	Raising the `COMPATIBLE` initialization parameter might cause your database to become incompatible with earlier releases of Oracle Database, and a backup ensures that you can return to the earlier release if necessary.
	See Also:
	[Oracle Database Backup and Recovery User's Guide](https://docs.oracle.com/cd/E11882_01/backup.112/e10642/toc.htm) for more information about performing a backup
2. If you are using a server parameter file, then complete the following steps:
	1. Update the server parameter file to set or change the value of the `COMPATIBLE` initialization parameter.
		For example, to set the `COMPATIBLE` initialization parameter to `11.0.0`, enter the following statement:
		```
		SQL> ALTER SYSTEM SET COMPATIBLE = '11.0.0' SCOPE=SPFILE;
		```
		2. Shut down and restart the instance.
	Note:
	When upgrading systems with HARD-compliant storage (Hardware Assisted Resilient Data), consider the following:
	- If the `COMPATIBLE` parameter is set to a release number earlier than 11.0.0, then you cannot locate the server parameter file (`SPFILE`) on HARD storage.
	- If the `COMPATIBLE` parameter is set to 11.0.0, then you can optionally locate the server parameter file on HARD storage.
	Because the default `SPFILE` location (ORACLE\_HOME/dbs) might not be on a HARD-compliant storage system, it is likely you must provide a parameter file that specifies the location of the `SPFILE`.
	See Also:
	[Oracle Database High Availability Overview](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=HAOVW003) or [Oracle Database Concepts](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=CNCPT1291) for more information on HARD storage
3. If you are using an initialization parameter file, then complete the following steps:
	1. Shut down the instance if it is running:
		```
		SQL> SHUTDOWN IMMEDIATE
		```
		2. Edit the initialization parameter file to set or change the value of the `COMPATIBLE` initialization parameter.
		For example, to set the `COMPATIBLE` initialization parameter to `11.0.0`, enter the following in the initialization parameter file:
		```
		COMPATIBLE = 11.0.0
		```
		3. Start the instance using `STARTUP`.

Note:

If you are using an ASM disk group, then the diskgroup's compatibility attribute must match or be lower than that of the database compatibility parameter in `init.ora`.

#### Configuring tnsnames.ora and Listener Parameters

After performing a manual upgrade, you may need to adjust `local_listener` and `remote_listener` parameter references if they need to be resolved in `tnsnames.ora`. DBUA handles changes to network naming and listeners during automatic upgrades, but during a manual upgrade, `tnsnames.ora` is not changed, nor are the listeners.

See Also:

- Local Naming Parameters (tnsnames.ora) in [Oracle Database Net Services Reference](https://docs.oracle.com/cd/E11882_01/network.112/e10835/tnsnames.htm#NETRF007)
- "Configuring the tnsnames.ora File After Installation" in [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/naming.htm#NETAG259)
- "Configuring and Administering Oracle Net Listener" in [Oracle Database Net Services Administrator's Guide for information on registering information with a local listener and a remote listener](https://docs.oracle.com/cd/E11882_01/network.112/e41945/listenercfg.htm#NETAG010)
- "Net Service Names (tnsnames.ora File)" in [Oracle Real Application Clusters Installation Guide](https://docs.oracle.com/cd/E11882_01/install.112/e48195/undrstnd.htm#RIWIN610) for Windows
- "Net Service Names (tnsnames.ora File)" in [Oracle Real Application Clusters Installation Guide for Linux and UNIX](https://docs.oracle.com/cd/E11882_01/install.112/e41962/undrstnd.htm#RILIN610)

### Configure Enterprise Manager

If you are not yet using Oracle Enterprise Manager to manage your database, then install and configure Enterprise Manager Database Control.

If your database is being managed by Oracle Enterprise Manager Database Control or Oracle Enterprise Manager Grid Control, then use the following command to update the configuration:

```
emca -upgrade (db | asm | db_asm) [-cluster] [-silent] [parameters]
```

You must run this from the Oracle home of the new Oracle Database 11g release. When prompted, provide the Oracle home from which the configuration is being upgraded.

You can also configure Enterprise Manager using DBCA. Select the Configure Database Options option, and then select the Enterprise Manager Repository option.

See Also:

[Oracle Enterprise Manager Advanced Configuration](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=OEMCG0116)

### Set CLUSTER\_DATABASE Initialization Parameter For Oracle RAC

For upgrades of Oracle RAC databases, in ["Preparing the New Oracle Home for a Manual Upgrade"](upgrade.md), you were instructed to set the `CLUSTER_DATABASE` initialization parameter to `false` before upgrading a cluster database. Now that the upgrade is finished, you must set this parameter to `true`.

## Required Tasks After Oracle Grid Infrastructure Upgrades

Oracle ASM release 11.2 and later are included as part of an Oracle Grid Infrastructure installation.

If you upgrade Oracle Clusterware and Oracle ASM for a cluster, then Oracle Clusterware and Oracle ASM are both located in the same home, which is referred to as grid home. You can have one installation owner that owns all Oracle software installations, or you can use role-allocated owners, in which case you use a separate software owner for the grid infrastructure installation, and separate software owners for one or more Oracle Database installations.

The following tasks are required after an upgrade from Oracle ASM, performed as a separate installation procedure, to an Oracle ASM installation as part of the Oracle Grid Infrastructure:

- Using Environment Variables for Grid Infrastructure Installations
- Upgrading An Earlier Release of Oracle ASM to Oracle Grid Infrastructure

See Also:

[Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=CWGEN) for your platform for more information about role-allocated installation owners

### Using Environment Variables for Grid Infrastructure Installations

If your operating system is Linux or UNIX, then you may need to change environment variable settings after performing an upgrade.

If you use a single Oracle installation owner for all installations, then be aware that you should change environment variables such as `ORACLE_HOME` either to an Oracle Database home, or to the grid home, depending on whether you are administering an Oracle Database instance as part of database administration, or administering an Oracle ASM instance as part of storage administration.

If you use role-allocated Oracle installation owners, so that you have a separate owner for the Oracle Grid Infrastructure (Oracle Clusterware and Oracle ASM) software, then set the following environment variables for the grid infrastructure installation owner so that they point to the directories of the Oracle ASM home in the grid infrastructure home:

- `ORACLE_HOME`
- `PATH`

Also, check that your `oratab` file and any client scripts for Oracle ASM that set the value of `ORACLE_HOME` point to the Oracle ASM home in the grid infrastructure home.

Note:

If you are upgrading a clustered Oracle ASM installation to an Oracle Grid Infrastructure for a cluster installation, then perform these checks on all cluster member nodes.

See Also:

Your operating system-specific Oracle Database installation documents for information about setting other important environment variables on your operating system.

### Upgrading An Earlier Release of Oracle ASM to Oracle Grid Infrastructure

In earlier releases, Oracle ASM was installed as part of the Oracle Database installation. With Oracle Database 11g Release 2 (11.2), Oracle ASM is installed when you install the grid infrastructure components. If you install Oracle Grid Infrastructure for a cluster, then it is part of the grid home, with Oracle Clusterware. If you install Oracle Grid Infrastructure for a single server, then Oracle ASM shares an Oracle home with Oracle Restart.

If you want to upgrade an existing Oracle ASM, then you must upgrade Oracle ASM by running an Oracle Grid Infrastructure upgrade. If you do not have Oracle ASM installed and you want to use Oracle ASM as your storage option, then you must complete an Oracle Grid Infrastructure installation before you start your Oracle Database installation.

See Also:

[Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=CWGEN) or [Oracle Database Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for your platform

Oracle ASM Configuration Assistant (ASMCA) supports installing and configuring Oracle ASM instances, disk groups, volumes, and Oracle ASM Cluster File System (Oracle ACFS). Additionally, you can use the ASMCA command-line interface as a non-GUI utility (command name `asmca`).

You can use the `asmca` command to complete the upgrade separately. However, you must run `asmca` soon after you upgrade Oracle Clusterware, as Oracle ASM management tools such as `srvctl` do not work until Oracle ASM is upgraded.

Note:

For cluster upgrades, ASMCA performs a rolling upgrade only if the earlier release of Oracle ASM is either 11.1.0.6 or 11.1.0.7. Otherwise, ASMCA performs a normal upgrade, in which case ASMCA brings down all Oracle ASM instances on all nodes of the cluster, and then brings them all up in the new grid infrastructure home.

#### Preparing to Upgrade Oracle ASM

Note the following information if you intend to perform rolling upgrades of Oracle ASM:

- You cannot change the owner of a home as part of an upgrade. For example, if you plan to install Oracle Grid Infrastructure as the user `grid`, then the home of an existing Oracle ASM must be owned by the user `grid` before you upgrade it.
- The active release of Oracle Clusterware must be 11g release 2 (11.2). To determine the active release, enter the following command:
	```
	$ crsctl query crs activeversion
	```
	See Also:
	[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/admin.htm#CWADD91105) for more information about `crsctl` and adding users to the CRS Administrators list
- You can upgrade a single instance Oracle ASM installation to a clustered Oracle ASM installation. However, you can only upgrade an existing single instance Oracle ASM installation if you run the installation from the node on which the Oracle ASM installation is installed. You cannot upgrade a single instance Oracle ASM installation on a remote node.
- You must ensure that any rebalance operations on your existing Oracle ASM installation are completed before starting the upgrade process.
- During the upgrade process, you alter the Oracle ASM instances to an upgrade state. Because this upgrade state limits Oracle ASM operations, you should complete the upgrade process soon after you begin. The following are the operations allowed when an Oracle ASM instance is in the upgrade state:
	- Diskgroup mounts and dismounts
		- Opening, closing, resizing, or deleting database files
		- Recovering instances
		- Queries of fixed views and packages: Users are allowed to query fixed views and run anonymous PL/SQL blocks using fixed packages, such as `dbms_diskgroup`)

### Upgrading Oracle ASM

The procedure in this section describes how to upgrade Oracle ASM using Oracle ASM Configuration Assistant (ASMCA).

To upgrade Oracle ASM

1. Log on as the installation owner of the Oracle Grid Infrastructure installation.
2. If you are upgrading on a cluster, then on the node you plan to start the upgrade, set the environment variable `ASMCA_ROLLING_UPGRADE` as `true`. For example:
	```
	$ export ASMCA_ROLLING_UPGRADE=true
	```
3. From the Oracle Grid Infrastructure 11g release 2 (11.2) home, start ASMCA. For example:
	```
	$ cd /u01/11.2/grid/bin
	$ ./asmca
	```
4. Select Upgrade.
	The Oracle ASM Configuration Assistant upgrades Oracle ASM in succession for all nodes in the cluster.

See Also:

[Oracle Database Storage Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/toc.htm) for additional information about preparing an upgrade plan for Oracle ASM, and for starting, completing, and stopping Oracle ASM upgrades

## Required Tasks After Oracle ASM Upgrades

This section contains the tasks that are required after an Oracle ASM Upgrade, and additional considerations.

- Set Environment Variables
- Single-Instance Oracle ASM Upgrade
- Cluster Oracle ASM Upgrade
- Additional Considerations After Oracle ASM Upgrades

### Set Environment Variables

If your operating system is Linux or UNIX, then make sure that the following environment variables point to the directories of the new Oracle Database 11g release:

- `ORACLE_HOME`
- `PATH`

Also check that your `oratab` file and any client scripts that set the value of `ORACLE_HOME` point to the Oracle home of the new Oracle Database 11g release.

Note:

The `ORACLE_HOME`, `PATH`, and `oratab` checks are required only if you upgrade manually. DBUA automatically points `oratab` to the new Oracle home. Client scripts must be checked no matter how you upgrade.

If you are upgrading a clustered Oracle ASM, then perform these checks on all nodes in which this clustered Oracle ASM has instances configured.

See Also:

Your operating system-specific Oracle Database installation documents for information about setting other important environment variables on your operating system.

### Single-Instance Oracle ASM Upgrade

The following procedure assumes that Oracle ASM is installed in Oracle home 1 (`OH1`) and the operating system user is `orauser`.

To perform a single-instance upgrade of Oracle ASM

1. As `orauser`, upgrade Oracle ASM to release 11.2 using OUI and ASMCA. The new Oracle ASM release 11.2 runs in the grid infrastructure home. Oracle ASM should still be running as `orauser`.
2. As `orauser`, bring down the Oracle ASM instance and the listener.
3. As `root`, run `/etc/init.d/init.cssd stop` to stop CSS.
4. As a new user (`asmuser`), install 11.2 in a third Oracle home (`OH3`). This should be a software-only installation.
5. As `root`, run `localconfig reset` from `OH3`.
6. Update `/etc/oratab` so that `OH3` is the Oracle home with the `+ASM` entry.
7. Copy `listener.ora`, `sqlnet.ora`, and `tnsnames.ora` from `OH2`.
8. Run EMCP to change the Oracle ASM instance path and `connect-string` role.
9. Make sure the disks are owned by `asmuser` and by OSASM for Oracle ASM. They should also have the `O660` permission set.
10. As `asmuser`, start the listener.
11. As `asmuser`, start Oracle ASM (connect as `SYSASM`).
12. Run the command, `GRANT sysasm TO sys`.

### Cluster Oracle ASM Upgrade

To perform an upgrade of Oracle ASM on a cluster

1. As `orauser`, upgrade Oracle ASM to release 11.2 using OUI and ASMCA. The new Oracle ASM release 11.2 should be running in a new Oracle home 2 (`OH2`). Oracle ASM should still be running as `orauser`.
2. Bring down the Oracle ASM and Listener resources from CRS home.
3. As a new user (`crs` for example), install 11.2 into a third Oracle home (`OH3`) to match that of the Grid Infrastructure home. This must be a software-only installation.
4. From CRS home, run:
	```
	srvctl remove listener -n node_name
	srvctl add listener -n node_name -o OH3
	srvctl modify asm -n node_name -i ASM_instance_name -o ORACLE_HOME_path
	```
	Caution:
	By default, any named user may create a server pool. To restrict the operating system users that have this privilege, Oracle strongly recommends that you add specific users to the CRS Administrators list.
	See Also: [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/admin.htm#CWADD91105) for more information about adding users to the CRS Administrators list
5. Update `/etc/oratab` so that `OH3` is the Oracle home with the `+ASM` entry.
6. Copy `listener.ora`, `sqlnet.ora`, and `tnsnames.ora` from `OH2`.
7. Run EMCP to change the Oracle ASM instance path and `connect-string` role.
8. Make sure the disks are owned by `asmuser` and by OSASM for Oracle ASM. They should also have the `O660` permission set.
9. Start Oracle ASM and Listener resources from the new Oracle ASM 11g ORACLE\_HOME or the new Oracle Database 11g ORACLE\_HOME.
10. Run the command, `GRANT sysasm TO sys`.

If you have clustered Oracle ASM instances, then you also have the option of performing a rolling Oracle ASM upgrade. A rolling upgrade enables you to independently upgrade or patch Oracle ASM nodes without affecting database availability, thus providing greater uptime.

See Also:

[Oracle Database Storage Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asminst.htm#OSTMG02400) for more information on rolling Oracle ASM upgrades

### Additional Considerations After Oracle ASM Upgrades

If you separate the operating system user ownership of the Oracle Grid Infrastructure binaries and the Oracle Database installation owners of one or more databases, then you must migrate the operating system user of an upgraded Oracle ASM or database home as described in "Role-Allocated Software Owners and Database Upgrade After Oracle ASM Upgrade".

#### Role-Allocated Software Owners and Database Upgrade After Oracle ASM Upgrade

If you are migrating from one software binary owner (such as `oracle`) to multiple role-allocated software owner user accounts (such as `grid`, `oracle1`, `oracle2`), then change the owner of the existing Oracle ASM installation owner to the installation owner that you plan to use for the Oracle Grid Infrastructure installation.

There are three scenarios to consider:

- Keeping the Existing User as the Oracle ASM Operating System User
- Changing the Operating System User for Single-Instance Oracle ASM
- Changing the Operating System User for an Oracle RAC Database

See Also:

[Oracle Database Storage Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmdiskgrps.htm#OSTMG02700) for information on making an Oracle ASM disk group compatible with Oracle Database 10g and Oracle Database 11g, and for additional information about Oracle ASM upgrades

#### Keeping the Existing User as the Oracle ASM Operating System User

If you are using the same operating system user for your Oracle Grid Infrastructure installation that you used for your existing Oracle ASM installation, then run Oracle Universal Installer (OUI) to perform a grid infrastructure installation, and select the upgrade option. OUI automatically upgrades your existing Oracle ASM installation from the prior release to 11g Release 2 (11.2) in the Oracle Grid Infrastructure home.

#### Changing the Operating System User for Single-Instance Oracle ASM

Consider your earlier release Oracle ASM installation is installed in Oracle home 4 (`OH4`) and currently running `oracle` as the operating system user, and you want to change the Oracle ASM operating system user to `grid`. This is useful if you have two databases using Oracle ASM, and you had installed Oracle ASM with an installation owner that is the same as that for the existing databases, and you want to change the operating system installation owner of Oracle ASM to enable separate databases to run as separate operating system users, where neither Oracle Database installation owner has Oracle Grid Infrastructure binary ownership.

#### Changing the Operating System User for an Oracle RAC Database

There may be scenarios where you must change the operating system user for an Oracle RAC database. For example, if your earlier release database is installed in Oracle home 4 (`OH4`) and currently running `oracle` as the operating system user, then you should consider changing the Oracle ASM operating system user to `grid`. Changing the operating system user of Oracle ASM enables separate databases to run as separate operating system users, where no Oracle Database installation owner has grid infrastructure binary ownership.

## Recommended Tasks After Oracle ASM Upgrades

Performing the following tasks is recommended, but not required, after you have upgraded Oracle ASM:

- Reset Oracle ASM Passwords to Enforce Case-Sensitivity
- Advance the Oracle ASM and Oracle Database Disk Group Compatibility
- Set Up Oracle ASM Preferred Read Failure Groups

You should also consider performing the following tasks, discussed earlier in this chapter:

- "Add New Features as Appropriate"
- "Develop New Administrative Procedures as Needed"

### Reset Oracle ASM Passwords to Enforce Case-Sensitivity

Starting with Oracle Database 11g Release 1 (11.1), you can enforce case sensitivity for passwords. For example, the password `hPP5620qr` fails if it is entered as `hpp5620QR` or `hPp5620Qr`. In previous releases, passwords were not case sensitive.

To take advantage of enforced case-sensitive passwords, you must reset the passwords of existing users during the database upgrade procedure. For new Oracle Oracle ASM instances, there are no additional tasks or management requirements. For upgraded Oracle ASM instances, each user password must be reset with an `ALTER` `USER` statement.

Note:

If the default Oracle Database 11g security settings are in place, then passwords must be at least eight characters, and passwords such as `welcome` and `oracle` are not allowed. See [Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/guidelines.htm#DBSEG10005) for more information.

See Also:

[Oracle Database Security Guide](https://docs.oracle.com/cd/E11882_01/network.112/e36292/authentication.htm#DBSEG3225)

### Advance the Oracle ASM and Oracle Database Disk Group Compatibility

Starting with Oracle Database 11g Release 1 (11.1), you can advance the Oracle Database and the Oracle ASM disk group compatibility settings across software versions.

Caution:

If you advance the `COMPATIBLE.RDBMS` attribute, then you cannot revert to the previous setting. Therefore, before advancing the `COMPATIBLE.RDBMS` attribute, ensure that the values for the `COMPATIBLE` initialization parameter for all of the databases that use the disk group are set to at least the new setting for `COMPATIBLE.RDBMS` before you advance the attribute value.

Advancing compatibility enables new features only available in the new release. However, doing so makes the disk group incompatible with older releases of the software. Note that advancing the on-disk compatibility is an irreversible operation.

You use the `compatible.rdbms` and `compatible.asm` attributes to specify the minimum software release required by the database instance and the Oracle ASM instance, respectively, to access the disk group. For example, the following `ALTER DISKGROUP` statement advances the Oracle ASM compatibility of the disk group `asmdg2`:

```
ALTER DISKGROUP asmdg2 SET ATTRIBUTE 'compatible.asm' = '11.1'
```

In this case, the disk group can be managed only by Oracle ASM software of release 11.1 or higher, while any database client of release 10.1 or higher can use the disk group.

See Also:

[Oracle Database Storage Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmdiskgrps.htm#OSTMG10045) for complete information about disk group compatibility, and [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_1007.htm#SQLRF01113) for more information about the disk group compatibility attributes on the `ALTER DISKGROUP` and `CREATE DISKGROUP` statements

### Set Up Oracle ASM Preferred Read Failure Groups

Oracle ASM administrators can specify some disks to be preferred over others for read I/O operations. When Oracle ASM preferred read failure groups are defined, Oracle ASM can read from the extent that is closest to it, rather than always reading the primary copy.

See Also:

- [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/toc.htm) for information about specifying failure groups settings in an extended cluster
- [Oracle Database Storage Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/toc.htm) for complete information about Oracle ASM preferred read failure groups, and specifying the new `ASM_PREFERRED_READ_FAILURE_GROUPS` initialization parameter to list failure group names that contain the preferred read disks for each node in a cluster
- [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams013.htm#REFRN10279) for the `ASM_PREFERRED_READ_FAILURE_GROUPS` initialization parameter