---
title: Broker
book: Data Guard Broker
doc_id: E85768-01
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/dgbkr/oracle-data-guard-broker-commands.html
tags:
  - oracle
  - 12c
  - data-guard-broker
---

Use the command reference to understand how you can use the Data Guard broker command-line interface (DGMGRL) to manage your broker configuration.

DGMGRL enables you to manage a Data Guard broker configuration and its various members directly from the command line, or from batch programs or scripts. You can use the Data Guard broker command-line interface as an alternative to Oracle Enterprise Manager Cloud Control (Cloud Control) for managing a Data Guard configuration.

- Starting the Data Guard Command-Line Interface
- Exiting the Data Guard Command-Line Interface

### 7.1 Starting the Data Guard Command-Line Interface

To start the Data Guard command-line interface (DGMGRL), enter `dgmgrl` at the command-line prompt on a system where Oracle is installed.

```
% dgmgrl
```

The DGMGRL command prompt is displayed:

```
DGMGRL>
```

To run DGMGRL, you must have `SYSDG` or `SYSDBA` administrative privilege.

#### 7.1.1 DGMGRL Optional Parameters

You can supply optional parameters on the command line to indicate how you want the Data Guard command-line interface to display output.

Output includes items such as command prompts, banners, and messages.

Additionally, a single command mode is available. In this mode, DGMGRL executes one command and exits upon the completion of the command. The exit code is the result of the command. If the exit code is 0, the command completed successfully. Otherwise, there was an error.

The command line of DGMGRL appears as follows:

`% dgmgrl [<options>] [<logon> [<command>] ]`

Specify any of the following keywords when you invoke the DGMGRL command-line interface:

- `<options>` can be one of the following choices:
	- `-echo`
		Displays command input and output to the default display device. If you do not use this parameter, only the output from the command is displayed.
		- `-logfile` \<file-spec> "\<dgmgrl-command>"
		Specifies a file into which you can capture the actions of the DGMGRL command-line interface. This is particularly useful when DGMGRL is being invoked to serve as the fast-start failover observer. See the " START OBSERVER " command for more information.
		Note:
		The DGMGRL `-logfile` option is deprecated as of Oracle Database 12c Release 2 (12.2.0.1). It is supported for backward compatibility only. Instead, the log file should now be specified using the `LOGFILE IS` clause on the `START OBSERVER` command.
	See Also:
	- The " START OBSERVER " command
	- [Capturing Observer Actions in the Observer Log File](troubleshooting-oracle-data-guard-broker.md)
- - `-silent`
		Suppresses the display of the DGMGRL (`DGMGRL>`) command prompt on your default display device. This option is useful if you are directing the command output to a file or to another display tool.
- `<logon>` is:
	- `username [@connect-identifier]`
		To connect to the database, enter a `username` and optionally, a `connect-identifier`. You will then be prompted for a password. The `connect-identifier` is a fully specified connect descriptor or a name to be resolved by an Oracle naming method (for example, TNS).
		If a fully specified connect descriptor is used, it needs to include quotation marks; otherwise the connections will fail with an `invalid option` error. The following is an example of connecting using quotation marks:
		```
		dgmgrl sys@'(DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=sales-server)(PORT=1521)))
		(CONNECT_DATA=(SERVICE_NAME=sales.us.example.com)))'
		```
		```
		Enter password: password
		```
		Whether the connect identifier is specified using a fully specified connect descriptor or using the Easy Connect naming method, any of the following syntax is valid (you will be prompted for a password):
		- `dgmgrl username@'connect_identifier'`
				- `dgmgrl username@"connect_identifier"`
				- `dgmgrl username@"'connect_identifier'"`
		WARNING:
		Including a password on the command line when invoking DGMGRL is a security risk. This risk can be avoided either by omitting the password when invoking DGMGRL and entering it when prompted, or by using an external authentication method.
		- You can connect as '/' when using operating-system authentication (remote database restarts will not work), Secure Sockets Layer (SSL) protocol, or database credentials stored in a wallet.
- `<command>` is a single command.
	For example:
	`dgmgrl sys "show database 'North_Sales'"`
	`Password`: password

The following subsections specify the command format that you enter at the `DGMGRL>` command prompt.

#### 7.1.2 DGMGRL Command Format and Parameters

The DGMGRL commands allow you to create and maintain one broker configuration at a time.

Table 7-1 Summary of DGMGRL Commands

| Command | Effect |
| --- | --- |
| @ (at sign) Command | Executes a DGMGRL script. |
| / (slash) Command | Repeats the last command entered at the DGMGRL command prompt. |
| ADD DATABASE | Adds a new standby database to the existing broker configuration. |
| ADD FAR\_SYNC | Adds an existing far sync instance to an Oracle Data Guard broker configuration. |
| ADD RECOVERY\_APPLIANCE | Adds a Zero Data Loss Recovery Appliance (Recovery Appliance) to an existing broker configuration. |
| CONNECT | Connects to the specified database using the specified username. |
| CONVERT DATABASE | Converts the specified database to either a snapshot standby database or a physical standby database. |
| CREATE CONFIGURATION | Creates a broker configuration and adds a primary database to that configuration. |
| DISABLE CONFIGURATION | Disables broker management of a configuration so that the configuration and all of its databases are no longer managed by the broker. |
| DISABLE DATABASE | Disables broker management of the named standby database. |
| DISABLE FAR\_SYNC | Disables broker management of a far sync instance. |
| DISABLE FAST\_START FAILOVER | Disables fast-start failover. |
| DISABLE FAST\_START FAILOVER CONDITION | Allows a user to remove conditions for which a fast-start failover should be performed. |
| DISABLE RECOVERY\_APPLIANCE | Disables broker management of the named Zero Data Loss Recovery Appliance (Recovery Appliance). |
| EDIT CONFIGURATION (Property) | Changes the value of a property for the broker configuration. |
| EDIT CONFIGURATION (Protection Mode) | Changes the current protection mode setting for the broker configuration. |
| EDIT CONFIGURATION (RENAME) | Changes the configuration name. |
| EDIT CONFIGURATION RESET (Property) | Resets the specified configuration property to its default value. |
| EDIT DATABASE (Property) | Changes the value of a property for the named database. |
| EDIT DATABASE (Rename) | Changes the name used by the broker to refer to the specified database. |
| EDIT DATABASE (State) | Changes the state of the specified database. |
| EDIT DATABASE RESET (Property) | Resets the specified property for the named database to its default value. |
| EDIT FAR\_SYNC | Changes the name, state, or properties of a far sync instance. |
| EDIT FAR\_SYNC RESET (Property) | Resets the specified property for the named far sync instance to its default value. |
| EDIT INSTANCE (AUTO PFILE) | Sets the name of the initialization parameter file for the specified instance. |
| EDIT INSTANCE (Property) | Changes the value of a property for the specified instance. |
| EDIT INSTANCE RESET (Property) | Resets an instance-specific property for the specified instance(s) to its default value. |
| EDIT RECOVERY\_APPLIANCE (Property) | Changes the value of the property for the named Zero Data Loss Recovery Appliance (Recovery Appliance). |
| EDIT RECOVERY\_APPLIANCE (Rename) | Changes the name used by the broker to refer to the specified Zero Data Loss Recovery Appliance (Recovery Appliance), as recorded in that Recovery Appliance's profile in the broker configuration. |
| EDIT RECOVERY\_APPLIANCE RESET (Property) | Resets the specified property for the named Zero Data Loss Recovery Appliance (Recovery Appliance) to its default value. |
| ENABLE CONFIGURATION | Enables broker management of the broker configuration and all of its databases. |
| ENABLE DATABASE | Enables broker management of the specified database. |
| ENABLE FAR\_SYNC | Enables broker management of the specified far sync instance. |
| ENABLE FAST\_START FAILOVER | Enables the broker to automatically failover from the primary database to a target standby database. |
| ENABLE FAST\_START FAILOVER CONDITION | Allows a user to add conditions for which a fast-start failover should be performed. |
| ENABLE RECOVERY\_APPLIANCE | Enables broker management of the specified Zero Data Loss Recovery Appliance (Recovery Appliance). |
| EXIT | Exits the Data Guard command-line interface. |
| FAILOVER | Performs a database failover operation in which the standby database, to which DGMGRL is currently connected, fails over to the role of primary database. |
| HELP | Displays online help for the Data Guard command-line interface. |
| HOST or! (exclamation point) | Executes operating system command(s) directly through the DGMGRL console without leaving DGMGRL. |
| MIGRATE PLUGGABLE DATABASE | Migrates a PDB from one CDB to another on the same host. |
| QUIT | Quits the Data Guard command-line interface. |
| REINSTATE DATABASE | Reinstates the database after a failover. |
| REMOVE CONFIGURATION | Removes the broker configuration and ends broker management of its members. |
| REMOVE DATABASE | Removes the specified standby database from the broker configuration. |
| REMOVE FAR\_SYNC | Removes a far sync instance from an Oracle Data Guard broker configuration. |
| REMOVE INSTANCE | Removes an instance from the broker configuration. |
| REMOVE RECOVERY\_APPLIANCE | Removes the specified Zero Data Loss Recovery Appliance (Recovery Appliance) from the broker configuration and terminates broker management of the Recovery Appliance. |
| SET MASTEROBSERVER TO | Lets you manually designate which observer is recognized as the master observer. |
| SET MASTEROBSERVERHOSTS | Sets the master observer of a broker configuration to the observer on the target host. |
| SET ObserverConfigFile | Sets the full path and file name of an observer configuration file. |
| SET TIME | Turns timestamp printing on and off. |
| SHOW CONFIGURATION | Displays information about the broker configuration. |
| SHOW CONFIGURATION WHEN PRIMARY IS | Shows the redo transport configuration that would be in effect if the specified database were the primary database. |
| SHOW DATABASE | Displays information about the specified database. |
| SHOW FAR\_SYNC | Shows information about a far sync instance. |
| SHOW FAST\_START FAILOVER | Displays all fast-start failover related information. |
| SHOW INSTANCE | Displays information about the specified instance. |
| SHOW OBSERVER | Shows information about all registered observers in a Data Guard broker configuration. |
| SHOW ObserverConfigFile | Shows the value of the `ObserverConfigFile` property. |
| SHOW OBSERVERS | Shows information about all observers for all broker configurations in a specific configuration group. |
| SHOW RECOVERY\_APPLIANCE | Displays information or property values of the specified Zero Data Loss Recovery Appliance (Recovery Appliance). |
| SHUTDOWN | Shuts down a currently running Oracle database. |
| SPOOL | Records the input and output of DGMGRL to a file. |
| SQL | Allows you to enter SQL statements from the Data Guard command-line interface (DGMGRL). |
| START OBSERVER | Starts the observer. |
| START OBSERVER IN BACKGROUND | Starts a fast-start failover observer as a background process on the host where the DGMGRL session is running. |
| START OBSERVING | Starts a new observer for each broker configuration in the specified group. |
| STARTUP | Starts an Oracle instance with the same options as SQL\*Plus, including mounting and opening a database. |
| STOP OBSERVER | Stops the observer. |
| STOP OBSERVING | Stops all local observers running on the host where this DGMGRL session is running, for all broker configurations in a specific group. |
| SWITCHOVER | Performs a switchover operation in which the current primary database becomes a standby database, and the specified standby database becomes the primary database. |
| VALIDATE DATABASE | Performs a comprehensive set of database checks prior to a role change. |
| VALIDATE DATABASE DATAFILE | Performs validation of data files across the primary database and standby databases. |
| VALIDATE FAR\_SYNC | Performs a comprehensive set of checks for a far sync instance. |

#### 7.1.3 DGMGRL Command Usage Notes

The items in this list describe usage notes specific to DGMGRL.

- The `DG_BROKER_START` dynamic initialization parameter is set to `TRUE`.
- To enable broker operations that require restarting instances without manual intervention, Oracle Net Services must be configured on each of the hosts that contain the primary and standby database instances. Specifically, the listener.ora file must contain static configuration information about the instance. The `GLOBAL_DBNAME` attribute must be set to `db_unique_name` `_DGMGRL.``db_domain`. See [Prerequisites](oracle-data-guard-broker-installation-requirements.md) for additional information.
- The connect identifier used while creating the configuration or adding a database, must be resolvable from any of the hosts in the configuration.
- You must have `SYSDG` or `SYSDBA` privileges to use the Oracle Data Guard command-line interface. Do not include `AS SYSDG` or `AS SYSDBA` on the `CONNECT` command. DGMGRL first attempts an `AS SYSDG` connection; if that fails, it then attempts an `AS SYSDBA` connection.
- If you specify more than one option on the command, you can specify the options in any order.
- A semicolon is required at the end of each DGMGRL command.
- Characters specified in a DGMGRL command string value are interpreted as lowercase characters, unless enclosed in double (") or single (') quotation marks. For example, database and DatAbaSe are equivalent, but "database" and "DatAbaSe" are not.
- You can use the backslash (\\) to escape a single quotation mark ('), a double quotation mark ("), and the backslash character (\\) itself if these characters appear in a character string.
- Some operations on a broker configuration may require that one or more databases be shut down and restarted. In most cases, DGMGRL will automatically shut down and restart a given database for you if the following are true:
	- The `instance-name` is the SID (this applies to Cloud Control as well as DGMGRL).
		- The broker must be able to connect to the database using the same credentials given in the last `CONNECT` command, even if the last `CONNECT` command was used to connect to another database.

Command Examples

Example 7-1 Connecting to DGMGRL on a Local System

This example demonstrates how to connect to the DGMGRL command-line interface on the local default system.

```
% dgmgrl
.
.
.
Welcome to DGMGRL, type "help" for information.

DGMGRL> CONNECT sysdg;
Password: password
Connected to "North_Sales"
Connected as SYSDG.
```

Example 7-2 Connecting to DGMGRL on a Remote System

This example demonstrates how to connect to the Oracle Data Guard (DGMGRL) command-line interface on a remote system.

```
DGMGRL> CONNECT sysdg@remote-stby;
Password: password
Connected to "remote-stdby"
Connected as SYSDG.
```

Example 7-3 Connecting Using the AS Option

This example demonstrates how to connect to the Oracle Data Guard (DGMGRL) command-line interface using the `CONNECT AS` option:

```
DGMGRL> CONNECT sys@remote-stby AS SYSDBA;
Password: password
Connected to "remote-stdby"
Connect as SYSDBA.
```

### 7.2 Exiting the Data Guard Command-Line Interface

When you are done working with the DGMGRL interface and want to return to the operating system, enter the `EXIT` or `QUIT` command.

For example:

```
DGMGRL> EXIT;
```

### 7.3 @ (at sign) Command

The @ command allows you to execute DGMGRL commands stored in script files.

You can put a sequence of commands into a script file and then use the @ command to execute the file. The commands contained in the script are executed sequentially.

Format

From within DGMGRL, the syntax is as follows:

DGMGRL> @ script\_file\_name

Command Parameters

| Flag | Description |
| --- | --- |
| \-echo | Prints all the commands in the script along with their execution results. |

Usage Notes

The script that you execute with this command must meet the following qualifications:

- DGMGRL must be able to access the script; otherwise the command fails because DGMGRL cannot open the file.
- Every DGMGRL command included in the script must end with a semi-colon.
- Recursive @ command execution is allowed, but the limit of recursive levels is 20. If the recursive level reaches 20, then the execution is aborted and none of the unexecuted commands is executed. Therefore, self-recursive execution of the @ command (for example, putting an @abc.script command in abc.script itself) should be used with caution.
- If there is a `START OBSERVER` command in the script, then any commands that come after it are ignored because the `START OBSERVER` command turns the DGMGRL session into an observer.
	The `START OBSERVER IN BACKGROUND` command is treated as a normal command; that is, any commands that come after it are executed.
- Comment lines are permitted in the script, but they must be terminated with a semi-colon. For example the following comments would be allowed in a script:
	```
	REM Hello World; 
	-- Hello Again!;
	```
	The double dash must be followed by a space character before the comment text.

### 7.4 / (slash) Command

Use the DGMGRL / (slash) command to repeat the last command entered at the command prompt.

Format

```
DGMGRL> /
```

Usage Notes

- The following commands are not repeatable using the / (slash) command:
	- Return
		- An unrecognized command
		- The `CONNECT` command (because it may contain credentials)
		- The / (slash) command itself

Command Example

In the following example, the / (slash) command is used to easily repeat the `SHOW CONFIGURATION` command.

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

DGMGRL> /

Configuration - Sales_Configuration
 
  Protection Mode: MaxAvailability
  Members:
  North_Sales  - Primary database
    Local_Sales  - Physical standby database
      Remote_Sales  - Physical standby database (receiving current redo)
 
Fast-Start Failover: DISABLED
 
Configuration Status:
SUCCESS

DGMGRL>
```

### 7.5 ADD DATABASE

The DGMGRL `ADD DATABASE` command adds a standby database to an existing broker configuration.

Format

ADD DATABASE database-name AS CONNECT IDENTIFIER IS connect-identifier;

Command Parameters

database-name

The name that will be used by the broker to refer to this standby database. It must match (case-insensitive) the value of the corresponding database `DB_UNIQUE_NAME` initialization parameter.

connect-identifier

A fully specified connect descriptor or a name to be resolved by an Oracle Net Services naming method (for example, TNS). The value you specify is also used as the initial value of the `DGConnectIdentifier` database property.

Usage Notes

- To issue this command, you must connect to the primary database or to an enabled standby database that is already in the configuration.
- The broker uses the specified `connect-identifier` to communicate with the specified database from other databases. Therefore, you must ensure that the `connect-identifier` can be used to address the specified database from all databases in your configuration. For example, if TNS is used as the naming method, you must ensure that the tnsnames.ora file on every database and instance that is part of the configuration contains an entry for the `connect-identifier`. The connect identifier must resolve to the same connect descriptor. If the database that is being added is an Oracle RAC database, the `connect-identifier` provided here must reach all instances of the Oracle RAC, preferably with `FAILOVER` attributes set.
	See Also:
	[Oracle Database Net Services Administrator's Guide](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/dgbkr&id=NETAG186)
- If the connection cannot be made, the broker does not add the new database to the configuration.
- You must clear any remote redo transport destinations on the standby database before it can be added to the configuration.

Command Example

The following example shows how to add a database named `South_Sales`.

```
DGMGRL> ADD DATABASE South_Sales AS CONNECT IDENTIFIER IS South_Sales.example.com;
Database "South_Sales" added
```

### 7.6 ADD FAR\_SYNC

The `ADD FAR_SYNC` command adds an existing far sync instance to an Oracle Data Guard broker configuration.

The far sync instance is disabled after creation. You must explicitly enable it before the broker can ship redo to and from it.

Format

ADD FAR SYNC far\_sync\_instance\_name AS CONNECT IDENTIFIER IS connect-identifier;

Command Parameters

far\_sync\_instance\_name

The name that will be used by the broker to refer to this far sync instance. It must match (case-insensitive) the value of the corresponding far sync instance `DB_UNIQUE_NAME` initialization parameter.

connect-identifier

A fully specified connect descriptor or a name to be resolved by an Oracle Net Services naming method (for example, TNS). The value you specify is also used as the initial value of the `DGConnectIdentifier` property.

Usage Notes

- The far sync instance must already exist before you can add it to a broker configuration.
- You must clear any remote redo transport destinations on the far sync instance before it can be added to the configuration.

Command Example

The following example adds a far sync instance named `chicago` to the configuration.

```
DGMGRL> ADD FAR_SYNC chicago AS CONNECT IDENTIFIER IS chicago.example.com;
```

### 7.7 ADD RECOVERY\_APPLIANCE

The `ADD RECOVERY_APPLIANCE` command adds a Zero Data Loss Recovery Appliance (Recovery Appliance) to an existing broker configuration.

The `AS CONNECT IDENTIFIER` clause is optional. If you do not specify this clause, then the broker searches the `LOG_ARCHIVE_DEST_n` initialization parameters on the primary database and all enabled standby databases for an entry that corresponds to the Recovery Appliance being added.

Format

ADD RECOVERY APPLIANCE object-name AS CONNECT IDENTIFIER IS connect-identifier;

Command Parameters

object name

The name that will be used by the broker to refer to this Recovery Appliance. It must match (case-insensitive) the value of the corresponding Recovery Appliance `DB_UNIQUE_NAME` initialization parameter.

connect-identifier

A fully specified connect descriptor or a name to be resolved by an Oracle Net Services naming method (for example, TNS). The value you specify is also used as the value of the `DGConnectIdentifier` database property.

Usage Notes

- To issue this command, you must connect to the primary database or to an enabled standby database that is already in the configuration.
- The broker uses the specified connect identifier to communicate with the specified Recovery Appliance from any database in the configuration. Therefore, you must ensure that the connect identifier can be used to address the specified Recovery Appliance from any database in the configuration. For example, if TNS is used as the naming method, you must ensure that the `tnsnames.ora` file on every database and instance that is part of the configuration contains an entry for the connect identifier. The connect identifier must resolve to the same connect descriptor.
- If the connection cannot be made, then the broker does not add the new Recovery Appliance to the configuration.
- It is possible to have more than one Recovery Appliance in the configuration.

Command Example

The following example shows how to add a Recovery Appliance named `EnterpriseRecoveryAppliance`.

```
DGMGRL> ADD RECOVERY_APPLIANCE EnterpriseRecoveryAppliance AS CONNECT IDENTIFIER IS 
EnterpriseRecoveryAppliance.example.com;Oracle Backup Appliance "EnterpriseRecoveryAppliance" added
```

### 7.8 CONNECT

The DGMGRL `CONNECT` command connects you to a database or far sync instance that is a member of a Data Guard broker configuration.

Format

CONNECT username @ connect-identifer \[AS {SYSDBA | SYSDG} \];

Command Parameters

username

Represents the username with which you want to connect to the configuration member. You will be prompted for a password after you enter a username and optionally, a connect-identifier.

connect-identifier

This parameter is optional. It is an Oracle Net Services connect identifier for the configuration member to which you want to connect. The exact syntax depends upon the Oracle Net Services communications protocol your Oracle installation uses.

Usage Notes

- The username and password must be valid for the configuration member to which you are trying to connect.
	The username you specify must have the `SYSDG` or `SYSDBA` privilege.
- The `AS` clause is optional. If it is specified, then DGMGRL attempts to connect as either SYSDG or SYSDBA, whichever one was specified. If the `AS` clause is not specified, then DGMGRL first attempts an `AS SYSDG` connection; if that fails, it then attempts an `AS SYSDBA` connection.
- If the `CONNECT` command returns an error, check to see that you specified a valid `connect-identifier`.
- When the `CONNECT` command is successful, the name of the configuration member to which the connection has been made is shown.

Command Examples

Example 1: Connecting to a Local Configuration Member

This example connects to the default database or far sync instance on the local system.

```
DGMGRL> CONNECT sysdg;
Password: password
Connected to "North_Sales"
Connected as SYSDG.
```

Example 2: Connecting to a Remote Configuration Member

This example connects to a database on the remote system (you could specify a far sync instead).

```
DGMGRL> CONNECT sysdg@South_Sales;
Password: password
Connected to "South_Sales"
Connected as SYSDG.
```

Example 3: Connecting Without Showing Connection Credentials

This example connects to a configuration member using `CONNECT '/'` so that connection credentials are not visible on the command line:

```
DGMGRL> CONNECT /@North_Sales.example.com;
Connected to "North_Sales"
```

You must set up Oracle Wallet or SSL to use `CONNECT '/'`. By setting up Oracle Wallet or SSL, you can write a script to securely start and run the observer as a background job without specifying database credentials in the script.

### 7.9 CONVERT DATABASE

The `CONVERT DATABASE` command converts a physical standby database to a snapshot standby database, or reverts the snapshot standby database back to a physical standby database.

A snapshot standby database is a fully updatable standby database. Like a physical or logical standby database, a snapshot standby database receives and archives redo data from a primary database. Unlike a physical or logical standby database, a snapshot standby database does not apply the redo data that it receives. The redo data received by a snapshot standby database is not applied until the snapshot standby is converted back into a physical standby database, after first discarding any local updates made to the snapshot standby database.

A snapshot standby database is best used in scenarios that require a temporary, updatable snapshot of a physical standby database. Note that because redo data received by a snapshot standby database is not applied until it is converted back into a physical standby, the time needed to perform a role transition is directly proportional to the amount of redo data that needs to be applied.

See [Oracle Data Guard Concepts and Administration](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/dgbkr&id=SBYDB4801) for additional information about snapshot standby databases.

Format

CONVERT DATABASE db\_unique\_name TO {SNAPSHOT | PHYSICAL} STANDBY;

Usage Notes

- A physical standby database cannot be converted to a snapshot standby database if it is the target of a fast-start failover. The `ORA-16668: operation cannot be performed on the fast-start failover target standby database` error will be returned.
- A physical standby database cannot be converted to a snapshot standby database if its `RedoRoutes` configurable property is set to non-NULL value.
- Use the DGMGRL ADD DATABASE command to import an existing snapshot standby database into an Oracle Data Guard broker configuration.
- A snapshot standby database cannot be the target of a switchover or a fast-start failover.
- A snapshot standby database can be the target of a manual failover if fast-start failover is disabled.
- You can use the `SHOW CONFIGURATION` or `SHOW DATABASE` command to verify the conversion result. For example:
	```
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
- After a snapshot standby database is converted back to a physical standby database, it will be in the default state for a physical standby database, `APPLY-ON`.

Command Examples

Example 1: Converting a Physical Standby to a Snapshot Standby

Issue the following to convert a physical standby database to a snapshot standby database:

```
DGMGRL> CONVERT DATABASE 'South_Sales' to SNAPSHOT STANDBY;
Converting database "South_Sales" to a Snapshot Standby database, please wait...
Database "South_Sales" converted successfully
```

Example 2: Converting a Snapshot Standby Back to a Physical Standby

Issue the following to convert the snapshot standby database back to a physical standby database:

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

### 7.10 CREATE CONFIGURATION

The `CREATE CONFIGURATION` command creates a new broker configuration that includes the specified primary database.

Format

CREATE CONFIGURATION configuration\_name AS PRIMARY DATABASE IS database-name CONNECT IDENTIFIER IS connect-identifier;

Command Parameters

configuration-name

A user-friendly name for the configuration you are creating. Valid names contain any alphanumeric characters. If spaces are included in the name, the name must be enclosed in double or single quotation marks. The name must consist of 30 or fewer bytes.

database-name

The name that will be used by the broker to refer to the primary database. It must match (case-insensitive) the value of the primary database `DB_UNIQUE_NAME` initialization parameter.

connect-identifier

A fully specified connect descriptor or a name to be resolved by an Oracle Net Services naming method (for example, TNS). The value you specify is also used as the initial value of the `DGConnectIdentifier` database property.

Usage Notes

- A broker configuration is a named collection of one or more databases that you want to manage as a group. You must specify a value for each of the command parameters. There are no default values.
- You must connect to the primary database to issue this command.
- The broker uses the specified `connect-identifier` to communicate with the specified database from other databases. Therefore, you must ensure that the `connect-identifier` can be used to address the specified database from all databases in your configuration. For example, if TNS is used as the naming method, you must ensure that the tnsnames.ora file on every database and instance that is part of the configuration contains an entry for the `connect-identifier`. The connect identifier must resolve to the same connect descriptor. If the database that is being added is an Oracle RAC database, the `connect-identifier` provided here must reach all instances of the Oracle RAC, preferably with `FAILOVER` attributes set.
	See Also:
	[Oracle Database Net Services Administrator's Guide](https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/dgbkr&id=NETAG186)
- To add standby databases after you create the broker configuration, use the ADD DATABASE command.
- You must clear any remote redo transport destinations on the primary database that do not have the `NOREGISTER` attribute, before a configuration can be created.

Command Example

The following example creates a new broker configuration named `DRSolution` with a primary database named `North_Sales`.

```
DGMGRL> CREATE CONFIGURATION 'DRSolution' AS
> PRIMARY DATABASE IS 'North_Sales'
> CONNECT IDENTIFIER IS North_Sales.example.com;
Configuration "DRSolution" created with primary database "North_Sales"
```

### 7.11 DISABLE CONFIGURATION

The `DISABLE CONFIGURATION` command disables broker management of a configuration so that the configuration and all of its databases are no longer managed by the broker.

Format

DISABLE CONFIGURATION;

Command Parameters

None.

Usage Notes

- A disabled configuration and all of its constituent databases are no longer managed by the broker.
- The only way to disable broker management of the primary database is to use the `DISABLE CONFIGURATION` command.
- This command does not remove the broker configuration from the configuration file. See the REMOVE CONFIGURATION command for more information about removing the configuration.
- You can edit database properties and modify the configuration's protection mode while the configuration is disabled. However, any changes made to properties or to the protection mode will not take effect until the configuration is enabled.
- This command cannot be executed if fast-start failover is enabled.

Command Example

The following example disables management of the broker configuration and all of its databases.

```
DGMGRL> DISABLE CONFIGURATION;
Disabled.
```

### 7.12 DISABLE DATABASE

The `DISABLE DATABASE` command disables broker management of the named standby database.

This means that broker directed state changes will be disallowed for this database, and the broker will not monitor the database for health status or for monitorable properties.

Format

DISABLE DATABASE database-name;

Command Parameters

database-name

Name of the standby database to be disabled.

Usage Notes

- You cannot specify the name of a primary database.
- Use the `DISABLE CONFIGURATION` command to disable the primary and all standby databases.
- If the sole standby database is disabled, you have no failover option. This standby database is not viable for failover until it is reenabled.
- This command cannot be used to disable the fast-start failover target database when fast-start failover is enabled.

Command Example

The following example shows how to disable a database named `South_Sales`.

```
DGMGRL> DISABLE DATABASE 'South_Sales';
Disabled.
```

### 7.13 DISABLE FAR\_SYNC

The `DISABLE FAR_SYNC` command disables broker management of a far sync instance.

Format

DISABLE FAR\_SYNC far\_sync\_instance\_name;

Command Parameters

far\_sync\_instance\_name

The name of the far sync instance to be disabled.

Usage Notes

- A far sync instance that has its `RedoRoutes` property set cannot be disabled.

Command Example

The following example disables broker management of a far sync instance named `chicago`.

```
DGMGRL> DISABLE FAR_SYNC 'chicago';
```

### 7.14 DISABLE FAST\_START FAILOVER

The `DISABLE FAST_START FAILOVER` command prevents the observer from initiating a failover to the target standby database.

See [Disabling Fast-Start Failover](using-data-guard-broker-to-manage-switchovers-failovers.md) for additional information.

Format

DISABLE FAST\_START FAILOVER \[ FORCE \];

Command Parameters

None.

Usage Notes

- If the primary and target standby database have a network connection, use `DISABLE FAST_START FAILOVER` without the `FORCE` option to disable fast-start failover on all databases in the broker configuration. If errors occur during the disable operation, the broker returns an error message and stops the disable operation. You may need to reissue the `DISABLE FAST_START FAILOVER` command with the `FORCE` option to override the error conditions and disable fast-start failover on the database to which you are connected. See [Disabling Fast-Start Failover](using-data-guard-broker-to-manage-switchovers-failovers.md) for more information.
- Use `DISABLE FAST_START FAILOVER` with the `FORCE` option when the network between the primary and target standby databases is disconnected or when the database upon which the command is received does not have a connection with the primary database. The `FORCE` option disables fast-start failover on the database to which you are connected, even when errors occur.
- Disabling fast-start failover with the `FORCE ` option on a primary database that is disconnected from the observer and the target standby database does not prevent the observer from initiating a fast-start failover to the target standby database.
- You can disable fast-start failover while connected to any database in the broker configuration so long as connectivity exists between that database and the primary.
- If disabled by force at the target standby database and the connection subsequently resumes with the primary database, fast-start failover is disabled on all databases in the configuration.
- Disabling fast-start failover with the `FORCE` option while connected to the primary will disable fast-start failover on the target standby database if there is network connectivity between both databases.

Command Examples

Example 1: Disabling a Fast-Start Failover

The following example shows how to disable fast-start failover.

```
DGMGRL> DISABLE FAST_START FAILOVER;
Disabled.
```

Example 2: Using FORCE When Disabling Fast-Start Failover

The following example uses the `FORCE` option which disables fast-start failover on the database to which you are connected.

```
DGMGRL> DISABLE FAST_START FAILOVER FORCE;
Disabled.
```

### 7.15 DISABLE FAST\_START FAILOVER CONDITION

The ` DISABLE FAST_START FAILOVER CONDITION` command allows you to remove conditions for which a fast-start failover should be performed.

Format

DISABLE FAST\_START FAILOVER CONDITION value;

Command Parameters

value

Possible values are any conditions for which a fast-start failover has been enabled.

Usage Notes

If the condition has not been set or if it is an unrecognized condition, then an error is raised.

Command Example

This example specifies that the detection of a corrupted control file does not automatically initiate an immediate fast-start failover.

```
DGMGRL> DISABLE FAST_START FAILOVER CONDITION "Corrupted Controlfile";
```

### 7.16 DISABLE RECOVERY\_APPLIANCE

The DISABLE RECOVERY\_APPLIANCE command disables broker management of the named Zero Data Loss Recovery Appliance (Recovery Appliance).

Disabling broker management of a Recovery Appliance means that the broker will not monitor the health of the transport to the Recovery Appliance. However, redo transport to the Recovery Appliance will not be shut off.

Format

DISABLE RECOVERY\_APPLIANCE object\_name;

Command Parameters

object name

Name of the Recovery Appliance to be disabled.

Command Example

The following example shows how to disable a Recovery Appliance named `EnterpriseRecoveryAppliance`.

```
DGMGRL> DISABLE RECOVERY_APPLIANCE 'EnterpriseRecoveryAppliance';
Disabled.
```

### 7.17 EDIT CONFIGURATION (Property)

The `EDIT CONFIGURATION SET PROPERTY` command changes the value of a property for the broker configuration.

hanges the value of a p

Format

EDIT CONFIGURATION SET PROPERTY property-name = value;

Command Parameters

property-name

The name of a configuration property.

value

The new value for the property.

See Also:

[Managing the Members of a Broker Configuration](managing-oracle-data-guard-broker-configuration-members.md) and [Oracle Data Guard Broker Properties](oracle-data-guard-broker-properties.md) for information about configuration properties

Usage Notes

- Issue this command while connected to the primary database or to any standby database in the broker configuration having connectivity to the primary database.
- Use the `SHOW CONFIGURATION` command to display the current property information for the configuration.

Command Example

The following example shows how to set the `FastStartFailoverThreshold` configuration property to 90 seconds.

```
DGMGRL> EDIT CONFIGURATION SET PROPERTY FastStartFailoverThreshold=90;
```

### 7.18 EDIT CONFIGURATION (Protection Mode)

The `EDIT CONFIGURATION SET PROTECTION MODE AS` command edits the current protection mode setting for the broker configuration.

Format

EDIT CONFIGURATION SET PROTECTION MODE AS protection-mode;

Command Parameters

protection-mode

The data protection mode in which you want the configuration to run when the configuration is enabled. The possible protection modes are:

- `MAXPROTECTION`
- `MAXAVAILABILITY`
- `MAXPERFORMANCE`

Usage Notes

- Before you use the `EDIT` `CONFIGURATION` command to set the protection mode, ensure that at least one standby is configured to receive redo via `SYNC` or `FASTSYNC` mode if it receives redo directly from the primary. If the standby receives redo via a far sync instance, the far sync instance must be configured to receive redo via `SYNC` or `FASTSYNC` mode and the standby must be configured to receive redo via `ASYNC` mode.
- The following table shows the configuration protection modes and the minimum corresponding settings for redo transport services:
	| Protection Mode | Redo Transport | Standby Redo Log Files Needed? | Usable with Fast-Start Failover? |
	| --- | --- | --- | --- |
	| `MAXPROTECTION` | `SYNC` | Yes | Yes |
	| `MAXAVAILABILITY` | `SYNC` or `FASTSYNC` | Yes | Yes |
	| `MAXPERFORMANCE` | `ASYNC` | Yes | Yes |
	The default protection mode for the configuration is `MAXPERFORMANCE`.
	See Also:
	[Managing the Members of a Broker Configuration](managing-oracle-data-guard-broker-configuration-members.md) for more information about the protection modes and redo transport services
- This command cannot be executed if fast-start failover is enabled.
- Upgrading from `MAXPERFORMANCE` to `MAXPROTECTION` is not allowed. You must first go to `MAXAVAILABILITY` and then to `MAXPROTECTION`.
- Use the `SHOW CONFIGURATION` command to display the current protection mode for the configuration.
	```
	DGMGRL> SHOW CONFIGURATION;
	 
	Configuration - DRSolution
	 
	  Protection Mode: MaxPerformance
	  Members:
	    North_Sales  - Primary database
	      South_Sales     - Physical standby database
	 
	Fast-Start Failover: DISABLED
	 
	Configuration Status:
	SUCCESS
	```

If broker management of the configuration is disabled when you enter the `EDIT CONFIGURATION` command, the protection mode of the configuration does not take effect until the next time you enable the configuration with the ENABLE CONFIGURATION command.

Command Example

The following example shows how to upgrade the broker configuration to the `MAXAVAILABILITY` protection mode.

Verify that standby redo log files are configured on the standby database and that the redo transport service is set to `SYNC`, for example:

```
DGMGRL> EDIT DATABASE 'South_Sales' SET PROPERTY 'LogXptMode'='SYNC';
Property "LogXptMode" updated
 
DGMGRL> EDIT CONFIGURATION SET PROTECTION MODE AS MAXAVAILABILITY;
Succeeded.
```

### 7.19 EDIT CONFIGURATION (RENAME)

The `EDIT CONFIGURATION RENAME TO` command changes a configuration’s name.

Format

EDIT CONFIGURATION RENAME TO new-configuration-name;

Command Parameters

new-configuration-name

The new name for the configuration.

Command Example

The following example shows how to rename a configuration named `DR_Sales` to `HA_Sales`.

```
DGMGRL> SHOW CONFIGURATION

Configuration - DR_Sales

  Protection Mode: MaxPerformance
  Members:
    North_Sales  - Primary database
      South_Sales  - Physical standby database

Fast-Start Failover: DISABLED

Configuration Status:
DISABLED

DGMGRL> EDIT CONFIGURATION RENAME TO "HA_Sales";
Succeeded.
DGMGRL> ENABLE CONFIGURATION
Enabled.
DGMGRL> SHOW CONFIGURATION

Configuration - HA_Sales

  Protection Mode: MaxPerformance
  Members:
    North_Sales  - Primary database
      South_Sales  - Physical standby database

Fast-Start Failover: DISABLED

Configuration Status:
SUCCESS
```

### 7.20 EDIT CONFIGURATION RESET (Property)

The `EDIT CONFIGURATION RESET PROPERTY` command resets the specified configuration property to its default value.

Format

EDIT CONFIGURATION RESET PROPERTY property-name;

Command Parameters

property-name

The name of an existing configuration property.

Usage Notes

- Issue this command while connected to the primary database or to any standby database in the broker configuration having connectivity to the primary database.
- Use the `SHOW CONFIGURATION` command to display the current property information for the configuration.

Command Example

The following example shows how to reset the `BystandersFollowChange` property.

```
DGMGRL> EDIT CONFIGURATION RESET PROPERTY BystandersFollowChange;
Succeeded.
```

### 7.21 EDIT DATABASE (Property)

The `EDIT DATABASE` command changes the name used by the broker for the specified database.

Format

EDIT DATABASE database-name SET PROPERTY property-name = value;

Command Parameters

database-name

The name of the database for which you want to change a property value.

property-name

The name of an existing database-specific property. If this is an Oracle RAC database, this property change affects all instances of the database.

See Also:

[Managing the Members of a Broker Configuration](managing-oracle-data-guard-broker-configuration-members.md) and [Oracle Data Guard Broker Properties](oracle-data-guard-broker-properties.md) for information about properties.

value

The new value for the property.

Note:

This command can be used to change the value of an instance-specific property if and only if just one instance is known by the broker for the named database. An attempt to use this command to change an instance-specific property when the broker knows of multiple instances of the database will be rejected. It is recommended to only use `EDIT INSTANCE (property)` to change the value of an instance-specific property.

Command Examples

Example 1: Editing a Configurable Property at the Database Level

The following example edits a configurable property at the database level.

```
DGMGRL> EDIT DATABASE 'North_Sales' SET PROPERTY 'ArchiveLagTarget'=1200;
Property "ArchiveLagTarget" updated
```

Example 2: Editing a Configurable Instance-Specific Property of a non-Oracle RAC Database

The following example edits a configurable instance-specific property of a non-Oracle RAC database.

```
DGMGRL> EDIT DATABASE 'South_Sales' SET PROPERTY 
> 'StandbyArchiveLocation'='/archfs/arch/';
Property "StandbyArchiveLocation" updated
```

Example 3: Editing a Configurable Instance-Specific Property of an Oracle RAC Database

The following example edits a configurable instance-specific property of an Oracle RAC database. This will not succeed because it is not clear to which instance the property change should be applied.

```
DGMGRL> EDIT DATABASE 'North_Sales' SET PROPERTY
> 'StandbyArchiveLocation'='/archfs/arch/';
Error: ORA-16587: ambiguous object specified to Data Guard broker Failed.
```

Example 4: Editing a List of Fast-Start Failover Targets

The following examples show how to specify a list of fast-start failover targets.

```
DGMGRL> EDIT DATBASE db1 SET PROPERTY FastStartFailoverTarget='db2, db3';
```
```
DGMGRL> EDIT DATABASE db2 SET PROPERTY FastStartFailoverTarget='db1,db3';
```
```
DGMGRL> EDIT DATABASE db3 SET PROPERTY FastStartFailoverTarget='db1';
```

### 7.22 EDIT DATABASE (Rename)

The `EDIT DATABASE` (Rename) command changes the name used by the broker to refer to the specified database.

Format

EDIT DATABASE database-name RENAME TO new-database-name;

Command Parameters

database-name

The name of the database that you want to change.

new-database-name

The new name of the database.

Usage Notes

- Use this command to track changes to the `DB_UNIQUE_NAME` initialization parameter for this database.
	Caution:
	The `database-name` must always match the value for that database's `DB_UNIQUE_NAME` initialization parameter.
- This command can only be done when broker management of the database that you are renaming is disabled.

Command Example

The following example shows how to edit and rename a database.

```
DGMGRL> DISABLE DATABASE 'South_Sales_typo';
Disabled.

DGMGRL> EDIT DATABASE 'South_Sales_typo' RENAME TO 'South_Sales';
Succeeded.

DGMGRL> ENABLE DATABASE 'South_Sales';
Enabled.
```

### 7.23 EDIT DATABASE (State)

The `EDIT DATABASE` (State) command changes the state of the specified database.

Format

EDIT DATABASE database-name SET STATE= state \[WITH APPLY INSTANCE= instance-name\];

Command Parameters

database-name

The name of the database for which you want to change the state.

state

The state in which you want the database to be running. The possible states are:

- `TRANSPORT-ON` (primary database only)
- `TRANSPORT-OFF` (primary database only)
- `APPLY-ON` (physical or logical standby database only)
- `APPLY-OFF` (physical or logical standby database only)

instance-name

The name of the instance you want to become the apply instance if this is an Oracle RAC standby database.

Usage Notes

- If the target state is `APPLY-ON` and this database is currently a physical or logical standby database, the optional `WITH APPLY INSTANCE` clause specifies which instance will become the apply instance.
- If the target state is not `APPLY-ON` or if the database is currently in the primary role, the `WITH APPLY INSTANCE` clause is ignored even if it is specified.
- You cannot change the state of a snapshot standby database.
- All instances of an Oracle RAC database are affected by this database state change.

Command Example

The following examples show how to change the state of a database.

```
DGMGRL> EDIT DATABASE 'South_Sales' SET STATE='APPLY-ON';
Succeeded.
```

### 7.24 EDIT DATABASE RESET (Property)

The `EDIT DATABASE RESET` (Property) command reset the specified property for the named database back to its default value.

Format

EDIT DATABASE database-name RESET PROPERTY property-name;

Command Parameters

database-name

The name of the database for which you want to reset the property value back to its default.

property-name

The name of an existing database-specific configurable property.

Command Example

The following example shows how to reset the `NetTimeout` property for the database named `South_Sales`.

```
DGMGRL> EDIT DATABASE 'South_Sales' RESET PROPERTY NetTimeout;
Succeeded.
```

### 7.25 EDIT FAR\_SYNC

The `EDIT FAR_SYNC` property changes the name and/or properties of a far sync instance.

Format

EDIT FAR\_SYNC far\_sync\_instance\_name RENAME TO new\_far\_sync\_instance\_name;  
  
EDIT FAR\_SYNC far\_sync\_instance\_name SET PROPERTY property\_name = value;

Command Parameters

far\_sync\_instance\_name

The name of the far sync instance for which you want to edit information. It must match (case-insensitive) the value of the corresponding database `DB_UNIQUE_NAME` initialization parameter.

new\_far\_sync\_instance\_name

The new name of the far sync instance.

property\_name

The name of an existing far sync instance-specific configurable property.

Command Example

The following example renames a far sync instance named `chicago` to the name `dallas`.

```
DGMGRL> DISABLE FAR_SYNC 'chicago_typo';EDIT FAR_SYNC 'chicago_typo' RENAME TO 'chicago';ENABLE FAR_SYNC 'chicago;
```

### 7.26 EDIT FAR\_SYNC RESET (Property)

The `EDIT FAR_SYNC RESET` (Property) command resets the specified property for the named far sync instance to its default value.

Format

EDIT FAR\_SYNC far\_sync\_instance\_name RESET PROPERTY property-name;

Command Parameters

far\_sync\_instance\_name

The name of the far sync instance for which you want to edit information. It must match (case-insensitive) the value of the corresponding database `DB_UNIQUE_NAME` initialization parameter.

property\_name

The name of the property to be reset to its default value.

Command Example

The following example shows how to reset the `ReopenSecs` property back to its default value for the far sync instance named `dallas`.

```
DGMGRL> EDIT FAR_SYNC 'dallas' RESET PROPERTY ReopenSecs;
```

### 7.27 EDIT INSTANCE (AUTO PFILE)

The `EDIT INSTANCE` (AUTO PFILE) command sets the name of the initialization parameter file for the specified instance.

Format

EDIT INSTANCE instance-name

\[ON DATABASE database-name\] SET AUTO PFILE \[= { initialization-file | OFF } \];

Command Parameters

instance-name

The name of the instance (SID) for which you want to specify its initialization parameter file.

database-name

The name of the database to which the `instance-name` is associated.

initialization-file

Executes the startup operation for the instance when a subsequent broker operation requires the instance to be started automatically. If `SET AUTO PFILE` is set to `OFF`, automatic restart of that instance is disabled. When a subsequent operation needs to start that instance, you must start it manually. If you do not specify `SET AUTO PFILE` for the instance, the automatic startup operation looks for the initialization parameter file at the default location.

Usage Notes

- The `instance-name` can be unique across the configuration. If `instance-name` is not unique, you must specify both the `database-name` and the `instance-name` to fully identify the instance.
- `SET AUTO PFILE` is valid only for the duration of the current DGMGRL session. You must specify `SET AUTO PFILE` again if you quit and reenter DGMGRL.

Command Example

The following example shows how to change the parameter file used to start an instance of a database.

```
DGMGRL> EDIT INSTANCE 'south_sales1' ON DATABASE 'South_Sales' 
> SET AUTO PFILE='initsales1.ora';
Instance 'south_sales1' updated
```

### 7.28 EDIT INSTANCE (Property)

The `EDIT INSTANCE` (Property) command changes the value of an instance-specific property for the specified instance(s).

Format

EDIT INSTANCE { { instance-name \[ON {DATABASE database-name | FAR\_SYNC far-sync-name }\] } | {\* ON {DATABASE database-name | FAR\_SYNC far-sync-name } } }

SET PROPERTY property-name = value;

Command Parameters

instance-name

The name of the instance (SID) for which you want to change an instance-specific property's value. If an asterisk is specified for instance-name, then either the `ON DATABASE` clause or the `ON` `FAR_SYNC` clause must also be specified and this change will be applied to the specified property for each instance associated with that database or far sync. See [Oracle Data Guard Broker Properties](oracle-data-guard-broker-properties.md) for the instance-specific properties that can be changed using this command.

database-name

The name of the database with which the `instance-name` is associated. This must be specified if an asterisk is specified for `instance-name`, or if `instance-name` is not unique across the configuration

far-sync-name

The name of the far sync with which the `instance-name` is associated.

property-name

The name of the instance-specific property for which you want to set a new value.

See Also:

[Managing the Members of a Broker Configuration](managing-oracle-data-guard-broker-configuration-members.md) and [Oracle Data Guard Broker Properties](oracle-data-guard-broker-properties.md) for information about properties.

value

The new value for the property.

Usage Notes

- The `instance-name` can be unique across the configuration. If `instance-name` is not unique, you must specify both the `database-name` (or `far-sync-name`) and the `instance-name` to fully identify the instance.
- This command cannot be used to change a database-specific property.

Command Examples

Example 1: Editing an Instance-Specific Property

Edit an instance-specific property.

```
DGMGRL> EDIT INSTANCE 'north_sales1' ON DATABASE 'North_Sales' 
> SET PROPERTY 'StandbyArchiveLocation'='/archfs/arch/';
Property "StandbyArchiveLocation" updated.
```

Example 2: Editing a Database-Specific Property

Edit a database-specific property. This will not be allowed.

```
DGMGRL> EDIT INSTANCE 'north_sales1' ON DATABASE 'North_Sales' 
> SET PROPERTY 'LogXptMode'='SYNC';
Error: ORA-16586: cannot change database property with EDIT INSTANCE command

Failed.
```

Example 3: Changing Instance-Specific Property for All Instances on an Oracle RAC Database

Change the value of an instance-specific property for all instances of an Oracle RAC database:

```
DGMGRL> EDIT INSTANCE * ON DATABASE 'North_Sales'
> SET PROPERTY LogArchiveTrace=4095;
```

Example 4: Changing Instance-Specific Property for All Instances of an Oracle RAC Far Sync

Change the value of an instance-specific property for all instances of an Oracle RAC far sync instance:

```
DGMGRL> EDIT INSTANCE * ON FAR_SYNC 'dallas' SET PROPERTY LogArchiveTrace=4095;
```

### 7.29 EDIT INSTANCE RESET (Property)

The `EDIT INSTANCE RESET` (Property) command resets an instance-specific property for the specified instance(s) to its default value.

Format

EDIT INSTANCE { { instance-name \[ON {DATABASE database-name | FAR\_SYNC far-sync-name }\] } | {\* ON {DATABASE database-name | FAR\_SYNC far-sync-name } } } RESET PROPERTY property-name;

Command Parameters

instance-name

The name of the instance (SID) for which you want to reset an instance-specific property's value to the default. If an asterisk is specified for instance-name, the `ON DATABASE` clause must also be specified and the property will be reset to the default for each instance associated with that database.

database-name

The name of the database with which the `instance-name` is associated. This must be specified if an asterisk is specified for `instance-name`, or if `instance-name` is not unique across the configuration.

property-name

The name of the instance-specific property that you want to reset to its default value.

See Also:

[Managing the Members of a Broker Configuration](managing-oracle-data-guard-broker-configuration-members.md) and [Oracle Data Guard Broker Properties](oracle-data-guard-broker-properties.md) for information about properties.

value

The new value for the property.

Usage Notes

- The `instance-name` can be unique across the configuration. If `instance-name` is not unique, you must specify both the `database-name` and the `instance-name` to fully identify the instance.
- This command cannot be used to change a database-specific property.

Command Examples

Example 1: Resetting a Property for a Specific Instance

The following command shows how to reset the `LogArchiveTrace` property for the specific instance `south1` on the database named `South_Sales`.

```
DGMGRL> EDIT INSTANCE 'south1' ON DATABASE 'South_Sales' 
> RESET PROPERTY LogArchiveTrace;
Succeeded.
```

Example 2: Resetting a Property for All Instances of a Database

The following example shows how to reset the LogArchiveTrace property for all instances of the database named South\_Sales.

```
DGMGRL> EDIT INSTANCE * ON DATABASE 'South_Sales' RESET PROPERTY LogArchiveTrace;
Succeeded.
```

### 7.30 EDIT RECOVERY\_APPLIANCE (Property)

The `EDIT RECOVERY_APPLIANCE` (Property) command changes the value of the property for the named Zero Data Loss Recovery Appliance (Recovery Appliance).

Format

EDIT object name SET PROPERTY property-name = value;

Command Parameters

object name

The name of the Recovery Appliance for which you want to change a property value.

property-name

The name of an existing Recovery Appliance-specific property. Valid properties are as follows:

- `DGConnectIdentifier`
- `LogXptMode`
- `DelayMins`
- `Binding`
- `MaxFailure`
- `MaxConnections`
- `ReopenSecs`
- `NetTimeout`
- `RedoCompression`
- `LogShipping`
- `ArchiveLagTarget`
- `LogArchiveMaxProcesses`
- `LogArchiveMinSucceedDest`
- `InconsistentProperties`
- `InconsistentLogXptProps`
- `AlternateLocation`

value

The new value for the property.

Command Example

The following example shows an example of editing a configurable property.

```
DGMGRL> EDIT RECOVERY_APPLIANCE 'EnterpriseRecoveryAppliance' SET PROPERTY 'ReopenSecs'=300;
Property "ReopenSecs" updated
```

### 7.31 EDIT RECOVERY\_APPLIANCE (Rename)

The `EDIT RECOVERY_APPLIANCE` (Rename) command changes the name used by the broker to refer to the specified Recovery Appliance, as recorded in that Recovery Appliance's profile in the broker configuration.

Format

EDIT RECOVERY\_APPLIANCE object name RENAME TO new object name;

Command Parameters

object name

The name of the Recovery Appliance that you want to change.

new object name

The new name of the Recovery Appliance.

Usage Notes

- Use this command to track changes to the `DB_UNIQUE_NAME` initialization parameter for this Recovery Appliance.
	Caution:
	The name of the Recovery Appliance must always match the value of the `DB_UNIQUE_NAME` initialization parameter for that Recovery Appliance.

Command Example

The following example shows how to edit and rename a Recovery Appliance.

```
DGMGRL> EDIT RECOVERY_APPLIANCE 'EnterpriseRecoveryAppliance_typo'
RENAME TO 'EnterpriseRecoveryAppliance';
Succeeded.
```

### 7.32 EDIT RECOVERY\_APPLIANCE RESET (Property)

The `EDIT RECOVERY_APPLIANCE RESET` (Property) command resets the specified property for the named Recovery Appliance to its default value.

Format

EDIT RECOVERY\_APPLIANCE object name RESET PROPERTY property-name;

Command Parameters

object name

The name of the Recovery Appliance for which you want to reset the property value back to its default.

property-name

The name of an existing database-specific configurable property.

Command Example

The following example shows how to reset the `ReopenSecs` property back to its default value for the Recovery Appliance named `South_Sales`.

```
DGMGRL> EDIT DATABASE 'South_Sales' RESET PROPERTY ReopenSecs;
Succeeded.
```

### 7.33 ENABLE CONFIGURATION

The `ENABLE CONFIGURATION` command enables the broker to manage the broker configuration, including all of its databases.

ble

Format

ENABLE CONFIGURATION;

Command Parameters

None.

Usage Notes

- Use this command to enable broker management of the primary database and all members of the configuration, if these members are not explicitly disabled by the user.
- To issue this command, you must connect to a database whose control file role is primary.
- By default, broker management of the configuration's databases is enabled in the `TRANSPORT-ON` state with redo transport services turned on at the primary database and `APPLY-ON` with log apply services started at the standby databases. Far sync instances will be enabled such that they receive redo data and send redo data. You can change the state of a database using the EDIT DATABASE (State) command, but not when the database or the entire configuration is disabled. You cannot change the state of a far sync instance.
- Use the SHOW CONFIGURATION command to display information about the configuration.
- Use this command to update the roles stored in the broker configuration if a failover or switchover was performed using SQL\*Plus instead of DGMGRL or Cloud Control.

Command Example

The following example enables management of a broker configuration.

```
DGMGRL> ENABLE CONFIGURATION;
Enabled.
```

### 7.34 ENABLE DATABASE

The `ENABLE DATABASE` command enables broker management of the specified standby database.

Caution:

Do not issue the `ENABLE DATABASE` command on a standby database that needs to be reinstated. See [Reenabling Disabled Databases After a Role Change](using-data-guard-broker-to-manage-switchovers-failovers.md) for more details.

Format

ENABLE DATABASE database-name;

Command Parameters

database-name

The name of the standby database for which you want to enable broker management.

Usage Notes

- You must connect to the primary database or to an already enabled standby database to issue this command.
- A standby database may have been disabled by the broker as a consequence of a prior failover or switchover operation. See [Reenabling Disabled Databases After a Role Change](using-data-guard-broker-to-manage-switchovers-failovers.md) to understand how the database can be reinstated or re-created.
- By default, broker management of the physical or logical standby database is enabled in the `APPLY-ON` state with log apply services enabled. You can change the state of the standby database using the EDIT DATABASE (State) command, but only when the database is enabled.
- Use the SHOW DATABASE command to display information about the database.
- For an Oracle RAC database, only one instance is required to be started and mounted for this command to succeed.

Command Example

The following example shows how to enable a database named `South_Sales`.

```
DGMGRL> ENABLE DATABASE 'South_Sales';
Enabled.
```

### 7.35 ENABLE FAR\_SYNC

The `ENABLE FAR_SYNC` command enables broker management of the specified far sync instance.

Format

ENABLE FAR\_SYNC far\_sync\_instance\_name;

Command Parameters

far\_sync\_instance\_name

The name of the far sync instance for which you want to enable broker management.

Command Example

The following example enables broker management of a far sync instance named `dallas`.

```
DGMGRL> ENABLE FAR_SYNC 'dallas';
```

### 7.36 ENABLE FAST\_START FAILOVER

The `ENABLE FAST_START FAILOVER` command enables the broker to fail over to a specifically-chosen standby database in the event of loss of the primary database, without requiring any manual steps.

See [Enabling Fast-Start Failover](using-data-guard-broker-to-manage-switchovers-failovers.md) for complete information.

Format

ENABLE FAST\_START FAILOVER;

Command Parameters

None.

Usage Notes

- The prerequisites described in [Prerequisites for Enabling Fast-Start Failover](using-data-guard-broker-to-manage-switchovers-failovers.md) must be met before you issue this command to enable fast-start failover.
- Issuing the `ENABLE FAST_START FAILOVER` command does not trigger a failover, it only allows the observer that is monitoring the configuration to initiate a fast-start failover if conditions warrant a failover.
- You can enable fast-start failover while connected to any database in the broker configuration.
- If you do not start the observer after you have enabled fast-start failover, the `ORA-16819` warning is displayed for the primary and target standby databases. For example:
	```
	DGMGRL> SHOW DATABASE 'South_Sales';
	Database - South_Sales
	 
	  Role:            PRIMARY
	  Intended State:  TRANSPORT-ON
	  Instance(s):
	    south_sales1
	 
	  Database Warning(s):
	    ORA-16819: fast-start failover observer not started
	 
	Database Status:
	WARNING
	```
- To enable fast-start failover for a broker configuration with multiple standby databases, the `FastStartFailoverTarget` configuration property on the primary database must specify one or more viable target standby databases. Both the primary database and the target standby databases must have:
	- Standby redo logs configured
		- Redo transport must be properly configured at both databases for the configured protection mode
	Oracle also recommends Flashback Database be enabled on both the primary and standby databases to allow for reinstatement of the old primary database after a failover. If it is not enabled, then you will receive a warning when you enable fast-start failover:
	```
	DGMGRL> enable fast_start failover; 
	Warning: ORA-16827: Flashback Database is disabled
	```
	Task 2 in [Enabling Fast-Start Failover](using-data-guard-broker-to-manage-switchovers-failovers.md), and [FastStartFailoverTarget](oracle-data-guard-broker-properties.md) provide more information about the `FastStartFailoverTarget` configuration property.
- Once you have enabled fast-start failover, you must comply with the restrictions described in [Restrictions When Fast-Start Failover is Enabled](using-data-guard-broker-to-manage-switchovers-failovers.md).

Command Examples

Example 1: Enabling a Fast-Start Failover

The following example enables fast-start failover.

```
DGMGRL> ENABLE FAST_START FAILOVER;
Enabled.
```

Example 2: Successful Enabling of Fast-Start Failover

The following example shows that fast-start failover was successfully enabled when the configuration is operating in maximum performance mode.

```
DGMGRL> SHOW FAST_START FAILOVER;
 
Fast-Start Failover: ENABLED
 
Threshold: 30 seconds
Target: South_Sales
Observer: (none)
Lag Limit: 30 seconds
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

### 7.37 ENABLE FAST\_START FAILOVER CONDITION

The `ENABLE FAST_START FAILOVER CONDITION` command specifies additional conditions for which a fast-start failover should be performed.

Format

ENABLE FAST\_START FAILOVER CONDITION value;

Command Parameters

value

Possible values are those described in the `SHOW FAST_START FAILOVER` command as health conditions. The Oracle error `ORA-00240` can also be named as a condition by specifying `240` as the value.

Usage Notes

- Table 7-2 lists some examples of health conditions maintained by the database health-check facility.
- An error is raised if the specified value is not recognized or if the condition has already been set.
- Table 7-2 Examples of Health Conditions
	| Health Condition | Description |
	| --- | --- |
	| "Datafile Offline" | Data file offline due to a write error.  As of Oracle Database 12c Release 2 (12.2.0.1), the Datafile Offline health condition is replaced with the Datafile Write Errors condition. The Datafile Offline condition can still be specified, for backward compatibility reasons. |
	| Datafile Write Errors | If fast-start failover is enabled and the Datafile Write Errors condition is specified, then a fast-start failover is initiated if write errors are encountered in any data files, including temp files, system data files, and undo files. |
	| "Corrupted Controlfile" | Corrupted controlfile. This condition is enabled by default. |
	| "Corrupted Dictionary" | Dictionary corruption of a critical database object. This condition is enabled by default. |
	| "Inaccessible Logfile" | LGWR is unable to write to any member of a log group due to an I/O error. |
	| "Stuck Archiver" | Archiver is unable to archive a redo log because device is full or unavailable. |
- You can display these configurable conditions with the `SHOW FAST_START FAILOVER` command.

Command Examples

Example 1

The following example specifies that a fast-start failover should be done if a corrupted controlfile is detected.

```
ENABLE FAST_START FAILOVER CONDITION "Corrupted Controlfile";
```

Example 2

The following example specifies that a fast-start failover should be done if an ORA-00240 error is raised.

```
ENABLE FAST_START FAILOVER CONDITION 240;
```

Example 3

The following example displays output that shows the condition Datafile Write Errors.

```
DGMGRL> ENABLE FAST_START FAILOVER CONDITION "Datafile Write Errors"
Succeeded.

DGMGRL> SHOW FAST_START FAILOVER

Fast-Start Failover: DISABLED

  Threshold:          180 seconds
  Target:             (none)
  Observer:           (none)
  Lag Limit:          300 seconds
  Shutdown Primary:   TRUE
  Auto-reinstate:     TRUE
  Observer Reconnect: (none)
  Observer Override:  FALSE

Configurable Failover Conditions
  Health Conditions:
    Corrupted Controlfile          YES
    Corrupted Dictionary           YES
    Inaccessible Logfile            NO
    Stuck Archiver                  NO
    Datafile Write Errors          YES

  Oracle Error Conditions:
    (none)
```

### 7.38 ENABLE RECOVERY\_APPLIANCE

The `ENABLE RECOVERY_APPLIANCE` command enables broker management of the specified Zero Data Loss Recovery Appliance (Recovery Appliance).

Format

ENABLE RECOVERY\_APPLIANCE object name;

Command Parameters

object name

The name of the Recovery Appliance for which you want to enable broker management.

Usage Notes

- You must connect to the primary database or to an already enabled standby database to issue this command.
- Use the `SHOW RECOVERY_APPLIANCE` command to display information about the Recovery Appliance.

Command Example

The following example shows how to enable a Recovery Appliance named `EnterpriseRecoveryAppliance`.

```
DGMGRL> ENABLE RECOVERY_APPLIANCE 'EnterpriseRecoveryAppliance';Enabled.
```

### 7.39 EXIT

The `EXIT` command exits (quits) the broker’s command-line interface.

Format

EXIT;

Command Parameters

None.

Usage Notes

- This command has the same effect as the QUIT command.
- A database connection is not required to execute this command. However, if you are connected, this command breaks the connection.

Command Example

The following example demonstrates how to exit (quit) the command-line interface.

```
DGMGRL> EXIT;
```

### 7.40 FAILOVER

The `FAILOVER` command invokes a failover that transitions the named (target) standby database into the role of a primary database.

This type of failover is referred to as a manual failover. See [Manual Failover](using-data-guard-broker-to-manage-switchovers-failovers.md) for more information.

Note:

Because a failover results in a transition of a standby database to the primary role, it should be performed when the primary database has failed or is unreachable and cannot be recovered in a timely manner. Failover may or may not result in data loss depending on the protection mode in effect at the time of the failover and whether the target standby database was synchronized with the primary database.

Use the `SWITCHOVER` command if the primary database has not failed and you want the current primary database and a standby database to switch roles with no data loss.

Format

FAILOVER TO database-name \[IMMEDIATE\];

Command Parameters

database-name

The name of a physical, logical, or snapshot standby database that you want to fail over to the primary database role.

Usage Notes

- Always try to perform a complete failover first unless Redo Apply has stopped at the failover target due to an `ORA-752` or `ORA-600` `[3020] ` error. If one of these errors has occurred, then before proceeding follow the guidelines in "Resolving ORA-752 or ORA-600 \[3020\] During Standby Recovery" in My Oracle Support Note 1265884.1 at [`http://support.oracle.com`](http://support.oracle.com/). An immediate failover should only be performed when a complete failover is unsuccessful or in the error case just noted.
- The specified standby database must be enabled before the primary database fails. However, an enabled standby database that was shut down can be a candidate for the failover operation. In this case, restart the standby database using DGMGRL `STARTUP` command, then issue the `FAILOVER` command.
- The failover operates on the specified standby database and changes its role to a primary database. Bystander standby databases (those not involved in the failover) remain in the standby role.
- Before you issue the `FAILOVER` command, verify that you are connected to the standby database that will become the new primary database. If necessary, issue a CONNECT command to connect to the standby database to which you want to failover.
- If the `FAILOVER` command is issued without any options, the standby database chosen as the failover target applies all unapplied redo it has received before changing to the primary role. This is referred to as a complete failover.
- If the broker configuration is operating in maximum protection mode, a manual failover operation will force the protection mode to be maximum performance. The redo transport service settings are unaffected. You need to restore the desired protection mode for the resulting configuration after the failover operation.
	Note:
	With fast-start failover, the broker preserves the protection mode that was in effect prior to the failover.
- If the `FAILOVER` command is issued with the `IMMEDIATE` option, no attempt is made to apply any unapplied redo that has been received. This option more likely results in lost application data even when standby redo log files are configured on the standby database. Additionally, any remaining standby databases in the configuration cannot function as such until they are reinstated or re-created. See [Reenabling Disabled Databases After a Role Change](using-data-guard-broker-to-manage-switchovers-failovers.md) for more information.
- You can perform a manual failover or set up the broker to perform a fast-start failover. See the ENABLE FAST\_START FAILOVER command for information about allowing the broker to automatically invoke failover, when conditions warrant a failover.
- If fast-start failover is enabled, you can perform a complete manual failover only to the fast-start failover target standby database and only if the fast-start failover target standby database is synchronized with, or within the lag limit of, the primary database, and only when the observer is started. You cannot perform an immediate manual failover when fast-start failover is enabled.
- If Flashback Database was enabled on the former (failed) primary database prior to the failover, the former primary database can be reinstated using the broker's `REINSTATE` command (see the REINSTATE DATABASE command).
	If failover was performed to a physical standby database, any other physical standby databases that were disabled by the failover can be reinstated if Flashback Database was enabled on the standby database and there are sufficient flashback logs available. See [Reenabling Disabled Databases After a Role Change](using-data-guard-broker-to-manage-switchovers-failovers.md) for step-by-step instructions.
- The original primary database can only participate in the configuration as a standby database after it is reinstated or re-created.
	Caution:
	You should shut down the original primary database if it still has any active instances running prior to failing over.
	See Also:
	[Reenabling Disabled Databases After a Role Change](using-data-guard-broker-to-manage-switchovers-failovers.md) about reenabling the original primary database so that it could serve as a standby database to the primary database

Command Example

The following example performs a failover in which the standby database, `South_Sales`, transitions to the primary role:

```
DGMGRL> FAILOVER TO 'South_Sales';
Performing failover NOW, please wait...
Failover succeeded, new primary is "South_Sales"

DGMGRL> SHOW CONFIGURATION;
Configuration - DRSolution
 
  Protection Mode: MaxPerformance
  Members:
    South_Sales - Primary database
    North_Sales - Physical standby database (disabled)
      ORA-16661: the standby database needs to be reinstated
 
Fast-Start Failover: DISABLED
 
Configuration Status:
WARNING
```

### 7.41 HELP

The `DISPLAY` command displays online help for the Data Guard command-line interface.

Format

HELP \[command\_name\];

Command Parameters

command\_name

The command for which you want to display help information. If you do not specify a command, then all commands are listed. The following commands are available:
```
@              Execute DGMGRL script file
!              Host operating system command
/              Repeat the last command
--             Comment to be ignored by DGMGRL
add            Adds a member to the broker configuration
connect        Connects to an Oracle database instance
convert        Converts a database from one type to another
create         Creates a broker configuration
disable        Disables a configuration, a member, or fast-start failover
edit           Edits a configuration or a member
enable         Enables a configuration, a member, or fast-start failover
exit           Exits the program
failover       Changes a standby database to be the primary database
help           Displays description and syntax for a command
host           Host operating system command
migrate        Migrate a pluggable database from one configuration to another.
quit           Exits the program
reinstate      Changes a database marked for reinstatement into a viable standby
rem            Comment to be ignored by DGMGRL
remove         Removes a configuration or a member
set            Set a property to a specified value
show           Displays information about a configuration or a member
shutdown       Shuts down a currently running Oracle database instance
spool          store input and output of DGMGRL CLI in a file
sql            Executes a SQL statement
start          Starts the fast-start failover observer
startup        Starts an Oracle database instance
stop           Stops the fast-start failover observer
switchover     Switches roles between a primary and standby database
validate       Performs an exhaustive set of validations for a database
```

Enter `help` ` command_name` to see syntax for individual commands.

Usage Notes

- A database connection is not required to execute this command.

Command Example

The following example gets help on the `EDIT` commands.

```
DGMGRL> HELP EDIT
```

### 7.42 HOST or! (exclamation point)

The DGMGRL `HOST` and! commands allow you to execute operating system command(s) directly through the DGMGRL console without leaving DGMGRL.

The `HOST` command and the! command have the same functionality. They allow you to submit operating system commands while you are logged in to DGMGRL. The DGMGRL prompt becomes a shell prompt which accepts operating system commands. You can also directly submit individual operating system commands to DGMGRL through the Host or! command.

Format

HOST \[command\]

Or alternatively,

! \[command\]

Command Parameters

command

Represents an operating system command

Usage Notes

- If you simply enter `HOST` without specifying a command, then the DGMGRL console becomes an operating system shell prompt until you issue the `EXIT` command to return to the DGMGRL console.
- The HOST and! commands take all the content entered on the command line after them as input for the operating system shell prompt. See Command Example 2 below.

Command Examples

Example 1

The following example shows the `HOST` and! commands being used to execute an individual operating system command in the DGMGRL console.

```
DGMGRL> host date
Executing operating system command(s):" date"
Fri Oct 23 14:08:42 EDT 2015
DGMGRL>

DGMGRL> ! date
Executing operating system command(s):" date"
Fri Oct 23 14:09:20 EDT 2015
DGMGRL>
```

Example 2

In the following example, both of the `DATE` commands are executed in the operating system shell before control is returned to DGMGRL.

```
DGMGRL> ! DATE;DATE;
Executing operating system command(s):" date;date;"
Fri Oct 23 14:11:40 EDT 2015
Fri Oct 23 14:11:40 EDT 2015
DGMGRL>
```

### 7.43 MIGRATE PLUGGABLE DATABASE

The `MIGRATE PLUGGABLE DATABASE` command lets you migrate a pluggable database (PDB) from one multitenant container database (CDB) to another on the same host.

You can migrate a PDB from a primary CDB to another primary CDB or failover a PDB from a standby CDB to a primary CDB. The `MIGRATE PLUGGABLE DATABASE` command has the following prerequisites:

- The destination CDB must be created and started in such a way that it can access the PDB data files at the same file path as the source CDB.
- The source and destination CDBs must each be in a different Data Guard broker configuration.
- The source CDB can either be a primary database or a physical standby database.
- If the source CDB is a physical standby database, then
	- the source and destination CDBs must be running the same Oracle version and patches.
		- the source and destination CDBs must have the same setting for the `COMPATIBLE` initialization parameter.
		- the PDB to be migrated must be closed on its primary CDB.
		- if a PDB failover will result in lost data, then you must specifically choose to execute the failover by using the `IMMEDIATE` option.
- If the source CDB is a primary database, then
	- the destination CDB cannot be running a lower version of Oracle.
		- the setting of the `COMPATIBLE` initialization parameter cannot be set to a lower value on the destination CDB than on the source CDB.
- The services for the PDB must be stopped and removed from the Oracle Clusterware repository of the source database to be migrated. This should be done for all databases in the Data Guard broker configuration of the source database.
- The destination CDB must be open.
- You must have `SYSDBA` privilege for both the source and destination CDBs.

Format

MIGRATE PLUGGABLE DATABASE \[IMMEDIATE\] pdb-name  
TO CONTAINER dest-cdb-name  
USING XML-description-file  
\[CONNECT AS { /@ dest-cdb-connect-identifer | dest-cdb-user / dest-cdb-pass @ dest-cdb-connect-identifer } \];

Command Parameters

pdb-name

The name of the PDB to be migrated.

dest-cdb-name

The database unique name of the CDB to receive the PDB to be migrated.

XML-description-file

An XML file that contains the description of the PDB to be migrated. This file is automatically created by the SQL statements executed by the `MIGRATE PLUGGABLE DATABASE` command.

dest-cdb-user

The user name of the user that has `SYSDBA` access to the destination CDB.

dest-cdb-pass

The password associated with the user name specified for `dest-cdb-user`.

dest-cdb-connect-identifier

An Oracle Net connect identifier used to reach the destination CDB.

Usage Notes

- By default, when this command is used for PDB failover, the failover attempt is rejected if there is a possibility of data loss. You can override this default behavior by using the `IMMEDIATE` option.
- The `IMMEDIATE` option is ignored if the source database is a primary database.
- If a connect identifier is specified, then database credentials are used to authenticate the user on the destination CDB.
- Operating system credentials cannot be used to authenticate the user on the destination CDB. A connect identifier must be specified; a slash (/) is not supported.
- For cases in which a slash (/) is used to specify a connect identifier (for example, `/@boston`), the credentials are fetched from the wallet.
- The following options are available if you want to specify a connect string:
	- `/@dest-cdb-connect-identifier` (credentials are fetched from the wallet)
		- `dest-cdb-user/dest-cdb-pass@dest-cdb-connect-identifier` (uses database credentials)
- To prevent the password from being visible on the command line, specify only a user name with a connect identifier. You will then be prompted for a password. The following options are supported when you supply only a user name and connect identifier:
	- `dest-cdb-user@dest-cdb-connect-identifier` (uses database credentials)
		- `dest-cdb-user/@dest-cdb-connect-identifier` (uses database credentials)
- If you omit the connect string entirely from the command line, then you will be prompted for a user name and password. The following options are supported:
	- `/@dest-cdb-connect-identifier` (no prompt for password, credentials are fetched from the wallet)
		- `dest-cdb-user@dest-cdb-connect-identifier` (uses database credentials)
		- `dest-cdb-user/@dest-cdb-connect-identifier` (uses database credentials)

Command Examples

Example 1: Migrating a PDB From a Primary CDB

```
DGMGRL> MIGRATE PLUGGABLE DATABASE REGION1 TO CONTAINER NORTH_SALES_NEW USING REGION1.xml 
CONNECT AS sys/mypassword@NORTH_SALES_NEW;
Connected to "NORTH_SALES_NEW"
Connected.

Beginning migration of pluggable database REGION1.
Source multitenant container database is NORTH_SALES.
Destination multitenant container database is NORTH_SALES_NEW.

Closing pluggable database REGION1 on all instances of multitenant container database NORTH_SALES.
Unplugging pluggable database REGION1 from multitenant container database NORTH_SALES.
Pluggable database description will be written to REGION1.xml.
Dropping pluggable database REGION1 from multitenant container database NORTH_SALES.
Creating pluggable database REGION1 on multitenant container database NORTH_SALES_NEW.
Opening pluggable database REGION1 on all instances of multitenant container database NORTH_SALES_NEW.
Succeeded.
```

Example 2: Failing over a PDB from a Physical Standby

```
DGMGRL> MIGRATE PLUGGABLE DATABASE REGION1 TO CONTAINER SOUTH_SALES_NEW 
USING REGION1.xml CONNECT AS sys/mypassword@SOUTH_SALES_NEW;
Connected to "SOUTH_SALES_NEW"
Connected.

Beginning migration of pluggable database REGION1.
Source multitenant container database is SOUTH_SALES.
Destination multitenant container database is SOUTH_SALES_NEW.

Continuing with migration of pluggable database REGION1 to multitenant container database SOUTH_SALES_NEW.
Stopping Redo Apply services on source multitenant container database SOUTH_SALES.
Succeeded.
Opening database SOUTH_SALES.
Opening pluggable database REGION1 on source multitenant container database SOUTH_SALES to prepare for migration.
Pluggable database description will be written to REGION1.xml.
Closing pluggable database REGION1 on all instances of multitenant container database SOUTH_SALES.
Disabling media recovery for pluggable database REGION1.
Closing database SOUTH_SALES.
Restarting redo apply services on source multitenant container database SOUTH_SALES.
Succeeded.
Creating pluggable database REGION1 on multitenant container database SOUTH_SALES_NEW.
Opening pluggable database REGION1 on all instances of multitenant container database SOUTH_SALES_NEW.
Unplugging pluggable database REGION1 from multitenant container database NORTH_SALES.
Dropping pluggable database REGION1 from multitenant container database NORTH_SALES.
Succeeded.
```

### 7.44 QUIT

The `QUIT` command quits (exits) the Data Guard command-line interface.

Format

QUIT;

Command Parameters

None.

Usage Notes

- This command has the same effect as the EXIT command.
- A database connection is not required to execute this command. However, if you are connected, this command breaks the connection.

Command Example

The following example shows how to quit (exit) the command-line interface.

```
DGMGRL> QUIT;
```

### 7.45 REINSTATE DATABASE

The `REINSTATE DATABASE` command reinstates a database as a new standby database in the broker configuration for the current primary database.

Format

REINSTATE DATABASE database-name;

Command Parameters

database-name

The name of the database that is to be reinstated in the broker configuration.

Usage Notes

- If the conditions for reinstatement described in [Reinstating the Former Primary Database in the Broker Configuration](using-data-guard-broker-to-manage-switchovers-failovers.md) are not satisfied, the reinstatement will fail with an appropriate error status and the specified database will remain disabled.
- If the `database-name` specified is that of the old primary and fast-start failover is enabled, the old primary database will be reinstated as a standby to the new primary, and the fast-start failover environment will be updated to reflect the availability of the new standby database. It will accept redo data from the new primary database and be the target of a fast-start failover should the new primary database fail. Reinstatement occurs automatically if the observer is running unless the `FastStartFailoverAutoReinstate ` configuration property is set to `FALSE`.
- This command does not require that fast-start failover be enabled. It can be used to reinstate an old primary database after a complete manual failover has been performed. It can also be used to reinstate a bystander standby database that had been disabled after either a complete or immediate failover.
- Issue this command while connected to any database in the broker configuration, except the database that is to be reinstated.

Command Example

The following example reinstates the `North_Sales` database as a standby database in the broker configuration.

```
DGMGRL> REINSTATE DATABASE 'North_Sales';
Reinstating database "North_Sales", please wait...
Reinstatement of database "North_Sales" succeeded
```

### 7.46 REMOVE CONFIGURATION

The `REMOVE CONFIGURATION` command removes the Oracle Data Guard broker configuration and ends broker management of all members in the configuration.

Format

REMOVE CONFIGURATION \[ PRESERVE DESTINATIONS \];

Command Parameters

None.

Usage Notes

- When you remove a broker configuration, management of all of the members associated with that configuration is disabled.
- By default, the command removes the corresponding broker settings of the `LOG_ARCHIVE_DEST_` `n` initialization parameter on the primary database and the `LOG_ARCHIVE_CONFIG` initialization parameters on all members of the configuration. To preserve these settings, use the `PRESERVE DESTINATIONS` option.
- This command does not remove or affect the actual primary or standby database instances, databases, far sync instances, data files, control files, initialization parameter files, server parameter files, or log files of the underlying Oracle Data Guard configuration.
- You cannot remove the configuration when fast-start failover is enabled.

Command Examples

The following examples show a successful and an unsuccessful `REMOVE CONFIGURATION` command.

Example 1

The following command shows how to remove configuration information from the configuration file.

```
DGMGRL> REMOVE CONFIGURATION;
Removed configuration
DGMGRL> SHOW CONFIGURATION;
Error: ORA-16532: Data Guard broker configuration does not exist
 
Configuration details cannot be determined by DGMGRL
```

Example 2

The following command is unsuccessful because fast-start failover is enabled.

```
DGMGRL> REMOVE CONFIGURATION;
Error: ORA-16654: fast-start failover is enabled
 
Failed.
 
DGMGRL> SHOW CONFIGURATION;
 
Configuration - DRSolution
 
  Protection Mode: MaxAvailability
  Members:
    North_Sales  - Primary database
      South_Sales  - (*) Physical standby database
 
Fast-Start Failover: ENABLED
 
Configuration status:
SUCCESS
```

### 7.47 REMOVE DATABASE

The `REMOVE DATABASE` command removes the specified standby database from the broker configuration and terminates broker management of that standby database.

Format

REMOVE DATABASE database-name \[ PRESERVE DESTINATIONS \];

Command Parameters

database-name

The name of the standby database that you want to remove from the broker configuration.

Usage Notes

- An error is returned if you specify the name of the primary database in the broker configuration.
- By default, this command removes all references to the specified database from all redo transport initialization parameters at each member of the configuration. To preserve these settings, use the `PRESERVE DESTINATIONS` option.
- This command cannot be executed if fast-start failover is enabled and database-name specifies the name of the target standby database.

Command Example

The following example shows how to remove a database from the Oracle Data Guard broker configuration.

```
DGMGRL> SHOW CONFIGURATION;
 
Configuration - DRSolution
 
  Protection Mode: MaxPerformance
  Members:
    North_Sales  - Primary database
      South_Sales  - Physical standby database
 
Fast-Start Failover: DISABLED
 
Configuration status:
SUCCESS
 
DGMGRL> REMOVE DATABASE 'South_Sales';
Removed database "South_Sales" from the configuration.
 
 
Configuration - DRSolution
 
  Protection Mode: MaxPerformance
  Members:
    North_Sales  - Primary database
 
Fast-Start Failover: DISABLED
 
Configuration status:
SUCCESS
```

### 7.48 REMOVE FAR\_SYNC

The `REMOVE FAR SYNC` command removes a far sync instance from an Oracle Data Guard broker configuration.

Format

REMOVE FAR\_SYNC far\_sync\_instance\_name;

Command Parameters

far\_sync\_instance\_name

The name of the far sync instance to be removed from the broker configuration. It must match (case-insensitive) the value of the corresponding database `DB_UNIQUE_NAME` initialization parameter.

Usage Notes

- A far sync instance that has its `RedoRoutes` property set cannot be removed.

Command Example

The following example removes a far sync instance named `dallas` from the broker configuration.

```
DGMGRL> REMOVE FAR_SYNC 'dallas';
```

### 7.49 REMOVE INSTANCE

The `REMOVE INSTANCE` command removes the specified instance from the broker configuration.

Format

REMOVE INSTANCE instance-name \[ON { DATABASE | FAR\_SYNC } object-name\];

Command Parameters

instance-name

The name of the instance (SID) that you want to remove from the broker configuration.

object-name

The name of the database or the far sync with which the `instance-name` is associated.

Usage Notes

- The broker automatically adds started instances to the broker configuration. However, the broker does not automatically remove instances from the database. The `REMOVE` `INSTANCE` command can be used to manually remove any instance that no longer exists from the configuration.
- If the `instance-name` is not unique within the configuration, then you must specify both the database-name or far sync-name, and the instance-name to fully identify the instance.
- This command is rejected for an instance that is currently active in the broker configuration.
- This command is rejected if this is the only instance currently associated with a database or far sync.

Command Example

The following example shows how to remove an instance of the database.

```
DGMGRL> REMOVE INSTANCE 'south_sales3' ON DATABASE 'South_Sales';
Removed instance "south_sales3" from the database "South_Sales"
```

### 7.50 REMOVE RECOVERY\_APPLIANCE

The `REMOVE RECOVERY_APPLIANCE` command removes the specified Zero Data Loss Recovery Appliance (Recovery Appliance) from the broker configuration and terminates broker management of the Recovery Appliance.

Caution:

When you use the `REMOVE RECOVERY_APPLIANCE` command, the Recovery Appliance profile information is deleted from the broker configuration file and cannot be recovered.

Format

REMOVE RECOVERY\_APPLIANCE object-name \[ PRESERVE DESTINATIONS \];

Command Parameters

object name

The name of the Recovery Appliance whose profile you want to remove from the broker configuration.

Usage Notes

- By default, this command removes the corresponding broker settings of the `LOG_ARCHIVE_DEST_n` initialization parameter on the database that was shipping redo data to the Recovery Appliance and the `LOG_ARCHIVE_CONFIG` initialization parameter on all databases in the configuration. To preserve these settings, use the `PRESERVE DESTINATIONS` option.

Command Example

The following example shows how to remove a Recovery Appliance from a Data Guard broker configuration.

```
DGMGRL> SHOW CONFIGURATION;
 Configuration - DRSolution
   Protection Mode: MaxPerformance
  Members:
    North_Sales   - Primary database
    South_Sales   - Physical standby database
    EnterpriseRecoveryAppliance - Oracle Backup Appliance

Fast-Start Failover: DISABLED
 Configuration status:
SUCCESS

DGMGRL> REMOVE RECOVERY_APPLIANCE 'EnterpriseRecoveryAppliance';
Removed Oracle Backup Appliance "EnterpriseRecoveryAppliance" from the configuration.

DGMGRL> SHOW CONFIGURATION;
 Configuration - DRSolution
   Protection Mode: MaxPerformance
  Members:
    North_Sales  - Primary database
    South_Sales  - Physical standby database

Fast-Start Failover: DISABLED
 Configuration status:
SUCCESS
```

### 7.51 SET MASTEROBSERVER TO

The `SET MASTEROBSERVER TO` command lets you manually change which observer is recognized as the master observer.

Use the `SET MASTEROBSERVER TO` command to manually designate which observer is to be used as the master.

Format

SET MASTEROBSERVER TO observer\_name

Command Parameters

observer\_name

The name of the observer that you want to be the master observer.

Usage Notes

- If the specified observer name does not exist, an error message is returned and the master observer is not changed
- When this command is issued, the actual switch does not happen until the next time the primary contacts the target standby, usually within three seconds if fast-start failover is enabled. You should use the ` SHOW OBSERVER` command to verify that the switch took place.
- For the manual setting to succeed, the following conditions must be met during the next fast-start failover ping:
	- The target standby is enabled and does not require reinstatement.
		- There is no role change, reinstating, or fast-start failover target switch in progress

Command Example

The following is an example of designating a new observer to be the master.

```
DGMGRL> SET MASTEROBSERVER TO boston-obsever;
Succeeded.
```

### 7.52 SET MASTEROBSERVERHOSTS

The `SET MASTEROBSERVERHOSTS` command sets the master observer of a broker configuration to the observer on the target host.

For each broker configuration in a specified group, if it has a backup observer running on the target host, then set the master observer of this broker configuration to the observer on the target host.

Format

SET MASTEROBSERVERHOSTS {FOR cfg\_group\_name } TO host-name;

Command Parameters

cfg\_group\_name

The name of a broker configuration group, on which you want to move the master observer to the target host.

host-name

The target host to which you want to move the master observer for the broker configurations in the specified group.

Usage Notes

- If no cfg\_group\_name is specified, then this command attempts to switch the master observer to the specified host for all broker configurations defined in the observer configuration file.
- The cfg\_group\_name cannot be the keyword `ALL`.
- The actual switch does not happen until the next time the primary contacts the target standby in each broker configuration, usually within three seconds if fast-start failover is enabled. You should use the `SHOW OBSERVERS` command to verify that the switch took place.

Command Example

```
DGMGRL > SET MASTEROBSERVERHOSTS FOR GRP_A TO dgnet0;
```

### 7.53 SET ObserverConfigFile

The `SET ObserverConfigFile` command sets the full path and file name of an observer configuration file.

An observer configuration file stores information about managed configurations. The commands `START OBSERVING`, `STOP OBSERVING`, and `SHOW OBSERVERS` read the information about broker configuration groups from the file specified on this command.

Format

SET ObserverConfigFile = filename

Command Parameters

filename

The full path of an observer configuration file.

Usage Notes

- `ObserverConfigFile` is a DGMGRL runtime property. It neither resides in broker configuration metadata nor is persisted to disk. If the observer configuration file name is not observer.ora or it does not exist in the current working directory, then you must specify the name every time you start a new DGMGRL client.
- The default value of the property `ObserverConfigFile` is `observer.ora`, and its default location is in the working directory.
- When you issue this command, the name of the configuration file is changed even if the file you specify does not exist or the content of the file is invalid.

Command Example

```
DGMGRL> SET ObserverConfigFile = /usr/oracle/observer.ora
```

### 7.54 SET TIME

The DGMGRL ` SET TIME` command turns timestamp printing on and off.

The timestamp printing feature records the timestamp as you input each command at the DGMGRL prompt. This information can be helpful with analysis of DGMGRL console input and output.

Format

SET TIME \[ON | OFF\];

Usage Notes

- None

Command Example

```
DGMGRL> SET TIME ON;
07/11/2016 09:28:21 DGMGRL> SHOW CONFIGURATION;

Configuration - DRSolution

  Protection Mode: MaxPerformance
  Members:
  North_Sales  - Primary database
    South_Sales - Physical standby database 

Fast-Start Failover: DISABLED

Configuration Status:
SUCCESS

07/11/2016 09:28:24 DGMGRL> SET TIME OFF;
DGMGRL>
```

### 7.55 SHOW CONFIGURATION

The `SHOW CONFIGURATION` command displays a summary and status of the broker configuration.

The summary lists all members included in the broker configuration and other information pertaining to the broker configuration itself, including the fast-start failover status.

Format

SHOW CONFIGURATION \[VERBOSE | property-name\];

Command Parameters

property-name

The name of the property for which you want to display summary information.

See [Oracle Data Guard Broker Properties](oracle-data-guard-broker-properties.md) for complete information about properties.

Usage Notes

- Use the `SHOW CONFIGURATION VERBOSE` command (or the `SHOW FAST_START FAILOVER` command) to show the properties related to fast-start failover.
- You can optionally specify either `VERBOSE` or `property-name`, but not both.
- The `SHOW` `CONFIGURATION` command displays the status of the configuration and its members as of the last time the health was evaluated. (The health of the configuration and its members is evaluated once a minute.)
	Specifying the `VERBOSE` keyword forces an immediate health evaluation of the configuration and its members before the health information is displayed.
- During a rolling upgrade done using the PL/SQL package `DBMS_ROLLING`, the `SHOW CONFIGURATION` command shows `Transient logical standby database` as the role of the upgrade target, and `ROLLING DATABASE MAINTENANCE IN PROGRESS` as the configuration status. See Example 3.
- The display highlights the current fast-start failover target with an asterisk (\*) when fast-start failover is enabled

Command Examples

Example 1: Showing a Summary of the DRSolution Configuration

The following example provides a summary of the `DRSolution` configuration for which fast-start failover is disabled. The output shows a far sync instance named `FS` in the broker configuration. The `North_Sales` database is shipping to `FS`, and `FS` is shipping to `South_Sales`.

```
DGMGRL> SHOW CONFIGURATION;
 
Configuration - DRSolution
 
  Protection Mode: MaxAvailability
  Members:
  North_Sales  - Primary database
    FS- Far sync instance
      South_Sales- Physical standby database
 
Fast-Start Failover: DISABLED
 
Configuration Status:
SUCCESS   (status updated 20 seconds ago)
```

Example 2: Showing Detailed Description of the DRSolution Configuration

The following example provides detailed information about the DRSolution configuration, including configuration properties, and fast-start failover-related information:

```
DGMGRL> SHOW CONFIGURATION VERBOSE;

Configuration - DRSolution

  Protection Mode: MaxAvailability
  Members:

  North_Sales  - Primary database
    FS- Far sync instance
      South_Sales- (*) Physical standby database

  (*) Fast-Start Failover target

  Properties:
    FastStartFailoverThreshold      = '30'
    OperationTimeout                = '30'
    TraceLevel                      = 'USER'
    FastStartFailoverLagLimit       = '30'
    CommunicationTimeout            = '180'
    ObserverReconnect               = '0'
    FastStartFailoverAutoReinstate  = 'TRUE'
    FastStartFailoverPmyShutdown    = 'TRUE'
    BystandersFollowRoleChange      = 'ALL'
    ObserverOverride                = 'FALSE'
    ExternalDestination1            = ''
    ExternalDestination2            = ''
    PrimaryLostWriteAction          = 'CONTINUE'
    ConfigurationWideServiceName = 'North_Sales_CFG'

Fast-Start Failover: ENABLED

  Threshold:          30 seconds
  Target:             South_Sales
  Observer:           observer.example.com
  Lag Limit:          30 seconds (not in use)
  Shutdown Primary:   TRUE
  Auto-reinstate:     TRUE
  Observer Reconnect: (none)
  Observer Override:  FALSE

Configuration Status:
WARNING
```

Example 3: Sample Output During a Rolling Upgrade Performed with the DBMS\_ROLLING Package

```
Configuration - DRSolution

  Protection Mode: MaxPerformance
  Members:

  North_Sales  - Primary database
    South_Sales - Transient logical standby database

Fast-Start Failover: DISABLED

Configuration Status:
    ROLLING DATABASE MAINTENANCE IN PROGRESS
```

### 7.56 SHOW CONFIGURATION WHEN PRIMARY IS

The `SHOW CONFIGURATION WHEN PRIMARY IS` command displays the redo transport configuration that would be in effect if the specified database were the primary database.

The display lists all members, but unlike `SHOW` `CONFIGURATION`, it does not provide status or any other configuration information.

Format

SHOW CONFIGURATION WHEN PRIMARY IS database-name;

Command Parameters

database-name

The name of the database for which you want to see what the redo transport configuration would be if it were the primary database.

Usage Notes

- Use the `SHOW` `CONFIGURATION` `WHEN` `PRIMARY` `IS` command to show the redo transport configuration that would be in effect if the specified database were the primary database. You can use this information to identify ahead of time any redo transport configurations that would be incorrect after a role change.

Command Example

The following example provides a summary of the `DRSolution` configuration before and after a role change to the `South_Sales` database.

```
DGMGRL> SHOW CONFIGURATION;
 
Configuration - DRSolution
 
  Protection Mode: MaxAvailability
  Members:
  North_Sales - Primary database
    North_FS    - Far Sync 
      South_Sales - Physical standby database 
 
  Members Not Receiving Redo:
  South_FS - Far Sync 
 
Fast-Start Failover: DISABLED
 
Configuration Status:
SUCCESS
 
DGMGRL> SHOW CONFIGURATION WHEN PRIMARY IS 'South_Sales';
 
Configuration when South_Sales is primary - DRSolution
 
  Members:
  South_Sales  - Primary database
    South_FS     - Far Sync 
      North_Sales  - Physical standby database 
 
  Members Not Receiving Redo:
  North_FS - Far Sync
```

These displays are based upon the `RedoRoutes` property being set as follows for each member:

```
DGMGRL> SHOW DATABASE 'North_Sales' RedoRoutes;
  RedoRoutes = '(LOCAL : North_FS)'
 
DGMGRL> SHOW FAR_SYNC 'North_FS' RedoRoutes;
  RedoRoutes = '(North_Sales : South_Sales)'
 
DGMGRL> SHOW DATABASE 'South_Sales' RedoRoutes;
  RedoRoutes = '(LOCAL : South_FS)'
 
DGMGRL> SHOW FAR_SYNC 'South_FS' RedoRoutes;
  RedoRoutes = '(South_Sales : North_Sales)'
```

### 7.57 SHOW DATABASE

The `SHOW DATABASE` command displays information or property values of the specified database and its instances.

Format

SHOW DATABASE \[VERBOSE\] database-name \[property-name\];

Command Parameters

database-name

The name of the database for which you want to display information. The `VERBOSE` keyword, if used, must come before the `database-name` or an error is returned.

property-name

The name of the property for which you want to display a value. If a property name is specified, the output shows only the specified property (not all properties of the database), regardless of whether or not the `VERBOSE` keyword is specified.

See Also:

[Managing the Members of a Broker Configuration](managing-oracle-data-guard-broker-configuration-members.md) and [Oracle Data Guard Broker Properties](oracle-data-guard-broker-properties.md) for information about properties.

Usage Notes

- The `SHOW DATABASE` command shows a brief summary of the database. The `SHOW DATABASE VERBOSE` command shows properties of the database in addition to the brief summary. They both show the status of the database.
- The `SHOW DATABASE VERBOSE` command shows the locations of the Oracle alert log file and of the broker log file. The broker log file is created in the same directory as the alert log and is named `drc<$ORACLE_SID>.log`.
- The `SHOW DATABASE VERBOSE` command shows database-specific properties and instance-specific properties. For a non-Oracle RAC database, the values of the instance-specific properties are those of the only instance of the database. For an Oracle RAC database, the values of the instance-specific properties will not be shown, although the property names are still listed. To see the instance-specific values of these properties, use the `SHOW INSTANCE` command.
- The properties that the `SHOW DATABASE VERBOSE` command shows depend on the database role and the configuration composition:
	- For the primary database, properties specific to physical or snapshot standby databases are shown only if there is at least one physical or snapshot standby database in the configuration. The properties specific to logical standby databases are shown only if there is at least one logical standby database in the configuration.
		- For physical and snapshot standby databases, properties specific to logical standby databases are not shown.
		- For logical standby databases, properties specific to physical and snapshot standby databases are not shown.
- This command is rejected if you use the `SHOW DATABASE ` `database-name property-name` command to show an instance-specific property in an Oracle RAC database.
- During a rolling upgrade done using the PL/SQL package ` DBMS_ROLLING`, the `SHOW DATABASE` command shows a `WARNING` with an appropriate `ORA` error for the upgrade target and the trailing or leading standbys, depending on the current rolling upgrade progress. See Example 3.

Command Examples

Example 1: Showing Database Information in Abbreviated Format

This example shows database information in an abbreviated format.

```
DGMGRL> SHOW DATABASE South_Sales;
 
Database - South_Sales
   
  Role:            PHYSICAL STANDBY
  Intended State:  APPLY-ON
  Transport Lag:   (unknown)
  Apply Lag:       0 seconds (computed 0 seconds ago)
  Apply Rate:      1.73 MByte/s
  Real Time Query: OFF
  Instance(s):
    south_sales1
 
Database Status:
SUCCESS
```

Example 2: Showing Database Information in Extended Format

This example shows database information in an extended format.

```
DGMGRL> SHOW DATABASE VERBOSE 'North_Sales';

Database - North_Sales

  Role:               PRIMARY
  Intended State:     TRANSPORT-ON
  Instance(s):
    c0

  Properties:
    DGConnectIdentifier             = 'North_Sales.example.com'
    ObserverConnectIdentifier       = ''
    LogXptMode                      = 'ASYNC'
    RedoRoutes                      = ''
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
    ApplyLagThreshold               = '0'
    TransportLagThreshold           = '0'
    TransportDisconnectedThreshold  = '0'
    ApplyParallel                   = 'AUTO'
    ApplyInstances                  = '0'
    StandbyFileManagement           = 'AUTO'
    ArchiveLagTarget                = '0'
    LogArchiveMaxProcesses          = '5'
    LogArchiveMinSucceedDest        = '1'
    DataGuardSyncLatency            = '0'
    DbFileNameConvert               = 'dbs/cdb2_, dbs/cdb1_, dbs/bt, dbs/t, dbs/cdb4_, dbs/cdb1_, dbs/dt, dbs/t'
    LogFileNameConvert              = 'dbs/cdb2_, dbs/cdb1_, dbs/bt, dbs/t, dbs/cdb4_, dbs/cdb1_, dbs/dt, dbs/t'
    FastStartFailoverTarget         = ''
    InconsistentProperties          = '(monitor)'
    InconsistentLogXptProps         = '(monitor)'
    SendQEntries                    = '(monitor)'
    LogXptStatus                    = '(monitor)'
    RecvQEntries                    = '(monitor)'
    PreferredObserverHosts          = ''
    StaticConnectIdentifier         = '(DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)
(HOST=North_Sales.example.com)(PORT=2840))
(CONNECT_DATA=(SERVICE_NAME=North_Sales_DGMGRL.example.com)
(INSTANCE_NAME=north_sales1)(SERVER=DEDICATED)))'
    StandbyArchiveLocation          = 'USE_DB_RECOVERY_FILE_DEST'
    AlternateLocation               = ''
    LogArchiveTrace                 = 255
    LogArchiveFormat                = 'db1r_%d_%t_%s_%R.arc'
    TopWaitEvents                   = '(monitor)'

  Log file locations:
    Alert log               : /dev/oracle/log/diag/rdbms/North_Sales/north1/trace/alert_north1.log
    Data Guard Broker log   : /dev/oracle/log/diag/rdbms/North_Sales/north1/trace/drcnorth1.log

Database Status:
SUCCESS
```

Example 3: Sample Output for the Target Database During a Rolling Upgrade Performed With the DBMS\_ROLLING Package

```
DGMGRL> SHOW DATABASE South_Sales;

Database - South_Sales

  Role:               Physical standby database
  Intended State:     APPLY-ON
  Transport Lag:      ***
  Apply Lag:          ***
  Average Apply Rate: ***
  Real Time Query:    OFF
  Instance(s):
    South

  Database Warning(s):
    ORA-16866: database converted to transient logical standby database for rolling database maintenance

Database Status:
WARNING
```

Example 4: Sample Output For the Leading Standby During a Rolling Upgrade Performed With the DBMS\_ROLLING Package

```
DGMGRL> SHOW DATABASE South_Sales;

Database - South_Sales

  Role: Physical standby database
  Intended State: APPLY-ON
  Transport Lag: 0 seconds (computed 0 seconds ago)
  Apply Lag: 0 seconds (computed 0 seconds ago)
  Average Apply Rate: 510.00 KByte/s
  Real Time Query: OFF
  Instance(s):
    South

  Database Warning(s):
    ORA-16881: standby database is not protecting the current primary database during rolling database maintenance

Database Status:
WARNING
```

### 7.58 SHOW FAR\_SYNC

The `SHOW FAR_SYNC` command shows information about a far sync instance.

Format

SHOW FAR\_SYNC \[VERBOSE\] far\_sync\_instance\_name \[property-name\];

Command Parameters

far\_sync\_instance\_name

The name of the far sync instance for which the broker will show information. It must match (case-insensitive) the value of the corresponding database `DB_UNIQUE_NAME` initialization parameter.

property-name

The name of the property for which you want to display a value. If a property name is specified, the output shows only the specified property (not all properties of the far sync), regardless of whether or not the `VERBOSE` keyword is specified.

See Also:

[Managing the Members of a Broker Configuration](managing-oracle-data-guard-broker-configuration-members.md) and [Oracle Data Guard Broker Properties](oracle-data-guard-broker-properties.md) for information about properties.

Command Examples

Example 1: Sample SHOW FAR\_SYNC Output Without VERBOSE

The following example shows sample output from this command:

```
DGMGRL> SHOW FAR_SYNC FS;
 
Far Sync - FS
 
Transport Lag: 0 seconds (computed 1 second ago)
Instance(s):
  fs1
 
Far Sync Status:
SUCCESS
```

Example 2: Sample SHOW FAR SYNC Output With VERBOSE

The following example shows sample output from this command when the `VERBOSE` option is used:

```
DGMGRL> SHOW FAR_SYNC VERBOSE FS;
 
Far Sync - FS
 
Transport Lag: 0 seconds (computed 0 seconds ago)
Instance(s):
  b02
 
Properties:
  DGConnectIdentifier            = 'fs.example.com'
  LogXptMode                     = 'sync'
  RedoRoutes                     = '(North_Sales : South_Sales)
(South_Sales : North_Sales)'
  Binding                        = 'optional'
  MaxFailure                     = '0'
  MaxConnections                 = '1'
  ReopenSecs                     = '300'
  NetTimeout                     = '30'
  RedoCompression                = 'DISABLE'
  LogShipping                    = 'ON'
  TransportLagThreshold          = '0'
  TransportDisconnectedThreshold = '0'
  ArchiveLagTarget               = '0'
  LogArchiveMaxProcesses         = '5'
  LogArchiveMinSucceedDest       = '1'
  InconsistentProperties         = '(monitor)'
  InconsistentLogXptProps        = '(monitor)'
  LogXptStatus                   = '(monitor)'
  StaticConnectIdentifier        = '(DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)
  (HOST=fs.example.com)(PORT=2202))
  (CONNECT_DATA=(SERVICE_NAME=FS_DGMGRL.example.com)
  (INSTANCE_NAME=fs1)(SERVER=DEDICATED)))'
  StandbyArchiveLocation         = 'USE_DB_RECOVERY_FILE_DEST'
  AlternateLocation              = ''
  LogArchiveTrace                = '255'
  LogArchiveFormat               = 'db2r_%d_%t_%s_%R.arc'
  TopWaitEvents                  = '(monitor)'
 
Far Sync Status:
SUCCESS
```

### 7.59 SHOW FAST\_START FAILOVER

The `SHOW FAST_START FAILOVER` command displays all fast-start failover related information.

If there is more than one registered observer running, then the output of this command shows all registered observers and indicates, with an asterisk, which one is the master observer. To see information in addition to host names of observers, use the `SHOW OBSERVER` command.

Format

SHOW FAST\_START FAILOVER;

Command Parameters

None.

Usage Notes

- The `SHOW FAST_START FAILOVER` command shows a summary of the fast-start failover configuration.
- The display shows the current fast-start failover target as well as candidate fast-start failover targets. If the `FastStartFailoverTarget` property of the primary database is set to `ANY`, then the candidate targets would include the standby databases that are properly configured for the prevailing protection mode.

Command Examples

Example 1: This example shows the output when there is only one registered observer running and there are multiple candidate targets.

```
DGMGRL> SHOW FAST_START FAILOVER;
Fast-Start Failover: ENABLED

  Threshold:           30 seconds
  Target:              South_Sales
  Candidate Targets:   East_Sales, West_Sales
  Observer:            observer.example.com
  Lag Limit:           30 seconds (not in use)
  Shutdown Primary:    TRUE
  Auto-reinstate:      TRUE
  Observer Reconnect:  (none)
  Observer Override:   FALSE
  
Configurable Failover Conditions
  Health Conditions:
    Corrupted Controlfile          YES
    Corrupted Dictionary           YES
    Inaccessible Logfile            NO
    Stuck Archiver                  NO
    Datafile Write Errors          YES

  Oracle Error Conditions:
    (none)
```

Example 2: This example shows the output when there are multiple registered observers running. The asterisk symbol (\*) indicates which observer is the master.

```
DGMGRL> SHOW FAST_START FAILOVER
Fast-Start Failover: ENABLED

  Threshold:           30 seconds
  Target:              South_Sales
  Observers:        (*)observer1.example.com
                       observer2.example.com
                       observer3.example.com
  Lag Limit:           30 seconds (not in use)
  Shutdown Primary:    TRUE
  Auto-reinstate:      TRUE
  Observer Reconnect:  (none)
  Observer Override:   FALSE
  
Configurable Failover Conditions
  Health Conditions:
    Corrupted Controlfile          YES
    Corrupted Dictionary           YES
    Inaccessible Logfile            NO
    Stuck Archiver                  NO
    Datafile Write Errors          YES

  Oracle Error Conditions:
    (none)
```

### 7.60 SHOW INSTANCE

The `SHOW INSTANCE` command displays information or property values for the specified instance.

Format

SHOW INSTANCE \[VERBOSE\] instance-name \[property-name\] \[ON {DATABASE database-name | FAR\_SYNC far-sync-name } \];

Command Parameters

instance-name

The name of the instance for which you want to display information. The `VERBOSE` keyword, if used, must come before the instance name.

property-name

The name of the property for which you want to display a value. If a property name is specified, the output shows only the specified property (not all properties), regardless of whether or not the `VERBOSE` keyword is specified.

See Also:

[Managing the Members of a Broker Configuration](managing-oracle-data-guard-broker-configuration-members.md) and [Oracle Data Guard Broker Properties](oracle-data-guard-broker-properties.md) for information about properties.

database-name | far-sync-name

The name of the database or far sync associated with the instance for which you want to show information.

Usage Notes

- The `SHOW INSTANCE` command shows a brief summary of the instance. The `SHOW INSTANCE VERBOSE` command shows properties of the instance in addition to the brief summary. They both show the status of the instance.
- The `SHOW INSTANCE VERBOSE` command shows the locations of the Oracle alert log file and of the broker log file. The broker log file is created in the same directory as the alert log and is named `drc<$ORACLE_SID>.log`.
- The `SHOW INSTANCE VERBOSE` command only shows instance-specific properties.
- The properties that the `SHOW INSTANCE VERBOSE` command shows depend on the database role and the configuration composition:
	- For instances of the primary database, properties specific to physical or snapshot standby instances are shown only if there is at least one physical or snapshot standby database in the configuration. The properties specific to logical standby instances are shown only if there is at least one logical standby database in the configuration.
		- For instances of physical or snapshot standby databases, properties specific to logical standby instances are not shown.
		- For instances of logical standby databases, properties specific to physical and snapshot standby instances are not shown.
- The `instance-name` can be unique across the configuration. If `instance-name` is not unique, you must specify both the `database-name` and the `instance-name` to fully identify the instance.

Command Examples

Example 1: Showing Instance Information in Abbreviated Format

The following example shows information about a specific instance of a database.

```
DGMGRL> SHOW INSTANCE 'north_sales1';
 
Instance 'north_sales1' of database 'North_Sales'
 
Instance Status:
SUCCESS
```

Example 2: Showing Instance Information in Extended Format

The following example shows instance information in an extended format.

```
DGMGRL> SHOW INSTANCE VERBOSE 'north_sales1';
 
Instance 'north_sales1' of database 'North_Sales'
 
  Host Name: north.example.com
  PFILE:
  Properties:
    SidName                         = 'north_sales1'
    StaticConnectIdentifier         = '(DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)
(HOST=north.example.com)(PORT=2094))
(CONNECT_DATA=(SERVICE_NAME=North_Sales_DGMGRL.example.com)
(INSTANCE_NAME=north_sales1)(SERVER=DEDICATED)))'
    StandbyArchiveLocation          = 'USE_DB_RECOVERY_FILE_DEST'
    AlternateLocation               = ''
    LogArchiveTrace                 = '255'
    LogArchiveFormat                = 'r_%d_%t_%s_%R.arc'
    LatestLog                       = '(monitor)'
    TopWaitEvents                   = '(monitor)'
 
Log file locations:
  Alert log               : /u01/oracle/diag/rdbms/orclbi/orclbi/trace/alert_South_Sales.log
  Data Guard Broker log   : /u01/oracle/diag/rdbms/orclbi/orclbi/trace/drc_South_Sales.log 

Instance Status:
SUCCESS
```

### 7.61 SHOW OBSERVER

The ` SHOW OBSERVER` command shows information about all registered observers in a Data Guard broker configuration.

The `SHOW OBSERVER` command displays the observer name, the host name where the observer is running, whether the observer is the master observer, and the last time the observer pinged the primary and standby. It shows this information for all the observers (up to 3) in this single configuration.

FORMAT

SHOW OBSERVER;

Command Parameters

None

Usage Notes

- This command requires a DGMGRL session, which submits this command, to be connected to a single configuration.

Command Example

The following example `SHOW OBSERVER` command displays information about all registered observers in the `DRSolution` broker configuration.

```
DGMGRL> SHOW OBSERVER;

Configuration - DRSolution

Primary:               North_Sales
Active Target Standby: South_Sales

Observer "ob2" - Master

   Host Name:              observer2.example.com
   Last Ping to Primary:   1 second ago
   Last Ping to Target:    2 seconds ago

Observer "ob1" - Backup

   Host Name:              observer1.example.com
   Last Ping to Primary:   1 second ago
   Last Ping to Target:    3 seconds ago

Observer "ob3" - Backup

   Host Name:              observer3.example.com
   Last Ping to Primary:   4 seconds ago
   Last Ping to Target:    5 seconds ago
```

### 7.62 SHOW ObserverConfigFile

The `SHOW ObserverConfigFile` command shows the value of the `ObserverConfigFile` property.

Format

SHOW ObserverConfigFile;

Command Parameters

None.

Usage Notes

- If the value of the `ObserverConfigFile` property is an empty string, then the output is `current_working_directory/observer.ora`.
- The `SHOW ObserverConfigFile` command attempts to parse the file pointed by the `ObserverConfigFile` property. If the file does not exist or parsing fails, then a message is returned that the file is not usable.

Command Example

```
DGMGRL> SHOW ObserverConfigFile;
ObserverConfigFile=/usr/oracle/observer 
observer configuration file parsing succeeded
```

### 7.63 SHOW OBSERVERS

The ` SHOW OBSERVERS` command shows information about all observers for all broker configurations in a specific configuration group.

The `SHOW OBSERVERS` command displays the observer name, the host name where the observer is running, whether the observer is the master observer, and the last time the observer pinged the primary and standby.

Format

SHOW OBSERVERS \[FOR cfg\_group\_name \];

Command Parameters

cfg\_group\_name

The name of a valid broker configuration group file for which you want to show information about all running observers. Specifying this parameter results in information being shown about observers for all configurations in the specified group. The information shown by this command is the same as that shown by a `SHOW OBSERVER` command on an individual configuration.

If a group name is not specified, then `SHOW OBSERVERS` alone is also a valid command. It shows observer information for all broker configuration groups defined in the observer configuration file.

The configuration group name cannot be `ALL`.

Usage Notes

- This command can be used to verify that a manually performed switch to a new master observer was successful.

Command Example

```
DGMGRL> SHOW OBSERVERS; 
ObserverConfigFile=observer.ora
observer configuration file parsing succeeded
Submit command SHOW OBSERVER using the connect identifier 'North_Sales'.
Connected to "North_Sales"

Configuration - DrSolution1

  Primary:            North_Sales
  Target:             South_Sales

Observer DRSolution1_Observer - Master

  Host Name:                    observer1.example.com
  Last Ping to Primary:         3 seconds ago
  Last Ping to Target:          3 seconds ago

Submit command SHOW OBSERVER using the connect identifier 'East_Sales'.
Connected to "East_Sales"

Configuration - DRSolution2

  Primary:            East_Sales
  Target:             West_Sales

Observer DRSolution2_Observer - Master

  Host Name:                    observer2.example.com
  Last Ping to Primary:         3 seconds ago
  Last Ping to Target:          3 seconds ago
```

### 7.64 SHOW RECOVERY\_APPLIANCE

The `SHOW RECOVERY_APPLIANCE` command displays information or property values of the specified Zero Data Loss Recovery Appliance (Recovery Appliance).

Format

SHOW RECOVERY\_APPLIANCE \[VERBOSE\] object name \[property name\];

Command Parameters

object name

The name of the Recovery Appliance for which you want to display information. The `VERBOSE` keyword, if used, must come before the Recovery Appliance name or an error is returned.

property name

The name of the property for which you want to display a value. If a property name is specified, the output shows only the specified property (not all properties of the Recovery Appliance), regardless of whether or not the `VERBOSE` keyword is specified.

Usage Notes

- The `SHOW RECOVERY_APPLIANCE` command shows a brief summary of the Recovery Appliance. The `SHOW RECOVERY_APPLIANCE VERBOSE` command shows properties of the Recovery Appliance in addition to the brief summary. They both show the status of the database.
- The `SHOW RECOVERY_APPLIANCE VERBOSE` command shows Recovery Appliance-specific properties.

Command Examples

Example 1: Recovery Appliance Information in Abbreviated Format

The following example shows Recovery Appliance information in an abbreviated format.

```
DGMGRL> SHOW RECOVERY_APPLIANCE 'EnterpriseRecoveryAppliance';
 Oracle Recovery Server - EnterpriseRecoveryAppliance
   Transport Lag:   0 seconds
  Redo Source:     South_Sales

Oracle Backup Appliance Status:
SUCCESS
```

Example 2: Recovery Appliance Information in Extended Format

The following example uses the `VERBOSE` parameter to show Recovery Appliance information in an extended format.

```
DGMGRL> SHOW RECOVERY_APPLIANCE VERBOSE 'EnterpriseRecoveryAppliance';
 
Oracle Backup Appliance - EnterpriseRecoveryAppliance
 
  Transport Lag:   0
  Redo Source:     South_Sales
 
  Properties:
    DGConnectIdentifier             = 'South_Sales.example.com'
    LogXptMode                      = 'ASYNC'
    DelayMins                       = '0'
    Binding                         = 'optional'
    MaxFailure                      = '0'
    MaxConnections                  = '1'
    ReopenSecs                      = '300'
    NetTimeout                      = '30'
    RedoCompression                 = 'DISABLE'
    LogShipping                     = 'ON'
    ArchiveLagTarget                = '0'
    LogArchiveMaxProcesses          = '5'
    LogArchiveMinSucceedDest        = '1'
    InconsistentProperties          = '(monitor)'
    InconsistentLogXptProps         = '(monitor)'
    AlternateLocation               = ''
    RedoSource                      = 'South_Sales'
 
Database Status:
SUCCESS
```

### 7.65 SHUTDOWN

Shuts down a currently running Oracle instance.

Format

SHUTDOWN \[ ABORT | IMMEDIATE | NORMAL \];

Command Parameters

None.

Usage Notes

- Using the `SHUTDOWN` command with no arguments is equivalent to using the `SHUTDOWN NORMAL` command.
- The following list describes the options to the `SHUTDOWN` command:
	- `ABORT`
		Proceeds with the fastest possible shutdown of the database without waiting for calls to complete or for users to disconnect from the database. Uncommitted transactions are not rolled back. Client SQL statements being processed are terminated. All users connected to the database are implicitly disconnected, and the next database startup will require instance recovery. You must use this option if a background process terminates abnormally.
		Caution:
		If you use the `ABORT` option on the primary database when fast-start failover is enabled and the observer is running, a fast-start failover may ensue. Use the `IMMEDIATE` or `NORMAL` option to prevent an unexpected fast-start failover from occurring.
		- `IMMEDIATE`
		Does not wait for current calls to complete or users to disconnect from the database. Further connections are prohibited. The database is closed and dismounted. The instance is shut down, and no instance recovery is required on the next database startup.
		- `NORMAL`
		This is the default option. The process waits for users to disconnect from the database. Further connections are prohibited. The database is closed and dismounted. The instance is shut down, and no instance recovery is required on the next database startup.

Command Example

The following command shuts down the primary database in normal mode.

```
DGMGRL> SHUTDOWN;

Database closed. 
Database dismounted. 
Oracle instance shut down.
```

### 7.66 SPOOL

The `SPOOL` command records the input and output of DGMGRL to a file.

Format

The `SPOOL` command has three possible formats:

`SPOOL;`

`SPOOL spool-file-name [CREATE | REPLACE | APPEND];`

`SPOOL OFF;`

If you simply enter `SPOOL` at the DGMGRL command prompt, then the current spool file name is displayed.

Otherwise, the available spooling options are defined as follows:

- `CREATE` —Create a new log file. If a spool file with the specified name already exists, the SPOOL command fails.
- `REPLACE` —Replace the existing spool file of the name specified. This is the default behavior if no option is specified.
- `APPEND` —Append the new log into the specified log file, if it exists. Otherwise create a new one.
- `OFF` —Turns spooling off.

Command Parameters

spool-file-name

The name of the file to which DGMGRL input and output will be written.

Usage Notes

- None

Command Example

The following example shows the output of the `SPOOL` command before and after spooling is started.

```
DGMGRL> SPOOL;
not spooling currently

DGMGRL> SPOOL mysession;

DGMGRL> SPOOL;
currently spooling to "mysession"

DGMGRL>
```

### 7.67 SQL

The SQL command executes a SQL statement or a PL/SQL stored procedure.

Format

SQL " sql\_statmement "

Command Parameters

sql\_statement

The SQL statement or PL/SQL stored procedure to be executed.

Usage Notes

- The SQL statement or PL/SQL stored procedure to be executed must be enclosed in double quotation marks.
- Do not include a semi-colon (;) after the SQL statement to be executed.
- If the string that DGMGRL passes to PL/SQL contains a filename, then the filename must be enclosed in single quotation marks and the entire string following the SQL command must be enclosed in double quotation marks. For example, use the following syntax:
	```
	SQL "CREATE TABLESPACE temp1 DATAFILE '?/oradata/trgt/temp1.dbf' SIZE 10M TEMPORARY"
	```
- You cannot execute `SELECT` statements.

Command Example

The following command opens the database.

```
DGMGRL> SQL "alter database open"
```

### 7.68 START OBSERVER

The `START OBSERVER` command starts a fast-start failover observer on this host (where the DGMGRL session is running), if there is no registered observer running on this host for this configuration.

Before using this command, you must first issue a `CONNECT` command to log into a specific broker configuration. Otherwise, an error message is returned stating that you are not logged on.

Format

START OBSERVER \[observer-name\] \[FILE IS observer-file\] \[LOGFILE IS logfile\] \[TRACE LEVEL IS USER | SUPPORT\];

Command Parameters

observer-name

A name to identify observers within the same Data Guard broker configuration.
- No two observers on the same Data Guard broker configuration can have the same name.
- If no name is specified for the observer then a default observer name, the host name of machine where the START OBSERVER command is issued, is used.
- An observer name is case-insensitive.
- The string "NONAME" cannot be used as an observer name.

observer-file

Specifies the path and name of the runtime data file. If not specified, then the file name defaults to `fsfo.dat` and the path is the current working directory.

log-file

The full path name of the observer log file. Each observer has its own log file.

Usage Notes

- You can register up to three observers to monitor a single Data Guard broker configuration. Each observer is identified by a name that you supply when you issue the `START OBSERVER` command. See [Installing and Starting the Observer](using-data-guard-broker-to-manage-switchovers-failovers.md).
- The optional clause `TRACE_LEVEL IS` lets you control the amount of tracing done and written to the observer log file. The default value is `USER`, which limits the observer log contents to tracing information about fast-start failover, status changes of the primary and target standby database, and error/warning messages. Setting `TRACE_LEVEL` to `SUPPORT` increases the amount of tracing information to include lower-level information needed by Oracle Support Services.
- The Oracle Client Administrator kit, or the full Oracle Database Enterprise Edition or Oracle Personal Edition kit must be installed on the observer computer to monitor a broker configuration for which fast-start failover is to be enabled. See [Prerequisites for Enabling Fast-Start Failover](using-data-guard-broker-to-manage-switchovers-failovers.md) for more information.
- The `START OBSERVER` command must be issued on the observer computer. Once the observer is successfully started, control is not returned to the user until the observer is stopped (for example, by issuing the STOP OBSERVER command from a different client connection). If you want to perform further interaction with the broker configuration, you must connect through another client.
	For information about how to start the observer in the background, see START OBSERVER IN BACKGROUND.
- If the `LOGFILE IS` clause is used, then all observer output is recorded in the specified file. If the specified log file is not accessible, or the `LOGFILE IS` clause is not used, then observer output is sent to standard output. Observer output is useful for troubleshooting problems with the observer and with fast-start failover in general.
- If a directory path is not specified with the `FILE IS` parameter, the observer searches the current working directory for the `fsfo.dat` file. If an `fsfo.dat` file is not found and this is the first time the `START OBSERVER` command is issued, the observer creates a `fsfo.dat` file.
- The primary and target standby database `DB_UNIQUE_NAME` initialization parameter and connect identifiers are stored in the `fsfo.dat` configuration file. Oracle recommends you ensure this file is protected from unauthorized access.
- Fast-start failover does not need to be enabled before you issue this command.
	- If fast-start failover is enabled, the observer will retrieve primary and target standby connect identifiers from the broker configuration and begin monitoring the configuration.
		- If fast-start failover is not enabled, the observer continually monitors for when fast-start failover is enabled.
- Only the primary database needs to be running when you issue this command; the standby database that will be the target of a fast-start failover does not need to be running in order for this command to complete successfully.
- Use the `SHOW OBSERVER` command or the `SHOW CONFIGURATION VERBOSE` command, or query the `V$FS_FAILOVER_OBSERVERS` view on the primary database to see the status of the observer and its host computer.
- If the primary and target standby databases stay connected but they lose the connection to the observer, then the primary database goes into an unobserved state. This state is reported by the broker's health check capability.
- The `SHOW OBSERVER` command indicates whether one or more observers have already been started.
	If the `SHOW OBSERVER` command shows one or more registered observers, but some of them are no longer running for some reason, then you can do either of the following:
	- Issue the `START OBSERVER` command on the same observer computer where it was started originally, with the observer configuration file used when the observer was first started.
		- Issue the `STOP OBSERVER` command and then the `START OBSERVER` command on any computer to start the observer.
	If the `SHOW OBSERVER` command shows one or more observers and one observer is already running at one location, then an attempt to start an observer at that location again will fail with the following error:
	```
	Unable to open the observer file
	```
	If the `SHOW OBSERVER` command shows three registered observers and you attempt to start an observer at a different location, then the command will fail with the following error:
	```
	ORA-16647: could not start more than three observers
	```

Command Examples

Example 1: Starting the Observer

The following example shows how to start the observer.

```
DGMGRL> CONNECT sysdg@North_Sales.example.com;
Password: password
Connected to "North_Sales"
Connected as SYSDG.
DGMGRL> START OBSERVER;
Observer started
```

Example 2: Starting the Observer Without Showing Credentials

The following example shows how to start the observer using `CONNECT '/' ` so that connection credentials are not visible on the command line:

```
DGMGRL> CONNECT /@North_Sales.example.com;
Connected to "North_Sales"
DGMGRL> START OBSERVER;
Observer started.
```

You must set up Oracle Wallet or SSL to use `CONNECT '/'`. By setting up Oracle Wallet or SSL, you can write a script to securely start and run the observer as a background job without specifying database credentials in the script. When using Oracle Wallet as a secure external password store, be sure to add credentials for both the primary and fast-start failover target standby databases. The database connect string that you specify when adding the credentials for each database must match the `ObserverConnectIdentifer` or `DGConnectIdentifier` database property.

### 7.69 START OBSERVER IN BACKGROUND

The `START OBSERVER IN BACKGROUND` command starts a fast-start failover observer on this host (where this DGMGRL session is running) as a background process.

After this command is issued, DGMGRL reports whether the `START OBSERVER IN BACKGROUND` command submitted successfully. If yes, then control returns to the user. (This is different behavior from the `START OBSERVER` command, in which control does not return to the user after the observer is started.)

This command uses Oracle wallet to obtain credentials to log into the database server and register observers. Even if you have successfully connected to a database server in the broker configuration using the `CONNECT` command, this command ignores the existing connection and uses the credentials stored in Oracle wallet. If the wallet is not configured, then the command will fail to start the Observer.

Format

START OBSERVER \[observer-name\] IN BACKGROUND \[FILE IS observer-file\] \[LOGFILE IS log-file\]  
CONNECT IDENTIFIER IS connect-identifier \[TRACE\_LEVEL IS USER | SUPPORT\];

Command Parameters

observer-name

The name to identify observers within the same data guard broker configuration.
- No two observers on the same Data Guard Broker configuration can have the same name.
- If no name is specified for the observer then a default observer name, the host name of machine where the `START OBSERVER` command is issued, is used.
- An observer name is case-insensitive.
- The string "NONAME" cannot be used as an observer name.

observer-file

Specifies the path and name of the runtime data file. If not specified, then the file name defaults to `fsfo.dat` and the path is the current working directory.

log-file

The full path of the observer log file. Each observer has its own log file.

connect-identifier

The connect identifier for a database in the broker configuration that the fast-start failover observer will monitor. Oracle wallet uses this identifier as the key to search oracle wallet.

Usage Notes

- Even if the `START OBSERVER` command is submitted successfully, the observer might fail to start due to credential problems, intermittent network connections, or failure on observer registration. To verify that the observer started successfully, use the `SHOW OBSERVERS` command or check the observer log file.
- This command ignores any connections you have made to a specific configuration member using the `CONNECT` command. In other words, even if you have not connected to a specific member in the broker configuration, you can still start an observer by using the ` START OBSERVER IN BACKGROUND` command.
- If you have connected to a specific configuration member before issuing the `START OBSERVER IN BACKGROUND` command, then you can continue to use the connection after the control is returned.
- If the observer-file parameter is not specified with the `FILE IS` parameter, then the observer searches the current working directory for the ` fsfo.dat` file. If it is not found, then the observer creates a `fsfo.dat` file.
- If the log-file parameter is not specified, then a file named `observer.log` in the current working directory is used as the observer log file. If this file does not exist, it is created.
- The optional clause `TRACE_LEVEL IS` lets you control the amount of tracing done and written to the observer log file. The default value is `USER`, which limits the observer log contents to tracing information about fast-start failover, status changes of the primary and target standby database, and error/warning messages. Setting `TRACE_LEVEL` to `SUPPORT` increases the amount of tracing information to include lower-level information needed by Oracle Support Services.

Command Example

```
DGMGRL> START OBSERVER observer1 IN BACKGROUND 
FILE IS  /net/sales/dat/oracle/broker/fsfo.dat 
LOGFILE IS /net/sales/dat/oracle/broker/observer.log 
CONNECT IDENTIFIER IS sales_p;
Submitted command "START OBSERVER" using connect identifier "sales_p"
```

### 7.70 START OBSERVING

The `START OBSERVING` command starts a new observer for each broker configuration in the specified group.

The effect of the `START OBSERVING` command is equivalent to submitting a `START OBSERVER` command on each individual configuration.

Format

START OBSERVING \[cfg\_group\_name\];

Command Parameters

cfg\_group\_name

The name of a broker configuration group, in which you want to start one observer for each broker configuration.

Usage Notes

- If no `cfg_group_name` is specified, then this command will start a new observer for each configuration defined in the observer configuration file.
- The `cfg_group_name` cannot be the keyword `ALL`.

Command Example

```
DGMGRL> START OBSERVING;
ObserverConfigFile=/net/oracle/dataguard/observer.ora
observer configuration file parsing succeeded
Submitted command “START OBSERVER” using connect identifier "cfg1_cid".  
Submitted command “START OBSERVER”  using connect identifier "cfg2_cid".  
Submitted command “START OBSERVER” using connect identifier "cfg3_cid".  

Check superobserver.log and individual observer logs for execution details.

DGMGRL> START OBSERVING GRP_A;
ObserverConfigFile=/net/oracle/dataguard/observer.ora
observer configuration file parsing succeeded
Submitted command “START OBSERVER” using connect identifier "cfg1_cid".  
Submitted command “START OBSERVER”  using connect identifier "cfg2_cid".  

Check superobserver.log and individual observer logs for execution details.
```

### 7.71 STARTUP

The `STARTUP` command starts an Oracle database instance, and allows you to specify a number of options.

The options you can specify are as follows:

- `FORCE`: shuts down the current Oracle instance in the `SHUTDOWN` `ABORT` mode before restarting it.
- `RESTRICT`: allows only Oracle users with the `RESTRICTED SESSION` system privilege to connect to the instance.
- `PFILE`: specifies the `PFILE` initialization parameter file to be used when the database instance is started.
- `MOUNT`: mounts the specified database without opening it.
- `OPEN`: mounts and opens the specified database.
- `NOMOUNT`: starts the specified database instance without mounting the database.

Format

STARTUP \[FORCE\] \[RESTRICT\] \[PFILE= filename\] \[MOUNT | OPEN \[open\_options\] | NOMOUNT\];

Command Parameters

filename

The name of the initialization parameter file to be used when starting the database instance. If you do not specify the `PFILE` parameter option, then the default server parameter file (specific to your operating system) is used.

open-options

The mode of access in which you want the specified database to start. The possible modes are:

- `READ ONLY`
- `READ WRITE`

Usage Notes

- Using the `STARTUP` command with no arguments is equivalent to using the `STARTUP OPEN` command.
- If you do not use the `FORCE` clause when you use the `STARTUP` command and the current database instance is running, an error results. The `FORCE` clause is useful when you are debugging or when error conditions are occurring. Otherwise, it should not be used.
- Use the `RESTRICT` clause to allow only Oracle users with the `RESTRICTED SESSION` system privilege to connect to the instance. Later, you can use the `ALTER SYSTEM` command through SQL\*Plus to disable the restricted session feature.
- If you do not use the `PFILE` clause to specify the initialization parameter file, the `STARTUP` command uses the default server parameter file, if it exists. Otherwise, the `STARTUP` command uses the default initialization parameter file. The default files are platform specific.
	See your operating system-specific documentation for more information about the default parameter files.
- Use the `OPEN` clause to mount and open the specified database.
- The `NOMOUNT` clause starts the database instance without mounting the database. You cannot use the `NOMOUNT` clause with the `MOUNT` or `OPEN` options.

Command Examples

Example 1: Two Methods for Starting a Database Instance

The following examples show two different methods for starting a database instance. Each command starts a database instance using the standard parameter file, mounts the default database in exclusive mode, and opens the database.

```
DGMGRL> STARTUP;
DGMGRL> STARTUP OPEN;
```

Example 2: Shutting Down the Current Instance and Restarting Without Mounting or Opening It

The following command shuts down the current instance, immediately restarts it without mounting or opening the database, and allows only users with restricted session privileges to connect to it.

```
DGMGRL> STARTUP FORCE RESTRICT NOMOUNT;
```

Example 3: Starting (But Not Mounting) an Instance Using a Parameter File

The following command starts an instance using the parameter file `testparm` without mounting the database.

```
DGMGRL> STARTUP PFILE=testparm NOMOUNT;
```

Example 4: Starting and Mounting an Instance Without Opening It

The following example starts and mounts a database instance, but does not open it.

```
DGMGRL> STARTUP MOUNT;
```

### 7.72 STOP OBSERVER

The `STOP OBSERVER` command stops the fast-start failover observer.

Format

STOP OBSERVER \[observer-name | ALL\];

Command Parameters

observer-name

The name of the observer you want to stop. If a name is not specified and there is only one registered observer for the configuration, then it will be stopped; if there is more than one registered observer in the configuration, then an error message is returned.

The `ALL` keyword stops all observers registered in this broker configuration.

Usage Notes

- You can issue this command while connected to any database in the broker configuration.
- This command does not disable fast-start failover, but a fast-start failover cannot be initiated in the absence of an observer.
- Fast-start failover does not need to be enabled when you issue this command.
- If fast-start failover is enabled when you issue the `STOP OBSERVER` command, then the primary and standby databases must be connected and communicating with each other. Otherwise the following error is returned:
	```
	ORA-16636 fast-start failover target standby in error state, cannot stop observer
	```
	If connectivity does not exist between the primary and standby databases, you can issue the `DISABLE FAST_START FAILOVER FORCE` command on the primary database and then issue the `STOP OBSERVER` command. Note that disabling fast-start failover with the `FORCE` option on a primary database that is disconnected from the observer and the target standby database does not prevent the observer from initiating a fast-start failover to the target standby database.
- If fast-start failover is not enabled when you issue the `STOP OBSERVER` command, then only the primary database must be running when you stop the observer.
- The observer does not stop immediately when the `STOP OBSERVER` command is issued. The observer does not discover it has been stopped until the next time the observer contacts the broker.
	As soon as you have issued the `STOP OBSERVER` command, you may enter the `START OBSERVER` command again on any computer. You can start a new observer right away, even if the old observer has not yet discovered it was stopped. Any attempt to restart the old observer will fail, because a new observer has been started for the broker configuration.
- The `STOP OBSERVER` command fails if a switch to a new fast-start failover target or new master observer is underway.
- The `STOP OBSERVER` command fails if there are two or more registered observers and you attempt to stop only the master.

Command Example

The following example stops all observers running in the broker configuration.

```
DGMGRL> STOP OBSERVER ALL;
```

### 7.73 STOP OBSERVING

The ` STOP OBSERVING` command stops all local observers running on this host (where this DGMGRL session is running) for all broker configurations in a specific group.

Format

STOP OBSERVING \[cfg\_group\_name\] \[TRACE\_LEVEL= USER | SUPPORT\];

Command Parameters

cfg\_group\_name

The name of a broker configuration group, on which you want to stop local observers running on this host (where DGMGRL is running).

TRACE\_LEVEL

The optional clause `TRACE_LEVEL IS` lets you control the amount of tracing done and written to the observer log file. The default value is `USER`, which limits the observer log contents to tracing information about fast-start failover, status changes of the primary and target standby database, and error/warning messages. Setting `TRACE_LEVEL` to `SUPPORT` increases the amount of tracing information to include lower-level information needed by Oracle Support Services.

Usage Notes

- If no cfg\_group\_name is specified, then this command stops all LOCAL observers running on this host (where this DGMGRL session is running) for all broker configurations defined in the observer configuration file.
- The `cfg_group_name` cannot be the keyword `ALL`.

Command Example

```
DGMGRL> STOP OBSERVING;
ObserverConfigFile=/net/oracle/dataguard/observer.ora
observer configuration file parsing succeeded
Submitted command "STOP OBSERVER HOST IS OBM1" using connect identifier cfg1_cid.  
Submitted command "STOP OBSERVER HOST IS OBM1" using connect identifier cfg2_cid.  
Submitted command "STOP OBSERVER HOST IS OBM1" using connect identifier cfg3_cid.  

Check superobserver.log and individual observer logs for execution details. 

DGMGRL> STOP OBSERVING GRP_A;
ObserverConfigFile=/net/oracle/dataguard/observer.ora
observer configuration file parsing succeeded
Submitted command "STOP OBSERVER HOST IS OBM1" using connect identifier cfg1_cid.  
Submitted command "STOP OBSERVER HOST IS OBM1" using connect identifier cfg2_cid.  

Check superobserver.log and individual observer logs for execution details.
```

### 7.74 SWITCHOVER

When you issue the `SWITCHOVER` command, the current primary database becomes a standby database, and the specified standby database becomes the primary database.

This is known as a switchover operation.

Format

SWITCHOVER TO database\_name \[WAIT \[timeout\_in\_seconds\]\];

The `WAIT` option specifies that you want to wait for sessions to drain before proceeding with the switchover. The broker determines the maximum `drain_timeout` value for all currently active services and waits for up to that amount of time for all current client requests to be processed, before proceeding with the switchover. The `drain-timeout` value is an option that is specified on the SRVCTL utility's ` add service` command. The `WAIT` option has no effect on a single instance database; it is valid only when services are configured with attributes related to Application Continuity in Oracle Clusterware.

You can also optionally specify the number of seconds to wait for sessions to drain. The value you specify overrides the `drain_timeout` value.

Command Parameters

database-name

The name of the standby database you want to change to the primary database role.

timeout-in-seconds

The time allowed for resource draining to be completed, in seconds, before the switchover operation proceeds.

Permitted values are "" (an empty string), 0 (zero), or any positive integer. The default value is an empty string indicating that this option is not set. If the value is zero, then draining occurs immediately. During the draining period, all current client requests are processed, but new requests are not accepted.

Usage Notes

- If fast-start failover is enabled, you may switch over only to the fast-start failover target standby database.
- The broker verifies that the primary and standby databases are in the following states before starting the switchover:
	- The primary database must be enabled and in the `TRANSPORT-ON` state so redo transport services are started.
		- The standby database must be enabled and in the `APPLY-ON` state, with log apply services started.
- The broker allows the switchover to proceed as long as there are no redo transport services errors for the standby database that you selected to participate in the switchover. However, errors occurring for any other bystander standby database will not prevent the switchover from proceeding.
- Switchover to a logical standby database is not allowed when the configuration is operating in maximum protection mode.
- If the broker configuration is operating in either maximum protection mode or maximum availability mode, the switchover maintains the protection mode even after the operation (described in [Before You Perform a Switchover Operation](using-data-guard-broker-to-manage-switchovers-failovers.md)). The switchover will not be allowed if the mode cannot be maintained because the target standby database of the switchover was the only standby that satisfied the protection mode requirement.
- If the standby database that is assuming the primary role is a physical standby database, then the old primary database will be restarted after the switchover completes. If the standby database is a logical standby database, then neither the primary database nor the logical standby database is restarted.
- If the standby database that is assuming the primary role is a physical standby database, then the original primary becomes a physical standby database.
- If the standby database that is assuming the primary role is a logical standby database, then the original primary becomes a logical standby database.
- If an Oracle RAC primary database is becoming a physical standby database, all but one instance of the primary database will be shut down before performing the switchover. See [Switchover](using-data-guard-broker-to-manage-switchovers-failovers.md) for details.
- You cannot switchover to a snapshot standby database.
- If the standby database that is assuming the primary role is a logical standby database and there are physical standby databases in the configuration, after the switchover, the physical standby databases will be disabled.
	Caution:
	For this reason, Oracle generally recommends that you specify your physical standby database for switchover instead of your logical standby database. If you must switch over to your logical standby database, see [Reenabling Disabled Databases After a Role Change](using-data-guard-broker-to-manage-switchovers-failovers.md) to re-create your physical standby database.
	If you intend to switch back to the original primary database relatively soon, you may allow the physical and snapshot standbys to remain disabled. Once you have completed the switchover back to the original primary, you may then reenable the physical and snapshot standby databases since they are still viable standbys for the original primary database.

Command Examples

Example 1: Successful Switchover From Physical to Primary

The following example shows a successful switchover in which the physical standby database, `South_Sales`, transitions into the primary role.

```
DGMGRL> SWITCHOVER TO 'South_Sales';
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

Example 2: Unsuccessful Switchover Due to Use of O/S Authentication

If you connect to the database using operating system authentication, you can use any username and password to connect. However, DGMGRL may not be able to shut down and start up the primary and standby database automatically because it cannot remotely authenticate itself.

The following example shows a switchover that succeeded but returns an error because DGMGRL cannot shut down and start up the primary and standby databases.

```
DGMGRL> SWITCHOVER TO 'South_Sales';
Performing switchover NOW, please wait...
New primary database "South_Sales" is opening...
Operation requires shutdown of instance "north_sales1" on database "North_Sales"
Shutting down instance "north_sales1"...
ORA-01031: insufficient privileges
 
Warning: You are no longer connected to ORACLE.
 
Please complete the following steps to finish switchover:
        shut down instance "north_sales1" of database "North_Sales"
        start up and mount instance "north_sales1" of database "North_Sales"
```

Note:

For DGMGRL to restart instances automatically, you must connect to the database using the same credentials given in the last `CONNECT` command, even if the last `CONNECT` command was used to connect to another database.

You must manually issue the SHUTDOWN and STARTUP commands to restart the new primary and any standby instances that may have been shut down.

### 7.75 VALIDATE DATABASE

The `VALIDATE DATABASE` command performs a comprehensive set of database checks prior to a role change.

The checks use information available in various Oracle Data Guard views as well as the Automatic Diagnostic Repository.

Format

```
VALIDATE DATABASE [VERBOSE] database-name;
```

Command Parameters

database-name

The name of the database for which you want to display information. The `VERBOSE` keyword, if used, must come before the `database-name` or an error is returned.

Usage Notes

The `VALIDATE` ` DATABASE` command shows a brief summary of the database, and reports any errors or warnings that were detected. `VALIDATE ` `DATABASE` ` VERBOSE` shows everything in the brief summary plus all items that were validated.

Command Examples

The examples in this section show what the `VALIDATE` ` DATABASE` command output might look like in both the brief and verbose forms for primary and standby databases.

The examples in this section show what the `VALIDATE` ` DATABASE` command output might look like in both the brief and verbose forms for primary and standby databases.

Example 1: VALIDATE DATABASE Output in Brief Format for a Primary

The following example shows brief output for a primary database:

```
DGMGRL> VALIDATE DATABASE 'South_Sales';
 
  Database Role:    Primary database
 
  Ready for Switchover:  Yes
```

Example 2: VALIDATE DATABASE Output in Brief Format for a Logical Standby

The following example shows brief output for a logical standby database:

```
DGMGRL> VALIDATE DATABASE 'West_Sales';
 
  Database Role:     Logical standby database
  Primary Database:  South_Sales
 
  Ready for Switchover:  Yes
  Ready for Failover:    Yes (Primary Running)
    Warning: Physical and snapshot standby databases will
    be disabled if a role change is performed to this database
```

Example 3: VALIDATE DATABASE Output in Brief Format for a Physical Standby

The following example shows brief output for a physical standby database:

```
DGMGRL> VALIDATE DATABASE 'North_Sales';
 
  Database Role:     Physical standby database
  Primary Database:  South_Sales
 
  Ready for Switchover:  Yes
  Ready for Failover:    Yes (Primary Running)
```

Example 4: VALIDATE DATABASE Output in Verbose Format for a Primary

The following example shows verbose output for a primary database:

```
DGMGRL> VALIDATE DATABASE VERBOSE 'South_Sales';
 
  Database Role:    Primary database
 
  Ready for Switchover:  Yes
 
  Capacity Information:
    Database     Instances        Threads        
    South_Sales      2                2              
 
  Temporary Tablespace File Information:
    South_Sales TEMP Files:  2
 
  Flashback Database Status:
    South_Sales:  On
 
  Data file Online Move in Progress:
    South_Sales:  No
 
  Transport-Related Information:
    Transport On:  Yes
 
  Log Files Cleared:
    South_Sales Standby Redo Log Files:  Cleared
 
  Automatic Diagnostic Repository Errors:
    Error                       South_Sales   
    No logging operation        NO     
    Control file corruptions    NO     
    System data file missing    NO     
    System data file corrupted  NO     
    System data file offline    NO     
    User data file missing      NO     
    User data file corrupted    NO     
    User data file offline      NO     
    Block Corruptions found     NO
```

Example 5: VALIDATE DATABASE Output in Verbose Format for a Logical Standby

The following command shows verbose output for a logical standby database:

```
DGMGRL> VALIDATE DATABASE VERBOSE 'West_Sales';
  Database Role:     Logical standby database
  Primary Database:  South_Sales
 
  Ready for Switchover:  Yes
  Ready for Failover:    Yes (Primary Running)
    Warning: Logical and snapshot standby databases will
    be disabled if a role change is performed to this database
 
  Capacity Information:
    Database      Instances        Threads        
    South_Sales      2                2              
    West_Sales       2                2              
 
  Temporary Tablespace File Information:
    South_Sales TEMP Files:   2
    West_Sales TEMP Files:  2
 
  Flashback Database Status:
    South_Sales:   On
    West_Sales:  On
 
  Data file Online Move in Progress:
    South_Sales:   No
    West_Sales:  No
 
  Standby Apply-Related Information:
    Apply State:      Running
    Apply Lag:        0 seconds
    Apply Delay:      0 minutes
 
  Transport-Related Information:
    Transport On:      Yes
    Gap Status:        No Gap
    Transport Lag:     0 seconds
    Transport Status:  Success
 
  Log Files Cleared:
    South_Sales Standby Redo Log Files: Cleared
    West_Sales Online Redo Log Files:   Not applicable for this database
    West_Sales Standby Redo Log Files:  Available
 
  Current Log File Groups Configuration:
    Thread #  Online Redo Log Groups   Standby Redo Log Groups  Status
              (South_Sales)            (West_Sales)                  
    1         4                        5                        Sufficient SRLs
    2         4                        5                        Sufficient SRLs
 
  Future Log File Groups Configuration:
    Thread #  Online Redo Log Groups   Standby Redo Log Groups  Status
              (West_Sales)             (South_Sales)                   
    1         4                        5                        Sufficient SRLs
    2         4                        5                        Sufficient SRLs
 
  Current Configuration Log File Sizes:
    Thread #   Smallest Online Redo      Smallest Standby Redo    
               Log File Size             Log File Size            
               (South_Sales)             (West_Sales)                  
    1          25 MBytes                 25 MBytes                
    2          25 MBytes                 25 MBytes                
 
  Future Configuration Log File Sizes:
    Thread #   Smallest Online Redo      Smallest Standby Redo    
               Log File Size             Log File Size            
               (West_Sales)              (South_Sales)                   
    1          25 MBytes                 25 MBytes                
    2          25 MBytes                 25 MBytes                
 
  Apply-Related Property Settings:
    Property                        South_Sales Value        West_Sales Value
    DelayMins                       0                        0
    LsbyMaxEventsRecorded           0                        0
    LsbyPreserveCommitOrder         <empty>                  <empty>
    LsbyRecordSkipErrors            <empty>                  <empty>
    LsbyRecordSkipDdl               <empty>                  <empty>
    LsbyRecordAppliedDdl            <empty>                  <empty>
 
  Transport-Related Property Settings:
    Property                        South_Sales Value        West_Sales Value
    LogXptMode                      SYNC                     SYNC
    Dependency                      <empty>                  <empty>
    DelayMins                       0                        0
    Binding                         optional                 optional
    MaxFailure                      0                        0
    MaxConnections                  1                        1
    ReopenSecs                      30                       30
    NetTimeout                      300                      300
    RedoCompression                 DISABLE                  DISABLE
    LogShipping                     ON                       ON
 
  Automatic Diagnostic Repository Errors:
    Error                       South_Sales     West_Sales  
    No logging operation        NO              NO     
    Control file corruptions    NO              NO     
    SRL Group Unavailable       NO              NO     
    System data file missing    NO              NO     
    System data file corrupted  NO              NO     
    System data file offline    NO              NO     
    User data file missing      NO              NO     
    User data file corrupted    NO              NO     
    User data file offline      NO              NO     
    Block Corruptions found     NO              NO
```

Example 6: VALIDATE DATABASE Output in Verbose Format for a Physical Standby

The following command shows verbose output for a physical standby database:

```
DGMGRL> VALIDATE DATABASE VERBOSE North_Sales';
  Database Role:     Physical standby database
  Primary Database:  South_Sales
 
  Ready for Switchover:  Yes
  Ready for Failover:    Yes (Primary Running)
 
  Capacity Information:
    Database     Instances        Threads        
    South_Sales      2                2              
    North_Sales      2                2              
 
  Temporary Tablespace File Information:
    South_Sales TEMP Files:   2
    North_Sales TEMP Files:  2
 
  Flashback Database Status:
    South_Sales:   On
    North_Sales:  On
 
  Data file Online Move in Progress:
    South_Sales:   No
    North_Sales:  No
 
  Standby Apply-Related Information:
    Apply State:      Running
    Apply Lag:        0 seconds
    Apply Delay:      0 minutes
 
  Transport-Related Information:
    Transport On:      Yes
    Gap Status:        No Gap
    Transport Lag:     0 seconds
    Transport Status:  Success
 
  Log Files Cleared:
    South_Sales Standby Redo Log Files:  Cleared
    North_Sales Online Redo Log Files:   Cleared
    North_Sales Standby Redo Log Files:  Available
 
  Current Log File Groups Configuration:
    Thread #  Online Redo Log Groups   Standby Redo Log Groups  Status
              (South_Sales)            (North_Sales)                 
    1         4                        5                        Sufficient SRLs
    2         4                        5                        Sufficient SRLs
 
  Future Log File Groups Configuration:
    Thread #  Online Redo Log Groups   Standby Redo Log Groups  
              (North_Sales)            (South_Sales)                   
    1         4                        5                        Sufficient SRLs
    2         4                        5                        Sufficient SRLs
 
  Current Configuration Log File Sizes:
    Thread #   Smallest Online Redo      Smallest Standby Redo    
               Log File Size             Log File Size            
               (South_Sales)             (North_Sales)                  
    1          25 MBytes                 25 MBytes                
    2          25 MBytes                 25 MBytes                
 
  Future Configuration Log File Sizes:
    Thread #   Smallest Online Redo      Smallest Standby Redo    
               Log File Size             Log File Size            
               (North_Sales)                   (South_Sales)                   
    1          25 MBytes                 25 MBytes                
    2          25 MBytes                 25 MBytes                
 
  Apply-Related Property Settings:
    Property                        South_Sales Value        North_Sales Value
    DelayMins                       0                        0
    ApplyParallel                   AUTO                     AUTO
 
  Transport-Related Property Settings:
    Property                        South_Sales Value        North_Sales Value
    LogXptMode                      SYNC                     SYNC
    Dependency                      <empty>                  <empty>
    DelayMins                       0                        0
    Binding                         optional                 optional
    MaxFailure                      0                        0
    MaxConnections                  1                        1
    ReopenSecs                      30                       30
    NetTimeout                      300                      300
    RedoCompression                 DISABLE                  DISABLE
    LogShipping                     ON                       ON
 
  Automatic Diagnostic Repository Errors:
    Error                       South_Sales     North_Sales  
    No logging operation        NO              NO     
    Control file corruptions    NO              NO     
    SRL Group Unavailable       NO              NO     
    System data file missing    NO              NO     
    System data file corrupted  NO              NO     
    System data file offline    NO              NO     
    User data file missing      NO              NO     
    User data file corrupted    NO              NO     
    User data file offline      NO              NO     
    Block Corruptions found     NO              NO
```

### 7.76 VALIDATE DATABASE DATAFILE

The `VALIDATE DATABASE DATAFILE` command performs validation of data files across the primary database and standby databases.

The validation of data files detects lost writes at either database.

Format

VALIDATE DATABASE \[database-name | ALL\] DATAFILE \[datafile-name | datafile-number | ALL\] OUTPUT=" output-file-name ";

Command Parameters

database-name

The name of the database for which you want to display information. The `VERBOSE` keyword, if used, must come before the `database-name` or an error is returned.

If the database to be validated is either the primary or `ALL`, then the data files for all standby databases are compared with data files of the primary.

If the database to be validated is a standby database, then its data files are compared with the data files of the primary.

datafile-name | datafile-number

You can specify a data file to be compared by name (datafile-name) or by number (datafile-number).

The datafile-name is the name of a specific date file that you want validated.

The datafile-number is the file identification number of a data file (as shown in the `FILE#` column of the `V$DATAFILE` view).

output-file-name

A file generated on the server that you must check to determine if block comparison is completed and whether there were any lost writes. Output files are created in the diagnostics `trace` directory of the database being compared.

Usage Notes

- The `VALIDATE` `DATABASE` command shows a brief summary of the database, and reports any errors or warnings that were detected.
- When the `VALIDATE` `DATABASE` command is issued, it immediately returns a message that data file comparison has started on a database, but this does not mean that data file comparison completed or that there were no lost-writes between data files. You must check the output files that are generated to determine whether data file comparison was completed, or if there were lost writes.

Command Example

Example: Using VALIDATE DATABASE DATAFILE to Compare Data Files

The following command would compare the data files on the standby to those on the primary. Output would be sent to a file named `dbcomp1.out`.

```
DGMGRL> VALIDATE DATABASE boston DATAFILE ALL OUTPUT=dbcomp1.out;
Operation requires a connection to database "boston"
Connecting ...
Output files are created in /path/to/trace on host "standby-host"
```

The following shows sample output from the command:

```
Client is connected to database: boston. Role: physical standby.

    ******************************
    Remote database chicago.
    remote db role: primary database

    Slave Id  0
    Summary:
    Different data block pairs: 66617

    Details:
***************************************************
    ID: Block Type Id
    TOTAL: Total number of blocks found
    DIFFV: Number of block pairs with different version
    LWLOC: Lost Writes at Local
    LWRMT: Lost Writes at Remote
    SAMEV: Number of block pairs with same version
    SAMEV&C: Number of block pairs with same version and checksum
    DIFFPAIR: Number of block pairs with same version but different contents
    ENCERR: Undecided blocks related to encryption/decrytion error.
            e.g. Wallet is not open.
    SKIPPED: Skipped blocks due to data corruption, direct load, etc

    ID TOTAL   DIFFV   LWLOC   LWRMT   SAMEV   SAMEV&C DIFFPAIR ENCERR SKIPPED
    02 0067698 0001032 0000000 0000000 0066666 0000049 0066617 0000000 0000000
    29 0000001 0000001 0000000 0000000 0000000 0000000 0000000 0000000 0000000
    30 0000125 0000001 0000000 0000000 0000124 0000124 0000000 0000000 0000000
    38 0000014 0000014 0000000 0000000 0000000 0000000 0000000 0000000 0000000
```

### 7.77 VALIDATE FAR\_SYNC

The `VALIDATE FAR_SYNC` command performs a comprehensive set of checks for a far sync instance.

The checks use information available in various Oracle Data Guard views.

Format

VALIDATE FAR\_SYNC \[VERBOSE\] far\_sync\_instance\_name \[WHEN PRIMARY IS database-name\];

Command Parameters

far\_sync\_instance\_name

The name of the far sync instance for which you want to display information. The `VERBOSE` keyword, if used, must come before the `far_sync_instance_name` or an error is returned.

database-name

The validation of the far sync instance is performed based on the specified database being the primary database.

Usage Notes

The `VALIDATE` `FAR_SYNC` command shows a brief summary of the far sync instance and reports any errors or warnings that were detected. The `VALIDATE` `FAR_SYNC` `VERBOSE` command shows everything in the brief summary plus redo transport-related information.

Command Examples

The examples in this section show what the `VALIDATE` `FAR_SYNC` command output might look like in various scenarios.

Example 1: Brief VALIDATE FAR\_SYNC Output

The following example shows brief output for a far sync instance:

```
DGMGRL> VALIDATE FAR_SYNC FS;
 
    Member Role:        Far Sync Instance   
    When Primary Is:    North_Sales                
 
    Active Redo Source: North_Sales                
    Redo Destinations:                      
                        South_Sales               
 
    Thread #  Online Redo Log Groups  Standby Redo Log Groups Status       
              North_Sales             FS                                
    1         4                       5                       Sufficient SRLs
```

Example 2: Verbose VALIDATE FAR\_SYNC Output

The following example shows verbose output for a far sync instance:

```
DGMGRL> VALIDATE FAR_SYNC VERBOSE FS;
 
    Member Role:        Far Sync Instance   
    When Primary Is:    North_Sales                
 
    Active Redo Source: North_Sales                
    Redo Destinations:                      
                        South_Sales               
 
    Thread #  Online Redo Log Groups  Standby Redo Log Groups Status       
              North_Sales             FS                                
    1         4                       5                       Sufficient SRLs
 
  Transport-Related Information:
    Transport On:      Yes
    Gap Status:        No Gap
    Transport Lag:     0 seconds (computed 0 seconds ago)
    Transport Status:  Success
```

Example 3: VALIDATE FAR\_SYNC Output When South\_Sales Is the Primary

The following example shows the output when the `South_Sales` database is specified as the primary database:

```
DGMGRL> VALIDATE FAR_SYNC FS WHEN PRIMARY IS 'South_Sales';
 
    Member Role:        Far Sync Instance   
    When Primary Is:    South_Sales               
    Redo Destinations:                      
                        North_Sales                
 
    Thread #  Online Redo Log Groups  Standby Redo Log Groups Status       
              South_Sales             FS                                
    1         4                       5                       Sufficient SRLs
```