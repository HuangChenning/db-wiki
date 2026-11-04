---
title: Changed and Deprecated Features
book: Data Guard Broker
doc_id: E40771-07
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40771/deprecated_appx.htm
tags:
  - oracle
  - 11g
  - data-guard-broker
---

## A Changed and Deprecated Features

This appendix describes the Data Guard broker features that were changed, deprecated, or made obsolete. This appendix provides the following sections:

- Changed Features
- Deprecated and Obsolete Features

## A.1 Changed Features

This section contains information about Data Guard broker features that were changed:

### A.1.1 General Features That Changed

The following sections list features that have changed:

- Changed Features in Release 11.2
- Changed Features in Release 11.1
- Changed Features in Release 10.2

#### A.1.1.1 Changed Features in Release 11.2

- A restart of the primary database when upgrading the protection mode from maximum availability to maximum protection is no longer performed. If upgrading from maximum performance to maximum protection mode, a restart can be avoided, if the configuration is first upgraded to maximum availability mode.

#### A.1.1.2 Changed Features in Release 11.1

- Changed database startup behavior.
	The Data Guard broker honors the startup option specified by the database administrator. This removes the current requirement that databases belonging in a Data Guard configuration only be mounted. Previously, a primary or a logical standby database would be opened even if the DBA had only mounted it, but this will no longer happen. This also means that Data Guard actions will not start taking place until the database is opened in the case of a primary or a logical standby database. The DBA must explicitly open the database.
- Database States and descriptions have changed.
	See Table A-4, "Database State Name Changes in Release 11.1"
- The `ADD DATABASE CONNECT IDENTIFIER IS` clause is now optional if a pre-existing standby is being added to the configuration.

#### A.1.1.3 Changed Features in Release 10.2

- Changed failover behavior
	After failover to a logical standby database, the broker disables all standby databases in the configuration that were not directly involved in the failover. The disabled databases must be re-created before they can serve as standby to the new primary database. Previously, failover to a logical standby database resulted in the broker disabling only physical standby databases.
- Changed behavior for the `DelayMins` database property
	When the `DelayMins` property is set to 0, log apply services apply redo data to the standby database as soon as possible, including using real-time apply if the standby database is configured with standby redo logs.
	Additionally, if you specified the `DelayMins` and `RealTimeApply` properties on your release 10.1 database, the delay behavior might change unexpectedly. This is due to the `RealTimeApply` property being deprecated in release 10.2
	For example, if your release 10.1 database had the `DelayMins` property set to a nonzero value and the `RealTimeApply` property set to `YES`, the delay setting was ignored because the real-time apply setting overrides any delay settings. However, because in release 10.2 the `RealTimeApply` property is deprecated, the release 10.2 database will no longer be affected by the `RealTimeApply` property and the application of redo according to the time specified by the `DelayMins` property may be unexpectedly delayed.

### A.1.2 Changed Properties

The following sections list properties that have changed:

- Changed Properties in Release 11.2
- Changed Properties in Release 11.1
- Changed Properties in Release 10.2

#### A.1.2.1 Changed Properties in Release 11.2

The behavior of the following properties was changed in release 11.2:

Table A-1 Changed Properties in Release 11.2

| Property Name | Description of Change |
| --- | --- |
| `StatusReport` | The `StatusReport` property is now included automatically when a `SHOW DATABASE` command is issued, so there is no longer any need to specify it on the command line. This new behavior enhances the output of the `SHOW DATABASE` command to include a list of errors or warnings about the status of the database. In an Oracle RAC database environment, it also includes the status of all running instances. This functionality is available starting with Oracle Database 11g Release 2 (11.2.0.2). |

#### A.1.2.2 Changed Properties in Release 11.1

The following properties were changed in release 11.1:

Table A-2 Changed Properties in Release 11.1

| Property Name | Description of Change |
| --- | --- |
| `InitialConnectIdentifier` | This property has been changed to `DGConnectIdentifier`. The value of `DGConnectIdentifier` will be used for all Data Guard network traffic, all of the time.  When upgrading a 10g configuration to Oracle Database release 11.1, the `InitialConnectIdentifier` value will be retained as the new `DGConnectIdentifier` value for that database. Before the upgrade, you must ensure that the `InitialConnectIdentifier` will reach all instances if this is an Oracle RAC database. |
| `LsbyTxnConsistency` | This property has been changed to `LsbyPreserveCommitOrder` |

#### A.1.2.3 Changed Properties in Release 10.2

The following properties were changed in release 10.2:

Table A-3 Changed Properties in Release 10.2

| Property Name | Description of Change |
| --- | --- |
| `ApplyInstanceTimeout` | The default value has changed from 120 seconds to 0 seconds. |
| `ApplyParallel` | New default is `AUTO` |
| `DelayMins` | Using this property is the preferred method for delaying the application of redo data to a standby database. If you set `DelayMins` property to 0:  - Any previously configured `DelayMins` setting will be ignored. - The standby database will apply redo data as soon as possible, including using real-time apply if the standby database is configured with standby redo logs.  If you have more than one physical standby database in the configuration, Oracle recommends using Flashback Database after a failing over to a physical standby databases. You can use Flashback Database to reinstate any physical standby databases that were disabled but were not the target of the failover. |
| `LogArchiveMaxProcesses` | Range of valid values is now from 1 to 30 (was from 1 to 10) |
| `LsbyTxnConsistency` | Now imports the value of `PRESERVE_COMMIT_ORDER` from `SYSTEM.LOGSTDBY$PARAMETERS` instead of `TRANSACTION_CONSISTENCY` |
| `NetTimeout` | The default value has changed from 30 seconds to 180 seconds. |

### A.1.3 Changed State Names

Table A-4 shows the database state names that changed in Release 11.1:

Table A-4 Database State Name Changes in Release 11.1

| Database Type | State Name Prior to Oracle Database 11.1 | New State Name as of Oracle Database 11.1 |
| --- | --- | --- |
| Primary | `ONLINE` | `TRANSPORT-ON` |
| Primary | `LOG-TRANSPORT-OFF` | `TRANSPORT-OFF` |
| Physical standby | `ONLINE` | `APPLY-ON` |
| Physical standby | `LOG-APPLY-OFF` | `APPLY-OFF` |
| Physical standby | `READ-ONLY` | None <sup>Foot 1</sup> |
| Logical standby | `ONLINE` | `APPLY-ON` |
| Logical standby | `LOG-APPLY-OFF` | `APPLY-OFF` |
| All | `OFFLINE` | None <sup>Foot 2</sup> |

<sup>Footnote 1</sup> Prior to Release 11.1, the `READ-ONLY` state allowed a physical standby database to be opened read-only. In Release 11.1, this database state has been deprecated because a physical standby database can apply redo while opened read-only. Therefore this state change operation through the broker is no longer necessary.

<sup>Footnote 2</sup> This database state has been deprecated. You can shut down a database using either the SQL\*Plus `SHUTDOWN` command or the DGMGRL `SHUTDOWN` command.

See Also:

[Section 4.2, "Database States"](dbresource.md)

### A.1.4 Changed DGMGRL Features in Release 10.2

Data Guard command-line interface (DGMGRL) commands that changed in Oracle Database 10g (10.2) include:

- `FAILOVER`
- `EDIT CONFIGURATION`
- `EDIT DATABASE`
- `SHOW CONFIGURATION`

See Also:

[Chapter 7, "Data Guard Command-Line Interface Reference"](dgmgrl.md)

## A.2 Deprecated and Obsolete Features

The following sections list features that have been deprecated or made obsolete:

- Deprecated and Obsolete Features in Release 11.2
- Deprecated and Obsolete Features in Release 11.1
- Deprecated and Obsolete Features in Release 10.2

### A.2.1 Deprecated and Obsolete Features in Release 11.2

This section contains information about Data Guard broker features that were deprecated or are obsolete.

- The `HostName` configurable instance-specific property has been deprecated. This is in effect as of Oracle Database 11g Release 2 (11.2.0.2).

### A.2.2 Deprecated and Obsolete Features in Release 11.1

This section contains information about Data Guard broker features that were deprecated or are obsolete.

- Deprecated database properties include:
	- LocalListenerAddress
		- The `READ-ONLY` state for physical standby databases has been deprecated
		- The `OFFLINE` and `ONLINE` states have been deprecated
- The `ADD DATABASE ... MAINTAINED AS {PHYSICAL|LOGICAL}` statement is deprecated. Specifically, the `MAINTAINED AS` clause of `ADD DATABASE` command is deprecated. The broker now automatically finds out the standby database type.

#### A.2.2.1 Deprecated and Obsolete Properties in Release 11.1

Table A-5 Deprecated and Obsolete Properties in Release 11.1

| Deprecated Property | Replacement Property (if any) |
| --- | --- |
| `LsbyTxnConsistency` | `LsbyPreserveCommitOrder` |

### A.2.3 Deprecated and Obsolete Features in Release 10.2

This section contains information about Data Guard broker features that were deprecated or are obsolete.

#### A.2.3.1 Deprecated and Obsolete Properties in Release 10.2

Table A-6 Deprecated and Obsolete Properties in Release 10.2

| Deprecated Property | Replacement Property (if any) |
| --- | --- |
| `ApplyNext` | No replacement. |
| `ApplyNoDelay` | Set the `DelayMins` property to zero (0). |
| `AsyncBlocks` | None. Specifying the number of blocks is no longer necessary. The transport mode is determined automatically by redo transport services, based on the protection mode defined for the Data Guard configuration. |
| `RealTimeApply` | Set the `DelayMins` property to zero (0). |