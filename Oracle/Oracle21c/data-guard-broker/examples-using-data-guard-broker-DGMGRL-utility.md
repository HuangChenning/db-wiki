---
title: Broker
book: Data Guard Broker
doc_id: F31839-04
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/dgbkr/examples-using-data-guard-broker-DGMGRL-utility.html
tags:
  - oracle
  - 21c
  - data-guard-broker
---

Use these scenarios to help you understand what you need to do to start creating, managing, and using an Oracle Data Guard broker configuration.

Read the information about prerequisites for getting started using the Oracle Data Guard command-line interface (DGMGRL), so that you can prepare your instances. Then read the scenarios to understand how you can use DGMGRL to create, manage, and monitor a broker configuration.

### Prerequisites for Getting Started

One of the prerequisites for using DGMGRL is that a primary database and any standby databases must already exist.

The `DG_BROKER_START` initialization parameter must be set to `TRUE` for all databases in the configuration. You must use a server parameter file with the broker.

Convert the initialization parameter files (PFILE) on both primary and standby databases into server parameter files (SPFILE), if necessary. Use the following SQL\*Plus command:

```
CREATE SPFILE='spfilename' FROM PFILE='pfilename';
```

If an instance was not started with a server parameter file, then you must shut down the instance and restart it using the server parameter file.

After starting the Oracle instance, set the `DG_BROKER_START=TRUE` initialization parameter using the SQL `ALTER SYSTEM` statement. The parameter value will be saved in the server parameter file. The next time you start the Oracle instance, the broker is started automatically, and you do not need to issue the SQL `ALTER SYSTEM` statement again.

The following assumptions are made in these scenarios:

- TCP/IP is used to connect to primary and standby databases.
- The standby database has been created from backups of the primary database control files and datafiles as described in the [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/dgbkr&id=SBYDB00210).
- The scenarios assume the following broker configuration:
	- The configuration name is `DRSolution`.
		- The database unique name (`DB_UNIQUE_NAME`) of the primary database is `North_Sales`.
		- The database unique name (`DB_UNIQUE_NAME`) of the remote standby database is `South_Sales`.
		- The protection mode is maximum performance mode.
		- There are standby redo log files configured for both the primary and standby database. The transport mode for both databases is `ASYNC`.
		- The standby database is a physical standby database.

### Scenario 1: Creating a Configuration

These examples create a broker configuration named `DRSolution` that includes a primary and standby database named `North_Sales` and `South_Sales`.

To create a configuration and add one physical standby database, perform the following tasks:

- Creating a Configuration Task 1: Invoke DGMGRL
- Creating a Configuration Task 2: Connect to the Primary Database
- Creating a Configuration Task 3: Clear Existing Remote Redo Transport Destinations
- Creating a Configuration Task 4: Create the Broker Configuration
- Creating a Configuration Task 5: Show the Configuration Information
- Creating a Configuration Task 6: Add a Standby Database to the Configuration

#### Creating a Configuration Task 1: Invoke DGMGRL

To start DGMGRL, enter `dgmgrl` at the command-line prompt on a system where Oracle Data Guard is installed.

```
$ dgmgrl
```

The DGMGRL prompt is displayed:

```
DGMGRL>
```

#### Creating a Configuration Task 2: Connect to the Primary Database

Before you specify any command (other than the `HELP,` `EXIT,` or `QUIT`), you must first connect to the primary database using the DGMGRL `CONNECT` command.

The account from which you connect to the database (`SYS` in this example) must have `SYSDG` or `SYSDBA` privileges on the primary and standby databases.

Note:

If no `AS` clause is specified on the `CONNECT` command, the connection is made as `SYSDBA`.

The following examples show two variations of the `CONNECT` command. Example 8-1 shows how to connect to the default database on the local system, and Example 8-2 includes the Oracle Net Services connect identifier (`North_Sales.example.com`) to make a connection to a database located on a remote system. In both examples, you are prompted for a password.

Example 8-1 Connecting to the Primary Database on the Local System

```
DGMGRL> CONNECT sysdg;
Password: password
Connected to "North_Sales"
Connected as SYSDG.
```

Example 8-2 Connecting to the Primary Database on a Remote System

```
DGMGRL> CONNECT sysdg@North_Sales.example.com;
Password: password
Connected to "North_Sales"
Connected as SYSDG.
```

#### Creating a Configuration Task 3: Clear Existing Remote Redo Transport Destinations on Standbys and Far Sync Instances To Be Added.

You must clear any remote redo transport destinations on standby databases and far sync instances before those standbys and far syncs can be added to a configuration.

If the remote redo transport destinations are not cleared, then the following error message is returned when you attempt to create the configuration:

```
ORA-16698: LOG_ARCHIVE_DEST_n parameter set for object to be added
 
Failed.
```

To clear `LOG_ARCHIVE_DEST_` `n` settings, use the `ALTER SYSTEM SET LOG_ARCHIVE_DEST_n=" "` SQL\*Plus command.

Remote redo transport destinations on the primary (whether they have the `REGISTER` or `NOREGISTER` attribute) can be left as is.

#### Creating a Configuration Task 4: Create the Broker Configuration

A broker configuration is initially created with just a primary database.

In this case, the primary is called `North_Sales`. In a later command, you will add the standby database, `South_Sales`.

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

#### Creating a Configuration Task 5: Show the Configuration Information

Use the `SHOW CONFIGURATION` command to display a brief summary of the configuration.

```
DGMGRL> SHOW CONFIGURATION;
```

DGMGRL returns the following information:

```
Configuration - DRSolution
 
  Protection Mode: MaxPerformance
  Members:
    North_Sales - Primary database
 
Fast-Start Failover: DISABLED
 
Configuration Status:
DISABLED
```

#### Creating a Configuration Task 6: Add a Standby Database to the Configuration

To add a standby database to the `DRSolution` configuration, use the `ADD DATABASE` command.

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
  Members:
    North_Sales  - Primary database
      South_Sales  - Physical standby database
 
Fast-Start Failover: DISABLED
 
Configuration Status:
DISABLED
 
DGMGRL>
```

### Scenario 2: Setting Database Properties

After you create the configuration with DGMGRL, you can set database properties at any time.

For example, the following statement sets the `StandbyArchiveLocation` database property for the `South_Sales` standby database:

```
DGMGRL> EDIT DATABASE 'South_Sales' SET PROPERTY 'StandbyArchiveLocation'='/archfs/arch/';
Property "StandbyArchiveLocation" updated.
```

Use the `SHOW DATABASE VERBOSE` command to view all properties and their values for a database. The following example shows the properties for the `South_Sales` database.

```
DGMGRL> SHOW DATABASE VERBOSE 'South_Sales'

Database - South_Sales

  Role:               PHYSICAL STANDBY
  Intended State:     APPLY-ON
  Transport Lag:      0 seconds (computed 0 seconds ago)
  Apply Lag:          0 seconds (computed 0 seconds ago)
  Average Apply Rate: 2.00 KByte/s
  Active Apply Rate:  0 Byte/s
  Maximum Apply Rate: 0 Byte/s
  Real Time Query:    ON
  Instance(s):
    South_sales1

  Properties:
    DGConnectIdentifier             = 'South_Sales.example.com'
    ObserverConnectIdentifier       = ''
    FastStartFailoverTarget         = ''
    PreferredObserverHosts          = ''
    LogShipping                     = 'ON'
    RedoRoutes                      = ''
    LogXptMode                      = 'ASYNC'
    DelayMins                       = '0'
    Binding                         = 'optional'
    MaxFailure                      = '0'
    ReopenSecs                      = '300'
    NetTimeout                      = '30'
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
    HostName                        = 'South_Sales.example.com'
    StaticConnectIdentifier         = '(DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=tcp)(HOST=South_Sales.example.com)(PORT=2879)))(CONNECT_DATA=(SERVICE_NAME=South_Sales_DGMGRL.example.com)(INSTANCE_NAME=south_sales1)(SERVER=DEDICATED)))'
    TopWaitEvents                   = '(monitor)'
    SidName                         = '(monitor)'

  Log file locations:
    Alert log               : /db/oracle/log/diag/rdbms/South_Sales/south_sales1/trace/alert_south_sales1.log
    Data Guard Broker log   : /db/oracle/log/diag/rdbms/South_Sales/south_sales1/trace/drcsouth_sales1.log

Database Status:
SUCCESS
```

If broker management of the database is enabled, setting a database property value causes the underlying parameter value to be changed in the corresponding database, and the value for the changed parameter is reflected in the server parameter file. Thus, if the database is shut down and restarted outside of Oracle Enterprise Manager Cloud Control (Cloud Control) and DGMGRL (such as from the SQL\*Plus interface), the database uses the new parameter values from the updated server parameter file when it starts. However, you should not make changes to the redo transport services initialization parameters through SQL statements. Doing so will cause an inconsistency between the database and the broker.

Note:

The database properties are typically displayed in mixed-case (for example, `LogXptMode`) typeface to help you visually differentiate database properties (from the corresponding initialization parameter, SQL statement, or PL/SQL procedure), which are typically documented in `UPPERCASE` typeface. However, the commands to manage properties are not case sensitive; you can issue commands in uppercase, lowercase, or mixed-case.

You can change a property if the database is enabled or disabled. However, if the database is disabled when you change a property, the change does not take effect until the database is enabled.

### Scenario 3: Enabling the Configuration and Databases

So far, the `DRSolution` configuration is disabled, which means it is not under the control of the Data Guard broker.

When you finish configuring the databases into a broker configuration and setting any necessary database properties, you must enable the configuration to allow the Data Guard broker to manage it.

You can enable:

- The entire configuration, including all of its databases
- A standby database

Enable the entire configuration

You can enable the entire configuration, including all of the databases, with the following command:

```
DGMGRL> ENABLE CONFIGURATION;
Enabled.
```

Show the configuration

Use the `SHOW` command to verify that the configuration and its databases were successfully enabled:

```
DGMGRL> SHOW CONFIGURATION;
```

DGMGRL returns the following information:

```
Configuration - DRSolution
 
  Protection Mode: MaxPerformance
  Members:
    North_Sales  - Primary database
      South_Sales  - Physical standby database
 
Fast-Start Failover: DISABLED
 
Configuration Status:
SUCCESS
```

Enable the database

This step is unnecessary except if the standby database was previously disabled with the `DISABLE DATABASE` command. Normally, enabling the configuration also enables the standby database.

```
DGMGRL> ENABLE DATABASE 'South_Sales';
Enabled.
```

Show the database

```
DGMGRL> SHOW DATABASE 'South_Sales';

Database - South_Sales
 
  Role:             PHYSICAL STANDBY
  Intended State:   APPLY-ON
  Transport Lag:    0 seconds (computed 1 second ago)
  Apply Lag:        0 seconds (computed 1 second ago)
  Apply Rate:       1.54 MByte/s
  Real Time Query:  OFF
  Instance(s):
    south_sales1
 
Database Status:
SUCCESS
```

### Scenario 4: Setting the Configuration Protection Mode

You can change the protection mode of the configuration at any time.

Note:

You cannot change the protection mode from maximum performance mode to maximum protection mode. You must first change the protection mode to maximum availability and then to maximum protection mode.

A restart of the primary database is not necessary when changing the protection mode.

This scenario sets the protection mode of the configuration to the `MAXAVAILABILITY` mode. Note that this protection mode requires that there be at least one standby configured to use standby redo log files and it must receive redo via `SYNC` or `FASTSYNC` mode if it receives redo directly from the primary database. If the standby receives redo via a far sync instance, then the far sync instance must receive redo via `SYNC` or `FASTYSYNC` mode and the standby must receive redo from the far sync instance via `ASYNC` mode.

1. Configure standby redo log files, if necessary.
	Because you will be setting the protection mode to the `MAXAVAILABILITY` mode, it is important to ensure that sufficient standby redo log files are configured on the standby database. For more information on setting up redo transport, see [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/dgbkr&id=SBYDB-GUID-04851F96-F8F3-4999-AAAD-83C4C3C7AE14).
2. Configure redo transport mode appropriately.
	Configure the standby to receive redo via `SYNC` or `FASTSYNC` mode, if the standby receives redo directly from the primary database. If the standby receives primary redo via a far sync instance, then configure the far sync instance to receive redo via `SYNC` or `FASTSYNC` mode and configure the standby to receive redo via `ASYNC` mode. For example:
	```
	DGMGRL> EDIT DATABASE 'South_Sales' SET PROPERTY 'LogXptMode'='SYNC';
	Property "LogXptMode" updated
	```
	The broker will not allow this command to succeed unless the standby database is configured with standby redo log files in the configuration.
3. Change the overall protection mode for the configuration.
	Use the `EDIT` `CONFIGURATION` command to upgrade the broker configuration to the `MAXAVAILABILITY` protection mode:
	```
	DGMGRL> EDIT CONFIGURATION SET PROTECTION MODE AS MAXAVAILABILITY;
	Succeeded.
	```
	If the configuration is disabled when you enter this command, the actual protection mode change is not applied until you enable the configuration with the `ENABLE CONFIGURATION` command. The broker will not allow you to enable the configuration if it does not find a standby database in the configuration that can support the requirements of the protection mode.
4. Verify the protection mode has changed.
	Use the `SHOW CONFIGURATION` command to display the current protection mode for the configuration:
	```
	DGMGRL> SHOW CONFIGURATION;
	 
	Configuration - DRSolution
	 
	  Protection Mode: MaxAvailability
	  Members:
	    North_Sales  - Primary database
	      South_Sales  - Physical standby database
	 
	Fast-Start Failover: DISABLED
	 
	Configuration Status:
	SUCCESS
	```
	See Also:
	[Managing Data Protection Modes](managing-oracle-data-guard-broker-configuration-members.md)

### Scenario 5: Setting up Maximum Availability Mode with a Far Sync Instance

A far sync instance can be used with maximum availability protection mode if the primary and standby database are geographically far enough apart to make the use of synchronous transport mode impractical.

The example in this tpoic shows how to add a far sync instance to the configuration and then set up the `RedoRoutes` property for all members of the configuration. Setting of `RedoRoutes` property for the far sync instance enables it to send redo data based on either the `North_Sales` or `South_Sales` database being the primary.

1. Issue the following commands to add the far sync instance named `FS` to the broker configuration:
	```
	DGMGRL> ADD FAR_SYNC 'FS' AS CONNECT IDENTIFIER IS FS.EXAMPLE.COM;
	DGMGRL> ENABLE FAR_SYNC 'FS';
	DGMGRL> SHOW CONFIGURATION;
	  
	Configuration - DRSolution
	 
	  Protection Mode: MaxPerformance
	  Members:
	  North_Sales - Primary database
	    South_Sales - Physical standby database
	    FS - Far Sync
	 
	Fast-Start Failover: DISABLED
	 
	Configuration Status:
	SUCCESS
	```
	In this output, `South_Sales` and `FS` are indented under `North_Sales`. This indicates that the primary is sending redo data to both `South_Sales` and `FS`.
2. Issue the following commands so that the current primary (`North_Sales`) sends redo data to the far sync instance only, and the far sync instance sends redo data to `South_Sales` when `North_Sales` is a primary:
	```
	DGMGRL> EDIT DATABASE 'North_Sales' SET PROPERTY RedoRoutes='(LOCAL : FS SYNC)';
	DGMGRL> EDIT FAR_SYNC 'FS' SET PROPERTY RedoRoutes='(North_Sales : South_Sales');
	DGMGRL> SHOW CONFIGURATION;
	 
	DGMGRL> SHOW CONFIGURATION;
	 
	Configuration - DRSolution
	 
	  Protection Mode: MaxPerformance
	  Members:
	  North_Sales - Primary database
	    FS - Far Sync
	      South_Sales - Physical standby database
	 
	Fast-Start Failover: DISABLED
	 
	Configuration Status:
	SUCCESS
	```
	The indentation scheme in the output above indicates that `North_Sales` sends redo data to `FS` and `FS` sends redo data to `South_Sales`.
3. Issue the following commands to upgrade the protection mode to maximum availability:
	```
	DGMGRL> EDIT CONFIGURATION SET PROTECTION MODE AS MaxAvailability;
	DGMGRL> SHOW CONFIGURATION;
	 
	Configuration - DRSolution
	 
	  Protection Mode: MaxAvailability
	  Members:
	  North_Sales - Primary database
	    FS - Far Sync
	      South_Sales - Physical standby database
	 
	Fast-Start Failover: DISABLED
	 
	Configuration Status:
	SUCCESS
	```
	If `South_Sales` ever becomes the primary and `North_Sales` becomes a standby database that receives redo data from the far sync instance, `FS`, then the `RedoRoutes` property must be set for `South_Sales`. Additionally, a new rule must be included in the `RedoRoutes` property for `FS` to allow it to send redo data to `North_Sales` when `South_Sales` is the primary database.
	If these rules are not created, then `North_Sales` will not be able to receive redo data. To check whether the proper rules have been set, use the `SHOW` `CONFIGURATION` `WHEN` `PRIMARY` `IS` command to see what the redo transport configuration would be if `South_Sales` were the primary database. For example:
	```
	DGMGRL> SHOW CONFIGURATION WHEN PRIMARY IS 'South_Sales';
	 
	Configuration when South_Sales is primary - DRSolution
	 
	  Members:
	  South_Sales  - Primary database
	    FS     - Far Sync 
	      North_Sales  - Physical standby database 
	 
	  Members Not Receiving Redo:
	  North_FS - Physical standby database
	  Warning: ORA-16685: database does not receive redo data
	```
	To correct this error, set the `RedoRoutes` property for `South_Sales` and `FS` as follows:
	```
	DGMGRL> EDIT DATABASE 'South_Sales' SET PROPERTY RedoRoutes='(LOCAL : FS SYNC)';
	DGMGRL> EDIT FAR_SYNC 'FS' SET PROPERTY RedoRoutes=('North_Sales : South_Sales)(South_Sales : North_Sales)';
	```
	After the change to the `RedoRoutes` property for `South_Sales` and `FS` is complete, use the `SHOW` `CONFIGURATION` `WHEN` `PRIMARY` `IS` command to confirm that the error has been cleared:
	```
	DGMGRL> SHOW CONFIGURATION WHEN PRIMARY IS 'South_Sales';
	 
	Configuration when South_Sales is primary - DRSolution
	 
	  Members:
	  South_Sales  - Primary database
	    FS     - Far Sync 
	      North_Sales  - Physical standby database
	```

### Scenario 6: Enabling Fast-Start Failover and Starting the Observer

You can enable fast-start failover from any site, including the observer site, while connected to any database in the broker configuration.

Enabling fast-start failover does not trigger a failover. Instead, it allows the observer that is monitoring the configuration to initiate a fast-start failover if conditions warrant a failover. This section describes the steps to enable fast-start failover and start the observer where the configuration protection mode is set to maximum availability mode.

1. Ensure standby redo logs are configured on the primary and target standby databases. You must stop log apply services prior to configuring standby redo logs.
	See Also:
	[Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/dgbkr&id=SBYDB00426) for instructions on configuring standby redo log files
2. Configure the primary and standby databases to receive redo via `SYNC` or `FASTSYNC` or `ASYNC` mode, if they receive redo directly rather than via a far sync instance. If either database receives redo via a far sync instance, then configure the far sync instance to receive redo via `SYNC` or `FASTSYNC` mode and configure the database to receive redo via `ASYNC` mode. For example:
	```
	DGMGRL> EDIT DATABASE 'North_Sales' SET PROPERTY 'LogXptMode'='SYNC';
	Property "LogXptMode" updated
	```
	```
	DGMGRL> EDIT DATABASE 'South_Sales' SET PROPERTY 'LogXptMode'='SYNC';
	Property "LogXptMode" updated
	```
	The broker does not allow these commands to succeed unless the databases are configured with standby redo log files.
3. If you have two or more standby databases, set up the `FastStartFailoverTarget` configuration property on the primary database to indicate the desired target standby database. The broker reciprocally sets this property for the target standby database to indicate the primary database as its future target standby database when fast-start failover is actually enabled. There is no need for you set this property on the target standby as this is done for you automatically. For example:
	```
	DGMGRL> EDIT DATABASE 'North_Sales' SET PROPERTY FastStartFailoverTarget='South_Sales';
	Property "FastStartFailoverTarget" updated
	```
4. If it is necessary to upgrade the protection mode, use the following DGMGRL `EDIT CONFIGURATION` command. For example:
	```
	DGMGRL> EDIT CONFIGURATION SET PROTECTION MODE AS MAXAVAILABILITY;
	```
5. If it is not already enabled on the primary and standby databases, enable Flashback Database by issuing the following statements on each database (This examples assumes the database is already in archive log mode):
	```
	ALTER SYSTEM SET DB_FLASHBACK_RETENTION_TARGET=4320 SCOPE=BOTH;
	ALTER DATABASE ARCHIVELOG;
	ALTER SYSTEM SET db_recovery_file_dest_size=<size>;
	ALTER SYSTEM SET db_recovery_file_dest=<directory-specification>;
	ALTER DATABASE FLASHBACK ON;
	```
	Ensure that the `DB_FLASHBACK_RETENTION_TARGET` initialization parameter is set to a sufficiently large value so that reinstatement is still possible after a prolonged outage.
6. Start up to four observers by logging into the observer computers and running DGMGRL. Connect to the configuration as a user who has the `SYSDG` or `SYSDBA` privilege and then issue the `START OBSERVER` command. Note that the command does not return; that is you will not get the DGMGRL prompt after issuing the command. Make sure Redo Apply has been stopped before enabling flashback database.
	```
	DGMGRL> CONNECT sysdg@North_Sales.example.com;
	Password: password
	Connected to "North_Sales"
	Connected as SYSDG.
	DGMGRL> START OBSERVER observer1 IN BACKGROUND
	> FILE IS /net/sales/dat/oracle/broker/fsfo.dat
	> LOGFILE IS /net/sales/dat/oracle/broker/observer.log
	> CONNECT IDENTIFIER IS North_Sales
	Submitted command "START OBSERVER" using connect identifier "North_Sales"
	```
	Oracle recommends using this command format for security reasons; no credentials are visible. This practice prevents other users on the system from using a utility (for example, the UNIX ps utility) to display connection credentials. It also prevents clear-text passwords from being visible on the user's terminal.
	When starting the observer from a script, Oracle recommends that you use a method that supports 'connect /', so that database connection credentials do not have to be embedded within the script. If you choose to use a client-side Oracle Wallet as a secure external password store (see [Oracle Database Enterprise User Security Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/dgbkr&id=DBIMI160)), be sure to add credentials for both the primary and fast-start failover target standby databases. The database connect string that you specify when adding the credentials for each database must match the `ObserverConnectIdentifer` or `DGConnectIdentifier` database property.
	When multiple observers are started, one observer is the master observer after fast-start failover is enabled, and the remaining observers are backup observers. Only the master observer can coordinate fast-start failover with Data Guard broker. If the primary and target standby databases stay connected but the connection to the master observer is lost, then the broker tries to nominate a backup observer as the new master observer.
7. Enable fast-start failover. You can enable fast-start failover while connected to any database system in the broker configuration. For example:
	```
	DGMGRL> ENABLE FAST_START FAILOVER;
	Enabled in Zero Data Loss Mode.
	```
8. Verify the fast-start failover configuration. Use the `SHOW FAST_START FAILOVER` command to display the fast-start failover settings:
	```
	DGMGRL> SHOW FAST_START FAILOVER;
	 
	Fast-Start Failover: DISABLED
	 
	  Protection Mode: MaxAvailability
	  Lag Limit: 0 seconds
	  Threshold: 30 seconds
	  Ping Interval: 3000 milliseconds
	  Ping Retry: 0
	  Active Target: (none)
	  Potential Targets: "South_Sales"
	    South_Sales valid
	  Observer: observer.example.com
	  Shutdown Primary: TRUE
	  Auto-reinstate: TRUE
	  Observer Reconnect: (none)
	  Observer Override: FALSE 
	Configurable Failover Conditions
	 Health Conditions:
	  Corrupted Controlfile  YES
	  Corrupted Dictionary   YES
	  Inaccessible Logfile    NO
	  Stuck Archiver          NO
	  Datafile Write Errors  YES
	 
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

### Scenario 7: Enabling Fast-Start Failover When a Far Sync Instance Is In Use

Fast-start failover can be enabled in maximum availability mode when the fast-start failover target is a logical or physical standby database that receives redo data from a far sync instance.

To enable fast-start failover when a far sync instance is used to ship redo data to the standby database, the `FastStartFailoverTarget` property must first be set on both the primary and target standby database, as follows:

```
DGMGRL> EDIT DATABASE 'North_Sales' SET PROPERTY FastStartFailoverTarget='South_Sales';
DGMGRL> EDIT DATABASE 'South_Sales' SET PROPERTY FastStartFailoverTarget='North_Sales';
```

Then, fast-start failover can be enabled, as follows:

```
DGMGRL> ENABLE FAST_START FAILOVER;
```

Note that the far sync instance database is not specified as the fast-start failover target for either `North_Sales` or `South_Sales`.

### Scenario 8: Performing Routine Management Tasks

There may be situations in which you want to change the state or properties of the databases in a broker configuration to perform routine maintenance on one or more databases.

You might also need to temporarily disable broker management of databases in a configuration.

#### Changing Properties and States

As you monitor the configuration, you might need to dynamically modify the states of the databases or their properties.

The following topics show how to change the state or properties of the databases in the configuration.

##### Alter a Database Property

You can modify the values of database properties at any time—whether the database is enabled or disabled.

The following example shows how to use the `EDIT DATABASE` command to change the `LogXptMode` database property to the value ASYNC for the `North_Sales` database.

```
DGMGRL> EDIT DATABASE 'North_Sales' SET PROPERTY 'LogXptMode'=ASYNC;
```

DGMGRL returns the following message to indicate that the `LogXptMode` property was updated successfully in the Data Guard configuration file:

```
Property "LogXptMode" updated
```

If the configuration is currently disabled, the database does not use the new property value until you enable the broker configuration with the `ENABLE CONFIGURATION` command.

##### Reset a Property to Its Default Value

You can reset a configuration or configurable property to its default value at any time whether the database or configuration is enabled or disabled.

The following example shows how to use the `EDIT` `DATABASE` command to reset the `LogXptMode` database configurable property to its default value for the `North_Sales` database.

```
EDIT DATABASE 'North_Sales' RESET PROPERTY LogXptMode;
```

The following example shows how to use the `EDIT` `CONFIGURATION` command to reset the `TraceLevel` configuration property to its default value.

```
EDIT CONFIGURATION RESET PROPERTY TraceLevel;
```

##### Alter the State of a Standby Database

You can temporarily stop Redo Apply on a physical standby.

To change the state of the standby database to `APPLY-OFF`, enter the `EDIT DATABASE` command as shown in the following example.

```
DGMGRL> EDIT DATABASE 'South_Sales' SET STATE='APPLY-OFF';
Succeeded.
```

Redo data is still being received when you put the physical standby database in the `APPLY-OFF` state.

##### Alter the State of a Primary Database

You can stop the transmittal of redo data to the standby database.

To change the state of the primary database to accommodate this, use the following command:

```
DGMGRL> EDIT DATABASE North_Sales SET STATE=TRANSPORT-OFF;
 
Succeeded.
```

To change the state of the primary database back to `TRANSPORT-ON`, do the following:

```
DGMGRL> EDIT DATABASE North_Sales SET STATE=TRANSPORT-ON;
 
Succeeded.
```

#### Disabling the Configuration and Databases

When you disable the broker configuration or any of its databases, you are disabling the broker's management of them and are effectively removing your ability to use DGMGRL to manage and monitor them.

However, disabling the broker's management of a broker configuration does not affect the actual operation of the underlying Oracle Data Guard configuration or the databases. For example, the redo transport services and log apply services in the Oracle Data Guard configuration continue to function unchanged, but you can no longer manage them.

##### Disable a Configuration

You must use the `DISABLE CONFIGURATION` command to disable management of the entire broker configuration including the primary database.

For example:

```
DGMGRL> DISABLE CONFIGURATION;
```

The only way to disable broker management of the primary database is to use the `DISABLE CONFIGURATION` command; the `DISABLE DATABASE` command only disables management of a standby database. Likewise, the `DISABLE` `FAR_SYNC` command only disables management of a far sync instance.

Note:

If you disable management of a configuration while connected to the standby database or far sync instance, you must connect to the primary database (that is, a database whose control file role is primary) to reenable the configuration.

Disabling the broker's management of a configuration member does not remove the member from the broker configuration file. You can reenable your ability to use DGMGRL (or Cloud Control) to manage the member by entering the appropriate `ENABLE` `CONFIGURATION` or `ENABLE DATABASE ` command.

##### Disable a Standby Database

You use the `DISABLE DATABASE` command when you temporarily do not want the broker to manage and monitor a standby database.

You can explicitly disable broker management of a standby database to prevent it from being enabled when the rest of the configuration is enabled. The following example shows how to disable the `South_Sales` standby database.

```
DGMGRL> DISABLE DATABASE 'South_Sales';
Disabled.
```

Note:

You cannot disable a standby database from the configuration if fast-start failover is enabled and the database to be disabled is the target standby database.

Note:

If you disable management of a standby database while connected to that standby database, you must connect to the primary database or another enabled standby database to reenable broker-management of the standby database.

WARNING:

If you disable broker management of a standby database in the broker configuration, that standby database cannot be used by the broker as a failover target in the event of loss of the primary database.

When operating under either maximum protection mode or maximum availability mode, the broker prevents you from disabling the last standby database that supports the protection mode.

##### Disabling a Far Sync Instance

Use the `DISABLE` `FAR_SYNC` command when you temporarily do not want the broker to manage and monitor a far sync instance.

You can explicitly disable broker management of a far sync instance to prevent it from being enabled when the rest of the configuration is enabled. The following example shows how to disable the far sync instance.

```
DGMGRL> DISABLE FAR_SYNC 'FS';
Disabled.
```

Note:

The following restrictions apply when disabling a far sync instance:

- You cannot disable a far sync instance if it is specified in the `RedoRoutes` property of any other configuration member.
- If you disable management of a far sync instance while connected to that far sync instance, you must connect to the primary database or another enabled standby database to reenable broker management of the far sync instance.

Caution:

If you disable broker management of a far sync instance in the broker configuration, that far sync instance cannot be specified in a `RedoRoutes` property for any other configuration member.

#### Removing the Configuration, a Standby Database, or a Far Sync Instance

When you use the `REMOVE` `CONFIGURATION`, `REMOVE` `DATABASE`, or `REMOVE` `FAR_SYNC` command, you effectively delete the configuration, standby database, or far sync instance from the broker configuration file, removing the ability of Oracle Data Guard broker to manage them.

A remove operation with the `PRESERVE DESTINATIONS` clause does not remove or delete the actual Oracle Data Guard configuration underneath, nor does it affect the operation of the actual Oracle Data Guard configuration and its databases.

Note:

After you use the `REMOVE` `CONFIGURATION`, `REMOVE` `DATABASE`, or `REMOVE` `FAR_SYNC` command, you must reissue the command(s) that you originally issued if you decide to re-create the deleted object. You must go through the steps in Scenario 1: Creating a Configuration as necessary, to create a broker configuration that can be managed with DGMGRL (or Cloud Control).

Note:

The following restrictions apply:

- You cannot remove a standby database from the configuration if fast-start failover is enabled and the database to be removed is the target standby database.
- You cannot remove a standby database or a far sync instance if it is specified in the `RedoRoutes` property for any other member in the configuration.

##### Removing a Standby Database from the Configuration

When you use the `REMOVE` `DATABASE` command, broker management and monitoring of the database ceases and the database is deleted from the broker configuration file.

Show the configuration before deletion of the `South_Sales` standby database:

```
DGMGRL> SHOW CONFIGURATION;
 
Configuration - DRSolution
 
  Protection Mode: MaxPerformance
  Members:
    North_Sales  - Primary database
      FS - Far Sync
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
  Members:
    North_Sales  - Primary database
      FS - Far Sync
 
Fast-Start Failover: DISABLED
 
Configuration Status:
SUCCESS
```

When operating under either maximum protection mode or maximum availability mode, the broker prevents you from deleting the last standby database that supports the protection mode.

##### Removing a Far Sync Instance from the Configuration

Use the `REMOVE FAR_SYNC` command to remove far sync instance information from the Oracle Data Guard configuration file.

For example, use the following command to remove the `FS` far sync instance information:

```
DGMGRL> REMOVE FAR_SYNC 'FS';
Removed far sync instance "FS" from the configuration
```

Show the configuration after deletion of the `FS` far sync instance:

```
DGMGRL> SHOW CONFIGURATION;
 
Configuration - DRSolution
 
Protection Mode: MaxPerformance
Members:
North_Sales - Primary database
 
Fast-Start Failover: DISABLED
 
Configuration Status:
SUCCESS
```

##### Removing a Broker Configuration

Use the DGMGRL `REMOVE CONFIGURATION` command to remove the entire configuration from management and monitoring by the broker.

For example:

```
DGMGRL> REMOVE CONFIGURATION;
Removed configuration
```

Note:

You cannot remove the configuration if fast-start failover is enabled.

DGMGRL returns the following message to indicate the command successfully removed all of the configuration information from the Data Guard configuration file:

```
DGMGRL> SHOW CONFIGURATION;
Error: ORA-16532: Data Guard broker configuration does not exist
 
Configuration details cannot be determined by DGMGRL
```

### Scenario 9: Performing a Switchover Operation

You can switch the role of the primary database and a standby database using the `SWITCHOVER` command.

Before you issue the `SWITCHOVER` command, you must ensure:

- The state of the primary and standby databases are `TRANSPORT-ON` and `APPLY-ON`, respectively.
- All participating databases are in good health, without any errors or warnings present.
- The standby database properties were set on the primary database, so that the primary database can function correctly when transitioning to a standby database (shown in the following examples in boldface type).
- Standby redo log files are configured on the primary database.
- If the configuration is in maximum availability mode, then the current primary is configured to receive redo via `SYNC` or `FASTSYNC` or `ASYNC` mode if it will receive redo directly from the new primary. If it will receive redo via a far sync instance, then the far sync instance is configured to receive redo via `SYNC` or `FASTSYNC` mode and the current primary is configured to receive redo via `ASYNC` mode. If the configuration is in maximum protection mode, then the current primary is configured to receive redo via `SYNC` mode.
- If fast-start failover is enabled, you can perform a switchover only to the standby database that was specified as the target standby database.

The following are the tasks necessary to perform a switchover using the `SWITCHOVER` command:

- Using the SWITCHOVER Command Task 1: Check the Primary Database
- Using the SWITCHOVER Command Task 2: Check the Standby Database That is the Target of the Switchover
- Using the SWITCHOVER Command Task 3: Confirm That the Database Is Ready for a Role Change
- Using the SWITCHOVER Command Task 4: Issue the Switchover Command
- Using the SWITCHOVER Command Task 5: Show the Configuration

#### Using the SWITCHOVER Command Task 1: Check the Primary Database

Use the `SHOW DATABASE VERBOSE` command to check the state, health, and properties of the primary database.

For example:

```
SHOW DATABASE VERBOSE 'North_Sales';

Database - North_Sales

  Role:               PRIMARY
  Intended State:     TRANSPORT-ON
  Instance(s):
    north_sales1

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
    ReopenSecs                      = '300'
    NetTimeout                      = '30'
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
    Alert log               : /dev/oracle/log/diag/rdbms/North_Sales/north_sales1/trace/alert_north_sales1.log
    Data Guard Broker log   : /dev/oracle/log/diag/rdbms/North_Sales/north_sales1/trace/drcnorth_sales1.log

Database Status:
SUCCESS
```

In particular, you should examine the boldface properties and the current status of the primary database.

#### Using the SWITCHOVER Command Task 2: Check the Standby Database That is the Target of the Switchover

Use the `SHOW DATABASE ` command to check the status of the standby database that is the target of the switchover.

For example:

```
DGMGRL> SHOW DATABASE 'South_Sales';
 
Database - South_Sales
 
  Role: PHYSICAL STANDBY
  Intended State: APPLY-ON
  Transport Lag: 0 seconds (computed 0 seconds ago)
  Apply Lag: 0 seconds (computed 0 seconds ago)
  Apply Rate: 1.44 MByte/s
  Real Time Query: OFF
  Instance(s):
    south_sales1
 
Database Status:
SUCCESS
```

#### Using the SWITCHOVER Command Task 3: Confirm That the Database Is Ready for a Role Change

Prior to performing a role change, you can use the `VALIDATE       DATABASE` command to perform an exhaustive set of checks on the database to confirm that it is ready for a role change.

The examples shown in this step use the `VALIDATE DATABASE` command for all three databases in the `DRSolution` configuration: a primary, logical standby, and physical standby database. The configuration looks as follows:

```
DGMGRL> SHOW CONFIGURATION;
 
Configuration - DRSolution
 
  Protection Mode: MaxAvailability
  Members:
  North_Sales - Primary database
    West_Sales - Logical standby database
    South_Sales - Physical standby database
 
Fast-Start Failover: DISABLED
 
Configuration Status:
SUCCESS
```

Example: Validate the Primary Database

```
DGMGRL> VALIDATE DATABASE North_Sales;

  Database Role:    Primary database

  Ready for Switchover:  Yes

  Managed by Clusterware:
    North_Sales:  YES
```

Example: Validate the Logical Standby Database

Validate the logical standby database, as follows:

```
DGMGRL> VALIDATE DATABASE West_Sales;

  Database Role:     Logical standby database
  Primary Database:  North_Sales

  Ready for Switchover:  Yes
  Ready for Failover:    Yes (Primary Running)
    Warning: Physical and Snapshot standby databases will be
    be disabled if a role change is performed to this database

  Managed by Clusterware:
    North_Sales :  NO             
    West_Sales  :  NO             
    The static connect identifier allows for a connection to database "North_Sales".

  Parameter Settings:
    Parameter                       North_Sales Value        South_Sales Value
    DB_BLOCK_CHECKING               true                     true
    DB_BLOCK_CHECKSUM               true                     true
    DB_LOST_WRITE_PROTECT           NONE                     NONE
```

Example: Validate the Physical Standby Database

Validate the physical standby database, as follows:

```
DGMGRL> VALIDATE DATABASE South_Sales;

  Database Role:     Physical standby database
  Primary Database:  North_Sales

  Ready for Switchover:  Yes
  Ready for Failover:    Yes (Primary Running)

  Managed by Clusterware:
    North_Sales :  NO             
    South_Sales :  NO             
    The static connect identifier allows for a connection to database "North_Sales".

  Parameter Settings:
    Parameter                       North_Sales Value        South_Sales Value
    DB_BLOCK_CHECKING               true                     true
    DB_BLOCK_CHECKSUM               true                     true
    DB_LOST_WRITE_PROTECT           NONE                     NONE
```

Because the configuration protection is set to maximum availability mode and database `South_Sales` is the only one that has its `LogXptMode` property set to `SYNC`, an error is displayed to indicate that a switchover is not possible. Note that when a database receives redo from a database or a far sync instance that has the `RedoRoutes` property configured with a transport mode, that mode overrides the transport mode specified by `LogXptMode`.

#### Using the SWITCHOVER Command Task 4: Issue the Switchover Command

Issue the `SWITCHOVER` command to swap the roles of the primary and standby databases.

The following example shows how the broker automatically shuts down and restarts the old primary database as a part of the switchover. (See the usage notes in [DGMGRL Command Usage Notes](oracle-data-guard-broker-commands.md) for information about how to set up the broker environment so that DGMGRL can automatically restart the primary and standby databases for you.)

```
DGMGRL> SWITCHOVER TO 'South_Sales';
Performing switchover NOW, please wait...
Operation requires a connection to instance "south_sales1" on database "South_Sales"
Connecting to instance "south_sales1"...
Connected as SYSDBA.
New primary database "South_Sales" is opening...
Operation requires startup of instance "north_sales1" on database "North_Sales"
Starting instance "north_sales1"...
ORACLE instance started.
Database mounted.
Switchover succeeded, new primary is "South_Sales"
```

After the switchover completes, use the `SHOW CONFIGURATION` and `SHOW DATABASE` commands to verify that the switchover operation was successful.

#### Using the SWITCHOVER Command Task 5: Show the Configuration

Use the `SHOW CONFIGURATION` command to verify that the switchover was successful.

```
DGMGRL> SHOW CONFIGURATION;
 
Configuration - DRSolution
 
  Protection Mode: MaxAvailability
  Members:
    South_Sales  - Primary database
      West_Sales  - Logical standby database
      North_Sales - Physical standby database
 
Fast-Start Failover: DISABLED
 
Configuration Status:
SUCCESS
```

### Scenario 10: Performing a Manual Failover Operation

You invoke a failover operation in response to an emergency situation, usually when the primary database cannot be accessed or is unavailable.

See [Choosing a Target Standby Database](using-data-guard-broker-to-manage-switchovers-failovers.md) before you fail over to decide which standby database should be the target of the failover. The following scenario describes a failover to the remote database called `South_Sales`.

Note:

If multiple fast-start failover targets are configured, then a manual failover is only possible to the current fast-start failover target.

If you want to perform a manual failover to a standby database that is not the fast-start failover target standby database, you must first disable fast-start failover using the `FORCE` option on the standby database you want to fail over. See [Disabling Fast-Start Failover](using-data-guard-broker-to-manage-switchovers-failovers.md) for more information about the `FORCE` option.

1. (Optional) Check the readiness of the target standby.
	To validate the target standby database to ensure that it's ready to become the new primary database, use the `VALIDATE DATABASE` command, as shown in the following example:
	```
	DGMGRL> VALIDATE DATABASE 'South_Sales';
	 
	Database Role: Physical standby database
	Primary Database: South_Sales
	 
	Ready for Switchover: Yes
	Ready for Failover: Yes
	  Managed by Clusterware:
	    North_Sales :  NO             
	    South_Sales:  NO             
	    The static connect identifier allows for a connection to database "North_Sales".
	  Parameter Settings:
	    Parameter                       North_Sales Value        South_Sales Value
	    DB_BLOCK_CHECKING               true                     true
	    DB_BLOCK_CHECKSUM               true                     true
	    DB_LOST_WRITE_PROTECT           NONE                     NONE
	```
2. To perform the failover operation, you must connect to the standby database to which you want to fail over as a user that has the `SYSDG` or `SYSDBA` privilege. For example:
	```
	DGMGRL> CONNECT sysdg@South_Sales.example.com;
	Password: password
	Connected to "South_Sales"
	Connected as SYSDG.
	```
3. Now you can issue the failover command to make the target standby database the new primary database for the configuration.
	```
	DGMGRL> FAILOVER TO 'South_Sales';
	Performing failover NOW, please wait...
	Failover succeeded, new primary is "South_Sales"
	```
	Note that after the failover completes, the original primary database cannot be used as a standby database of the new primary database unless it is reinstated or re-created (as described in [Reenabling Disabled Databases After a Role Change](using-data-guard-broker-to-manage-switchovers-failovers.md)).
4. Issue the SHOW CONFIGURATION command to verify the failover.
	```
	DGMGRL> SHOW CONFIGURATION;
	 
	Configuration - DRSolution
	 
	  Protection Mode: MaxAvailability
	  Members:
	    South_Sales  - Primary database
	      Warning: ORA-16629: database reports a different protection level from the protection mode
	 
	      North_Sales - Physical standby database (disabled)
	        ORA-16661: the standby database needs to be reinstated
	 
	Fast-Start Failover: DISABLED
	 
	Configuration Status:
	WARNING
	```
	Note that in this example, the configuration was operating in maximum availability mode. The protection mode was preserved after the failover. The configuration also has a warning status. The `SHOW DATABASE` command for the new primary shows that the warning is the result of not having an enabled physical standby database. As a result, the warning status indicates that the protection level of the configuration is not the same as the configured mode.
5. ```
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
6. Issue the `SHOW DATABASE` command to see that the former (failed) primary database was disabled by the broker as a consequence of the failover. It must be reinstated (as described in [Reenabling Disabled Databases After a Role Change](using-data-guard-broker-to-manage-switchovers-failovers.md)).
	```
	DGMGRL> SHOW DATABASE 'North_Sales';
	Database - North_Sales
	 
	  Role: PHYSICAL STANDBY
	  Intended State: APPLY-ON
	  Transport Lag: (unknown)
	  Apply Lag: (unknown)
	  Apply Rate: (unknown)
	  Real Time Query: OFF
	  Instance(s):
	    north_sales1
	 
	Database Status:
	ORA-16661: the standby database needs to be reinstated
	```

### Scenario 11: Reinstating a Failed Primary Database

If your former primary database was configured with Flashback Database, you can easily reinstate the failed primary database as a standby database of the new primary database.

The failed primary database will be reinstated as a standby type that matches the old standby database. For example, if you failed over to a physical standby database, the old primary will be reinstated as a physical standby database.

To reinstate the failed primary database, start it to the mounted state. Then run DGMGRL, connect to the new primary database and reinstate the old primary database.

1. ```
	% dgmgrl connect sysdg
	Password: password
	Connected to "North_Sales"
	Connected as SYSDG.
	DGMGRL> startup mount;
	ORACLE instance started.
	Database mounted.
	```
2. ```
	% dgmgrl connect sysdg
	Password: password
	Connected to "North_Sales"
	Connected as SYSDG.
	DGMGRL> REINSTATE DATABASE 'North_Sales';
	Reinstating database "North_Sales", please wait...
	Reinstatement of database "North_Sales" succeeded
	 
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
3. Show the configuration and its members:
	```
	DGMGRL> SHOW CONFIGURATION
	 
	Configuration - DRSolution
	 
	  Protection Mode: MaxAvailability
	  Members:
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
	 
	Database - 'North_Sales'
	 
	  Role: PHYSICAL STANDBY
	  Intended State: APPLY-ON
	  Transport Lag: 0 seconds (computed 1 second ago)
	  Apply Lag: 0 seconds (computed 1 second ago)
	  Apply Rate: 0 Byte/s
	  Real Time Query: OFF
	  Instance(s):
	    north_sales1
	 
	Database Status:
	SUCCESS
	```

### Scenario 12: Converting a Physical Standby to a Snapshot Standby

If you have a physical standby database that you would like to convert to a snapshot standby database, use the DGMGRL `CONVERT DATABASE` command.

Redo data will continue to be received by the database while it is operating as a snapshot standby database, but it will not be applied until the snapshot standby is converted back into a physical standby database.

A physical standby database must be configured with a fast recovery area to convert it to a snapshot standby database. This is because a guaranteed restore point is created during the conversion process, and guaranteed restore points require a fast recovery area.

```
DGMGRL> convert database 'South_Sales' to snapshot standby;
Converting database "South_Sales" to a Snapshot Standby database, please wait...
Database "South_Sales" converted successfully

DGMGRL> SHOW CONFIGURATION;
 
Configuration - DRSolution
 
  Protection Mode: MaxPerformance
  Members:
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
Database "South_Sales" converted successfully
```

### Scenario 13: Monitoring a Data Guard Configuration

These steps demonstrate the tasks necessary to use the `SHOW` command and monitorable properties to identify and resolve a failure situation.

- Monitoring a Configuration Task 1: Check the Configuration Status
- Monitoring a Configuration Task 2: Check the Database Status
- Monitoring a Configuration Task 3: Check the LogXptStatus Monitorable Property
- Monitoring a Configuration Task 4: Check the InconsistentLogXptProps Monitorable Property

#### Monitoring a Configuration Task 1: Check the Configuration Status

The status of the broker configuration is an aggregated status of all databases and instances in the broker configuration.

You can check the configuration status first to determine whether or not any further action needs to be taken. If the configuration status is SUCCESS, everything in the broker configuration is working properly. However, if you see a status of WARNING or ERROR, then something is wrong in the configuration.

For example, in the following display, you can see that the primary database has multiple warnings:

```
DGMGRL> SHOW CONFIGURATION;
Configuration - DRSolution
 
  Protection Mode: MaxPerformance
  Members:
    North_Sales  - Primary database
      Warning: ORA-16809: multiple warnings detected for the database
 
      South_Sales  - Physical standby database
 
Fast-Start Failover: DISABLED
 
Configuration Status:
WARNING
```

#### Monitoring a Configuration Task 2: Check the Database Status

To identify the warnings on the primary database, show its status using the `SHOW DATABASE` command.

For example:

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

#### Monitoring a Configuration Task 3: Check the LogXptStatus Monitorable Property

The `SHOW DATABASE` output in step 2 shows a Warning for error ORA-16737.

To identify the exact transport error, use the `LogXptStatus` monitorable property:

```
DGMGRL> SHOW DATABASE 'North_Sales' 'LogXptStatus';
LOG TRANSPORT STATUS
PRIMARY_INSTANCE_NAME  STANDBY_DATABASE_NAME  STATUS 
         north_sales1            South_Sales  ORA-12541: TNS:no listener
```

The output shows that the listener for the physical standby database is not running. To fix this error, start the listener for the physical standby database `South_Sales`.

#### Monitoring a Configuration Task 4: Check the InconsistentLogXptProps Monitorable Property

To identify the inconsistent values for the redo transport database property, `ReopenSecs`, you can use the `InconsistentLogXptProps` monitorable property.

This is useful, for example, for the warning shown in the `SHOW DATABASE` display in Step 2 is ORA-16715.

```
DGMGRL> SHOW DATABASE 'North_Sales' 'InconsistentLogXptProps';
INCONSISTENT LOG TRANSPORT PROPERTIES
 INSTANCE_NAME  STANDBY_NAME  PROPERTY_NAME  MEMORY_VALUE  BROKER_VALUE 
   south_sales1   South_Sales     ReopenSecs           600           300
```

The current database memory value (600) is different from the Oracle Data Guard broker's property value (300). If you think the broker's property value is correct, you can fix the inconsistency by re-editing the property of the standby database with the same value, as shown in the following example:

```
DGMGRL> EDIT DATABASE 'South_Sales' SET PROPERTY 'ReopenSecs'=300;
Property "ReopenSecs" updated
```

You can also reenable the standby database or reset the state of the primary database to `TRANSPORT-ON` to fix this inconsistency.

### Scenario 14: Adding a Recovery Appliance to a Broker Configuration

These steps show how to add a Zero Data Loss Recovery Appliance (Recovery Appliance) to a broker configuration.

See Also:

[Example 4-9](managing-oracle-data-guard-broker-configuration-members.md) for an example of how to set up a Recovery Appliance as the redo destination of a physical standby

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

### Scenario 15: Exporting and Importing a Broker Configuration File

You can export the broker configuration metadata into a text file. When you need to recreate the broker configuration, you can import the exported metadata into the current broker configuration.

In this example, you save the broker configuration by exporting the configuration metadata into a text file. The configuration is then restored by importing the text file that you had previously exported.

1. Exporting a Broker Configuration
2. Importing a Broker Configuration

#### Exporting a Broker Configuration

Use the `EXPORT CONFIGURATION` command to export the metadata contained in the broker configuration file to a text file.

The directory in which the broker configuration file is stored must be accessible to the Oracle server process.

1. ```
	DGMGRL> CONNECT sysdg@North_Sales.example.com;
	Password: password
	Connected to "North_Sales"
	Connected as SYSDG.
	```
2. The following command exports the broker configuration and stores it in a file named `myconfig.txt` in the trace directory.
	```
	DGMGRL> EXPORT CONFIGURATION TO 'myconfig.txt';
	Succeeded.
	```

#### Importing a Broker Configuration

Use the `IMPORT CONFIGURATION` command to import the broker configuration metadata that is stored in a text file into your current broker configuration.

1. ```
	DGMGRL> CONNECT sysdg@North_Sales.example.com;
	Password: password
	Connected to "North_Sales"
	Connected as SYSDG.
	```
2. Import the broker configuration metadata that is stored in the file named `myconfig.txt` in the `trace` directory into your current broker configuration.
	```
	DGMGRL> IMPORT CONFIGURATION 'myconfig.txt';
	Succeeded.
	```

### Scenario 16: Using the Observe-only Mode for Fast-Start Failover

The observe-only mode enables you to test the impact of using fast-start failover in your configuration, without making any actual changes to the configuration. You can use the DGMGRL commands or data dictionary views to verify the observe-only mode setting.

Topics:

- Configuring Observe-only Mode for Fast-Start Failover
- Sample Content of the Log Files in Observe-only Mode
- Disabling Observe-only Mode for Fast-start Failover

#### Configuring Observe-only Mode for Fast-Start Failover

Use the `ENABLE FAST_START FAILOVER` command to configure observe-only mode for fast-start failover.

1. Use the following command to configure the observe-only mode for fast-start failover.
	```
	DGMGRL> ENABLE FAST_START FAILOVER OBSERVE ONLY;
	```
	All existing observers and ones that will be started in the future will run in observe-only mode.
2. Verify that the observe-only mode has be set by using one of the following methods:
	1. Display the current fast-start failover configuration using the following command:
		```
		DGMGRL> SHOW FAST_START FAILOVER;
		Fast-Start Failover: Enabled in Observe-Only Mode
		  Protection Mode: MaxAvailability
		  Lag Limit: 30 seconds
		  Threshold: 30 seconds
		  Ping Interval: 3000 milliseconds
		  Ping Retry: 0
		  Active Target: South_Sales
		  Potential Targets: "South_Sales"
		    South_Sales valid
		  Observer: observer.example.com
		  Shutdown Primary: TRUE
		  Auto-reinstate: TRUE
		  Observer Reconnect: (none)
		  Observer Override: FALSE
		```
	2. Display the current fast-start failover mode using the following command:
		```
		SQL> SELECT fs_failover_mode from V$DATABASE;
		FS_FAILOVER_MODE
		-------------------
		OBSERVE-ONLY
		```

#### Sample Content of the Log Files in Observe-only Mode

This section shows the entries made to the log files when you configure fast-start failover in observe-only mode.

Example 1: When Fast-start Failover Should be Initiated

Observer Log

```
A fast-start failover would have been initiated...
Unable to failover since this observer is in observe-only mode
```

Broker Log

```
Fast-Start Failover cannot proceed because: "observe-only mode"
```

Example 2: Primary Database Opens During Startup Without an Acknowledgement from Observer or Target Standby

The broker log file (drc\*.log) and alert log contain the following:

```
This database is allowed to open in observe-only mode. An acknowledgement from observer or target standby would have been required in normal FSFO mode.
```

Example 3: Switchover or Manual Failover to a Bystander Database

The broker log file (drc\*.log) and alert logs contain the following information:

```
FAILOVER to database 'database name' is allowed even though observe-only mode is enabled. It would have been rejected since database 'database name' is a bystander database.
```

#### Disabling Observe-only Mode for Fast-start Failover

Use the `DISABLE FAST_START FAILOVER` command to exit the observe-only mode of fast-start failover. You must first disable fast-start failover and then enable fast-start failover without the `OBSERVE ONLY` clause.

Use the following commands to disable observe-only mode for fast-start failover:

```
DGMGRL> DISABLE FAST_START FAILOVER;
DGMGRL> ENABLE FAST_START FAILOVER;
```

Fast-start failover is now enabled, without observe-only mode.