---
title: Broker
book: Data Guard Broker
doc_id: F31839-04
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/dgbkr/oracle-data-guard-broker-installation-requirements.html
tags:
  - oracle
  - 21c
  - data-guard-broker
---

For all members that you want to add to a broker configuration, you must complete installation and configuration tasks.

- Oracle Data Guard Installation
- Prerequisites
	See Also:
	[Oracle Data Guard Broker Upgrading and Downgrading](upgrading-downgrading-in-data-guard-broker-configuration.md) for help with upgrading to a new release in an Oracle Data Guard broker configuration

### Oracle Data Guard Installation

Oracle Data Guard is included with the Enterprise Edition and Personal Edition of the Oracle database software.

You can manage an Oracle Data Guard configuration by using either SQL\*Plus, the Oracle Data Guard broker's command-line interface (DGMGRL), or a compatible version of Oracle Enterprise Manager Cloud Control (Cloud Control).

Install the Oracle Enterprise Edition or Personal Edition database software on each location you expect to include in broker configurations. You must install a compatible version of Cloud Control if you want to use the graphical user interface for Oracle Data Guard.

In addition, to use fast-start failover you must install DGMGRL and run the observer software. Oracle recommends running observers on computer systems that are separate from the primary and standby systems. To install DGMGRL on an observer computer, use one of the methods described in the following list:

- Install the complete Oracle Client Administrator by choosing the `Administrator` option from Oracle Universal Installer.
	This installation includes DGMGRL but it does not include the Cloud Control agent. This allows you to manage observer processes using DGMGRL commands, but not Cloud Control. (The Cloud Control agent can be installed separately.)
- Install the full Oracle Database Enterprise Edition or Personal Edition software kit
	This installation includes DGMGRL and the Cloud Control agent, allowing you to manage observer processes using Cloud Control or DGMGRL commands.
	Note:
	An observer can be run from any platform that supports it, and that platform can be different from the platform of the primary or target standby database.

Note:

Zero Data Loss Recovery Appliance does not require broker software to be installed.

### Prerequisites

These are the conditions that must be met before you can use the broker.

- The primary and standby databases and far sync instances must be using the same version of Oracle Database and each can be installed in either a single-instance or multi-instance environment. The database must be licensed for Oracle Enterprise Edition or Personal Edition.
- You must use a server parameter file (SPFILE) to ensure the broker can persistently reconcile values between broker properties and any related initialization parameter values. See [Configurable (Changeable) Properties](managing-oracle-data-guard-broker-configuration-members.md) for more information.
	If any of the databases in the configuration is an Oracle RAC database, you must configure the server parameter file (SPFILE) appropriately for use in an Oracle RAC environment.
	See Also:
	[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/dgbkr&id=RACAD020) for information about initialization files in an Oracle RAC
- The value of the `DG_BROKER_START` initialization parameter must be set to `TRUE` for all databases in the configuration. See [Starting the Data Guard Broker](managing-oracle-data-guard-broker-configurations.md) for more information. (Cloud Control sets this parameter automatically.)
- If any of the databases in the configuration is an Oracle RAC database, you must set up the `DG_BROKER_CONFIG_FILE` `n` initialization parameters for that database such that they point to the same shared files for all instances of that database. The shared files could be files on a cluster file system, if available, or stored using Oracle Automatic Storage Management (Oracle ASM).
	See Also:
	Configuration file information in [Configuration Management](oracle-data-guard-broker-concepts.md). Also, see [Setting Up the Broker Configuration Files](managing-oracle-data-guard-broker-configurations.md) for details about setting up the broker configuration file.
- Network configuration files must be set up on the primary database and on the standby database if you configure an existing standby database into the broker configuration. Cloud Control can assist you in creating the configuration files when creating a standby database.
	See Also:
	[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/dgbkr&id=NETAG187) for more information about network configuration files
- In a broker configuration, you use the `DGConnectIdentifer` property to specify a connect identifier for each database. The connect identifier for a database must:
	- Allow all other databases in the configuration to reach it.
		- Allow all instances of an Oracle RAC database to be reached.
		- Specify a service that all instances dynamically register with the listeners so that connect-time failover on an Oracle RAC database is possible.
		Caution:
		The service should NOT be one that is defined and managed by Oracle Clusterware.
		- Have failover attributes set to allow the primary database's Redo Transport Services to continue shipping redo data to an Oracle RAC standby database, even if the receiving instance of that standby database has failed.
	See Also:
	[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/dgbkr&id=NETAG364) for more information about connect identifiers
- To enable DGMGRL to restart instances during the course of broker operations, a static service must be registered with the local listener of each instance. For configurations where Oracle Clusterware or Oracle Restart are not being used, a static service must be registered with the local listener associated with each instance. The static service allows DGMGRL to restart instances during the course of broker operations and to allows the observer to restart instances during automatic reinstatement of the old primary database after a fast-start failover has occurred.
	By default, the broker assumes a static service name of `db_unique_name_DGMGRL.db_domain` and expects the listener has been started with the following content in the `listener.ora` file:
	```
	LISTENER = (DESCRIPTION =
	     (ADDRESS_LIST=(ADDRESS=(PROTOCOL=tcp)(HOST=host_name)
	     (PORT=port_num))))
	SID_LIST_LISTENER=(SID_LIST=(SID_DESC=(SID_NAME=sid_name)
	     (GLOBAL_DBNAME=db_unique_name_DGMGRL.db_domain)
	     (ORACLE_HOME=oracle_home)
	     (ENVS="TNS_ADMIN=oracle_home/network/admin")))
	```
	Alternatively, you can use a different static service name. If you do, be sure to modify the `StaticConnectIdentifier` instance-specific property to reflect the static service that has been registered.
	To ensure that the connect identifier has been set up correctly, use the `VALIDATE STATIC CONNECT IDENTIFIER` command.
	See Also:
	- See [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/dgbkr&id=NETAG1589) for more information about configuring static services
	- See the My Oracle Support Note 1387859.1 at [`http://support.oracle.com`](http://support.oracle.com/) for additional information about using static services and the `StaticConnectIdentifier` configurable property
	- [VALIDATE STATIC CONNECT IDENTIFIER](oracle-data-guard-broker-commands.md)
- The primary database must be opened in `ARCHIVELOG` mode.
- You must set the `COMPATIBLE` initialization parameter to 12.2.0 or higher for both the primary and standby databases. However, if you want to take advantage of Oracle Database Release 21c new features, then set the `COMPATIBLE` parameter to 21.1 on all databases within the Oracle Data Guard configuration.
	For the broker to work, the `COMPATIBLE` initialization parameter must be set to the same value on both the primary and standby databases. If the values differ, redo transport services may be unable to transmit redo data from the primary database to the standby databases.
- Select and configure a redo transport authentication method, as described in [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/dgbkr&id=SBYDB00424).

See Also:

- [Starting the Data Guard Broker](managing-oracle-data-guard-broker-configurations.md) for more information about preparing and starting Oracle Data Guard broker