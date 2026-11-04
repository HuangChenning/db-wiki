---
title: Broker
book: Data Guard Broker
doc_id: F31839-04
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/dgbkr/managing-oracle-data-guard-broker-configuration-members.html
tags:
  - oracle
  - 21c
  - data-guard-broker
---

Learn how to manage broker configuration members, and monitor the state of each member of the configuration.

### Managing Broker Configuration Members

The broker uses information in its configuration file to manage and monitor the state of each member of the configuration.

The broker distinguishes between different types of members in a broker configuration. Each type of member has a set of states and properties that are appropriate for that type of member.

### Managing States of Broker Configuration Members

The members of a configuration can be in various states which, in an enabled configuration, determine the behavior of Oracle Data Guard.

The following table describes the various states.

Note that the following are not listed in the table:

- Snapshot standby databases (because they do not have states; they only receive redo data)
- Far sync instances (because they do not have states; they only receive redo and forward it to a standby database)
- Zero Data Loss Recovery Appliances (because they do not have states)

Table 4-1 Database States and Descriptions

| Database Role | State Name | Description |
| --- | --- | --- |
| Primary | `TRANSPORT-ON` | Redo transport services are set up to transmit redo data to the standby databases or far sync instances when the primary database is open for read/write access.  If this is an Oracle RAC database, all instances open in read/write mode will have redo transport services running.  This is the default state for a primary database when it is enabled for the first time. |
| Primary | `TRANSPORT-OFF` | Redo transport services are stopped on the primary database.  If this is an Oracle RAC database, redo transport services are not running on any instances. |
| Physical standby | `APPLY-ON` | Redo Apply is started on a physical standby database.  If the standby database is an Oracle RAC database, the broker starts Redo Apply on exactly one standby instance, called the apply instance. If this instance fails, the broker automatically chooses another instance that is either mounted or open read-only. This new instance then becomes the apply instance.  As of Oracle Database 12c Release 2 (12.2.0.1), Redo Apply can be set up to run on each active running physical standby instance. If a database has already been set up to run Redo Apply on multiple instances, then you can use the Data Guard broker property `ApplyInstances` to restrict the number of instances that are involved in Redo Apply on an Oracle RAC physical standby database.  `APPLY-ON` is the default state for a physical standby database when it is enabled for the first time.  If a license for the Oracle Active Data Guard option has been purchased, a physical standby database can be open while Redo Apply is active. This capability is known as real-time query. See [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/dgbkr&id=SBYDB00706) for more details. |
| Physical standby | `APPLY-OFF` | Redo Apply is stopped.  If this is an Oracle RAC database, there is no instance running Apply Services until you change the database state to `APPLY-ON`. |
| Logical standby | `APPLY-ON` | SQL Apply is started on the logical standby database when it is opened and the logical standby database guard is on.  If this is an Oracle RAC database, SQL Apply is running on one instance, the apply instance. If this instance fails, the broker automatically chooses another open instance. This new instance becomes the apply instance.  This is the default state for a logical standby database when it is enabled for the first time. |
| Logical standby | `APPLY-OFF` | SQL Apply is stopped. The logical standby database guard is on.  If this is an Oracle RAC database, there is no instance running SQL Apply until you change the state to `APPLY-ON`. |

#### Database State Transitions

You can use the DGMGRL `EDIT DATABASE` command to explicitly change the state of a database.

For example, the `EDIT DATABASE` command in the following example changes the state of the `North_Sales` database to `TRANSPORT-OFF`.

```
DGMGRL> EDIT DATABASE 'North_Sales' SET STATE='TRANSPORT-OFF';
Succeeded.
```

The following sections describe in more detail the possible state transitions for primary and standby databases.

Primary Database State Transitions

When transitioning the primary database to the `TRANSPORT-ON` state, the broker sets up redo transport services using the redo transport-related properties of the configuration members and the `RedoRoutes` property at the primary database. Redo transport services setup is done by setting the `LOG_ARCHIVE_DEST_` n and `LOG_ARCHIVE_DEST_STATE_` n initialization parameters on the primary database, and the `LOG_ARCHIVE_CONFIG` initialization parameter on all databases (primary or standby) and far sync instances. If necessary, the broker also sets up the data protection mode of the database to match the protection mode recorded in the broker configuration file. Finally, if the database is open, the broker switches a log for each thread to initiate redo transport services.

When transitioning the primary database to the `TRANSPORT-OFF` state, the broker turns off redo transport services to all broker-managed standbys by resetting the `LOG_ARCHIVE_DEST_STATE_` n initialization parameter. Transmission of redo data to all broker-managed standbys is stopped. Log files continue to be archived at the primary database.

If the primary database is an Oracle RAC database, the broker configures redo transport services on all primary instances with the exact same settings.

Physical Standby Database State Transitions

When transitioning a physical standby database to the `APPLY-ON` state, the broker starts Redo Apply with options specified by the Redo Apply-related properties. If the standby is an Oracle RAC database, then the broker starts Redo Apply on one standby instance, called the apply instance.

Redo Apply can be set up to run on multiple active running physical standby instances. (This feature requires the standby database to have a license for the Oracle Active Data Guard option.) If a database has already been set up to run Redo Apply on multiple instances, then you can use the Data Guard broker property `ApplyInstances` to restrict the number of instances that are involved in Redo Apply on an Oracle RAC physical standby database.

If a license for the Oracle Active Data Guard option has been purchased, a physical standby database can be open while Redo Apply is active. This capability is known as real-time query. See [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/dgbkr&id=SBYDB00706) for more details.

The apply instance must be open before starting Redo Apply if any other instance is open.

When transitioning to the `APPLY-OFF` state, the broker stops Redo Apply.

Note:

If you perform online database relocation with Oracle RAC One Node on a physical standby, then the new instance is started in the same mode as the currently running instance. Therefore, if the database is mounted on the original instance, then the database will be mounted on the new instance. Likewise, if the database is open on the original instance, then the database will be open on the new instance. This may result in the new instance starting in a mode that does not match the start option recorded with Oracle Clusterware for the database.

Logical Standby Database State Transitions

When transitioning a logical standby database to the `APPLY-ON` state, the broker will wait until the database is open, and then enable the database guard to prevent modifications to tables in the logical standby database, and start SQL Apply with options specified by the log apply-related properties. If the logical standby database is an Oracle RAC database, the broker starts SQL Apply on one standby instance, the apply instance.

When transitioning to the `APPLY-OFF` state, the broker stops SQL Apply.

See Also:

- Managing Log Apply Services for information about managing SQL Apply
- Managing Redo Transport Services for more details on managing redo transport services and a list of redo transport-related properties
- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/dgbkr&id=SBYDB4827) for information about the database guard
- [Oracle Data Guard Command-Line Interface Reference](oracle-data-guard-broker-commands.md) for complete information about the `EDIT DATABASE` command.

### Managing Database Properties

There are two types of database properties: monitorable and configurable.

Both monitorable and configurable properties can be further divided into properties having database-wide scope or instance-specific scope.

- Monitorable property values can be viewed only when the associated database is enabled.
	Monitorable properties allow you to view run-time information related to databases, but you cannot change the values of these properties.
- Configurable property values can be viewed and dynamically updated.
	Configurable properties affect the operation or configuration of the broker. You can change the value of these properties using DGMGRL or Cloud Control. You can edit properties whether the configuration and its members are enabled or disabled. However, if a configuration member is disabled, then the new property value does not take effect until you enable the configuration or member, as appropriate.
	See Also:
	[Oracle Data Guard Broker Properties](oracle-data-guard-broker-properties.md) for a detailed list of all database properties

To see these properties, you can use the DGMGRL `SHOW` command or Edit Properties page in Cloud Control. Example 4-1 uses the `SHOW DATABASE VERBOSE` command to display information about the `North_Sales` database.

See Also:

[Oracle Data Guard Command-Line Interface Reference](oracle-data-guard-broker-commands.md) for complete information about the DGMGRL command-line interface

Example 4-1 Using the SHOW DATABASE VERBOSE Command to Display Properties

```
SHOW DATABASE VERBOSE 'North_Sales';

Database - North_Sales

  Role:               PRIMARY
  Intended State:     TRANSPORT-ON
  Instance(s):
    North_sales1

  Properties:
    DGConnectIdentifier             = 'North_Sales.example.com'
    ObserverConnectIdentifier       = ''
    FastStartFailoverTarget         = ''
    PreferredObserverHosts          = ''
    LogShipping                     = 'ON'
    RedoRoutes                      = ''
    LogXptMode                      = 'ASYNC'
    DelayMins                       = '0'
    Binding                         = 'optional'
    MaxFailure                      = '0'
    ReopenSecs                      = '30'
    NetTimeout                      = '300'
    RedoCompression                 = 'DISABLE'
    PreferredApplyInstance          = ''
    ApplyInstanceTimeout            = '0'
    ApplyLagThreshold               = '0'
    TransportLagThreshold           = '0'
    TransportDisconnectedThreshold  = '0'
    ApplyParallel                   = 'AUTO'
    ApplyInstances                  = '0'
    ArchiveLocation                 = ''
    AlternateLocation               = ''
    StandbyArchiveLocation          = ''
    StandbyAlternateLocation        = ''
    InconsistentProperties          = '(monitor)'
    InconsistentLogXptProps         = '(monitor)'
    LogXptStatus                    = '(monitor)'
    SendQEntries                    = '(monitor)'
    RecvQEntries                    = '(monitor)'
    HostName                        = ’North_Sales.example.com'
    StaticConnectIdentifier         = '(DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)
(HOST=North_Sales.example.com)(PORT=2840))
(CONNECT_DATA=(SERVICE_NAME=North_Sales_DGMGRL.example.com)
(INSTANCE_NAME=north_sales1)(SERVER=DEDICATED)))'
    TopWaitEvents                   = '(monitor)'
    SidName                         = '(monitor)’

  Log file locations:
    Alert log               : /dev/oracle/log/diag/rdbms/North_Sales/north1/trace/alert_north1.log
    Data Guard Broker log   : /dev/oracle/log/diag/rdbms/North_Sales/north1/trace/drcnorth1.log

Database Status:
SUCCESS
```

#### Monitorable (Read-Only) Properties

Monitorable properties allow you to view information related to a configuration member, but you cannot change the property values.

Monitorable properties can be very helpful when you are trying to diagnose problems in the broker configuration. For example, you can view the `InconsistentLogXptProps` monitorable property to determine where there is a discrepancy in redo transport services properties between the broker configuration file and the actual value currently used by the database.

You can list all monitorable properties using the DGMGRL `SHOW DATABASE VERBOSE` command. Use the `SHOW DATABASE` command to obtain more details about a particular property. For example, the following shows the `InconsistentLogXptProps` property:

```
DGMGRL> SHOW DATABASE 'North_Sales' 'InconsistentLogXptProps';

INCONSISTENT LOG TRANSPORT PROPERTIES

 INSTANCE_NAME     STANDBY_NAME  PROPERTY_NAME  MEMORY_VALUE  BROKER_VALUE 
  south_sales1      South_Sales     ReopenSecs           600           300
```

Cloud Control displays the information obtained from these properties on the Edit Properties page.

#### Configurable (Changeable) Properties

Configurable properties affect the operation or configuration of a database or far sync instance.

When you use DGMGRL or Cloud Control to create a primary database and import existing standby databases and far sync instances into a new broker configuration, the property values are initially imported from the database or far sync instance settings.

You can update many property values when a configuration member is either disabled or enabled. When a new member is added into the configuration, the broker connects to that member and imports initial values for the member's properties from the current member settings. For example:

```
DGMGRL> SHOW DATABASE 'North_Sales' LogXptMode;
  LogXptMode = ASYNC

DGMGRL> EDIT DATABASE 'North_Sales' SET PROPERTY LogXptMode='SYNC';
  Property "LogXptMode" updated

DGMGRL> SHOW DATABASE 'North_Sales' LogXptMode;
  LogXptMode = SYNC
```

When the configuration is enabled, for properties related to redo transport, the broker keeps the member property values in the broker configuration file consistent with the values being used by the member. The broker no longer maintains values for properties related to initialization parameters in the configuration file. Note that there is no issue with maintaining consistency. Although the broker no longer maintains values for these properties, it is still possible to use the broker CLI to update and examine the value of these properties. Due to user action, it is possible for the parameter value in the system global area (SGA) to differ from the parameter value in the server parameter file. This is not flagged as an inconsistency and only means that the server parameter file value will take effect the next time the database is restarted. The specified database must be accessible to be able to make these property changes.

Note:

Even though you can change a property value when the configuration is disabled, the change does not take effect on the configuration member unless the configuration is enabled. Also note that some property values can only be changed in the disabled state.

##### Resetting Broker Configurable Properties to Default Values

Most broker configurable properties have a default value, but you can specify a different value to override it.

The broker recognizes when a default value has been restored for a property and no longer considers it a user-supplied value. This is expedient in upgrade scenarios because if a default value for a property changes between releases, then the new default value is automatically put into effect after an upgrade is complete. Values that are considered user-supplied are not automatically upgraded.

You do not need to know the actual default value in order to reset it. You can reset a default value at the configuration, configuration member, or instance level.

### Managing Redo Transport Services

To manage redo transport services, you specify configurable properties on each configuration member.

The properties you specify are as follows::

- `DGConnectIdentifier`
- `StandbyAlternateLocation`
- `Binding`
- `Encryption` (This property can be set only on a Recovery Appliance)
- `LogShipping`
- `LogXptMode`
- `MaxFailure`
- `NetTimeout`
- `RedoCompression`
- `RedoRoutes`
- `ReopenSecs`
- `StandbyArchiveLocation`

You can use these properties to specify how the broker configures redo transport services for the standby database. The actual redo transport setup, such as setting the `LOG_ARCHIVE_DEST_` n initialization parameter, is carried out by the broker on the primary database (except for the `StandbyArchiveLocation` property). If changing the property requires that you change the `LOG_ARCHIVE_DEST_` n initialization parameter attributes, the broker forces a log switch on each thread so that the new setting is adopted immediately by the primary database.

You should also preset these properties on the primary database in preparation for it to be switched over to a standby database.

#### Setting Up For Redo Transport

Redo data is transported to a standby database using Oracle Net.

An Oracle Net service name is specified with the `SERVICE` attribute of the `LOG_ARCHIVE_DEST_n` initialization parameter and is used to transmit redo data to the standby database. The Oracle Net service name is translated into a connect descriptor that contains the information necessary for connecting to the standby database.

The `SERVICE` attribute can be set or changed by using the `DGConnectIdentifier` database property. The `DGConnectIdentifier` property is set when a database is first added to the configuration. Its initial value is the connect identifier that is specified in the optional `CONNECT IDENTIFIER IS` clause of the `ADD DATABASE` command.

The `DGConnectIdentifier` property value is also used to set up the `FAL_SERVER` initialization parameter. If the `DGConnectIdentifier` property for any database is changed, the `SERVICE` attribute of the corresponding `LOG_ARCHIVE_DEST_n` initialization parameter will also be changed. In addition, the `FAL_SERVER` initialization parameter will also be updated on every enabled standby database in the configuration.

#### Managing Redo Transport Services for Data Protection Modes

As a part of the overall configuration protection mode, you must ensure that redo transport services are also properly set up for the data protection mode that you choose.

Managing Data Protection Modes describes how the broker handles data protection modes.

You use the `LogXptMode` or `RedoRoutes` database properties to set the `SYNC`, `ASYNC`, or `FASTSYNC` mode for redo transport services.

The following redo transport modes are supported:

SYNC

Configures redo transport services for this standby database using the `SYNC` and `AFFIRM` attributes of the `LOG_ARCHIVE_DEST_` n initialization parameter. This mode, along with standby redo log files, is required for configurations operating in either maximum protection mode or maximum availability mode. This redo transport service enables the highest grade of data protection to the primary database, but also can incur a higher performance impact.

ASYNC

Configures redo transport services for this standby database using the `ASYNC` and `NOAFFIRM` attributes of the `LOG_ARCHIVE_DEST_` n initialization parameter. This mode, along with standby redo log files, enables a moderate grade of protection to the primary database, and lower performance impact.

FASTSYNC

Configures redo transport services for this standby database using the `SYNC` and `NOAFFIRM` attributes of the `LOG_ARCHIVE_DEST_` `n` initialization parameter. This mode is only available in maximum availability protection mode.

#### Advanced Redo Transport Settings

You can use the `RedoRoutes` property to override the default behavior in which a primary database sends its redo to every possible redo transport destination in the configuration.

An example of redo transport topology other than the default would be one in which a physical standby or a far sync instance forwards redo received from the primary database to one or more destinations, or one in which the redo transport mode used for a given destination is dependent on which database is in the primary role.

See Also:

- [RedoRoutes](oracle-data-guard-broker-properties.md) for information about redo routing rules when you use the `RedoRoutes` property

Example 4-2 Using the RedoRoutes Property for Real-Time Cascading

Consider a configuration that has a primary database (`North_Sales`) and two physical standby databases (`Local_Sales` and `Remote_Sales`). The `Local_Sales` database is located in the same data center as the primary for high availability purposes. The `Remote_Sales` database is located in a remote data center for disaster recovery purposes. Instead of the primary having to ship its redo to both databases, it is possible to use the `RedoRoutes` property to configure real-time cascading, in which the local physical standby database forwards redo from `North_Sales` to the remote physical standby database, `Remote_Sales`. To accomplish this, the `RedoRoutes` property must be set as follows:

- On the `North_Sales` database, the `RedoRoutes` property must specify that if `North_Sales` is in the primary role, then it should ship redo to the `Local_Sales` database using synchronous transport mode. This rule prevents the primary from shipping redo data directly to the `Remote_Sales` database.
- On the `Local_Sales` database, the `RedoRoutes` property must specify that if `North_Sales` is in the primary role, then `Local_Sales` should forward redo it receives from `North_Sales` on to `Remote_Sales`.
```
DGMGRL> EDIT DATABASE 'North_Sales' SET PROPERTY 'RedoRoutes' = '(LOCAL : Local_Sales SYNC)';
DGMGRL> EDIT DATABASE 'Local_Sales' SET PROPERTY 'RedoRoutes' = '(North_Sales : Remote_Sales ASYNC)';
```

To see the runtime `RedoRoutes` configuration, use the `SHOW` `CONFIGURATION` command. For example:

```
DGMGRL> SHOW CONFIGURATION;
 
Configuration - Sales_Configuration
 
  Protection Mode: MaxAvailability
  Members:
  North_Sales  - Primary database
    Local_Sales  - Physical standby database
      Remote_Sales  - Physical standby database (receiving current redo)
 
Fast-Start Failover: DISABLED
 
Configuration Status:
SUCCESS
```

Note that the `ASYNC` redo transport attribute was explicitly specified in the redo route rule for the `Remote_Sales` destination to enable real-time cascading of redo to that destination. (Real-time cascading requires a license for the Oracle Active Data Guard option.)

To disable real-time cascading of redo, do not specify the `ASYNC` redo transport attribute. For example:

```
DGMGRL> EDIT DATABASE 'Local_Sales' SET PROPERTY 'RedoRoutes' = '(North_Sales : Remote_Sales)';
```

Example 4-3 Using the RedoRoutes Property for Remote Alternate Destinations

The `RedoRoutes` property can also be used to set up a remote alternate destination so that a terminal member can still receive redo data even if the member from which it was receiving the redo data fails. Using the previous example, it would be possible to have the primary database, `North_Sales`, send redo data directly to `Remote_Sales` if the `Local_Sales` standby database failed. It is also possible, using the `PRIORITY` attribute, to set it up so that once the `Local_Sales` failure has been resolved it can resume shipping redo to `Remote_Sales`.

```
DGMGRL> EDIT DATABASE 'North_Sales' SET PROPERTY 'RedoRoutes' = '(LOCAL : ( Local_Sales ASYNC PRIORITY=1, Remote_Sales ASYNC PRIORITY=2 ))';
Property "RedoRoutes" updated

DGMGRL> EDIT DATABASE 'Local_Sales' SET PROPERTY 'RedoRoutes' = '(North_Sales : Remote_Sales ASYNC)';
Property "RedoRoutes" updated

DGMGRL> SHOW CONFIGURATION;

Configuration - Sales_Configuration

  Protection Mode: MaxPerformance
  Members:
  North_Sales    - Primary database
    Local_Sales  - Physical standby database
      Remote_Sales - Physical standby database
Fast-Start Failover: DISABLED

Configuration Status:
SUCCESS
```

To see the full `RedoRoutes` configuration, use the `SHOW` `CONFIGURATION` `VERBOSE` command. For example:

```
DGMGRL> SHOW CONFIGURATION VERBOSE;

Configuration - Sales_Configuration

  Protection Mode: MaxPerformance
  Members:
    North_Sales - Primary database
      Local_Sales - Physical standby database
        Remote_Sales - Physical standby database
      Remote_Sales - Physical standby database (alternate of Local_Sales)

  Properties:
    FastStartFailoverThreshold      = '180'
    OperationTimeout                = '30'
    TraceLevel                      = 'USER'
    FastStartFailoverLagLimit       = '300'
    CommunicationTimeout            = '180'
    ObserverReconnect               = '0'
    FastStartFailoverAutoReinstate  = 'TRUE'
    FastStartFailoverPmyShutdown    = 'TRUE'
    BystandersFollowRoleChange      = 'ALL'
    ObserverOverride                = 'FALSE'
    ExternalDestination1            = ''
    ExternalDestination2            = ''
    PrimaryLostWriteAction          = 'CONTINUE'
    ConfigurationWideServiceName    = 'c0_CFG'

Fast-Start Failover: DISABLED

Configuration Status:
SUCCESS
```

#### Turning Redo Transport Services On and Off

You turn redo transport services on and off by setting the state of the primary database.

Setting the primary database state to `TRANSPORT-ON` starts redo transport services at the primary database, and setting the primary database state to `TRANSPORT-OFF` stops redo transport services at the primary database.

Note:

Oracle does not recommend turning off redo transport services to all standby databases. This increases the risk of data loss if the primary database fails.

Turn redo transport services on and off to an individual standby database using the `LogShipping` database property on the standby database. The `LogShipping` property accepts values `ON` and `OFF`. If you set the `LogShipping` property to `OFF` for a standby database, redo transport services to this standby database are turned off, while redo transport services to other databases are not affected. You can set `LogShipping` to `ON` to turn back on redo transport services to the standby database.

The relationship between setting the primary database state and setting the `LogShipping` property is as follows:

- If the primary database state is set to `TRANSPORT-OFF`, redo transport services to all the standby databases are stopped regardless of the `LogShipping` property values of the individual standby databases.
- If the primary database state is set to `TRANSPORT-ON`, redo transport services to each standby database are determined by the `LogShipping` property of that database.

Example 4-4 and Example 4-5 show how to turn off redo transport services in two different scenarios.

Example 4-4 Turn Off Redo Transport Services to All Standby Databases

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

Example 4-5 Turn Off Redo Transport Services to a Specific Standby Database

```
DGMGRL> EDIT DATABASE 'South_Sales' SET PROPERTY 'LogShipping'='OFF';
Property "LogShipping" updated

DGMGRL> SHOW DATABASE 'South_Sales' 'LogShipping';
  LogShipping = 'OFF'
```

#### Specifying Locations for Archived Redo Log Files

You can use broker configurable properties to set up locations to store both archived standby redo log files and archived online redo log files.

For online redo log files, use the `ArchiveLocation` and `AlternateLocation` properties on a primary, logical, or snapshot standby database.

For standby redo log files, use the `StandbyArchiveLocation` and `StandbyAlternateLocation` properties on a standby database. If the `StandbyArchiveLocation` is not set, `ArchiveLocation` or `AlternateLocation` specify the archiving location for both of online and standby redo log files. If `StandbyArchiveLocation` is set, `ArchiveLocation` and `AlternateLocation` specify the archiving location for online redo log files.

The `StandbyArchiveLocation` property specifies a location to store archived redo log files. The broker uses the location to store only archived redo log files received from the primary database. For archived redo log files generated locally when the database is either the primary database, a logical standby database, or a snapshot standby database, you need to specify the `ArchiveLocation` property. The broker allows the value of the `StandbyArchiveLocation` and `ArchiveLocation` properties to be the same as the location you set up for locally generated logs, in which case the broker sets up the `VALID_FOR` attribute of the destination appropriately so that it can be used for both the archived redo log files received from the primary database and archived redo log files generated locally. When a location is used for both online and standby redo log files, you must configure the `ArchiveLocation` property to the shared location and leave the `StandbyArchiveLocation` property empty.

You can also set up an alternate location to store archived redo log files by using the `StandbyAlternateLocation` and `AlternateLocation` properties. The alternate locations specified by these properties are where the archived redo log files are stored if the original archive location (specified by `StandbyArchiveLocation` or `Archivelocation`) fails. The broker sets up the alternate location properly using the `ALTERNATE` attribute of the `LOG_ARCHIVE_DEST_n` initialization parameter.

Note:

You can use the database recovery area to store archived redo log files on the standby. In such a case, the value of the `StandbyArchiveLocation` or `ArchiveLocation` properties can be set to `USE_DB_RECOVERY_FILE_DEST`.

If you are not using a database recovery area, then on a logical standby database Oracle recommends that the `ArchiveLocation` property be different from the value of the `StandbyArchiveLocation` property.

Example 4-6 Using the Same Archiving Location for Standby Redo Log Files and Online Redo Log Files

The following example uses the same archiving location for online redo log files and standby redo log files.

```
ArchiveLocation='/archfs/arch'
```

Example 4-7 Specifying an Alternate Location for Archived Standby and Online Redo Log Files

The following example uses the same archiving location for online redo log files and standby redo log files. Configuring the `AlternateLocation` property ensures that a shared, alternate, location is available to store standby redo log files if the location specified by the `ArchiveLocation` property is unavailable.

```
ArchiveLocation='/archfs/arch'
AlternateLocation='/archfs/alt'
```

Example 4-8 Specifying Separate Archiving Locations for Online and Standby Redo Log Files

This example configures separate archiving locations for standby redo log files and online redo log files. Also, alternate archiving locations are configured for the online and standby redo log files by using the `AlternateLocation` and `StandbyAlternateLocation` properties respectively

```
ArchiveLocation='/archfs/arch/online'
AlternateLocation='/archfs/alt/online'
StandbyArchiveLocation='/archfs/arch/standby'
StandbyAlternateLocation='/archfs/alt/standby'
```

#### Other Redo Transport Settings

You can use database properties to tune the performance of redo transport services and to set up redo transport services failure policies.

The properties used are: `Binding`, `MaxFailure`, `NetTimeout`, `RedoCompression`, and `ReopenSecs` . These properties correspond to attributes on the `LOG_ARCHIVE_DEST_` n initialization parameter.

See Also:

[Oracle Data Guard Broker Properties](oracle-data-guard-broker-properties.md) for complete information about these database properties

#### Redo Transport Services in an Oracle RAC Database Environment

If the primary database is an Oracle RAC database, the broker ensures that redo transport services are set up identically on each of the primary database instances.

Each instance has the same remote destinations, and for each remote destination, all instances are set up the same in terms of redo transport service, performance related settings, local archival of the online redo logs, and so on. If an instance has different settings, the broker raises a health check warning on that particular instance

Settings relative to redo transport services are saved in the broker configuration file as properties. When you update a redo transport-related property on a standby database, the corresponding change is also made automatically by the broker to the `LOG_ARCHIVE_DEST_` n initialization parameter on all of the primary database instances. If a new instance comes up on the primary database, the broker sets up redo transport services for the new instance using the redo transport-related properties of all the configuration members currently being managed by the broker. After the new instance is opened for activity, all archived redo log files generated on this instance begin to transmit to members of the configuration.

See also:

[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/dgbkr&id=SBYDB01100) for additional information about the `LOG_ARCHIVE_DEST_` n initialization parameter

#### Transport Lag

Transport lag is a measure of the degree to which the transport of redo to a standby database or far sync instance lags behind the generation of redo on the primary database.

If there are one or more redo gaps on a standby database or far sync instance, then the transport lag is calculated as if no redo has been received after the beginning of the earliest redo gap.

Both Cloud Control and the DGMGRL client display the redo transport lag for each managed standby or far sync instance. Cloud Control displays the transport lag on the Oracle Data Guard home page. The DGMGRL client displays the transport lag in the `SHOW         DATABASE` output. There is no transport lag displayed for a primary database. Here is an example of the transport lag for a physical standby database:

```
DGMGRL> show database 'South_Sales';
 
Database - South_Sales
 
  Role:            PHYSICAL STANDBY
  Intended State:  APPLY-ON
  Transport Lag:   0 seconds (computed 0 seconds ago)
  Apply Lag:       0 seconds (computed 0 seconds ago)
  Apply Rate:      255.00 KByte/s
  Real Time Query: OFF
  Instance(s):
    south_sales1
 
Database Status:
SUCCESS
```

Starting with Oracle Database Release 19c, the `SHOW CONFIGURATION LAG` command displays a summary of the broker configuration and the transport lag of all standby databases.

The transport lag can help you identify any problems that may exist with the redo transport services.

You can set the `TransportLagThreshold` database configurable property to generate a health check warning when the transport of redo data to a standby database or far sync instance lags behind the generation of redo data on the primary database.

The following command sets the `TransportLagThreshold` property to 15 seconds:

```
DGMGRL> EDIT DATABASE 'South_Sales' SET PROPERTY 'TransportLagThreshold'=15;
Property TransportLagThreshold updated
```

Additionally, you can set the `TransportDisconnectedThreshold` database configurable property to generate a health check warning if a standby or far sync instance finds that it has not had any redo transport-related communication with the primary database. The property has a default value of 30 seconds.

The following command sets the `TransportDisconnectedThreshold` property to 15 seconds:

```
DGMGRL> EDIT DATABASE 'South_Sales' SET PROPERTY 'TransportDisconnectedThreshold'=15;
Property TransportDisconnectedThreshold updated
```

### Managing Redo Transport Services for Recovery Appliance

Redo transport services for a Zero Data Loss Recovery Appliance (Recovery Appliance) are managed in the same way as for a standby database.

You can use the broker to manage redo transport services to a Recovery Appliance from any member in the configuration. For example, to add a Recovery Appliance to a broker configuration and then enable it, you would take the following steps:

1. Add the Recovery Appliance to the broker configuration.
	```
	DGMGRL> ADD RECOVERY_APPLIANCE EnterpriseRecoveryAppliance AS CONNECT IDENTIFIER IS
	EnterpriseRecoveryAppliance.example.com;
	Oracle Recovery Appliance "EnterpriseRecoveryAppliance" added
	 
	DGMGRL> SHOW RECOVERY_APPLIANCE 'EnterpriseRecoveryAppliance';
	 Oracle Recovery Appliance - EnterpriseRecoveryAppliance
	   Transport Lag: 0 seconds
	  Redo Source: North_Sales
	 
	Oracle Recovery Appliance Status:
	DISABLED
	```
2. ```
	DGMGRL> ENABLE RECOVERY_APPLIANCE 'EnterpriseRecoveryAppliance';
	 
	DGMGRL> SHOW RECOVERY_APPLIANCE 'EnterpriseRecoveryAppliance';
	 Oracle Recovery Appliance - EnterpriseRecoveryAppliance
	   Transport Lag: 0 seconds
	  Redo Source: North_Sales
	 
	Oracle Recovery Appliance Status:
	SUCCESS
	```
3. Set the `TransportLagThreshold` database configurable property to generate a health check warning when the transport of redo data to the Recovery Appliance lags behind the generation of redo data on the source database. This step is optional, but if you do not specify a transport lag threshold, then the default value of 30 seconds is used and a warning is generated if a transport lag exceeds 30 seconds.
	The following command sets the `TransportLagThreshold` property to 15 seconds:
	```
	DGMGRL> EDIT RECOVERY_APPLIANCE 'EnterpriseRecoveryAppliance'
	SET PROPERTY 'TransportLagThreshold'=15;
	Property TransportLagThreshold updated
	```

Example 4-9 Setting Up Redo Transport From a Physical Standby To a Recovery Appliance

Consider a configuration that has a primary database (`North_Sales`) a physical standby database (`South_Sales`), and a Recovery Appliance (`EnterpriseRecoveryAppliance`). Instead of the primary having to ship its redo to both the standby and the Recovery Appliance, you can set up the `RedoRoutes` property so that the primary sends redo only to the physical standby, and the physical standby then forwards that redo to the Recovery Appliance. To accomplish this, the `RedoRoutes` property must be set as follows:

- On the `North_Sales` database, the `RedoRoutes` property must specify that if `North_Sales` is in the primary role, then it should ship redo to the `South_Sales` database using synchronous transport mode. This rule prevents the primary from shipping redo data directly to the Recovery Appliance, `EnterpriseRecoveryAppliance`.
- On the `South_Sales` database, the `RedoRoutes` property must specify that if `North_Sales` is in the primary role, then `South_Sales` should forward redo it receives from `North_Sales` on to `EnterpriseRecoveryAppliance`.
```
DGMGRL> EDIT DATABASE 'North_Sales' SET PROPERTY 'RedoRoutes' = '(LOCAL : South_Sales SYNC)';
DGMGRL> EDIT DATABASE 'South_Sales' SET PROPERTY 'RedoRoutes' = '(North_Sales : EnterpriseRecoveryAppliance ASYNC)';
```

Note that the `ASYNC` redo transport attribute was explicitly specified in the redo route rule for the `EnterpriseRecoveryAppliance` destination to enable real-time cascading of redo to that destination.

Once a Recovery Appliance has been added to a broker configuration, it can receive redo from either the primary database or a standby database. Example 4-9 shows how to set up a Recovery Appliance to receive redo from a physical standby database.

See Also:

- Managing Redo Transport Services for information about managing redo transport services

### Managing Log Apply Services

You can manage Redo Apply and SQL Apply on physical and logical standby databases by using database properties related to log apply.

The database properties related to log apply are as follows:

- Properties common to Redo Apply and SQL Apply
	- `ApplyInstanceTimeout`
		- `DelayMins`
		- `PreferredApplyInstance`
- Properties specific to Redo Apply
	- `ApplyParallel`
		- `ApplyInstances`

There are some properties related to SQL Apply that, if changed, may require a restart of SQL Apply if the current database state is `APPLY-ON`. See the information in [Oracle Data Guard Broker Properties](oracle-data-guard-broker-properties.md) about properties related to SQL Apply, to determine which ones require SQL Apply to be restarted.

If the current database state is `APPLY-OFF`, the property changes will take effect the next time the database state is changed to `APPLY-ON`.

#### Managing Delayed Apply

You can set up Apply Services so that the application of redo to the standby database is delayed.

This allows the standby database to lag behind the primary database, and if a user error (for example, dropping a table) occurs during this window of time, the standby database will still contain the correct data that can be transmitted back to the primary database to repair the data.

By default, no delay is configured and the redo data is applied on a standby database as soon as possible. If the standby database has standby redo logs configured, the broker will enable real-time apply. When Redo Apply and SQL Apply apply redo in real time, the redo data is recovered directly from the standby redo log files as they are being filled. This means that the standby database does not have to wait for the log files to be archived before applying redo data from the archived redo log files. This minimizes the transactional lag between the primary and the standby.

Use the `DelayMins` database property to specify the number of minutes that log apply services must wait before applying redo data to the standby database. Note that only log apply services on the standby database are delayed. Redo transport services on the primary database are not delayed, thus the primary database data is still well protected by the standby database.

Caution:

Because the broker automatically enables real-time apply on standby databases, Oracle recommends that you configure all databases to use Flashback Database.

#### Managing Parallel Apply with Redo Apply

For Redo Apply, you can configure whether multiple parallel processes are used to apply redo data received from the primary database by using the `ApplyParallel` database property.

Parallelism is enabled by default, which means Redo Apply automatically chooses the optimal number of parallel processes based on the number of CPUs in the system. (This is equivalent to setting the `ApplyParallel` property to `AUTO`.) You can disable parallelism by setting the `ApplyParallel` property to `NO`.

Note:

Parallel Redo Apply is different from multi-instance Redo Apply. Parallel Redo Apply means that there are multiple Redo Apply slaves per instance; this value is set using the broker `ApplyParallel` property. Multi-instance Redo Apply means that there are multiple instances running Redo Apply; this value is set with the broker `ApplyInstances` property. The two properties can be used together to control the Redo Apply slaves on each instance on which apply is running in multi-instance apply. The number of parallel slaves specified by the `ApplyParallel` property will be the same on each instance in a multi-instance apply configuration.

See Also:

[ApplyParallel](oracle-data-guard-broker-properties.md)

[ApplyInstances](oracle-data-guard-broker-properties.md)

#### Managing Multi-Instance Redo Apply

For Redo Apply in an Oracle RAC database, you can configure the number of instances that can be engaged in recovery by means of the `ApplyInstances` property value.

By default, only one instance is involved in recovery activity. However, the `ApplyInstances` property can be set to indicate a specific number of instances or the value `ALL`, to indicate all instances. When recovery is started, it checks to see if enough instances as configured are available to start recovery on. If not, then broker delays starting recovery for one minute to allow other instances to start up and then starts recovery.

During periodic health checks, broker checks to see if more instances have started that could potentially be engaged in recovery. If so, then broker stops and restarts recovery to engage the additional instances.

Changing the value of the `ApplyInstances` property value results in recovery being restarted with the new values.

All instances must be in the same state (open or mounted) to be able to engage that instance in recovery.

#### Apply Services in an Oracle RAC Database Environment

When a standby database is an Oracle RAC database, SQL Apply and Redo Apply make use of an apply instance.

SQL Apply can run on only one instance of an Oracle RAC database at any time. This instance is called the apply instance.

Redo Apply can run on all instances of an Oracle RAC database at the same time, but only one of the instances is the apply coordinator and that is the instance that the broker considers to be the apply instance. This feature requires that the `ApplyInstances` database configurable property (valid only on physical standby databases) be set to a non-zero value. See [ApplyInstances](oracle-data-guard-broker-properties.md).

If the apply instance fails, then the broker automatically restarts SQL Apply, or the Redo Apply coordinator, as appropriate, on a different instance. This is called apply instance failover (see Apply Instance Failover).

##### Selecting the Apply Instance

If you have no preference which instance is to be the apply instance in an Oracle RAC standby database, the broker randomly picks an apply instance. If you want to select a particular instance as the apply instance, there are two methods to do so.

Note:

The information in this section is not applicable to snapshot standby databases or far sync instances.

- The first method is to set the value of the `PreferredApplyInstance` database property to the name of the instance (see the `InstanceName` property) you want to be the apply instance. The broker starts log apply services on that instance if no apply instance is yet selected in the Oracle RAC standby database. This could be the case before you enable the standby database for the first time, or if the apply instance just failed and the broker is about to do an apply instance failover, or if the Oracle RAC database is currently the primary and you want to specify its apply instance in preparation for a switchover. Once the apply instance is selected and, as long as the apply instance is still running, the broker disregards the value of the `PreferredApplyInstance` property even if you change it.
- The second method is to change the apply instance when the apply instance is already selected and is running. To change the apply instance, issue the DGMGRL `SET STATE` command to set the standby database state to `APPLY-ON`, with a specific apply instance argument. The `SET STATE` command will update the `PreferredApplyInstance` property to the new apply instance value, and then move log apply services to the new instance. For example, use DGMGRL `SHOW` command to show the available instances for the standby database, then issue the `EDIT DATABASE` command to move log apply services to the new instance:
	```
	DGMGRL> SHOW DATABASE 'South_Sales'
	 
	Database - South_Sales
	 
	  Role:            PHYSICAL STANDBY
	  Intended State:  APPLY-ON
	  Transport Lag:   0 seconds (computed 1 second ago)
	  Apply Lag:       0 seconds (computed 1 second ago)
	  Apply Rate:      1017.00 KByte/s
	  Real Time Query: OFF
	  Instance(s):
	    south_sales1   (apply instance)
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
	  Transport Lag:   0 seconds (computed 1 second ago)
	  Apply Lag:       0 seconds (computed 1 second ago)
	  Apply Rate:      1017.00 KByte/s
	  Real Time Query: OFF
	  Instance(s):
	    south_sales1
	    south_sales2   (apply instance)
	 
	Database Status:
	SUCCESS
	```

Ensure that the new apply instance is running when the command is issued. Otherwise, the apply instance remains the same.

Once the apply instance is selected, the broker keeps apply instance information in the broker configuration file so that even if the standby database is shut down and restarted, the broker still selects the same instance to start log apply services. The apply instance remains unchanged until changed by the user or it fails for any reason and the broker decides to do an apply instance failover.

##### Apply Instance Failover

To tolerate a failure of the apply instance, the broker leverages the availability of the Oracle RAC standby database by automatically failing over log apply services to a different standby instance.

The apply instance failover capability provided by the broker enhances data protection.

To set up apply instance failover, set the `ApplyInstanceTimeout` database property to specify the time period that the broker will wait after detecting an apply instance failure and before initiating an apply instance failover. To select an appropriate timeout value, you need to consider:

- If there is another mechanism in the cluster (such as Oracle Clusterware) that will try to recover the failed apply instance.
- How long your business can tolerate not applying redo data on the standby database.
- The overhead associated with moving the log apply services to a different instance.

The broker default value of the `ApplyInstanceTimeout` property is 0 seconds, indicating that apply instance failover should occur immediately upon detection of the failure of the current apply instance.

After the broker initiates an apply instance failover, the broker selects a new apply instance according to the following rule: if the `PreferredApplyInstance` property indicates an instance that is currently running, select it as the new apply instance; otherwise pick a random instance that is currently running to be the new apply instance.

In addition, if the physical standby database was operating in real-time query mode when the apply instance failed, then after Oracle recovery cleanup is completed, the broker opens any instances that had been automatically closed. If the failed apply instance was the only instance open, then the instance chosen as the new apply instance is opened before starting apply services so that real-time query is once again in effect.

See Also:

- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/dgbkr&id=SBYDB00707) for more information about real-time query mode
- The My Oracle Support note 1357597.1 at [`http://support.oracle.com`](http://support.oracle.com/) for additional information about apply instance failures in an Oracle Active Data Guard Oracle RAC standby

#### Apply Lag

Apply lag is a measure of the degree to which the data in a standby database lags behind the data in the primary database, due to delays in propagating and applying the redo.

Both Cloud Control and the DGMGRL client display the apply lag for each managed standby database. Cloud Control displays the apply lag on the Oracle Data Guard home page. The DGMGRL client displays the apply lag in the `SHOW DATABASE` output. There is no apply lag displayed for a primary database or far sync instance. For example:

```
DGMGRL> SHOW DATABASE 'South_Sales';
Database - South_Sales
 
  Role:            PHYSICAL STANDBY
  Intended State:  APPLY-ON
  Transport Lag:   0 seconds (computed 0 seconds ago)
  Apply Lag:       0 seconds (computed 0 seconds ago)
  Apply Rate:      255.00 KByte/s
  Real Time Query: OFF
  Instance(s):
    south_sales1
 
Database Status:
SUCCESS
```

Starting with Oracle Database Release 19c, the `SHOW CONFIGURATION LAG` command displays a summary of the broker configuration and the apply lag of all standby databases.

The apply lag can help you identify any problems that may exist with both the redo transport services and the log apply services.

You can set the `ApplyLagThreshold` database configurable property to generate a health check warning when a standby database or far sync instance lags behind the data in the primary database.

The following command sets the `ApplyLagThreshold` property to 15 seconds:

```
DGMGRL> EDIT DATABASE 'South_Sales' SET PROPERTY 'ApplyLagThreshold'=15;
Property ApplyLagThreshold updated
```

### Managing Data Protection Modes

You can use the broker to set up a configuration having any of the different data protection modes.

The available modes of data protection are: maximum protection, maximum availability, and maximum performance.

This section contains the following topics to help you configure the proper protection for your configuration:

- Setting the Protection Mode for Your Configuration
- How the Protection Modes Influence Broker Operations

#### Setting the Protection Mode for Your Configuration

These are the steps for setting the protection mode for your configuration.

- Setting the Protection Mode Task 1: Determine Which Data Protection Mode You Want to Use
- Setting the Protection Mode Task 2: Set up standby redo log files
- Setting the Protection Mode Task 3: Set the redo transport mode
- Setting the Protection Mode Task 4: Using DGMGRL or Cloud Control

##### Setting the Protection Mode Task 1: Determine Which Data Protection Mode You Want to Use

Each data protection mode provides a different balance of data protection, data availability, and database performance.

To select the data protection mode that meets the needs of your business, carefully consider your data protection requirements and the performance expectations of your users.

Note:

Maximum protection mode cannot be used in the following situations:

- If the only standby database in a configuration is a snapshot standby
- If a far sync instance is the only configuration member receiving redo in synchronous mode from the primary database

Maximum Availability

This protection mode provides the highest level of data protection that is possible without compromising the availability of a primary database. Transactions do not commit until all redo data needed to recover those transactions has been written to the online redo log and to the standby redo log on at least one synchronized standby database or far sync instance. If the primary database cannot write its redo stream to at least one synchronized standby database, it operates as if it were in maximum performance mode to preserve primary database availability until it is again able to write its redo stream to a synchronized standby database or far sync instance.

This mode ensures that no data loss will occur if the primary database fails, but only if a second fault does not prevent a complete set of redo data from being sent from the primary database to at least one standby database.

You can enable fast-start failover if the protection mode is maximum availability.

Maximum Performance

This protection mode provides the highest level of data protection that is possible without affecting the performance of a primary database. This is accomplished by allowing transactions to commit as soon as all redo data generated by those transactions has been written to the online log. Redo data is also written to one or more standby databases, but this is done asynchronously with respect to transaction commitment, so primary database performance is unaffected by delays in writing redo data to the standby database(s).

This protection mode offers slightly less data protection than maximum availability mode and has minimal impact on primary database performance.

This is the default protection mode.

You can enable fast-start failover if the protection mode is maximum performance.

Maximum Protection

This protection mode ensures that no data loss will occur if the primary database fails. To provide this level of protection, the redo data needed to recover a transaction must be written to both the online redo log and to the standby redo log on at least one synchronized standby database before the transaction commits. To ensure that data loss cannot occur, the primary database will shut down, rather than continue processing transactions, if it cannot write its redo stream to at least one synchronized standby database.

Transactions on the primary are considered protected as soon as Oracle Data Guard has written the redo data to persistent storage in a standby redo log file. Once that is done, acknowledgment is quickly made back to the primary database so that it can proceed to the next transaction. This minimizes the impact of synchronous transport on primary database throughput and response time. To fully benefit from complete Oracle Data Guard validation at the standby database, be sure to operate in real-time apply mode so that redo changes are applied to the standby database as fast as they are received. Oracle Data Guard signals any corruptions that are detected so that immediate corrective action can be taken.

Because this data protection mode prioritizes data protection over primary database availability, Oracle recommends that a minimum of two standby databases be used to protect a primary database that runs in maximum protection mode to prevent a single standby database failure from causing the primary database to shut down. If only one standby database is supporting maximum protection mode, Oracle Data Guard broker will disallow the shutdown of the apply instance. This prevents the primary database from shutting down.

You can enable fast-start failover if the protection mode is maximum protection.

See Also:

- [Fast-Start Failover](using-data-guard-broker-to-manage-switchovers-failovers.md) for information on fast-start failover
- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/dgbkr&id=SBYDB00439) for complete information about data protection modes

##### Setting the Protection Mode Task 2: Set up standby redo log files

You must add standby redo log files on all standby databases, regardless of the protection mode you are using.

Also, Oracle requires that you add standby redo log files on the primary database in preparation for a future switchover or failover. Standby redo log files are required on the primary database if you want to enable fast-start failover.

Cloud Control automatically prompts you to select one or more standby databases in the configuration and sets up standby redo log (SRL) files on them and on the primary database in preparation for a future role change.

See Also:

If you are using the DGMGRL command-line interface, follow the instructions in [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/dgbkr&id=SBYDB00426) to configure standby redo log files.

##### Setting the Protection Mode Task 3: Set the redo transport mode

If the data protection mode requires that you change the redo transport mode used by any of the standby databases, then either change the `LogXptMode` database property on each standby database, or set the `RedoRoutes` property on the primary database or on the far sync instance that is directly connected to the standby database.

See Managing Redo Transport Services for more information about setting the redo transport service. Table 4-2 shows the protection modes and the corresponding redo transport service.

Cloud Control automatically specifies the correct redo transport service on the primary database in preparation for a future switchover.

Table 4-2 Oracle Data Guard Protection Modes and Requirements

| Protection Mode | Redo Transport | Standby Redo Log Files Needed? | Usable with Fast-Start Failover? |
| --- | --- | --- | --- |
| `MAXPROTECTION` | `SYNC` | Yes | Yes |
| `MAXAVAILABILITY` | `SYNC`, `FASTSYNC` | Yes | Yes <sup>Foot 1</sup> |
| `MAXPERFORMANCE` | `ASYNC` | Yes | Yes |

<sup>Footnote 1</sup>

Because `FASTSYNC` transport mode uses the `NOAFFIRM` attribute of the `LOG_ARCHIVE_DEST_n` parameter, data loss is possible. This means that a fast-start failover cannot be initiated when `FASTSYNC` is used and the standby is missing redo data.

##### Setting the Protection Mode Task 4: Using DGMGRL or Cloud Control

These steps describe how to set the protection mode using DGMGRL commands or Cloud Control.

With DGMGRL:

1. Use the `EDIT DATABASE (property)` command and specify the standby database whose redo transport service should be changed to correspond to the protection mode you plan to set. For example, if you plan to set the overall Oracle Data Guard configuration to operate in maximum availability mode, you must use the `EDIT DATABASE` command to set the `SYNC` mode for redo transport services. For example:
	```
	DGMGRL> EDIT DATABASE 'South_Sales' SET PROPERTY LogXptMode='SYNC';
	```
	Do this also for the primary database or another standby database in the configuration to ensure that it can support the chosen protection mode after a switchover.
	You could also use the `RedoRoutes` property, as follows:
	```
	EDIT DATABASE 'North_Sales' SET PROPERTY RedoRoutes = '(LOCAL : South_Sales SYNC)';
	```
2. Use the `EDIT CONFIGURATION SET PROTECTION MODE AS ` `protection-mode` command to set the overall configuration protection mode. For example:
	```
	DGMGRL> EDIT CONFIGURATION SET PROTECTION MODE AS MAXAVAILABILITY;
	```

See [Scenario 4: Setting the Configuration Protection Mode](examples-using-data-guard-broker-DGMGRL-utility.md) for a DGMGRL scenario showing how to set the protection mode.

With Cloud Control:

1. On the Oracle Data Guard overview page, click the link to the right of the Protection Mode label.
2. Select Maximum Protection, Maximum Availability, or Maximum Performance and click Continue.
3. If prompted, log in to the database with `SYSDG` or `SYSDBA` privileges and click Login.
4. Select one or more standby databases to support the protection mode that you selected. If standby redo log files are needed, verify the names of the log files. Click OK.
5. On the Confirmation page, click Yes.

The broker does not allow the protection mode to be directly upgraded from maximum performance mode to maximum protection mode. You must first change from maximum performance to maximum availability, and then to maximum protection.

#### How the Protection Modes Influence Broker Operations

These topics describe how an Oracle Data Guard configuration's protection mode and redo transport services can affect operations such as switchovers, failovers, and disabling or enabling the configuration.

This section This section contains the following sections:

- Upgrading or Downgrading the Current Protection Mode
- Switchover Operations
- Failover Operations
- Disable and Enable Operations
- Requirements For Removing a Database from the Configuration
- Requirements On Other Operations

##### Upgrading or Downgrading the Current Protection Mode

No restart is necessary when you upgrade the current Oracle Data Guard protection mode to maximum availability or when you downgrade the current Oracle Data Guard protection mode.

Follow these recommendations when upgrading or downgrading the Oracle Data Guard protection mode:

- When upgrading the protection mode, upgrade the redo transport service before you upgrade the overall protection mode. At the time when you change the protection mode or reset the redo transport service of a standby database, the broker verifies that there is at least one standby database in the configuration that can support the desired grade of protection. If not, then the broker does not change the protection mode and returns an error.
- When downgrading the protection mode, downgrade the protection mode first and then change the redo transport service (if necessary). The broker will disallow a change of the redo transport service if doing so invalidates the current overall protection mode.

If you upgrade the protection mode from the maximum performance mode, the broker ensures that there is at least one standby database that receives redo via the `SYNC` transport, either directly or through a far sync instance. Additionally, for upgrades to maximum protection mode, the broker ensures there are no gaps in the redo data on the standby database. If there are no standby databases in the configuration that meet these requirements, the request to upgrade the protection mode is rejected with an error.

Starting with Oracle Database Release 21c, you can upgrade the protection mode to maximum availability even if the primary does not have any `SYNC` standbys.

The protection mode cannot be changed if fast-start failover is enabled. An exception to this is that a downgrade to maximum availability mode is allowed when fast-start failover has been enabled in maximum protection mode.

##### Switchover Operations

A switchover does not change the overall Oracle Data Guard protection mode. The protection mode remains the same as it was before the switchover.

This requires that there be a standby database that is properly configured to support the current protection mode once the switchover completes. This can be either another standby database in the configuration or the current primary database that will become a standby database after the switchover completes.

Before you perform a switchover, if necessary you can add standby redo log files and set the redo transport properties on the current primary database, or on another standby database in the configuration, to the transport mode that is required to support the Oracle Data Guard protection mode. Then, when the switchover begins:

- The broker verifies the presence of standby redo log files and the redo transport service setting on each standby database and on the current primary database.
- The broker verifies there are no gaps in the redo data present on the target standby database.

If the verification is successful, the switchover continues; otherwise, the switchover fails, and the database roles and the broker configuration files remain unchanged.

WARNING:

- If the target of the switchover is a physical standby database, then the broker shuts down and restarts the primary database.

See Also:

[Switchover](using-data-guard-broker-to-manage-switchovers-failovers.md) for more information about switchovers

##### Failover Operations

After you perform a manual failover, the Oracle Data Guard protection mode is downgraded to maximum performance mode if the protection mode was at maximum protection. You can upgrade the protection mode later, if necessary. If the protection mode was at maximum availability or maximum performance, it remains unchanged. The redo transport services of the standby databases remain unchanged.

If fast-start failover occurs, the broker preserves the protection mode that was in effect just prior to the fast-start failover. If the protection mode was maximum protection, then the configuration protection mode is preserved, but the new primary database is set to maximum availability to allow the instance to open. When a standby becomes available that supports maximum protection mode (either because the old primary database was reinstated or due to the presence of another standby in the configuration), the database protection mode is elevated to match the configuration protection mode of maximum protection.

See Also:

[Manual Failover](using-data-guard-broker-to-manage-switchovers-failovers.md) and [Fast-Start Failover](using-data-guard-broker-to-manage-switchovers-failovers.md) for more information about manual failover and fast-start failover, respectively

##### Disable and Enable Operations

When you disable broker management of a standby database, the broker checks to see if the overall protection mode can still be satisfied by any of the remaining standby databases. If not, the broker rejects the disable operation. Otherwise, the broker allows the disable operation to proceed as long as fast-start failover is not enabled. If it is enabled, the broker allows the disable operation to proceed only if the standby database is not the target standby database for fast-start failovers.

WARNING:

If you disable broker management of a standby database in the broker configuration, that standby database cannot be used by the broker as a failover target in the event of loss of the primary database.

As long as fast-start failover is not enabled, you can disable the entire configuration regardless of the protection mode. You cannot disable the configuration if fast-start failover is enabled. See [Restrictions When Fast-Start Failover is Enabled](using-data-guard-broker-to-manage-switchovers-failovers.md) for more information.

When enabling broker management of the entire configuration, the broker first checks to see if the protection mode will be satisfied by the redo transport settings of the standby databases that will be enabled. If not, the enable operation fails and the configuration remains disabled. Otherwise, the enable operation successfully enables the configuration, and the broker enables the database using the settings saved in the broker configuration file.

##### Requirements For Removing a Database from the Configuration

When removing a standby database from the broker configuration, the broker checks to see if the protection mode will still be satisfied. The operation fails if:

- Removing the database compromises the protection mode
- Fast-start failover is enabled and you try to remove the standby database that is the target of the fast-start failover
- The configuration member to be removed has its `RedoRoutes` configurable property set to a non-null value

You can remove the configuration at any time, unless fast-start failover is enabled.

##### Requirements On Other Operations

Some operations that take place in a broker configuration, especially operations related to redo transport services, can affect the overall protection mode. These operations include:

- Stopping redo transport services on the primary database
- Stopping redo transport services to individual standby databases
- Downgrading the redo transport mode from `SYNC` to `ASYNC` to the only standby database that supports a configuration operating in maximum availability mode or maximum protection mode

Before any of these operations can proceed, the broker checks to see if the protection mode will be supported by the redo transport service settings on the standby databases after the operation completes. If not, the broker fails the operation and returns an error.

### Managing Far Sync Instances

An Oracle Data Guard far sync instance is a redo transport destination that accepts redo from a primary database and forwards that redo to one or more redo destinations in the configuration.

It is similar to a physical standby database in that it has a control file, receives redo into Standby Redo Log files (SRLs), and archives those SRLs to local Archived Redo Logs (ARLs). But unlike a standby database, a far sync instance does not have data files, cannot be opened, and cannot apply received redo. These limitations yield the benefit of using fewer disk and processing resources. More importantly, a far sync instance provides the ability to failover to a terminal database with no data loss if it receives redo data using synchronous transport mode and the configuration protection mode is set to maximum availability.

Starting with Oracle Database Release 21c, you can use the `CREATE         FAR_SYNC` command to create a new far sync instance and add it to the broker configuration. See [CREATE FAR\_SYNC](oracle-data-guard-broker-commands.md).

The following example shows how to add a far sync instance to a broker configuration.

```
DGMGRL> ADD FAR_SYNC FS1 AS CONNECT IDENTIFIER IS FS1.example.com;
Far Sync FS1 added
DGMGRL> ENABLE FAR_SYNC FS1;
Enabled.
DGMGRL> SHOW CONFIGURATION;
 
Configuration - DRSolution
 
  Protection Mode: MaxPerformance
  Members:
  North_Sales  - Primary database
    FS1        - Far Sync
    South_Sales - Physical standby database
 
Fast-Start Failover: DISABLED
Configuration Status:
SUCCESS
```

After a far sync instance has been added to the configuration, set up redo transport to support maximum availability and then upgrade the protection mode:

```
DGMGRL> EDIT DATABASE 'North_Sales' SET PROPERTY 'RedoRoutes' = '(LOCAL : FS1 SYNC)';
DGMGRL> EDIT FAR_SYNC 'FS1' SET PROPERTY 'RedoRoutes' = '(North_Sales : South_Sales ASYNC)';
DGMGRL> EDIT CONFIGURATION SET PROTECTION MODE AS MaxAvailability;
DGMGRL> SHOW CONFIGURATION;
 
Configuration - DRSolution
 
  Protection Mode: MaxAvailability
  Members:
  North_Sales  - Primary database
    FS1          - Far Sync
      South_Sales - Physical standby database
 
Fast-Start Failover: DISABLED
Configuration Status:
SUCCESS
```

To ensure that maximum availability protection mode can be maintained when `South_Sales` is the primary database, after a switchover or a failover, add a second far sync instance to the configuration so that `South_Sales` can send redo in synchronous mode which in turn will send redo to the new terminal database, `North_Sales,` after the role transition.

The following example shows how to add a second far sync instance to the broker configuration:

```
DGMGRL> ADD FAR_SYNC FS2 AS CONNECT IDENTIFIER IS FS2.example.com;
Far Sync FS2 added
DGMGRL> EDIT FAR_SYNC 'FS2' SET PROPERTY 'RedoRoutes' = '(South_Sales : North_Sales ASYNC)';
DGMGRL> ENABLE FAR_SYNC FS2;
Enabled.
DGMGRL> EDIT DATABASE 'South_Sales' SET PROPERTY 'RedoRoutes' = '(LOCAL : FS2 SYNC)';
DGMGRL> SHOW CONFIGURATION;
 
Configuration - DRSolution
 
  Protection Mode: MaxAvailability
  Members:
  North_Sales  - Primary database
    FS1          - Far Sync
      South_Sales - Physical standby database
      FS2         - Far Sync (inactive)
 
Fast-Start Failover: DISABLED
Configuration Status:
SUCCESS
```

If a far sync instance is monitored for availability by Oracle Clusterware (for example, in an Oracle Restart, Oracle Real Application Clusters (Oracle RAC), or Oracle RAC One Node installation), then use the SRVCTL utility to specify a default open mode of mount. You can use a command such as the following:

```
srvctl modify database -d <db_unique_name> -startoption MOUNT
```

See Also:

- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/dgbkr&id=SBYDB5416) for more information about creating a far sync instance and redo transport

### Managing Fast-Start Failover

You can enable fast-start failover to allow the broker to determine if a failover is necessary and to initiate a failover to a standby database from a list of one or more pre-specified target standby databases.

The failover can be set up for either no data loss or a configurable amount of data loss. In addition, you can specify under which conditions or errors you want a failover to be initiated. Oracle also provides the `DBMS_DG` PL/SQL package to allow an application to request a fast-start failover.

You use broker configuration properties to control the behavior of fast-start failover. You can also use Cloud Control or the DGMGRL `ENABLE FAST_START FAILOVER CONDITION` and `DISABLE FAST_START FAILOVER CONDITION` commands to specify conditions for which a fast-start failover should occur.

#### Configure Properties to Tune Fast-Start Failover

You can set various properties to tune how fast-start failover behaves.

The configurable properties for fast-start failover include:

- `FastStartFailoverThreshold`
	Set the `FastStartFailoverThreshold` configuration property to specify the number of seconds you want the observer and target standby database to wait (after detecting the primary database is unavailable) before initiating a failover. See [Enabling Fast-Start Failover](using-data-guard-broker-to-manage-switchovers-failovers.md) for more information and an example.
- `FastStartFailoverPmyShutdown`
	The `FastStartFailoverPmyShutdown` configuration property controls whether the primary database will shut down if redo generation has been stalled (`FS_FAILOVER_STATUS` column of `V$DATABASE` contains a value of `STALLED`) and the primary database has lost connectivity with the observer and target standby database for longer than the number of seconds specified by the `FastStartFailoverThreshold` configuration property. The default value for FastStartFailoverPmyShutdown is `TRUE`.
	Note:
	The primary database is always shut down if a user configurable fast-start failover condition is detected or if an application initiated a fast-start failover by calling the `DBMS_DG.INITIATE_FS_FAILOVER` function.
- `FastStartFailoverLagLimit`
	The fast-start failover feature can be configured on databases operating in maximum performance mode. Destinations that receive redo in `ASYNC` mode will be acceptable fast-start failover target standby databases, and these destinations can lag the primary in terms of redo received and applied. A configurable time-based limit can be specified through the `FastStartFailoverLagLimit` configuration property. If the standby database's applied redo point is within this many seconds of the primary's redo generation point, a fast-start failover will be allowed. If its applied point lags beyond this limit, a fast-start failover is not allowed.
	The `FastStartFailoverLagLimit` configuration property can also be used if fast-start failover is enabled when the configuration is operating in maximum availability mode. It cannot be used when the configuration is operating in maximum protection mode. When `FastStartFailoverLagLimit` is set to a non-zero value and the configuration is operating in maximum availability mode, a zero data loss failover or a data loss failover is possible. If a data loss failover is performed, the amount of data loss will not exceed the number of seconds specified by the `FastStartFailoverLagLimit` configuration property. Note that the redo transport mode of the target standby must be set to the value of `SYNC` or `FASTSYNC` or `ASYNC` when a non-zero value is specified for the `FastStartFailoverLagLimit` property and the protection mode is maximum availability mode or maximum performance mode. If you want to change protection mode or redo transport mode to `SYNC` or `FASTSYNC`, you must first disable fast-start failover. Likewise, changing the protection mode from maximum availability mode to maximum performance mode will require first disabling fast-start failover. Reinstatement of an old primary will be possible after a fast-start failover to a target standby. If the observer rediscovers the old primary, it will automatically reinstate the old primary and any redo generated within the specified lag will be lost.
	See Also:
	[Oracle Data Guard Broker Properties](oracle-data-guard-broker-properties.md) for more information
- `FastStartFailoverAutoReinstate`
	The `FastStartFailoverAutoReinstate` configuration property controls whether the former primary database is automatically reinstated if a fast-start failover occurred because the primary database crashed or was stalled for longer than `FastStartFailoverThreshold` seconds. The default value for `FastStartFailoverAutoReinstate` is `TRUE`.
	If you want to perform diagnostic or repair work after failover has completed, you can avoid an automatic reinstatement by setting the `FastStartFailoverAutoReinstate` configuration property to `FALSE`.
	Note:
	The former primary database is never automatically reinstated if a fast-start failover occurred because a user configurable fast-start failover condition was detected or because an application initiated a fast-start failover by calling the `DBMS_DG.INITIATE_FS_FAILOVER` function.
- `FastStartFailoverTarget`
	The `FastStartFailoverTarget` configuration property specifies the `DB_UNIQUE_NAME` values of the databases that are eligible to be targets of a fast-start failover when this database is the primary database.
- `ObserverPingInterval`
	The `ObserverPingInterval` configuration property specifies how frequently the observer must ping the primary database. This property is measured in milliseconds. The minimum value is 100 milliseconds. To achieve lower detection times for primary database failures, you must set the `ObserverPingInterval` and `ObserverPingRetry` properties before enabling fast-start failover.
- `ObserverPingRetry`
	The `ObserverPingRetry` configuration property pecifies the number of times that the observer retries a failed ping before it initiates a failover to the target standby database. A failed ping is a ping to the primary database that failed or took longer than the time specified by the `ObserverPingInterval` property. You must set both the `ObserverPingRetry` and `ObserverPingInterval` properties to achieve lower detection times for primary database failures. The minimum value is 10.
- `ObserverReconnect`
	The `ObserverReconnect` configuration property specifies how often the observer establishes a new connection to the primary database. When this property is set to the default value of 0, it prevents the observer from periodically establishing a new connection with the primary database. While this eliminates the processing overhead associated with periodically establishing a new observer connection to the primary database, it also prevents the observer from detecting that it is not possible to create new connections to the primary database. Oracle recommends that this property be set to a value that is small enough to allow timely detection of faults at the primary database, but large enough to limit the overhead associated with periodic observer connections to an acceptable level.
- `ObserverOverride`
	The `ObserverOverride` configuration property, when set to `TRUE`, allows an automatic failover to occur when the observer has lost connectivity to the primary, even if the standby has a healthy connection to the primary.

#### Configure Conditions for Fast-start Failover

By default, a fast-start failover is done when neither the observer nor the standby can reach the primary after the configured time threshold (`FastStartFailoverThreshold`) has passed.

There are also other conditions under which you might want a fast-start failover to occur.

The configurable conditions fall into two classes: those detected through the database health-check mechanism and those detected through errors raised by the Oracle server (such as ORA errors). When a specified condition occurs, the observer will initiate a fast-start failover without waiting for `FastStartFailoverThreshold` to expire, assuming the standby is in a valid state to accept a failover.

Each condition may be enabled or disabled individually. The Oracle Data Guard configuration persists all user specified configurable fast-start failover conditions in the broker configuration file.

The observer will detect when the primary database has signaled any of the enabled health-check conditions and will immediately initiate a fast-start failover, assuming the standby is in a valid fast-start failover state (observed and either synchronized or within lag limits) to accept a failover.

For specified Oracle ORA-Error conditions, the primary database will notify the observer if the error is signaled and the observer will immediately initiate a fast-start failover, assuming the standby is in a valid fast-start failover state (observed and either synchronized or within lag limits) to accept a failover. Please note that the only Oracle ORA-Error for which fast-start failover can be triggered is ORA-240.

Note:

The primary database will shut down and the observer will not attempt to automatically reinstate the former primary database.

See Also:

- Cloud Control online help
- [ENABLE FAST\_START FAILOVER CONDITION](oracle-data-guard-broker-commands.md)
- [DISABLE FAST\_START FAILOVER CONDITION](oracle-data-guard-broker-commands.md)

#### Application Initiated Fast-Start Failover

You can use the `DBMS_DG` PL/SQL package to allow an application to direct a fast-start failover when it encounters specific conditions.

See " [Directing a Fast-Start Failover From an Application](using-data-guard-broker-to-manage-switchovers-failovers.md) ".

### Managing Database Conversions

You can use the DGMGRL `CONVERT DATABASE` command to convert a physical standby database to a snapshot standby database.

A snapshot standby database is a fully updatable standby database.

Like a physical or logical standby database, a snapshot standby database receives and archives redo data from a primary database. However, unlike a physical or logical standby database, a snapshot standby database does not apply the redo data that it receives. The redo data received by a snapshot standby database is not applied until the snapshot standby is converted back into a physical standby database, after first discarding any local updates made to the snapshot standby database.

To convert a physical standby database to a snapshot standby database you must have Flashback Database enabled. The following example shows how to convert a physical standby database to a snapshot standby database:

```
DGMGRL> CONVERT DATABASE 'South_Sales' TO SNAPSHOT STANDBY;
```

When you are ready to convert the snapshot back into a physical standby, use the DGMGRL `CONVERT DATABASE` command as follows:

```
DGMGRL> CONVERT DATABASE 'South_Sales' TO PHYSICAL STANDBY;
```

### Database Status

In general, the broker checks the health of a database by verifying that the actual database state and settings match those described in the broker configuration file.

This is done by checking if any component of the Oracle Data Guard configuration is functioning incorrectly (for example, if redo transport services have an error), and by checking if other required database settings are correctly set (for example, if the server parameter files are available and if the `ARCHIVELOG` mode is turned on). The following is a detailed list of what is being checked by the broker on a primary database and a standby database.

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

#### Querying Database Status

Certain monitorable properties can be used to query the database status.

The following properties are directly accessed through the DGMGRL command-line interface:

- `LogXptStatus`
- `InconsistentLogXptProps`
	Note:
	Cloud Control rearranges the values of these properties for presentation in the GUI.

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

To further check the details about the database status, you can use the following monitorable properties:

- `LogXptStatus` — lists all log transport errors detected on all instances of the primary database.
- `InconsistentLogXptProps` — lists all redo transport-related properties of standby databases that have inconsistent values between the broker configuration file and the redo transport settings.

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

[Oracle Data Guard Broker Properties](oracle-data-guard-broker-properties.md) for detailed information about database properties

#### Validating a Database Before a Role Change

You can use the `VALIDATE` `DATABASE` command to perform a comprehensive set of database checks prior to performing a role change.

The command checks the following items:

- Whether there is missing redo data on a standby database
- Whether flashback is enabled
- The number of temporary tablespace files configured
- Whether an online data file move is in progress
- Whether online redo logs are cleared for a physical standby database
- Whether standby redo logs are cleared for a primary database
- The online log file configuration
- The standby log file configuration
- Apply-related property settings
- Transport-related property settings
- Whether there are any errors in the Automatic Diagnostic Repository (for example, control file corruptions, system data file problems, user data file problems)

See Also:

- " [VALIDATE DATABASE](oracle-data-guard-broker-commands.md) " for a description of the command and for examples that show command output for various scenarios

#### Validating the Server Parameter Files Before a Role Change

Use the `VALIDATE DATABASE SPFILE` command to compare the contents of the server parameter file (SPFILE) between the primary and standby database.

Comparing the primary to the standby lets you determine whether there are any missing parameters in either database’s SPFILE, or whether the entries contain different values.

See Also:

- [VALIDATE DATABASE SPFILE](oracle-data-guard-broker-commands.md) for a description of the command and for examples that show command output

#### Validating the Network Configuration Before a Role Change

Use the `VALIDATE NETWORK CONFIGURATION` command to perform network connectivity checks between members of a configuration.

Performing a network connectivity check identifies potential network configuration problems before a role change is attempted.

See Also:

- Validating the Network Configuration Before a Role Change

#### Validating the Static Connect Identifier Before a Role Change

A single-instance database on which Oracle Restart is not configured must have a static service registered with the listener so that the DGMGRL CLI can automatically start the instance when necessary (for example, for the new standby after a switchover).

The broker sets up a default value for the `StaticConnectIdentifier` property that uses that static service (assuming the default value of `db_unique_name_DGMGRL` is used for the static service name). This connect identifier is used for instance restart.

Use the `VALIDATE STATIC CONNECT IDENTIFIER` command to confirm that the connect identifier specified by the `StaticConnectIdentifier` property can be used to restart an instance. The command does not restart the database, but rather checks that the service specified in the connect identifier is registered with the listener.

#### Validating the DGConnectIdentifier Property

The DGMGRL command `VALIDATE DGConnectIdentfier` enables users to check to see whether a connection string is valid for the `DGConnectidentifier` property or not..

The `VALIDATE DGConnectIdentifier` command checks if it is able to be translated to something useful and makes a connection using it on all configuration members. This can also be used prior to adding a member to the configuration. If no configuration exists, the command checks a connection string at the database DGMGRL is connected to. If a configuration exists, all members use the specified connection string to see that the connection works.

This command performs the following for each instance of all members.
- Prints a network translation of the connection string at the instance.
- Prints environment variables related to network configuration at the instance.
- Makes a new connection using the translated network address at the instance.
- If a connection test succeeds, the instance name and `db_unique_name` of the connected database will be printed.

See Also:

- [VALIDATE DGConnectIdentifier](unresolvable-reference.md) for a description of the command and for examples that show command output