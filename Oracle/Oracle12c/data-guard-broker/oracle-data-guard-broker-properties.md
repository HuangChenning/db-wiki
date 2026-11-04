---
title: Broker
book: Data Guard Broker
doc_id: E85768-01
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/dgbkr/oracle-data-guard-broker-properties.html
tags:
  - oracle
  - 12c
  - data-guard-broker
---

Use Oracle Data Guard broker properties to manage instances or the entire configuration.

Broker configuration and database properties help you to view and control the behavior of entire broker configurations, individual configuration members, redo transport services, and log apply services.

Properties have either configuration-wide scope, database-wide scope, far sync instance-wide scope, or instance-specific scope. Configuration-wide properties control the behavior of the broker on all members of the configuration. The values of such properties apply uniformly across all members of the configuration.

Database-wide properties allow you to view or control the behavior of a specific database. If the database (primary or standby) is an Oracle RAC database consisting of multiple instances, then the value of such a property applies uniformly across all instances of that database.

Far sync instance-wide properties allow you to view or control the behavior of a far sync instance.

Instance-specific properties allow you to view or control the behavior of an individual database instance. Such a property exists for all instances of an Oracle RAC database, but its value can differ from one specific instance to another.

Note:

You can use the Oracle Data Guard broker command-line interface (DGMGRL) to view or modify broker properties.

Oracle Enterprise Manager Cloud Control (Cloud Control) explicitly presents some broker properties on the Edit Properties page. Information from other properties can be implicitly incorporated into other Web pages displayed by Cloud Control. See the individual description of each property for information about how Cloud Control presents that property.

### 8.1 Configuration Properties

Configuration properties control the behavior of the broker configuration.

You can view and dynamically update the values of these properties using either DGMGRL or Cloud Control. However, some properties can only be updated through DGMGRL.

A configuration property has configuration-wide scope; meaning that the value you set for the property applies uniformly to each member in the configuration.

Configuration properties are set using the `EDIT CONFIGURATION SET PROPERTY` command, as shown in the following examples.

Example 1

This example sets the `FastStartFailoverThreshold` configuration property to 90 seconds.

```
DGMGRL> EDIT CONFIGURATION SET PROPERTY FastStartFailoverThreshold=90;
```

Example 2

This example sets the `ExternalDestination1` configuration property to point to a redo transport destination with a service name of `Sales ` and a `DB_UNIQUE_NAME` of `chicago`.

```
EDIT CONFIGURATION SET PROPERTY ExternalDestination1='SERVICE=Sales DB_UNIQUE_NAME=chicago';
```

Note:

In general, quotation marks are not necessary around property values unless the case you specify needs to be preserved. By default, DGMGRL lowercases any string you supply, unless it is placed within quotation marks.

Quotation marks are required for any property values that include spaces or punctuation characters (for example, `RedoRoutes`, `LogFileNameConvert`, or `DBFileNameConvert`).

The following sections describe the configuration properties:

- BystandersFollowRoleChange
- CommunicationTimeout
- ConfigurationWideServiceName
- ExternalDestination1
- ExternalDestination2
- FastStartFailoverAutoReinstate
- FastStartFailoverLagLimit
- FastStartFailoverPmyShutdown
- FastStartFailoverThreshold
- ObserverOverride
- ObserverReconnect
- OperationTimeout
- PreferredObserverHosts
- PrimaryLostWriteAction
- TraceLevel

#### 8.1.1 BystandersFollowRoleChange

The `BystandersFollowRoleChange` configuration property establishes whether bystander standby databases are evaluated during failover (value = `ALL`) or after failover (value = `NONE`).

Descriptions of the `ALL` and `NONE` options are as follows:

- `ALL` - During the failover process, the broker determines whether the bystander standby databases are ahead of or behind the failover target standby (that is, the standby that will be the new primary).
	If the bystander standbys are ahead, they will be disabled with a status of `ORA-16661` as part of the failover operation. The bystander standbys must be reinstated after failover completes. The broker reinstates a standby through a flashback to the SCN at which the target standby became a primary database, and sets up the redo transport configuration from the new primary to the standby.
	If the bystander standbys are behind, then the broker simply sets up the redo transport configuration from the soon-to-be-new-primary to these standbys and completes the failover process.
- `NONE` - During the failover process, the broker does NOT evaluate the status of the bystander standbys as part of the failover operation. They are marked as disabled with a status of `ORA-16661` so that they can be evaluated later. The broker simply completes the failover to produce a new primary database as soon as possible.
	After the failover is completed, you can reinstate the bystander standbys. During reinstatement of a bystander, the broker determines whether the bystander is ahead of, or behind, the new primary. If the bystander is ahead of the new primary, then the broker automatically flashes back the standby to the SCN at which the target standby became a primary database and sets up redo transport from the new primary to the standby. (Even if a flashback is not required, the broker sets up the redo transport configuration from the new primary to these standbys.)
	The `NONE` option decreases the processing time for failover, but disables broker management of all bystander databases in the configuration. If fast-start failover is enabled, then the observer automatically reinstates the standby databases after failover has completed. Otherwise, you will have to manually reinstate the standby databases after failover has completed.

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
| Cloud Control name | Not applicable |

#### 8.1.2 CommunicationTimeout

The `CommunicationTimeout` configuration property allows you to decide how many seconds the broker should wait before timing out its network communication between members in the configuration.

A value of zero indicates that a network communication should never be timed out.

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
| Cloud Control name | Not applicable |

#### 8.1.3 ConfigurationWideServiceName

The `ConfigurationWideServiceName` configuration property is used to change the name of the configuration-wide service.

The broker publishes a service on each member of a configuration with a unified service name. The default service name of this configuration-wide service is `primarydbname_CFG`, where the primary database name is appended with a suffix of `_CFG`. The service name does not change after a role transition.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | - The characters are limited to the following: \[a...z\], \[A...Z\], \[0...9\], and \_ - The first character must be an alphanumeric character. - There is a 30–character maximum. |
| Broker default | `primarydbname_CFG` |
| Imported? | No |
| Parameter class | Not applicable |
| Role | Primary and standby |
| Standby type | Not applicable |
| Corresponds to | Not applicable |
| Scope | Configuration |
| Cloud Control name | Not applicable |

#### 8.1.4 ExternalDestination1

The `ExternalDestination1` configuration property is used to specify a redo transport destination that can receive redo data from the current primary database.

Note:

The `Externaldestination1` configuration property is available only in Oracle Database 11g Release 2 (11.2.0.4) and in Oracle Database 12c Release 1 (12.1.0.2) and later.

To set up transport of redo data to the specified destination, the broker uses the values specified for this parameter to define a `LOG_ARCHIVE_DEST_` `n` initialization parameter on the primary database. The broker also monitors the health of the transport to the specified destination.

After a role change, the broker automatically sets up a `LOG_ARCHIVE_DEST_` `n` initialization parameter on the new primary database to ship redo data to the specified destination.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | Any `LOG_ARCHIVE_DEST_` `n` attributes, except the following:  - `ALTERNATE` - `DELAY` - `GROUP` - `LOCATION` - `MANDATORY` - `MAX_FAILURE` - `NET_TIMEOUT` - `PRIORITY` - `SYNC` - `VALID_FOR`  See [Oracle Data Guard Concepts and Administration](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/dgbkr&id=SBYDB01100) for more information about the `LOG_ARCHIVE_DEST_` `n` parameter. |
| Broker default | Empty string |
| Imported? | No |
| Parameter class | Not applicable |
| Role | Primary |
| Standby type | Not applicable |
| Corresponds to | Not applicable |
| Scope | Configuration |
| Cloud Control name | Not applicable |

#### 8.1.5 ExternalDestination2

The `ExternalDestination2` configuration property is used to specify a redo transport destination that can receive redo data from the current primary database.

Note:

The `Externaldestination2` configuration property is available only in Oracle Database 11g Release 2 (11.2.0.4) and in Oracle Database 12c Release 1 (12.1.0.2) and later.

To set up transport of redo data to the specified destination, the broker uses the values specified for this parameter to define a `LOG_ARCHIVE_DEST_` `n` initialization parameter on the primary database. The broker also monitors the health of the transport to the specified destination.

After a role change, the broker automatically sets up a `LOG_ARCHIVE_DEST_` `n` initialization parameter on the new primary database to ship redo data to the specified destination.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | Any `LOG_ARCHIVE_DEST_` `n` attributes, except the following:  - `ALTERNATE` - `DELAY` - `GROUP` - `LOCATION` - `MANDATORY` - `MAX_FAILURE` - `NET_TIMEOUT` - `PRIORITY` - `SYNC` - `VALID_FOR`  See [Oracle Data Guard Concepts and Administration](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/dgbkr&id=SBYDB01100) for more information about the `LOG_ARCHIVE_DEST_` `n` parameter. |
| Broker default | Empty string |
| Imported? | No |
| Parameter class | Not applicable |
| Role | Primary |
| Standby type | Not applicable |
| Corresponds to | Not applicable |
| Scope | Configuration |
| Cloud Control name | Not applicable |

#### 8.1.6 FastStartFailoverAutoReinstate

The `FastStartFailoverAutoReinstate` configuration property causes the former primary database to be automatically reinstated if a fast-start failover was initiated because the primary database was either isolated or had crashed.

To prevent automatic reinstatement of the former primary database in these cases, set this configuration property to `FALSE`.

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
| Cloud Control name | Automatically Reinstate Primary |

#### 8.1.7 FastStartFailoverLagLimit

The `FastStartFailoverLagLimit` configuration property establishes an acceptable limit, in seconds, that the standby is allowed to fall behind the primary in terms of redo applied.

If the limit is reached, then a fast-start failover is not allowed. The lowest possible value is 10 seconds.

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
| Cloud Control name | Lag Limit |

#### 8.1.8 FastStartFailoverPmyShutdown

The `FastStartFailoverPmyShutdown` configuration property causes the primary database to shut down under certain conditions.

The primary database shuts down if fast-start failover is enabled and `V$DATABASE.FS_FAILOVER_STATUS` indicates the primary has been `STALLED` for longer than `FastStartFailoverThreshold` seconds. In such a situation, it is likely that the primary has been isolated and a fast-start failover has already occurred. A value of `TRUE` helps to ensure that an isolated primary database cannot satisfy user queries.

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
| Cloud Control name | Automatically Shutdown Primary |

#### 8.1.9 FastStartFailoverThreshold

The `FastStartFailoverThreshold` configuration property defines the number of seconds the master observer attempts to reconnect to the primary database before initiating a fast-start failover.

(If there is only one observer, then by default it is considered the master. The time interval starts when the observer first loses connection with the primary database. If the observer is unable to regain a connection to the primary database within the specified time, then the observer initiates a fast-start failover to the target standby database. See Task 4 in [Enabling Fast-Start Failover](using-data-guard-broker-to-manage-switchovers-failovers.md) for more information about setting this property.

The observer ignores the threshold completely if a configurable fast-start failover condition is detected or an application has requested that fast-start failover be initiated.

For help in determining an appropriate value for this property, you can use the information provided in the `V$FS_OBSERVER_HISTOGRAM` view. This view displays statistics that are based on the frequency of successful pings between the observer and primary database for different time intervals. (This view is available in Oracle Database 12c Release 1 (12.1.0.2) and later. It is also available in Oracle Database 11g Release 2 (11.2.0.4), but not in Oracle Database 12c Release 1 (12.1.0.1).) See [Oracle Database Reference](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/dgbkr&id=REFRN30735) for a description of the `V$FS_OBSERVER_HISTOGRAM` view.

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
| Cloud Control name | Cloud Control presents this as "Failover Threshold" on the Oracle Data Guard Overview page. |

#### 8.1.10 ObserverOverride

The `ObserverOverride` configuration property, when set to `TRUE`, allows an automatic failover to occur when the observer has lost connectivity to the primary.

This is the behavior even if the standby has a healthy connection to the primary.

| Category | Description |
| --- | --- |
| Datatype | Boolean |
| Valid values | `TRUE` or `FALSE` |
| Broker default | `FALSE` |
| Imported? | No |
| Parameter class | Not applicable |
| Role | Primary and standby |
| Standby type | Not applicable |
| Corresponds to | Not applicable |
| Scope | Broker configuration. This property will be consumed by the observer after fast-start failover has been enabled. |
| Cloud Control name | Not applicable |

#### 8.1.11 ObserverReconnect

The `ObserverReconnect` configuration property specifies how often the observer establishes a new connection to the primary database.

When this property is set to the default value of 0, the observer creates and maintains a connection to the primary database, but it does not periodically create a new connection to the primary database. While this eliminates the processing overhead associated with periodically establishing a new observer connection to the primary database, it also prevents the observer from detecting that it is not possible to create new connections to the primary database. Oracle recommends that this property be set to a value that is small enough to allow timely detection of faults at the primary database, but large enough to limit the overhead associated with periodic observer connections to an acceptable level.

| Category | Description |
| --- | --- |
| Datatype | Integer |
| Valid values | Integral number of seconds. Must be greater than, or equal to, 0. |
| Broker default | 0 |
| Imported? | No |
| Parameter class | Not applicable |
| Role | Primary and standby |
| Standby type | Not applicable |
| Corresponds to | Not applicable |
| Scope | Broker configuration. This property will be consumed by the observer after fast-start failover has been enabled. |
| Cloud Control name | Not applicable |

#### 8.1.12 OperationTimeout

The `OperationTimeout` configuration property specifies the maximum amount of time the broker should wait for health check, get monitorable property, and set property operations to complete.

| Category | Description |
| --- | --- |
| Datatype | Integer |
| Valid values | \>= 30 and <= 3600 |
| Broker default | 30 seconds |
| Imported? | No |
| Parameter class | Not applicable |
| Role | Primary and standby |
| Standby type | Not applicable |
| Corresponds to | Not applicable |
| Scope | Broker configuration. This property will be consumed by broker on all databases in the configuration. |
| Cloud Control name | Not applicable |

#### 8.1.13 PreferredObserverHosts

The `PreferredObserverHosts` configurable property allows you to list the hosts that you would prefer as hosts for the master observer when that database is in the primary role.

The value of this property can be changed at any time, regardless of whether Fast-Start Failover is enabled or not, or whether the observer is in an OBSERVED state. However, the change does not affect the location of the master observer until the next role change.

If this property is set, then after a role change the broker takes the following steps:

1. Checks whether the current master observer is running on a host in the list specified by the `PreferredObserverHosts` property of the new primary. If yes, stop here; otherwise, go to step 2.
2. Scans the list from the beginning to look for a host where one observer is running, and connects to the primary and target standby databases. If found, go to step 3; otherwise, stop here.
3. Attempts to switch the master observer to the host found in step 2. If switching fails, no other hosts are tried.

| Category | Description |
| --- | --- |
| Data type | String |
| Valid value | A character string that contains one or more host names, separated by comma: ``` host_name_1 [,host_name_n] ```  Each host name can be any character string for a valid network name, even if there is no observer running on this host when it is set. |
| Broker default | Null |
| Imported? | No |
| Parameter class | Not applicable |
| Role | Primary, standby |
| Standby type | Physical standby and logical standby |
| Corresponds to | Not applicable |
| Scope | Database |
| Cloud Control name | Not applicable |

#### 8.1.14 PrimaryLostWriteAction

The `PrimaryLostWriteAction` configuration property determines what action is taken if a standby database detects that a lost write has occurred at the primary database.

Note:

The `PrimaryLostWriteAction` configuration property is available only in Oracle Database 11g Release 2 (11.2.0.4) and in Oracle Database 12c Release 1 (12.1.0.2) and later.

The possible actions are as follows:

- `CONTINUE` - The primary database continues operating even if a standby database detects that a lost write has occurred at the primary database. This is the default action.
- `SHUTDOWN` - If a standby database detects that a lost write has occurred at the primary database, then fast start failover is disabled and the primary database performs a shutdown abort. Automatic failover will not occur.
- `FAILOVER` - If fast-start failover is enabled in maximum performance mode, and the configuration is within the acceptable limit specified for the `FastStartFailoverLagLimit` property, then the observer initiates a failover.
- `FORCEFAILOVER` - If fast-start failover is enabled (in either maximum performance or maximum availability mode), then the observer initiates a failover. This option results in a data loss failover.

For both the `FAILOVER` and `FORCEFAILOVER` options, if fast-start failover is disabled then no failover occurs, but the primary is shut down.

Fast start failover is disabled if a standby detects that a lost write has occurred at the primary database. Automatic failover will therefore not occur if a standby detects that a lost write has occurred at the primary database, even if `PrimaryLostWriteAction` is set to `SHUTDOWN`.

Diagnostic information is written to the database alert and broker logs at the primary database and at the standby database where the lost write was detected.

If a lost write occurs at the primary database, then follow the guidelines in "Resolving ORA-752 or ORA-600 \[3020\] During Standby Recovery" in My Oracle Support Note 1265884.1 located at [`http://support.oracle.com`](http://support.oracle.com/).

Note:

The `DB_LOST_WRITE_PROTECT` database initialization parameter must be set to `TYPICAL` or `FULL` at the primary database and at each standby database in the configuration to ensure that lost primary writes can be detected by all standby databases in the configuration.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | `CONTINUE`, `SHUTDOWN`, `FAILOVER`, or `FORCEFAILOVER` |
| Broker default | `CONTINUE` |
| Imported? | No |
| Parameter class | Not applicable |
| Role | Primary and standby |
| Standby type | Not applicable |
| Corresponds to | Not applicable |
| Scope | Broker configuration |
| Cloud Control name | Not applicable |

#### 8.1.15 TraceLevel

The `TraceLevel` configuration property is used to control the amount of tracing performed by the broker for every member in the configuration.

Setting the property to `USER` limits the tracing to completed operations and to any warning or error messages resulting from an operation or health check. Setting the property to `SUPPORT` increases the amount of tracing to include lower-level information needed by Oracle Support Services.

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
| Cloud Control name | Not applicable |

### 8.2 Monitorable (Read-Only) Properties

Monitorable properties allow you to view information related to the database, database instance, or far sync instance.

You cannot change the values of monitorable properties. You can view all of them using the DGMGRL `SHOW` commands.

Note:

Information for monitorable properties can be seen only when broker management of the entity is enabled. Cloud Control displays the information obtained from these properties on the Property page.

If the database is an Oracle RAC database, the output values of some properties may also show instance-specific information. For example if the primary database is an Oracle RAC database, `LogXptStatus` may show `Instance1` transmitting redo data to `Standby2` has an error and `Instance2` transmitting redo data to `Standby4` has an error.

The following sections describe the monitorable properties:

- InconsistentLogXptProps (Inconsistent Redo Transport Properties)
- InconsistentProperties (Inconsistent Properties)
- LogXptStatus (Redo Transport Status)
- LsbyFailedTxnInfo (Logical Standby Failed Transaction Information)
- LsbyParameters (Logical Standby Parameters)
- RecvQEntries (Receive Queue Entries)
- SendQEntries (Send Queue Entries)
- TopWaitEvents

#### 8.2.1 InconsistentLogXptProps (Inconsistent Redo Transport Properties)

The `InconsistentLogXptProps` monitorable property returns a table that shows all properties related to redo transport services whose values are inconsistent between the broker configuration file and the runtime value.

Although the properties reported in this table are database-specific or far sync instance-specific properties, the inconsistency is reported on an instance-specific basis. A database or far sync instance-specific property only ensures that there is one value in the broker's configuration file for all instances of the database or far sync instance, but the runtime values can be different. This means that a database or far sync instance-specific property may be inconsistent only on some instances.

This property pertains to the primary database, a physical standby database that ships redo data, or a far sync instance. The table contains the following columns:

- `INSTANCE_NAME`
	The value identifying the SID for the instance.
- `STANDBY_NAME`
	The database unique name (`DB_UNIQUE_NAME`) of the standby database or far sync instance to which this redo transport services property pertains.
- `PROPERTY_NAME`
	The name of the redo transport services property with an inconsistent value.
- `MEMORY_VALUE`
	The runtime value being used in the database or far sync instance.
- `BROKER_VALUE`
	The value of the redo transport services property saved in the broker configuration file.

#### 8.2.2 InconsistentProperties (Inconsistent Properties)

The `InconsistentProperties` monitorable property shows all property values in the broker configuration file that are inconsistent with the values in the corresponding server parameter file or the runtime values.

The information is shown in table format. Although the properties reported in this table are database-specific or far sync instance-specific properties, the inconsistency is reported on an instance-specific basis. A database or far sync instance-specific property only ensures that there is one value in the broker's configuration file for all instances of the database or far sync instance, but the runtime values can be different. This means that a database or far sync instance-specific property may be inconsistent only on some instances

Each individual configuration member has this property. The table contains the following columns:

- `INSTANCE_NAME`
	The value identifying the SID for the instance.
- `PROPERTY_NAME`
	The name of the property with the inconsistent value.
- `MEMORY_VALUE`
	The corresponding runtime value being used.
- `SPFILE_VALUE`
	The corresponding value saved in the server parameter file (SPFILE).
- `BROKER_VALUE`
	The value of the property saved in the broker configuration file.

#### 8.2.3 LogXptStatus (Redo Transport Status)

The `LogXptStatus` monitorable property returns a table that contains the error status of redo transport services for each of the enabled configuration members.

This property pertains to the primary database, a physical standby database that ships redo data, or a far sync instance.

The table contains the following columns:

- `PRIMARY_INSTANCE_NAME`
	The value identifying the SID for the instance on the primary database.
- `STANDBY_DATABASE_NAME`
	The database unique name (`DB_UNIQUE_NAME`) of the standby database or far sync instance.
- `ERROR`
	The text of the redo transport error. If there is no error, the field is empty.

Each entry in the table indicates the status of redo transport services on one redo source to one redo destination.

The error status can be an empty string, which indicates there is no error.

In the following example, the `STATUS` from `South_Sales` is empty because there is no error for the `South_Sales` destination. The `South_Report` destination returned the `ORA-01034` message.

```
DGMGRL> SHOW DATABASE 'North_Sales' 'LogXptStatus' ;
LOG TRANSPORT STATUS
PRIMARY_INSTANCE_NAME STANDBY_DATABASE_NAME               STATUS
         north_sales1          South_Sales
         north_sales1          South_Report    ORA-01034: ORACLE not available
```

#### 8.2.4 LsbyFailedTxnInfo (Logical Standby Failed Transaction Information)

The `LsbyFailedTxnInfo` monitorable property identifies a failed transaction that caused log apply services to stop.

This property contains a string with the following values from the `DBA_LOGSTDBY_EVENTS` view:

- `XIDUSN`: Transaction ID undo segment number
- `XIDSLT`: Transaction ID slot number
- `XIDSQN`: Transaction ID sequence number
- `STATUS_CODE`: Status (or Oracle error code) belonging to the `STATUS` message
- `STATUS`: Description of the current activity of the process or the reason why log apply services stopped

The transaction IDs and status information are separated by a string of number signs (###).

This property pertains to a logical standby database.

#### 8.2.5 LsbyParameters (Logical Standby Parameters)

The `LsbyParameters` monitorable property contains a string that identifies the value of `MAX_SGA` and `MAX_SERVERS` specifically reserved for log apply services.

The `MAX_SGA` is the maximum system global area and `MAX_SERVERS` is the maximum number of parallel query servers. These values are separated by a string of number signs (###) in the `LsbyParameters` property.

This property pertains to a logical standby database.

#### 8.2.6 RecvQEntries (Receive Queue Entries)

The `RecvQEntries` monitorable property returns a table indicating all log files that were received by the standby database but have not yet been applied.

If no rows are returned, it implies all log files received have been applied. This property pertains to a standby database.

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

Cloud Control displays this information on the Log File Details page.

#### 8.2.7 SendQEntries (Send Queue Entries)

The `SendQEntries` monitorable property returns a table that shows all log files on the primary database that were not successfully archived to one or more standby databases.

This property pertains to the primary database.

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

Cloud Control displays this information on the Log File Details page.

#### 8.2.8 TopWaitEvents

The `TopWaitEvents` monitorable property specifies the 5 events with the longest waiting time in the specified instance.

The events and their waiting time are retrieved from `V$SYSTEM_EVENT`. Each instance in the configuration has this property. This property is an instance-specific monitorable property. The table contains the following columns in the order shown:

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

### 8.3 Configurable Properties

Configurable properties control the behavior of broker configuration members.

You can view and dynamically update the values of these properties using either DGMGRL or Cloud Control. However, some properties can only be updated through DGMGRL.

These properties control certain database initialization parameters and SQL statements that the broker uses to manage an Oracle Data Guard broker configuration. Therefore, you should not manually set those initialization parameters or issue those SQL statements on a broker configuration.

In most cases, the configurable property is said to apply to the entire member, meaning the value you set for the property applies to each instance of the member (that is, database or far sync instance). However, in a few cases, the configurable property is said to have instance-specific scope which means that for a multiple-instance database or far sync instance, it is possible that the values of some particular properties may differ between instances. The following table lists each configurable property and indicates whether the scope of the property is member-wide or instance-specific. If the Scope column contains:

- Member—The value of the property is database or far sync instance-wide, not instance or configuration specific.
- Instance—The value of the property is instance specific.
	If there is an asterisk (\*) present, it indicates that the property value can be set for all instances of an Oracle RAC database using the `EDIT INSTANCE * ON DATABASE` command.
- Configuration—The value of the property is configuration wide, not instance or member specific.

Table 8-1 Configurable Properties

| Configurable Property Name | Scope | Pertains To |
| --- | --- | --- |
| AlternateLocation | Instance | Redo transport services |
| ApplyInstances | Member | Redo Apply |
| ApplyInstanceTimeout | Member | Redo Apply and SQL Apply |
| ApplyLagThreshold | Member | Redo transport services |
| ApplyParallel | Member | Redo Apply |
| ArchiveLagTarget | Member | Redo transport services |
| Binding | Member | Redo transport services |
| DataGuardSyncLatency | Member | Redo transport services |
| DbFileNameConvert | Member | Redo Apply |
| DelayMins | Member | Redo Apply and SQL Apply |
| DGConnectIdentifier | Member | Broker communication, Redo transport services |
| Encryption | Member | Redo transport services |
| FastStartFailoverTarget | Member | Fast-start failover |
| LogArchiveFormat | Instance \* | Redo transport services |
| LogArchiveMaxProcesses | Member | Redo transport services |
| LogArchiveMinSucceedDest | Member | Redo transport services |
| LogArchiveTrace | Instance \* | Diagnosis |
| LogFileNameConvert | Member | Redo Apply |
| LogShipping | Member | Redo transport services |
| LogXptMode | Member | Redo transport services |
| LsbyMaxEventsRecorded | Member | SQL Apply |
| LsbyMaxServers | Instance \* | SQL Apply |
| LsbyMaxSga | Instance \* | SQL Apply |
| LsbyPreserveCommitOrder | Member | SQL Apply |
| LsbyRecordAppliedDdl | Member | SQL Apply |
| LsbyRecordSkipDdl | Member | SQL Apply |
| LsbyRecordSkipErrors | Member | SQL Apply |
| MaxConnections | Member | Redo transport services |
| MaxFailure | Member | Redo transport services |
| NetTimeout | Member | Redo transport services |
| ObserverConnectIdentifier | Member | Fast-start failover |
| PreferredApplyInstance | Member | Redo Apply and SQL Apply |
| PreferredObserverHosts | Member | Fast-start failover |
| RedoCompression | Member | Redo transport services |
| RedoRoutes | Member | Redo transport services |
| ReopenSecs | Member | Redo transport services |
| SidName | Instance | Instance identification |
| StandbyArchiveLocation | Instance | Redo transport services |
| StandbyFileManagement | Member | Redo Apply and SQL Apply |
| StaticConnectIdentifier | Instance | Instance Startup and Shutdown |
| TransportDisconnectedThreshold | Member | Redo transport services |
| TransportLagThreshold | Member | Redo transport services |

See Also:

[Managing the Members of a Broker Configuration](managing-oracle-data-guard-broker-configuration-members.md) for more information about property management

Note:

When a broker configuration with its primary database is created and members are added to the configuration, the broker imports existing settings from the members to set many of the properties. If importing an existing setting fails, or if a property value is not imported, then the broker uses a broker default value. The default values and whether or not a property is imported is indicated within each property description.

Broker Controlled Database Initialization Parameters and SQL Statements

The following database initialization parameters are controlled by broker configurable properties. Therefore, you should not set these parameters manually:

- `LOG_ARCHIVE_DEST_` `n`
- `LOG_ARCHIVE_DEST_STATE_` `n`
- `ARCHIVE_LAG_TARGET`
- `DB_FILE_NAME_CONVERT`
- `LOG_ARCHIVE_FORMAT`
- `LOG_ARCHIVE_MAX_PROCESSES`
- `LOG_ARCHIVE_MIN_SUCCEED_DEST`
- `LOG_ARCHIVE_TRACE`
- `LOG_FILE_NAME_CONVERT`
- `STANDBY_FILE_MANAGEMENT`

The broker also uses configurable property settings to manage how apply is to be started. Therefore, the following SQL statements are managed automatically by the broker:

- `ALTER DATABASE RECOVER MANAGED STANDBY DATABASE`
- `ALTER DATABASE START LOGICAL STANDBY APPLY IMMEDIATE`

The broker sets the following apply parameters on a logical standby automatically; you should not manually set them:

- `MAX_EVENTS_RECORDED`
- `MAX_SERVERS`
- `MAX_SGA`
- `PRESERVE_COMMIT_ORDER`
- `RECORD_APPLIES_DDL`
- `RECORD_SKIP_DDL`
- `RECORD_SKIP_ERRORS`

#### 8.3.1 AlternateLocation

The `AlternateLocation` configurable property specifies an alternate disk location to store the archived redo log files in the standby when the location specified by the `StandbyArchiveLocation` configurable property fails.

The property has instance-specific scope, and the location it specifies has to be accessible by the instance.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | Directory specification on system where the standby instance is located |
| Broker default | Empty string |
| Imported? | No |
| Parameter class | Dynamic |
| Role | Standby database, far sync instance, Recovery Appliance |
| Standby type | Physical, logical, or snapshot standby, or a far sync instance or Recovery Appliance |
| Corresponds to | - On the standby database or the far sync instance, the `LOCATION` attribute for the `LOG_ARCHIVE_DEST_` `n` initialization parameter that represents an alternate destination of the local destination that matches the configurable property StandbyArchiveLocation. |
| Scope | Instance |
| Cloud Control name | `Alternate Standby Location` |

Note:

On a logical standby database, Oracle recommends the `LOCATION` attribute of the `LOG_ARCHIVE_DEST_` `n` initialization parameter for the local destination be different from the value of `AlternateLocation` configurable property.

#### 8.3.2 ApplyInstances

The `ApplyInstances` property lets you specify how many physical standby instances run Redo Apply.

As of Oracle Database 12c Release 2 (12.2.0.1), a new `INSTANCES` keyword is available on the SQL `ALTER RECOVER MANAGED STANDBY DATABASE` statement (only for Oracle Real Application Clusters (Oracle RAC) or Oracle RAC One Node databases). When used, it causes Redo Apply to run on each active running physical standby instance that is running in the same mode as the instance on which Redo Apply was started. You can specify `ALL` or you can specify a specific number to restrict the number of instances that Redo Apply uses. If a database has already been set up to run Redo Apply on multiple instances, then you can use the Data Guard broker property `ApplyInstances` to restrict the number of instances that are involved in Redo Apply on an Oracle RAC physical standby database.

See Also:

- [Oracle Data Guard Concepts and Administration](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/dgbkr&id=SBYDB-GUID-00B72AF1-0453-4FBD-901F-A3764631BE1F) for more information about setting up multi-instance Redo Apply.

| Category | Description |
| --- | --- |
| Datatype | Integer |
| Valid values | 0 to 16, ALL - ALL: indicates that redo apply will be started on all currently active instances - 0 and 1: recovery will be started in single instance mode. - \>1: indicates that redo apply should not run on any more than the number of instances specified. |
| Broker default | The default is 0. |
| Imported? | Yes |
| Parameter class | Not applicable |
| Role | Standby |
| Standby type | Physical standby |
| Corresponds to | `INSTANCES` keyword of `ALTER DATABASE RECOVER MANAGED STANDBY DATABASE` command. |
| Scope | Database |
| Cloud Control name | Not applicable |

#### 8.3.3 ApplyInstanceTimeout

The `ApplyInstanceTimeout` configurable property specifies the number of seconds the broker waits after detecting the current apply instance failed before initiating the apply instance failover.

| Category | Description |
| --- | --- |
| Datatype | Integer |
| Valid values | `>=0` (seconds) |
| Broker default | `0` (results in immediate apply instance failover) |
| Imported? | No |
| Parameter class | Not applicable |
| Role | Standby, Recovery Appliance |
| Standby type | Physical, logical, Recovery Appliance |
| Corresponds to | Not applicable |
| Scope | Database |
| Cloud Control name | Not applicable |

#### 8.3.4 ApplyLagThreshold

The `ApplyLagThreshold` configurable property generates a warning status for a logical or physical standby when the member's apply lag exceeds the value specified by the property.

The property value is expressed in seconds. A value of 0 seconds results in no warnings being generated when an apply lag exists.

| Category | Description |
| --- | --- |
| Datatype | Number |
| Valid values | \>=0 |
| Broker default | 30 seconds |
| Imported? | No |
| Parameter class | Not applicable |
| Role | Standby, Recovery Appliance |
| Standby type | Physical, logical |
| Corresponds to | Not applicable |
| Scope | Database |
| Cloud Control name | Not applicable |

#### 8.3.5 ApplyParallel

The `ApplyParallel` configurable property specifies whether Redo Apply should use multiple processes to apply redo data to the physical standby database.

If Redo Apply is shut off, then setting the property has no immediate effect. However, when Redo Apply is running again, the value of the property is used to determine the parallel apply behavior of Redo Apply.

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
| Cloud Control name | Not applicable |

#### 8.3.6 ArchiveLagTarget

The `ArchiveLagTarget` configurable property limits the amount of data that can be lost.

In effect, limiting the amount of data that can be lost increases the availability of the standby database by forcing a log switch after the amount of time you specify (in seconds) elapses. That way, the standby database will not miss redo records generated from a time range longer than the value set for the `ARCHIVE_LAG_TARGET` initialization parameter.

| Category | Description |
| --- | --- |
| Datatype | Number |
| Valid values | Seconds (either 0 seconds, or any number from 60 to 7200 seconds) |
| Broker default | Value imported from the `ARCHIVE_LAG_TARGET` initialization parameter |
| Imported? | Yes, from the `ARCHIVE_LAG_TARGET` initialization parameter |
| Parameter class | Dynamic |
| Role | Primary database, far sync instance, Recovery Appliance |
| Standby type | Not applicable |
| Corresponds to | `ARCHIVE_LAG_TARGET=` `seconds` initialization parameter |
| Scope | Database |
| Cloud Control name | `Archive Lag Target` |

#### 8.3.7 Binding

The `Binding` configurable property specifies whether the destination is `MANDATORY` or `OPTIONAL`.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | - `MANDATORY` 	You can specify a policy for reuse of online redo log files using the `MANDATORY` value. If the archiving operation of a mandatory destination fails, online redo log files cannot be overwritten. - `OPTIONAL` 	You can specify a policy for reuse of online redo log files using the `OPTIONAL` value. If the archiving operation of an optional destination fails, the online redo log files are overwritten. |
| Broker default | `OPTIONAL` |
| Imported? | No |
| Parameter class | Dynamic |
| Role | Standby database, Recovery Appliance, far sync instance <sup>Foot 1</sup> |
| Standby type | Physical, logical, or snapshot standby, far sync instance, Recovery Appliance |
| Corresponds to | - `MANDATORY` and `OPTIONAL` attributes for the `LOG_ARCHIVE_DEST_` `n` initialization parameter of the database or far sync instance that is sending redo data - `BINDING` column of the `V$ARCHIVE_DEST` view of the database or far sync instance that is sending redo data |
| Scope | Database, far sync instance, Recovery Appliance |
| Cloud Control name | Not applicable |

<sup>Footnote 1</sup>

Although this property is set for the redo destination, it is indirectly related to the redo transport services for the database or far sync instance that is sending redo data. The broker propagates the setting you specify to the corresponding attributes of the `LOG_ARCHIVE_DEST_` `n` value of the database or far sync instance that is sending redo data.

#### 8.3.8 DataGuardSyncLatency

The `DataGuardSyncLatency` database property supports the database initialization parameter, `DATA_GUARD_SYNC_LATENCY`.

The database initialization parameter, `DATA_GUARD_SYNC_LATENCY`, applies to all synchronous standby destinations. It defines the maximum amount of time (in seconds) that the primary database must wait before disconnecting subsequent destinations after at least one synchronous standby has acknowledged receipt of the redo. If you add a member to a broker configuration, then the broker automatically determines the `DATA_GUARD_SYNC_LATENCY` value and updates broker metadata with that value. If you edit the `DataGuardSyncLatency` property, then the broker updates the ` DATA_GUARD_SYNC_LATENCY` parameter on the database.

The broker periodically runs a health-check routine to check the consistency between the value of the `DataGuardSyncLatency` property value and the value of the `DATA_GUARD_SYNC_LATENCY` initialization parameter on each member of the configuration. If an inconsistency is found, the health-check report signals an error.

| Category | Description |
| --- | --- |
| Data type | Integer |
| Valid values | \>= 0 |
| Broker default | Value imported from the `DATA_GUARD_SYNC_LATENCY` database initialization parameter. |
| Imported? | Yes, from the `DATA_GUARD_SYNC_LATENCY` initialization parameter |
| Parameter class | Dynamic |
| Role | Primary |
| Standby type | Not applicable |
| Corresponds to | `DATA_GUARD_SYNC_LATENCY` database initialization parameter |
| Scope | Database |
| Cloud Control name | Not applicable |

#### 8.3.9 DbFileNameConvert

The `DbFileNameConvert` configurable property distinguishes physical standby datafile filenames from primary datafile filenames.

If you add a datafile to the primary database, this property converts the datafile name on the primary database to the datafile on the physical standby database.

This property is used in the following situations:

- At physical standby mount time, it is used to rename primary datafile filenames to standby datafile filenames if the datafile file path on the physical standby system is different from the primary database system.
- When a new data file is created on the primary database, a corresponding new data file will be created on the physical standby database if the `StandbyFileManagement` configurable property is set to `'AUTO'`. Oracle uses the data-file file-path mapping information from the `DbFileNameConvert` property to determine the standby file path of the new standby data file. If the `StandbyFileManagement` property is set to `'MANUAL'`, you must add a corresponding file to the physical standby database.

Note:

When a database is added to the configuration, the broker sets the initial value of this property to the in-memory value of the `DB_FILE_NAME_CONVERT` initialization parameter. It is possible that the in-memory value and server parameter file (SPFILE) value of this parameter will differ. If you want to use the parameter's in-memory value, then enable the database and the broker will ensure that the SPFILE value of the parameter is set to the in-memory value. If you want to use the SPFILE value, then set the property value to be the parameter's value stored in the SPFILE. Then enable the database.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | Set the value of this property to a list of string pairs:  1. The first string is the substring found in the datafile names on the primary database. 2. The second string is the substring found in the datafile names on the standby database.  For example, `('string1', 'string2', 'string3', 'string4',...)`  Where:  - `string1` is the substring of the primary database filename. - `string2` is the substring of the standby database filename. - `string3` is the substring of the primary database filename. - `string4` is the substring of the standby database filename. |
| Broker default | Value of the `DB_FILE_NAME_CONVERT` initialization parameter |
| Imported? | Yes, from the `DB_FILE_NAME_CONVERT` initialization parameter |
| Parameter class | Static |
| Role | Standby |
| Standby type | Physical |
| Corresponds to | `DB_FILE_NAME_CONVERT` initialization parameter |
| Scope | Database |
| Cloud Control name | `DB File Name Convert` |

#### 8.3.10 DelayMins

The `DelayMins` configurable property specifies the number of minutes log apply services will delay applying the archived redo log data on the standby database.

When the `DelayMins` property is set to the default value of 0 minutes, log apply services apply redo data as soon as possible.

If the `DelayMins` property is set to 0, start log apply services as follows:

- Start Redo Apply on physical standby databases using the following SQL statement:
	```
	ALTER DATABASE RECOVER MANAGED STANDBY DATABASE;
	```
- Start SQL Apply on logical standby databases using the following SQL statement:
	```
	ALTER DATABASE START LOGICAL STANDBY APPLY IMMEDIATE;
	```

| Category | Description |
| --- | --- |
| Datatype | Integer |
| Valid values | \>=0 (minutes) <sup>Foot 2</sup> |
| Broker default | `0` |
| Imported? | No |
| Parameter class | Dynamic |
| Role | Standby <sup>Foot 3</sup>, Recovery Appliance |
| Standby type | Physical, logical, Recovery Appliance |
| Corresponds to | - `DELAY` attribute for the `LOG_ARCHIVE_DEST_` `n` initialization parameter of the database or far sync instance that is sending redo data - `DELAY_MINS` column of the `V$ARCHIVE_DEST` view of the database or far sync instance that is sending redo data - Options used to start Redo Apply and SQL Apply |
| Scope | Database |
| Cloud Control name | `Apply Delay (mins)` |

<sup>Footnote 2</sup> The `DelayMins` property must be reset to 0 before attempting a switchover to a standby with `DelayMins` greater than 0.

<sup>Footnote 3</sup>

Although this property is set for the standby database, it is indirectly related to the redo transport services for the database or far sync instance that is sending redo data. The broker propagates the setting you specify on the standby database to the corresponding attributes of the `LOG_ARCHIVE_DEST_` `n` value of the database or far sync instance that is sending redo data.

#### 8.3.11 DGConnectIdentifier

The `DGConnectIdentifier` configurable property specifies the connection identifier the broker uses when making connections to a configuration member.

If you are using DGMGRL, then you supply the value when you enter the `CREATE` `CONFIGURATION`, `ADD` `DATABASE`, or `ADD` `FAR_SYNC` command. If you are using Cloud Control, the value is supplied automatically. The connect identifier for a configuration member must:

- Allow all other members in the configuration to reach it.
- Allow the member to reach itself.
- Allow all instances of an Oracle RAC database to be reached.
- Specify a service that all instances dynamically register with the listeners so that connect-time failover on an Oracle RAC database is possible.
	Caution:
	The service should NOT be one that is defined and managed by Oracle Clusterware.
- Have failover attributes set to allow the primary database's Redo Transport Services to continue shipping redo data to an Oracle RAC standby database, even if the receiving instance of that standby database has failed.

The value of this property is specified in the `SERVICE` attribute of the `LOG_ARCHIVE_DEST_` n parameter when the broker configures redo transport services on the primary database.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | A connect identifier that can be used to connect to this database |
| Broker default | Not applicable |
| Imported? | No |
| Parameter class | Not applicable |
| Role | Primary, standby, far sync instance, Recovery Appliance |
| Standby type | Physical, logical, or snapshot standby, far sync instance, Recovery Appliance |
| Corresponds to | `SERVICE_NAME` attribute of the `LOG_ARCHIVE_DEST_` `n` initialization parameter of the configuration member that is sending redo data |
| Scope | Database, far sync instance, Recovery Appliance |
| Cloud Control name | Not applicable |

See Also:

[Oracle Database Net Services Administrator's Guide](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/dgbkr&id=NETAG186)

#### 8.3.12 Encryption

The `Encryption` configurable property is used to specify whether redo data is encrypted before transmitting it to a Recovery Appliance.

Note:

Redo transport encryption can only be used with a Recovery Appliance.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | `DISABLE`, `ENABLE` - When `ENABLE` is specified, the redo data is encrypted before it is sent to a Recovery Appliance. - When `DISABLE` is specified, the redo data is not encrypted before it is sent to a Recovery Appliance. |
| Broker Default | `DISABLE` |
| Imported? | No |
| Parameter class | Dynamic |
| Role | Recovery Appliance |
| Standby type | Recovery Appliance |
| Corresponds to | - `ENCRYPTION` attribute for the `LOG_ARCHIVE_DEST_n` initialization parameter of the database or far sync instance that is sending redo data - `ENCRYPTION` column of the `V$ARCHIVE_DEST` view of the database or far sync instance that is sending redo data to the Recovery Appliance |
| Scope | Recovery Appliance |
| Cloud Control name | Not Applicable |

#### 8.3.13 FastStartFailoverTarget

The `FastStartFailoverTarget` configuration property specifies the `DB_UNIQUE_NAME` of one or more standby databases that can act as target databases in a fast-start failover situation when the database on which the property is set is the primary database.

These possible target databases are referred to as candidate fast-start failover targets. See Task 2 in [Enabling Fast-Start Failover](using-data-guard-broker-to-manage-switchovers-failovers.md) for more information about setting this property.

The `FastStartFailoverTarget` configuration property can only be set to the name of physical or logical standbys. It cannot be set to the name of a snapshot standby database, far sync instance, or Zero Data Loss Recovery Appliance.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid value | `DB_UNIQUE_NAME` of the database that is the target of the fast-start failover. You can specify names of multiple standbys or the keyword `ANY`. If multiple names are specified, then the broker selects them in the order in which they are listed. If the property is set to `ANY`, then the broker can select any one of all viable standbys of the primary as the current FSFO target. |
| Broker default | If only one physical or logical standby database exists, then the broker selects that as the default value for this property on the primary database when fast-start failover is enabled.  If more than one physical or logical standby database exists, then the broker selects one based on the order in which they are specified in the property definition. Targets are verified when fast-start failover is enabled.  For the target standby database, the broker automatically selects the current primary database as the value for this property when fast-start failover is enabled. |
| Imported? | No |
| Parameter class | Not applicable |
| Role | Primary or standby |
| Standby type | Physical or logical |
| Corresponds to | Not applicable |
| Scope | Database |
| Cloud Control name | Cloud Control displays the value for the current primary database on the Oracle Data Guard Overview page, along with whether or not fast-start failover has been enabled. |

#### 8.3.14 LogArchiveFormat

The `LogArchiveFormat` configurable instance-specific property specifies the format for filenames of archived redo log files.

To specify the format, it uses a database ID (`%d`), thread (`%t`), sequence number (`%s`), and resetlogs ID (`%r`).

Note:

When a member is added to the configuration, the broker sets the initial value of this property to the in-memory value of the `LOG_ARCHIVE_FORMAT` initialization parameter. It is possible that the in-memory value and server parameter file (SPFILE) value of this parameter will differ. If you want to use the parameter's in-memory value, then enable the member and the broker will ensure that the SPFILE value of the parameter is set to the in-memory value. If you want to use the SPFILE value, then set the property value to be the parameter's value stored in the SPFILE. Then enable the member.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | `%d_%t_%s_%r` |
| Broker default | Value of the `LOG_ARCHIVE_FORMAT` initialization parameter |
| Imported? | Yes, from the `LOG_ARCHIVE_FORMAT` initialization parameter on the primary database |
| Parameter class | Static |
| Role | Primary, standby, far sync instance |
| Standby type | Physical, logical, or snapshot standby, or a far sync instance |
| Corresponds to | `LOG_ARCHIVE_FORMAT` initialization parameter |
| Scope | Instance (On an Oracle RAC database, you can use the `EDIT INSTANCE * ON DATABASE ` command to have all instances use the same value for this property.) |
| Cloud Control name | Not applicable |

#### 8.3.15 LogArchiveMaxProcesses

The `LogArchiveMaxProcesses` configurable property specifies the initial number of archiver processes (ARCn) that are invoked.

The actual number of archiver processes in use may increase subsequently based on the archiving workload.

| Category | Description |
| --- | --- |
| Datatype | Integer |
| Valid values | 1 to 30 |
| Broker default | Value of the ` LOG_ARCHIVE_MAX_PROCESSES` initialization parameter |
| Imported? | Yes, from the `LOG_ARCHIVE_MAX_PROCESSES` initialization parameter |
| Parameter class | Dynamic |
| Role | Primary, standby, far sync instance, Recovery Appliance |
| Standby type | Physical, logical, or snapshot standby, far sync instance, Recovery Appliance |
| Corresponds to | `LOG_ARCHIVE_MAX_PROCESSES` initialization parameter |
| Scope | Database, far sync instance |
| Cloud Control name | `Archiver Processes` |

#### 8.3.16 LogArchiveMinSucceedDest

The `LogArchiveMinSucceedDest` configurable property controls when online redo log files are available for reuse.

For the online redo log files to be available for reuse, archiving must succeed to a minimum number of destinations.

| Category | Description |
| --- | --- |
| Datatype | Integer |
| Valid values | 1 to 10 |
| Broker default | Value of the `LOG_ARCHIVE_MIN_SUCCEED_DEST` initialization parameter |
| Imported? | Yes, from the `LOG_ARCHIVE_MIN_SUCCEED_DEST` initialization parameter |
| Parameter class | Dynamic |
| Role | Primary database, far sync instance, Recovery Appliance |
| Standby type | Not applicable |
| Corresponds to | `LOG_ARCHIVE_MIN_SUCCEED_DEST` initialization parameter |
| Scope | Database, far sync instance |
| Cloud Control name | Not applicable |

#### 8.3.17 LogArchiveTrace

Set the `LogArchiveTrace` configurable instance-specific property to an integer value to see the progression of the archiving of online redo log files on the primary and the standby databases.

The Oracle database writes an audit trail of the archived redo log files received from the primary database into process trace files.

| Category | Description |
| --- | --- |
| Datatype | Integer |
| Valid values | A valid value is the sum of any combination of any of the following values:  0: Disable archive redo log tracing  1: Track archiving of online redo log file  2: Track archiving status of each archive redo log destination  4: Track archiving operational phase  8: Track `ARCHIVELOG` destination activity  16: Track detailed `ARCHIVELOG` destination activity  32: Track `ARCHIVELOG` destination parameter modifications  64: Track ARC `n` process state activity  128: Track FAL (fetch archive log) server related activities  256: Tracks RFS Logical Client  512: Tracks LGWR redo shipping network activity  1024: Tracks RFS physical client  2048: Tracks RFS/ARCn ping heartbeat  4096: Tracks real-time apply activity  8192: Tracks Redo Apply (media recovery or physical standby)  16384: Tracks archive I/O buffers  32768: Tracks LogMiner dictionary archiving |
| Broker default | Value of the ` LOG_ARCHIVE_TRACE` initialization parameter |
| Imported? | Yes, from the `LOG_ARCHIVE_TRACE` initialization parameter |
| Parameter class | Dynamic |
| Role | Primary, standby, far sync instance |
| Standby type | Physical, logical, or snapshot standby, or a far sync instance |
| Corresponds to | `LOG_ARCHIVE_TRACE` initialization parameter |
| Scope | Instance (On an Oracle RAC database, you can use the `EDIT INSTANCE * ON DATABASE ` command to have all instances use the same value for this property.) |
| Cloud Control name | `Log Archive Trace` |

#### 8.3.18 LogFileNameConvert

The `LogFileNameConvert` configurable property converts the filename of an online redo log file on the primary database to the filename of a corresponding online redo log file on the physical standby database.

Note:

When a database is added to the configuration, the broker sets the initial value of this property to the in-memory value of the `LOG_FILE_NAME_CONVERT` initialization parameter. It is possible that the in-memory value and server parameter file (SPFILE) value of this parameter will differ. If you want to use the parameter's in-memory value, then enable the database and the broker will ensure that the SPFILE value of the parameter is set to the in-memory value. If you want to use the SPFILE value, then set the property value to be the parameter's value stored in the SPFILE. Then enable the database.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | Set the value of this property to a list of an even number of string pairs, separated by commas.  1. The first string is the substring found in the datafile names on the primary database. 2. The second string is the substring found in the datafile names on the standby database.  For example, `('string1', 'string2', 'string3', 'string4',...)`  Where:  - `string1` is the substring of the primary database filename. - `string2` is the substring of the standby database filename. - `string3` is the substring of the primary database filename. - `string4` is the substring of the standby database filename. |
| Broker default | Value of the `LOG_FILE_NAME_CONVERT` initialization parameter |
| Imported? | Yes, from the `LOG_FILE_NAME_CONVERT` initialization parameter |
| Parameter class | Static |
| Role | Standby |
| Standby type | Physical database and far sync instance |
| Corresponds to | `LOG_FILE_NAME_CONVERT` initialization parameter |
| Scope | Database |
| Cloud Control name | `Log File Name Convert` |

#### 8.3.19 LogShipping

The broker uses the value of the `LogShipping` property when the primary database is in the `TRANSPORT-ON` state or when the physical standby or far sync instance forwards redo data to another member.

The other member can be a physical, logical, or snapshot standby, or a far sync instance.

- If the primary database is in the `TRANSPORT-ON` state and the value of the `LogShipping` property is `ON`, then redo transport services are enabled to send redo data to the particular configuration member. If the `LogShipping` property is `OFF`, then redo transport services are disabled to that member.
- If a configuration member that forwards redo data has its `LogShipping` property set to `ON` and the member to which it sends redo data also has its `LogShipping` property set to `ON`, then redo transport services are enabled from the member sending redo data to the member that is to receive redo data.
	If a member that forwards redo data has its `LogShipping` property set to `ON` but the member to which it sends redo data has its `LogShipping` property set to `OFF`, then redo transport services are disabled from the member sending redo data to the member that is to receive redo data.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | `ON` or `OFF` |
| Broker default | `ON` |
| Imported? | No |
| Parameter class | Dynamic |
| Role | Standby database, Recovery Appliance, far sync instance <sup>Foot 4</sup> |
| Standby type | Physical, logical, or snapshot standby, far sync instance, Recovery Appliance |
| Corresponds to | `ENABLE` and `DEFER` values for the `LOG_ARCHIVE_DEST_STATE_` n initialization parameter of the database or far sync instance that is sending redo data |
| Scope | Database, Recovery Appliance |
| Cloud Control name | `Log Shipping` |

<sup>Footnote 4</sup>

Although this property is set for a standby database or far sync instance, it is indirectly related to the redo transport services for the database or far sync instance that is sending redo data. The broker propagates the setting you specify on the standby database to the corresponding attributes of the `LOG_ARCHIVE_DEST_` `n` value of the database or far sync instance that is sending redo data.

#### 8.3.20 LogXptMode

The `LogXptMode` configurable property enables you to set the redo transport service.

You set the redo transport services on each configuration member to one of the following modes:

- `SYNC`
	Configures redo transport services for this configuration member using the `SYNC` and `AFFIRM` attributes of the `LOG_ARCHIVE_DEST_` `n` initialization parameter. Standby redo log files are required. This mode is required for the maximum protection or maximum availability data protection modes. This redo transport service enables the highest grade of data protection to the primary database, but also incurs the highest performance impact.
- `ASYNC`
	Configures redo transport services for this configuration member using the `ASYNC` and `NOAFFIRM` attributes of the `LOG_ARCHIVE_DEST_` `n` initialization parameter. Standby redo log files are required. This mode enables a moderate grade of data protection to the primary database, and incurs a lower performance impact than `SYNC`.
- `FASTSYNC`
	Configures redo transport services for this configuration member using the `SYNC` and `NOAFFIRM` attributes of the `LOG_ARCHIVE_DEST_` `n` initialization parameter. This mode is only available in maximum availability protection mode. Because `FASTSYNC` transport mode uses the `NOAFFIRM` attribute of the `LOG_ARCHIVE_DEST_n` parameter, data loss is possible.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | `SYNC`, `ASYNC`, or `FASTSYNC` |
| Broker default | `ASYNC` |
| Imported? | No |
| Parameter class | Dynamic |
| Role | Standby database, Recovery Appliance, far sync instance <sup>Foot 5</sup> |
| Standby type | Physical, logical, or snapshot standby, far sync instance, Recovery Appliance |
| Corresponds to | - `SYNC`, `ASYNC`, `AFFIRM`, and `NOAFFIRM` attributes for the `LOG_ARCHIVE_DEST_` `n` initialization parameter of the database or far sync instance that is sending redo data - `ARCHIVER`, `TRANSMIT_MODE`, and `AFFIRM` columns of `V$ARCHIVE_DEST` view of the database or far sync instance that is sendng redo data |
| Scope | Database, far sync instance, Recovery Appliance |
| Cloud Control name | `Redo Transport Service` |

<sup>Footnote 5</sup>

Although this property is set for the standby database or far sync instance, it is indirectly related to the redo transport services for the database or far sync instance that is sending redo. The broker propagates the setting you specify on the standby database or far sync instance to the corresponding attributes of the `LOG_ARCHIVE_DEST_` `n` value of the database or far sync instance that is sending redo data. Note that if a database receives redo from a database or far sync instance where the `RedoRoutes` property has been configured with a redo transport mode, then the mode specified by that `RedoRoutes` property value overrides the value of the `LogXptMode` property.

See Also:

[Managing the Members of a Broker Configuration](managing-oracle-data-guard-broker-configuration-members.md) for more information about setting data protection modes for redo transport services

#### 8.3.21 LsbyMaxEventsRecorded

The `LsbyMaxEventsRecorded` configurable property specifies the number of events that will be stored in the `DBA_LOGSTDBY_EVENTS` table, which stores logical standby event information.

| Category | Description |
| --- | --- |
| Datatype | Integer |
| Valid values | \>=0 |
| Broker default | Value of the `MAX_EVENTS_RECORDED` row of `SYSTEM.LOGSTDBY$PARAMETERS` |
| Imported? | Yes, from the `MAX_EVENTS_RECORDED` row of `SYSTEM.LOGSTDBY$PARAMETERS` |
| Parameter class | Dynamic; SQL Apply does not require restart |
| Role | Standby |
| Standby type | Logical |
| Corresponds to | `DBMS_LOGSTDBY.APPLY_SET('MAX_EVENTS_RECORDED')` and the `DBMS_LOGSTDBY.APPLY_UNSET('MAX_EVENTS_RECORDED')` procedures |
| Scope | Database |
| Cloud Control name | `Max Events Recorded` |

#### 8.3.22 LsbyMaxServers

The `LsbyMaxServers` configurable instance-specific property specifies the number of parallel query servers specifically reserved for SQL Apply.

If the value is 0, then SQL Apply uses all available parallel query servers to read the log files and apply changes.

| Category | Description |
| --- | --- |
| Datatype | Integer |
| Valid values | \>=0 |
| Broker default | Value of the `MAX_SERVERS` row of `SYSTEM.LOGSTDBY$PARAMETERS` |
| Imported? | Yes, from the `MAX_SERVERS` row of `SYSTEM.LOGSTDBY$PARAMETERS` |
| Parameter class | Dynamic; SQL Apply does not require restart |
| Role | Standby |
| Standby type | Logical |
| Corresponds to | `DBMS_LOGSTDBY.APPLY_SET('MAX_SERVERS')` and the `DBMS_LOGSTDBY.APPLY_UNSET('MAX_SERVERS')` procedures |
| Scope | Instance (On an Oracle RAC database, you can use the `EDIT INSTANCE * ON DATABASE ` command to have all instances use the same value for this property.) |
| Cloud Control name | `Max Servers` |

#### 8.3.23 LsbyMaxSga

The `LsbyMaxSga` configurable instance-specific property specifies the number of megabytes for the allocation of SQL Apply cache in the system global area (SGA).

If the value is 0, SQL Apply uses one quarter of the value set for the `SHARED_POOL_SIZE` initialization parameter.

| Category | Description |
| --- | --- |
| Datatype | Integer |
| Valid values | \>=0 |
| Broker default | Value of the `MAX_SGA` row of `SYSTEM.LOGSTDBY$PARAMETERS` |
| Imported? | Yes, from the `MAX_SGA` row of `SYSTEM.LOGSTDBY$PARAMETERS` |
| Parameter class | Dynamic; SQL Apply does not require restart |
| Role | Standby |
| Standby type | Logical |
| Corresponds to | `DBMS_LOGSTDBY.APPLY_SET('MAX_SGA')` and the `DBMS_LOGSTDBY.APPLY_UNSET('MAX_SGA')` procedures |
| Scope | Instance (On an Oracle RAC database, you can use the `EDIT INSTANCE * ON DATABASE ` command to have all instances use the same value for this property.) |
| Cloud Control name | `Max SGA (MB)` |

#### 8.3.24 LsbyPreserveCommitOrder

The `LsbyPreserveCommitOrder` configurable property controls whether transactions are committed on the logical standby database in the exact same order in which they were committed on the primary database.

Specify one of the following values:

- `TRUE`: Transactions are applied to the logical standby database in the exact order in which they were committed on the primary database.
- `FALSE`: Transactions containing non-overlapping sets of rows may be committed in a different order than they were committed on the primary database.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | `TRUE` or `FALSE` |
| Broker default | Value of the `PRESERVE_COMMIT_ORDER` row of SYSTEM.LOGSTDBY$PARAMETERS |
| Imported? | Yes, from the `PRESERVE_COMMIT_ORDER` row of `` `SYSTEM.LOGSTDBY$PARAMETERS` `` |
| Parameter class | Static; SQL Apply requires restart |
| Role | Standby |
| Standby type | Logical |
| Corresponds to | `DBMS_LOGSTDBY.APPLY_SET('PRESERVE_COMMIT_ORDER')` and `DBMS_LOGSTDBY.APPLY_UNSET('PRESERVE_COMMIT_ORDER')` procedures |
| Scope | Database |
| Cloud Control name | `Preserve Commit Order` |

#### 8.3.25 LsbyRecordAppliedDdl

The `LsbyRecordAppliedDdl` configurable property controls whether or not SQL statements that were applied to the logical standby database are recorded in the `DBA_LOGSTDBY_EVENTS` table.

Specify one of the following values:

- `TRUE`: DDL statements applied to the logical standby database are recorded in the `DBA_LOGSTDBY_EVENTS` table. This is the default setting.
- `FALSE`: Applied DDL statements are not recorded.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | `TRUE` or `FALSE` |
| Broker default | Value of the `RECORD_APPLIED_DDL` row of `SYSTEM.LOGSTDBY$PARAMETERS` |
| Imported? | Yes, from the `RECORD_APPLIED_DDL` row of `SYSTEM.LOGSTDBY$PARAMETERS` |
| Parameter class | Dynamic; SQL Apply does not require restart |
| Role | Standby |
| Standby type | Logical |
| Corresponds to | `DBMS_LOGSTDBY.APPLY_SET('RECORD_APPLIED_DDL')` and the `DBMS_LOGSTDBY.APPLY_UNSET('RECORD_APPLIED_DDL')` procedures |
| Scope | Database |
| Cloud Control name | `Record Applied DDL` |

#### 8.3.26 LsbyRecordSkipDdl

The `LsbyRecordSkipDdl` configurable property controls whether or not skipped DDL statements are recorded in the `DBA_LOGSTDBY_EVENTS` table.

Specify one of the following values:

- `TRUE`: Skipped DDL statements are recorded in the `DBA_LOGSTDBY_EVENTS` table. This is the default setting.
- `FALSE`: Skipped DDL statements are not recorded in the `DBA_LOGSTDBY_EVENTS` table.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | `TRUE` or `FALSE` |
| Broker default | Value of the `RECORD_SKIP_DDL` row of `SYSTEM.LOGSTDBY$PARAMETERS` |
| Imported? | Yes, from the `RECORD_SKIP_DDL` row of `SYSTEM.LOGSTDBY$PARAMETERS` |
| Parameter class | Dynamic; SQL Apply does not require restart |
| Role | Standby |
| Standby type | Logical |
| Corresponds to | `DBMS_LOGSTDBY.APPLY_SET('RECORD_SKIP_DDL')` and the `DBMS_LOGSTDBY.APPLY_UNSET('RECORD_SKIP_DDL')` procedures |
| Scope | Database |
| Cloud Control name | `Record Skip DDL` |

#### 8.3.27 LsbyRecordSkipErrors

The `LsbyRecordSkipErrors` configurable property controls whether or not skipped errors (as described by the `DBMS_LOGSTDBY.SKIP_ERROR` procedure) are recorded in the `DBA_LOGSTDBY_EVENTS` table.

Specify one of the following values:

- `TRUE`: Skipped errors are recorded in the `DBA_LOGSTDBY_EVENTS` table.
- `FALSE`: Skipped errors are not recorded in the `DBA_LOGSTDBY_EVENTS` table.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | `TRUE` or `FALSE` |
| Broker default | Value of the `RECORD_SKIP_ERRORS` row of `SYSTEM.LOGSTDBY$PARAMETERS` |
| Imported? | Yes, from the `RECORD_SKIP_ERRORS` row of `SYSTEM.LOGSTDBY$PARAMETERS` |
| Parameter class | Dynamic; SQL Apply does not require restart |
| Role | Standby |
| Standby type | Logical |
| Corresponds to | `DBMS_LOGSTDBY.APPLY_SET('RECORD_SKIP_ERRORS')` and the `DBMS_LOGSTDBY.APPLY_UNSET('RECORD_SKIP_ERRORS')` procedures |
| Scope | Database |
| Cloud Control name | `Record Skip Errors` |

#### 8.3.28 MaxConnections

The `MaxConnections` configurable property specifies how many ARCn processes will be used in parallel to transmit redo data from a single archived redo log on the database or far sync instance to the archived redo log at the remote site.

If the `MaxConnections` property is set to a value greater than 1, then redo transport services use multiple ARCn processes to transmit redo data to archived redo log files at the remote destinations.

| Category | Description |
| --- | --- |
| Datatype | Integer |
| Valid values | 1 to 20 |
| Broker default | 1 |
| Imported? | No |
| Parameter class | Dynamic |
| Role | Standby, Recovery Appliance |
| Standby type | Physical, logical, snapshot, Recovery Appliance |
| Corresponds to | - `LOG_ARCHIVE_MAX_PROCESSES` initialization parameter <sup>Foot 6</sup> - `MAX_CONNECTIONS` attribute for the `LOG_ARCHIVE_DEST_` `n` initialization parameter of the database or far sync instance that is sending redo data - `MAX_CONNECTIONS` column of the `V$ARCHIVE_DEST` view of the database or far sync instance that is sending redo data |
| Scope | Database, Recovery Appliance |
| Cloud Control name | Not applicable |

<sup>Footnote 6</sup>

The `LOG_ARCHIVE_MAX_PROCESSES` initialization parameter affects the actual number of ARCn processes used by an instance.

#### 8.3.29 MaxFailure

The `MaxFailure` configurable property specifies the maximum number of contiguous archiving failures before the redo transport services stop trying to transport archived redo log files to the standby database.

A value of zero indicates that an unlimited number of failures are allowed.

| Category | Description |
| --- | --- |
| Datatype | Integer |
| Valid values | \>=0 |
| Broker default | If the standby database is part of a group as specified with the broker `RedoRoutes` property, then the default value 1. Otherwise, the default value is 0. |
| Imported? | No |
| Parameter class | Dynamic |
| Role | Standby <sup>Foot 7</sup>, Recovery Appliance |
| Standby type | Physical, logical, snapshot, Recovery Appliance |
| Corresponds to | - `MAX_FAILURE` attribute for the `LOG_ARCHIVE_DEST_` n initialization parameter of the database or far sync instance that is sending redo data - `MAX_FAILURE` column of the `V$ARCHIVE_DEST` view of the database or far sync instance that is sending redo data |
| Scope | Database, Recovery Appliance |
| Cloud Control name | Not applicable |

<sup>Footnote 7</sup>

Although this property is set for a standby database or far sync instance, it is indirectly related to the redo transport services for the database or far sync instance that is sending redo data. The broker propagates the setting you specify on the standby database or far sync instance to the corresponding attributes of the `LOG_ARCHIVE_DEST_` n value of the database or far sync instance that is sending redo data.

#### 8.3.30 NetTimeout

The `NetTimeout` configurable property specifies the number of seconds the LGWR waits for Oracle Net Services to respond to a LGWR request.

It is used to bypass the long connection timeout in TCP.

| Category | Description |
| --- | --- |
| Datatype | Integer |
| Valid values | 0, 15 to 1200 |
| Broker default | 30 |
| Imported? | No |
| Parameter class | Dynamic |
| Role | Primary, standby, far sync instance, Recovery Appliance |
| Standby type | Physical, logical, or snapshot standby, far sync instance, Recovery Appliance |
| Corresponds to | - `NET_TIMEOUT` attribute of the `LOG_ARCHIVE_DEST_` `n` initialization parameter of the database or far sync instance that is sending redo data - `NET_TIMEOUT` column of `V$ARCHIVE_DEST` view of the database or far sync instance that is sending redo data |
| Scope | Database, far sync instance, Recovery Appliance |
| Cloud Control name | Not applicable |

#### 8.3.31 ObserverConnectIdentifier

The `ObserverConnectIdentifier` configurable property specifies a connect identifier that can be used by the observer to connect to this database.

The connect identifier can pertain only to the primary database, or to the target standby database when fast-start failover is enabled.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid Values | A connect identifier that observer can use to connect to this database |
| Broker Default | Empty String <sup>Foot 8</sup> |
| Imported? | No |
| Parameter Class | Not applicable |
| Role | Primary and Standby |
| Standby Type | Physical or logical |
| Corresponds to | Not applicable |
| Scope | Database |
| Cloud Control name | `Observer Connect Identifier` |

<sup>Footnote 8</sup>

When this is Empty String (not set by the user), the connect identifier specified by this database's DGConnectIdentifier property will be used by the observer.

#### 8.3.32 PreferredApplyInstance

The `PreferredApplyInstance` configurable property indicates that a particular instance is the preferred choice for serving log apply services.

It is only used when the database is a standby Oracle RAC database. The value could be an empty string (default) which means the broker chooses the apply instance.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid Values | The instance name (SID) or empty string. Note that on certain platforms, SIDs may be case-sensitive. |
| Broker Default | Empty string |
| Imported? | No |
| Parameter Class | Not applicable |
| Role | Standby, Recovery Appliance |
| Standby Type | Physical, logical, Recovery Appliance |
| Corresponds to | Not applicable |
| Scope | Database, Recovery Appliance |
| Cloud Control name | `Apply Instance` |

See Also:

- [Oracle Database Administrator's Guide](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/dgbkr&id=ADMIN11074) for more information about SIDs
- [Apply Services in an Oracle RAC Database Environment](managing-oracle-data-guard-broker-configuration-members.md) for information about apply services in an Oracle RAC environment

#### 8.3.33 PreferredObserverHosts

The `PreferredObserverHosts` configurable property allows you to list the hosts that you would prefer as hosts for the master observer when that database is in the primary role.

The value of this property can be changed at any time, regardless of whether Fast-Start Failover is enabled or not, or whether the observer is in an OBSERVED state. However, the change does not affect the location of the master observer until the next role change.

If this property is set, then after a role change the broker takes the following steps:

1. Checks whether the current master observer is running on a host in the list specified by the `PreferredObserverHosts` property of the new primary. If yes, stop here; otherwise, go to step 2.
2. Scans the list from the beginning to look for a host where one observer is running, and connects to the primary and target standby databases. If found, go to step 3; otherwise, stop here.
3. Attempts to switch the master observer to the host found in step 2. If switching fails, no other hosts are tried.

| Category | Description |
| --- | --- |
| Data type | String |
| Valid value | A character string that contains one or more host names, separated by comma: ``` host_name_1 [,host_name_n] ```  Each host name can be any character string for a valid network name, even if there is no observer running on this host when it is set. |
| Broker default | Null |
| Imported? | No |
| Parameter class | Not applicable |
| Role | Primary, standby |
| Standby type | Physical standby and logical standby |
| Corresponds to | Not applicable |
| Scope | Database |
| Cloud Control name | Not applicable |

#### 8.3.34 RedoCompression

The `RedoCompression` configurable property is used to specify whether redo data is transmitted to a standby database or far sync instance in compressed or uncompressed form.

Note:

Redo transport compression is a feature of the Oracle Advanced Compression option. You must purchase a license for this option before using the redo transport compression feature.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid value | `DISABLE`,`ENABLE`, `ZLIB`, or `LZO` - When `ENABLE` is specified, the default compression algorithm is `ZLIB`. - `LZO` is not supported when `LogXptMode` is set to `SYNC` or `FASTSYNC`. |
| Broker Default | `DISABLE` |
| Imported? | No |
| Parameter class | Dynamic |
| Role | Standby database, far sync instance <sup>Foot 9</sup>, Recovery Appliance |
| Standby type | Physical, logical, or snapshot standby, far sync instance, Recovery Appliance |
| Corresponds to | - `COMPRESSION` attribute for the `LOG_ARCHIVE_DEST_` n initialization parameter of the database or far sync instance that is sending redo data - `COMPRESSION` column of the `V$ARCHIVE_DEST` view of the database or far sync instance that is sending redo data |
| Scope | Database, far sync instance, Recovery Appliance |
| Cloud Control name | Not applicable |

<sup>Footnote 9</sup>

Although this property is set for a standby database or far sync instance, it is indirectly related to the redo transport services for the database or far sync instance that is sending redo data. The broker propagates the setting you specify on the standby database or far sync instance to the corresponding attributes of the `LOG_ARCHIVE_DEST_` `n` value of the database or far sync instance that is sending redo data.

#### 8.3.35 RedoRoutes

The `RedoRoutes` property lets you override the default behavior by which a primary database sends the redo that it generates to every other redo transport destination in the configuration.

You can use the `RedoRoutes` property to create a more complex redo transport topology, such as one in which a physical standby database or a far sync instance forwards redo received from the primary database to one or more destinations, or one in which the redo transport mode used for a given destination is dependent on which database is in the primary role.

The `RedoRoutes` property is set to a character string that contains one or more redo routing rules. Each rule contains one or more redo sources and one or more redo destinations. A redo routing rule becomes active when one of the redo sources in the rule is in the primary role. This results in redo from the primary database being sent to every redo destination in that rule.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | A character string that contains one or more redo routing rules, each contained within a pair of parentheses:  ``` (redo_routing_rule_1) [(redo_routing_rule_n)] ```  See " Redo Routing Rules " for more information about redo routing rules. |
| Broker default | Null |
| Imported? | No |
| Parameter class | Not applicable |
| Role | Primary, standby, far sync instance |
| Standby type | Physical standby and far sync instance |
| Corresponds to | `LOG_ARCHIVE_DEST_` `n` |
| Scope | Database, far sync instance |
| Cloud Control Name | RedoRoutes |

##### 8.3.35.1 Redo Routing Rules

The `RedoRoutes` property is set to a character string that contains one or more redo routing rules.

Each rule is contained within a set of parentheses, as follows:

```
(redo_routing_rule_1) [(redo_routing_rule_n)]
```

A redo routing rule contains a redo source field and a redo destination field separated by a colon:

```
(redo source : redo destination)
```

The redo source field must contain the keyword `LOCAL` or `ANY`, or a comma-separated list of `DB_UNIQUE_NAME` values, as follows:

```
{LOCAL | ANY | db_unique_name_1,[,db_unique_name_n]}
```
- The `LOCAL` keyword is an alias for the local database name. This keyword cannot be used at a far sync instance.
- The `ANY` keyword is an alias for any database in the configuration.
- A database cannot be specified as a redo source in more than one redo routing rule defined at a given database, either explicitly or implicitly through use of the `LOCAL` keyword.

The redo destination field must contain the keyword `ALL` or a comma-separated list of redo destination groups, each of which consists of destination databases with optional priority attributes and optional redo transport mode attributes:

```
{ALL [xpt_mode] | redo_dest_group_1 [, redo_dest_group_n]}
```
- The `ALL` keyword is an alias for all possible destinations in the configuration.
- The `redo_dest_group_n` is:
	```
	{ db_unique_name_1 [xpt_mode] | ( db_unique_name_1 [xpt_mode] [PRIORITY=n] [,db_unique_name_n [xpt_mode] [PRIORITY=n]] ) }
	```
	The optional `xpt_mode` specifies the redo transport mode to be used to send redo to the associated destination. It can have one of three values: `ASYNC`, `SYNC`, or `FASTSYNC`. If the redo transport attribute is not specified, then the transport mode used will be the one specified by the `LogXptMode` property for the redo destination.
	The optional \[`PRIORITY=` n\] can have n =1 ~ 8. It is important to understand how different group and priority settings affect redo transport under various conditions. The following examples describe some sample situations.

Example 1: Different Priorities Within a Group

Assume there are three members in a broker configuration:
- `PRI` (primary database)
- `SB1` (standby database)
- `FS1` (far sync instance)

The primary database `PRI` generates the redo log for use by the standby database `SB1`. Because there is a far sync instance, `FS1`, there are two possible redo delivery paths to the standby database:
- (path 1) `PRI` —> `FS1` —> `SB1`
- (path 2) `PRI` —> `SB1`

Assume (path 1) is more desirable than (path 2). This can be expressed with the `RedoRoutes` property as follows:
- `PRI` — `RedoRoutes = (local :  ( FS1 PRIORITY=1, SB1 PRIORITY=2 ) )`
- `FS1` — `RedoRoutes = ( PRI : SB1 )`

As specified in the `PRI` `RedoRoutes` property, the primary (`PRI`) has two destinations: one for `FS1` with `PRIORITY=1` and one for `SB1` with `PRIORITY=2`. Smaller priority numbers mean higher priority, so primary `PRI` tries to ship the redo log to `FS1` first.

If `FS1` is available, then the primary ships to `FS1` which has `PRIORITY=1`. If `FS1` is unavailable, then the primary ships to `SB1` which has `PRIORITY=2`. When `FS1` becomes active again, the primary will ship to it again because priority 1 is higher than priority 2.

Example 2: The Same Priorities Within a Group

Suppose you add one more far sync instance, `FS2`, to the configuration set up in Example 1, and then update the `RedoRoutes` property as follows:
- `PRI` — `RedoRoutes = (local :  ( FS1 PRIORITY=1, FS2 PRIORITY=1 ) )`
- `FS1` — `RedoRoutes = ( PRI : SB1 )`
- `FS2` — `RedoRoutes = ( PRI : SB1 )`

The primary `PRI` now has two destinations, `FS1` and `FS2`, with the same priority. The primary must choose either `FS1` or `FS2`. Assume the primary chooses `FS1`.

If `FS1` is available, then the primary ships to `FS1`. If `FS1` is unavailable, then the primary ships to `FS2`. Even after `FS1` becomes active again, the primary continues shipping to `FS2` because `FS1` and `FS2` have the same priority. If `FS2` fails, then the primary ships to `FS1`.

Example 3: Multiple Groups

Assume that you add one more standby, `SB2`, to the configuration, and then update the `RedoRoutes` property as follows so that the primary has two destination groups:
- `PRI` — `RedoRoutes = (local :  ( FS1 PRIORITY=1, SB1 PRIORITY=2 ), ( FS2 PRIORITY=1, SB2 PRIORITY=2 ) )`
- `FS1` — `RedoRoutes = ( PRI : SB1 )`
- `FS2` — `RedoRoutes = ( PRI : SB2 )`

The general rule is that there is one active redo path for each group. (See Example 4 for a scenario in which there are multiple active redo paths.) The primary establishes one redo delivery path for the first group ( `FS1 PRIORITY=1`, `SB1 PRIORITY=2` ), and establishes another redo delivery path for the second group (` FS2 PRIORITY=1`, `SB2 PRIORITY=2` ).

- If both `FS1` and `FS2` are available, then the primary ships to `FS1` and `FS2`.
- If `FS1` is unavailable and `FS2` is available, then the primary ships to `SB1` and `FS2`.
- If `FS1` is available and `FS2` is unavailable, then the primary ships to `FS1` and `SB2`.
- If both `FS1` and `FS2` are unavailable, then the primary ships to `SB1` and `SB2`.

Example 4: The PRIORITY Attribute is Set to 8

Setting `PRIORITY=8` has special meaning. If a primary ships redo to a destination with `PRIORITY=8`, then it must ship to every `PRIORITY=8` destination. Suppose you update the `RedoRoutes` property as follows so that the primary has one group containing three destinations:
- `PRI` — `RedoRoutes = (local :  ( FS1 PRIORITY=1, SB1 PRIORITY=8, SB2 PRIORITY=8 ) )`
- `FS1` — `RedoRoutes = ( PRI : SB1, SB2 )`

These settings result in the following behavior:

- If `FS1` is available, then the primary ships to `FS1`.
- If `FS1` is unavailable, then the primary ships to both `SB1` and `SB2` because they both have `PRIORITY=8`
- If `FS1` becomes active again, then the primary ships to `FS1`.

Usage Notes for Advanced Redo Transport Settings

The following usage notes apply regarding advanced redo transport settings:

- The `RedoRoutes` property has a default value of NULL, which is treated as `(LOCAL : ALL)` at a primary database.
- A redo routing rule is active if its redo source field specifies the current primary database. If a rule is active, primary database redo is sent by the database at which the rule is defined to each destination specified in the redo destination field of that rule.
- The `ASYNC` redo transport attribute must be explicitly specified for a cascaded destination to enable real-time cascading to that destination.
- The `RedoRoutes` property cannot be configured such that when a physical standby database is converted to a snapshot standby, the snapshot standby would send redo data to another member.
- The `RedoRoutes` property can be set for a logical standby database only if the redo source field is set to `LOCAL`.

#### 8.3.36 ReopenSecs

The `ReopenSecs` configurable property specifies the minimum number of seconds before the archiver process (ARCn, foreground, or log writer process) should try again to access a previously failed destination.

| Category | Description |
| --- | --- |
| Datatype | Integer |
| Valid values | \>=0 seconds |
| Broker default | `300` |
| Imported? | No |
| Parameter class | Dynamic |
| Role | Standby database, far sync instance <sup>Foot 10</sup>, Recovery Appliance |
| Standby type | Physical, logical, snapshot standby, far sync instance, Recovery Appliance |
| Corresponds to | - `REOPEN` attribute for the `LOG_ARCHIVE_DEST_` n initialization parameter of the database or far sync instance that is sending redo data - `REOPEN_SECS` column of the `V$ARCHIVE_DEST` view of the database or far sync instance that is sending redo data |
| Scope | Database, far sync instance, Recovery Appliance |
| Cloud Control name | Not applicable |

<sup>Footnote 10</sup>

Although this property is set for a standby database or far sync instance, it is indirectly related to the redo transport services for the database or far sync instance that is sending redo data. The broker propagates the setting you specify on the standby database or far sync instance to the corresponding attributes of the `LOG_ARCHIVE_DEST_` `n` value of the database or far sync instance that is sending redo data.

#### 8.3.37 SidName

The `SidName` configurable property specifies the Oracle System Identifier (SID) of the instance.

The property can only be updated when broker management of the database is disabled. You should only update the value when the SID is changed, in which case you need to disable broker management of the database, update the `SidName` property to match with the new SID, and reenable broker management of the database.

Note:

If no existing instance in the broker configuration, for the database whose name matches this instance's `db_unique_name`, has a `SidName` property with a value that matches this instance's actual `SID`, then the broker creates a new instance for this database that has this instance's `db_unique_name`.

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
| Cloud Control name | Not applicable |

See Also:

[Oracle Database Administrator's Guide](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/dgbkr&id=ADMIN11074) for more information about SIDs

#### 8.3.38 StandbyArchiveLocation

The `StandbyArchiveLocation` configurable property specifies the location of archived redo log files arriving from a redo source.

Oracle recommends that you always explicitly set the value.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | Nonempty file specification of the location of archived redo log files on the database or far sync instance. Specify `USE_DB_RECOVERY_FILE_DEST` if a database recovery area is desired. |
| Broker default | `dgsby_` db\_unique\_name |
| Imported? | Yes, from the `DESTINATION` column of the `V$ARCHIVE_DEST` fixed view of the standby database or far sync instance where the destination is a local destination and where the `VALID_FOR` attribute is compatible with the string `(STANDBY_ROLE, STANDBY_LOGFILE)`; if no such destination exists, import is from the `STANDBY_ARCHIVE_DEST` initialization parameter. Note that the `STANDBY_ARCHIVE_DEST` parameter has been deprecated and is supported for backward compatibility only. |
| Parameter class | Dynamic |
| Role | Standby database or far sync instance |
| Standby type | Physical, logical, or snapshot standby, or a far sync instance |
| Corresponds to | - `LOCATION` attribute of the `LOG_ARCHIVE_DEST_` n initialization parameter of the standby database or far sync instance with `VALID_FOR` compatible with `(STANDBY_ROLE, STANDBY_LOGFILE)` - `DESTINATION` column of the `V$ARCHIVE_DEST` view of the standby database |
| Scope | Instance |
| Cloud Control name | `Standby Archive Location` |

Note:

On a logical standby database, Oracle recommends the `LOCATION` attribute of the `LOG_ARCHIVE_DEST_` n initialization parameter for the local destination be different from the value of `StandbyArchiveLocation` property, unless you are using a database recovery area.

#### 8.3.39 StandbyFileManagement

The `StandbyFileManagement` configurable property affects how the add datafile operation on the primary database is applied on the standby database.

If this property is set to `AUTO`, in conjunction with valid settings in the `DbFileNameConvert` configurable property, a corresponding new datafile is automatically created on the standby database. The location of this new standby datafile is determined by the value of the `DbFileNameConvert` property.

If this property is set to `MANUAL`, you have to create the correct new datafile on the standby database manually.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | `AUTO` or `MANUAL` |
| Broker default | `AUTO` |
| Imported? | Yes, from the `STANDBY_FILE_MANAGEMENT` initialization parameter |
| Parameter class | Dynamic |
| Role | Standby |
| Standby type | Physical or snapshot |
| Corresponds to | `STANDBY_FILE_MANAGEMENT` initialization parameter |
| Scope | Database |
| Cloud Control name | Not applicable |

#### 8.3.40 StaticConnectIdentifier

The `StaticConnectIdentifier` configurable instance-specific property specifies the connection identifier that the DGMGRL client will use when starting database instances.

If this property has a null value, then the `DGConnectIdentifier` value is used for operations that involve shutting down and starting up the instance.

| Category | Description |
| --- | --- |
| Datatype | String |
| Valid values | A connect identifier that refers to a service that is statically registered. |
| Broker default | Connect descriptor that is the concatenation of:<sup>Foot 11</sup>  - The `ADDRESS` attribute value of the listener that is specified for the `LOCAL_LISTENER` initialization parameter - The value for the `SERVICE_NAME` attribute will be set to a concatenation of `db_unique_name_DGMGRL.db_domain` |
| Imported? | Yes, from the `LOCAL_LISTENER` and `DB_UNIQUE_NAME` initialization parameters. |
| Parameter class | Not applicable |
| Role | Primary and standby |
| Standby type | Physical, logical, or snapshot |
| Corresponds to | Not applicable |
| Scope | Instance |
| Cloud Control name | Not applicable |

<sup>Footnote 11</sup>

If the instance specified by the `SidName` property is started on a different host (read from the `HOST_NAME` column of the `V$INSTANCE` view) than the host on which it had been previously started, the broker automatically updates the default value of the `StaticConnectIdentifier` property to incorporate the current `ADDRESS` attribute of the listener that is specified for the `LOCAL_LISTENER` initialization parameter.

See Also:

- See [Oracle Database Net Services Administrator's Guide](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/dgbkr&id=NETAG1589) for more information about statically registered services
- See the My Oracle Support Note 1387859.1 at [`http://support.oracle.com`](http://support.oracle.com/) for additional information about using static services and the `StaticConnectIdentifier` configurable property

#### 8.3.41 TransportDisconnectedThreshold

The `TransportDisconnectedThreshold` configurable property can be used to generate a warning status for a logical, physical, or snapshot standby, or a far sync instance when the last communication from the primary database exceeds the property value.

The property value is expressed in seconds. A value of 0 seconds results in no warnings being generated.

| Category | Description |
| --- | --- |
| Datatype | Number |
| Valid values | \>=0 |
| Broker default | 30 seconds |
| Imported? | No |
| Parameter class | Not applicable |
| Role | Standby database, far sync instance |
| Standby type | Physical, logical, or snapshot standby, or a far sync instance |
| Corresponds to | Not applicable |
| Scope | Database, far sync instance |
| Cloud Control name | Not applicable |

#### 8.3.42 TransportLagThreshold

The `TransportLagThreshold` configurable property can be used to generate a warning status for a logical, physical, or snapshot standby, or a far sync instance when the member's transport lag exceeds the property value.

The property value is expressed in seconds. A value of 0 seconds results in no warnings being generated when a transport lag exists.

| Category | Description |
| --- | --- |
| Datatype | Number |
| Valid values | \>=0 |
| Broker default | 30 seconds |
| Imported? | No |
| Parameter class | Not applicable |
| Role | Standby database, far sync instance |
| Standby type | Physical, logical, or snapshot standby, or a far sync instance |
| Corresponds to | Not applicable |
| Scope | Database, far sync instance |
| Cloud Control name | Not applicable |