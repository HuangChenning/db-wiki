---
title: "What's New in Oracle Data Guard Broker?"
book: Data Guard Broker
doc_id: E40771-07
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40771/whatsnew.htm
tags:
  - oracle
  - 11g
  - data-guard-broker
---

This preface describes the new features added to Oracle Data Guard broker in Oracle Database 11g and provides links to additional information. For information about features that were introduced in earlier releases, refer to the documentation for those releases.

## New Features in Oracle Data Guard Broker 11.2.0.4

This section describes the new features and enhancements that were added to Oracle Data Guard broker in Oracle Database 11g Release 2 (11.2.0.4):

- The new `ApplyLagThreshold` configurable database property allows you to set a maximum value for the apply lag on physical and logical standbys. A warning is issued if the limit is exceeded. See [Section 8.3.3](dbpropref.md).
- The `ExternalDestination1` and `ExternalDestination2` configuration properties let you set up a redo transport destination that can receive redo data from the current primary database. See [Section 8.1.3](dbpropref.md) and [Section 8.1.4](dbpropref.md).
- The new `ObserverOverride` configuration property allows you to specify whether the observer should initiate an automatic failover when it loses connectivity to the primary, even if the standby has a healthy connection to the primary. See [Section 8.1.9](dbpropref.md).
- The new `ObserverReconnect` configuration property allows you to specify an interval at which the observer disconnects and reconnects to the primary database. See [Section 8.1.10](dbpropref.md).
- The new `PrimaryLostWriteAction` configuration property determines what action is taken if a standby database detects that a lost write has occurred at the primary database. See [Section 8.1.12](dbpropref.md).
- The new `TransportDisconnectedThreshold` configurable database property allows you to set a limit on the amount of time that can elapse without communication from the primary. A warning is issued if the limit is exceeded. See [Section 8.3.42](dbpropref.md).
- The new `TransportLagThreshold` configurable database property allows you to set a limit for a database's transport lag. A warning is issued if the limit is exceeded. See [Section 8.3.43](dbpropref.md).
- You can now use the information provided in the new `V$FS_OBSERVER_HISTOGRAM` view for help in determining an appropriate value for the `FastStartFailoverThreshold` configuration property. See [Section 8.1.8](dbpropref.md).

## New Features in Oracle Data Guard Broker 11.2.0.3

This section describes the new features and enhancements that were added to Oracle Data Guard broker in Oracle Database 11g Release 2 (11.2.0.3)

- The new `TraceLevel` configuration property lets you control the amount of tracing performed by the broker for every database in the configuration. See [Section 8.1.13](dbpropref.md).

## New Features in Oracle Data Guard Broker 11.2

This section describes the new features and enhancements that were added to Oracle Data Guard broker in Oracle Database 11g Release 2 (11.2):

- As of Oracle Database 11g Release 2 (11.2.0.2), Oracle Data Guard broker is fully integrated with Oracle Real Application Clusters One Node (Oracle RAC One Node).
- A broker configuration can now consist of a primary database and up to 30 standby databases.
- The value of an instance-specific property can be changed for all instances in one command.
- Redo transport compression is no longer limited to compressing redo data only when a redo gap is being resolved. When compression is enabled for a destination, all redo data sent to that destination is compressed.
- Reinstatement of logical bystanders after a physical standby or logical standby failover.
- Reinstatement of bystanders after an immediate failover.
- Reinstatement of the old (original) primary database after an immediate failover.
- Shutting down all instances but one on a target physical standby for role changes is no longer required.
- FAN/ONS (Fast Application Notification/Oracle Notification Services) notification is sent after a failover for databases configured with Oracle Clusterware and for single-instance databases registered with Oracle Restart.
- FAN/AQ (Fast Application Notification/Advanced Queuing) notification is sent after a failover to a logical standby database.
- Improved status and error reporting for the `SHOW CONFIGURATION` and `SHOW DATABASE` commands.
- The `SHOW DATABASE` command displays the apply lag and transport lag of a standby database.
- Integration with Active Data Guard (automatic stop and restart of apply) when an apply instance is opened.
- The broker configuration files can now reside on disks having any sector size (physical block size) up to 4KB.
- Improved hang detection and resolution for broker network communications. In addition, a new configuration property, `CommunicationTimeout`, enables the user to select an appropriate timeout value for their environment.
- New database property, `StaticConnectIdentifier`, which allows the user to specify a static connect identifier that the DGMGRL client will use to start database instances.
- Protection mode upgrades from maximum availability to maximum protection no longer require a restart of the primary database.
	This means that when upgrading from maximum performance mode to maximum protection mode, you can avoid a restart of the primary database by first upgrading to maximum availability. Once in maximum availability mode, you can then upgrade to maximum protection mode.
- Data Recovery Adviser now uses Data Guard to suggest viable repair options for a primary database that cannot be repaired in a timely manner.

## New Features in Oracle Data Guard Broker 11.1

This section describes the new features and enhancements that were added to Oracle Data Guard broker in Oracle Database 11g Release 1 (11.1):

- Fast-start failover enhancements
	The following features increase the flexibility and manageability of customers' disaster-recovery configurations using Data Guard:
	- Fast-start failover for a configuration operating in maximum performance mode
		Allows fast-start failover to be enabled in a Data Guard broker configuration operating in maximum performance mode. The administrator can choose the maximum amount of data that may be lost if a fast-start failover is initiated.
		- New `DBMS_DG` PL/SQL package
		The `DBMS_DG` PL/SQL package allows applications to notify the observer process to initiate a fast-start failover to the target standby database.
		- Fast-start failover for configurable conditions
		Fast-start failover can be configured to occur when specific database conditions are detected. Certain conditions detectable through the database health-check mechanism and errors raised by the Oracle server (such as ORA errors) may be designated as conditions under which a fast-start failover should occur.
		- After a failover, the observer automatically attempts to reinstate bystander standby databases.
	See Also:
	- [Section 5.5, "Fast-Start Failover"](sofo.md)
	- The `DBMS_DG` PL/SQL package in [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm)
- Manageability enhancements
	The following enhancements make it possible to use the Data Guard broker in a wider variety of disaster-recovery configurations:
	- Support for snapshot standby databases
		See Also:
		The DGMGRL [CONVERT DATABASE](dgmgrl.md) command
		- Support for Redo Apply on physical standby databases opened for read
		- Improved support for redo transport options. Enables the administrator to specify a connect identifier for Redo Transport Services.
		- Elimination of database downtime when changing the protection mode to and from maximum availability and maximum performance
		- Allow a primary or logical standby database in a Data Guard Broker configuration to be mounted without having to be opened automatically
		- The DGMGRL client `ADD DATABASE` command can import a pre-configured service attribute from a `LOG_ARCHIVE_DEST_` `n` parameter when adding a standby database to the configuration.
		- Simplification of the database states managed by the broker. A primary database can be in either the TRANSPORT-OFF or TRANSPORT-ON state. A standby database can be in either the APPLY-OFF or APPLY-ON state.
- Compression of redo traffic over the network in a Data Guard configuration
	This feature improves the network bandwidth utilization in a Data Guard configuration by compressing archived redo logs as they are transmitted over the network to standby databases, when the log is sent to satisfy a gap at a standby database.
	See Also:
	[Section 8.3.36, "RedoCompression"](dbpropref.md)
- Better integration with the database recovery area because you can now specify `USE_DB_RECOVERY_FILE_DEST` as the value for the `AlternateLocation` and `StandbyArchiveLocation` instance-specific properties.
- New Data Guard command-line interface (DGMGRL) commands include:
	- `CONVERT DATABASE TO [SNAPSHOT | PHYSICAL] STANDBY`
		- `DISABLE FAST_START FAILOVER CONDITION`
		- `ENABLE FAST_START FAILOVER CONDITION`
		- `SHOW FAST_START FAILOVER`
	See Also:
	[Chapter 7, "Data Guard Command-Line Interface Reference"](dgmgrl.md)
- New database properties include:
	- `DGConnectIdentifier` (replaces `InitialConnectIdentifier`)
		- `ObserverConnectIdentifier`
		- `RedoCompression`
- New configuration properties include:
	- `FastStartFailoverAutoReinstate`
		- `FastStartFailoverLagLimit`
		- `FastStartFailoverPmyShutdown`
- `The LsbyTxnConsistency` database property has been renamed to `LsbyPreserveCommitOrder`
- New default of `ASYNC` for the `LogXptMode` database property