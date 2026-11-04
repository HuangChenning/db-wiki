---
title: Installing Oracle Database 11g with Oracle Real Application Clusters
book: Real Application Clusters Installation Guide for Microsoft Windows x64 (64-Bit)
doc_id: E48195-02
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/install.112/e48195/racinstl.htm
tags:
  - oracle
  - 11g
  - real-application-clusters-installation-guide-for-microsoft-windows-x64-64-bit
---

## 2 Installing Oracle Database 11g with Oracle Real Application Clusters

This chapter describes phase two of the installation procedures for installing Oracle Database 11g release 2 (11.2) with Oracle Real Application Clusters (Oracle RAC). Phase one is the completion of the Oracle Clusterware installation, as described in [Oracle Grid Infrastructure Installation Guide for Microsoft Windows x64 (64-Bit)](https://docs.oracle.com/cd/E11882_01/install.112/e48194/toc.htm).

See Also:

[Oracle Database Installation Guide for Microsoft Windows](https://docs.oracle.com/cd/E11882_01/install.112/e47798/toc.htm) for additional information, such as how to open compressed installation files, and other information about setting up files for installation

Also, during installation, click Help to find explanations of options and prompts for each installation screen, and click Details to see the log file.

This chapter contains the following topics:

## 2.1 Reviewing Oracle Application Express Requirements

With Oracle Database 11g, Oracle Application Express is provided as an Oracle Database option, rather than as an Oracle Application option. If you intend to install Oracle Database after installing Oracle Clusterware, and you have an existing Oracle Database installation that you are upgrading, then review the Oracle Application Express requirements in [Oracle Application Express Installation Guide](https://docs.oracle.com/cd/E11882_01/install.112/e12196/toc.htm).

## 2.2 Selecting an Installation Type

When you run Oracle Universal Installer (OUI), you can select the Typical or the Advanced installation type.

The Typical installation type installs a default configuration of Oracle Database, with basic configuration choices. Oracle recommends that most users select Typical as their installation type.

The Advanced installation type is for customized installations, and should be used only when you have a specific requirement for it, such as adding specific components to your installation, requiring different passwords for the SYS, SYSMAN, SYSTEM and DBSNMP accounts, using a different database character set than is in use on your servers, changing product languages, or other nonstandard configurations.

You can install Oracle RAC One Node on two or more nodes in the cluster. An Oracle RAC One Node installation starts up an instance on one of the nodes you select as an Oracle RAC One Node pool member. If that instance goes down, then the Oracle RAC One Node instance is started up on another pool member using Online Database Relocation. This feature migrates database instances and connections to other cluster nodes for high availability.

See Also:

- [Oracle Database High Availability Overview](https://docs.oracle.com/cd/E11882_01/server.112/e17157/toc.htm) for information about Oracle RAC One Node
- [Appendix C, "Converting to Oracle RAC and Oracle RAC One Node from Single-Instance Oracle Databases"](cvrt2rac.md) for information about how to convert single-instance databases to Oracle RAC

## 2.3 Selecting an Installation Option

On the Select Installation Option page, you can select one of the following options:

- Create and Configure a Database: Provides you with the option to create a database using a preconfigured database template designed for particular system load demands, such as an online transaction processing (OLTP) database, or a decision support or data warehouse database.
	If you select the Oracle Automatic Storage Management (Oracle ASM) option for storage, then you must have previously configured Oracle ASM. If you did not select Oracle ASM as the storage option for the Oracle Clusterware files when installing Oracle Grid Infrastructure, then you must first use Oracle ASM Configuration Assistant (ASMCA) from the Grid home to configure Oracle ASM, You must create an Oracle ASM instance and create a disk group to use for your Oracle Database storage before you can select Oracle ASM as a storage option for your Oracle RAC database.
- Install database software only: Installs Oracle Database software; you must complete the database configuration after the installation completes using the installed utilities.
- Upgrade an existing database: Upgrades an existing database.

If you are installing Oracle Database software, then Oracle recommends that you use a preconfigured database option, or select the Advanced option on the Select Configuration page, and configure a custom starter database. See "Selecting an Oracle Database Configuration Type" for more information about the different preconfigured database options.

See Also:

If you have an existing Oracle installation, then write down the version numbers, patches, and other configuration information, and review upgrade procedures for your existing installation. Review [Oracle Database Upgrade Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23633/toc.htm) before proceeding with the installation, to decide how you want to proceed.

For late-breaking updates and best practices about pre-upgrade, post-upgrade steps, compatibility, and interoperability discussions, see "Oracle Upgrade Companion," which is available through Note 785351.1 on My Oracle Support:

`https://support.oracle.com/`

## 2.4 Selecting an Oracle Database Configuration Type

When you run OUI, you can select the General Purpose/Transaction Processing, Data Warehouse, or Advanced database configuration type.

For the first two configuration types, you can complete additional procedures that are described later in this chapter.

If you select Advanced configuration, then you can use Oracle Database Configuration Assistant (DBCA) to create the database as described in [Chapter 3, "Creating Oracle Real Application Clusters Databases with Oracle Database Configuration Assistant"](dbcacrea.md). Oracle recommends that you use DBCA to create your database.

### 2.4.1 Preconfigured Database Types Supplied with Oracle Database

The General Purpose and Transaction Processing type and the Data Warehouse type use preconfigured database templates optimized for each type of database.

During installation, OUI starts Oracle Net Configuration Assistant (NETCA) and DBCA, and installs the preconfigured database without further input. During database installation, OUI displays a progress indicator.

DBCA processing for these two configuration types creates a starter database, and configures the Oracle network services.

### 2.4.2 Using the Advanced Database Configuration Type

Advanced configuration options available using this installation type include Oracle RAC, Automatic Storage Management, backup and recovery configuration, integration with Enterprise Manager Grid Control, and more fine-grained memory tuning, as well as other options.

### 2.4.3 Installing Oracle Database with Other Languages

To use languages other than the default (English), either for the database or for applications running on the database, you must use the Advanced Installation method.

See Also:

[Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/toc.htm)

## 2.5 Selecting the Oracle Database Vault Option

Installing and configuring Oracle Database Vault requires actions during and after installation, as described in the following topics:

- Overview of Oracle Database Vault Accounts
- Overview of Oracle Database Vault Installation

### 2.5.1 Overview of Oracle Database Vault Accounts

Oracle Database Vault prompts for two accounts that you can create during installation. These are the Oracle Database Vault Owner and the Oracle Database Vault Account Manager accounts. Creating an Oracle Database Vault Account Manager is optional, but Oracle recommends that you create this account for better separation of duty.

You must supply a database user name and password for the Database Vault Owner during installation. Do not use the names of Oracle Database Vault roles (such as DV\_OWNER and DV\_ACCTMGR) for these two user accounts. See [Oracle Database Vault Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23090/db_objects.htm#DVADM70328) for a full list of Database Vault roles.

#### 2.5.1.1 Oracle Database Vault Owner

The Oracle Database Vault Owner account is granted the DV\_OWNER role. This account can manage Oracle Database Vault roles and configuration.

The Oracle Database Vault Owner user name can be a minimum of 2, and a maximum of 30 characters. The account password can be a minimum of 8, and a maximum of 30 characters.

The password that you choose for the Oracle Database Vault Owner account must be secure. The following password restrictions are enforced:

- The password must include at least one alphabet, one digit, and one nonalphanumeric character (symbol).
- The password cannot be the same as the account name.
- The password cannot contain any consecutive repeating characters.

#### 2.5.1.2 Oracle Database Vault Account Manager

The Oracle Database Vault Account Manager is granted the DV\_ACCTMGR role. This account is used to manage database user accounts. The Oracle Database Vault Account Manager is created to facilitate separation of duties. If you do not choose to create the Oracle Database Vault Account Manager account, then the DV\_ACCTMGR role is granted to the Oracle Database Vault Owner account by default.

The same password restrictions that apply to Oracle Database Vault Owner are applicable to Oracle Database Vault Account Manager as well.

### 2.5.2 Overview of Oracle Database Vault Installation

Oracle Database Vault is installed with the Advanced Install option of Oracle Database Enterprise Edition. After the Oracle Database Vault software has been installed, you configure Oracle Database Vault using DBCA. Oracle Database Vault is not installed or configured by default.

## 2.6 Selecting the Oracle Configuration Manager Option

During installation, you are prompted to provide information needed to enable Oracle Configuration Manager (OCM). This option enables you to associate information about your Oracle RAC configuration with your My Oracle Support (formerly OracleMetalink) account. In the event that you must place a service request with Oracle Support Services, that configuration information can help provide a more rapid resolution to the service issue.

You can enable Oracle Configuration Manager during or after installation, or choose not to enable it. Configuring the OCM tool requires that you have the following information available from your Oracle Support Services service agreement:

- My Oracle Support e-mail address or user name
- Password

In addition, you are prompted for server proxy information if the host system does not have a direct connection to the Internet.

Go to My Oracle Support (`https://support.oracle.com`) if you encounter registration failures.

See Also:

[Oracle Configuration Manager Installation and Administration Guide](http://www.oracle.com/pls/topic/lookup?ctx=db112&id=CCRIA) for more information

## 2.7 Selecting a Database Name

The database name input field is used to set the following Oracle initialization parameter values:

- `DB_NAME`
- `DB_UNIQUE_NAME`
- `DB_DOMAIN`

In Oracle RAC environments, the database name (`DB_UNIQUE_NAME`) portion is a string of no more than 30 characters that can contain alphanumeric, underscore (\_), dollar ($), and pound (#) characters, but must begin with an alphabetic character. No other special characters are permitted in a database name. The `DB_NAME` parameter for a database is set to the first 8 characters of the database name.

The domain portion of the global database name (`DB_DOMAIN`) can be no more than 128 characters. Domain names using underscores (\_) are not allowed. The values for `DB_UNIQUE_NAME`.`DB_DOMAIN` in its entirety must be unique within the enterprise.

For example, if your database has a global database name of `orl$racprod2551.example.com` which you supplied during installation, then the following values are used for initialization parameters:

| Initialization Parameter | Example Value |
| --- | --- |
| DB\_UNIQUE\_NAME | orl$racprod2551 |
| DB\_DOMAIN | example.com |
| DB\_NAME | orl$racp |

The SID prefix is the first 8 characters of the database name. The SID prefix can contain only the characters a-z, A-Z, and 0-9. The SID prefix cannot contain operating system special characters, so if you use special characters in the first 8 characters of the database name, then these special characters are omitted in the SID prefix. There is a single SID prefix for every database. The SID prefix for a database must be unique within the cluster.

For an Oracle RAC database, each instance has a unique identifier, `ORACLE_SID`, which consists of the SID prefix and an instance number. The `ORACLE_SID` for Oracle RAC database instances is generated differently, depending on how you choose to manage the database. If you select a policy-managed database, then Oracle generates the SID in the format `name_#`, where name is the first eight alphanumeric characters of `DB_UNIQUE_NAME`, and # is the instance number. If you select an admin-managed database, then DBCA generates the SID for the instance names in advance, and the SID is in the format `name#`.

For example, if the `DB_UNIQUE_NAME` for a database is `orl$racprod2551`, then the following SID values are used:

| Database or Instance Type | Value Used for ORACLE\_SID |
| --- | --- |
| Single-instance Oracle database | `orlracpr` |
| Policy-managed Oracle RAC instance | `orlracpr_1` |
| Admin-managed Oracle RAC instance | `orlracpr1` |

## 2.8 Creating Database Passwords

Apply the following guidelines when specifying passwords:

- Passwords should be between 8 and 30 characters long.
- Passwords must be from the ASCII character set.
- Passwords must not start with a numeral.
- Passwords should not be the same as the user name.
- Passwords must not be Oracle reserved words.
- The SYS account password should not be `change_on_install`.
- The SYSTEM account password should not be `manager`.
- To use the same password for all the accounts, the password should not be `change_on_install`, `manager`, `sysman`, or `dbsnmp`.
- Passwords should have at least 1 alphabetic, 1 numeric, and 1 punctuation character.
- Passwords should not be simple or obvious words, such as `welcome`, `account`, `database`, `oracle`, or `user`.

## 2.9 Understanding the Actions of OUI and DBCA During Installation

After installing Oracle Database, OUI runs DBCA to create your database, in accordance with Optimal Flexible Architecture (OFA) guidelines. An installation created following OFA guidelines means that DBCA creates your database files, including the default server parameter file (SPFILE), using standard file naming and file placement practices.

Note:

NETCA is run as part of an Oracle Grid Infrastructure installation.

The primary tasks of DBCA are the following:

- Create the database.
- Configure the Oracle network services, if necessary.
- Start the listeners and database instances.

You can also use DBCA in standalone mode to create or delete a database, or to switch database management from Oracle Enterprise Manager Database Control to Oracle Enterprise Manager Grid Control. See ["Managing Database Control Using EMCA"](srvpool.md).

See Also:

[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm) if you experience problems (for example, with the listener configuration), and for more information about Lightweight Directory Access Protocol (LDAP) support

### 2.9.1 Managing Database Services After Installation

Starting with Oracle Database 11g release 1 (11.1), you cannot use DBCA to manage database services for Oracle RAC databases. Use the Server Control Utility (SRVCTL), Oracle Enterprise Manager Database Control or Oracle Enterprise Manager Grid Control for all administration and monitoring of database services for an Oracle RAC database.

See Also:

[Oracle Database 2 Day + Real Application Clusters Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e17264/configwlm.htm#TDPRC307) for service management using Oracle Enterprise Manager

### 2.9.2 Installing Earlier NLS Compatibility Definition Files

In Oracle Database 10g and later releases, some database language and territory definition files have been updated to better reflect locale conventions used in associated locales.

If the resulting changes in default National Language Support (NLS) parameter values adversely affect your existing applications, then you can revert the changes by installing Oracle9i Database compatibility definition files. To install Oracle9i Database files in place of Oracle11g Database files, you must run OUI from a command line, as described in "Using Oracle Universal Installer to Install Oracle RAC", and use the following statement to set the `b_cr9idata` variable to `true`:

```
setup.exe oracle.rsf.nlsrtl_rsf:b_cr9idata=true
```

See Also:

[Oracle Database Globalization Support Guide](https://docs.oracle.com/cd/E11882_01/server.112/e10729/toc.htm) for additional information about updates to the Oracle Database language and territory definition files

## 2.10 Using Oracle Universal Installer to Install Oracle RAC

To install Oracle Database 11g release 2 (11.2) with Oracle RAC:

1. Log in to Windows as a user with Administrator privileges.
2. Verify that you have Administrator privileges on the other nodes. To do this, enter the following command for each node that is a part of the cluster where node\_name is the name of the remote node:
	```
	net use \\node_name\C$
	```
3. To use the Software Updates option to obtain the most current system requirement updates, critical patch updates, and other recommended updates for installation, use a valid My Oracle Support username and password, or provide the path to a downloaded Software Updates option package when prompted.
4. Start the `setup.exe` command from the base directory of the Oracle Database 11g release 2 (11.2) installation media, and select the database type to install.
5. Provide information when prompted by OUI. If you need assistance during installation, then click Help. If you encounter problems during installation, then examine the OUI actions recorded in the installation log file. The log file is located in the Oracle Inventory directory with a name that includes the time stamp (`date_time`) of the installation process, as shown in this example:
	```
	C:\Program Files\Oracle\Inventory\logs\installActionsdate_time.log
	```
	In the preceding example, the variables `date` and `time` represent the date and the time of the log file.
	Caution:
	The Oracle home name and path that you provide during database installation must be different from the home that you used during Oracle Grid Infrastructure installation. Do not install Oracle Database 11g with Oracle RAC software into the same home in which you installed Oracle Grid Infrastructure software.
	If you are upgrading a database, then you must use the same type of Oracle home. For example, you should not change from local Oracle homes to a shared Oracle home.
	Note that because Oracle ASM is part of the Grid Infrastructure home, it cannot be upgraded during an Oracle RAC installation.

When you have completed this second and final phase of the installation, proceed to [Chapter 4, "Oracle Real Application Clusters Postinstallation Procedures"](postinst.md) to perform the postinstallation tasks.

Caution:

After installation is completed and you have created the database, if you decide to install additional Oracle Database 11g release 2 (11.2) products in the database, then you must stop all processes running in the Oracle home before you attempt to install the additional products. See [Appendix E, "How to Stop Processes in an Existing Oracle Real Application Clusters Database"](procstop.md) for additional information.

The following is a list of additional information to note about installation:

- On the Select Database Management Option page, if you completed the Grid Control Management Agent installation, then you can select either Oracle Enterprise Manager Grid Control or Database Control. If you did not complete the Grid Control Management Agent installation, then only Database Control for database management is supported for Oracle RAC. When you use the Oracle Enterprise Manager Database Control console, you can choose the e-mail option for alerts and enter the outgoing mail server name and e-mail address.
- If you perform an installation that does not include Oracle Enterprise Manager (for example, an Advanced installation without configuring Oracle Enterprise Manager, an installation with no Oracle Enterprise Manager configuration, or a database creation with your own scripts), then you can configure Oracle Enterprise Manager later using OUI, DBCA, or the Oracle Enterprise Manager Configuration Assistant (EMCA) utility. See ["Managing Database Control Using EMCA"](srvpool.md).

## 2.11 Using Oracle Universal Installer to Install Oracle RAC One Node

To install Oracle RAC One Node:

1. Login to Windows as a user with Administrative privileges.
2. Start the `setup.exe` command from the base directory of the Oracle Database 11g release 2 (11.2) installation media, and select the database type to install.
3. Select to configure an Oracle RAC One Node database, and select to install Oracle RAC on all nodes where Oracle RAC One Node will run.
4. Provide information when prompted by OUI. If you need assistance during installation, click Help. Click Details to see the log file.
	If you encounter problems during installation, then examine the OUI actions recorded in the installation log file. The log file is located in the Oracle Inventory directory with a name that includes the timestamp (`date_time`) of the install process, as shown in this example:
	```
	C:\Program Files\Oracle\Inventory\logs\installActionsdate_time.log
	```
	Caution:
	The Oracle home name and path that you provide during database installation must be different from the home that you used during the Oracle Grid Infrastructure installation in phase one. You must not install Oracle Database 11g with Oracle RAC software into the same home in which you installed the Oracle Grid Infrastructure for a cluster software.
	If you are upgrading a database, then you must use the same type of Oracle home. For example, you should not change from local Oracle homes to a shared Oracle home.
	Note that because Oracle ASM is part of the Oracle Grid Infrastructure home, it cannot be upgraded during an Oracle RAC installation.

## 2.12 Installing Oracle RAC and Oracle Database Vault

To install Oracle Database Vault while installing Oracle RAC:

1. Start OUI and select Advanced installation.
2. Select Enterprise Edition, and then select Options.
3. In addition to the default installation components, select Oracle Label Security (OLS) and Oracle Database Vault.
4. Continue the rest of the installation process as you normally would.

Note:

You must set the database initialization parameter `db_block_size` to 4096 or higher. You can configure this parameter during the installation of Oracle RAC.

After you have installed Oracle RAC with the Oracle Database Vault option you must complete the configuration of Oracle Database Vault, as described in [Oracle Database Vault Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e23090/toc.htm).

## 2.13 Using DBCA to Configure Oracle RAC One Node

If you have selected to install Oracle RAC software only on cluster nodes, you can use Oracle Database Configuration Assistant (DBCA) to configure Oracle RAC One Node.

After installation, start up DBCA, and on the Welcome page, select Oracle RAC One Node database. DBCA starts on only one node of the set of nodes you select. You can add additional nodes to the cluster later.

Selecting one node deploys Oracle RAC One Node on a single node. Oracle recommends that you select all nodes in the cluster to which you want Oracle RAC One Node to be able to fail over.

Caution:

By default, any named user may create a server pool. To restrict the operating system users that have this privilege, Oracle strongly recommends that you add specific users to the CRS Administrators list. See [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41959/admin.htm#CWADD91105) for more information about adding users to the CRS Administrators list.

If you select less than two nodes, or create server pools with a cardinality of `2` or more, then DBCA posts a warning message that the configuration you select will not support failover of the Oracle RAC One Node instance.

When you create an administrator-managed Oracle RAC One Node database, note that while the database is started on only one of the pool of nodes you installed the binaries, all the candidate servers are placed into the Generic server pool. If the servers are not already in Generic or Free, then this may result in stopping resources that are running on candidate servers.

See Also:

Oracle Technology Network for more information about Oracle RAC One Node:
```
http://www.oracle.com/technetwork/database/clustering/overview/
```

## 2.14 Updating Environment Variables on Remote Nodes

During the installation, the Windows registry and environment variables are modified on each node on which you installed Oracle RAC. The new registry entries and environment variable settings are visible on the node where the installation was performed. However, the new settings on the remote nodes are not immediately available to your user session. Attempting to run scripts or applications from the newly installed Oracle home can produce errors similar to the following:

- ORACONFIG.exe - Unable to Locate Component
- OCI.dll not found

To make the modified environment variables available on the remote nodes, you can close your current session on the remote nodes (log off) and then log on to the remote nodes to create a new session, or perform the following actions:

1. From the Start menu, right-click My Computer, then select Properties.
	Alternatively, enter `SYSDM.CPL` in the Run window.
2. Select the Advanced tab.
3. Click Environment Variables.
	The modified environment variables are now visible.
4. Click OK to close the System Properties window.