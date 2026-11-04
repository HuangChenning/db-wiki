---
title: Data Guard Broker Properties
book: Data Guard Broker
doc_id: E40771-07
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40771/dbpropref.htm
tags:
  - oracle
  - 11g
  - data-guard-broker
---

## 8 Data Guard Broker Properties

This chapter describes the various configuration and database properties that help you view and control the behavior of entire broker configurations, individual databases, redo transport services, and log apply services.

This chapter discusses the following topics:

Properties have either configuration-wide scope, database-wide scope, or instance-specific scope. Configuration-wide properties control the behavior of the broker on all databases in the configuration. The values of such properties apply uniformly across all databases in the configuration.

Database-wide properties allow you to view or control the behavior of a specific database. If the database (primary or standby) is an Oracle RAC database consisting of multiple instances, the value of such a property applies uniformly across all instances of that database.

Instance-specific properties allow you to view or control the behavior of an individual database instance. Such a property exists for all instances of an Oracle RAC database, but its value may differ from one specific instance to another.

Note:

This chapter presents properties primarily from the point of view of the Data Guard command-line interface (DGMGRL). Using DGMGRL, the properties described in this chapter may be viewed or modified using discrete DGMGRL commands.

Enterprise Manager explicitly presents some of these properties on the Edit Properties page. Information from other properties may be implicitly incorporated into other Web pages displayed by Enterprise Manager. Each property's description in this chapter indicates how Enterprise Manager presents that property.

## 8.1 Configuration Properties

Configuration properties control the behavior of the broker configuration. You can view and dynamically update the values of these properties using either DGMGRL or Enterprise Manager. However, some properties can only be updated through DGMGRL.

A configuration property has configuration-wide scope; meaning that the value you set for the property applies uniformly to each database in the configuration.

The following sections describe the configuration properties:

- BystandersFollowRoleChange
- CommunicationTimeout
- ExternalDestination1
- ExternalDestination2
- FastStartFailoverAutoReinstate
- FastStartFailoverLagLimit
- FastStartFailoverPmyShutdown
- FastStartFailoverThreshold
- ObserverOverride
- ObserverReconnect
- OperationTimeout
- PrimaryLostWriteAction
- TraceLevel

### 8.1.1 BystandersFollowRoleChange

The `BystandersFollowRoleChange` configuration property allows the user to decide whether the broker should determine whether bystander standby databases will be viable standby databases for the new primary database as part of performing a complete failover. Setting the property to `ALL` directs the broker to evaluate and detect each standby database that can be a viable standby database to the new primary database, as part of failover processing. Setting the property to `NONE` directs the broker to perform failover without evaluating standby database viability. This option decreases the processing time for failover, but disables broker management of all databases in the configuration. If fast-start failover is enabled, the observer will automatically reinstate the standby databases after failover has completed. Otherwise, you will have to manually reinstate the standby databases after failover has completed.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid value | `ALL` or `NONE` |
| Broker default | `ALL` |
| Imported? | No |
| Parameter class | Not applicable |
| Role | Primary and standby |
| Standby type | Not applicable |
| Corresponds to | Not applicable |
| Scope | Broker configuration. This property will be consumed by broker on the database that is the target of a complete failover. |
| Enterprise Manager name | Not applicable |

### 8.1.2 CommunicationTimeout

The `CommunicationTimeout` configuration property allows you to decide how many seconds the broker should wait before timing out its network communication between databases in the configuration. A value of zero indicates that a network communication should never be timed out.

| Category | Description |
| --- | --- |
| Datatype | Integer |
| Valid values | \>= 0 |
| Broker default | 180 seconds |
| Imported? | No |
| Parameter class | Not applicable |
| Role | Primary and standby |
| Standby type | Not applicable |
| Corresponds to | Not applicable |
| Scope | Broker configuration. This property will be consumed by broker on all databases in the configuration. |
| Enterprise manager name | Not applicable |

### 8.1.3 ExternalDestination1

The `ExternalDestination1` configuration property is used to specify a redo transport destination that can receive redo data from the current primary database. To set up transport of redo data to the specified destination, the broker uses the values specified for this parameter to define a `LOG_ARCHIVE_DEST_` `n` initialization parameter on the primary database. The broker also monitors the health of the transport to the specified destination.

Note:

In Oracle Database 11g Release 2 (11.2.0.4), the `ExternalDestination1` configuration property supports Zero Data Loss Recovery Appliance as a redo transport destination.

After a role change, the broker automatically sets up a `LOG_ARCHIVE_DEST_` `n` initialization parameter on the new primary database to ship redo data to the specified destination.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | Any `LOG_ARCHIVE_DEST_` `n` attributes, with the exception of the following: - `ALTERNATE` - `LOCATION` - `MAX_FAILURES` - `SYNC` - `VALID_FOR` - `TEMPLATE` - `MANDATORY` - `DELAY` - `NET_TIMEOUT`  See [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/log_arch_dest_param.htm#SBYDB01100) for more information about the `LOG_ARCHIVE_DEST_` `n` parameter. |
| Broker default | Empty string |
| Imported? | No |
| Parameter class | Not applicable |
| Role | Primary |
| Standby type | Not applicable |
| Corresponds to | Not applicable |
| Scope | Configuration |
| Enterprise Manager name | Not applicable |

### 8.1.4 ExternalDestination2

The `ExternalDestination2` configuration property is used to specify a redo transport destination that can receive redo data from the current primary database. To set up transport of redo data to the specified destination, the broker uses the values specified for this parameter to define a `LOG_ARCHIVE_DEST_` `n` initialization parameter on the primary database. The broker also monitors the health of the transport to the specified destination.

Note:

In Oracle Database 11g Release 2 (11.2.0.4), the `ExternalDestination2` configuration property supports Zero Data Loss Recovery Appliance as a redo transport destination.

After a role change, the broker automatically sets up a `LOG_ARCHIVE_DEST_` `n` initialization parameter on the new primary database to ship redo data to the specified destination.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | Any `LOG_ARCHIVE_DEST_` `n` attributes, with the exception of the following: - `ALTERNATE` - `LOCATION` - `MAX_FAILURES` - `SYNC` - `VALID_FOR` - `TEMPLATE` - `MANDATORY` - `DELAY` - `NET_TIMEOUT`  See [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/log_arch_dest_param.htm#SBYDB01100) for more information about the `LOG_ARCHIVE_DEST_` `n` parameter. |
| Broker default | Empty string |
| Imported? | No |
| Parameter class | Not applicable |
| Role | Primary |
| Standby type | Not applicable |
| Corresponds to | Not applicable |
| Scope | Configuration |
| Enterprise Manager name | Not applicable |

### 8.1.5 FastStartFailoverAutoReinstate

The `FastStartFailoverAutoReinstate` configuration property causes the former primary database to be automatically reinstated if a fast-start failover was initiated because the primary database was either isolated or had crashed. To prevent automatic reinstatement of the former primary database in these cases, set this configuration property to `FALSE`.

The broker never automatically reinstates the former primary database if a fast-start failover was initiated because a user configuration condition was detected or was requested by an application calling the `DBMS_DG.INITIATE_FS_FAILOVER` function.

| Category | Description |
| --- | --- |
| Datatype | Boolean |
| Valid value | `TRUE` or `FALSE` |
| Broker default | `TRUE` |
| Imported? | No |
| Parameter class | Not applicable |
| Role | Primary and standby |
| Standby type | Not applicable |
| Corresponds to | Not applicable |
| Scope | Broker configuration. This property will be consumed by the observer after fast-start failover has been enabled. |
| Enterprise Manager name | Automatically Reinstate Primary |

### 8.1.6 FastStartFailoverLagLimit

The `FastStartFailoverLagLimit` configuration property establishes an acceptable limit, in seconds, that the standby is allowed to fall behind the primary in terms of redo applied, beyond which a fast-start failover will not be allowed. The lowest possible value is 10 seconds.

This property is used when fast-start failover is enabled and the configuration is operating in maximum performance mode.

| Category | Description |
| --- | --- |
| Datatype | Integer |
| Valid value | Integral number of seconds. Must be greater than, or equal to, 10. |
| Broker default | 30 seconds |
| Imported? | No |
| Parameter class | Not applicable |
| Role | Primary and standby |
| Standby type | Not applicable |
| Corresponds to | Not applicable |
| Scope | Broker configuration. This property will be consumed by the primary database after fast-start failover has been enabled. |
| Enterprise Manager name | Lag Limit |

### 8.1.7 FastStartFailoverPmyShutdown

The `FastStartFailoverPmyShutdown` configuration property causes the primary database to shut down if fast-start failover is enabled and `V$DATABASE.FS_FAILOVER_STATUS` indicates the primary has been `STALLED` for longer than `FastStartFailoverThreshold` seconds. In such a situation, it is likely that the primary has been isolated and a fast-start failover has already occurred. A value of `TRUE` helps to ensure that an isolated primary database cannot satisfy user queries.

Setting this property to `FALSE` will not prevent the primary database from shutting down if a fast-start failover occurred because a user configuration condition was detected or was requested by an application by calling the `DBMS_DG.INITIATE_FS_FAILOVER` function.

| Category | Description |
| --- | --- |
| Datatype | Boolean |
| Valid value | `TRUE` or `FALSE` |
| Broker default | `TRUE` |
| Imported? | No |
| Parameter class | Not applicable |
| Role | Primary and standby |
| Standby type | Not applicable |
| Corresponds to | Not applicable |
| Scope | Broker configuration. This property will be consumed by the primary database after fast-start failover has been enabled. |
| Enterprise Manager name | Automatically Shutdown Primary |

### 8.1.8 FastStartFailoverThreshold

The `FastStartFailoverThreshold` configuration property defines the number of seconds the observer attempts to reconnect to the primary database before initiating a fast-start failover to the target standby database. The time interval starts when the observer first loses connection with the primary database. If the observer is unable to regain a connection to the primary database within the specified time, then the observer initiates a fast-start failover. See Step [4](sofo.md) in [Section 5.5.2](sofo.md) for more information about setting this property.

The observer ignores the threshold completely if a configurable fast-start failover condition is detected or an application has requested that fast-start failover be initiated.

For help in determining an appropriate value for this property, you can use the information provided in the `V$FS_OBSERVER_HISTOGRAM` view. This view displays statistics that are based on the frequency of successful pings between the observer and primary database for different time intervals. (See [Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1151.htm#REFRN30735) for a description of the `V$FS_OBSERVER_HISTOGRAM` view.)

| Category | Description |
| --- | --- |
| Datatype | Integer |
| Valid value | Integral number of seconds. Must be greater than, or equal to, 6. |
| Broker default | 30 seconds |
| Imported? | No |
| Parameter class | Not applicable |
| Role | Target standby database that is about to fail over to the primary role |
| Standby type | Not applicable |
| Corresponds to | Not applicable |
| Scope | Broker configuration. This property will be consumed by the observer after fast-start failover has been enabled. |
| Enterprise Manager name | Oracle Enterprise Manager presents this as "Failover Threshold" on the Data Guard Overview page. |

### 8.1.9 ObserverOverride

The `ObserverOverride` configuration property, when set to `TRUE`, allows an automatic failover to occur when the observer has lost connectivity to the primary, even if the standby has a healthy connection to the primary.

The `ObserverOverride` configuration property is available only in Oracle Database 11g Release 2 (11.2.0.4) and higher.

| Category | Description |
| --- | --- |
| Datatype | Boolean |
| Valid values | `TRUE` or `FALSE` |
| Broker default | `FALSE` |
| Imported? | No |
| Parameter class | Not applicable |
| Role | Primary and Standby |
| Standby type | Not applicable |
| Corresponds to | Not applicable |
| Scope | Broker configuration. This property will be consumed by the observer after fast-start failover has been enabled. |
| Enterprise Manager name | Not applicable |

### 8.1.10 ObserverReconnect

The `ObserverReconnect` configuration property specifies how often the observer establishes a new connection to the primary database. When this property is set to the default value of 0, the observer creates and maintains a connection to the primary database, but it does not periodically create a new connection to the primary database. While this eliminates the processing overhead associated with periodically establishing a new observer connection to the primary database, it also prevents the observer from detecting that it is not possible to create new connections to the primary database. Oracle recommends that this property be set to a value that is small enough to allow timely detection of faults at the primary database, but large enough to limit the overhead associated with periodic observer connections to an acceptable level.

The `ObserverReconnect` configuration property is available only in Oracle Database 11g Release 2 (11.2.0.4) and higher.

| Category | Description |
| --- | --- |
| Datatype | Integer |
| Valid values | \>=0 |
| Broker default | 0 |
| Imported? | No |
| Parameter class | Not applicable |
| Role | Primary and standby |
| Standby type | Not applicable |
| Corresponds to | Not applicable |
| Scope | Broker configuration. This property will be consumed by the observer after fast-start failover has been enabled. |
| Enterprise Manager name | Not applicable |

### 8.1.11 OperationTimeout

The `OperationTimeout` configuration property specifies the maximum amount of time the broker should wait for health check, get monitorable property, and set property operations to complete.

| Category | Description |
| --- | --- |
| Datatype | Integer |
| Valid values | \>= 30 and <= 600 |
| Broker default | 30 seconds |
| Imported? | No |
| Parameter class | Not applicable |
| Role | Primary and standby |
| Standby type | Not applicable |
| Corresponds to | Not applicable |
| Scope | Broker configuration. This property will be consumed by broker on all databases in the configuration. |
| Enterprise Manager name | Not applicable |

### 8.1.12 PrimaryLostWriteAction

The `PrimaryLostWriteAction` configuration property determines what action is taken if a standby database detects that a lost write has occurred at the primary database:

- `CONTINUE` - The primary database continues operating if a standby database detects that a lost write has occurred at the primary database. This is the default action.
- `SHUTDOWN` - The primary database performs a shutdown abort if a standby database detects that a lost write has occurred at the primary database.

Fast start failover is disabled if a standby detects that a lost write has occurred at the primary database. Automatic failover will therefore not occur if a standby detects that a lost write has occurred at the primary database, even if `PrimaryLostWriteAction` is set to `SHUTDOWN`.

Diagnostic information is written to the database alert and broker logs at the primary database and at the standby database where the lost write was detected.

If a lost write occurs at the primary database, then follow the guidelines in "Resolving ORA-752 or ORA-600 \[3020\] During Standby Recovery" in My Oracle Support Note 1265884.1 located at `http://support.oracle.com`.

The `PrimaryLostWriteAction` configuration property is available only in Oracle Database 11g Release 2 (11.2.0.4).

Note:

The `DB_LOST_WRITE_PROTECT` database initialization parameter must be set to `TYPICAL` or `FULL` at the primary database and at each standby database in the configuration to ensure that lost primary writes can be detected by all standby databases in the configuration.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | `CONTINUE` or `SHUTDOWN` |
| Broker default | `CONTINUE` |
| Imported? | No |
| Parameter class | Not applicable |
| Role | Primary and standby |
| Standby type | Not applicable |
| Corresponds to | Not applicable |
| Scope | Broker configuration |
| Enterprise Manager name | Not applicable |

### 8.1.13 TraceLevel

The `TraceLevel` configuration property is used to control the amount of tracing performed by the broker for every member in the configuration. Setting the property to `USER` limits the tracing to completed operations and to any warning or error messages resulting from an operation or health check. Setting the property to `SUPPORT` increases the amount of tracing to include lower-level information needed by Oracle Support Services.

The `TraceLevel` configuration property is available only in Oracle Database 11g Release 2 (11.2.0.3) and higher.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | `USER`, `SUPPORT` |
| Broker default | `USER` |
| Imported? | No |
| Parameter class | Not applicable |
| Role | Primary and standby |
| Standby type | Not applicable |
| Corresponds to | Not applicable |
| Scope | Database |
| Enterprise Manager name | Not applicable |

## 8.2 Monitorable (Read-Only) Database Properties

Monitorable database properties allow you to view information related to the database or the instance, but you cannot change the values of these properties. You can view all of the monitorable properties using the DGMGRL `SHOW` commands.

Note:

Information for monitorable properties can be seen only when broker management of the database is enabled. Enterprise Manager displays the information obtained from these properties on the Property page.

If the database is an Oracle RAC database, the output values of some properties may also show instance-specific information. For example if the primary database is an Oracle RAC database, `LogXptStatus` may show `Instance1` transmitting redo data to `Standby2` has an error and `Instance2` transmitting redo data to `Standby4` has an error.

The following sections describe the monitorable database properties:

- InconsistentLogXptProps (Inconsistent Redo Transport Properties)
- InconsistentProperties (Inconsistent Database Properties)
- LogXptStatus (Redo Transport Status)
- LsbyFailedTxnInfo (Logical Standby Failed Transaction Information)
- LsbyParameters (Logical Standby Parameters)
- LsbySkipTable (Logical Standby Skip Table)
- LsbySkipTxnTable (SQL Apply Skip Transaction Table)
- RecvQEntries (Receive Queue Entries)
- SendQEntries (Send Queue Entries)
- TopWaitEvents

### 8.2.1 InconsistentLogXptProps (Inconsistent Redo Transport Properties)

The `InconsistentLogXptProps` monitorable database property returns a table that shows all properties related to redo transport services whose values are inconsistent between the broker configuration file and the runtime value in the database.

Although the properties reported in this table are database-specific properties, the inconsistency is reported on an instance-specific basis. A database-specific property only ensures that there is one value in the broker's configuration file for all instances sharing the database, but the runtime values among the instances can be different. This means that a database-specific property may be inconsistent only on some instances.

This property pertains to the primary database. The table contains the following columns:

- `INSTANCE_NAME`
	The value identifying the SID for the instance.
- `STANDBY_NAME`
	The database unique name (`DB_UNIQUE_NAME`) of the standby database to which this redo transport services property pertains.
- `PROPERTY_NAME`
	The name of the redo transport services property with an inconsistent value.
- `MEMORY_VALUE`
	The runtime value being used in the database.
- `BROKER_VALUE`
	The value of the redo transport services property saved in the broker configuration file.

### 8.2.2 InconsistentProperties (Inconsistent Database Properties)

The `InconsistentProperties` monitorable database property returns a table that shows all database properties whose values contained in the broker configuration file are inconsistent with the values in the corresponding server parameter file or the runtime values in the database.

The properties reported in this table can be either database-specific properties or instance-specific properties. A database-specific property only ensures that there is one value in the broker's configuration file for all instances sharing the database, but the runtime memory values or SPFILE values among the instances can be different. This means that a database-specific property may be inconsistent only on some instances.

Each individual database has this property. The table contains the following columns:

- `INSTANCE_NAME`
	The value identifying the SID for the instance.
- `PROPERTY_NAME`
	The name of the database property with the inconsistent value.
- `MEMORY_VALUE`
	The corresponding runtime value being used in the database.
- `SPFILE_VALUE`
	The corresponding value saved in the server parameter file (SPFILE).
- `BROKER_VALUE`
	The value of the database property saved in the broker configuration file.

### 8.2.3 LogXptStatus (Redo Transport Status)

The `LogXptStatus` monitorable database property returns a table that contains the error status of redo transport services for each of the enabled standby databases. This property pertains to the primary database.

The table contains the following columns:

- `PRIMARY_INSTANCE_NAME`
	The value identifying the SID for the instance on the primary database.
- `STANDBY_DATABASE_NAME`
	The database unique name (`DB_UNIQUE_NAME`) of the standby database.
- `ERROR`
	The text of the redo transport error. If there is no error, the field is empty.

Each entry in the table indicates the status of redo transport services on one primary instance to one standby database.

The error status can be an empty string, which indicates there is no error.

In the following example, the `STATUS` from `South_Sales` is empty because there is no error for the `South_Sales` destination. The `South_Report` destination returned the `ORA-01034` message.

```
DGMGRL> SHOW DATABASE 'North_Sales' 'LogXptStatus' ;
LOG TRANSPORT STATUS
PRIMARY_INSTANCE_NAME STANDBY_DATABASE_NAME               STATUS
         north_sales1           South_Sales
         north_sales1          South_Report    ORA-01034: ORACLE not available
```

### 8.2.4 LsbyFailedTxnInfo (Logical Standby Failed Transaction Information)

The `LsbyFailedTxnInfo` monitorable database property identifies a failed transaction that caused log apply services to stop. This property contains a string with the following values from the `DBA_LOGSTDBY_EVENTS` view:

- `XIDUSN`: Transaction ID undo segment number
- `XIDSLT`: Transaction ID slot number
- `XIDSQN`: Transaction ID sequence number
- `STATUS_CODE`: Status (or Oracle error code) belonging to the `STATUS` message
- `STATUS`: Description of the current activity of the process or the reason why log apply services stopped

The transaction IDs and status information are separated by a string of number signs (###).

This property pertains to a logical standby database.

### 8.2.5 LsbyParameters (Logical Standby Parameters)

The `LsbyParameters` monitorable database property contains a string that identifies the value of `MAX_SGA` (maximum system global area) and `MAX_SERVERS` (maximum number of parallel query servers) specifically reserved for log apply services. These values are separated by a string of number signs (###) in the `LsbyParameters` property.

This property pertains to a logical standby database.

### 8.2.6 LsbySkipTable (Logical Standby Skip Table)

The `LsbySkipTable` monitorable database property lists the SQL Apply skip specifications. These skip specifications specify filters for SQL Apply to skip applying a certain class of online redo log files on the logical standby database. This property returns a table with the following columns from the `DBA_LOGSTDBY_SKIP` view:

- `ERROR`
	Indicates if the statement should be skipped (`Y`) or if errors should be returned for the statement (`N`)
- `STATEMENT_OPT`
	Indicates the type of statement that should be skipped
- `SCHEMA`
	The schema name for which this skip option should be used
- `NAME`
	Name of the object for which this skip option should be used
- `PROCEDURE`
	Name of the stored procedure to execute when processing the skip option

This property pertains to a logical standby database.

### 8.2.7 LsbySkipTxnTable (SQL Apply Skip Transaction Table)

The `LsbySkipTxnTable` monitorable database property lists the skip settings chosen. This property returns a table with following columns:

- `XIDUSN`: Transaction ID undo segment number
- `XIDSLT`: Transaction ID slot number
- `XIDSQN`: Transaction ID sequence number
- `ACTIVE`: Description of the current activity of the process or the reason why SQL Apply stopped

This property pertains to SQL Apply.

### 8.2.8 RecvQEntries (Receive Queue Entries)

The `RecvQEntries` monitorable database property returns a table indicating all log files that were received by the standby database but have not yet been applied. If no rows are returned, it implies all log files received have been applied. This property pertains to a standby database.

The table contains the following columns in the order shown:

- `STATUS`
	The `STATUS` column is set to one of the following values for a log file on a logical standby database:
	- `NOT_APPLIED`: No redo records in this log file have been applied.
		- `PARTIALLY_APPLIED`: Some of the redo records in this log file have been applied while others have not.
		- `COMMITTED_TRANSACTIONS_APPLIED`: This status value only applies to a logical standby database. All redo records belonging to the committed transactions have been applied. Redo records belonging to uncommitted transactions have not been read by LogMiner and may still be needed when the transactions are committed in the future. Therefore, it is not safe yet to discard this online redo log file.
- `RESETLOGS_ID`
	Resetlogs identifier associated with the archived redo log file
- `THREAD`
	The redo thread number
- `LOG_SEQ`
	The online redo log file sequence number
- `TIME_GENERATED`
	The first time when the online redo log file was written to the primary database
- `TIME_COMPLETED`
	The next time when the log file was archived on the primary database (corresponds to the `NEXT_CHANGE#` column)
- `FIRST_CHANGE#`
	First change number in the archived redo log file
- `NEXT_CHANGE#`
	First change in the next log file
- `SIZE (KBs)`
	The `SIZE` of the online redo log file in kilobytes

For example:

```
DGMGRL> SHOW DATABASE 'South_Sales' 'RecvQEntries' ;
              STATUS     RESETLOGS_ID           THREAD
LOG_SEQ          TIME_GENERATED       TIME_COMPLETED    FIRST_CHANGE#
NEXT_CHANGE#        SIZE (KBs)
         NOT_APPLIED        497198843                1                    5
06/20/2003 14:55:38  06/20/2003 16:31:26           202138
210718             7364
         NOT_APPLIED        497198843                1                    6
06/20/2003 16:31:26  06/20/2003 16:31:39           210718
210753               13
         NOT_APPLIED        497198843                1                    7
06/20/2003 16:31:39  06/20/2003 16:31:54           210753
210758                1
         NOT_APPLIED        497198843                1                    8
06/20/2003 16:31:54  06/20/2003 16:31:59           210758
210789               11
```

Note:

Enterprise Manager displays this information on the Log File Details page.

### 8.2.9 SendQEntries (Send Queue Entries)

The `SendQEntries` monitorable database property returns a table that shows all log files on the primary database that were not successfully archived to one or more standby databases. This property pertains to the primary database.

The table contains the following columns:

- `STANDBY_NAME`
	The value can be empty or it can contain the database unique name (`DB_UNIQUE_NAME`) of a standby database. If empty, the `STATUS` column will contain a value of `CURRENT` or `NOT_ARCHIVED`.
- `STATUS`
	The `STATUS` column is set to one of the following values:
	- `CURRENT`: A log file to which online redo is currently being written.
		- `NOT_ARCHIVED`: A completed online redo log file that has not been archived locally.
		- `ARCHIVED`: A completed log file that has been archived locally but has not been transmitted to the standby database specified in the `STANDBY_NAME` column.
	The table contains exactly one row with the value of `STATUS=CURRENT`. There can be multiple rows with the value `STATUS=ARCHIVED` or `STATUS=NOT_ARCHIVED`.
- `RESETLOGS_ID`
	Resetlogs identifier associated with the archived redo log file
- `THREAD`
	The redo thread number.
- `LOG_SEQ`
	The log sequence number. Multiple rows may have the same `LOG_SEQ` value (for different `STANDBY_NAME` values).
- `TIME_GENERATED`
	The first time when the online redo log file was written to the primary database.
- `TIME_COMPLETED`
	The next time when the log file was archived on the primary database (corresponds to the `NEXT_CHANGE#` column).
- `FIRST_CHANGE#`
	First change number in the archived redo log file.
- `NEXT_CHANGE#`
	First change in the next log file.
- `SIZE (KBs)`
	The `SIZE` of the online redo log file in kilobytes.

For example, the following shows output from a `SHOW DATABASE` command:

```
DGMGRL> SHOW DATABASE 'North_Sales' 'SendQEntries' ;
PRIMARY_SEND_QUEUE
        STANDBY_NAME       STATUS     RESETLOGS_ID
THREAD              LOG_SEQ       TIME_GENERATED       TIME_COMPLETED
FIRST_CHANGE#     NEXT_CHANGE#       SIZE (KBs)
       South_Sales   ARCHIVED        497198843
1                    9  06/20/2003 16:31:59  06/20/2003 16:39:57
210789           211411              186
       South_Sales   ARCHIVED        497198843
1                   10  06/20/2003 16:39:57  06/20/2003 16:40:01
211411           211415                1
       South_Sales   ARCHIVED        497198843
1                   11  06/20/2003 16:40:01  06/20/2003 16:40:07
211415           211418                1
                          CURRENT        497198843
1                   12  06/20/2003 16:40:07
211418                                 1
```

Note:

Enterprise Manager displays this information on the Log File Details page.

### 8.2.10 TopWaitEvents

The `TopWaitEvents` monitorable database property specifies the 5 events with the longest waiting time in the specified instance. The events and their waiting time are retrieved from `V$SYSTEM_EVENT`. Each instance in the configuration has this property. This property is an instance-specific monitorable property. The table contains the following columns in the order shown:

- Event
	The system wait event.
- Wait Time
	The total amount of time waited for this event in hundredths of a second.

The following example shows output from a `SHOW INSTANCE` command:

```
DGMGRL> SHOW INSTANCE north_sales1 'TopWaitEvents';
TOP SYSTEM WAIT EVENTS
               Event            Wait Time
   rdbms ipc message               671350
SQL*Net message from client         62390
          pmon timer                47897
  Queue Monitor Wait                43016
 wakeup time manager                38508
```

## 8.3 Configurable Database Properties

Configurable database properties control the behavior of databases in a broker configuration. You can view and dynamically update the values of these properties using either DGMGRL or Enterprise Manager. However, some properties can only be updated through DGMGRL.

In most cases, the configurable database property is said to have database-wide scope; meaning the value you set for the property applies uniformly to each instance of the database. However, in a few cases, the configurable database property is said to have instance-specific scope; meaning, for a multiple-instance database environment, it is possible that the values of some particular properties may differ from one instance of the database to the next. Table 8-1 lists each configurable database property and indicates if the scope of the property is database-wide or instance-specific. If the Scope column contains:

- Database—The value of the property is database wide, not instance or configuration specific.
- Instance—The value of the property is instance specific, not database or configuration specific.
	If there is an asterisk (\*) present, it indicates that the property value can be set for all instances of an Oracle RAC database using the `EDIT INSTANCE * ON DATABASE` command.
- Configuration—The value of the property is configuration wide, not instance or database specific.

Table 8-1 Configurable Properties

| Configurable Property Name | Scope | Pertains To |
| --- | --- | --- |
| AlternateLocation | Instance | Redo transport services |
| ApplyInstanceTimeout | Database | Redo Apply and SQL Apply |
| ApplyLagThreshold | Database | Redo transport services |
| ApplyParallel | Database | Redo Apply |
| ArchiveLagTarget | Database | Redo transport services |
| Binding | Database | Redo transport services |
| DbFileNameConvert | Database | Redo Apply |
| DelayMins | Database | Redo Apply and SQL Apply |
| DGConnectIdentifier | Database | Broker communication, Redo transport services |
| FastStartFailoverTarget | Database | Fast-start failover |
| LogArchiveFormat | Instance \* | Redo transport services |
| LogArchiveMaxProcesses | Database | Redo transport services |
| LogArchiveMinSucceedDest | Database | Redo transport services |
| LogArchiveTrace | Instance \* | Diagnosis |
| LogFileNameConvert | Database | Redo Apply |
| LogShipping | Database | Redo transport services |
| LogXptMode | Database | Redo transport services |
| LsbyASkipCfgPr | Database | SQL Apply |
| LsbyASkipErrorCfgPr | Database | SQL Apply |
| LsbyASkipTxnCfgPr | Database | SQL Apply |
| LsbyDSkipCfgPr | Database | SQL Apply |
| LsbyDSkipErrorCfgPr | Database | SQL Apply |
| LsbyDSkipTxnCfgPr | Database | SQL Apply |
| LsbyMaxEventsRecorded | Database | SQL Apply |
| LsbyMaxSga | Instance \* | SQL Apply |
| LsbyMaxServers | Instance \* | SQL Apply |
| LsbyPreserveCommitOrder | Database | SQL Apply |
| LsbyRecordAppliedDdl | Database | SQL Apply |
| LsbyRecordSkipDdl | Database | SQL Apply |
| LsbyRecordSkipErrors | Database | SQL Apply |
| MaxConnections | Database | Redo transport services |
| MaxFailure | Database | Redo transport services |
| NetTimeout | Database | Redo transport services |
| ObserverConnectIdentifier | Database | Fast-start failover |
| PreferredApplyInstance | Database | Redo Apply and SQL Apply |
| RedoCompression | Database | Redo transport services |
| ReopenSecs | Database | Redo transport services |
| SidName | Instance | Instance identification |
| StandbyArchiveLocation | Instance | Redo transport services |
| StandbyFileManagement | Database | Redo Apply and SQL Apply |
| StaticConnectIdentifier | Instance | Instance Startup |
| TransportDisconnectedThreshold | Database | Redo transport services |
| TransportLagThreshold | Database | Redo transport services |

See Also:

[Chapter 4](dbresource.md) for more information about database property management

Note:

When a broker configuration with its primary database is created and standby databases are added to the configuration, the broker imports existing settings from the databases to set many of the properties. If importing an existing setting fails, or if a property value is not imported, then the broker uses a broker default value. The default values and whether or not a property is imported is indicated within each property description.

### 8.3.1 AlternateLocation

The `AlternateLocation` configurable database property specifies an alternate disk location to store the archived redo log files in the standby when the location specified by the `StandbyArchiveLocation` configurable database property fails. The property has instance-specific scope, and the location it specifies has to be accessible by the instance.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | Directory specification on system where the standby instance is located |
| Broker default | Empty string |
| Imported? | No |
| Parameter class | Dynamic |
| Role | Standby <sup>Foot 1</sup> |
| Standby type | Physical, logical, or snapshot |
| Corresponds to | - On the standby instance, the `LOCATION` attribute for the `LOG_ARCHIVE_DEST_` `n` initialization parameter that represents an alternate destination of the local destination that matches the configurable database property `StandbyArchiveLocation` - On the primary database, the `TEMPLATE` attribute for the `LOG_ARCHIVE_DEST_` `n` initialization parameter that represents an alternate destination |
| Scope | Instance |
| Enterprise Manager name | `Alternate Standby Location` |

<sup>Footnote 1</sup> Although this property is set for the standby instance, it is indirectly related to redo transport services for the primary database. The broker sets up both an alternate local destination on the standby instance and an alternate remote destination on the primary database.

Note:

On a logical standby database, Oracle recommends the `LOCATION` attribute of the `LOG_ARCHIVE_DEST_` `n` initialization parameter for the local destination be different from the value of `AlternateLocation` configurable database property.

### 8.3.2 ApplyInstanceTimeout

The `ApplyInstanceTimeout` configurable database property specifies the number of seconds the broker waits after detecting the current apply instance failed before initiating the apply instance failover.

| Category | Description |
| --- | --- |
| Datatype | Integer |
| Valid values | `>=0` (seconds) |
| Broker default | `0` (results in immediate apply instance failover) |
| Imported? | No |
| Parameter class | Not applicable |
| Role | Standby |
| Standby type | Physical or logical |
| Corresponds to | Not applicable |
| Scope | Database |
| Enterprise Manager name | Not applicable |

### 8.3.3 ApplyLagThreshold

The `ApplyLagThreshold` configurable database property generates a warning status for a logical or physical standby when the database's apply lag exceeds the value specified by the property. The property value is expressed in seconds. A value of 0 seconds results in no warnings being generated when an apply lag exists.

The `ApplyLagThreshold` configuration property is available only in Oracle Database 11g Release 2 (11.2.0.4) and higher.

| Category | Description |
| --- | --- |
| Datatype | Number |
| Valid values | \>=0 |
| Broker default | 0 seconds |
| Imported? | No |
| Parameter class | Not applicable |
| Role | Standby |
| Standby type | Physical, logical |
| Corresponds to | Not applicable |
| Scope | Database |
| Enterprise Manager name | Not applicable |

### 8.3.4 ApplyParallel

The `ApplyParallel` configurable database property specifies whether Redo Apply should use multiple processes to apply redo data to the physical standby database. If Redo Apply is shut off, then setting the property has no immediate effect. However, when Redo Apply is running again, the value of the property is used to determine the parallel apply behavior of Redo Apply.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | - `AUTO` —the number of parallel processes used for Redo Apply is automatically determined by Oracle based on the number of CPUs that the system has. - `NO` —no parallel apply - `2`, `3`, and so on—manually specify the number of parallel processes used for Redo Apply. (Specifying `0` is the same as specifying `NO`; specifying `1` is the same as specifying `AUTO`.) |
| Broker default | `AUTO` |
| Imported? | No |
| Parameter class | Not applicable |
| Role | Standby |
| Standby type | Physical |
| Corresponds to | - `AUTO` corresponds to the `PARALLEL` clause of the `ALTER DATABASE RECOVER MANAGED STANDBY DATABASE` statement - `NO` corresponds to the `NOPARALLEL` clause of the `ALTER DATABASE RECOVER MANAGED STANDBY DATABASE` statement - `2`, `3`, and so on corresponds to the `PARALLEL` `n` clause of the `ALTER DATABASE RECOVER MANAGED STANDBY DATABASE` statement |
| Scope | Database |
| Enterprise Manager name | Not applicable |

### 8.3.5 ArchiveLagTarget

The `ArchiveLagTarget` configurable database property limits the amount of data that can be lost and effectively increases the availability of the standby database by forcing a log switch after the amount of time you specify (in seconds) elapses. That way, the standby database will not miss redo records generated from a time range longer than the value set for the `ARCHIVE_LAG_TARGET` initialization parameter.

| Category | Description |
| --- | --- |
| Datatype | Number |
| Valid values | Seconds (either 0 seconds, or any number from 60 to 7200 seconds) |
| Broker default | 0 (disabled) |
| Imported? | Yes, from the `ARCHIVE_LAG_TARGET` initialization parameter |
| Parameter class | Dynamic |
| Role | Primary |
| Standby type | Not applicable |
| Corresponds to | `ARCHIVE_LAG_TARGET=` `seconds` initialization parameter |
| Scope | Database |
| Enterprise Manager name | `Archive Lag Target` |

### 8.3.6 Binding

The `Binding` configurable database property specifies whether the standby destination is `MANDATORY` or `OPTIONAL`.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | - `MANDATORY` 	You can specify a policy for reuse of online redo log files using the `MANDATORY` value. If the archiving operation of a mandatory destination fails, online redo log files cannot be overwritten. - `OPTIONAL` 	You can specify a policy for reuse of online redo log files using the `OPTIONAL` value. If the archiving operation of an optional destination fails, the online redo log files are overwritten. |
| Broker default | `OPTIONAL` |
| Imported? | Yes, from the `BINDING` column of the `V$ARCHIVE_DEST` view of the primary database |
| Parameter class | Dynamic |
| Role | Standby <sup>Foot 1</sup> |
| Standby type | Physical, logical, or snapshot |
| Corresponds to | - `MANDATORY` and `OPTIONAL` attributes for the `LOG_ARCHIVE_DEST_` `n` initialization parameter of the primary database - `BINDING` column of the `V$ARCHIVE_DEST` view of the primary database |
| Scope | Database |
| Enterprise Manager name | Not applicable |

<sup>Footnote 1</sup> Although this property is set for the standby database, it is indirectly related to the redo transport services for the primary database. The broker propagates the setting you specify on the standby database to the corresponding attributes of the `LOG_ARCHIVE_DEST_` `n` value of the primary database.

### 8.3.7 DbFileNameConvert

The `DbFileNameConvert` configurable database property distinguishes physical standby datafile filenames from primary datafile filenames. If you add a datafile to the primary database, this property converts the datafile name on the primary database to the datafile on the physical standby database.

This property is used in the following situations:

- At physical standby mount time, it is used to rename primary datafile filenames to standby datafile filenames if the datafile file path on the physical standby system is different from the primary database system.
- When a new data file is created on the primary database, a corresponding new data file will be created on the physical standby database if the `StandbyFileManagement` configurable database property is set to `'AUTO'`. Oracle uses the data-file file-path mapping information from the `DbFileNameConvert` property to determine the standby file path of the new standby data file. If the `StandbyFileManagement` property is set to `'MANUAL'`, you must add a corresponding file to the physical standby database.

Note:

When a database is added to the configuration, the broker sets the initial value of this property to the in-memory value of the `DB_FILE_NAME_CONVERT` initialization parameter. It is possible that the in-memory value and server parameter file (SPFILE) value of this parameter will differ. If you want to use the parameter's in-memory value, then enable the database and the broker will ensure that the SPFILE value of the parameter is set to the in-memory value. If you want to use the SPFILE value, then set the property value to be the parameter's value stored in the SPFILE. Then enable the database.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | Set the value of this property to a list of string pairs: 1. The first string is the substring found in the datafile names on the primary database. 2. The second string is the substring found in the datafile names on the standby database.  For example, `('string1', 'string2', 'string3', 'string4',...)`  Where:  - `string1` is the substring of the primary database filename. - `string2` is the substring of the standby database filename. - `string3` is the substring of the primary database filename. - `string4` is the substring of the standby database filename. |
| Broker default | Empty string |
| Imported? | Yes, from the `DB_FILE_NAME_CONVERT` initialization parameter |
| Parameter class | Static |
| Role | Standby |
| Standby type | Physical |
| Corresponds to | `DB_FILE_NAME_CONVERT` initialization parameter |
| Scope | Database |
| Enterprise Manager name | `DB File Name Convert` |

### 8.3.8 DelayMins

The `DelayMins` configurable database property specifies the number of minutes log apply services will delay applying the archived redo log data on the standby database. When the `DelayMins` property is set to the default value of 0 minutes, log apply services apply redo data as soon as possible.

If the `DelayMins` property is set to 0, start log apply services as follows:

- Start Redo Apply on physical standby databases using the following SQL statement:
	```
	ALTER DATABASE RECOVER MANAGED STANDBY DATABASE USING CURRENT LOGFILE;
	```
- Start SQL Apply on logical standby databases using the following SQL statement:
	```
	ALTER DATABASE START LOGICAL STANDBY APPLY IMMEDIATE;
	```

| Category | Description |
| --- | --- |
| Datatype | Integer |
| Valid values | \>=0 (minutes) |
| Broker default | `0` |
| Imported? | Yes, from the `DELAY_MINS` column of the `V$ARCHIVE_DEST` view of the primary database |
| Parameter class | Dynamic |
| Role | Standby <sup>Foot 1</sup> |
| Standby type | Physical and logical |
| Corresponds to | - `DELAY` attribute for the `LOG_ARCHIVE_DEST_` `n` initialization parameter of the primary database - `DELAY_MINS` column of the `V$ARCHIVE_DEST` view of the primary database - Options used to start Redo Apply and SQL Apply |
| Scope | Database |
| Enterprise Manager name | `Apply Delay (mins)` |

<sup>Footnote 1</sup> Although this property is set for the standby database, it is indirectly related to the redo transport services for the primary database. The broker propagates the setting you specify on the standby database to the corresponding attributes of the `LOG_ARCHIVE_DEST_` `n` value of the primary database.

### 8.3.9 DGConnectIdentifier

The `DGConnectIdentifier` configurable database property specifies the connection identifier the broker uses when making connections to a database. If using DGMGRL, you supply the value when you enter the `CREATE CONFIGURATION` or `ADD DATABASE` command. If you are using Enterprise Manager, the value is supplied automatically. The connect identifier for a database must:

- Allow all other databases in the configuration to reach it.
- Allow the database to reach itself.
- Allow all instances of an Oracle RAC database to be reached.
- Specify a service that all instances dynamically register with the listeners so that connect-time failover on an Oracle RAC database is possible.
- Have failover attributes set to allow the primary database's Redo Transport Services to continue shipping redo data to an Oracle RAC standby database, even if the receiving instance of that standby database has failed.

The value of this property is specified in the `SERVICE` attribute of the `LOG_ARCHIVE_DEST_` n parameter when the broker configures redo transport services on the primary database.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | A connect identifier that can be used to connect to this database |
| Broker default | Not applicable |
| Imported? | No |
| Parameter class | Not applicable |
| Role | Primary and standby |
| Standby type | Physical, logical, or snapshot |
| Corresponds to | `SERVICE_NAME` attribute of the `LOG_ARCHIVE_DEST_` `n` initialization parameter of the primary database |
| Scope | Database |
| Enterprise Manager name | Not applicable |

Note:

Prior to Oracle Database release 11.1, the `DGConnectIdentifier` configurable database property was known as the `InitialConnectIdentifier` property. When upgrading a 10g configuration to this release, the `InitialConnectIdentifier` value will be retained as the new `DGConnectIdentifier` value for that database.

If this is an Oracle RAC database, then before the upgrade, you must ensure that the `InitialConnectIdentifier` meets the criteria just listed for `DGConnectIdentifier`.

See Also:

[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm)

### 8.3.10 FastStartFailoverTarget

The `FastStartFailoverTarget` configuration property specifies the `DB_UNIQUE_NAME` of the database that will be the target of a fast-start failover when this database is the primary database. See Step [2](sofo.md) in [Section 5.5.2](sofo.md) for more information about setting this property.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid value | `DB_UNIQUE_NAME` of the database that is the target of the fast-start failover. |
| Broker default | If only one physical or logical standby database exists, then the broker selects that as the default value for this property on the primary database when fast-start failover is enabled.  If more than one physical or logical standby database exists, you must specify the `FastStartFailoverTarget` value explicitly, prior to enabling fast-start failover. The indicated target is verified when fast-start failover is enabled.  For the target standby database, the broker automatically selects the current primary database as the value for this property when fast-start failover is enabled. |
| Imported? | No |
| Parameter class | Not applicable |
| Role | Primary or standby |
| Standby type | Physical or logical |
| Corresponds to | Not applicable |
| Scope | Database |
| Enterprise Manager name | Enterprise Manager displays the value for the current primary database on the Data Guard Overview page, along with whether or not fast-start failover has been enabled. |

### 8.3.11 LogArchiveFormat

The `LogArchiveFormat` configurable instance-specific property specifies the format for filenames of archived redo log files using a database ID (`%d`), thread (`%t`), sequence number (`%s`), and resetlogs ID (`%r`).

Note:

When a database is added to the configuration, the broker sets the initial value of this property to the in-memory value of the `LOG_ARCHIVE_FORMAT` initialization parameter. It is possible that the in-memory value and server parameter file (SPFILE) value of this parameter will differ. If you want to use the parameter's in-memory value, then enable the database and the broker will ensure that the SPFILE value of the parameter is set to the in-memory value. If you want to use the SPFILE value, then set the property value to be the parameter's value stored in the SPFILE. Then enable the database.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | `%d_%t_%s_%r` |
| Broker default | Empty string |
| Imported? | Yes, from the `LOG_ARCHIVE_FORMAT` initialization parameter on the primary database |
| Parameter class | Static |
| Role | Primary and standby |
| Standby type | Physical, logical, or snapshot |
| Corresponds to | `LOG_ARCHIVE_FORMAT` initialization parameter |
| Scope | Instance (On an Oracle RAC database, you can use the `EDIT INSTANCE * ON DATABASE` command to have all instances use the same value for this property.) |
| Enterprise Manager name | Not applicable |

### 8.3.12 LogArchiveMaxProcesses

The `LogArchiveMaxProcesses` configurable database property specifies the initial number of archiver processes (ARCn) the Oracle database invokes. The actual number of archiver processes in use may increase subsequently based on the archiving workload.

| Category | Description |
| --- | --- |
| Datatype | Integer |
| Valid values | 1 to 30 |
| Broker default | `4` |
| Imported? | Yes, from the `LOG_ARCHIVE_MAX_PROCESSES` initialization parameter |
| Parameter class | Dynamic |
| Role | Primary and standby |
| Standby type | Physical, logical, or snapshot |
| Corresponds to | `LOG_ARCHIVE_MAX_PROCESSES` initialization parameter |
| Scope | Database |
| Enterprise Manager name | `Archiver Processes` |

### 8.3.13 LogArchiveMinSucceedDest

The `LogArchiveMinSucceedDest` configurable database property controls when online redo log files are available for reuse. For the online redo log files to be available for reuse, archiving must succeed to a minimum number of destinations.

| Category | Description |
| --- | --- |
| Datatype | Integer |
| Valid values | 1 to 10 |
| Broker default | 1 |
| Imported? | Yes, from the `LOG_ARCHIVE_MIN_SUCCEED_DEST` initialization parameter |
| Parameter class | Dynamic |
| Role | Primary |
| Standby type | Not applicable |
| Corresponds to | `LOG_ARCHIVE_MIN_SUCCEED_DEST` initialization parameter |
| Scope | Database |
| Enterprise Manager name | Not applicable |

### 8.3.14 LogArchiveTrace

Set the `LogArchiveTrace` configurable instance-specific property to an integer value to see the progression of the archiving of online redo log files on the primary and the standby databases. The Oracle database writes an audit trail of the archived redo log files received from the primary database into process trace files.

| Category | Description |
| --- | --- |
| Datatype | Integer |
| Valid values | A valid value is the sum of any combination of any of the following values:  0: Disable archive redo log tracing  1: Track archiving of online redo log file  2: Track archiving status of each archive redo log destination  4: Track archiving operational phase  8: Track `ARCHIVELOG` destination activity  16: Track detailed `ARCHIVELOG` destination activity  32: Track `ARCHIVELOG` destination parameter modifications  64: Track ARC `n` process state activity  128: Track FAL (fetch archive log) server related activities  256: Tracks RFS Logical Client  512: Tracks LGWR redo shipping network activity  1024: Tracks RFS physical client  2048: Tracks RFS/ARCn ping heartbeat  4096: Tracks real-time apply activity  8192: Tracks Redo Apply (media recovery or physical standby) |
| Broker default | 255 |
| Imported? | Yes, from the `LOG_ARCHIVE_TRACE` initialization parameter |
| Parameter class | Dynamic |
| Role | Primary and standby |
| Standby type | Physical, logical, or snapshot |
| Corresponds to | `LOG_ARCHIVE_TRACE` initialization parameter |
| Scope | Instance (On an Oracle RAC database, you can use the `EDIT INSTANCE * ON DATABASE` command to have all instances use the same value for this property.) |
| Enterprise Manager name | `Log Archive Trace` |

### 8.3.15 LogFileNameConvert

The `LogFileNameConvert` configurable database property converts the filename of an online redo log file on the primary database to the filename of a corresponding online redo log file on the physical standby database.

Note:

When a database is added to the configuration, the broker sets the initial value of this property to the in-memory value of the `LOG_FILE_NAME_CONVERT` initialization parameter. It is possible that the in-memory value and server parameter file (SPFILE) value of this parameter will differ. If you want to use the parameter's in-memory value, then enable the database and the broker will ensure that the SPFILE value of the parameter is set to the in-memory value. If you want to use the SPFILE value, then set the property value to be the parameter's value stored in the SPFILE. Then enable the database.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | Set the value of this property to a list of an even number of string pairs, separated by commas. 1. The first string is the substring found in the datafile names on the primary database. 2. The second string is the substring found in the datafile names on the standby database.  For example, `('string1', 'string2', 'string3', 'string4',...)`  Where:  - `string1` is the substring of the primary database filename. - `string2` is the substring of the standby database filename. - `string3` is the substring of the primary database filename. - `string4` is the substring of the standby database filename. |
| Broker default | Empty string |
| Imported? | Yes, from the `LOG_FILE_NAME_CONVERT` initialization parameter |
| Parameter class | Static |
| Role | Standby |
| Standby type | Physical |
| Corresponds to | `LOG_FILE_NAME_CONVERT` initialization parameter |
| Scope | Database |
| Enterprise Manager name | `Log File Name Convert` |

### 8.3.16 LogShipping

The `LogShipping` configurable database property specifies whether or not redo transport services can send redo data to the particular standby database. The broker uses the value of the `LogShipping` property only when the primary database is in the `TRANSPORT-ON` state:

- If the primary database is in the `TRANSPORT-OFF` state, then redo transport services to all standby databases are disabled, regardless of whether or not the `LogShipping` property is set to `ON` or `OFF`.
- If the primary database is in the `TRANSPORT-ON` state and the value of the `LogShipping` property is `ON`, then redo transport services are enabled to send redo data to the particular standby database. If the `LogShipping` property is `OFF`, then redo transport services are disabled to send redo data to the particular standby database.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | `ON` or `OFF` |
| Broker default | `ON` |
| Imported? | No |
| Parameter class | Dynamic |
| Role | Standby <sup>Foot 1</sup> |
| Standby type | Physical, logical, or snapshot |
| Corresponds to | `ENABLE` and `DEFER` values for the `LOG_ARCHIVE_DEST_STATE_` n initialization parameter of the primary database |
| Scope | Database |
| Enterprise Manager name | `Log Shipping` |

<sup>Footnote 1</sup> Although this property is set for the standby database, it is indirectly related to the redo transport services for the primary database. The broker propagates the setting you specify on the standby database to the corresponding attributes of the `LOG_ARCHIVE_DEST_` n value of the primary database.

### 8.3.17 LogXptMode

The `LogXptMode` configurable database property enables you to set the redo transport service. You set the redo transport services on each standby database to one of the following modes:

- `SYNC`
	Configures redo transport services for this standby database using the `SYNC` and `AFFIRM` attributes of the `LOG_ARCHIVE_DEST_` `n` initialization parameter. Standby redo log files are required. This mode is required for the maximum protection or maximum availability data protection modes. This redo transport service enables the highest grade of data protection to the primary database, but also incurs the highest performance impact.
- `ASYNC`
	Configures redo transport services for this standby database using the `ASYNC` and `NOAFFIRM` attributes of the `LOG_ARCHIVE_DEST_` `n` initialization parameter. Standby redo log files are required. This mode enables a moderate grade of data protection to the primary database, and incurs a lower performance impact than `SYNC`.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | `SYNC` or `ASYNC` |
| Broker default | `ASYNC` |
| Imported? | Yes, from the `ARCHIVER`, `TRANSMIT_MODE`, and `AFFIRM` columns of `V$ARCHIVE_DEST` view of the primary database |
| Parameter class | Dynamic |
| Role | Standby <sup>Foot 1</sup> |
| Standby type | Physical, logical, or snapshot |
| Corresponds to | - `SYNC`, `ASYNC`, `AFFIRM`, and `NOAFFIRM` attributes for the `LOG_ARCHIVE_DEST_` `n` initialization parameter of the primary database - `ARCHIVER`, `TRANSMIT_MODE`, and `AFFIRM` columns of `V$ARCHIVE_DEST` view of the primary database |
| Scope | Database |
| Enterprise Manager name | `Redo Transport Service` |

<sup>Footnote 1</sup> Although this property is set for the standby database, it is indirectly related to the redo transport services for the primary database. The broker propagates the setting you specify on the standby database to the corresponding attributes of the `LOG_ARCHIVE_DEST_` `n` value of the primary database.

See Also:

[Chapter 4](dbresource.md) for more information about setting data protection modes for redo transport services

### 8.3.18 LsbyASkipCfgPr

The `LsbyASkipCfgPr` configurable database property provides a way to add a skip specification to SQL Apply to control the apply service to skip (ignore) SQL statements that you do not want to apply to the logical standby database. The `SKIP` operation:

- Sets the criteria for identifying the SQL statements that will not be applied to the standby database
- Specifies any additional processing that will be done, if necessary

Specifying a value for this property has no effect and will be ignored if management of the standby database is disabled.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | A valid set of arguments to the `DBMS_LOGSTDBY.SKIP` procedure |
| Broker default | Empty string |
| Imported? | No |
| Parameter class | Dynamic; SQL Apply does not require restart |
| Role | Standby |
| Standby type | Logical |
| Corresponds to | `DBMS_LOGSTDBY.SKIP` procedure |
| Scope | Database |
| Enterprise Manager name | `Add Skip Table Entries` |

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm)

### 8.3.19 LsbyASkipErrorCfgPr

The `LsbyASkipErrorCfgPr` configurable database property adds a skip error specification to SQL Apply. It provides criteria to determine if an error should cause SQL Apply to stop. All errors to be skipped are stored in system tables that describe how exceptions should be handled.

Specifying a value for this property has no effect and will be ignored if management of the standby database is disabled.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | A valid set of arguments to the `DBMS_LOGSTDBY.SKIP_ERROR` procedure. The string must contain comma separators between the arguments. |
| Broker default | Empty string |
| Imported? | No |
| Parameter class | Dynamic; SQL Apply does not require restart |
| Role | Standby |
| Standby type | Logical |
| Corresponds to | `DBMS_LOGSTDBY.SKIP_ERROR` procedure |
| Scope | Database |
| Enterprise Manager name | `Add Skip Table Entries` |

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm)

### 8.3.20 LsbyASkipTxnCfgPr

The `LsbyASkipTxnCfgPr` configurable database property skips over a transaction that caused SQL Apply to stop applying transactions to the logical standby database. This property enables you to specify the transaction ID (`XIDSQN NUMBER`) of the problematic transaction that you want SQL Apply to ignore. Before you restart SQL Apply, you should issue a SQL transaction that will correctly update the logical standby database in place of the skipped transaction. Applying a compensating transaction will help keep the logical standby database transactionally consistent with the primary database.

Specifying a value for this property has no effect and will be ignored if management of the standby database is disabled.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | A valid set of arguments to the `DBMS_LOGSTDBY.SKIP_TRANSACTION` procedure. Use comma separators between the arguments. |
| Broker default | Empty string |
| Imported? | No |
| Parameter class | Dynamic; SQL Apply does not require restart |
| Role | Standby |
| Standby type | Logical |
| Corresponds to | `DBMS_LOGSTDBY.SKIP_TRANSACTION` procedure |
| Scope | Database |
| Enterprise Manager name | `Skip Edit Properties` |

Note:

Enterprise Manager indirectly supports skipping a transaction using the Skip Edit Properties page.

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm)

### 8.3.21 LsbyDSkipCfgPr

The `LsbyDSkipCfgPr` configurable database property deletes an existing skip specification from SQL Apply. It reverses or removes the actions of the LsbyASkipCfgPr property by finding the record, matching all the parameters, and removing the record from the system table. The match must be exact, and multiple skip actions can be removed only by a matching number of unskip actions. You cannot remove multiple skip actions by using wildcard characters as a value to this property.

Specifying a value for this property has no effect and will be ignored if management of the standby database is disabled.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid Values | A valid set of arguments to the `DBMS_LOGSTDBY.UNSKIP` procedure |
| Broker Default | Empty string |
| Imported? | No |
| Parameter Class | Dynamic; SQL Apply does not require restart |
| Role | Standby |
| Standby type | Logical |
| Corresponds to | `DBMS_LOGSTDBY.UNSKIP` procedure |
| Scope | Database |
| Enterprise Manager name | `Remove Skip Table Entries` |

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm)

### 8.3.22 LsbyDSkipErrorCfgPr

The `LsbyDSkipErrorCfgPr` configurable database property deletes an existing skip error specification from SQL Apply. It reverses or removes the actions of the LsbyASkipErrorCfgPr property by finding the record, matching all of the parameters and removing the record from the system table. The match must be exact, and multiple skip actions can be removed only by a matching number of unskip actions. You cannot remove multiple skip actions by using wildcard characters as a value to this property.

Specifying a value for this property has no effect and will be ignored if management of the standby database is disabled.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | A valid set of arguments to the `DBMS_LOGSTDBY.UNSKIP_ERROR` procedure. The string must contain comma separators between the arguments. |
| Broker default | Empty string |
| Imported? | No |
| Parameter class | Dynamic; SQL Apply does not require restart |
| Role | Standby |
| Standby type | Logical |
| Corresponds to | `DBMS_LOGSTDBY.UNSKIP_ERROR` procedure |
| Scope | Database |
| Enterprise Manager name | `Remove Skip Table Entries` |

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm)

### 8.3.23 LsbyDSkipTxnCfgPr

The `LsbyDSkipTxnCfgPr` configurable database property reverses or removes the actions of the LsbyASkipTxnCfgPr property. The transaction IDs must match exactly, and multiple skip transaction actions can be removed only by a matching number of unskip transaction actions. You cannot remove multiple skip transaction actions by using wildcard characters as a value to this property.

Specifying a value for this property has no effect and will be ignored if management of the standby database is disabled.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | A valid set of arguments to the `DBMS_LOGSTDBY.UNSKIP_TRANSACTION` procedure |
| Broker default | Empty string |
| Imported? | No |
| Parameter class | Dynamic; SQL Apply does not require restart |
| Role | Standby |
| Standby type | Logical |
| Corresponds to | `DBMS_LOGSTDBY.UNSKIP_TRANSACTION` procedure |
| Scope | Database |
| Enterprise Manager name | Not applicable |

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm)

### 8.3.24 LsbyMaxEventsRecorded

The `LsbyMaxEventsRecorded` configurable database property specifies the number of events that will be stored in the `DBA_LOGSTDBY_EVENTS` table, which stores logical standby event information.

| Category | Description |
| --- | --- |
| Datatype | Integer |
| Valid values | \>=0 |
| Broker default | 0 |
| Imported? | Yes, from the `MAX_EVENTS_RECORDED` row of `SYSTEM.LOGSTDBY$PARAMETERS` |
| Parameter class | Dynamic; SQL Apply does not require restart |
| Role | Standby |
| Standby type | Logical |
| Corresponds to | `DBMS_LOGSTDBY.APPLY_SET('MAX_EVENTS_RECORDED')` and the `DBMS_LOGSTDBY.APPLY_UNSET('MAX_EVENTS_RECORDED')` procedures |
| Scope | Database |
| Enterprise Manager name | `Max Events Recorded` |

### 8.3.25 LsbyMaxSga

The `LsbyMaxSga` configurable instance-specific property specifies the number of megabytes for the allocation of SQL Apply cache in the system global area (SGA). If the value is 0, SQL Apply uses one quarter of the value set for the `SHARED_POOL_SIZE` initialization parameter.

| Category | Description |
| --- | --- |
| Datatype | Integer |
| Valid values | \>=0 |
| Broker default | 0 |
| Imported? | Yes, from the `MAX_SGA` row of `SYSTEM.LOGSTDBY$PARAMETERS` |
| Parameter class | Dynamic; SQL Apply does not require restart |
| Role | Standby |
| Standby type | Logical |
| Corresponds to | `DBMS_LOGSTDBY.APPLY_SET('MAX_SGA')` and the `DBMS_LOGSTDBY.APPLY_UNSET('MAX_SGA')` procedures |
| Scope | Instance (On an Oracle RAC database, you can use the `EDIT INSTANCE * ON DATABASE` command to have all instances use the same value for this property.) |
| Enterprise Manager name | `Max SGA (MB)` |

### 8.3.26 LsbyMaxServers

The `LsbyMaxServers` configurable instance-specific property specifies the number of parallel query servers specifically reserved for SQL Apply. If the value is 0, SQL Apply uses all available parallel query servers to read the log files and apply changes.

| Category | Description |
| --- | --- |
| Datatype | Integer |
| Valid values | \>=0 |
| Broker default | 0 |
| Imported? | Yes, from the `MAX_SERVERS` row of `SYSTEM.LOGSTDBY$PARAMETERS` |
| Parameter class | Dynamic; SQL Apply does not require restart |
| Role | Standby |
| Standby type | Logical |
| Corresponds to | `DBMS_LOGSTDBY.APPLY_SET('MAX_SERVERS')` and the `DBMS_LOGSTDBY.APPLY_UNSET('MAX_SERVERS')` procedures |
| Scope | Instance (On an Oracle RAC database, you can use the `EDIT INSTANCE * ON DATABASE` command to have all instances use the same value for this property.) |
| Enterprise Manager name | `Max Servers` |

### 8.3.27 LsbyPreserveCommitOrder

The `LsbyPreserveCommitOrder` configurable database property controls whether transactions are committed on the logical standby database in the exact same order in which they were committed on the primary database. Specify one of the following values:

- `TRUE`: Transactions are applied to the logical standby database in the exact order in which they were committed on the primary database.
- `FALSE`: Transactions containing non-overlapping sets of rows may be committed in a different order than they were committed on the primary database.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | `TRUE` or `FALSE` |
| Broker default | `TRUE` |
| Imported? | Yes, from the `PRESERVE_COMMIT_ORDER` row of `SYSTEM.LOGSTDBY$PARAMETERS` |
| Parameter class | Static; SQL Apply requires restart |
| Role | Standby |
| Standby type | Logical |
| Corresponds to | `DBMS_LOGSTDBY.APPLY_SET('PRESERVE_COMMIT_ORDER')` and `DBMS_LOGSTDBY.APPLY_UNSET('PRESERVE_COMMIT_ORDER')` procedures |
| Scope | Database |
| Enterprise Manager name | `Preserve Commit Order` |

### 8.3.28 LsbyRecordAppliedDdl

The `LsbyRecordAppliedDdl` configurable database property controls whether or not SQL statements that were applied to the logical standby database are recorded in the `DBA_LOGSTDBY_EVENTS` table. Specify one of the following values:

- `TRUE`: DDL statements applied to the logical standby database are recorded in the `DBA_LOGSTDBY_EVENTS` table. This is the default setting.
- `FALSE`: Applied DDL statements are not recorded.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | `TRUE` or `FALSE` |
| Broker default | `TRUE` |
| Imported? | Yes, from the `RECORD_APPLIED_DDL` row of `SYSTEM.LOGSTDBY$PARAMETERS` |
| Parameter class | Dynamic; SQL Apply does not require restart |
| Role | Standby |
| Standby type | Logical |
| Corresponds to | `DBMS_LOGSTDBY.APPLY_SET('RECORD_APPLIED_DDL')` and the `DBMS_LOGSTDBY.APPLY_UNSET('RECORD_APPLIED_DDL')` procedures |
| Scope | Database |
| Enterprise Manager name | `Record Applied DDL` |

### 8.3.29 LsbyRecordSkipDdl

The `LsbyRecordSkipDdl` configurable database property controls whether or not skipped DDL statements are recorded in the `DBA_LOGSTDBY_EVENTS` table. Specify one of the following values:

- `TRUE`: Skipped DDL statements are recorded in the `DBA_LOGSTDBY_EVENTS` table. This is the default setting.
- `FALSE`: Skipped DDL statements are not recorded in the `DBA_LOGSTDBY_EVENTS` table.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | `TRUE` or `FALSE` |
| Broker default | `TRUE` |
| Imported? | Yes, from the `RECORD_SKIP_DDL` row of `SYSTEM.LOGSTDBY$PARAMETERS` |
| Parameter class | Dynamic; SQL Apply does not require restart |
| Role | Standby |
| Standby type | Logical |
| Corresponds to | `DBMS_LOGSTDBY.APPLY_SET('RECORD_SKIP_DDL')` and the `DBMS_LOGSTDBY.APPLY_UNSET('RECORD_SKIP_DDL')` procedures |
| Scope | Database |
| Enterprise Manager name | `Record Skip DDL` |

### 8.3.30 LsbyRecordSkipErrors

The `LsbyRecordSkipErrors` configurable database property controls whether or not skipped errors (as described by the `DBMS_LOGSTDBY.SKIP_ERROR` procedure) are recorded in the `DBA_LOGSTDBY_EVENTS` table. Specify one of the following values:

- `TRUE`: Skipped errors are recorded in the `DBA_LOGSTDBY_EVENTS` table.
- `FALSE`: Skipped errors are not recorded in the `DBA_LOGSTDBY_EVENTS` table.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | `TRUE` or `FALSE` |
| Broker default | `TRUE` |
| Imported? | Yes, from the `RECORD_SKIP_ERRORS` row of `SYSTEM.LOGSTDBY$PARAMETERS` |
| Parameter class | Dynamic; SQL Apply does not require restart |
| Role | Standby |
| Standby type | Logical |
| Corresponds to | `DBMS_LOGSTDBY.APPLY_SET('RECORD_SKIP_ERRORS')` and the `DBMS_LOGSTDBY.APPLY_UNSET('RECORD_SKIP_ERRORS')` procedures |
| Scope | Database |
| Enterprise Manager name | `Record Skip Errors` |

### 8.3.31 MaxConnections

The `MaxConnections` configurable database property specifies how many ARCn processes will be used in parallel to transmit redo data from a single archived redo log on the primary database to the archived redo log at the remote site. If the `MaxConnections` property is set to a value greater than 1, redo transport services use multiple ARCn processes to transmit redo data to archived redo log files at the remote destinations.

| Category | Description |
| --- | --- |
| Datatype | Integer |
| Valid values | 1 to 20 |
| Broker default | 1 |
| Imported? | Yes, from the `MAX_CONNECTIONS` column of the `V$ARCHIVE_DEST` view for the primary database. |
| Parameter class | Dynamic |
| Role | Standby |
| Standby type | Physical, logical, or snapshot |
| Corresponds to | - `LOG_ARCHIVE_MAX_PROCESSES` initialization parameter <sup>Foot 1</sup> - `MAX_CONNECTIONS` attribute for the `LOG_ARCHIVE_DEST_` `n` initialization parameter of the primary database - `MAX_CONNECTIONS` column of the `V$ARCHIVE_DEST` view of the primary database |
| Scope | Database |
| Enterprise Manager name | Not applicable |

<sup>Footnote 1</sup> The `LOG_ARCHIVE_MAX_PROCESSES` initialization parameter affects the actual number of ARCn processes used by an instance.

### 8.3.32 MaxFailure

The `MaxFailure` configurable database property specifies the maximum number of contiguous archiving failures before the redo transport services stop trying to transport archived redo log files to the standby database. A value of zero indicates that an unlimited number of failures are allowed.

| Category | Description |
| --- | --- |
| Datatype | Integer |
| Valid values | \>=0 |
| Broker default | `0` |
| Imported? | Yes, from the `MAX_FAILURE` column of `V$ARCHIVE_DEST` view of the primary database |
| Parameter class | Dynamic |
| Role | Standby <sup>Foot 1</sup> |
| Standby type | Physical, logical, or snapshot |
| Corresponds to | - `MAX_FAILURE` attribute for the `LOG_ARCHIVE_DEST_` n initialization parameter of the primary database - `MAX_FAILURE` column of the `V$ARCHIVE_DEST` view of the primary database |
| Scope | Database |
| Enterprise Manager name | Not applicable |

<sup>Footnote 1</sup> Although this property is set for the standby database, it is indirectly related to the redo transport services for the primary database. The broker propagates the setting you specify on the standby database to the corresponding attributes of the `LOG_ARCHIVE_DEST_` n value of the primary database.

### 8.3.33 NetTimeout

The `NetTimeout` configurable database property specifies the number of seconds the LGWR waits for Oracle Net Services to respond to a LGWR request. It is used to bypass the long connection timeout in TCP.

| Category | Description |
| --- | --- |
| Datatype | Integer |
| Valid values | 0, 15 to 1200 |
| Broker default | 30 |
| Imported? | Yes, from the `NET_TIMEOUT` column of `V$ARCHIVE_DEST` view of the primary database |
| Parameter class | Dynamic |
| Role | Primary and Standby |
| Standby type | Physical, logical, or snapshot |
| Corresponds to | - `NET_TIMEOUT` attribute of the `LOG_ARCHIVE_DEST_` `n` initialization parameter of the primary database - `NET_TIMEOUT` column of `V$ARCHIVE_DEST` view of the primary database |
| Scope | Database |
| Enterprise Manager name | Not applicable |

### 8.3.34 ObserverConnectIdentifier

The `ObserverConnectIdentifier` configurable database property specifies a connect identifier that can be used by the observer to connect to this database. This can pertain only to the primary database, or to the target standby database when fast-start failover is enabled.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid Values | A connect identifier that observer can use to connect to this database |
| Broker Default | Empty String <sup>Foot 1</sup> |
| Imported? | No |
| Parameter Class | Not applicable |
| Role | Primary and Standby |
| Standby Type | Physical or logical |
| Corresponds to | Not applicable |
| Scope | Database |
| Enterprise Manager name | `Observer Connect Identifier` |

<sup>Footnote 1</sup> When this is Empty String (not set by the user), the connect identifier specified by this database's DGConnectIdentifier property will be used by the observer.

### 8.3.35 PreferredApplyInstance

The `PreferredApplyInstance` configurable database property indicates that a particular instance is the preferred choice for serving log apply services. It is only used when the database is a standby Oracle RAC database. The value could be an empty string (default) which means the broker chooses the apply instance.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid Values | The instance name (SID) or empty string. Note that on certain platforms, SIDs may be case-sensitive. |
| Broker Default | Empty string |
| Imported? | No |
| Parameter Class | Not applicable |
| Role | Standby |
| Standby Type | Physical or logical |
| Corresponds to | Not applicable |
| Scope | Database |
| Enterprise Manager name | `Apply Instance` |

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/create.htm#ADMIN11074) for more information about SIDs
- [Section 4.5.7](dbresource.md) for information about apply services in an Oracle RAD environment

### 8.3.36 RedoCompression

The `RedoCompression` configurable database property is used to specify whether redo data is transmitted to a standby database in compressed or uncompressed form.

Note:

Redo transport compression is a feature of the Oracle Advanced Compression option. You must purchase a license for this option before using the redo transport compression feature.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid value | `DISABLE` or `ENABLE` |
| Broker Default | `DISABLE` |
| Imported? | Yes, from the `COMPRESSION` column of the `V$ARCHIVE_DEST` view of the primary database |
| Parameter class | Dynamic |
| Role | Standby <sup>Foot 1</sup> |
| Standby type | Physical, logical, or snapshot |
| Corresponds to | - `COMPRESSION` attribute for the `LOG_ARCHIVE_DEST_` n initialization parameter of the primary database - `COMPRESSION` column of the `V$ARCHIVE_DEST` view of the primary database |
| Scope | Database |
| Enterprise Manager name | Not applicable |

<sup>Footnote 1</sup> Although this property is set for the standby database, it is indirectly related to the redo transport services for the primary database. The broker propagates the setting you specify on the standby database to the corresponding attributes of the `LOG_ARCHIVE_DEST_` `n` value of the primary database.

### 8.3.37 ReopenSecs

The `ReopenSecs` configurable database property specifies the minimum number of seconds before the archiver process (ARCn, foreground, or log writer process) should try again to access a previously failed destination.

| Category | Description |
| --- | --- |
| Datatype | Integer |
| Valid values | \>=0 seconds |
| Broker default | `300` |
| Imported? | Yes, from the `REOPEN_SECS` column of `V$ARCHIVE_DEST` view of the primary database |
| Parameter class | Dynamic |
| Role | Standby <sup>Foot 1</sup> |
| Standby type | Physical, logical, or snapshot |
| Corresponds to | - `REOPEN` attribute for the `LOG_ARCHIVE_DEST_` n initialization parameter of the primary database - `REOPEN_SECS` column of the `V$ARCHIVE_DEST` view of the primary database |
| Scope | Database |
| Enterprise Manager name | Not applicable |

<sup>Footnote 1</sup> Although this property is set for the standby database, it is indirectly related to the redo transport services for the primary database. The broker propagates the setting you specify on the standby database to the corresponding attributes of the `LOG_ARCHIVE_DEST_` `n` value of the primary database.

### 8.3.38 SidName

The `SidName` configurable database property specifies the Oracle System Identifier (SID) of the instance. The property can only be updated when broker management of the database is disabled. You should only update the value when the SID is changed, in which case you need to disable broker management of the database, update the `SidName` property to match with the new SID, and reenable broker management of the database.

Note:

If no existing instance object in the broker configuration, for the database object whose name matches this instance's `db_unique_name`, has a `SidName` property with a value that matches this instance's actual `SID`, then the broker will create a new instance object for this database that has this instance's `db_unique_name`. See [Section 1.3, "Data Guard Broker Management Model"](concepts.md) for more information.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | SID of the instance. Note that on certain platforms, SIDs may be case-sensitive. |
| Broker default | Not applicable |
| Imported? | Yes |
| Parameter class | Not applicable |
| Role | Primary and standby |
| Standby type | Physical, logical, or snapshot |
| Corresponds to | `INSTANCE_NAME` column of the `V$INSTANCE` view |
| Scope | Instance |
| Enterprise Manager name | Not applicable |

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/create.htm#ADMIN11074) for more information about SIDs

### 8.3.39 StandbyArchiveLocation

The `StandbyArchiveLocation` configurable database property specifies the location of archived redo log files arriving from a primary database. Oracle recommends that you always explicitly set the value.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | Nonempty file specification of the location of archived redo log files on the standby database. Use `DB_RECOVERY_FILE_DEST` if a database recovery area is desired. |
| Broker default | `dgsby_` db\_unique\_name |
| Imported? | Yes, from the `DESTINATION` column of the `V$ARCHIVE_DEST` fixed view of the standby database where the destination is a local destination and where the `VALID_FOR` attribute is compatible with the string `(STANDBY_ROLE, STANDBY_LOGFILE)`; if no such destination exists, import is from the `STANDBY_ARCHIVE_DEST` initialization parameter. Note that the `STANDBY_ARCHIVE_DEST` parameter has been deprecated and is supported for backward compatibility only. |
| Parameter class | Dynamic |
| Role | Standby |
| Standby type | Physical, logical, or snapshot |
| Corresponds to | - `LOCATION` attribute of the `LOG_ARCHIVE_DEST_` n initialization parameter of the standby database with `VALID_FOR` compatible with `(STANDBY_ROLE, STANDBY_LOGFILE)` - `DESTINATION` column of the `V$ARCHIVE_DEST` view of the standby database |
| Scope | Instance |
| Enterprise Manager name | `Standby Archive Location` |

Note:

On a logical standby database, Oracle recommends the `LOCATION` attribute of the `LOG_ARCHIVE_DEST_` n initialization parameter for the local destination be different from the value of `StandbyArchiveLocation` property, unless you are using a database recovery area.

### 8.3.40 StandbyFileManagement

The `StandbyFileManagement` configurable database property affects how the add datafile operation on the primary database is applied on the standby database. If this property is set to `AUTO`, in conjunction with valid settings in the `DbFileNameConvert` configurable database property, a corresponding new datafile is automatically created on the standby database. The location of this new standby datafile is determined by the value of the `DbFileNameConvert` property.

If this property is set to `MANUAL`, you have to create the correct new datafile on the standby database manually.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | `AUTO` or `MANUAL` |
| Broker default | `AUTO` |
| Imported? | Yes, from the `STANDBY_FILE_MANAGEMENT` initialization parameter |
| Parameter class | Dynamic |
| Role | Standby |
| Standby type | Physical, logical, or snapshot |
| Corresponds to | `STANDBY_FILE_MANAGEMENT` initialization parameter |
| Scope | Database |
| Enterprise Manager name | Not applicable |

### 8.3.41 StaticConnectIdentifier

The `StaticConnectIdentifier` configurable instance-specific property specifies the connection identifier that the DGMGRL client will use when starting database instances.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | A connect identifier that refers to a service that is statically registered. |
| Broker default | Connect descriptor that is the concatenation of:<sup>Foot 1</sup> - The `ADDRESS` attribute value of the listener that is specified for the `LOCAL_LISTENER` initialization parameter - The value for the `SERVICE_NAME` attribute will be set to a concatenation of `db_unique_name_DGMGRL.db_domain` |
| Imported? | Yes, from the `LOCAL_LISTENER` and `DB_UNIQUE_NAME` initialization parameters. |
| Parameter class | Not applicable |
| Role | Primary and standby |
| Standby type | Physical, logical, or snapshot |
| Corresponds to | Not applicable |
| Scope | Instance |
| Enterprise Manager name | Not applicable |

<sup>Footnote 1</sup> If the instance specified by the `SidName` property is started on a different host (read from the `HOST_NAME` column of the `V$INSTANCE` view) than the host on which it had been previously started, the broker automatically updates the default value of the `StaticConnectIdentifier` property to incorporate the current `ADDRESS` attribute of the listener that is specified for the `LOCAL_LISTENER` initialization parameter.

See Also:

[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm) for more information about statically registered services

### 8.3.42 TransportDisconnectedThreshold

The `TransportDisconnectedThreshold` configurable database property can be used to generate a warning status for a logical, physical, or snapshot standby when the last communication from the primary database exceeds the value specified by the property. The property value is expressed in seconds. A value of 0 seconds results in no warnings being generated.

The `TransportDisconnectedThreshold` configuration property is available only in Oracle Database 11g Release 2 (11.2.0.4) and higher.

| Category | Description |
| --- | --- |
| Datatype | Number |
| Valid values | \>=0 |
| Broker default | 30 seconds |
| Imported? | No |
| Parameter class | Not applicable |
| Role | Standby database |
| Standby type | Physical, logical, or snapshot standby |
| Corresponds to | Not applicable |
| Scope | Database |
| Enterprise Manager name | Not applicable |

### 8.3.43 TransportLagThreshold

The `TransportLagThreshold` configurable database property can be used to generate a warning status for a logical, physical, or snapshot standby when the database's transport lag exceeds the value specified by the property. The property value is expressed in seconds. A value of 0 seconds results in no warnings being generated when a transport lag exists.

The `TransportLagThreshold` configuration property is available only in Oracle Database 11g Release 2 (11.2.0.4) and higher.

| Category | Description |
| --- | --- |
| Datatype | Number |
| Valid values | \>=0 |
| Broker default | 0 seconds |
| Imported? | No |
| Parameter class | Not applicable |
| Role | Standby database |
| Standby type | Physical, logical, or snapshot standby |
| Corresponds to | Not applicable |
| Scope | Database |
| Enterprise Manager name | Not applicable |