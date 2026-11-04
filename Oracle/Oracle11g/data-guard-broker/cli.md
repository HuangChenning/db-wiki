---
title: Scenarios Using the DGMGRL Command-Line Interface
book: Data Guard Broker
doc_id: E40771-07
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40771/cli.htm
tags:
  - oracle
  - 11g
  - data-guard-broker
---

## 6 Scenarios Using the DGMGRL Command-Line Interface

This chapter describes the prerequisites for getting started using the Data Guard command-line interface (DGMGRL). It also describes scenarios that demonstrate how to use DGMGRL to create, manage, and monitor a broker configuration.

This chapter contains the following sections:

## 6.1 Prerequisites for Getting Started

One of the prerequisites for using DGMGRL is that a primary database and any standby databases must already exist. The `DG_BROKER_START` initialization parameter must be set to `TRUE` for all databases in the configuration. You must use a server parameter file with the broker (see [Section 2.1](install.md) and [Section 7.1.3](dgmgrl.md)).

Convert the initialization parameter files (PFILE) on both primary and standby databases into server parameter files (SPFILE), if necessary. Use the following SQL\*Plus command:

```
CREATE SPFILE FROM PFILE='pfilename';
```

If an instance was not started with a server parameter file, then you must shut down the instance and restart it using the server parameter file.

After starting the Oracle instance, set the `DG_BROKER_START=TRUE` initialization parameter using the SQL `ALTER SYSTEM` statement. The parameter value will be saved in the server parameter file. The next time you start the Oracle instance, the broker is started automatically, and you do not need to issue the SQL `ALTER SYSTEM` statement again.

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for detailed information about creating server parameter files

The following assumptions are made for the scenarios in this chapter:

- TCP/IP is used to connect to primary and standby databases.
- The standby database has been created from backups of the primary database control files and datafiles as described in the [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/create_ps.htm#SBYDB00210).
- The scenarios in this chapter assume the following broker configuration:
	- The configuration name is `DRSolution`.
		- The database unique name (`DB_UNIQUE_NAME`) of the primary database is `North_Sales`.
		- The database unique name (`DB_UNIQUE_NAME`) of the remote standby database is `South_Sales`.
		- The protection mode is maximum performance mode.
		- There are standby redo log files configured for both the primary and standby database. The transport mode for both databases is `ASYNC`.
		- The standby database is a physical standby database.

## 6.2 Scenario 1: Creating a Configuration

This section provides examples that create a broker configuration named  
`DRSolution` that includes a primary and standby database named `North_Sales` and `South_Sales`.

The following steps show how to create a configuration and add one physical standby database.

Step 1 Invoke DGMGRL.

To start DGMGRL, enter `dgmgrl` at the command-line prompt on a system where Oracle Data Guard is installed:

```
$ dgmgrl
```

The DGMGRL prompt is displayed:

```
DGMGRL>
```

Step 2 Connect to the primary database.

Before you specify any command (other than the `HELP,` `EXIT,` or `QUIT`), you must first connect to the primary database using the DGMGRL `CONNECT` command.

The account from which you connect to the database (`SYS` in this example) must have `SYSDBA` privileges on the primary and standby databases.

Note:

You do not have to include `AS SYSDBA` on the `CONNECT` command because `SYSDBA` is the default setting for this command.

The following examples show two variations of the `CONNECT` command. Example 6-1 shows how to connect to the default database on the local system, and Example 6-2 includes the Oracle Net Services connect identifier  
(`North_Sales.example.com`) to make a connection to a database located on a remote system. In both examples, you are prompted for a password.

Example 6-1 Connecting to the Primary Database on the Local System

```
DGMGRL> CONNECT sys;
Password: password
Connected.
```

Example 6-2 Connecting to the Primary Database on a Remote System

```
DGMGRL> CONNECT sys@North_Sales.example.com;
Password: password
Connected.
```

Step 3 Create the broker configuration.

To create the broker configuration, you first define the configuration including a profile for the primary database, which in this case is called `North_Sales`. In a later command, you will add a profile for the standby database, `South_Sales`.

Note:

The names for the primary and standby databases must match their database unique names. Fetch these from their `DB_UNIQUE_NAME` initialization parameter as follows:
```
SQL> SHOW PARAMETER DB_UNIQUE_NAME;
```

Use the `CREATE CONFIGURATION` command to create the `DRSolution` configuration and define the primary database, `North_Sales`:

```
DGMGRL> CREATE CONFIGURATION 'DRSolution' AS
>  PRIMARY DATABASE IS 'North_Sales'
>  CONNECT IDENTIFIER IS North_Sales.example.com;
```

DGMGRL returns the following information:

```
Configuration "DRSolution" created with primary database "North_Sales"
```

The name `North_Sales` is the value of this database's `DB_UNIQUE_NAME` initialization parameter.

Step 4 Show the configuration information.

Use the `SHOW CONFIGURATION` command to display a brief summary of the configuration:

```
DGMGRL> SHOW CONFIGURATION;
```

DGMGRL returns the following information:

```
Configuration - DRSolution
 
  Protection Mode: MaxPerformance
  Databases:
    North_Sales - Primary database
 
Fast-Start Failover: DISABLED
 
Configuration Status:
DISABLED
```

Step 5 Add a standby database to the configuration.

To add a standby database to the `DRSolution` configuration, use the `ADD DATABASE` command to create a broker configuration profile for the standby database.

The following command defines `South_Sales` as a standby database, which is the standby database associated with the primary database called `North_Sales`:

```
DGMGRL> ADD DATABASE 'South_Sales' AS
>  CONNECT IDENTIFIER IS South_Sales.example.com;
```

DGMGRL returns the following information:

```
Database "South_Sales" added
```

The name `South_Sales` is the value of the database's `DB_UNIQUE_NAME` initialization parameter.

Use the `SHOW CONFIGURATION` command to verify that the `South_Sales` database was added to the `DRSolution` configuration:

```
DGMGRL> SHOW CONFIGURATION;
```

DGMGRL returns the following information:

```
Configuration - DRSolution
 
  Protection Mode: MaxPerformance
  Databases:
    North_Sales  - Primary database
    South_Sales  - Physical standby database
 
Fast-Start Failover: DISABLED
 
Configuration Status:
DISABLED
 
DGMGRL>
```

## 6.3 Scenario 2: Setting Database Properties

After you create the configuration with DGMGRL, you can set database properties at any time. For example, the following statements set the `LogArchiveFormat` and `StandbyArchiveLocation` database properties for the `South_Sales` standby database:

```
DGMGRL> EDIT DATABASE 'South_Sales' SET PROPERTY 'LogArchiveFormat'='log_%t_%s_%r_%d.arc';
Property "LogArchiveFormat" updated.

DGMGRL> EDIT DATABASE 'South_Sales' SET PROPERTY 'StandbyArchiveLocation'='/archfs/arch/';
Property "StandbyArchiveLocation" updated.
```

Use the `SHOW DATABASE VERBOSE` command to view all properties and their values for a database. The following example shows the properties for the `South_Sales` database.

```
DGMGRL> SHOW DATABASE VERBOSE 'South_Sales';
 
Database - South_Sales
 
  Role:            PHYSICAL STANDBY
  Intended State:  OFFLINE
  Transport Lag:   (unknown)
  Apply Lag:       (unknown)
  Real Time Query: OFF
  Instance(s):
    south_sales1
 
  Properties:
    DGConnectIdentifier             = 'South_Sales.example.com'
    ObserverConnectIdentifier       = ''
    LogXptMode                      = 'ASYNC'
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
    DbFileNameConvert               = 'dbs/t, dbs/bt'
    LogFileNameConvert              = 'dbs/t, dbs/bt'
    FastStartFailoverTarget         = ''
    InconsistentProperties          = '(monitor)'
    InconsistentLogXptProps         = '(monitor)'
    SendQEntries                    = '(monitor)'
    LogXptStatus                    = '(monitor)'
    RecvQEntries                    = '(monitor)'
    SidName                         = 'south_sales1'
    StaticConnectIdentifier         = '(DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)
(HOST=south_sales1.example.com)(PORT=2840))
(CONNECT_DATA=(SERVICE_NAME=South_Sales_DGMGRL.example.com)
(INSTANCE_NAME=south_sales1)(SERVER=DEDICATED)))'
    StandbyArchiveLocation          = 'USE_DB_RECOVERY_FILE_DEST'
    AlternateLocation               = ''
    LogArchiveTrace                 = '255'
    LogArchiveFormat                = 'db2r_%d_%t_%s_%R.arc'
    LatestLog                       = '(monitor)'
    TopWaitEvents                   = '(monitor)'
 
Database Status:
DISABLED
```

If broker management of the database is enabled, setting a database property value causes the underlying parameter value to be changed in the corresponding database, and the value for the changed parameter is reflected in the server parameter file. Thus, if the database is shut down and restarted outside of Oracle Enterprise Manager and DGMGRL (such as from the SQL\*Plus interface), the database uses the new parameter values from the updated server parameter file when it starts. However, you should not make changes to the redo transport services initialization parameters through SQL statements. Doing so will cause an inconsistency between the database and the broker.

Note:

The database properties are typically displayed in mixed-case (for example, `LogArchiveFormat`) typeface to help you visually differentiate database properties (from the corresponding initialization parameter, SQL statement, or PL/SQL procedure), which are typically documented in `UPPERCASE` typeface. However, the commands to manage properties are not case sensitive; you can issue commands in uppercase, lowercase, or mixed-case.

You can change a property if the database is enabled or disabled. However, if the database is disabled when you change a property, the change does not take effect until the database is enabled.

## 6.4 Scenario 3: Enabling the Configuration and Databases

So far, the `DRSolution` configuration is disabled, which means it is not under the control of the Data Guard broker. When you finish configuring the databases into a broker configuration and setting any necessary database properties, you must enable the configuration to allow the Data Guard broker to manage it.

You can enable:

- The entire configuration, including all of its databases
- A standby database

Enable the entire configuration.

You can enable the entire configuration, including all of the databases, with the following command:

```
DGMGRL> ENABLE CONFIGURATION;
Enabled.
```

Show the configuration.

Use the `SHOW` command to verify that the configuration and its databases were successfully enabled:

```
DGMGRL> SHOW CONFIGURATION;
```

DGMGRL returns the following information:

```
Configuration - DRSolution
 
  Protection Mode: MaxPerformance
  Databases:
    North_Sales  - Primary database
    South_Sales  - Physical standby database
 
Fast-Start Failover: DISABLED
 
Configuration Status:
SUCCESS
```

Enable the database.

This step is unnecessary except if the standby database was previously disabled with the `DISABLE DATABASE` command. Normally, enabling the configuration also enables the standby database.

```
DGMGRL> ENABLE DATABASE 'South_Sales';
Enabled.
```

Show the database.

```
DGMGRL> SHOW DATABASE 'South_Sales';

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

## 6.5 Scenario 4: Setting the Configuration Protection Mode

You can change the protection mode of the configuration at any time. However, it is best if you do this when there is no activity occurring in the configuration if you are moving to the maximum protection or maximum availability modes.

Note:

If you change the protection mode from maximum performance mode to maximum protection mode, the broker automatically restarts the primary database. If you wish to avoid restarting the database, first change the protection mode to maximum availability mode and then change the protection mode to maximum protection mode.

A restart of the primary database is not required when changing the protection mode from:

- maximum performance to maximum availability
- maximum availability to maximum protection

This scenario sets the protection mode of the configuration to the `MAXAVAILABILITY` mode. Note that this protection mode requires that there be at least one standby database configured to use standby redo log files, with its `LogXptMode` database property set to `SYNC`.

Step 1 Configure standby redo log files, if necessary.

Because you will be setting the protection mode to the `MAXAVAILABILITY` mode, it is important to ensure that sufficient standby redo log files are configured on the standby database.

Step 2 Set the LogXptMode database property appropriately.

Use the `EDIT DATABASE (property)` command on the standby database to set the redo transport service that corresponds to the protection mode you plan to set. If the protection mode to be set is `MAXAVAILABILITY`, it is required that the redo transport service of at least one standby database is set to `SYNC`. For example:

```
DGMGRL> EDIT DATABASE 'South_Sales' SET PROPERTY 'LogXptMode'='SYNC';
Property "LogXptMode" updated
```

The broker will not allow this command to succeed unless the standby database is configured with standby redo log files in the configuration.

Step 3 Change the overall protection mode for the configuration.

Use the `EDIT` `CONFIGURATION` command to upgrade the broker configuration to the `MAXAVAILABILITY` protection mode:

```
DGMGRL> EDIT CONFIGURATION SET PROTECTION MODE AS MAXAVAILABILITY;
Succeeded.
```

If the configuration is disabled when you enter this command, the actual protection mode change is not applied until you enable the configuration with the `ENABLE CONFIGURATION` command. The broker will not allow you to enable the configuration if it does not find a standby database in the configuration that can support the requirements of the protection mode.

Step 4 Verify the protection mode has changed.

Use the `SHOW CONFIGURATION` command to display the current protection mode for the configuration:

```
DGMGRL> SHOW CONFIGURATION;
 
Configuration - DRSolution
 
  Protection Mode: MaxAvailability
  Databases:
    North_Sales  - Primary database
    South_Sales  - Physical standby database
 
Fast-Start Failover: DISABLED
 
Configuration Status:
SUCCESS
```

See Also:

[Section 4.6, "Managing Data Protection Modes"](dbresource.md)

## 6.6 Scenario 5: Enabling Fast-Start Failover and Starting the Observer

You can enable fast-start failover from any site, including the observer site, while connected to any database in the broker configuration. Enabling fast-start failover does not trigger a failover. Instead, it allows the observer that is monitoring the configuration to initiate a fast-start failover if conditions warrant a failover.

Fast-start failover can be enabled in configurations operating in either maximum performance or maximum availability protection mode. This section describes the steps to enable fast-start failover and start the observer where the configuration protection mode is set to maximum availability mode.

Step 1 Ensure standby redo logs are configured on the primary and target standby databases.

Standby redo logs must be configured on the primary and standby databases. You must stop log apply services prior to configuring standby redo logs.

See Also:

[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/create_ps.htm#SBYDB00426) for instructions on configuring standby redo log files

Step 2 Ensure the LogXptMode Property is set to SYNC.

The `LogXptMode` database property must be set to `SYNC` on the primary and target standby databases.

To set the redo transport service that corresponds to the protection mode you plan to set, use the `EDIT DATABASE` (property) command on the primary and target standby databases. For example, if the protection mode to be set is `MAXAVAILABILITY`, you must set the `LogXptMode` property to `SYNC` on the primary database and on the target standby database, as shown in the following examples:

```
DGMGRL> EDIT DATABASE 'North_Sales' SET PROPERTY 'LogXptMode'='SYNC';
Property "LogXptMode" updated
```
```
DGMGRL> EDIT DATABASE 'South_Sales' SET PROPERTY 'LogXptMode'='SYNC';
Property "LogXptMode" updated
```

The broker does not allow these commands to succeed unless the databases are configured with standby redo log files.

Step 3 Set the FastStartFailoverTarget configuration property.

If you have two or more standby databases, set up the `FastStartFailoverTarget` configuration property on the primary database to indicate the desired target standby database. The broker reciprocally sets this property for the target standby database to indicate the primary database as its future target standby database when fast-start failover is actually enabled. There is no need for you set this property on the target standby as this is done for you automatically.For example:

```
DGMGRL> EDIT DATABASE 'North_Sales' SET PROPERTY FastStartFailoverTarget='South_Sales';
Property "FastStartFailoverTarget" updated
```

Step 4 Upgrade the protection mode to `MAXAVAILABILITY`, if necessary.

If it is necessary to upgrade the protection mode, use the following DGMGRL `EDIT CONFIGURATION` command. For example:

```
DGMGRL> EDIT CONFIGURATION SET PROTECTION MODE AS MAXAVAILABILITY;
```

Step 5 Enable Flashback Database on the primary and target standby databases, if necessary.

If it is not already enabled on the primary and standby databases, enable Flashback Database by issuing the following statements on each database:

```
ALTER SYSTEM SET UNDO_RETENTION=3600 SCOPE=SPFILE;
ALTER SYSTEM SET UNDO_MANAGEMENT='AUTO' SCOPE=SPFILE;
SHUTDOWN IMMEDIATE;
STARTUP MOUNT;
SHOW PARAMETER UNDO;
ALTER SYSTEM SET DB_FLASHBACK_RETENTION_TARGET=4320 SCOPE=BOTH;
ALTER DATABASE ARCHIVELOG;
ALTER SYSTEM SET db_recovery_file_dest_size=<size>;
ALTER SYSTEM SET db_recovery_file_dest=<directory-specification>;
ALTER DATABASE FLASHBACK ON;
ALTER DATABASE OPEN;
```

Ensure the `UNDO_RETENTION` and `DB_FLASHBACK_RETENTION_TARGET` initialization parameters are set to sufficiently large values so that reinstatement is still possible after a prolonged outage.

Step 6 Start the observer.

Start the observer by logging into the observer computer and running DGMGRL. Connect to the configuration as a user who has the `SYSDBA` privilege and then issue the `START OBSERVER` command. Note that the command does not return; that is you will not get the DGMGRL prompt after issuing the command.

```
DGMGRL> CONNECT sys@North_Sales.example.com;
Password: password
Connected.
DGMGRL> START OBSERVER;
Observer started
```

When starting the observer interactively, Oracle recommends that connection credentials not be supplied as command line parameters to the DGMGRL connect command. This practice prevents other users on the system from using a utility (for example, the UNIX ps utility) to display connection credentials. It also prevents clear-text passwords from being visible on the user's terminal.

When starting the observer from a script, Oracle recommends that you use a method that supports 'connect /', so that database connection credentials do not have to be embedded within the script. If you choose to use a client-side Oracle Wallet as a secure external password store (see [Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm)), be sure to add credentials for both the primary and fast-start failover target standby databases. The database connect string that you specify when adding the credentials for each database must match the `ObserverConnectIdentifer` or `DGConnectIdentifier` database property.

Step 7 Enable fast-start failover.

You can enable fast-start failover while connected to any database system in the broker configuration. For example:

```
DGMGRL> ENABLE FAST_START FAILOVER;
Enabled.
```

Step 8 Verify the fast-start failover configuration.

Use the `SHOW FAST_START FAILOVER` command to display the fast-start failover settings:

```
DGMGRL> SHOW FAST_START FAILOVER;
 
Fast-Start Failover: ENABLED
 Threshold:           30 seconds
 Target:              South_Sales
 Observer:            observer.example.com
 Lag Limit:           30 seconds (not in use)
 Shutdown Primary:    TRUE
 Auto-reinstate:      TRUE
 
Configurable Failover Conditions
 Health Conditions:
   Corrupted Controlfile          YES
   Corrupted Dictionary           YES
   Inaccessible Logfile            NO
   Stuck Archiver                  NO
   Datafile Offline               YES
 
 Oracle Error Conditions:
   (none)
```

The following commands show that the `FastStartFailoverTarget` property is set up reciprocally once fast-start failover is enabled. The first command, issued for the current primary database `North_Sales`, shows the value of the `FastStartFailoverTarget` property to be the current target standby, `South_Sales`. The second command, issued for the target standby `South_Sales`, shows the current primary, `North_Sales`, as the target standby's future target standby should it ever take over as a primary.

```
DGMGRL> SHOW DATABASE 'North_Sales' FastStartFailoverTarget;
 FastStartFailoverTarget='South_Sales';
 
DGMGRL> SHOW DATABASE 'South_Sales' FastStartFailoverTarget;
 FastStartFailoverTarget='North_Sales';
```

## 6.7 Scenario 6: Performing Routine Management Tasks

There may be situations in which you want to change the state or properties of the databases in a broker configuration to perform routine maintenance on one or more databases. You might also need to temporarily disable broker management of databases in a configuration.

### 6.7.1 Changing Properties and States

As you monitor the configuration, you might need to dynamically modify the states of the databases or their properties. The following sections show how to change the state or properties of the databases in the configuration.

#### 6.7.1.1 Alter a Database Property

You can modify the values of database properties at any time—if the database is enabled or disabled.

Example 6-3 shows how to use the `EDIT DATABASE` command to change the `LogXptMode` database property to the value ASYNC for the `North_Sales` database.

Example 6-3 Altering a Database Property

```
DGMGRL> EDIT DATABASE 'North_Sales' SET PROPERTY 'LogXptMode'=ASYNC;
```

DGMGRL returns the following message to indicate that the `LogXptMode` property was updated successfully in the Data Guard configuration file:

```
Property "LogXptMode" updated
```

If the configuration is currently disabled, the database does not use the new property value until you enable the broker configuration with the `ENABLE CONFIGURATION` command.

#### 6.7.1.2 Alter the State of a Standby Database

You might want to temporarily stop Redo Apply on a physical standby. To change the state of the standby database to `APPLY-OFF`, enter the `EDIT DATABASE` command as shown in Example 6-4.

Example 6-4 Altering a Standby Database State

```
DGMGRL> EDIT DATABASE 'South_Sales' SET STATE='APPLY-OFF';
Succeeded.
```

Redo data is still being received when you put the physical standby database in the `APPLY-OFF` state.

#### 6.7.1.3 Alter the State of a Primary Database

You might want to stop the transmittal of redo data to the standby database. To change the state of the primary database to accommodate this, use the following command:

```
DGMGRL> EDIT DATABASE North_Sales SET STATE=TRANSPORT-OFF;
 
Succeeded.
```

To change the state of the primary database back to TRANSPORT-ON, do the following:

```
DGMGRL> EDIT DATABASE North_Sales SET STATE=TRANSPORT-ON;
 
Succeeded.
```

### 6.7.2 Disabling the Configuration and Databases

When you disable the broker configuration or any of its databases, you are disabling the broker's management of those objects and are effectively removing your ability to use DGMGRL to manage and monitor the disabled object. However, disabling the broker's management of a broker configuration does not affect the actual operation of the underlying Data Guard configuration or the databases. For example, the redo transport services and log apply services in the Data Guard configuration continue to function unchanged, but you can no longer manage them.

#### 6.7.2.1 Disable a Configuration

You must use the `DISABLE CONFIGURATION` command to disable management of the entire broker configuration including the primary database as shown in Example 6-5.

Example 6-5 Disabling the Configuration and Primary Database

```
DGMGRL> DISABLE CONFIGURATION;
```

The only way to disable broker management of the primary database is to use the `DISABLE CONFIGURATION` command; the `DISABLE DATABASE` command only disables management of a standby database.

Note:

If you disable management of a configuration while connected to the standby database, you must connect to the primary database to reenable the configuration.

Disabling the broker's management of an object does not remove its profile from the broker configuration file. You can reenable your ability to use DGMGRL (or Enterprise Manager) to manage the object by entering the appropriate `ENABLE` `CONFIGURATION` or `ENABLE DATABASE` command.

#### 6.7.2.2 Disable a Standby Database

You use the `DISABLE DATABASE` command when you temporarily do not want the broker to manage and monitor a standby database.

You can explicitly disable broker management of a standby database to prevent it from being enabled when the rest of the configuration is enabled. Example 6-6 shows how to disable the `South_Sales` standby database.

Example 6-6 Disabling a Standby Database

```
DGMGRL> DISABLE DATABASE 'South_Sales';
Disabled.
```

Note:

You cannot disable a standby database from the configuration if fast-start failover is enabled and the database to be disabled is the target standby database.

Note:

If you disable management of a standby database while connected to that standby database, you must connect to the primary database or another enabled standby database to reenable broker-management of the standby database.

Caution:

If you disable broker management of a standby database in the broker configuration, that standby database cannot be used by the broker as a failover target in the event of loss of the primary database.

When operating under either maximum protection mode or maximum availability mode, the broker prevents you from disabling the last standby database that supports the protection mode.

### 6.7.3 Removing the Configuration or a Standby Database

When you use either the `REMOVE CONFIGURATION` or `REMOVE DATABASE` command, you effectively delete the configuration or standby database profile from the broker configuration file, removing the ability of the Data Guard broker to manage the configuration or the standby database, respectively.

A remove operation with the `PRESERVE DESTINATIONS` clause does not remove or delete the actual Data Guard configuration underneath, nor does it affect the operation of the actual Data Guard configuration and its databases.

Caution:

After you use the `REMOVE CONFIGURATION` or `REMOVE DATABASE` command, you cannot recover the configuration or database profile that was deleted from the broker configuration file. You must go through the steps in Section 6.2 as necessary, to create a broker configuration that can be managed with DGMGRL (or the Enterprise Manager).

Note:

You cannot remove a standby database from the configuration if fast-start failover is enabled and the database to be removed is the target standby database.

Step 1 Remove a standby database from the configuration.

When you use the `REMOVE DATABASE` command, broker management and monitoring of the database ceases and the database's profile is deleted from the broker configuration file.

Show the configuration before deletion of the `South_Sales` standby database:

```
DGMGRL> SHOW CONFIGURATION;
 
Configuration - DRSolution
 
  Protection Mode: MaxPerformance
  Databases:
    North_Sales  - Primary database
    South_Sales  - Physical standby database
 
Fast-Start Failover: DISABLED
 
Configuration Status:
SUCCESS
```

Issue the DGMGRL `REMOVE DATABASE` command to remove the `South_Sales` database information from the Data Guard configuration file:

```
DGMGRL> REMOVE DATABASE 'South_Sales';
Removed database "South_Sales" from the configuration
```

Show the configuration after deletion of the `South_Sales` standby database:

```
DGMGRL> SHOW CONFIGURATION;
 
Configuration - DRSolution
 
  Protection Mode: MaxPerformance
  Databases:
    North_Sales  - Primary database
 
Fast-Start Failover: DISABLED
 
Configuration Status:
SUCCESS
```

When operating under either maximum protection mode or maximum availability mode, the broker prevents you from deleting the last standby database that supports the protection mode.

Step 2 Remove the broker configuration.

Use the following command to remove the entire configuration from management and monitoring by the broker:

```
DGMGRL> REMOVE CONFIGURATION;
```

Note:

You cannot remove the configuration if fast-start failover is enabled.

DGMGRL returns the following message to indicate the command successfully removed all of the configuration information from the Data Guard configuration file:

```
Removed configuration
 
DGMGRL> SHOW CONFIGURATION;
Error: ORA-16532: Data Guard broker configuration does not exist
 
Configuration details cannot be determined by DGMGRL
```

## 6.8 Scenario 7: Performing a Switchover Operation

You can switch the role of the primary database and a standby database using the `SWITCHOVER` command. Before you issue the `SWITCHOVER` command, you must ensure:

- The state of the primary and standby databases are `TRANSPORT-ON` and `APPLY-ON`, respectively.
- All participating databases are in good health, without any errors or warnings present.
- The standby database properties were set on the primary database, so that the primary database can function correctly when transitioning to a standby database (shown in the following examples in boldface type).
- Standby redo log files on the primary database are set up, and the `LogXptMode` database property is set to `SYNC` if the configuration is operating in either maximum availability mode or maximum protection mode.
- If fast-start failover is enabled, you can perform a switchover only to the standby database that was specified as the target standby database.

Step 1 Check the primary database.

Use the `SHOW DATABASE VERBOSE` command to check the state, health, and properties of the primary database, as follows:

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
    StaticConnectIdentifier         = '(DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)
(HOST=North_Sales.example.com)(PORT=2840))
(CONNECT_DATA=(SERVICE_NAME=North_Sales_DGMGRL.example.com)
(INSTANCE_NAME=north_sales1)(SERVER=DEDICATED)))'
    StandbyArchiveLocation          = 'USE_DB_RECOVERY_FILE_DEST'
    AlternateLocation               = ''
    LogArchiveTrace                 = '255'
    LogArchiveFormat                = 'db1r_%d_%t_%s_%R.arc'
    LatestLog                       = '(monitor)'
    TopWaitEvents                   = '(monitor)'
 
Database Status:
SUCCESS
 
DGMGRL>
```

In particular, you should examine the boldface properties and the current status of the primary database. See [Chapter 4](dbresource.md) for information about managing databases.

Step 2 Check the standby database that is the target of the switchover.

Use the `SHOW DATABASE VERBOSE` command to check the state, health, and properties of the standby database that is the target of the switchover. For example:

```
DGMGRL> SHOW DATABASE VERBOSE 'South_Sales';
 
Database - South_Sales
 
  Role:            PHYSICAL STANDBY
  Intended State:  ONLINE
  Transport Lag:   0
  Apply Lag:       0
  Real Time Query: OFF
  Instance(s):
    south_sales1
Properties:
    DGConnectIdentifier             = 'South_Sales.example.com'
    ObserverConnectIdentifier       = ''
    LogXptMode                      = 'ASYNC'
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
    DbFileNameConvert               = 'dbs/t, dbs/bt'
    LogFileNameConvert              = 'dbs/t, dbs/bt'
    FastStartFailoverTarget         = 'North_Sales'
    InconsistentProperties          = '(monitor)'
    InconsistentLogXptProps         = '(monitor)'
    SendQEntries                    = '(monitor)'
    LogXptStatus                    = '(monitor)'
    RecvQEntries                    = '(monitor)'
    SidName                         = 'south_sales1'
    StaticConnectIdentifier         = '(DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)
(HOST=south_sales1.example.com)(PORT=2840))
(CONNECT_DATA=(SERVICE_NAME=South_Sales_DGMGRL.example.com)
(INSTANCE_NAME=south_sales1)(SERVER=DEDICATED)))'
    StandbyArchiveLocation          = 'USE_DB_RECOVERY_FILE_DEST'
    AlternateLocation               = ''
    LogArchiveTrace                 = '255'
    LogArchiveFormat                = 'db2r_%d_%t_%s_%R.arc'
    LatestLog                       = '(monitor)'
    TopWaitEvents                   = '(monitor)'
 
Database Status:
SUCCESS
```

In particular, you should examine the current status of the database.

Step 3 Issue the switchover command.

Issue the `SWITCHOVER` command to swap the roles of the primary and standby databases. The following example shows how the broker automatically shuts down and restarts the old primary database as a part of the switchover. (See the usage notes in [Section 7.1.3](dgmgrl.md) for information about how to set up the broker environment so that DGMGRL can automatically restart the primary and standby databases for you.)

```
DGMGRL> switchover to 'South_Sales';
Performing switchover NOW, please wait...
New primary database "South_Sales" is opening...
Operation requires shutdown of instance "north_sales1" on database "North_Sales"
Shutting down instance "north_sales1"...
ORA-01109: database not open
 
Database dismounted.
ORACLE instance shut down.
Operation requires startup of instance "north_sales1" on database "North_Sales"
Starting instance "north_sales1"...
ORACLE instance started.
Database mounted.
Switchover succeeded, new primary is "South_Sales"
```

After the switchover completes, use the `SHOW CONFIGURATION` and `SHOW DATABASE` commands to verify that the switchover operation was successful.

Step 4 Show the configuration.

Issue the `SHOW CONFIGURATION` command to verify that the switchover was successful.

```
DGMGRL> SHOW CONFIGURATION;
 
Configuration - DRSolution
 
  Protection Mode: MaxAvailability
  Databases:
    South_Sales  - Primary database
    North_Sales  - Physical standby database
 
Fast-Start Failover: DISABLED
 
Configuration Status:
SUCCESS
```

## 6.9 Scenario 8: Performing a Manual Failover Operation

You invoke a failover operation in response to an emergency situation, usually when the primary database cannot be accessed or is unavailable. See [Section 5.2](sofo.md) before you fail over to decide which standby database should be the target of the failover. The following scenario describes a failover to the remote database called `South_Sales`.

Note:

If fast-start failover is enabled, you can perform a manual failover only to the standby database that was specified as the target of a fast-start failover and only when the observer is running and currently has connectivity with the standby database.

If you want to perform a manual failover to a standby database that is not the fast-start failover target standby database, you must first disable fast-start failover using the `FORCE` option on the standby database you want to fail over. See [Section 5.5.5, "Disabling Fast-Start Failover"](sofo.md) for more information about the `FORCE` option.

Step 1 Connect to the target standby database.

To perform the failover operation, you must connect to the standby database to which you want to fail over to as a user that has the `SYSDBA` privilege. For example:

```
DGMGRL> CONNECT sys@South_Sales.example.com;
Password: password
Connected.
```

Step 2 Issue the failover command.

Now you can issue the failover command to make the target standby database the new primary database for the configuration.

```
DGMGRL> FAILOVER TO 'South_Sales';
Performing failover NOW, please wait...
Failover succeeded, new primary is "South_Sales"
```

Note that after the failover completes, the original primary database cannot be used as a standby database of the new primary database unless it is reinstated or re-created (as described in [Section 5.4.3](sofo.md)).

Step 3 Show the configuration.

Issue the `SHOW CONFIGURATION` command to verify the failover.

```
DGMGRL> SHOW CONFIGURATION;
 
Configuration - DRSolution
 
  Protection Mode: MaxAvailability
  Databases:
    South_Sales  - Primary database
      Warning: ORA-16629: database reports a different protection level from the protection mode
 
    North_Sales - Physical standby database (disabled)
      ORA-16661: the standby database needs to be reinstated
 
Fast-Start Failover: DISABLED
 
Configuration Status:
WARNING
```

Note that in this example, the configuration was operating in maximum availability mode. The protection mode was preserved after the failover. The configuration also has a warning status. The `SHOW DATABASE` command for the new primary shows that the warning is the result of not having an enabled physical standby database. As a result, the warning status indicates that the protection level of the configuration is not the same as the configured mode.

Step 4 Show the new primary database.

```
DGMGRL> SHOW DATABASE South_Sales;
Database - South_Sales
 
  Role:            PRIMARY
  Intended State:  TRANSPORT-ON
  Instance(s):
    south_sales1
 
  Database Warning(s):
    ORA-16629: database reports a different protection level from the protection mode
 
Database Status:
WARNING
```

Step 5 Show the old primary database.

Issue the `SHOW DATABASE` command to see that the former (failed) primary database was disabled by the broker as a consequence of the failover. It must be reinstated (as described in [Section 5.4.3](sofo.md)).

```
DGMGRL> SHOW DATABASE 'North_Sales';
Database - North_Sales
 
  Role:            PHYSICAL STANDBY
  Intended State:  APPLY-ON
  Transport Lag:   (unknown)
  Apply Lag:       (unknown)
  Real Time Query: OFF
  Instance(s):
    north_sales1
 
Database Status:
ORA-16661: the standby database needs to be reinstated
```

## 6.10 Scenario 9: Reinstating a Failed Primary Database

If your primary database had been configured with Flashback Database, you can easily reinstate the failed primary database as a standby database of the new primary database. The failed primary database will be reinstated as a standby type that matches the old standby database. For example, if you failed over to a physical standby database, the old primary will be reinstated as a physical standby database.

To reinstate the failed primary database, start it to the mounted state. Then run DGMGRL, connect to the new primary database and reinstate the old primary database.

Step 1 Restart the Old Primary Database.

```
% sqlplus sys as sysdba
Enter password: password

SQL> STARTUP MOUNT;
ORACLE instance started.
 
Total System Global Area  234364928 bytes
Fixed Size                  1296352 bytes
Variable Size             209717280 bytes
Database Buffers           16777216 bytes
Redo Buffers                6574080 bytes
Database mounted.
```

Step 2 Reinstate the old primary database.

```
% dgmgrl connect sys
Password: password
Connected.
DGMGRL> REINSTATE DATABASE 'North_Sales';
Reinstating database "North_Sales", please wait...
Operation requires shutdown of instance "north_sales1" on database "North_Sales"
Shutting down instance "north_sales1"...
ORA-01109: database not open
 
Database dismounted.
ORACLE instance shut down.
Operation requires startup of instance "north_sales1" on database "North_Sales"
Starting instance "north_sales1"...
ORACLE instance started.
Database mounted.
Continuing to reinstate database "North_Sales" ...
Reinstatement of database "North_Sales" succeeded
```

After the primary has been reinstated, issue the `SHOW CONFIGURATION` and `SHOW DATABASE` commands to confirm that the old primary has been successfully reinstated.

Step 3 Show the Configuration and Databases.

```
DGMGRL> SHOW CONFIGURATION
 
Configuration - DRSolution
 
  Protection Mode: MaxAvailability
  Databases:
    South_Sales  - Primary database
    North_Sales  - Physical standby database
 
Fast-Start Failover: DISABLED
 
Configuration Status:
SUCCESS

DGMGRL> SHOW DATABASE 'South_Sales';
 
Database - South_Sales
 
  Role:            PRIMARY
  Intended State:  TRANSPORT-ON
  Instance(s):
    south_sales1
 
Database Status:
SUCCESS
 
DGMGRL> SHOW DATABASE 'North_Sales'
 
Database - North_Sales
 
  Role:            PHYSICAL STANDBY
  Intended State:  APPLY-ON
  Transport Lag:   0 seconds
  Apply Lag:       0 seconds
  Real Time Query: OFF
  Instance(s):
    north_sales1
 
Database Status:
SUCCESS
```

## 6.11 Scenario 10: Converting a Physical Standby to a Snapshot Standby

If you have a physical standby database that you would like to convert to a snapshot standby database, use the DGMGRL `CONVERT DATABASE` command. Redo data will continue to be received by the database while it is operating as a snapshot standby database, but it will not be applied until the snapshot standby is converted back into a physical standby database.

A physical standby database must be configured with a fast recovery area to convert it to a snapshot standby database. This is because a guaranteed restore point is created during the conversion process, and guaranteed restore points require a fast recovery area.

```
DGMGRL> convert database 'South_Sales' to snapshot standby;
Converting database "South_Sales" to a Snapshot Standby database, please wait...
Database "South_Sales" converted successfully

DGMGRL> SHOW CONFIGURATION;
 
Configuration - DRSolution
 
  Protection Mode: MaxPerformance
  Databases:
    North_Sales  - Primary database
    South_Sales  - Snapshot standby database
 
Fast-Start Failover: DISABLED
 
Configuration Status:
SUCCESS
```

When you are ready to revert the database back to a physical standby database, use the DGMGRL `CONVERT DATABASE` command again as follows. Any updates made to the database while it was operating as a snapshot standby database will be discarded. All accumulated redo data will be applied by Redo Apply services after the database is converted back to a physical standby database.

```
DGMGRL> CONVERT DATABASE 'South_Sales' to PHYSICAL STANDBY;
Converting database "South_Sales" to a Physical Standby database, please wait...
Operation requires shutdown of instance "south_sales1" on database "South_Sales"
Shutting down instance "south_sales1"...
Database closed.
Database dismounted.
ORACLE instance shut down.
Operation requires startup of instance "south_sales1" on database "South_Sales"
Starting instance "south_sales1"...
ORACLE instance started.
Database mounted.
Continuing to convert database "South_Sales" ...
Operation requires shutdown of instance "south_sales1" on database "South_Sales"
Shutting down instance "south_sales1"...
ORA-01109: database not open
Database dismounted.
ORACLE instance shut down.
Operation requires startup of instance "south_sales1" on database "South_Sales"
Starting instance "south_sales1"...
ORACLE instance started.
Database mounted.
Database "South_Sales" converted successfully
```

## 6.12 Scenario 11: Monitoring a Data Guard Configuration

The scenario in this section demonstrates how to use the `SHOW` command and monitorable database properties to identify and resolve a failure situation.

Step 1 Check the configuration status.

The status of the broker configuration is an aggregated status of all databases and instances in the broker configuration. You can check the configuration status first to determine whether or not any further action needs to be taken. If the configuration status is SUCCESS, everything in the broker configuration is working properly. However, if you see a status of WARNING or ERROR, then something is wrong in the configuration.

For example, in the following display, you can see that the primary database has multiple warnings:

```
DGMGRL> SHOW CONFIGURATION;
Configuration - DRSolution
 
  Protection Mode: MaxPerformance
  Databases:
    North_Sales  - Primary database
      Warning: ORA-16809: multiple warnings detected for the database
 
    South_Sales  - Physical standby database
 
Fast-Start Failover: DISABLED
 
Configuration Status:
WARNING
```

Step 2 Check the database status.

To identify the warnings on the primary database, show its status using the `SHOW DATABASE` command:

```
DGMGRL> SHOW DATABASE 'North_Sales';
Database - North_Sales
 
  Role:            PRIMARY
  Intended State:  TRANSPORT-ON
  Instance(s):
    north_sales1
      Warning: ORA-16737: the redo transport service for standby "South_Sales" has an error
      Warning: ORA-16714: the value of property LogArchiveTrace is inconsistent with the database setting
      Warning: ORA-16715: redo transport-related property ReopenSecs of standby
 database "South_Sales" is inconsistent

Database Status:
WARNING
```

Step 3 Check the LogXptStatus monitorable database property.

The `SHOW DATABASE` output in step 2 shows a Warning for error ORA-16737. To identify the exact transport error, use the `LogXptStatus` monitorable database property:

```
DGMGRL> SHOW DATABASE 'North_Sales' 'LogXptStatus';
LOG TRANSPORT STATUS
PRIMARY_INSTANCE_NAME  STANDBY_DATABASE_NAME  STATUS 
         north_sales1            South_Sales  ORA-12541: TNS:no listener
```

The output shows that the listener for the physical standby database is not running. To fix this error, start the listener for the physical standby database `South_Sales`.

Step 4 Check the InconsistentProperties monitorable database property.

The `SHOW DATABASE` output in step 2 also shows a Warning for error ORA-16714. To identify the exact error, use the `InconsistentProperties` monitorable database property:

```
DGMGRL> SHOW DATABASE 'North_Sales' 'InconsistentProperties';
INCONSISTENT PROPERTIES
 INSTANCE_NAME  PROPERTY_NAME   MEMORY_VALUE SPFILE_VALUE BROKER_VALUE
 north_sales1   LogArchiveTrace 511          255          255
```

The current database memory value (511) is different from both the server parameter file (SPFILE) value (255) and the Data Guard broker's property value (255). If you decide the database memory value is correct, you can update the Data Guard broker's property value using the following command:

```
DGMGRL> EDIT DATABASE 'North_Sales' SET PROPERTY 'LogArchiveTrace'=511;
Property "LogArchiveTrace" updated
```

This command will result in the broker updating the SPFILE value so that the value of `LogArchiveTrace` is kept consistent.

Step 5 Check the InconsistentLogXptProps monitorable database property.

Another warning shown in the `SHOW DATABASE` display in Step 2 is ORA-16715. To identify the inconsistent values for the redo transport database property, `ReopenSecs`, you can use the `InconsistentLogXptProps` monitorable database property:

```
DGMGRL> SHOW DATABASE 'North_Sales' 'InconsistentLogXptProps';
INCONSISTENT LOG TRANSPORT PROPERTIES
 INSTANCE_NAME  STANDBY_NAME  PROPERTY_NAME  MEMORY_VALUE  BROKER_VALUE 
   south_sales1   South_Sales     ReopenSecs           600           300
```

The current database memory value (600) is different from the Data Guard broker's property value (300). If you think the broker's property value is correct, you can fix the inconsistency by re-editing the property of the standby database with the same value, as shown in the following example:

```
DGMGRL> EDIT DATABASE 'South_Sales' SET PROPERTY 'ReopenSecs'=300;
Property "ReopenSecs" updated
```

You can also reenable the standby database or reset the state of the primary database to `TRANSPORT-ON` to fix this inconsistency.