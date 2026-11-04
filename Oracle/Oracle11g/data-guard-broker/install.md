---
title: Oracle Data Guard Installation
book: Data Guard Broker
doc_id: E40771-07
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40771/install.htm
tags:
  - oracle
  - 11g
  - data-guard-broker
---

## 2 Oracle Data Guard Installation

This chapter includes the following topics:

- Oracle Data Guard Installation
- Prerequisites
	See Also:
	[Appendix B](upgrade_appx.md) for help with upgrading to a new release in a Data Guard broker configuration

## 2.1 Oracle Data Guard Installation

Oracle Data Guard is included with the Enterprise Edition and Personal Edition of the Oracle database software. You can manage a Data Guard configuration by using either SQL\*Plus, the Data Guard broker's command-line interface (DGMGRL), or a compatible version of Oracle Enterprise Manager Grid Control.

To use DGMGRL, the best practice is to install the Oracle Enterprise Edition or Personal Edition database software on each location you expect to include in broker configurations. You must install a compatible version of Oracle Enterprise Manager Grid Control to use the Enterprise Manager Web-based user interface for Data Guard.

In addition, to use fast-start failover you must install DGMGRL and run the observer software. Oracle recommends running the observer on a computer system that is separate from the primary and standby systems. To install DGMGRL on the observer computer, use one of the methods described in the following list:

- Install the complete Oracle Client Administrator by choosing the `Administrator` option from Oracle Universal Installer.
	This installation includes DGMGRL but it does not include the Oracle Enterprise Manager agent. This allows you to manage the observer using DGMGRL commands but not Oracle Enterprise Manager. (The Oracle Enterprise Manager agent can be installed separately.)
- Install the full Oracle Database 11g software kit.
	This installation includes DGMGRL and the Oracle Enterprise Manager agent, allowing you to manage the observer using Oracle Enterprise Manager or DGMGRL commands.
	Note:
	The observer can be run from any platform that supports it, and that platform can be different from the platform of the primary or target standby database.

## 2.2 Prerequisites

The following conditions must be met before you can use the broker:

- The primary and standby databases must be using the same version of Oracle Database 11g and each can be installed in either a single-instance or multi-instance environment. The database must be licensed for Oracle Enterprise Edition or Personal Edition.
- You must use a server parameter file (SPFILE) to ensure the broker can persistently reconcile values between broker properties and any related initialization parameter values. See [Section 4.3.2](dbresource.md) for more information.
	If any of the databases in the configuration is an Oracle RAC database, you must configure the server parameter file (SPFILE) appropriately for use in an Oracle RAC environment.
	See Also:
	[Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/cd/E11882_01/rac.112/e41960/admin.htm#RACAD020) for information about initialization files in an Oracle RAC
- The value of the `DG_BROKER_START` initialization parameter must be set to `TRUE`. See [Section 3.3](configure.md) for more information. (Enterprise Manager sets this parameter automatically.)
- If any of the databases in the configuration is an Oracle RAC database, you must set up the `DG_BROKER_CONFIG_FILE` `n` initialization parameters for that database such that they point to the same shared files for all instances of that database. The shared files could be files on a cluster file system, if available, on raw devices, or stored using Oracle Automatic Storage Management (Oracle ASM).
	See Also:
	Configuration file information in [Section 1.6.2](concepts.md). Also, see [Section 3.2](configure.md) for details about setting up the broker configuration file, and [Section 3.2.2.3](configure.md) for details about sizing the raw devices.
- Oracle Net Services network files must be set up on the primary database and on the standby database if you configure an existing standby database into the broker configuration. Enterprise Manager can assist you in creating the network files when creating a standby database.
	See Also:
	[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm)
- In a broker configuration, you use the `DGConnectIdentifer` property to specify a connect identifier for each database. The connect identifier for a database must:
	- Allow all other databases in the configuration to reach it.
		- Allow the database to reach itself.
		- Allow all instances of an Oracle RAC database to be reached.
		- Specify a service that all instances dynamically register with the listeners so that connect-time failover on an Oracle RAC database is possible.
		- Have failover attributes set to allow the primary database's Redo Transport Services to continue shipping redo data to an Oracle RAC standby database, even if the receiving instance of that standby database has failed.
	See Also:
	[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm) for more information about connect identifiers
- To enable DGMGRL to restart instances during the course of broker operations, a static service must be registered with the local listener of each instance. A static service registration is also required to enable the observer to restart instances as part of automatic reinstatement of the old primary database after a fast-start failover has occurred. By default, the broker assumes a static service name of `db_unique_name_DGMGRL.db_domain` and expects the listener has been started with the following content in the `listener.ora` file:
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
	You should also be aware of the following additional considerations in an Oracle Clusterware environment:
	- The static service must be set in the `listener.ora` file in the GRID\_HOME of all the nodes.
		- The ORACLE\_HOME `listener.ora` parameter in the static service definition must be set to the ORACLE\_HOME of the instance, not the GRID\_HOME.
		- The ENVS `listener.ora` parameter must be used in the static service definition to explicitly set the TNS\_ADMIN environment variable to the appropriate network admin directory, which is usually the network admin directory of the Oracle Home for the Oracle database.
		- In an Oracle RAC One Node or Policy Managed Oracle RAC environment, the `SID_NAME` of each possible instance must be specified in the `SID_LIST`. The `SID_NAME` of each instance must match the `INSTANCE_NAME` database initialization parameter of that instance. In an Oracle RAC One Node or Policy Managed Oracle RAC environment, the default value of the `INSTANCE_NAME` parameter is `db_unique_name_instance_number`.
	See Also:
	- See [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/listenercfg.htm#NETAG297) for more information about configuring static services
	- See the My Oracle Support Note 1387859.1 at `http://support.oracle.com` for additional information about using static services and the `StaticConnectIdentifier` configurable property
- The primary database must be opened in `ARCHIVELOG` mode.
- You must set the `COMPATIBLE` initialization parameter to 10.2.0.1.0 or higher for both the primary and standby databases. However, if you want to take advantage of new Oracle Database 11.2 features, set the `COMPATIBLE` parameter to 11.2.0 on all databases within the Data Guard configuration.
	Ensure the `COMPATIBLE` initialization parameter is set to the same value on both the primary and standby databases. If the values differ, redo transport services may be unable to transmit redo data from the primary database to the standby databases.
- Select and configure a redo transport authentication method, as described in [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/create_ps.htm#SBYDB00424).

See Also:

- [Section 3.3](configure.md) for more information about preparing and starting Oracle Data Guard broker
- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/toc.htm) for more information about setting up network files
- [Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm)