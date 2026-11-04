---
title: Managing Databases
book: Data Guard Broker
doc_id: E40771-07
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40771/dbresource.htm
tags:
  - oracle
  - 11g
  - data-guard-broker
---

## 4 Managing Databases

This chapter describes managing the states and properties that pertain to the database. It contains the following topics:

## 4.1 Database Objects

The broker manages database objects. A database object corresponds to a primary or standby database. The broker uses each object's profile to manage and monitor the state of a single database.

The broker distinguishes between physical, snapshot, and logical standby databases. These databases are configured with profiles having states and properties that are appropriate for their standby types.

## 4.2 Database States

When a configuration is enabled, its databases can be in one of several states that direct the behavior of Data Guard, for example transmitting redo data or applying redo data. Table 4-1 describes the various database states.

Snapshot standby databases are not listed in this table because they do not have states; they only receive redo data.

Table 4-1 Database States and Descriptions

| Database Role | State Name | Description |
| --- | --- | --- |
| Primary | `TRANSPORT-ON` | Redo transport services are set up to transmit redo data to the standby databases when the primary database is open for read/write access.  If this is an Oracle RAC database, all instances open in read/write mode will have redo transport services running.  This is the default state for a primary database when it is enabled for the first time. |
| Primary | `TRANSPORT-OFF` | Redo transport services are stopped on the primary database.  If this is an Oracle RAC database, redo transport services are not running on any instances. |
| Physical standby | `APPLY-ON` | Redo Apply is started on a physical standby database.  If the standby database is an Oracle RAC database, the broker starts Redo Apply on exactly one standby instance, called the apply instance. If this instance fails, the broker automatically chooses another instance that is either mounted or open read-only. This new instance then becomes the apply instance.  This is the default state for a physical standby database when it is enabled for the first time.  If a license for the Oracle Active Data Guard option has been purchased, a physical standby database can be open while Redo Apply is active. This capability is known as real-time query. See [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/manage_ps.htm#SBYDB00706) for more details. |
| Physical standby | `APPLY-OFF` | Redo Apply is stopped.  If this is an Oracle RAC database, there is no instance running Apply Services until you change the database state to `APPLY-ON`. |
| Logical standby | `APPLY-ON` | SQL Apply is started on the logical standby database when it is opened and the logical standby database guard is on.  If this is an Oracle RAC database, SQL Apply is running on one instance, the apply instance. If this instance fails, the broker automatically chooses another open instance. This new instance becomes the apply instance.  This is the default state for a logical standby database when it is enabled for the first time. |
| Logical standby | `APPLY-OFF` | SQL Apply is stopped. The logical standby database guard is on.  If this is an Oracle RAC database, there is no instance running SQL Apply until you change the state to `APPLY-ON`. |

### 4.2.1 Database State Transitions

You can use the DGMGRL `EDIT DATABASE` command to explicitly change the state of a database. For example, the `EDIT DATABASE` command in the following example changes the state of the `North_Sales` database to `TRANSPORT-OFF`.

```
DGMGRL> EDIT DATABASE 'North_Sales' SET STATE='TRANSPORT-OFF';
Succeeded.
```

See Also:

[Chapter 7](dgmgrl.md) for complete information about the `EDIT DATABASE` command.

The following sections describe in more detail the possible state transitions for primary and standby databases.

Primary database state transitions

When transitioning the primary database to the `TRANSPORT-ON` state, the broker sets up redo transport services to all broker-managed standby databases using the redo transport-related properties of the standby databases (see Section 4.4 for the list of all redo transport-related properties). Redo transport services setup is done by setting the `LOG_ARCHIVE_DEST_` n and `LOG_ARCHIVE_DEST_STATE_` n initialization parameters on the primary database, and the `LOG_ARCHIVE_CONFIG` initialization parameter on all databases (primary or standby). If necessary, the broker also sets up the data protection mode of the database to match the protection mode recorded in the broker configuration file. Finally, if the database is open, the broker switches a log for each thread to initiate redo transport services.

When transitioning the primary database to the `TRANSPORT-OFF` state, the broker turns off redo transport services to all broker-managed standby databases by resetting the `LOG_ARCHIVE_DEST_STATE_` n initialization parameter. Transmission of redo data to all broker-managed standby databases is stopped. Log files continue to be archived at the primary database.

If the primary database is an Oracle RAC database, the broker configures redo transport services on all primary instances with the exact same settings.

See Also:

Section 4.4 for more details on managing redo transport services

Physical standby database state transitions

When transitioning a physical standby database to the APPLY-ON state, the broker starts Redo Apply with options specified by the Redo Apply-related properties (see Section 4.5 for the property list). If the standby database is an Oracle RAC database, the broker starts Redo Apply on one standby instance, called the apply instance.

If a license for the Oracle Active Data Guard option has been purchased, a physical standby database can be open while Redo Apply is active. This capability is known as real-time query. See [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/manage_ps.htm#SBYDB00706) for more details.

Note:

The apply instance must be open before starting Redo Apply if any other instance is open.

When transitioning to the APPLY-OFF state, the broker stops Redo Apply.

Note:

If you perform online database relocation with Oracle RAC One Node on a physical standby, then the new instance is started in the same mode as the currently running instance. Therefore, if the database is mounted on the original instance, then the database will be mounted on the new instance. Likewise, if the database is open on the original instance, then the database will be open on the new instance. This may result in the new instance starting in a mode that does not match the start option recorded with Oracle Clusterware for the database.

Snapshot standby database state transitions

A snapshot standby database does not have states. It only receives redo data.

Logical standby database state transitions

When transitioning a logical standby database to the `APPLY-ON` state, the broker will wait until the database is open, and then enable the database guard to prevent modifications to tables in the logical standby database, and start SQL Apply with options specified by the log apply-related properties. If the logical standby database is an Oracle RAC database, the broker starts SQL Apply on one standby instance, the apply instance.

When transitioning to the `APPLY-OFF` state, the broker stops SQL Apply.

See Also:

- Section 4.5 for information about managing SQL Apply
- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/toc.htm) for information about the database guard

## 4.3 Database Properties

There are two types of database properties: monitorable and configurable. Both monitorable and configurable properties can be further divided into properties having database-wide scope or instance-specific scope.

- Monitorable property values can be viewed only when the associated database object is enabled.
	Monitorable properties allow you to view run-time information related to database objects, but you cannot change the values of these properties.
- Configurable property values can be viewed and dynamically updated.
	Configurable properties affect the operation or configuration of the broker. You can change the value of these properties using DGMGRL or Enterprise Manager. You can edit properties if the configuration and its databases are enabled or disabled. However, if the database is disabled, the new property value will not take effect until you enable the configuration or database, as appropriate.
	See Also:
	[Chapter 8](dbpropref.md) for a detailed list of all database properties

To see these properties, you can use the DGMGRL `SHOW` command or Edit Properties page in Enterprise Manager. Example 4-1 uses the `SHOW DATABASE VERBOSE` command to display information about the `North_Sales` database.

Example 4-1 Using the SHOW DATABASE VERBOSE Command to Display Properties

```
DGMGRL> SHOW DATABASE VERBOSE 'North_Sales';
 
Database - North_Sales
 
  Role:            PRIMARY
  Intended State:  TRANSPORT-ON
  Instance(s):
    north_sales1
 
  Properties:
    DGConnectIdentifier             = 'North_Sales.example.com'
    ObserverConnectIdentifier       = ''
    LogXptMode                      = 'sync'
    DelayMins                       = '0'
    Binding                         = 'optional'
    MaxFailure                      = '0'
    MaxConnections                  = '1'
    ReopenSecs                      = '300'
    NetTimeout                      = '30'
    RedoCompression                 = 'DISABLE'
    LogShipping                     = 'ON'
    PreferredApplyInstance          = ''
    ApplyInstanceTimeout            = '0'
    ApplyParallel                   = 'AUTO'
    StandbyFileManagement           = 'AUTO'
    ArchiveLagTarget                = '0'
    LogArchiveMaxProcesses          = '5'
    LogArchiveMinSucceedDest        = '1'
    DbFileNameConvert               = 'dbs/bt, dbs/t'
    LogFileNameConvert              = 'dbs/bt, dbs/t'
    FastStartFailoverTarget         = 'South_Sales'
    InconsistentProperties          = '(monitor)'
    InconsistentLogXptProps         = '(monitor)'
    SendQEntries                    = '(monitor)'
    LogXptStatus                    = '(monitor)'
    RecvQEntries                    = '(monitor)'
    SidName                         = 'north_sales1'
    StaticConnectIdentifier         =
 '(DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST=North_Sales.example.com)
(PORT=2840))(CONNECT_DATA=(SERVICE_NAME=North_Sales_DGMGRL.example.com)
(INSTANCE_NAME=north_sales1)(SERVER=DEDICATED)))'
    StandbyArchiveLocation          = 'USE_DB_RECOVERY_FILE_DEST'
    AlternateLocation               = ''
    LogArchiveTrace                 = '255'
    LogArchiveFormat                = 'db1r_%d_%t_%s_%R.arc'
    LatestLog                       = '(monitor)'
    TopWaitEvents                   = '(monitor)'
 
Database Status:
SUCCESS
```

See Also:

[Chapter 7](dgmgrl.md) for complete information about the DGMGRL command-line interface

### 4.3.1 Monitorable (Read-Only) Properties

Monitorable database properties allow you to view information related to the database, but you cannot change the values of these properties. These properties can be very helpful when you are trying to diagnose problems in the broker configuration. For example, you can view the `InconsistentLogXptProps` monitorable database property to determine where there is a discrepancy in redo transport services properties between the broker configuration file and the actual value currently used by the database.

You can list all monitorable database properties using the DGMGRL `SHOW DATABASE VERBOSE` command. Use the `SHOW DATABASE` command to obtain more details about a particular property. For example, the following shows the `InconsistentLogXptProps` property:

```
DGMGRL> SHOW DATABASE 'North_Sales' 'InconsistentLogXptProps';

INCONSISTENT LOG TRANSPORT PROPERTIES

 INSTANCE_NAME     STANDBY_NAME  PROPERTY_NAME  MEMORY_VALUE  BROKER_VALUE 
  south_sales1      South_Sales     ReopenSecs           600           300
```

Enterprise Manager displays the information obtained from these properties on the Edit Properties page.

### 4.3.2 Configurable (Changeable) Database Properties

Configurable database properties affect the operation or configuration of the database. When you use DGMGRL or Enterprise Manager to create a primary database object and import existing standby databases into a new broker configuration, the property values are initially imported from the database settings.

You can update many property values when the database is either disabled or enabled. When a new database is added into the configuration, the broker connects to the database and imports initial values for the database properties from the current database settings. For example:

```
DGMGRL> SHOW DATABASE 'North_Sales' 'ArchiveLagTarget';
  ArchiveLagTarget = '0'

DGMGRL> EDIT DATABASE 'North_Sales' SET PROPERTY 'ArchiveLagTarget'=1200;
  Property "ArchiveLagTarget" updated

DGMGRL> SHOW DATABASE 'North_Sales' 'ArchiveLagTarget';
  ArchiveLagTarget = '1200'
```

When the configuration is enabled, the broker keeps the database property values in the broker configuration file consistent with the values being used in the database. For those that are related to initialization parameter properties, the broker maintains the consistency among the value in the broker configuration file, the current database value, and the initialization parameter value in the server parameter file, as follows:

- For dynamic parameters, the broker keeps the value of the database parameter consistent in the system global area (SGA) for the instance, in the broker configuration file, and in the server parameter file.
- For static parameters and properties, the database parameter value in the system global area (SGA) for the instances may temporarily differ from what is in the broker configuration file and in the server parameter file. Typically, the database value becomes the same as the server parameter file value and the broker configuration file value the next time the database instance is stopped and restarted.

Even when the configuration is disabled, you can update database property values through the broker. The broker retains the property settings (without validating the values) and updates the database initialization parameters in the server parameter file and the settings in memory the next time you enable the broker configuration.

Note:

Even though you can change a property value when the configuration is disabled, the change does not take effect on the database unless the configuration is enabled. Also note that some property values can only be changed in the disabled state.

## 4.4 Managing Redo Transport Services

To manage redo transport services, you specify the following set of configurable database properties on each standby database:

- `DGConnectIdentifier`
- `AlternateLocation`
- `Binding`
- `LogShipping`
- `LogXptMode`
- `MaxConnections`
- `MaxFailure`
- `NetTimeout`
- `RedoCompression`
- `ReopenSecs`
- `StandbyArchiveLocation`

You can use these properties to specify how the broker configures redo transport services for the standby database. The actual redo transport setup, such as setting the `LOG_ARCHIVE_DEST_` n initialization parameter, is carried out by the broker on the primary database (except for the `StandbyArchiveLocation` property). If changing the property requires that you change the `LOG_ARCHIVE_DEST_` n initialization parameter attributes, the broker forces a log switch on each thread so that the new setting is adopted immediately by the primary database.

You should also preset these properties on the primary database in preparation for it to be switched over to a standby database.

### 4.4.1 Setting Up For Redo Transport

Redo data is transported to a standby database using Oracle Net. An Oracle Net service name is specified with the `SERVICE` attribute of the `LOG_ARCHIVE_DEST_n` initialization parameter and is used to transmit redo data to the standby database. The Oracle Net service name is translated into a connect descriptor that contains the information necessary for connecting to the standby database.

The `SERVICE` attribute can be set or changed by using the `DGConnectIdentifier` database property. The `DGConnectIdentifier` property is set when a database is first added to the configuration. Its initial value is the connect identifier that is specified in the optional `CONNECT IDENTIFIER IS` clause of the `ADD DATABASE` command. If that optional clause is not specified, the initial value of the `DGConnectIdentifier` property is extracted from the `SERVICE` attribute of the `LOG_ARCHIVE_DEST_n` initialization parameter whose `DB_UNIQUE_NAME` attribute matches the `DB_UNIQUE_NAME` of the database specified in the `ADD DATABASE` command.

The `DGConnectIdentifier` property value is also used to set up the `FAL_SERVER` initialization parameter. If the `DGConnectIdentifier` property for any database is changed, the `SERVICE` attribute of the corresponding `LOG_ARCHIVE_DEST_n` initialization parameter will also be changed. In addition, the `FAL_SERVER` initialization parameter will also be updated on every enabled standby database in the configuration.

### 4.4.2 Managing Redo Transport Services for Data Protection Modes

Section 4.6 describes how the broker handles data protection modes. As a part of the overall configuration protection mode, you must ensure that redo transport services are also properly set up for the data protection mode that you choose.

You use the `LogXptMode` database property to set the `SYNC` or `ASYNC` mode for redo transport services. See Table 4-2 for additional information about protection modes and redo transport services.

The values for the `LogXptMode` property are described in the following list:

SYNC

Configures redo transport services for this standby database using the `SYNC` and `AFFIRM` attributes of the `LOG_ARCHIVE_DEST_` n initialization parameter. This mode, along with standby redo log files, is required for configurations operating in either maximum protection mode or maximum availability mode. This redo transport service enables the highest grade of data protection to the primary database, but also can incur a higher performance impact.

ASYNC

Configures redo transport services for this standby database using the `ASYNC` and `NOAFFIRM` attributes of the `LOG_ARCHIVE_DEST_` n initialization parameter. This mode, along with standby redo log files, enables a moderate grade of protection to the primary database, and lower performance impact.

### 4.4.3 Turning Redo Transport Services On and Off

Turn redo transport services on and off by setting the state of the primary database. Setting the primary database state to `TRANSPORT-ON` starts redo transport services to the standby databases, and setting the primary database state to `TRANSPORT-OFF` stops redo transport services to all the standby database.

Note:

Oracle does not recommend turning off redo transport services to all standby databases. This increases the risk of data loss if the primary database fails.

Turn redo transport services on and off to an individual standby database using the `LogShipping` database property on the standby database. The `LogShipping` property accepts values `ON` and `OFF`. If you set the `LogShipping` property to `OFF` for a standby database, redo transport services to this standby database are turned off, while redo transport services to other databases are not affected. You can set `LogShipping` to `ON` to turn back on redo transport services to the standby database.

The relationship between setting the primary database state and setting the `LogShipping` property is as follows:

- If the primary database state is set to `TRANSPORT-OFF`, redo transport services to all the standby databases are stopped regardless of the `LogShipping` property values of the individual standby databases.
- If the primary database state is set to `TRANSPORT-ON`, redo transport services to each standby database are determined by the `LogShipping` property of that database.

Example 4-2 and Example 4-3 show how to turn off redo transport services in two different scenarios.

Example 4-2 Turn Off Redo Transport Services to All Standby Databases

```
DGMGRL> EDIT DATABASE 'North_Sales' SET STATE='TRANSPORT-OFF';
DGMGRL> SHOW DATABASE 'North_Sales';
 
Database - North_Sales
 
  Role:            PRIMARY
  Intended State:  TRANSPORT-OFF
  Instance(s):
    north_sales1
 
Database Status:
SUCCESS
```

Example 4-3 Turn Off Redo Transport Services to a Specific Standby Database

```
DGMGRL> EDIT DATABASE 'South_Sales' SET PROPERTY 'LogShipping'='OFF';
Property "LogShipping" updated

DGMGRL> SHOW DATABASE 'South_Sales' 'LogShipping';
  LogShipping = 'OFF'
```

### 4.4.4 Specifying Locations for Archived Redo Log Files

You can set up locations on the standby database to store the archived redo log files to be used by log apply services on the standby database. This is done by setting the `StandbyArchiveLocation` and `AlternateLocation` database properties on the standby database.

`StandbyArchiveLocation` specifies a standby location where the archived redo log files will be stored. The broker only manages the location to store archived redo log files received from the primary database. For archived redo log files generated locally when the database is either the primary database or a logical standby database, you need to set up local destinations directly through the `LOG_ARCHIVE_DEST_` n initialization parameter. The broker allows the value of `StandbyArchiveLocation` to be the same as the location you set up for locally generated logs, in which case the broker sets up the `VALID_FOR` attribute of the destination appropriately so that it can be used for both the archived redo log files received from the primary database and archived redo log files generated locally.

Note:

On a logical standby database, Oracle recommends that the `LOCATION` attribute of the `LOG_ARCHIVE_DEST_` `n` initialization parameter for the local destination be different from the value of either the `StandbyArchiveLocation` or `AlternateLocation` property unless you are using a database recovery area.

You can also set up an alternate location to store archived redo log files on the standby using the `AlternateLocation` property on the standby database. This is useful for avoiding disk capacity problems or disk errors when archiving the online redo log files on the standby database. `AlternateLocation` specifies a standby location where the archived redo log files will be stored if the location specified by the `StandbyArchiveLocation` fails. The broker sets up the alternate location properly using the `ALTERNATE` attribute of the `LOG_ARCHIVE_DEST_` n initialization parameter.

Note:

You can use the database recovery area to store archived redo log files on the standby. In such a case, the value of the `StandbyArchiveLocation` or `AlternateLocation` properties can be set to `USE_DB_RECOVERY_FILE_DEST`.

### 4.4.5 Other Redo Transport Settings

You can use the `Binding`, `MaxFailure`, `MaxConnections`, `NetTimeout`, `RedoCompression`, and `ReopenSecs` database properties to tune the performance of redo transport services and to set up redo transport services failure policies. These properties correspond to attributes on the `LOG_ARCHIVE_DEST_` n initialization parameter.

When creating a new standby database, the broker sets these properties with default values. When importing an existing standby database, the broker imports existing settings corresponding to these properties if it finds a match between the service string of a current destination and the connect identifier that was specified when the database was added to the configuration. If that fails, it finds a match between the `db_unique_name` of a current destination and the name that was specified when the database was added to the configuration.

For most cases, the default values or the imported values should be sufficient for normal operations. If for some reason you need to change these property values, you can use DGMGRL commands to set up these properties. Enterprise Manager does not provide an interface for modifying these properties.

See Also:

[Chapter 8](dbpropref.md) for complete information about these database properties

### 4.4.6 Redo Transport Services in an Oracle RAC Database Environment

If the primary database is an Oracle RAC database, the broker ensures that redo transport services are set up identically on each of the primary database instances. Each instance has the same remote destinations, and for each remote destination, all instances are set up the same in terms of redo transport service, performance related settings, and so on. If an instance has different settings, the broker raises a health check warning on that particular instance

Settings relative to redo transport services are saved in the broker configuration file as properties. When you update a redo transport-related property on a standby database, the corresponding change is also made automatically by the broker to the `LOG_ARCHIVE_DEST_` n initialization parameter on all of the primary database instances. If a new instance comes up on the primary database, the broker sets up redo transport services for the new instance using the redo transport-related properties of all the standby databases currently being managed by the broker. After the new instance is opened for activity, all archived redo log files generated on this instance will begin to transmit to the standby databases.

See also:

[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/log_arch_dest_param.htm#SBYDB01100) for additional information about the `LOG_ARCHIVE_DEST_` n initialization parameter

### 4.4.7 Transport Lag

Transport lag is a measure of the degree to which the transport of redo to the standby database lags behind the generation of redo on the primary database.

If there are one or more redo gaps on the standby database, the transport lag is calculated as if no redo has been received after the beginning of the earliest redo gap.

Both Enterprise Manager and the DGMGRL client display the redo transport lag for each managed standby database. Enterprise Manager displays the transport lag on the Data Guard home page. The DGMGRL client displays the transport lag in the `SHOW DATABASE` output for a standby database. There is no transport lag displayed for a primary database. For example:

```
DGMGRL> show database 'South_Sales';
Database - South_Sales
  Role:            PHYSICAL STANDBY
  Intended State:  APPLY-ON
  Transport Lag:   0 seconds
  Apply Lag:       0 seconds
  Real Time Query: OFF
  Instance(s):
  south_sales1
 
Database Status:
SUCCESS
```

The transport lag can help you identify any problems that may exist with the redo transport services.

## 4.5 Managing Log Apply Services

You can manage Redo Apply and SQL Apply on physical and logical standby databases through the following log apply-related database properties:

- Properties common to Redo Apply and SQL Apply
	- `ApplyInstanceTimeout`
		- `DelayMins`
		- `PreferredApplyInstance`
- Properties specific to Redo Apply
	- `ApplyParallel`
- Properties specific to SQL Apply
	- `LsbyASkipTxnCfgPr`
		- `LsbyDSkipTxnCfgPr`
		- `LsbyASkipCfgPr`
		- `LsbyDSkipCfgPr`
		- `LsbyASkipErrorCfgPr`
		- `LsbyDSkipErrorCfgPr`
		- `LsbyMaxEventsRecorded`
		- `LsbyPreserveCommitOrder`
		- `LsbyRecordSkipErrors`
		- `LsbyRecordSkipDdl`
		- `LsbyRecordAppliedDdl`
		- `LsbyMaxSga`
		- `LsbyMaxServers`
	There are some properties related to SQL Apply that, if changed, may require a restart of SQL Apply if the current database state is `APPLY-ON`. See the information in [Chapter 8](dbpropref.md) about properties related to SQL Apply, to determine which ones require SQL Apply to be restarted.
	If the current database state is `APPLY-OFF`, the property changes will take effect the next time the database state is changed to `APPLY-ON`.

### 4.5.1 Managing Delayed Apply

You can set up Apply Services so that the application of redo to the standby database is delayed. This allows the standby database to lag behind the primary database, and if a user error (for example, dropping a table) occurs during this window of time, the standby database will still contain the correct data that can be transmitted back to the primary database to repair the data.

By default, no delay is configured and the redo data is applied on a standby database as soon as possible. If the standby database has standby redo logs configured, the broker will enable real-time apply. When Redo Apply and SQL Apply apply redo in real time, the redo data is recovered directly from the standby redo log files as they are being filled. This means that the standby database does not have to wait for the log files to be archived before applying redo data from the archived redo log files. This minimizes the transactional lag between the primary and the standby.

Use the `DelayMins` database property to specify the number of minutes that log apply services must wait before applying redo data to the standby database. Note that only log apply services on the standby database are delayed. Redo transport services on the primary database are not delayed, thus the primary database data is still well protected by the standby database.

Caution:

Because the broker automatically enables real-time apply on standby databases, Oracle recommends that you configure all databases to use Flashback Database.

### 4.5.2 Managing Parallel Apply with Redo Apply

For Redo Apply, you can configure whether multiple parallel processes are used to apply redo data received from the primary database by using the `ApplyParallel` database property. Parallelism is enabled by default, which means Redo Apply automatically chooses the optimal number of parallel processes based on the number of CPUs in the system. (This is equivalent to setting the `ApplyParallel` property to `AUTO`.) You can disable parallelism by setting the `ApplyParallel` property to `NO`.

Note:

The `ApplyParallel` database property is not displayed on the Edit Properties page of Enterprise Manager.

See Also:

The `ApplyParallel` property in [Section 8.3.4, "ApplyParallel"](dbpropref.md)

### 4.5.3 Allocating Resources to SQL Apply

You can control how much SGA memory is available for SQL Apply. This can be set using the `LsbyMaxSga` database property.

To control the number of parallel query servers used by SQL Apply, you can use the `LsbyMaxServers` database property.

You can control the trade off between SQL Apply performance and the commit order of transactions. The `LsbyPreserveCommitOrder` database property controls whether transactions are committed on the logical standby database in the exact same order in which they were committed on the primary database. Preserving commit order may affect performance.

See Also:

[Section 8.3.25, "LsbyMaxSga"](dbpropref.md) and [Section 8.3.26, "LsbyMaxServers"](dbpropref.md)

### 4.5.4 Managing SQL Apply Filtering

One of the benefits of a logical standby database is to allow control of what to apply and what not to apply. This is done by setting up SQL Apply filters. The granularity of the filtering ranges from a specific transaction to database objects to a particular class of SQL statement on a particular schema.

To add a SQL Apply filter in Data Guard broker, use the `LsbyASkip*` database properties (for example, `LsbyASkipTxnCfgPr` or `LsbyASkipCfgPr`). To delete a previously added SQL Apply filter, use the `LsbyDSkip*` database properties (for example, `LsbyDSkipTxnCfgPr` or `LsbyDSkipCfgPr`).

See Also:

[Chapter 8](dbpropref.md) for information on these properties

### 4.5.5 Managing SQL Apply Error Handling

You can fine-tune SQL Apply to handle apply errors on a specified set of SQL statements on particular schemas. When such SQL Apply errors are encountered, Data Guard can either skip the error to continue SQL Apply or call a specified stored procedure at the time when the error is encountered.

To add this error handling capability, use the `LsbyASkipErrorCfgPr` database property. To delete a previously added error handling specification, use the `LsbyDSkipErrorCfgPr` database property.

Changing these properties results in restarting SQL Apply if the current database state is `APPLY-ON`. If the current database state is `APPLY-OFF`, the property changes take effect the next time the database state is changed to `APPLY-ON`.

### 4.5.6 Managing the DBA\_LOGSTDBY\_EVENTS Table

The `DBA_LOGSTDBY_EVENTS` table records important events that affect SQL Apply. Because every logical standby database might have a different interest in the set of events to be recorded in this table, Data Guard provides a means to control the event recording. From the Data Guard broker, you can use the `LsbyRecord*` database properties (for example, `LsbyRecordSkipDdl` or `LsbyRecordSkipErrors`) to control recording of a particular set of events. The value of these properties are either `TRUE` or `FALSE`, indicating the turning on or off of the event recording.

### 4.5.7 Apply Services in an Oracle RAC Database Environment

If a standby database is an Oracle RAC database, only one instance of the Oracle RAC database can have log apply services running at any time. This instance is called the apply instance. If the apply instance fails, the broker automatically moves log apply services to a different instance; this is called apply instance failover.

#### 4.5.7.1 Selecting the Apply Instance

Note:

The information in this section is not applicable to snapshot standby databases.

If you have no preference which instance is to be the apply instance in an Oracle RAC standby database, the broker randomly picks an apply instance. If you want to select a particular instance as the apply instance, there are two methods to do this.

- The first method is to pick an apply instance before there is an apply instance running in the Oracle RAC standby database. To do so, set the value of the `PreferredApplyInstance` database property to the name of the instance (see the `SidName` property) you prefer to be the apply instance. The broker starts log apply services on the instance specified by the `PreferredApplyInstance` property when no apply instance is yet selected in the Oracle RAC standby database. This could be the case before you enable the standby database for the first time, or if the apply instance just failed and the broker is about to do an apply instance failover, or if the Oracle RAC database is currently the primary and you want to specify its apply instance in preparation for a switchover. Once the apply instance is selected and, as long as the apply instance is still running, the broker disregards the value of the `PreferredApplyInstance` property even if you change it.
- The second method is to change the apply instance when the apply instance is already selected and is running. To change the apply instance, issue the DGMGRL `SET STATE` command to set the standby database state to `APPLY-ON`, with a specific apply instance argument. The `SET STATE` command will update the `PreferredApplyInstance` property to the new apply instance value, and then move log apply services to the new instance. For example, use DGMGRL `SHOW` command to show the available instances for the standby database, then issue the `EDIT DATABASE` command to move log apply services to the new instance:
	```
	DGMGRL> SHOW DATABASE 'South_Sales'
	 
	Database - South_Sales
	 
	  Role:            PHYSICAL STANDBY
	  Intended State:  APPLY-ON
	  Transport Lag:   0 seconds
	  Apply Lag:       0 seconds
	  Real Time Query: OFF
	  Instance(s):
	    south_sales1 (apply instance)
	    south_sales2
	 
	Database Status:
	SUCCESS
	```
	```
	DGMGRL> EDIT DATABASE 'South_Sales' SET STATE='APPLY-ON' WITH APPLY INSTANCE='south_sales2';
	Succeeded.
	DGMGRL> SHOW DATABASE 'South_Sales' 'PreferredApplyInstance';
	  PreferredApplyInstance = 'south_sales2'
	```
	```
	DGMGRL> SHOW DATABASE 'South_Sales'
	 
	Database - South_Sales
	 
	  Role:            PHYSICAL STANDBY
	  Intended State:  APPLY-ON
	  Transport Lag:   0 seconds
	  Apply Lag:       0 seconds
	  Real Time Query: OFF
	  Instance(s):
	    south_sales1
	    south_sales2 (apply instance)
	 
	Database Status:
	SUCCESS
	```

Ensure that the new apply instance is running when the command is issued. Otherwise, the apply instance remains the same.

Once the apply instance is selected, the broker keeps apply instance information in the broker configuration file so that even if the standby database is shut down and restarted, the broker still selects the same instance to start log apply services. The apply instance remains unchanged until changed by the user or it fails for any reason and the broker decides to do an apply instance failover.

#### 4.5.7.2 Apply Instance Failover

To tolerate a failure of the apply instance, the broker leverages the availability of the Oracle RAC standby database by automatically failing over log apply services to a different standby instance. The apply instance failover capability provided by the broker enhances data protection.

To set up apply instance failover, set the `ApplyInstanceTimeout` database property to specify the time period that the broker will wait after detecting an apply instance failure and before initiating an apply instance failover. To select an appropriate timeout value, you need to consider:

- If there is another mechanism in the cluster that will try to recover the failed apply instance.
- How long your business can tolerate not applying redo data on the standby database.
- The overhead associated with moving the log apply services to a different instance. The overhead may include retransmitting, from the primary database, all log files accumulated on the failed apply instance that have not been applied if those log files are not saved in a shared file system that can be accessed from other standby instances.

The broker default value of the `ApplyInstanceTimeout` property is 0 seconds, indicating that apply instance failover should occur immediately upon detection of the failure of the current apply instance.

After the broker initiates an apply instance failover, the broker selects a new apply instance according to the following rule: if the `PreferredApplyInstance` property indicates an instance that is currently running, select it as the new apply instance; otherwise pick a random instance that is currently running to be the new apply instance.

In addition, if the physical standby database was operating in real-time query mode when the apply instance failed, then after Oracle recovery cleanup is completed, the broker opens any instances that had been automatically closed. If the failed apply instance was the only instance open, then the instance chosen as the new apply instance is opened before starting apply services so that real-time query is once again in effect.

See Also:

- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/manage_ps.htm#SBYDB00707) for more information about real-time query mode
- The My Oracle Support note 1357597.1 at `http://support.oracle.com` for additional information about apply instance failures in an Active Data Guard Oracle RAC standby

### 4.5.8 Apply Lag

Apply lag is a measure of the degree to which the data in a standby database lags behind the data in the primary database, due to delays in propagating and applying redo to the standby database.

Both Enterprise Manager and the DGMGRL client display the apply lag for each managed standby database. Enterprise Manager displays the apply lag on the Data Guard home page. The DGMGRL client displays the apply lag in the `SHOW DATABASE` output for a standby database. There is no apply lag displayed for a primary database. For example:

```
DGMGRL> show database 'South_Sales';
Database - South_Sales
  Role:            PHYSICAL STANDBY
  Intended State:  APPLY-ON
  Transport Lag:   0 seconds
  Apply Lag:       0 seconds
  Real Time Query: OFF
  Instance(s):
    south_sales1
 
Database Status:
SUCCESS
```

The apply lag can help you identify any problems that may exist with both the redo transport services and the log apply services.

## 4.6 Managing Data Protection Modes

The broker can simplify the process of setting up your configuration for any of the different grades of data protection: maximum protection, maximum availability, or maximum performance.

This section contains the following topics to help you configure the proper protection for your configuration:

- Section 4.6.1, "Setting the Protection Mode for Your Configuration"
- Section 4.6.2, "How the Protection Modes Influence Broker Operations"

### 4.6.1 Setting the Protection Mode for Your Configuration

To set the protection mode, perform the following steps:

Step 1 Determine which data protection mode you want to use.

Each data protection mode provides a different balance of data protection, data availability, and database performance. To select the data protection mode that meets the needs of your business, carefully consider your data protection requirements and the performance expectations of your users.

Note:

The maximum protection and maximum availability modes cannot be used if the only standby database in a configuration is a snapshot standby.

Maximum Availability This protection mode provides the highest level of data protection that is possible without compromising the availability of a primary database. Transactions do not commit until all redo data needed to recover those transactions has been written to the online redo log and to the standby redo log on at least one synchronized standby database. If the primary database cannot write its redo stream to at least one synchronized standby database, it operates as if it were in maximum performance mode to preserve primary database availability until it is again able to write its redo stream to a synchronized standby database.

This mode ensures that no data loss will occur if the primary database fails, but only if a second fault does not prevent a complete set of redo data from being sent from the primary database to at least one standby database.

You can enable fast-start failover if the protection mode is maximum availability.

Maximum Performance This protection mode provides the highest level of data protection that is possible without affecting the performance of a primary database. This is accomplished by allowing transactions to commit as soon as all redo data generated by those transactions has been written to the online log. Redo data is also written to one or more standby databases, but this is done asynchronously with respect to transaction commitment, so primary database performance is unaffected by delays in writing redo data to the standby database(s).

This protection mode offers slightly less data protection than maximum availability mode and has minimal impact on primary database performance.

This is the default protection mode.

You can enable fast-start failover if the protection mode is maximum performance.

Maximum Protection This protection mode ensures that no data loss will occur if the primary database fails. To provide this level of protection, the redo data needed to recover a transaction must be written to both the online redo log and to the standby redo log on at least one synchronized standby database before the transaction commits. To ensure that data loss cannot occur, the primary database will shut down, rather than continue processing transactions, if it cannot write its redo stream to at least one synchronized standby database.

Transactions on the primary are considered protected as soon as Data Guard has written the redo data to persistent storage in a standby redo log file. Once that is done, acknowledgment is quickly made back to the primary database so that it can proceed to the next transaction. This minimizes the impact of synchronous transport on primary database throughput and response time. To fully benefit from complete Data Guard validation at the standby database, be sure to operate in real-time apply mode so that redo changes are applied to the standby database as fast as they are received. Data Guard signals any corruptions that are detected so that immediate corrective action can be taken.

Because this data protection mode prioritizes data protection over primary database availability, Oracle recommends that a minimum of two standby databases be used to protect a primary database that runs in maximum protection mode to prevent a single standby database failure from causing the primary database to shut down. If only one standby database is supporting maximum protection mode, Data Guard broker will disallow the shutdown of the apply instance. This prevents the primary database from shutting down.

You cannot enable fast-start failover if the protection mode is maximum protection.

See Also:

- [Section 5.5](sofo.md) for information on fast-start failover
- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/toc.htm) for complete information about data protection modes

Step 2 Set up standby redo log files.

You must add standby redo log files on all standby databases, regardless of the protection mode you are using. Also, Oracle requires that you add standby redo log files on the primary database in preparation for a future switchover or failover. Standby redo log files are required on the primary database if you want to enable fast-start failover.

Enterprise Manager automatically prompts you to select one or more standby databases in the configuration and sets up standby redo log (SRL) files on them and on the primary database in preparation for a future role change.

See Also:

If you are using the DGMGRL command-line interface, follow the instructions in [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/create_ps.htm#SBYDB00426) to configure standby redo log files.

Step 3 Set the LogXptMode configurable database property, if necessary.

If the data protection mode requires that you change the redo transport service used by any of the standby databases, change the setting of the `LogXptMode` database property appropriately on each standby database. See Section 4.4 for more information about setting the redo transport service. Table 4-2 shows the protection modes and the corresponding redo transport service.

Enterprise Manager automatically specifies the correct redo transport service on the primary database in preparation for a future switchover.

Table 4-2 Data Guard Protection Modes and Requirements

| Protection Mode | Redo Transport | Standby Redo Log Files Needed? | Usable with Fast-Start Failover? |
| --- | --- | --- | --- |
| `MAXPROTECTION` | `SYNC` | Yes | No |
| `MAXAVAILABILITY` | `SYNC` | Yes | Yes |
| `MAXPERFORMANCE` | `ASYNC` | Yes | Yes |

Step 4 Set the protection mode.

Set the protection mode using DGMGRL commands or Enterprise Manager.

With DGMGRL:

1. Use the `EDIT DATABASE (property)` command and specify the standby database whose redo transport service should be changed to correspond to the protection mode you plan to set. For example, if you plan to set the overall Data Guard configuration to operate in maximum availability mode, you must use the `EDIT DATABASE` command to set the `SYNC` mode for redo transport services. For example:
	```
	DGMGRL> EDIT DATABASE 'South_Sales' SET PROPERTY 'LogXptMode'='SYNC';
	```
	Do this also for the primary database or another standby database in the configuration to ensure that it can support the chosen protection mode after a switchover.
2. Use the `EDIT CONFIGURATION SET PROTECTION MODE AS` `protection-mode` command to set the overall configuration protection mode. For example:
	```
	DGMGRL> EDIT CONFIGURATION SET PROTECTION MODE AS MAXAVAILABILITY;
	```

See [Section 6.5](cli.md) for a DGMGRL scenario showing how to set the protection mode.

With Enterprise Manager:

1. On the Data Guard overview page, click the link to the right of the Protection Mode label.
2. Select Maximum Protection, Maximum Availability, or Maximum Performance and click Continue.
3. If prompted, log in to the database with `SYSDBA` privileges and click Login.
4. Select one or more standby databases to support the protection mode that you selected. If standby redo log files are needed, verify the names of the log files. Click OK.
5. On the Confirmation page, click Yes.

After upgrading the protection mode from maximum performance mode to maximum protection mode using either DGMGRL or Enterprise Manager, the primary database will be restarted automatically if you are upgrading to maximum protection mode. The primary database need not be restarted following a downgrade of the protection mode.

No restart is required when upgrading the protection mode from maximum performance to maximum availability or from maximum availability to maximum protection.

Note:

You can avoid a restart of the primary database when upgrading from maximum performance mode to maximum protection mode by first upgrading to maximum availability. Once in maximum availability mode, then upgrade to maximum protection.

Note:

Online database relocation with Oracle RAC One Node cannot be performed on the only physical standby database that supports maximum protection mode.

If online database relocation must be performed, then you must first downgrade the protection mode to maximum availability. After the online database relocation of the physical standby database is performed, you can upgrade the protection mode back to maximum protection. A restart of the primary database is not required.

### 4.6.2 How the Protection Modes Influence Broker Operations

This section describes how operations such as switchover, failover, disabling, or enabling the Data Guard configuration can have an effect on the configuration's protection mode and redo transport services. This section contains the following sections:

- Upgrading or Downgrading the Current Protection Mode
- Switchover Operations
- Failover Operations
- Disable and Enable Operations
- Requirements For Removing a Database from the Configuration
- Requirements On Other Operations

#### 4.6.2.1 Upgrading or Downgrading the Current Protection Mode

No restart is necessary when you upgrade the current Data Guard protection mode to maximum availability or when you downgrade the current Data Guard protection mode. Follow these recommendations when upgrading or downgrading the Data Guard protection mode:

- When upgrading the protection mode, upgrade the redo transport service before you upgrade the overall protection mode. At the time when you change the protection mode or reset the redo transport service of a standby database, the broker verifies that there is at least one standby database in the configuration that can support the desired grade of protection. If not, then the broker does not change the protection mode and returns an error.
- When downgrading the protection mode, downgrade the protection mode first and then change the redo transport service (if necessary). The broker will disallow a change of the redo transport service if doing so invalidates the current overall protection mode.

If you upgrade the protection mode from the maximum performance mode, the broker ensures that there is at least one standby database whose `LogXptMode` database property is set to `SYNC`. Additionally, for upgrades to maximum protection mode, the broker ensures there are no gaps in the redo data on the standby database. If there are no standby databases in the configuration that meet these requirements, the request to upgrade the protection mode is rejected with an error.

The protection mode cannot be changed if fast-start failover is enabled.

WARNING:

The primary database will be shut down and restarted if you upgrade the protection mode from maximum performance to maximum protection. You can avoid this by first upgrading to maximum availability. Once in maximum availability mode, then upgrade to maximum protection.

#### 4.6.2.2 Switchover Operations

A switchover does not change the overall Data Guard protection mode. The protection mode remains the same as it was before the switchover.

This requires that there be a standby database that is properly configured to support the current protection mode once the switchover completes. This can be either another standby database in the configuration or the current primary database that will become a standby database after the switchover completes.

Before you perform a switchover, if necessary, you can add standby redo log files and set the redo transport service on the current primary database, or on another standby database in the configuration, to the `SYNC` or `ASYNC` mode that is required to support the Data Guard protection mode. Then, when the switchover begins:

- The broker verifies the presence of standby redo log files and the redo transport service setting on each standby database and on the current primary database.
- The broker verifies there are no gaps in the redo data present on the target standby database.

If the verification is successful, the switchover continues; otherwise, the switchover fails, and the database roles and the broker configuration files remain unchanged.

WARNING:

The broker will shut down and restart the primary database if the target of the switchover is a physical standby database.

See Also:

[Section 5.3](sofo.md) for more information about switchovers

#### 4.6.2.3 Failover Operations

After you perform a manual failover, the Data Guard protection mode is downgraded to maximum performance mode if the protection mode was at maximum protection. You can upgrade the protection mode later, if necessary. If the protection mode was at maximum availability or maximum performance, it remains unchanged. The redo transport services of the standby databases remain unchanged.

If fast-start failover occurs, the broker preserves the protection mode that was in effect just prior to the fast-start failover.

See Also:

[Section 5.4](sofo.md) and [Section 5.5](sofo.md) for more information about manual failover and fast-start failover, respectively

#### 4.6.2.4 Disable and Enable Operations

When you disable broker management of a standby database, the broker checks to see if the overall protection mode can still be satisfied by any of the remaining standby databases. If not, the broker rejects the disable operation. Otherwise, the broker allows the disable operation to proceed as long as fast-start failover is not enabled. If it is enabled, the broker allows the disable operation to proceed only if the standby database is not the target standby database for fast-start failovers.

Caution:

If you disable broker management of a standby database in the broker configuration, that standby database cannot be used by the broker as a failover target in the event of loss of the primary database.

After a standby database is successfully disabled, you can change the redo transport service for that database and the broker will record the change in the broker configuration file. The change will not affect the overall protection mode because it is guaranteed that at least one of the enabled standby databases already satisfies the overall protection mode requirement.

As long as fast-start failover is not enabled, you can disable the entire configuration regardless of the protection mode. You cannot disable the configuration if fast-start failover is enabled. See [Section 5.5.2.2, "Restrictions When Fast-Start Failover is Enabled"](sofo.md) for more information.

If the entire configuration is disabled, you can change any broker settings, including the redo transport services of the standby databases and the protection mode of the configuration. The broker saves the changes in the broker configuration file, but the changes will not be made to the database itself.

When enabling broker management of the entire configuration, the broker first checks to see if the protection mode will be satisfied by the redo transport services of the standby databases that will be enabled. If not, the enable operation fails and the configuration remains disabled. Otherwise, the enable operation successfully enables the configuration, and the broker enables the database using the settings saved in the broker configuration file.

#### 4.6.2.5 Requirements For Removing a Database from the Configuration

When removing a standby database from the broker configuration, the broker checks to see if the protection mode will still be satisfied. The operation fails if:

- Removing the database compromises the protection mode
- Fast-start failover is enabled and you try to remove the standby database that is the target of the fast-start failover

You can remove the configuration at any time, unless fast-start failover is enabled.

#### 4.6.2.6 Requirements On Other Operations

Some operations that take place in a broker configuration, especially operations related to redo transport services, can affect the overall protection mode. These operations include:

- Stopping redo transport services on the primary database
- Stopping redo transport services to individual standby databases
- Downgrading the `LogXptMode` database property from `SYNC` to `ASYNC` on the only standby database that supports a configuration operating in maximum availability mode or maximum protection mode

Before any of these operations can proceed, the broker checks to see if the protection mode will be supported by the redo transport service settings on the standby databases after the operation completes. If not, the broker fails the operation and returns an error.

## 4.7 Managing Fast-Start Failover

For lights out administration, you can enable fast-start failover to allow the broker to determine if a failover is necessary and to initiate a failover to a pre-specified target standby database, with either no data loss or a configurable amount of data loss. In addition, you can specify under which conditions or errors you want a failover to be initiated. Oracle also provides the `DBMS_DG` PL/SQL package to allow an application to request a fast-start failover.

The following configuration properties are used to control the behavior of fast-start failover:

- `FastStartFailoverThreshold`
- `FastStartFailoverPmyShutdown`
- `FastStartFailoverLagLimit`
- `FastStartFailoverAutoReinstate`
- `FastStartFailoverTarget`

You can also use Oracle Enterprise Manager or the DGMGRL `ENABLE FAST_START FAILOVER CONDITION` and `DISABLE FAST_START FAILOVER CONDITION` commands to specify conditions for which a fast-start failover should occur.

### 4.7.1 Configure Properties to Tune Fast-Start Failover

The configurable properties for fast-start failover include:

- `FastStartFailoverThreshold`
	Set the `FastStartFailoverThreshold` configuration property to specify the number of seconds you want the observer and target standby database to wait (after detecting the primary database is unavailable) before initiating a failover. See [Section 5.5.2, "Enabling Fast-Start Failover"](sofo.md) for more information and an example.
- `FastStartFailoverPmyShutdown`
	The `FastStartFailoverPmyShutdown` configuration property controls whether the primary database will shut down if redo generation has been stalled (`FS_FAILOVER_STATUS` column of `V$DATABASE` contains a value of `STALLED`) and the primary database has lost connectivity with the observer and target standby database for longer than the number of seconds specified by the `FastStartFailoverThreshold` configuration property. The default value for FastStartFailoverPmyShutdown is `TRUE`.
	Note:
	The primary database is always shut down if a user configurable fast-start failover condition is detected or if an application initiated a fast-start failover by calling the `DBMS_DG.INITIATE_FS_FAILOVER` function.
- `FastStartFailoverLagLimit`
	The fast-start failover feature can be configured on databases operating in maximum performance mode. Destinations that receive redo in `ASYNC` mode will be acceptable fast-start failover target standby databases, and these destinations can lag the primary in terms of redo received and applied. A configurable time-based limit can be specified through the `FastStartFailoverLagLimit` configuration property. If the standby database's applied redo point is within this many seconds of the primary's redo generation point, a fast-start failover will be allowed. If its applied point lags beyond this limit, a fast-start failover is not allowed. The `FastStartFailoverLagLimit` configuration property is not used if fast-start failover is enabled when the configuration is operating in maximum availability mode.An `ASYNC` destination is only a valid fast-start failover target in a configuration operating in maximum performance mode. If you want to change protection mode or change the destination to sync, you must first disable fast-start failover. Likewise, changing the protection mode from `MAXAVAILABILITY` to `MAXPERFORMANCE` will require first disabling fast-start failover and changing the `LogXptMode` property of the primary and target standby to `ASYNC`.Reinstatement of an old primary will be possible after a fast-start failover to an `ASYNC` target standby. If the observer rediscovers the old primary, it will automatically reinstate the old primary and any redo generated within the specified lag will be lost.
	See Also:
	[Chapter 8, "Data Guard Broker Properties"](dbpropref.md) for more information
- `FastStartFailoverAutoReinstate`
	The `FastStartFailoverAutoReinstate` configuration property controls whether the former primary database is automatically reinstated if a fast-start failover occurred because the primary database crashed or was stalled for longer than `FastStartFailoverThreshold` seconds. The default value for `FastStartFailoverAutoReinstate` is `TRUE`.
	If you want to perform diagnostic or repair work after failover has completed, you can avoid an automatic reinstatement by setting the `FastStartFailoverAutoReinstate` configuration property to `FALSE`.
	Note:
	The former primary database is never automatically reinstated if a fast-start failover occurred because a user configurable fast-start failover condition was detected or because an application initiated a fast-start failover by calling the `DBMS_DG.INITIATE_FS_FAILOVER` function.

### 4.7.2 Configure Conditions for Fast-start Failover

By default, a fast-start failover is done when neither the observer nor the standby can reach the primary after the configured time threshold (`FastStartFailoverThreshold`) has passed. There are also other conditions under which you might want a fast-start failover to occur.

The configurable conditions fall into two classes: those detected through the database health-check mechanism and those detected through errors raised by the Oracle server (such as ORA errors). When a specified condition occurs, the observer will initiate a fast-start failover without waiting for `FastStartFailoverThreshold` to expire, assuming the standby is in a valid state to accept a failover.

Each condition may be enabled or disabled individually. The Data Guard configuration persists all user specified configurable fast-start failover conditions in the broker configuration file.

The observer will detect when the primary database has signaled any of the enabled health-check conditions and will immediately initiate a fast-start failover, assuming the standby is in a valid fast-start failover state (observed and either synchronized or within lag limits) to accept a failover.

For specified Oracle ORA-Error conditions, the primary database will notify the observer if the error is signaled and the observer will immediately initiate a fast-start failover, assuming the standby is in a valid fast-start failover state (observed and either synchronized or within lag limits) to accept a failover.

Note:

The primary database will shut down and the observer will not attempt to automatically reinstate the former primary database.

See Also:

- Oracle Enterprise Manager online help
- [ENABLE FAST\_START FAILOVER CONDITION](dgmgrl.md)
- [DISABLE FAST\_START FAILOVER CONDITION](dgmgrl.md)

### 4.7.3 Application Initiated Fast-Start Failover

You can use the `DBMS_DG` PL/SQL package to allow an application to direct a fast-start failover when it encounters specific conditions. See ["Directing a Fast-Start Failover From an Application"](sofo.md).

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_dg.htm#ARPLS920) for more information about the `DBMS_DG` package

## 4.8 Managing Database Conversions

You can use the DGMGRL `CONVERT DATABASE` command to convert a physical standby database to a snapshot standby database. A snapshot standby database is a fully updatable standby database.

Like a physical or logical standby database, a snapshot standby database receives and archives redo data from a primary database. However, unlike a physical or logical standby database, a snapshot standby database does not apply the redo data that it receives. The redo data received by a snapshot standby database is not applied until the snapshot standby is converted back into a physical standby database, after first discarding any local updates made to the snapshot standby database.

To convert a physical standby database to a snapshot standby database you must have Flashback Database enabled. The following example shows how to convert a physical standby database to a snapshot standby database:

```
DGMGRL> CONVERT DATABASE 'South_Sales' TO SNAPSHOT STANDBY;
```

When you are ready to convert the snapshot back into a physical standby, use the DGMGRL `CONVERT DATABASE` command as follows:

```
DGMGRL> CONVERT DATABASE 'South_Sales' TO PHYSICAL STANDBY;
```

## 4.9 Database Status

Database status reveals the health of the database. In general, the broker checks the health of a database by verifying if the actual database state and settings match with those described in the broker configuration file. This is done by checking if any component of the Data Guard configuration is functioning incorrectly (for example, if redo transport services have an error), and by checking if other required database settings are correctly set (for example, if the server parameter files are available and if the `ARCHIVELOG` mode is turned on). The following is a detailed list of what is being checked by the broker on a primary database and a standby database.

On a primary database, the health check determines whether the following conditions are met:

- Database is in the state specified by the user, as recorded in the broker configuration file
- Database is in the correct data protection mode
- Database is using a server parameter file
- Database is in the `ARCHIVELOG` mode
- Database guard is turned off
- Supplemental logging is turned on when there is a logical standby database in the configuration
- Redo transport services do not have any errors
- Database settings match those specified by the broker configurable properties
- Redo transport settings match those specified by the redo transport-related properties of the standby databases
- Current data protection level is consistent with configured data protection mode
- Primary database is able to resolve all gaps for all standby databases

On a standby database, the health check determines whether the following conditions are met:

- Database is in the state specified by the user, as recorded in the broker configuration file
- Database is using a server parameter file
- Database settings match those specified by the broker configurable properties
- Database guard is turned on when the database is a logical standby database
- Primary and target standby databases are synchronized or within lag limits if fast-start failover is enabled

The following monitorable database properties can be used to query the database status:

- `LogXptStatus`
- `InconsistentProperties`
- `InconsistentLogXptProps`
	Note:
	These properties are directly accessed through the DGMGRL command-line interface. Enterprise Manager rearranges the values of these properties for presentation in the GUI.

You can use the `SHOW DATABASE <db_unique_name>` command to get a brief description of the database (name, role, and so on), database status, and information about any health check problems. For example, the output of the following `SHOW DATABASE` command shows two problems: some redo transport services errors and an inconsistent redo transport-related property

```
DGMGRL> SHOW DATABASE 'North_Sales';
 
Database - North_Sales
  Role: PRIMARY
  Intended State: TRANSPORT-OFF
  Instance(s):
    north_sales1
      Error: ORA-16737: the redo transport service for standby
        database "South_Sales" has an error
 
    north_sales2
      Error: ORA-16737: the redo transport service for standby
        database "South_Sales" has an error
      Warning: ORA-16715: redo transport-related property
        ReopenSecs of standby "South_Sales" is inconsistent
Database Status:
ERROR
```

To further check the details about the database status, you can use the `LogXptStatus`, `InconsistentProperties`, and `InconsistentLogXptProps` monitorable database properties. `LogXptStatus` lists all log transport errors detected on all instances of the primary database. `InconsistentProperties` lists all properties that have inconsistent values between the broker configuration file and the database settings. `InconsistentLogXptProps` lists all redo transport-related properties of standby databases that have inconsistent values between the broker configuration file and the redo transport settings.

Issue the following `SHOW DATABASE` commands to obtain further details about the problems.

```
DGMGRL> SHOW DATABASE 'North_Sales' 'LogXptStatus';
LOG TRANSPORT STATUS
PRIMARY_INSTANCE_NAME  STANDBY_DATABASE_NAME  STATUS 
         north_sales1            South_Sales  ORA-12541: TNS:no listener
         north_sales2            South_Sales  ORA-12541: TNS:no listener
 
DGMGRL> SHOW DATABASE 'North_Sales' 'InconsistentLogXptProps';
INCONSISTENT LOG TRANSPORT PROPERTIES
 INSTANCE_NAME  STANDBY_NAME  PROPERTY_NAME  MEMORY_VALUE  BROKER_VALUE 
  north_sales2   South_Sales     ReopenSecs           600           300
```

See Also:

[Chapter 8](dbpropref.md) for detailed information about database properties