---
title: Installing Oracle Database 11g with Oracle Real Application Clusters
book: Real Application Clusters Installation Guide for Linux and UNIX
doc_id: E41962-05
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e41962/racinstl.htm
tags:
  - oracle
  - 11g
  - real-application-clusters-installation-guide-for-linux-and-unix
---

## 2 Installing Oracle Database 11g with Oracle Real Application Clusters

This chapter describes phase two of the installation procedures for installing Oracle Database 11g release 2 (11.2) with Oracle Real Application Clusters (Oracle RAC). Phase one is the completion of installing Oracle Clusterware, as described in The [Oracle Grid Infrastructure Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=CWGEN) for your platform.

See Also:

[Oracle Database Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for your platform for additional information, such as how to open compressed files, and other information about setting up files for installation

Also, during installation, click Help to find explanations of options and prompts for each installation screen, and click Details to see the log file

This chapter contains the following topics:

## 2.1 Reviewing Oracle Application Express Requirements

With Oracle Database 11g release, Oracle Application Express is provided as an Oracle Database option, rather than as an Oracle Application option. If you intend to install Oracle Database after installing Oracle Clusterware, and you have an existing Oracle Database installation that you are upgrading, then review the following Oracle Application Express requirements:

- Browser Requirements for Oracle Application Express
- Installing with Existing Oracle HTML Server Installations
- Oracle Text Requirement for Oracle Application Express
- Oracle XML DB Requirement for Oracle Application Express

### 2.1.1 Browser Requirements for Oracle Application Express

To view or develop Oracle Application Express applications, Web browsers must support Java Script, and the HTML 4.0 and CSS 1.0 standards. The following browsers meet this requirement:

- Mozilla 1.7 or a later version
- Firefox 1.0.4 or a later version

### 2.1.2 Installing with Existing Oracle HTML Server Installations

Oracle Application Express must have access to Oracle HTTP Server and `mod_plsql` to run. The following products include the versions of HTTP Server and `mod_plsql` that meet this requirement:

- Oracle 9i Database release 2 (9.2) or a later version
- Oracle 9i Application Server release 1 (1.0.2.2) or a later version

### 2.1.3 Oracle Text Requirement for Oracle Application Express

Oracle Text must be installed so that you can use the searchable online Help in Oracle Application Express. By default, Oracle Text is installed as part of Oracle Database.

See Also:

[Oracle Text Application Developer's Guide](https://docs.oracle.com/cd/E11882_01/text.112/e24435/toc.htm) for more information about Oracle Text

### 2.1.4 Oracle XML DB Requirement for Oracle Application Express

To upgrade to Oracle Database 11g release 2 (11.2), Oracle XML DB must be installed in the Oracle database that you want to upgrade. If you are using a preconfigured database created either during an installation or by Database Configuration Assistant (DBCA), then Oracle XML DB is already installed and configured.

See Also:

[Oracle XML DB Developer's Guide](https://docs.oracle.com/cd/E11882_01/appdev.112/e23094/toc.htm) for more information about manually adding Oracle XML DB to an existing database

## 2.2 Selecting a Configuration Option

This section describes OUI features that you should understand before beginning the Oracle RAC installation process.

See Also:

[Appendix C, " Converting to Oracle RAC and Oracle RAC One Node from Single-Instance Oracle Databases"](cvrt2rac.md) for information about how to convert single-instance databases to Oracle RAC

On the Select Installation Option page, you are given the following options:

- Create and Configure a Database: Provides you with the option to create a database using a preconfigured database template designed for particular system load demands, such as an online transaction processing (OLTP) database, or a decision support or data warehouse database.
- Install database software only: Installs Oracle Database software; you must complete the database configuration later.
- Upgrade an existing database: Upgrades an existing database.

If you are installing Oracle Database software, then Oracle recommends that you use one of the preconfigured database options, or select the Advanced option on the Select Configuration page, and configure a custom starter database.

See Also:

If you have an existing Oracle installation, then record your environment's version numbers, patches, and other configuration information, and review upgrade procedures for your existing installation. Review the Oracle upgrade documentation before proceeding with your installation to decide how to proceed.

For late-breaking updates and best practices about preupgrade, post-upgrade, compatibility, and interoperability discussions, refer to "Oracle Upgrade Companion." "Oracle Upgrade Companion" is available through Note 785351.1 on My Oracle Support:

`https://support.oracle.com/`

## 2.3 Oracle Database Vault Installation and Configuration

Review the following information if you want to install Oracle Database Vault:

- Oracle Database Vault Requirements
- Oracle Database Vault Accounts
- Multiple Oracle Database Vault Homes
- Starting the Listener with Oracle Database Vault Installations
- Installing Oracle Database Vault

### 2.3.1 Oracle Database Vault Requirements

Oracle Database Vault requires the following:

- An Oracle Database Enterprise Edition installation (single-instance or Oracle RAC)
- Setting the initialization parameter `db_block_size` to 4096 or higher
- Oracle Enterprise Manager Console
- Oracle Clusterware running (for installation in an Oracle RAC environment)
	Note:
	You must have `root` access to start Oracle Clusterware.
	The command `crsctl start crs` also starts the database. Before you start OUI to install Oracle Database Vault, shut down the database.
	See Also:
	[Section E.3.1, "Stopping Oracle Database Processes Before Adding Products or Upgrading"](procstop.md)
- A listener configured for the database into which you are installing Oracle Database Vault. To ensure that the new listener process starts during the installation, you must shut down existing listeners before starting Oracle Universal Installer.
- Oracle Database Vault installation owner write access to the Oratab file (AIX: `/etc/oratab`; Solaris, HP-UX: `/var/opt/oracle/oratab`) and to the `oraInst.loc` file (AIX: `/etc/oraInst.loc`; Solaris, HP-UX: `/var/opt/oracle/oraInst.loc`). This access is provided either by using the same installation owner as you use with the Oracle Database installation, or another user with `oinstall` group membership.
- An existing password file for Oracle Database. In addition, the password file authentication parameter, `REMOTE_LOGIN_PASSWORDFILE`, must have been set to `EXCLUSIVE` or `SHARED`.
	You can set the `REMOTE_LOGIN_PASSWORDFILE` parameter in the Oracle Database initialization file. Use the `orapwd` utility to create and manage password files.
	See Also:
	[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for more information on creating and maintaining a password file

### 2.3.2 Oracle Database Vault Accounts

Oracle Database Vault prompts for two accounts that you can create during installation. These are the Oracle Database Vault Owner and the Oracle Database Vault Account Manager accounts. You must provide an account name and password for the Database Vault Owner during installation. Do not use the names of Oracle Database Vault roles (such as DV\_OWNER and DV\_ACCTMGR) for these two user accounts. Creating an Oracle Database Vault Account Manager is optional.

See Also:

[Oracle Database Vault Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23090/db_objects.htm#DVADM70328) for a full list of Oracle Database Vault roles

#### 2.3.2.1 Oracle Database Vault Owner

The Oracle Database Vault Owner account is granted the `DV_OWNER` role. This account can manage Oracle Database Vault roles and configuration.

The Oracle Database Vault Owner user name can be a minimum of 2, and a maximum of 30 characters long. The account password can be a minimum of 8, and a maximum of 30 characters.

The password that you choose for the Oracle Database Vault Owner account must be secure. The following password restrictions are enforced:

- The password must include at least one alphabet, one digit, and one nonalphanumeric character (symbol).
- The password cannot be the same as the account name.
- The password cannot contain any consecutive repeating characters.

#### 2.3.2.2 Oracle Database Vault Account Manager

The Oracle Database Vault Account Manager is granted the `DV_ACCTMGR` role. This account is used to manage database user accounts. The Oracle Database Vault Account Manager is created to facilitate separation of duties. If you do not choose to create the Oracle Database Vault Account Manager account, then the `DV_ACCTMGR` role is granted to the Oracle Database Vault Owner account by default.

The Oracle Database Vault Account Manager user name can be a minimum of 2, and a maximum of 30 characters long. The account password can be a minimum of 8, and a maximum of 30 characters.

The same password restrictions that apply to Oracle Database Vault Owner are applicable to Oracle Database Vault Account Manager as well.

### 2.3.3 Multiple Oracle Database Vault Homes

You can install Oracle Database Vault more than once on the same system, in different Oracle homes.

### 2.3.4 Starting the Listener with Oracle Database Vault Installations

You need to start the listener and database on all Oracle RAC nodes other than the one on which the installation is performed. You must use the Server Control (`srvctl`) utility to start and stop Oracle Database Vault Oracle RAC instances. Do not use SQL\*Plus to start and stop Oracle RAC instances.

For example:

```
$ORACLE_HOME/bin/lsnrctl start listener_name
$ORACLE_HOME/bin/srvctl start instance -d database_name -i instance_name
```

### 2.3.5 Installing Oracle Database Vault

Oracle Database Vault is installed with the Advanced Install option. You can configure Oracle Database Vault after installation using DBCA, or choose not to configure Oracle Database Vault.

#### 2.3.5.1 Configuring Oracle Database Vault During Oracle RAC Installation

To install Oracle Database Vault while installing Oracle RAC:

1. Start Oracle Universal Installer, and select Advanced installation.
2. Select Enterprise Edition, and then Select Options.
3. In addition to the default installation components, select Oracle Label Security (OLS) and Oracle Database Vault.
4. After installation, proceed with creating the database.
5. After you create the database, start DBCA.
6. Select the option to configure the database.
7. Select the OLS and Oracle Database Vault to configure to the database.
8. Provide the required Oracle Database Vault user IDs and passwords to proceed with configuration. If you want to enable a separate Oracle Database Vault administrator, then you can choose to configure the DV\_ACCTMGR user.

#### 2.3.5.2 Configuring Oracle Database Vault After Oracle RAC Installation

To configure Oracle Database Vault after installing Oracle RAC:

1. Install the Oracle RAC Enterprise Edition database.
2. Stop all database processes.
3. Enter the following commands:
	```
	$ make -f $ORACLE_HOME/rdbms/lib/ins_rdbms.mk dv_on
	$ make -f $ORACLE_HOME/rdbms/lib/ins_rdbms.mk ioracle
	```
4. Start up all Oracle RAC processes.
5. Start DBCA, and select the option Configure Database.
6. In the component list, select Oracle Label Security and Oracle Database Vault.
7. Provide the required administrative user accounts and passwords, and proceed with configuration.

## 2.4 Oracle Database Configuration Type Descriptions

When you run OUI, you can select the Typical or the Advanced Install type.

The Typical install type installs a default configuration of Oracle Database, with basic configuration choices. Oracle recommends that most users select Typical as their installation type.

The Advanced installation type is for customized installations, and should be used only when you have a specific requirement for it, such as requiring different passwords for the SYS, SYSMAN, SYSTEM and DBSNMP accounts, or using a different database character set than is in use on your servers, changing product languages, or other nonstandard configurations.

You can install Oracle RAC One Node on two or more nodes in the cluster. An Oracle RAC One Node installation starts up an instance on one of the nodes you select as an Oracle RAC One Node pool member. If that instance goes down, then the Oracle RAC One Node instance is started up on another pool member using Online Database Relocation. This feature migrates database instances and connections to other cluster nodes for high availability.

See Also:

[Oracle Database High Availability Overview](https://docs.oracle.com/cd/E11882_01/server.112/e17157/toc.htm) for information about Oracle RAC One Node

### 2.4.1 General Purpose and Transaction Processing, and Data Warehouse Configuration Types

The General Purpose and Transaction Processing type and the Data Warehouse configuration type use preconfigured database templates optimized for each type of database.

During installation, OUI starts Oracle Network Configuration Assistant (NETCA) and DBCA, and installs the preconfigured database without further input. During database installation, OUI displays a progress indicator.

DBCA processing for these two configuration types creates a starter database, and configures the Oracle network services.

If you select Advanced configuration, then you must enter specific information as described in the next section.

### 2.4.2 Using the Advanced Install Type

Use the Advanced Install type to address specific requirements, such as selecting specific components to add or remove from the installation, creating a database in a nondefault character set, or adding translation of product user interface into languages other than English. By default, the installation configures the character set of a new database based on the language of the operating system.

See Also:

[Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/toc.htm) for detailed information on character sets and language configuration

The following section provides more detail about OUI and DBCA processing when creating an Oracle RAC database.

See Also:

[Oracle Database Installation Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=GINST) for your platform for information about configuring globalization

## 2.5 Oracle Configuration Manager Option

During installation, you are prompted to provide information needed to enable Oracle Configuration Manager. This option enables you to associate information about your Oracle RAC configuration with your My Oracle Support (formerly OracleMetalink) account. In the event that you need to place a service request with Oracle Support, that configuration information can help to provide a more rapid resolution to the service issue.

Configuring the OCM tool requires that you have the following information from your service agreement:

- My Oracle Support e-mail address/username
- Password

In addition, you are prompted for server proxy information, if the host system does not have a direct connection to the Internet.

Refer to My Oracle Support (`https://support.oracle.com`) if you encounter registration failures and are uncertain that the correct country code has been specified. You can find the country associated with your My Oracle Support account by selecting the menu option More, then selecting Settings. In the Settings menu, select Accounts & Privileges.

See Also:

[Oracle Configuration Manager Installation and Administration Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=CCRIA) for further information

## 2.6 Database Security Options

During installation, you are prompted to select database security configuration.The Secure Configuration option configures the database with database auditing options, and password policy and expiration settings.

For new database installations, the default configuration for Oracle Database 11g release 2 (11.2) includes the Secure Configuration option. If you want to disable these enhanced security controls, then you can check the Disable security settings box. Oracle Database is then installed with default options for Oracle Database 10g release 2. After installation, you can change security settings by starting DBCA and modifying security settings. You can enable or disable auditing or password security settings, or revert to a previous security setting.

For database upgrades, the upgraded database retains your existing database security configuration, to ensure compatibility with existing applications. After installation, you can use DBCA to enable or disable the Secure Configuration auditing or password security settings for testing.

To enable or disable secure configuration after installation, you must use command line DBCA options. By design, The DBCA 11g release 2 and later graphic user interface does not have the option to enable or disable secure configuration.

Note:

Oracle strongly recommends configuring your database with the Secure Configuration option either during installation, or after installation using command line DBCA.

## 2.7 Changing Administrative Account Database Passwords

All databases include the administrative accounts `SYS`, `SYSTEM`, and `SYSMAN`. Administrative accounts are highly privileged accounts, and are needed only by individuals authorized to perform administrative tasks such as starting and stopping the database, managing database memory and storage, creating and managing database users, and so on.

Passwords for all Oracle system administration accounts except SYS, SYSTEM, SYSMAN, and DBSMP are revoked after installation. You should change the administrative account and DBSMP passwords after installation. You must change the administrative account passwords to a password that is different from the default password.

See Also:

[Oracle Database 2 Day DBA Online Help](https://docs.oracle.com/cd/E11882_01/server.112/e10897/users_secure.htm#ADMQS007) and [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/create.htm#ADMIN11086) for more information administrative accounts

Apply the following guidelines when specifying passwords:

- Passwords must be between 8 and 30 characters long.
- Passwords must not start with a numeral.
- Passwords must not be the same as the user name.
- Passwords must not be Oracle reserved words.
- The `SYS` account password must not be `change_on_install`.
- The `SYSTEM` account password must not be `manager`.
- The `SYSMAN` account password must not be `sysman`.
- The `DBSNMP` account password must not be `dbsnmp`.
- To use the same password for all the accounts, that password must not be `change_on_install`, `manager`, `sysman`, or `dbsnmp`.
- Passwords should have at least 1 alphabetic, 1 numeric, and 1 punctuation character
- Passwords should not be simple or obvious words, such as welcome, account, database, and user.

## 2.8 Actions of OUI and DBCA During Installation

After installing Oracle Database, OUI runs DBCA to create your database, in accordance with Optimal Flexible Architecture (OFA) guidelines. An installation created following OFA guidelines means that DBCA creates your database files, including the default server parameter file (SPFILE), using standard file naming and file placement practices.

The primary phases of DBCA processing are the following:

- Create the database.
- Configure the Oracle network services, if necessary.
- Start the listeners and database instances.

You can also use DBCA in standalone mode to create or delete a database, or to switch database management from Oracle Enterprise Manager Database Control to Oracle Enterprise Manager Grid Control.

Note that with Oracle Database release 11.1 and later releases, service management is no longer performed for Oracle RAC databases using DBCA. Use `srvctl`, Oracle Enterprise Manager DB Control or Grid Control for all administration and monitoring of services. Oracle Net Configuration Assistant (NetCA) is run as part of an Oracle Grid Infrastructure installation".

See Also:

The following documents for further information:
- [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm) if you experience problems (for example, with the listener configuration), and for further information about Lightweight Directory Access Protocol (LDAP) support
- [Oracle Enterprise Manager Real Application Clusters Guide Online Help](https://docs.oracle.com/cd/E11882_01/rac.112/e17264/toc.htm) for service management using Oracle Enterprise Manager

In Oracle Database 10g and later releases, some database language and territory definition files have been updated to better reflect locale conventions used in associated locales.

If the resulting changes in default NLS parameter values adversely affect your existing applications, then you can revert the changes by installing Oracle9i compatibility definition files. To install Oracle9i files in place of Oracle11g files, you must run OUI from a command line, as described in "Using Oracle Universal Installer to Install Oracle RAC", and use the following statement to set the `b_cr9idata` variable to `true`:

```
./runInstaller oracle.rsf.nlsrtl_rsf:b_cr9idata=true
```

See Also:

[Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/toc.htm) for additional information about updates to the Oracle Database language and territory definition files

## 2.9 Installing Oracle Database with Other Languages

To use languages other than the default (English), either for the database or for applications running on the database, you must use the Advanced Installation type.

See Also:

[Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/toc.htm)

## 2.10 Selecting a Database Name

The database name input field is used to set the following Oracle initialization parameter values:

- DB\_NAME
- DB\_UNIQUE\_NAME
- DB\_DOMAIN

In Oracle RAC environments, the database name (DB\_UNIQUE\_NAME) portion is a string of no more than 30 characters that can contain alphanumeric, underscore (\_), dollar ($), and pound (#) characters, but must begin with an alphabetic character. No other special characters are permitted in a database name. The DB\_NAME parameter for a database is set to the first 8 characters of the database name.

The domain portion of the global database name (DB\_DOMAIN) can be no more than 128 characters. Domain names using underscores (\_) are not allowed. The values for DB\_UNIQUE\_NAME.DB\_DOMAIN in its entirety must be unique within the enterprise.

For example, if your database has a global database name of `orl$racprod2551.example.com`, which you supplied during installation, then the following values are used for initialization parameters:

| Parameter | Value |
| --- | --- |
| DB\_UNIQUE\_NAME | `orl$racprod2551` |
| DB\_DOMAIN | `example.com` |
| DB\_NAME | `orl$racp` |

The SID prefix is the first 8 characters of the database name. The SID prefix can contain only the characters a-z, A-Z, and 0-9. The SID prefix cannot contain operating system special characters, so if you use special characters in the first 8 characters of the database name, then these special characters are omitted in the SID prefix. There is a single SID prefix for every database. The SID prefix for a database must be unique within the cluster.

For an Oracle RAC database, each instance has a unique identifier, ORACLE\_SID, which consists of the SID prefix and an instance number. The ORACLE\_SID for Oracle RAC database instances is generated differently, depending on how you choose to manage the database. If you select a policy-managed database, then Oracle generates the SID in the format name\_#, where name is the first eight alphanumeric characters of DB\_UNIQUE\_NAME, and # is the instance number. If you select an admin-managed database, then DBCA generates the SID for the instance names in advance, and the SID is in the format name#.

For example, if the DB\_UNIQUE\_NAME for a database is orl$racprod2551, then the following SID values are used:

| Database or Instance Type | Value used for ORACLE\_SID |
| --- | --- |
| Single-instance Oracle database | orlracpr |
| Policy-managed Oracle RAC instance | orlracpr\_1 |
| Admin-managed Oracle RAC instance | orlracpr1 |

## 2.11 Using Oracle Universal Installer to Install Oracle RAC

To install Oracle Database software with Oracle RAC:

1. Ensure that you can access other nodes with SSH. OUI requires that the user account running the Oracle RAC installation is permitted to set up passwordless SSH. OUI can set this up for you automatically, or your system administrator can set this up for you before installation is started.
2. Open the terminal from which you intend to run OUI, and log in as the user account that you want to own the Oracle Database installation (for example, `oracle`).
	If you are not able to turn off `stty` commands, or have other restrictions that would prevent automatic SSH configuration from within OUI, then you must ensure that SSH is configured and enabled before you proceed to start the Installer.
3. Ensure that you have `su` or `sudo` credentials, because you will be prompted to run a script as the `root` user during installation.
	To use the Software Updates option to obtain the most current system requirement updates, critical patch updates, and other recommended updates for installation, use a valid My Oracle Support username and password, or provide the path to a downloaded Software Updates option package when prompted.
4. Start the `runInstaller` command from the Disk1 on the Oracle Database 11g release 2 (11.2) installation media or install binary download area. For example, where the software binary download area is `/home/oracle/oraclesw`, enter the following commands:
	```
	$ cd /home/oracle/oraclesw/Disk1
	$ ./runInstaller
	```
5. Provide information or run scripts as `root` when prompted by OUI. If you need assistance during installation, click Help. Click Details to see the log file.
	Note:
	You can run the `root.sh` script simultaneously on all nodes in the cluster for Oracle RAC installations or upgrades.
	If you encounter problems during installation, then examine the OUI actions recorded in the installation log file. The log file is located in the Oracle Inventory directory in the following location:
	```
	OraInventory/logs/installActionsdate_time.log
	```
	Caution:
	The Oracle home name and path that you provide during database installation must be different from the home that you used during the Oracle Grid Infrastructure installation in phase one. You must not install Oracle Database 11g with Oracle RAC software into the same home in which you installed the Oracle Grid Infrastructure for a cluster software.
	Note that because Oracle ASM is part of the Oracle Grid Infrastructure home, it cannot be upgraded during an Oracle RAC installation.

When you have completed the second and final phase of the installation, proceed to [Chapter 4, "Oracle Real Application Clusters Postinstallation Procedures"](postinst.md) to perform the postinstallation tasks.

Caution:

After installation is completed and you have created the database, if you decide that you want to install additional Oracle Database 11g release 2 (11.2) products in the database, then you must stop all processes running in the Oracle home before you attempt to install the additional products. For the Oracle Universal Installer to relink certain executables and libraries, all database processes must be stopped. Refer to [Appendix E, "How to Stop Processes in an Existing Oracle Real Application Clusters Database"](procstop.md) for additional information.

The following is a list of additional information to note about installation:

- On the Select Database Management Option page, if you have already completed the Grid Control Management Agent installation, then you can select either Grid or Local Database control. Otherwise, only Local Database control for database management is supported for Oracle RAC. When you use the local Database Control, you can choose the e-mail option and enter the outgoing SMTP server name and e-mail address.
	If you perform an installation that does not include Oracle Enterprise Manager (for example, an Advanced Installation software install without Oracle Enterprise Manager, an installation with no Oracle Enterprise Manager configuration, or a database creation with your own scripts), then you can configure Oracle Enterprise Manager later using OUI, DBCA, or the Oracle Enterprise Manager Configuration Assistant (EMCA) utility.

## 2.12 Using Oracle Universal Installer to Install Oracle RAC One Node

To install Oracle RAC One Node:

1. Open the terminal from which you intend to run OUI, and log in as the user account that you want to own the Oracle Database installation (for example, `oracle`).
	If you are not able to turn off `stty` commands, or have other restrictions that would prevent automatic SSH configuration from within OUI, then you must ensure that SSH is configured and enabled before you proceed to start the Installer.
2. Ensure that you have `su` or `sudo` credentials, because you will be prompted to run a script as the `root` user during installation.
3. Start the `runInstaller` command from the Disk1 on the Oracle Database 11g release 2 (11.2) installation media or install binary download area. For example, where the software binary download area is `/home/oracle/oraclesw`, enter the following commands:
	```
	$ cd /home/oracle/oraclesw/Disk1
	$ ./runInstaller
	```
4. Select to configure an Oracle RAC One Node database, and select to and install Oracle RAC on all nodes where Oracle RAC One Node will run.
5. Provide information or run scripts as `root` when prompted by OUI. If you need assistance during installation, click Help. Click Details to see the log file.
	Note:
	You can run the `root.sh` script simultaneously on all nodes in the cluster for Oracle RAC installations or upgrades.
	If you encounter problems during installation, then examine the OUI actions recorded in the installation log file. The log file is located in the Oracle Inventory directory in the following location:
	```
	OraInventory/logs/installActionsdate_time.log
	```
	Caution:
	The Oracle home name and path that you provide during database installation must be different from the home that you used during the Oracle Grid Infrastructure installation in phase one. You must not install Oracle Database 11g with Oracle RAC software into the same home in which you installed the Oracle Grid Infrastructure for a cluster software.
	If you are upgrading a database, then you must use the same type of Oracle home. For example, you should not change from local Oracle homes to a shared Oracle home.
	Note that because Oracle ASM is part of the Oracle Grid Infrastructure home, it cannot be upgraded during an Oracle RAC installation.

## 2.13 Using DBCA to Configure Oracle RAC One Node

If you have selected to install Oracle RAC software only on cluster nodes, you can use Oracle Database Configuration Assistant (DBCA) to configure Oracle RAC One Node.

After installation, start up DBCA, and on the Welcome page, select Oracle RAC One Node database. DBCA starts on only one node of the set of nodes you select. You can add additional nodes to the cluster later.

Selecting one node deploys Oracle RAC One Node on a single node. Oracle recommends that you select all nodes in the cluster to which you want Oracle RAC One Node to be able to fail over.

If you select less than two nodes, or create server pools with a cardinality of `2` or more, then DBCA posts a warning message that the configuration you select will not support failover of the Oracle RAC One Node instance.

When you create an admin-managed Oracle RAC One Node database, note that while the database is started on only one of the pool of nodes you installed the binaries, all the candidate servers are placed into the Generic server pool. If the servers are not already in Generic or Free, then this may result in stopping resources that are running on candidate servers.

See Also:

Oracle Technology Network for more information about Oracle RAC One Node:
```
http://www.oracle.com/technology/products/database/clustering/index.html
```