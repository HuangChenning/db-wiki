---
title: Oracle Real Application Clusters Postinstallation Procedures
book: Real Application Clusters Installation Guide for Linux and UNIX
doc_id: E41962-05
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e41962/postinst.htm
tags:
  - oracle
  - 11g
  - real-application-clusters-installation-guide-for-linux-and-unix
---

## 4 Oracle Real Application Clusters Postinstallation Procedures

This chapter describes how to complete the postinstallation tasks after you have installed the Oracle Database 11g release 2 (11.2) with Oracle Real Application Clusters (Oracle RAC) software. This chapter contains the following topics:

Note:

This chapter describes only basic configurations. Refer to [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/dba.htm#ADMIN001), and the product administration and tuning guides for more detailed configuration and tuning information. Refer also to [Oracle Database Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for your platform for additional postinstallation configuration information.

## 4.1 Required Postinstallation Tasks

Perform the following tasks after completing your installation:

- Downloading and Installing Patch Updates
- Setting External Jobs Ownership for Installations on HP-UX
- Configuring Oracle Products
- Relocating Instance-Related Memory-Mapped files from OCFS2 Using Symbolic Links

### 4.1.1 Downloading and Installing Patch Updates

Refer to the My Oracle Support Web site for required patch updates for your installation.

Note:

Browsers require an Adobe Flash plug-in, version 9.0.115 or higher to use My Oracle Support. Check your browser for the correct version of Flash plug-in by going to the Adobe Flash checker page, and installing the latest version of Adobe Flash.

If you do not have Flash installed, then download the latest version of the Flash Player from the Adobe web site:

```
http://www.adobe.com/go/getflashplayer
```

To download required patch updates:

1. Use a Web browser to view the My Oracle Support Web site:
	`https://support.oracle.com`
2. Log in to My Oracle Support.
	Note:
	If you are not a My Oracle Support registered user, then click Register for My Oracle Support and register.
3. On the main My Oracle Support page, click Patches & Updates.
4. In the Patches section, click Simple Search.
5. Specify the following information, then click Go:
	- In the Search By field, select Product or Family, and then specify RDBMS Server.
		- In the Release field, specify the current release number.
		- In the Patch Type field, specify Patchset/Minipack.
		- In the Platform or Language field, select your platform.
6. In the Results list, find the latest patch set for Oracle Database.
	Patch sets for Oracle databases are identified in the Description column as Product:Patchset x.x.x.x PATCH SET FOR ORACLE DATABASE SERVER.
7. In the Patch column, click the number of the patch that you want to download.
8. On the Patch Set page, click View README and read the page that appears. The README page contains information about the patch set and how to apply the patches to your installation.
9. Return to the Patch Set page, click Download, and save the file on your system.
10. Use the unzip utility provided with Oracle Database 11g release 2 (11.2) to uncompress the Oracle patch updates that you downloaded from My Oracle Support. The unzip utility is located in the `$ORACLE_HOME/bin` directory.

### 4.1.2 Setting External Jobs Ownership for Installations on HP-UX

On HP-UX platforms only, complete the following procedure to set external jobs ownership to the low-privilege user `extjob`:

1. Log on as root.
2. Change directory to the Oracle Database Oracle home:
	```
	# cd $ORACLE_HOME/rdbms/admin/
	```
3. Open `externaljob.ora` with a text editor, and find the parameters `run_user` and `run_group`.
4. Set `run_user` to the external jobs user (`extjob`), and set `run_group` to a low-privileged group, such as `other`. For example:
	```
	run_user=extproc
	run_group=other
	```
5. Save the file.
	Note:
	Modify `externaljob.ora` only as `root`.

### 4.1.3 Configuring Oracle Products

Many Oracle products and options must be configured before you use them for the first time. Before using individual Oracle Database 11g release 2 (11.2) database products or options, refer to the manual in the product documentation library which is available in the DOC directory on the Oracle Database installation media, or on the OTN Web site.

## 4.2 Recommended Postinstallation Tasks

Oracle recommends that you complete the following tasks after installing Oracle RAC:

- Backing Up the root.sh Script
- Setting the Oracle User Environment Variables
- Recompiling all PL/SQL modules
- Setting Up Additional User Accounts
- Running Oracle RAC Configuration Audit Tool

### 4.2.1 Backing Up the root.sh Script

Oracle recommends that you back up the `root.sh` script after you complete an installation. If you install other products in the same Oracle home directory, then the Oracle Universal Installer (OUI) updates the contents of the existing `root.sh` script during the installation. If you require information contained in the original `root.sh` script, then you can recover it from the `root.sh` file copy.

### 4.2.2 Setting the Oracle User Environment Variables

On each node, in the installation owner user profile file (in this example, `oracle`), set the environment variables `ORACLE_BASE` and `ORACLE_HOME`, and `ORACLE_SID`; also add `ORACLE_HOME/bin` to the path environment variable.

For example:

```
export ORACLE_BASE=/u01/app/oracle
export ORACLE_HOME=/u01/app/oracle/11.2.0/dbhome_1
export PATH=$PATH:$ORACLE_HOME/bin
export ORACLE_SID=sales1
```

If the environment variables `ORACLE_HOME` and `ORACLE_SID` are not set, and you try to use SQL\*Plus or other tools, then you receive an error message requesting that you set these variables.

### 4.2.3 Recompiling all PL/SQL modules

Oracle recommends that you run the `utlrp.sql` script after creating or upgrading a database. This script recompiles all PL/SQL modules that might be in an invalid state, including packages, procedures, and types. This is an optional step but Oracle recommends that you do it immediately following installation, not at a later date.

1. Complete setting up the Oracle software owner user account environment (for example, `oracle`), as described in "Setting the Oracle User Environment Variables" in the preceding section.
2. Start SQL\*Plus, as follows:
	```
	$ sqlplus "/ AS SYSDBA"
	```
3. Run the `utlrp.sql` script, where `Oracle_home` is the Oracle home path:
	```
	SQL> @Oracle_home/rdbms/admin/utlrp.sql
	```

### 4.2.4 Setting Up Additional User Accounts

For information about setting up additional optional user accounts, refer to Oracle Database 11g Administrator's Guide for UNIX Systems.

When you complete these procedures, you are ready to perform the initial configuration tasks described in [Chapter 5, " Configuring the Server Parameter File in Oracle Real Application Clusters Environments"](params.md).

### 4.2.5 Running Oracle RAC Configuration Audit Tool

Oracle recommends that you run the Oracle RAC Configuration Audit tool (RACcheck) to check your Oracle RAC installation. RACcheck is an Oracle RAC auditing tool that checks various important configuration settings within Oracle Real Application Clusters, Oracle Clusterware, Oracle Automatic Storage Management and the Oracle Grid Infrastructure environment.

Oracle recommends that you download and run the latest version of RACcheck from My Oracle Support. For information about downloading, configuring, and running RACcheck configuration audit tool, refer to My Oracle Support note 1268927.1, which is available at the following URL:

`https://support.oracle.com/CSP/main/article?cmd=show&type=NOT&id=1268927.1`

See Also:

[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/racchk.htm#RACAD8365)

## 4.3 Oracle Configuration Manager Postinstallation Configuration for Oracle RAC

If you have installed Oracle Configuration Manager, then you must run a script to create a database account to collect database configuration collections. You must create this account in both Connected and Disconnected modes. The database account stores the PL/SQL procedures that collect the configuration information, and the account owns the database management system (DBMS) job that performs the collection. After the account has been set up, the account is locked because login privileges are no longer required.

To configure the database for configuration collection, run the following script:

```
$ORACLE_HOME/ccr/admin/scripts/installCCRSQL.sh collectconfig -s SID -r\ 
SYSDBA-USER -p SYSDBA-PASSWORD
```

The script `installCCRSQL.sh` creates an Oracle Configuration Manager user and loads the PL/SQL procedure into the database defined by the `ORACLE_SID`. You can also specify the database SID by using the `-s` option in the command line, as in the following example, where the SID is `orcl`:

```
$ORACLE_HOME/ccr/admin/scripts/installCCRSQL.sh collectconfig -s orcl
```

For Oracle RAC, you must run the database script against only one instance, such as the local instance on which you performed the installation. However, Oracle Configuration Manager must be installed in all instance homes.

See Also:

- [Oracle Configuration Manager Installation and Administration Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=CCRIA) for further information
- [Oracle Database Vault Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23090/dvca.htm#DVADM19006) for additional configuration tasks

## 4.4 Enabling and Disabling Database Options After Installation

When you install Oracle Database, some options are enabled and others are disabled. To enable or disable a particular database feature for an Oracle home, shut down the database and use the `chopt` tool.

The chopt tool is a command-line utility that is located in the directory `ORACLE_HOME/bin`. It uses the following syntax, where db\_option is the option whose status you want to modify:

chopt \[enable | disable\] db\_option

The possible values for db\_option are described in Table 4-1:

Table 4-1 Chopt Tool Command Options for Database Options

| Value | Description |
| --- | --- |
| `dm` | Oracle Data Mining Database Files |
| `dv` | Oracle Database Vault |
| `lbac` | Oracle Label Security |
| `olap` | Oracle OLAP |
| `partitioning` | Oracle Partitioning |
| `rat` | Oracle Real Application Testing |
| `ode_net` | Oracle Database Extensions for.NET 1.x |
| `ode_net_2` | Oracle Database Extensions for.NET 2.0 |

Example 4-1 How to Enable a Database Option Using Chopt

In this example, the `chopt` tool is used to enable Oracle Label Security in the database `oradb1`:

```
$ cd $ORACLE_HOME/bin
$ srvctl stop database -d oradb1
$ chopt enable lbac
$ srvctl start database -d oradb1
```