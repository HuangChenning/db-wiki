---
title: Oracle Real Application Clusters Postinstallation Procedures
book: Real Application Clusters Installation Guide for Microsoft Windows x64 (64-Bit)
doc_id: E48195-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e48195/postinst.htm
tags:
  - oracle
  - 11g
  - real-application-clusters-installation-guide-for-microsoft-windows-x64-64-bit
---

## 4 Oracle Real Application Clusters Postinstallation Procedures

This chapter describes how to complete the postinstallation tasks after you have installed the Oracle Database 11g release 2 (11.2) with Oracle Real Application Clusters (Oracle RAC) software. This chapter contains the following topics:

Note:

This chapter describes only basic configurations. See also:
- [Oracle Database Platform Guide for Microsoft Windows](https://docs.oracle.com/cd/E11882_01/win.112/e10845/toc.htm) and the product administration and tuning guides for more detailed configuration and tuning information
- [Oracle Database Installation Guide for Microsoft Windows](https://docs.oracle.com/cd/E11882_01/install.112/e47798/postcfg.htm#NTDBI004) for additional postinstallation configuration information

## 4.1 Required Postinstallation Tasks

You must perform the following tasks after completing your installation:

- Determine If Any Patches Are Required For Your New Software
- Types of Patches Available for Oracle Software
- Downloading and Installing Patch Updates
- Configuring Exceptions for the Windows Firewall
- Configuring Oracle Products
- Configuring Storage for External Tables, Shared Files, or Directory Objects

### 4.1.1 Determine If Any Patches Are Required For Your New Software

After installing the Oracle software, sometimes you will need to apply one or more patches to enable certain software features to work correctly. To determine if any patches are required for your system, review the [Oracle Database Readme](https://docs.oracle.com/cd/E11882_01/readmes.112/e41331/toc.htm) and the Oracle Database Release Notes 11g Release 2 (11.2.0.3) for Microsoft Windows.

See Also:

"Required Patches for Earlier Oracle Database Releases or Databases Being Upgraded" for information about patches required for Oracle Database software release 11.1 or earlier

### 4.1.2 Types of Patches Available for Oracle Software

On a regular basis Oracle provides patch sets that include generic and port specific fixes encountered by customers since the base product was released. Patch sets increment the 4th digit of the version number e.g. 10.2.0.1.0 to 10.2.0.4.0, these patch sets are fully regression tested in the same way that the base release is (i.e. 10.2.0.1.0). Customers are encouraged to apply these fixes.

If a customer encounters a critical problem that requires a fix prior to the next patch set becoming available, they can request that a one off fix is made available on top of the latest patch set. This delivery mechanism is similar to the Microsoft Hot Fixes and is known as an Oracle patch set exception (or interim patch). Unlike Unix platforms these patch set exceptions are delivered in a patch set exception bundle (cumulative patch bundle), which includes all fixes since the current patch set. For example, bug 12393432 is a patch set exception bundle, Patch 12, for Oracle Database release 11.2.0.1 for Microsoft Windows (x64). You should always apply the latest patch bundle available for your release.

The patch set exception bundles also include the fixes for the CPU (Critical Patch Update), DST (Daylight Saving Time), PSU (Patch Set Update) and Recommended Patch Bundles. It is not required to have previous security patches applied before applying the patch set exception bundle. However, you must be on the stated patch set level for a given product home before applying the patch set exception bundle for that release.

See Also:

[Oracle Database High Availability Overview](https://docs.oracle.com/cd/E11882_01/server.112/e17157/planned.htm#HAOVW156) for more information about the various types of patches.

### 4.1.3 Downloading and Installing Patch Updates

Go the My Oracle Support web site for required patch updates for your installation.

Note:

Browsers require an Adobe Flash plug-in, version 9.0.115 or later to use My Oracle Support. Check your browser for the correct version of the Flash player by going to the Adobe Flash checker page, and installing the latest version of Adobe Flash.

If you do not have Adobe Flash installed, then download the latest version of the Flash Player from the Adobe web site:

```
http://www.adobe.com/go/getflashplayer
```

To download required patch set updates:

1. Use a web browser to view the My Oracle Support web site:
	`https://support.oracle.com`
2. Log in to My Oracle Support.
	Note:
	If you are not a My Oracle Support registered user, then click Register for My Oracle Support and register.
3. On the main My Oracle Support page, click the Patches & Updates tab.
4. On the left side of the page, in the Patching Quick Links section, under the heading Oracle Server / Tools, click Latest Patchsets.
	A new browser window or tab is opened, displaying the Quick Links page.
5. In the Patch Sets for Product Bundles section, cursor over the link for Oracle Database. In the floating list that appears, move your cursor to highlight your operating system, for example Microsoft Windows x64 (64-bit). In the drill-down list that appears, click the desired patch set version, for example, 11.2.0.2.
	A Search Results page appears, with the selected patch set displayed at the bottom. Patch sets for Oracle databases are identified in the Description column as Oracle Database Family:Patchset x.x.x.x PATCH SET FOR ORACLE DATABASE SERVER.
	1. Click the number of the desired patch set in the first column of the search results. On the patch set information page, click View Readme to view the Patch Set Notes, also called the README file, for that patch. The README page contains information about the patch set and how to apply the patches to your installation.
		2. To download the patch to your local file system, click the Download button on the patch set information page.
6. To locate all the available patches instead of patch sets, use your browser navigation buttons to return to the Search Results page. In the middle of the Search Results page, in the Patch Type action list, change the current setting to Patch. Below the search fields, click the Go button.
	The previous search is repeated, but this time, a list of all available patches is displayed instead of a list of patch sets. To access the patch information, perform the tasks listed in Step 5.a. and Step 5.b.
7. After you have downloaded the patch and transferred it to your server, use the UNZIP utility provided with Oracle Database 11g release 2 (11.2) to uncompress the Oracle patch updates. The UNZIP utility is located in the `Oracle_home\bin` directory.

Note:

You can click the link on the bottom of the patch set information page to obtain an UNZIP utility for most operating systems.

### 4.1.4 Configuring Exceptions for the Windows Firewall

If the Windows Firewall feature is enabled on one or more of the nodes in your cluster, then virtually all TCP network ports are blocked to incoming connections. As a result, any Oracle product that listens for incoming connections on a TCP port does not receive any of those connection requests and the clients making those connection requests report errors.

If the Windows Firewall feature is enabled on one or more nodes of your Oracle RAC cluster, you must create exceptions for Oracle RAC applications and ports as described in [Oracle Grid Infrastructure Installation Guide for Microsoft Windows x64 (64-Bit)](https://docs.oracle.com/cd/E11882_01/install.112/e48194/toc.htm).

### 4.1.5 Configuring Oracle Products

Many Oracle products and options must be configured before you use them for the first time. Before using individual Oracle Database 11g release 2 (11.2) products or options, refer to the appropriate manual in the product documentation library, which is available in the `DOC` directory on the Oracle Database installation media, or on the Oracle Technology Network (OTN) web site at:

`http://www.oracle.com/technetwork/indexes/documentation/`

#### 4.1.5.1 Configuring Oracle Database Vault

If you installed Oracle Database Vault during the Oracle RAC installation, then you must register Oracle Database Vault with the database and create database user accounts.

See Also:

[Oracle Database Vault Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23090/dvca.htm#DVADM022) for more information about configuring Oracle Database Vault after installation

#### 4.1.5.2 Configuring Oracle Database Security Settings

To enable or disable the database security configuration after installation, you must use command-line Oracle Database Configuration Assistant (DBCA) options. By design, the DBCA graphical user interface (GUI) does not have the option to enable or disable secure configuration. For example, to enable the security settings after installation, you would use a command of the following form, where `myRACdb1.example.com` is the either the name of the local database instance or the `DB_UNIQUE_NAME`:

```
dbca –configureDatabase –sourceDB myRACdb1.example.com -SID
–enableSecurityConfiguration true
```

See Also:

[Oracle Database Installation Guide for Microsoft Windows](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=NTDBI003) for more information about enabling and disabling the database security option

### 4.1.6 Configuring Storage for External Tables, Shared Files, or Directory Objects

If your Oracle RAC database uses files that are external to the database, then the external files should be located on shared storage that is accessible to all nodes. Each node should use the same mount point to access the file. Acceptable shared file systems include Database File System (DBFS), Oracle ASM Cluster File System (Oracle ACFS), Oracle Cluster File System (OCFS) for Windows, or a supported network file system (NFS).

The database directory object used to write and read files external to the database must point to a shared storage location, and each node must use the same mount point for the same shared storage location. For example, each node might have a directory object called `DPUMP` for the mount point `C:\app\acfsmounts\dpump`, which accesses Oracle ACFS shared storage.

Note:

There is no checking of the contents of the external files or directory object specified as part of the external table to ensure that the directory contents are consistent on each node. To avoid unpredictable results, you must ensure that the same file is accessed from all nodes, or that the same file is used on all nodes.

## 4.2 Recommended Postinstallation Tasks

Oracle recommends that you complete the following tasks after completing an Oracle RAC installation:

- Setting the Oracle User Environment Variables
- Recompiling All PL/SQL modules
- Setting Up User Accounts
- Configuring Oracle Administration Assistant for Windows
- Using Oracle9i Database Language and Definition Files with Oracle Database 11g
- Logging in to Oracle Enterprise Manager Database Control

### 4.2.1 Setting the Oracle User Environment Variables

Unlike on other platforms, you should not set `ORACLE_HOME` as a fixed environment variable when running Oracle on Windows operating systems. This is because the Oracle software determines where executable files reside at run time.

When you invoke an Oracle executable program on Windows, for example `sqlplus.exe`, the `ORACLE_HOME`, `ORACLE_BASE`, and `ORACLE_SID` variables are determined by the `PATH` environment variable and the location of the executable program (which Oracle home it resides in). If you want to use SQL\*Plus to manage a different database or Oracle ASM instance, then you can click the Windows Start button, select the correct Oracle Home for the instance you want to manage, and then select the SQL\*Plus utility.

You can use Oracle Universal Installer (OUI) to specify an Oracle home as the default Oracle home and update the `PATH` environment variable to point to that Oracle home. Refer to [Section 7.3, "Working with Multiple Oracle Home Directories on Windows"](undrstnd.md) for detailed instructions on how to change the default Oracle home.

### 4.2.2 Recompiling All PL/SQL modules

Oracle recommends that you run the `utlrp.sql` script after creating or upgrading a database. This script recompiles all PL/SQL modules that might be in an invalid state, including packages, procedures, and types. This is an optional step, but Oracle recommends that you do it immediately following installation, not at a later date.

1. Complete setting up the Oracle software owner user account environment (for example, `oracle`), as described in "Setting the Oracle User Environment Variables".
2. Start SQL\*Plus, as follows:
	Click Start, select Programs (or All Programs), then Oracle - HOME\_NAME, then Application Development, and then SQL\*Plus.
3. Run the `utlrp.sql` script, where `Oracle_home` is the Oracle home path:
	```
	SQL> @Oracle_home\rdbms\admin\utlrp.sql
	```

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/dba.htm#ADMIN00102) for information about connecting to the database using SQL\*Plus

### 4.2.3 Setting Up User Accounts

For information about setting up additional optional user accounts, see [Oracle Database Platform Guide for Microsoft Windows](https://docs.oracle.com/cd/E11882_01/win.112/e10845/external.htm#NTQRF130).

When you complete these procedures, you are ready to perform the initial configuration tasks described in [Chapter 5, " Configuring the Server Parameter File in Oracle Real Application Clusters Environments"](params.md).

### 4.2.4 Configuring Oracle Administration Assistant for Windows

Oracle Administration Assistant for Windows requires the Microsoft Management Console and HTML Help 1.2 or later to run. Microsoft Management Console (MMC) version 2.0 ships with Windows Server 2003; version 3.0 of MMC is available with Windows Server 2003 R2 and later releases. Oracle recommends that you use the latest version of MMC that is available.

See Also:

- [Oracle Database Platform Guide for Microsoft Windows](https://docs.oracle.com/cd/E11882_01/win.112/e10845/tools.htm#NTQRF040)
- Microsoft documentation at:
	`http://www.microsoft.com/`

### 4.2.5 Using Oracle9i Database Language and Definition Files with Oracle Database 11g

You can use Oracle9i Database language and territory definition files with Oracle Database 11g release 2 (11.2). To enable this functionality:

1. Run the `cr9idata.pl` script, by default located in `Oracle_home` `\nls\data\old`.
	Alternatively, before you install Oracle Database, you can run the Oracle Universal Installer (OUI) setup command with the `b_cr9idata` variable set to true, as follows:
	```
	setup.exe oracle.rsf.nlsrtl_rsf:b_cr9idata=true
	```
2. Set the `ORA_NLS10` environment variable to point to the directory where you installed the new language and territory definition files, which by default are in `Oracle_home` `\nls\data`.
3. Restart the Oracle database.

### 4.2.6 Logging in to Oracle Enterprise Manager Database Control

If you configured Oracle Enterprise Manager Database Control during installation, then you can use it to manage your database. Oracle Enterprise Manager Database Control provides a web-based user interface that you can use to monitor, administer, and maintain an Oracle database, including Automatic Storage Management.

See Also:

- [Oracle Database Installation Guide for Microsoft Windows](https://docs.oracle.com/cd/E11882_01/install.112/e47798/startrdb.htm#NTDBI0052) for information about logging in to Enterprise Manager Database Control
- ["Managing Database Control Using EMCA"](srvpool.md)

## 4.3 Oracle Configuration Manager Postinstallation Configuration for Oracle RAC

If you have installed Oracle Configuration Manager, then you must run a script to create a database account to collect database configuration collections. You must create this account in both Connected and Disconnected modes. The database account stores the PL/SQL procedures that collect the configuration information, and the account owns the database management system (DBMS) job that performs the collection. After the account has been set up, the account is locked because login privileges are no longer required.

To configure the database for configuration collection, run the following script:

```
Oracle_home\ccr\admin\scripts\installCCRSQL.exe collectconfig -s SID -r \
SYSDBA-USER
```

The script `installCCRSQL.``exe` creates an Oracle Configuration Manager user and loads the PL/SQL procedure into the database defined by the `ORACLE_SID` environment variable. You can also specify the database SID by using the `-s` option in the command line, as in the following example, where the SID is `orcl`:

```
Oracle_home\ccr\admin\scripts\installCCRSQL.exe collectconfig -s orcl
```

For Oracle RAC, you must run the database script against only one instance, such as the local instance on which you performed the installation. However, Oracle Configuration Manager must be installed in all instance homes.

By default, the connection to the database is through operating system authentication, " `/as sysdba`." To specify a different user name and password, you can use these options:

`-r SYSDBA-USER`: The login name for the user with the SYSDBA privilege

`-p SYSDBA-PASSWORD`: The password for the user with the SYSDBA privilege

Note:

- If you specify the user name without specifying the password, then you are prompted to enter the password.
- If you specify only the password without specifying the user name, then the user `SYS` is used by default.

See Also:

- [Oracle Configuration Manager Installation and Administration Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=CCRIA) for more information
- [Oracle Database Vault Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23090/dvca.htm#DVADM19006) for additional configuration tasks

### 4.3.1 Additional Step for Oracle Enterprise Manager Grid Control

If the database is used as a repository for Oracle Enterprise Manager Grid Control, then you must also run the following script when configuring Oracle Configuration Manager:

`Oracle_home` `\ccr\admin\scripts\installCCRSQL.exe collectemrep`

When you run this script, the application prompts you for the `SYSMAN` password. To automate the installation, run the `installCCRSQL` script to specify the `SYSMAN` password. For example:

`Oracle_home` `\ccr\admin\scripts\installCCRSQL.exe collectemrep   -e` `SYSMAN` `PASSWORD`

You can add the `-s` `SID` command to specify the `SID` of the Oracle Enterprise Manager Grid Control database instance. You must run this script from the Oracle\_home in which the Oracle Enterprise Manager Grid Control database has been hosted.

If you are not using operating system authentication to connect to the database, then you must use the `-r` and `-p` parameters to specify the following:

`-r SYSDBA-USER`: The login name for the user with the SYSDBA privilege

`-p SYSDBA-PASSWORD`: The password for the user with the SYSDBA privilege

If you do not specify the `-p` parameter, then you are prompted to enter the password for the specified user.

## 4.4 Enabling and Disabling Database Options

When you install Oracle Database, some options are enabled and others are disabled. You can view the enabled Oracle Database options by querying the V$OPTION view using SQL\*Plus.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/dba.htm#ADMIN00102) for information about connecting to the database using SQL\*Plus

To enable or disable a particular database feature for an Oracle home, use the `chopt` tool. The `chopt` tool is a command-line utility that is located in the `Oracle_home` `\bin` directory. The syntax for `chopt` is as follows:

```
chopt [ enable | disable] db_option
```

The possible values for `db_option` are described in Table 4-1:

Table 4-1 Database Options for Chopt Tool Command

| Value | Description |
| --- | --- |
| `dm` | Oracle Data Mining Database Files |
| `dv` | Oracle Database Vault |
| `lbac` | Oracle Label Security |
| `olap` | Oracle OLAP |
| `partitioning` | Oracle Partitioning |
| `rat` | Oracle Real Application Testing |
| `ode_net_2` | Oracle Database Extensions for.NET 2.0 |

Before you run the `chopt` tool, shut down any Oracle databases running from the Oracle home being modified.

Example 4-1 How to Enable the Oracle Label Security Database Option Using Chopt

To enable the Oracle Label Security option in your Oracle executable files, perform the following tasks:

1. Shut down the Oracle RAC database, and any other databases running out of the Oracle home directory, using the Server Control Utility (SRVCTL).
	```
	srvctl stop database -d myRACdb
	```
2. Use the Windows Services console to stop the service for each Oracle database that runs from the Oracle home being modified.
	For example, if your Oracle RAC database is named `myRACdb`, then on the first node of the cluster you would stop the `OracleServiceMYRACDB1` service.
3. Change directories to the `Oracle_home` `\bin` directory:
	```
	cd %ORACLE_HOME%\bin
	```
4. Run the `chopt` tool, as follows:
	```
	chopt enable lbac
	```
5. Use the Windows Services console to restart the services you stopped in Step 2.
6. Use SRVCTL to restart the databases you stopped in Step 1, for example:
	```
	srvctl start database -d myRACdb
	```

## 4.5 Using Earlier Oracle Database Releases with Oracle Grid Infrastructure

The following topics describe using earlier Oracle Database releases with Oracle Clusterware 11g release 2 (11.2) installations:

- General Restrictions for Using Earlier Oracle Database Releases
- Required Patches for Earlier Oracle Database Releases or Databases Being Upgraded
- Pinning Cluster Nodes for Oracle Database Release 10.2 or 11.1

### 4.5.1 General Restrictions for Using Earlier Oracle Database Releases

You can use Oracle Database release 10.2 and release 11.1 with Oracle Clusterware and Oracle ASM release 11.2.

Note:

Refer to [Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmdiskgrps.htm#OSTMG10045) for details on configuring disk group compatibility for databases using Oracle Database versions 11.1 or earlier with Oracle Grid Infrastructure 11.2.

If you upgrade an existing release of Oracle Clusterware and Oracle ASM to Oracle Grid Infrastructure release 11.2 (which includes Oracle Clusterware and Oracle ASM), and also upgrade your Oracle RAC database to release 11.2, then the required configuration of existing databases is completed automatically.

If you plan to use Oracle Clusterware and Oracle ASM release 11.2 with Oracle RAC 10.2 or 11.1, then you must complete additional configuration tasks as described in the following sections. You also must apply patches to the Oracle RAC 10.2 or 11.1 software installations before Oracle RAC 10.2 and 11.1 will work correctly with Oracle Clusterware 11.2 and Oracle ASM 11.2. See the [Oracle Database Readme](https://docs.oracle.com/cd/E11882_01/readmes.112/e41331/toc.htm) for information about specific patches.

Note:

If you are upgrading Oracle RAC or Oracle Database from releases 11.1.0.7, 11.1.0.6, or 10.2.0.4, and you have upgraded to Oracle Clusterware and Oracle ASM release 11.2, then Oracle recommends that you check for the latest recommended patches for the release you are upgrading from, and install those patches as needed before upgrading to Oracle RAC or Oracle Database release 11.2.

For more information about recommended patches, see "Oracle Upgrade Companion," which is available through Note 785351.1 on My Oracle Support:

`https://support.oracle.com`

You can also see Oracle Support Notes 756388.1 and 756671.1 for the current list of recommended patches for each release.

See Also:

"Downloading and Installing Patch Updates"

### 4.5.2 Required Patches for Earlier Oracle Database Releases or Databases Being Upgraded

Before you use DBCA to create an Oracle RAC or Oracle Database 10.x or 11.1 database on an Oracle Clusterware and Oracle ASM release 11.2 installation, you must install patches to the Oracle RAC or Oracle Database home. See [Oracle Database Readme](https://docs.oracle.com/cd/E11882_01/readmes.112/e41331/toc.htm) for information about specific patches.

See Also:

"Downloading and Installing Patch Updates"

Before applying any patches to your Oracle Database 10g release 2 or Oracle Database 11g release 1 software, you must first stop the `OracleRemExecService` Windows service on all the nodes in your cluster. If you do not stop this process before applying patches to your Oracle Database 10g release 2 or Oracle Database 11g release 1 database, then you will receive errors during the patching operation and the Oracle software will not be patched correctly.

For Oracle Database release 11.2.0.3, if you plan to create or upgrade Oracle databases or release 11.2.0.2 (or earlier) after upgrading to or installing Oracle Grid Infrastructure release 11.2.0.3, then you must first apply the patches listed in Table 4-2.

Table 4-2 Patches Required for Oracle Database and Oracle Grid Infrastructure Release 11.2.0.3

| Environment | Patches | Apply to Oracle Grid Home? | Apply to Oracle RAC Home? |
| --- | --- | --- | --- |
| Create an Oracle RAC release 11.1 database to run on Oracle Grid Infrastructure 11.2.0.3 | 8288940  10636465 | No | Yes |
| Upgrade Oracle Grid Infrastructure and Oracle Database release 11.2.0.1 to release 11.2.0.3 | 10100101 | Yes, after creating the Oracle Database release 11.2.0.1 database | Yes, after creating the Oracle Database release 11.2.0.1 database |
| Create an Oracle Database release 11.2.0.1 database to run on a fresh install of Oracle Grid Infrastructure 11.2.0.3 | 10100101 | No | Yes, after creating the Oracle Database release 11.2.0.1 database |
| Starting an Oracle Database 10g Release 2 database (10.2.0.5) running on Oracle Grid Infrastructure release 11.2.0.3 | 12799034 | No | Yes |

### 4.5.3 Pinning Cluster Nodes for Oracle Database Release 10.2 or 11.1

When Oracle Database release 10.2 or 11.1 is installed on a new Oracle Grid Infrastructure for a cluster configuration, it is configured for dynamic cluster configuration, in which some or all Internet Protocol (IP) addresses are provisionally assigned, and other cluster identification information is dynamic. This configuration is incompatible with earlier database releases, which require fixed addresses and configurations.

You can change the nodes where you want to run the older database to create a persistent configuration. Creating a persistent configuration for a node is called pinning a node.

To pin a node in preparation for installing an earlier Oracle Database version, use `CRS_home` `\bin\crsctl` with the following command syntax, where `nodes` is a space-delimited list of the names of one or more nodes in the cluster whose configuration you want to pin:

```
crsctl pin css -n nodes
```

For example, to pin nodes `node3` and `node4`, log in as an Administrator user and enter the following command:

```
C:\> crsctl pin css -n node3 node4
```

To determine if a node is in a pinned or unpinned state, use `CRS_home` `\bin\olsnodes` with the following syntax:

```
olsnodes -t -n
```

For example, to list all pinned nodes, use the following command:

```
C:\> app\11.2.0\grid\bin\olsnodes -t -n
node1 1       Pinned
node2 2       Pinned
node3 3       Pinned
node4 4       Pinned
```

To list the state of a particular node, use the `-n` option as shown in the following example:

```
C:\> app\11.2.0\grid\bin\olsnodes -t -n node3
node3 3       Pinned
```

See Also:

[Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/toc.htm) for more information about pinning and unpinning nodes