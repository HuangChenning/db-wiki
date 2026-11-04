---
title: Data Guard Command-Line Interface Reference
book: Data Guard Broker
doc_id: E40771-07
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40771/dgmgrl.htm
tags:
  - oracle
  - 11g
  - data-guard-broker
---

## 7 Data Guard Command-Line Interface Reference

The Data Guard command-line interface (DGMGRL) enables you to manage a Data Guard broker configuration and its databases directly from the command line, or from batch programs or scripts. You can use the Data Guard command-line interface as an alternative to Oracle Enterprise Manager for managing a Data Guard configuration.

This chapter contains the following sections, which provide reference information for the Data Guard command-line interface:

- Starting the Data Guard Command-Line Interface
- Exiting the Data Guard Command-Line Interface

## 7.1 Starting the Data Guard Command-Line Interface

To run DGMGRL, you must have `SYSDBA` privileges.

Start the command-line interface by entering `dgmgrl` at the command-line prompt on a system where Oracle is installed:

```
% dgmgrl
```

The DGMGRL command prompt is displayed:

```
DGMGRL>
```

### 7.1.1 DGMGRL Optional Parameters

You can supply optional parameters on the command line to indicate how you want the Data Guard command-line interface to display output such as command prompts, banners, and messages.

Additionally, a single command mode is available. In this mode, DGMGRL executes one command and exits upon the completion of the command. The exit code is the result of the command. If the exit code is 0, the command completed successfully. Otherwise, there was an error.

The command line of DGMGRL appears as follows:

`% dgmgrl [<options>] [<logon> [<command>] ]`

Specify any of the following keywords when you invoke the DGMGRL command-line interface:

- `<options>` can be one of the following choices:
	- `-echo`
		Displays command input and output to the default display device. If you do not use this parameter, only the output from the command is displayed.
		- `-logfile` \<file-spec> "\<dgmgrl-command>"
		Specifies a file into which you can capture the actions of the DGMGRL command-line interface. This is particularly useful when DGMGRL is being invoked to serve as the fast-start failover observer. See the "START OBSERVER" command for more information.
	See Also:
	- The "START OBSERVER" command
	- [Section 9.5.3, "Capturing Observer Actions in the Observer Log File"](troubleshooting.md)
- - `-silent`
		Suppresses the display of the DGMGRL (`DGMGRL>`) command prompt on your default display device. This option is useful if you are directing the command output to a file or to another display tool.
- `<logon>` is:
	- `username [@connect-identifier]`
		To connect to the database, enter a `username` and optionally, a `connect-identifier`. You will then be prompted for a password. The `connect-identifier` is a fully specified connect descriptor or a name to be resolved by an Oracle naming method (for example, TNS).
		WARNING:
		Including a password on the command line when invoking DGMGRL is a security risk. This risk can be avoided either by omitting the password when invoking DGMGRL and entering it when prompted, or by using an external authentication method.
		- You can connect as '/' when using operating-system authentication (remote database restarts will not work), Secure Sockets Layer (SSL) protocol, or database credentials stored in a wallet.
- `<command>` is a single command.
	For example:
	`% dgmgrl sys/ "show database 'North_Sales'"`
	`Password`: password

The following subsections specify the command format that you enter at the `DGMGRL>` command prompt.

### 7.1.2 DGMGRL Command Format and Parameters

The DGMGRL commands allow you to create and maintain one broker configuration at a time. A broker configuration can consist of a primary database and up to 30 standby databases.

After you invoke the command-line interface, you can enter any of the DGMGRL commands listed in Table 7-1. Each command and its associated parameters are described in detail in later sections of this chapter.

Table 7-1 Summary of DGMGRL Commands

| Command | Effect |
| --- | --- |
| ADD DATABASE | Adds a new standby database profile to the existing broker configuration. |
| CONNECT | Connects to the specified database using the specified username. |
| CONVERT DATABASE | Converts the specified database to either a snapshot standby database or a physical standby database. |
| CREATE CONFIGURATION | Creates a broker configuration and adds a primary database profile to the configuration. |
| DISABLE CONFIGURATION | Disables broker management of a configuration so that the configuration and all of its databases are no longer managed by the broker. |
| DISABLE DATABASE | Disables broker management of the named standby database. |
| DISABLE FAST\_START FAILOVER | Disables fast-start failover. |
| DISABLE FAST\_START FAILOVER CONDITION | Allows a user to remove conditions for which a fast-start failover should be performed. |
| EDIT CONFIGURATION (Property) | Changes the value of a property for the broker configuration. |
| EDIT CONFIGURATION (Protection Mode) | Changes the current protection mode setting for the broker configuration. |
| EDIT DATABASE (Property) | Changes the value of a property for the named database. |
| EDIT DATABASE (Rename) | Changes the name used by the broker to refer to the specified database. |
| EDIT DATABASE (State) | Changes the state of the specified database. |
| EDIT INSTANCE (AUTO PFILE) | Sets the name of the initialization parameter file for the specified instance. |
| EDIT INSTANCE (Property) | Changes the value of a property for the specified instance. |
| ENABLE CONFIGURATION | Enables broker management of the broker configuration and all of its databases. |
| ENABLE DATABASE | Enables broker management of the specified database. |
| ENABLE FAST\_START FAILOVER | Enables the broker to automatically failover from the primary database to a target standby database. |
| ENABLE FAST\_START FAILOVER CONDITION | Allows a user to add conditions for which a fast-start failover should be performed. |
| EXIT | Exits the Data Guard command-line interface. |
| FAILOVER | Performs a database failover operation in which the standby database, to which DGMGRL is currently connected, fails over to the role of primary database. |
| HELP | Displays online help for the Data Guard command-line interface. |
| QUIT | Quits the Data Guard command-line interface. |
| REINSTATE DATABASE | Reinstates the database after a failover. |
| REMOVE CONFIGURATION | Removes the broker configuration including all of its database profiles from the broker configuration file. |
| REMOVE DATABASE | Removes the specified standby database profile from the broker configuration. |
| REMOVE INSTANCE | Removes knowledge of an instance from an existing database profile in the broker configuration. |
| SHOW CONFIGURATION | Displays information about the broker configuration. |
| SHOW DATABASE | Displays information about the specified database. |
| SHOW FAST\_START FAILOVER | Displays all fast-start failover related information. |
| SHOW INSTANCE | Displays information about the specified instance. |
| SHUTDOWN | Shuts down a currently running Oracle database. |
| START OBSERVER | Starts the observer. |
| STARTUP | Starts an Oracle instance with the same options as SQL\*Plus, including mounting and opening a database. |
| STOP OBSERVER | Stops the observer. |
| SWITCHOVER | Performs a switchover operation in which the current primary database becomes a standby database, and the specified standby database becomes the primary database. |

### 7.1.3 DGMGRL Command Usage Notes

To use DGMGRL, the following must be true:

- The `DG_BROKER_START` dynamic initialization parameter is set to `TRUE`.
- To enable broker operations that require restarting instances without manual intervention, Oracle Net Services must be configured on each of the hosts that contain the primary and standby database instances. Specifically, the listener.ora file must contain static configuration information about the instance. The `GLOBAL_DBNAME` attribute must be set to `db_unique_name` `_DGMGRL.``db_domain`. See [Section 2.2](install.md) for additional information.
- The Connect Identifier used while creating the configuration or adding a database, must be resolvable from any of the hosts in the configuration.
	See Also:
	[Chapter 6](cli.md) for more information about preparing and starting Oracle Data Guard broker. See the [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for more information about setting up the network files and listener on the standby database.
- You must have SYSDBA privileges to use the Data Guard command-line interface. Do not include `AS SYSDBA` on the `CONNECT` command because SYSDBA is the default setting for this command.
- If you specify more than one option on the command, you can specify the options in any order.
- A semicolon is required at the end of each DGMGRL command.
- Characters specified in a DGMGRL command string value are interpreted as lowercase characters, unless enclosed in double (") or single (') quotation marks. For example, database and DatAbaSe are equivalent, but "database" and "DatAbaSe" are not.
- You can use the backslash (\\) to escape a single quotation mark ('), a double quotation mark ("), and the backslash character (\\) itself if these characters appear in a character string.
- Some operations on a broker configuration may require that one or more databases be shut down and restarted. In most cases, DGMGRL will automatically shut down and restart a given database for you if the following are true:
	- The `instance-name` is the SID (this applies to Enterprise Manager as well as DGMGRL).
		- The broker must be able to connect to the database using the same credentials given in the last `CONNECT` command, even if the last `CONNECT` command was used to connect to another database.

Command Examples

Example 1

This example demonstrates how to connect to the DGMGRL command-line interface on a local system.

```
% dgmgrl
.
.
.
Welcome to DGMGRL, type "help" for information.

DGMGRL> CONNECT sys;
Password: password
Connected.
```

Example 2

This example demonstrates how to connect to the Data Guard (DGMGRL) command-line interface on a remote system.

```
DGMGRL> CONNECT sys@remote-stby;
Password: password
Connected.
```

## 7.2 Exiting the Data Guard Command-Line Interface

When you are done working with the command-line interface and want to return to the operating system, enter the `EXIT` or `QUIT` command at the DGMGRL command prompt. For example:

```
DGMGRL> EXIT;
```

## ADD DATABASE

Creates a new standby database profile and adds it to the existing broker configuration. The `AS CONNECT IDENTIFIER` clause is optional. If you do not specify this clause, the broker will search the `LOG_ARCHIVE_DEST_` `n` initialization parameters on the primary database for an entry that corresponds to the database being added.

The `MAINTAINED AS` clause allows you the option of specifying the standby database type. Otherwise, the broker automatically determines whether the standby database type is a physical, logical, or snapshot standby database.

Format

ADD DATABASE database-name

\[AS CONNECT IDENTIFIER IS connect-identifier\]

Command Parameters

database-name

The name that will be used by the broker to refer to this standby database. It must match (case-insensitive) the value of the corresponding database `DB_UNIQUE_NAME` initialization parameter.

connect-identifier

A fully specified connect descriptor or a name to be resolved by an Oracle Net Services naming method (for example, TNS). The value you specify is also used as the initial value of the `DGConnectIdentifier` database property. If you do not specify this option, the broker will search the primary database `LOG_ARCHIVE_DEST_` `n` parameters for a corresponding entry to the standby database and use its `SERVICE` value for the connect-identifier.

Usage Notes

- To issue this command, you must connect to the primary database or to an enabled standby database that is already in the configuration.
- The broker uses the specified `connect-identifier` to communicate with the specified database from other databases. Therefore, you must ensure that the `connect-identifier` can be used to address the specified database from all databases in your configuration. For example, if TNS is used as the naming method, you must ensure that the tnsnames.ora file on every database and instance that is part of the configuration contains an entry for the `connect-identifier`. The connect identifier must resolve to the same connect descriptor. If the database that is being added is an Oracle RAC database, the `connect-identifier` provided here must reach all instances of the Oracle RAC, preferably with `FAILOVER` attributes set.
	See Also:
	[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm)
- If the connection cannot be made, the broker does not add the new database to the configuration.
- The `MAINTAINED AS` clause is deprecated in this release. The broker will determine standby database type automatically.

Command Example

Example 1

The following example shows how to add a database named `South_Sales`.

```
DGMGRL> ADD DATABASE South_Sales AS CONNECT IDENTIFIER IS South_Sales.example.com;
Database "South_Sales" added
```

## CONNECT

Connects a given username to the specified database.

Format

CONNECT username \[@connect-identifier\];

Command Parameters

username

Represents the username with which you want to connect to the database. You will be prompted for a password after you enter a username and optionally, a connect-identifier.

connect-identifier

This parameter is optional. It is an Oracle Net Services connect identifier for the database to which you want to connect. The exact syntax depends upon the Oracle Net Services communications protocol your Oracle installation uses.

Usage Notes

- The username and password must be valid for the database to which you are trying to connect. The username you specify must have the SYSDBA privilege. You do not have to include `AS SYSDBA` on the `CONNECT` command because SYSDBA is the default setting for this command.
- If the `CONNECT` command returns an error, check to see that you specified a valid `connect-identifier`.

Command Examples

Example 1

This example connects to the default database on the local system.

```
DGMGRL> CONNECT sys;
Password: password
Connected.
```

Example 2

This example connects to a remote database whose `connect-identifier` is `North_Sales.example.com`.

```
DGMGRL> CONNECT sys@North_Sales.example.com;
Password: password
Connected.
```

Example 3

This example connects to a database using `CONNECT '/'` so that connection credentials are not visible on the command line:

```
DGMGRL> CONNECT /@North_Sales.example.com;
```

You must set up Oracle Wallet or SSL to use `CONNECT '/'`. By setting up Oracle Wallet or SSL, you can write a script to securely start and run the observer as a background job without specifying database credentials in the script.

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm) for more information about Oracle Wallet and SSL

## CONVERT DATABASE

Converts a physical standby database to a snapshot standby database, or reverts the snapshot standby database back to a physical standby database.

A snapshot standby database is a fully updatable standby database. Like a physical or logical standby database, a snapshot standby database receives and archives redo data from a primary database. Unlike a physical or logical standby database, a snapshot standby database does not apply the redo data that it receives. The redo data received by a snapshot standby database is not applied until the snapshot standby is converted back into a physical standby database, after first discarding any local updates made to the snapshot standby database.

A snapshot standby database is best used in scenarios that require a temporary, updatable snapshot of a physical standby database. Note that because redo data received by a snapshot standby database is not applied until it is converted back into a physical standby, the time needed to perform a role transition is directly proportional to the amount of redo data that needs to be applied.

See [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/toc.htm) for additional information about snapshot standby databases.

Format

CONVERT DATABASE db\_unique\_name TO {SNAPSHOT | PHYSICAL} STANDBY;

Usage Notes

- A physical standby database cannot be converted to a snapshot standby database if it is the target of a fast-start failover. The `ORA-16668: operation cannot be performed on the fast-start failover target standby database` error will be returned.
- Use the DGMGRL ADD DATABASE command to import an existing snapshot standby database into a Data Guard broker configuration.
- A snapshot standby database cannot be the target of a switchover or a fast-start failover.
- A snapshot standby database can be the target of a manual failover if fast-start failover is disabled.
- You can use the `SHOW CONFIGURATION` or `SHOW DATABASE` command to verify the conversion result. For example:
	```
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
- After a snapshot standby database is converted back to a physical standby database, it will be in the default state for a physical standby database, `APPLY-ON`.

Command Examples

Example 1

Issue the following to convert a physical standby database to a snapshot standby database:

```
DGMGRL> CONVERT DATABASE 'South_Sales' to SNAPSHOT STANDBY;
Converting database "South_Sales" to a Snapshot Standby database, please wait...
Database "South_Sales" converted successfully
```

Example 2

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

## CREATE CONFIGURATION

Creates a new broker configuration and adds a primary database profile to the configuration.

Format

CREATE CONFIGURATION configuration-name AS

PRIMARY DATABASE IS database-name

CONNECT IDENTIFIER IS connect-identifier;

Command Parameters

configuration-name

A user-friendly name for the configuration you are creating. Valid names contain any alphanumeric characters. If spaces are included in the name, the name must be enclosed in double or single quotation marks. The name must consist of 30 or fewer bytes.

database-name

The name that will be used by the broker to refer to the primary database. It must match (case-insensitive) the value of the primary database `DB_UNIQUE_NAME` initialization parameter.

connect-identifier

A fully specified connect descriptor or a name to be resolved by an Oracle Net Services naming method (for example, TNS). The value you specify is also used as the initial value of the `DGConnectIdentifier` database property. If you do not specify this option, the broker will search the primary database `LOG_ARCHIVE_DEST_` `n` parameters for a corresponding entry to the standby database and use its `SERVICE` value for the connect-identifier.

Usage Notes

- A broker configuration is a named collection of one or more databases that you want to manage as a group. You must specify a value for each of the command parameters. There are no default values.
- You must connect to the primary database to issue this command.
- The broker uses the specified `connect-identifier` to communicate with the specified database from other databases. Therefore, you must ensure that the `connect-identifier` can be used to address the specified database from all databases in your configuration. For example, if TNS is used as the naming method, you must ensure that the tnsnames.ora file on every database and instance that is part of the configuration contains an entry for the `connect-identifier`. The connect identifier must resolve to the same connect descriptor. If the database that is being added is an Oracle RAC database, the `connect-identifier` provided here must reach all instances of the Oracle RAC, preferably with `FAILOVER` attributes set.
	See Also:
	[Oracle Database Net Services Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e41945/toc.htm)
- To add standby databases after you create the broker configuration, use the ADD DATABASE command.

Command Example

Example 1

The following example creates a new broker configuration named `DRSolution` with a primary database named `North_Sales`.

```
DGMGRL> CREATE CONFIGURATION 'DRSolution' AS
> PRIMARY DATABASE IS 'North_Sales'
> CONNECT IDENTIFIER IS North_Sales.example.com;
Configuration "DRSolution" created with primary database "North_Sales"
```

## DISABLE CONFIGURATION

Disables broker management of a configuration so that the configuration and all of its databases are no longer managed by the broker.

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

Example 1

The following example disables management of the broker configuration and all of its databases.

```
DGMGRL> DISABLE CONFIGURATION;
Disabled.
```

## DISABLE DATABASE

Disables broker management of the named standby database. This means that broker directed state changes will be disallowed for this database, and the broker will not monitor the database for health status or for monitorable database properties.

Format

DISABLE DATABASE database-name;

Command Parameter

database-name

Name of the standby database to be disabled.

Usage Notes

- You cannot specify the name of a primary database.
- Use the `DISABLE CONFIGURATION` command to disable the primary and all standby databases.
- If the sole standby database is disabled, you have no failover option. This standby database is not viable for failover until it is reenabled.
- This command cannot be used to disable the fast-start failover target database when fast-start failover is enabled.

Command Example

Example 1

The following example shows how to disable a database named `South_Sales`.

```
DGMGRL> DISABLE DATABASE 'South_Sales';
Disabled.
```

## DISABLE FAST\_START FAILOVER

Disables fast-start failover and prevents the observer from initiating a failover to the target standby database. See [Section 5.5.5, "Disabling Fast-Start Failover"](sofo.md) for additional information.

Format

DISABLE FAST\_START FAILOVER \[ FORCE \];

Command Parameters

None.

Usage Notes

- If the primary and target standby database have a network connection, use `DISABLE FAST_START FAILOVER` without the `FORCE` option to disable fast-start failover on all databases in the broker configuration. If errors occur during the disable operation, the broker returns an error message and stops the disable operation. You may need to reissue the `DISABLE FAST_START FAILOVER` command with the `FORCE` option to override the error conditions and disable fast-start failover on the database to which you are connected. See [Section 5.5.5, "Disabling Fast-Start Failover"](sofo.md) for more information.
- Use `DISABLE FAST_START FAILOVER` with the `FORCE` option when the network between the primary and target standby databases is disconnected or when the database upon which the command is received does not have a connection with the primary database. The `FORCE` option disables fast-start failover on the database to which you are connected, even when errors occur.
- Disabling fast-start failover with the `FORCE` option on a primary database that is disconnected from the observer and the target standby database does not prevent the observer from initiating a fast-start failover to the target standby database.
- You can disable fast-start failover while connected to any database in the broker configuration so long as connectivity exists between that database and the primary.
- If disabled by force at the target standby database and the connection subsequently resumes with the primary database, fast-start failover is disabled on all databases in the configuration.
- Disabling fast-start failover with the `FORCE` option while connected to the primary will disable fast-start failover on the target standby database if there is network connectivity between both databases.

Command Example

Example 1

The following example shows how to disable fast-start failover.

```
DGMGRL> DISABLE FAST_START FAILOVER;
Disabled.
```

## DISABLE FAST\_START FAILOVER CONDITION

Allows a user to remove conditions for which a fast-start failover should be performed.

Format

DISABLE FAST\_START FAILOVER CONDITION value;

Command Parameters

value

Possible values are those described in the `SHOW FAST_START FAILOVER` command as Health Conditions or Oracle error numbers.

Usage Notes

An error will be raised if the condition is not recognized or if it has not been set.

Command Example

Example 1

```
DISABLE FAST_START FAILOVER CONDITION "Corrupted Controlfile";
```

This specifies that the detection of a corrupted controlfile does not automatically initiate an immediate fast-start failover.

Example 2

```
DISABLE FAST_START FAILOVER CONDITION 27102;
```

This specifies that the `ORA-27102` error does not automatically initiate an immediate fast-start failover.

## EDIT CONFIGURATION (Property)

Changes the value of a property for the broker configuration.

Format

EDIT CONFIGURATION SET PROPERTY property-name = value;

Command Parameter

property-name

The name of a configuration property.

value

The new value for the property.

See Also:

[Chapter 4](dbresource.md) and [Chapter 8](dbpropref.md) for information about configuration properties

Usage Notes

- Issue this command while connected to the primary database or to any standby database in the broker configuration having connectivity to the primary database.
- Use the `SHOW CONFIGURATION` command to display the current property information for the configuration.

Command Example

Example 1

The following example shows how to set the `FastStartFailoverThreshold` configuration property to 90 seconds.

```
DGMGRL> EDIT CONFIGURATION SET PROPERTY FastStartFailoverThreshold=90;
```

## EDIT CONFIGURATION (Protection Mode)

Edits the current protection mode setting for the broker configuration.

Format

EDIT CONFIGURATION SET PROTECTION MODE AS protection-mode;

Command Parameter

protection-mode

The data protection mode in which you want the configuration to run when the configuration is enabled. The possible protection modes are:

  
`MAXPROTECTION`  
`MAXAVAILABILITY`  
`MAXPERFORMANCE`

Usage Notes

- Before you use the `EDIT CONFIGURATION` command to set the protection mode to either the `MAXPROTECTION` or `MAXAVAILABILITY` mode, ensure that at least one standby database has its `LogXptMode` database property set to `SYNC`.
- The following table shows the configuration protection modes and the minimum corresponding settings for redo transport services:
	| Protection Mode | Redo Transport | Standby Redo Log Files Needed? | Usable with Fast-Start Failover? |
	| --- | --- | --- | --- |
	| `MAXPROTECTION` | `SYNC` | Yes | No |
	| `MAXAVAILABILITY` | `SYNC` | Yes | Yes |
	| `MAXPERFORMANCE` | `ASYNC` | Yes | Yes |
	The default protection mode for the configuration is `MAXPERFORMANCE`.
	See Also:
	[Chapter 4](dbresource.md) for more information about the protection modes and redo transport services
- `MAXAVAILABILITY` or `MAXPERFORMANCE` is required in order to enable fast-start failover.
- This command cannot be executed if fast-start failover is enabled.
- After you change the protection mode, the broker will automatically restart the primary database, if necessary.
- Use the `SHOW CONFIGURATION` command to display the current protection mode for the configuration.
	```
	DGMGRL> SHOW CONFIGURATION;
	 
	Configuration - DRSolution
	 
	  Protection Mode: MaxPerformance
	  Databases:
	    North_Sales  - Primary database
	    South_Sales     - Physical standby database
	 
	Fast-Start Failover: DISABLED
	 
	Configuration Status:
	SUCCESS
	```

If broker management of the configuration is disabled when you enter the `EDIT CONFIGURATION` command, the protection mode of the configuration does not take effect until the next time you enable the configuration with the ENABLE CONFIGURATION command.

Command Example

Example 1

The following example shows how to upgrade the broker configuration to the `MAXAVAILABILITY` protection mode.

Verify that standby redo log files are configured on the standby database and that the redo transport service is set to `SYNC`, for example:

```
DGMGRL> EDIT DATABASE 'South_Sales' SET PROPERTY 'LogXptMode'='SYNC';
Property "LogXptMode" updated
 
DGMGRL> EDIT CONFIGURATION SET PROTECTION MODE AS MAXAVAILABILITY;
Succeeded.
```

## EDIT DATABASE (Property)

Changes the value of a property for the named database.

Format

EDIT DATABASE database-name

SET PROPERTY property-name = value;

Command Parameters

database-name

The name of the database for which you want to change a property value.

property-name

The name of an existing database-specific property. If this is an Oracle RAC database, this property change affects all instances of the database.

See Also:

[Chapter 4](dbresource.md) and [Chapter 8](dbpropref.md) for information about properties.

value

The new value for the property.

Caution:

This command can be used to change the value of an instance-specific property if and only if just one instance is known by the broker for the named database. An attempt to use this command to change an instance-specific property when the broker knows of multiple instances of the database will be rejected. It is recommended to only use `EDIT INSTANCE (property)` to change the value of an instance-specific property.

Command Examples

Example 1

Edit a configurable database-specific property at the database level.

```
DGMGRL> EDIT DATABASE 'North_Sales' SET PROPERTY 'ArchiveLagTarget'=1200;
Property "ArchiveLagTarget" updated
```

Example 2

Edit a configurable instance-specific property of a non-Oracle RAC database.

```
DGMGRL> EDIT DATABASE 'South_Sales' SET PROPERTY 
> 'StandbyArchiveLocation'='/archfs/arch/';
Property "StandbyArchiveLocation" updated
```

Example 3

Edit a configurable instance-specific property of an Oracle RAC database. This will not succeed because it is not clear to which instance the property change should be applied.

```
DGMGRL> EDIT DATABASE 'North_Sales' SET PROPERTY
> 'StandbyArchiveLocation'='/archfs/arch/';
Error: ORA-16587: ambiguous object specified to Data Guard broker

Failed.
```

## EDIT DATABASE (Rename)

Changes the name used by the broker to refer to the specified database, as recorded in that database's profile in the broker configuration.

Format

EDIT DATABASE database-name

RENAME TO new-database-name;

Command Parameters

database-name

The name of the database that you want to change.

new-database-name

The name of the new database.

Usage Notes

- Use this command to track changes to the `DB_UNIQUE_NAME` initialization parameter for this database.
	Caution:
	The `database-name` must always match the value for that database's `DB_UNIQUE_NAME` initialization parameter.
- This command can only be done when broker management of the database that you are renaming is disabled.

Command Example

Example 1

The following example shows how to edit and rename a database.

```
DGMGRL> DISABLE DATABASE 'South_Sales_typo';
Disabled.

DGMGRL> EDIT DATABASE 'South_Sales_typo' RENAME TO 'South_Sales';
Succeeded.

DGMGRL> ENABLE DATABASE 'South_Sales';
Enabled.
```

## EDIT DATABASE (State)

Changes the state of the specified database.

Format

EDIT DATABASE database-name

SET STATE = state

\[WITH APPLY INSTANCE = instance-name\];

Command Parameters

database-name

The name of the database for which you want to change the state.

state

The state in which you want the database to be running. The possible states are:

  
`TRANSPORT-ON` (primary database only)  
`TRANSPORT-OFF` (primary database only)  
`APPLY-ON` (physical or logical standby database only)  
`APPLY-OFF` (physical or logical standby database only)

instance-name

The name of the instance you want to become the apply instance if this is an Oracle RAC standby database.

Usage Notes

- If the target state is `APPLY-ON` and this database is currently a physical or logical standby database, the optional `WITH APPLY INSTANCE` clause specifies which instance will become the apply instance.
- If the target state is not `APPLY-ON` or if the database is currently in the primary role, the `WITH APPLY INSTANCE` clause is ignored even if it is specified.
- You cannot change the state of a snapshot standby database.
- All instances of an Oracle RAC database are affected by this database state change.

Command Example

The following examples show how to change the state of a database.

Example 1

```
DGMGRL> EDIT DATABASE 'South_Sales' SET STATE='APPLY-ON';
Succeeded.
```

## EDIT INSTANCE (AUTO PFILE)

Sets the name of the initialization parameter file for the specified instance.

Format

EDIT INSTANCE instance-name

\[ON DATABASE database-name\]

SET AUTO PFILE \[= { initialization-file | OFF } \];

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

Example 1

The following example shows how to change the parameter file used to start an instance of a database.

```
DGMGRL> EDIT INSTANCE 'south_sales1' ON DATABASE 'South_Sales' 
> SET AUTO PFILE='initsales1.ora';
Instance 'south_sales1' updated
```

## EDIT INSTANCE (Property)

Changes the value of an instance-specific property for the specified instance(s).

Format

EDIT INSTANCE { {instance-name \[ON DATABASE database-name\] } | {\* ON DATABASE database-name} }

SET PROPERTY property-name = value;

Command Parameters

instance-name

The name of the instance (SID) for which you want to change an instance-specific property's value. If an asterisk is specified for instance-name, the `ON DATABASE` clause must also be specified and this change will be applied to the specified property for each instance associated with that database. See [Chapter 8](dbpropref.md) for the instance-specific properties that can be changed using the `EDIT INSTANCE * ON DATABASE` `database-name` command.

database-name

The name of the database with which the `instance-name` is associated. This must be specified if an asterisk is specified for `instance-name`, or if `instance-name` is not unique across the configuration

property-name

The name of the instance-specific property for which you want to set a new value.

See Also:

[Chapter 4](dbresource.md) and [Chapter 8](dbpropref.md) for information about properties.

value

The new value for the property.

Usage Notes

- The `instance-name` can be unique across the configuration. If `instance-name` is not unique, you must specify both the `database-name` and the `instance-name` to fully identify the instance.
- This command cannot be used to change a database-specific property.

Command Examples

Example 1

Edit an instance-specific property.

```
DGMGRL> EDIT INSTANCE 'north_sales1' ON DATABASE 'North_Sales' 
> SET PROPERTY 'StandbyArchiveLocation'='/archfs/arch/';
Property "StandbyArchiveLocation" updated.
```

Example 2

Edit a database-specific property. This will not be allowed.

```
DGMGRL> EDIT INSTANCE 'north_sales1' ON DATABASE 'North_Sales' 
> SET PROPERTY 'LogXptMode'='SYNC';
Error: ORA-16586: cannot change database property with EDIT INSTANCE command

Failed.
```

Example 3

Change the value of an instance-specific property for all instances of an Oracle RAC database:

```
DGMGRL> EDIT INSTANCE * ON DATABASE 'North_Sales' LogArchiveTrace=4095;
```

## ENABLE CONFIGURATION

Enables the broker to actively manage the broker configuration including all of its databases.

Format

ENABLE CONFIGURATION;

Command Parameters

None.

Usage Notes

- Use this command to enable broker management of the primary database and all standby databases, if these standby database are not explicitly disabled by the user.
- You must connect to the primary database to issue this command.
- By default, broker management of the configuration's databases is enabled in the `TRANSPORT-ON` state with redo transport services turned on at the primary database and `APPLY-ON` with log apply services started at the standby databases. You can change the state of a database using the EDIT DATABASE (State) command, but not when the database or the entire configuration is disabled.
- Use the SHOW CONFIGURATION command to display information about the configuration.

Command Example

Example 1

The following example enables management of a broker configuration.

```
DGMGRL> ENABLE CONFIGURATION;
Enabled.
```

## ENABLE DATABASE

Enables broker management of the specified standby database.

Caution:

Do not issue the `ENABLE DATABASE` command on a standby database that needs to be reinstated. See [Section 5.4.3](sofo.md) for more details.

Format

ENABLE DATABASE database-name;

Command Parameter

database-name

The name of the standby database for which you want to enable broker management.

Usage Notes

- You must connect to the primary database or to an already enabled standby database to issue this command.
- A standby database may have been disabled by the broker as a consequence of a prior failover or switchover operation. See [Section 5.4.3](sofo.md) to understand how the database can be reinstated or re-created.
- By default, broker management of the physical or logical standby database is enabled in the `APPLY-ON` state with log apply services enabled. You can change the state of the standby database using the EDIT DATABASE (State) command, but only when the database is enabled.
- Use the SHOW DATABASE command to display information about the database.
- For an Oracle RAC database, only one instance is required to be started and mounted for this command to succeed.

Command Example

Example 1

The following example shows how to enable a database named `South_Sales`.

```
DGMGRL> ENABLE DATABASE 'South_Sales';
Enabled.
```

## ENABLE FAST\_START FAILOVER

Enables the broker to fail over to a specifically-chosen standby database in the event of loss of the primary database, without requiring you to perform any manual steps to invoke the failover. See [Section 5.5.2, "Enabling Fast-Start Failover"](sofo.md) for complete information.

Format

ENABLE FAST\_START FAILOVER;

Command Parameters

None.

Usage Notes

- The prerequisites described in [Section 5.5.1](sofo.md) must be met before you issue this command to enable fast-start failover.
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
- To enable fast-start failover for a broker configuration with multiple standby databases, the `FastStartFailoverTarget` configuration property on the primary database must be set to point to the desired target standby database. Both the primary database and the target standby database must have:
	- Standby redo logs configured
		- Either the `LogXptMode` database property set to `SYNC` and protection mode set to `MAXAVAILABILITY`, or the `LogXptMode` property set to `ASYNC` and the protection mode set to `MAXPERFORMANCE`
		- Flashback Database enabled on both the primary and standby databases
	Step [2](sofo.md) in [Section 5.5.2](sofo.md) and [Section 8.3.10](dbpropref.md) provide more information about the `FastStartFailoverTarget` configuration property.
- Once you have enabled fast-start failover, you must comply with the restrictions described in [Section 5.5.2.2, "Restrictions When Fast-Start Failover is Enabled"](sofo.md).

Command Example

Example 1

The following example enables fast-start failover.

```
DGMGRL> ENABLE FAST_START FAILOVER;
Enabled.
```

Example 2

The following example shows that fast-start failover was successfully enabled when the configuration is operating in maximum performance mode.

```
DGMGRL> SHOW FAST_START FAILOVER;
 
Fast-Start Failover: ENABLED
 Threshold:           30 seconds
 Target:              South_Sales
 Observer:            (none)
 Lag Limit:           30 seconds
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

## ENABLE FAST\_START FAILOVER CONDITION

Specifies additional conditions for which a fast-start failover should be performed.

Format

ENABLE FAST\_START FAILOVER CONDITION value;

Command Parameters

value

Possible values are those described in the `SHOW FAST_START FAILOVER` command as Health Conditions or Oracle error numbers.

Usage Notes

- Possible values are the set maintained by the database health-check facility or a number corresponding to any ORA-xxxx error.
- While the conditions maintained by the health-check facility are subject to change in the future, some common examples are shown in Table 7-2:
	Table 7-2 Examples of Health Conditions
	| Health Condition | Description |
	| --- | --- |
	| "Datafile Offline" | Data file offline due to a write error. |
	| "Corrupted Controlfile" | Corrupted controlfile. |
	| "Corrupted Dictionary" | Dictionary corruption of a critical database object. |
	| "Inaccessible Logfile" | LGWR is unable to write to any member of a log group due to an I/O error. |
	| "Stuck Archiver" | Archiver is unable to archive a redo log because device is full or unavailable. |
	| Oracle error number (for example, 27102) | If the error number is encountered, a fast-start failover is performed. |
	The following are enabled by default: "Datafile Offline," "Corrupted Controlfile," and "Corrupted Dictionary."
- You can display these configurable conditions with the `SHOW FAST_START FAILOVER` command.

Command Example

Example 1

```
ENABLE FAST_START FAILOVER CONDITION "Corrupted Controlfile";
```

This specifies that a fast-start failover should be done if a corrupted controlfile is detected.

Example 2

```
ENABLE FAST_START FAILOVER CONDITION 27102;
```

This specifies that a fast-start failover should be done if an `ORA-27102` error is raised.

## EXIT

Exits (quits) the command-line interface.

Format

EXIT;

Command Parameters

None.

Usage Notes

- This command has the same effect as the QUIT command.
- A database connection is not required to execute this command. However, if you are connected, this command breaks the connection.

Command Example

Example 1

The following example demonstrates how to exit (quit) the command-line interface.

```
DGMGRL> EXIT;
```

## FAILOVER

Invokes a failover that transitions the named (target) standby database into the role of a primary database. This type of failover is referred to as manual failover. See [Section 5.4, "Manual Failover"](sofo.md) for more information.

Note:

Because a failover results in a transition of a standby database to the primary role, it should be performed when the primary database has failed or is unreachable and cannot be recovered in a timely manner. Failover may or may not result in data loss depending on the protection mode in effect at the time of the failover and whether the target standby database was synchronized with the primary database.

Use the `SWITCHOVER` command if the primary database has not failed and you want the current primary database and a standby database to switch roles with no data loss.

Format

FAILOVER TO database-name

\[ IMMEDIATE \];

Command Parameters

database-name

The name of a physical, logical, or snapshot standby database that you want to fail over to the primary database role.

Usage Notes

- Always try to perform a complete failover first unless Redo Apply has stopped at the failover target due to an `ORA-752` or `ORA-600` `[3020]` error. If one of these errors has occurred, then before proceeding follow the guidelines in "Resolving ORA-752 or ORA-600 \[3020\] During Standby Recovery" in My Oracle Support Note 1265884.1 at `http://support.oracle.com`. An immediate failover should only be performed when a complete failover is unsuccessful or in the error case just noted.
- The specified standby database must be enabled before the primary database fails. However, an enabled standby database that was shut down can be a candidate for the failover operation. In this case, restart the standby database using DGMGRL `STARTUP` command, then issue the `FAILOVER` command.
- The failover operates on the specified standby database and changes its role to a primary database. Bystander standby databases (those not involved in the failover) remain in the standby role.
- Before you issue the `FAILOVER` command, verify that you are connected to the standby database that will become the new primary database. If necessary, issue a CONNECT command to connect to the standby database to which you want to failover.
- If the `FAILOVER` command is issued without any options, the standby database chosen as the failover target applies all unapplied redo it has received before changing to the primary role. This is referred to as a complete failover.
- If the broker configuration is operating in maximum protection mode, a manual failover operation will force the protection mode to be maximum performance. The redo transport service settings are unaffected. You need to restore the desired protection mode for the resulting configuration after the failover operation.
	Note:
	With fast-start failover, the broker preserves the protection mode that was in effect prior to the failover. The broker configuration cannot be in maximum protection mode while fast-start failover is enabled.
- If the `FAILOVER` command is issued with the `IMMEDIATE` option, no attempt is made to apply any unapplied redo that has been received. This option more likely results in lost application data even when standby redo log files are configured on the standby database. Additionally, any remaining standby databases in the configuration cannot function as such until they are reinstated or re-created. See [Section 5.4.3](sofo.md) for more information.
- You can perform a manual failover or set up the broker to perform a fast-start failover. See the ENABLE FAST\_START FAILOVER command for information about allowing the broker to automatically invoke failover, when conditions warrant a failover.
- If fast-start failover is enabled, you can perform a complete manual failover only to the fast-start failover target standby database and only if the fast-start failover target standby database is synchronized with, or within the lag limit of, the primary database, and only when the observer is started. You cannot perform an immediate manual failover when fast-start failover is enabled.
- If Flashback Database was enabled on the former (failed) primary database prior to the failover, the former primary database can be reinstated using the broker's `REINSTATE` command (see the REINSTATE DATABASE command).
	If failover was performed to a physical standby database, any other physical standby databases that were disabled by the failover can be reinstated if Flashback Database was enabled on the standby database and there are sufficient flashback logs available. See [Section 5.4.3, "Reenabling Disabled Databases After a Role Change"](sofo.md) for step-by-step instructions.
- The original primary database can only participate in the configuration as a standby database after it is reinstated or re-created.
	Caution:
	You should shut down the original primary database if it still has any active instances running prior to failing over.
	See Also:
	[Section 5.4.3](sofo.md) about reenabling the original primary database so that it could serve as a standby database to the primary database

Command Examples

Example 1

The following example performs a failover in which the standby database, `South_Sales`, transitions to the primary role:

```
DGMGRL> FAILOVER TO 'South_Sales';
Performing failover NOW, please wait...
Failover succeeded, new primary is "South_Sales"

DGMGRL> SHOW CONFIGURATION;
Configuration - DRSolution
 
  Protection Mode: MaxPerformance
  Databases:
    South_Sales - Primary database
    North_Sales - Physical standby database (disabled)
      ORA-16661: the standby database needs to be reinstated
 
Fast-Start Failover: DISABLED
 
Configuration Status:
WARNING
```

## HELP

Displays online help for the Data Guard command-line interface.

Format

HELP \[topic\];

Command Parameter

topic

The topic for which you want to display help information. If you do not specify a topic, the command lists all of the topics and the format. Valid topics are:

  
`ADD`  
`CONNECT`  
`CONVERT`  
`CREATE`  
`DISABLE`  
`EDIT`  
`ENABLE`  
`EXIT`  
`FAILOVER`  
`HELP`  
`QUIT`  
`REINSTATE`  
`REM`  
`REMOVE`  
`SHOW`  
`SHUTDOWN`  
`START`  
`STARTUP`  
`STOP`  
`SWITCHOVER`

Usage Notes

- A database connection is not required to execute this command.

Command Examples

Example 1

The following example gets help on the `EDIT` commands.

```
DGMGRL> HELP EDIT;
 
Edits a configuration, database, or instance
 
Syntax:
 
  EDIT CONFIGURATION SET PROTECTION MODE AS
    {MaxProtection|MaxAvailability|MaxPerformance};
 
  EDIT CONFIGURATION SET PROPERTY <property name> = <value>;
 
  EDIT DATABASE <database name> SET PROPERTY <property name> = <value>;
 
  EDIT DATABASE <database name> RENAME TO <new database name>;
 
  EDIT DATABASE <database name> SET STATE = <state>
    [WITH APPLY INSTANCE = <instance name>];
 
  EDIT INSTANCE <instance name> [ON DATABASE <database name>]
    SET AUTO PFILE [ = {<initialization file path>|OFF} ];
 
  EDIT INSTANCE <instance name> [ON DATABASE <database name>]
    SET PROPERTY <property name> = <value>;
 
  EDIT INSTANCE * ON DATABASE <database name>
    SET PROPERTY <property name> = <value>;
```

## QUIT

Quits (exits) the Data Guard command-line interface.

Format

QUIT;

Command Parameters

None.

Usage Notes

- This command has the same effect as the EXIT command.
- A database connection is not required to execute this command. However, if you are connected, this command breaks the connection.

Command Example

Example 1

The following example shows how to quit (exit) the command-line interface.

```
DGMGRL> QUIT;
```

## REINSTATE DATABASE

Reinstates a database as a new standby database in the broker configuration for the current primary database.

Format

REINSTATE DATABASE database-name;

Command Parameter

database-name

The name of the database that is to be reinstated in the broker configuration.

Usage Notes

- If the conditions for reinstatement described in [Section 5.5.8](sofo.md) are not satisfied, the reinstatement will fail with an appropriate error status and the specified database will remain disabled.
- If the `database-name` specified is that of the old primary and fast-start failover is enabled, the old primary database will be reinstated as a standby to the new primary, and the fast-start failover environment will be updated to reflect the availability of the new standby database. It will accept redo data from the new primary database and be the target of a fast-start failover should the new primary database fail. Reinstatement occurs automatically if the observer is running unless the `FastStartFailoverAutoReinstate` configuration property is set to `FALSE`.
- This command does not require that fast-start failover be enabled. It can be used to reinstate an old primary database after a complete manual failover has been performed. It can also be used to reinstate a bystander standby database that had been disabled after either a complete or immediate failover.
- Issue this command while connected to any database in the broker configuration, except the database that is to be reinstated.

Command Examples

Example 1

The following example reinstates the `South_Sales` database as a standby database in the broker configuration.

```
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

## REMOVE CONFIGURATION

Removes all of the broker configuration information, including all database profiles, from the Data Guard broker configuration file, and terminates broker management of all of the databases associated with the broker configuration.

Caution:

When you use the `REMOVE CONFIGURATION` command, all profile information is deleted from the Data Guard broker configuration file and cannot be recovered.

Format

REMOVE CONFIGURATION \[ PRESERVE DESTINATIONS \];

Command Parameters

None.

Usage Notes

- When you remove a broker configuration, management of all of the databases associated with that configuration is disabled.
- By default, the command removes the corresponding broker settings of the `LOG_ARCHIVE_DEST_` `n` initialization parameter on the primary database and the `LOG_ARCHIVE_CONFIG` initialization parameters on all databases in the configuration. To preserve these settings, use the `PRESERVE DESTINATIONS` option.
- This command does not remove or affect the actual primary or standby database instances, databases, datafiles, control files, initialization parameter files, server parameter files, or log files of the underlying Data Guard configuration.
- You cannot remove the configuration when fast-start failover is enabled.

Command Example

The following examples show a successful and an unsuccessful `REMOVE CONFIGURATION` command.

Example 1 Successful REMOVE CONFIGURATION Command

The following command shows how to remove configuration information from the configuration file.

```
DGMGRL> REMOVE CONFIGURATION;
Removed configuration
DGMGRL> SHOW CONFIGURATION;
Error: ORA-16532: Data Guard broker configuration does not exist
 
Configuration details cannot be determined by DGMGRL
```

Example 2 Unsuccessful REMOVE CONFIGURATION Command

The following command is unsuccessful because fast-start failover is enabled.

```
DGMGRL> REMOVE CONFIGURATION;
Error: ORA-16654: fast-start failover is enabled
 
Failed.

 
DGMGRL> SHOW CONFIGURATION;
 
Configuration - The SUPER cluster
 
  Protection Mode: MaxAvailability
  Databases:
    North_Sales  - Primary database
    South_Sales  - (*) Physical standby database
 
Fast-Start Failover: ENABLED
 
Configuration status:
SUCCESS
```

## REMOVE DATABASE

Removes the specified standby database's profile from the broker configuration and terminates broker management of the standby database.

Caution:

When you use the `REMOVE DATABASE` command, the database's profile information is deleted from the broker configuration file and cannot be recovered.

Format

REMOVE DATABASE database-name \[ PRESERVE DESTINATIONS \];

Command Parameter

database-name

The name of the standby database whose profile you want to remove from the broker configuration.

Usage Notes

- An error is returned if you specify the name of the primary database in the broker configuration.
- By default, the command removes the corresponding broker settings of the `LOG_ARCHIVE_DEST_` `n` initialization parameter on the primary database and the `LOG_ARCHIVE_CONFIG` initialization parameter on all databases in the configuration. To preserve these settings, use the `PRESERVE DESTINATIONS` option.
- This command cannot be executed if fast-start failover is enabled and database-name specifies the name of the target standby database.

Command Example

Example 1

The following example shows how to remove a database from the Data Guard broker configuration.

```
DGMGRL> SHOW CONFIGURATION;
 
Configuration - The SUPER cluster
 
  Protection Mode: MaxPerformance
  Databases:
    North_Sales  - Primary database
    South_Sales  - Physical standby database
 
Fast-Start Failover: DISABLED
 
Configuration status:
SUCCESS
 
DGMGRL> REMOVE DATABASE 'South_Sales';
Removed database "South_Sales" from the configuration.
 
 
Configuration - The SUPER cluster
 
  Protection Mode: MaxPerformance
  Databases:
    North_Sales  - Primary database
 
Fast-Start Failover: DISABLED
 
Configuration status:
SUCCESS
```

## REMOVE INSTANCE

Removes an instance from an existing database profile in the broker configuration.

Format

REMOVE INSTANCE instance-name

\[ON DATABASE database-name\];

Command Parameters

instance-name

The name of the instance (SID) that you want to remove from the broker configuration.

database-name

The name of the database to which the `instance-name` is associated.

Usage Notes

- In an Oracle RAC database, the broker automatically adds started instances into the corresponding database profile. However, the broker may not automatically remove instances from the database profile. The `REMOVE INSTANCE` command can be used to manually remove any instance that no longer exists from the database profile.
- The `instance-name` can be unique across the configuration. If `instance-name` is not unique, you must specify both the `database-name` and the `instance-name` to fully identify the instance.
- This command is rejected for an instance that is currently active in the broker configuration.
- This command is rejected if this is the only instance currently associated with a database profile.

Command Example

Example 1

The following example shows how to remove an instance of the database.

```
DGMGRL> REMOVE INSTANCE 'south_sales3' ON DATABASE 'South_Sales';
Removed instance "south_sales3" from the database "South_Sales"
```

## SHOW CONFIGURATION

Displays a summary and status of the broker configuration. The summary lists all databases included in the broker configuration and other information pertaining to the broker configuration itself, including the fast-start failover status.

Format

SHOW CONFIGURATION \[VERBOSE | property-name\];

Command Parameters

property-name

The name of the property for which you want to display summary information.

See [Chapter 8, "Data Guard Broker Properties"](dbpropref.md) for complete information about properties.

Usage Notes

- Use the `SHOW CONFIGURATION VERBOSE` command (or the `SHOW FAST_START FAILOVER` command) to show the properties related to fast-start failover.
- You can optionally specify either `VERBOSE` or `property-name`, but not both.

Command Examples

Example 1 Showing a Summary of the DRSolution Configuration

The following example provides a summary of the `DRSolution` configuration for which fast-start failover is disabled.

```
DGMGRL> SHOW CONFIGURATION;
 
Configuration - The SUPER cluster
 
  Protection Mode: MaxPerformance
  Databases:
    North_Sales  - Primary database
    South_Sales  - Physical standby database
 
Fast-Start Failover: DISABLED
 
Configuration status:
SUCCESS
```

Example 2 Showing Detailed Description of the DRSolution Configuration

The following example provides detailed information about the DRSolution configuration, including configuration properties, and fast-start failover-related information:

```
DGMGRL> SHOW CONFIGURATION VERBOSE;
 
Configuration - DRSolution
 
  Protection Mode: MaxAvailability
  Databases:
    North_Sales  - Primary database
    South_Sales  - (*) Physical standby database
 
  (*) Fast-Start Failover target
 
  Properties:
    FastStartFailoverThreshold      = '60'
    OperationTimeout                = '30'
    FastStartFailoverLagLimit       = '30'
    CommunicationTimeout            = '180'
    FastStartFailoverAutoReinstate  = 'TRUE'
    FastStartFailoverPmyShutdown    = 'TRUE'
    BystandersFollowRoleChange      = 'ALL'
 
Fast-Start Failover: ENABLED
 
  Threshold:        180 seconds
  Target:           South_Sales
  Observer:         observer.example.com
  Lag Limit:        30 seconds (not in use)
  Shutdown Primary: TRUE
  Auto-reinstate:   TRUE
 
Configuration Status:
SUCCESS
```

## SHOW DATABASE

Displays information or property values of the specified database and its instances.

Format

SHOW DATABASE \[VERBOSE\] database-name \[property-name\];

Command Parameters

database-name

The name of the database for which you want to display information. The `VERBOSE` keyword, if used, must come before the `database-name` or an error is returned.

property-name

The name of the property for which you want to display a value. If a property name is specified, the output shows only the specified property (not all properties of the database), regardless of whether or not the `VERBOSE` keyword is specified.

See Also:

[Chapter 4](dbresource.md) and [Chapter 8](dbpropref.md) for information about properties.

Usage Notes

- The `SHOW DATABASE` command shows a brief summary of the database. `SHOW DATABASE VERBOSE` shows properties of the database in addition to the brief summary. They both show the status of the database.
- The `SHOW DATABASE VERBOSE` command shows database-specific properties and instance-specific properties. For a non-Oracle RAC database, the values of the instance-specific properties are those of the only instance of the database. For an Oracle RAC database, the values of the instance-specific properties will not be shown, although the property names are still listed. To see the instance-specific values of these properties, use the `SHOW INSTANCE` command.
- The properties that the `SHOW DATABASE VERBOSE` command shows depend on the database role and the configuration composition:
	- For the primary database, properties specific to physical or snapshot standby databases are shown only if there is at least one physical or snapshot standby database in the configuration. The properties specific to logical standby databases are shown only if there is at least one logical standby database in the configuration.
		- For physical and snapshot standby databases, properties specific to logical standby databases are not shown.
		- For logical standby databases, properties specific to physical and snapshot standby databases are not shown.
- This command is rejected if you use the `SHOW DATABASE` `database-name property-name` command to show an instance-specific property in an Oracle RAC database.

Command Examples

Example 1

Shows database information in an abbreviated format.

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

Example 2

Shows database information in an extended format.

```
DGMGRL> SHOW DATABASE VERBOSE 'South_Sales';
 
Database - South_Sales
 
  Role:            PHYSICAL STANDBY
  Intended State:  OFFLINE
  Transport Lag:   0
  Apply Lag:       0
  Real Time Query: OFF
  Instance(s):
    south_sales1
 
  Properties:
    DGConnectIdentifier             = 'South_Sales.example.com'
    ObserverConnectIdentifier       = ''
    LogXptMode                      = 'SYNC'
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

## SHOW FAST\_START FAILOVER

Displays all fast-start failover related information.

Format

SHOW FAST\_START FAILOVER;

COMMAND PARAMETERS

None.

Usage Notes

The `SHOW FAST_START FAILOVER` command shows a summary of the fast-start failover configuration.

Command Example

```
DGMGRL> SHOW FAST_START FAILOVER;
 
Fast-Start Failover: DISABLED
 Threshold:           30 seconds
 Target:              (none)
 Observer:            (none)
 Lag Limit:           30 seconds
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
   ORA-27102: out of memory
```

## SHOW INSTANCE

Displays information or property values for the specified instance.

Format

SHOW INSTANCE \[VERBOSE\] instance-name \[property-name\] \[ON DATABASE database-name\];

Command Parameters

instance-name

The name of the instance for which you want to display information. The `VERBOSE` keyword, if used, must come before the instance name.

property-name

The name of the property for which you want to display a value. If a property name is specified, the output shows only the specified property (not all properties), regardless of whether or not the `VERBOSE` keyword is specified.

See Also:

[Chapter 4](dbresource.md) and [Chapter 8](dbpropref.md) for information about properties.

database-name

The name of the database to which is associated the instance for which you want to show information.

Usage Notes

- The `SHOW INSTANCE` command shows a brief summary of the instance. `SHOW INSTANCE VERBOSE` shows properties of the instance in addition to the brief summary. They both show the status of the instance.
- The `SHOW INSTANCE VERBOSE` command only shows instance-specific properties.
- The properties that the `SHOW INSTANCE VERBOSE` command shows depend on the database role and the configuration composition:
	- For instances of the primary database, properties specific to physical or snapshot standby instances are shown only if there is at least one physical or snapshot standby database in the configuration. The properties specific to logical standby instances are shown only if there is at least one logical standby database in the configuration.
		- For instances of physical or snapshot standby databases, properties specific to logical standby instances are not shown.
		- For instances of logical standby databases, properties specific to physical and snapshot standby instances are not shown.
- The `instance-name` can be unique across the configuration. If `instance-name` is not unique, you must specify both the `database-name` and the `instance-name` to fully identify the instance.

Command Example

Example 1

The following example shows information about a specific instance of a database.

```
DGMGRL> SHOW INSTANCE 'north_sales1';
 
Instance 'north_sales1' of database 'North_Sales'
 
Instance Status:
SUCCESS
```

Example 2

Shows instance information in an extended format.

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
 
Instance Status:
SUCCESS
```

## SHUTDOWN

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

Example 1

The following command shuts down the primary database in normal mode.

```
DGMGRL > SHUTDOWN;

Database closed. 
Database dismounted. 
Oracle instance shut down.
```

## START OBSERVER

Starts the fast-start failover observer.

Format

START OBSERVER \[ FILE=observer\_configuration\_filename \];

Command Parameters

observer\_configuration\_filename

Specifies an explicit directory path and file name on the observer computer.

Usage Notes

- The Oracle Client Administrator kit, or the full Oracle Database Enterprise Edition or Oracle Personal Edition kit must be installed on the observer computer to monitor a broker configuration for which fast-start failover is to be enabled. See [Section 5.5.1](sofo.md) for more information.
- The `START OBSERVER` command must be issued on the observer computer. Once the observer is successfully started, control is not returned to the user until the observer is stopped (for example, by issuing the STOP OBSERVER command from a different client connection). If you want to perform further interaction with the broker configuration, you must connect through another client.
- The observer runs autonomously once it has been successfully started. For this reason, it is recommended that when invoking DGMGRL for the purpose of issuing the `START OBSERVER` command, specify the `-logfile` optional parameter on the command line so that output generated while acting as the observer is not lost. See Section 7.1.1 for more information about this parameter and see [Section 9.5.3](troubleshooting.md) for an example use of the `-logfile` option.
- If a directory path is not specified with the `FILE` parameter, the observer searches the current working directory for the `fsfo.dat` file. If an `fsfo.dat` file is not found and this is the first time the `START OBSERVER` command is issued, the observer creates a `fsfo.dat` file.
- The primary and target standby database `DB_UNIQUE_NAME` initialization parameter and connect identifiers are stored in the `fsfo.dat` configuration file. Oracle recommends you ensure this file is protected from unauthorized access.
- Fast-start failover does not need to be enabled before you issue this command.
	- If fast-start failover is enabled, the observer will retrieve primary and target standby connect identifiers from the broker configuration and begin monitoring the configuration.
		- If fast-start failover is not enabled, the observer continually monitors for when fast-start failover is enabled.
- Only the primary database needs to be running when you issue this command; the standby database that will be the target of a fast-start failover does not need to be running in order for this command to complete successfully.
- Use the `SHOW FAST_START FAILOVER` command, the `SHOW CONFIGURATION VERBOSE` command, or query the `FS_FAILOVER_*` columns in the `V$DATABASE` view on the primary database to see the status of the observer and its host computer.
- The `SHOW FAST_START FAILOVER` command indicates whether the broker configuration believes that an observer has already been started. If the command displays the following, then you can issue the `START OBSERVER` command on any computer to start the observer:
	```
	Observer:       (none)
	```
	If the `SHOW FAST_START FAILOVER` command shows a value for "Observer:", but the observer at that observer location is no longer running for some reason, you can do either of the following:
	- issue the `START OBSERVER` command on the same observer computer where it was started originally, with the observer configuration file used when the observer was first started
		- issue the `STOP OBSERVER` command and then the `START OBSERVER` command on any computer to start the observer
	If the `SHOW FAST_START FAILOVER` command shows a value for "Observer:" and the observer is already running at that location, an attempt to start an observer at that location again will fail with the following error:
	```
	DGM-16954: Unable to open and lock the Observer configuration file
	```
	If the `SHOW FAST_START FAILOVER` command shows a value for "Observer:" and you attempt to start an observer at a different location, the command will fail with the following error:
	```
	ORA-16647: could not start more than one observer
	```
- If the primary and target standby databases stay connected but they lose the connection to the observer, then the primary database goes into an unobserved state. This state is reported by the broker's health check capability.

Command Examples

Example 1

The following example shows how to start the observer.

```
DGMGRL> CONNECT sys@North_Sales.example.com;
Password: password
Connected.
DGMGRL> START OBSERVER;
Observer started
```

Example 2

The following example shows how to start the observer using `CONNECT '/'` so that connection credentials are not visible on the command line:

```
DGMGRL> CONNECT /@North_Sales.example.com;
DGMGRL> START OBSERVER;
Observer started.
```

You must set up Oracle Wallet or SSL to use `CONNECT '/'`. By setting up Oracle Wallet or SSL, you can write a script to securely start and run the observer as a background job without specifying database credentials in the script. When using Oracle Wallet as a secure external password store, be sure to add credentials for both the primary and fast-start failover target standby databases. The database connect string that you specify when adding the credentials for each database must match the `ObserverConnectIdentifer` or `DGConnectIdentifier` database property.

See Also:

[Oracle Database Advanced Security Administrator's Guide](https://docs.oracle.com/cd/E11882_01/network.112/e40393/toc.htm) for more information about Oracle Wallet

## STARTUP

Starts an Oracle database instance with any of the following options:

- `FORCE`: shuts down the current Oracle instance in the `SHUTDOWN` `ABORT` mode before restarting it.
- `RESTRICT`: allows only Oracle users with the `RESTRICTED SESSION` system privilege to connect to the instance.
- `PFILE`: specifies the `PFILE` initialization parameter file to be used when the database instance is started.
- `MOUNT`: mounts the specified database without opening it.
- `OPEN`: mounts and opens the specified database.
- `NOMOUNT`: starts the specified database instance without mounting the database.

Format

STARTUP

\[FORCE\]

\[RESTRICT\]

\[PFILE=filename\]

\[MOUNT | OPEN \[open-options\] | NOMOUNT\];

Command Parameters

filename

The name of the initialization parameter file to be used when starting the database instance. If you do not specify the `PFILE` parameter option, then the default server parameter file (specific to your operating system) is used.

open-options

The mode of access in which you want the specified database to start. The possible modes are:

  
`READ ONLY`  
`READ WRITE`

Usage Notes

- Using the `STARTUP` command with no arguments is equivalent to using the `STARTUP OPEN` command.
- If you do not use the `FORCE` clause when you use the `STARTUP` command and the current database instance is running, an error results. The `FORCE` clause is useful when you are debugging or when error conditions are occurring. Otherwise, it should not be used.
- Use the `RESTRICT` clause to allow only Oracle users with the `RESTRICTED SESSION` system privilege to connect to the instance. Later, you can use the `ALTER SYSTEM` command through SQL\*Plus to disable the restricted session feature.
- If you do not use the `PFILE` clause to specify the initialization parameter file, the `STARTUP` command uses the default server parameter file, if it exists. Otherwise, the `STARTUP` command uses the default initialization parameter file. The default files are platform specific.
	See your operating system-specific documentation for more information about the default parameter files.
- Use the `OPEN` clause to mount and open the specified database.
- The `NOMOUNT` clause starts the database instance without mounting the database. You cannot use the `NOMOUNT` clause with the `MOUNT` or `OPEN` options.

Command Examples

Example 1

The following examples show two different methods for starting a database instance. Each command starts a database instance using the standard parameter file, mounts the default database in exclusive mode, and opens the database.

```
DGMGRL> STARTUP;
DGMGRL> STARTUP OPEN;
```

Example 2

The following command shuts down the current instance, immediately restarts it without mounting or opening the database, and allows only users with restricted session privileges to connect to it.

```
DGMGRL > STARTUP FORCE RESTRICT NOMOUNT;
```

Example 3

The following command starts an instance using the parameter file `testparm` without mounting the database.

```
DGMGRL > STARTUP PFILE=testparm NOMOUNT;
```

Example 4

The following example starts and mounts a database instance, but does not open it.

```
DGMGRL> STARTUP MOUNT;
```

## STOP OBSERVER

Stops the fast-start failover observer.

Format

STOP OBSERVER;

Command Parameters

None.

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

Command Examples

Example 1

The following example stops the observer.

```
DGMGRL> STOP OBSERVER;
```

## SWITCHOVER

A switchover operation is a planned transition in which the primary database exchanges roles with one of the standby databases. When you issue the `SWITCHOVER` command, the current primary database becomes a standby database, and the specified standby database becomes the primary database.

Format

SWITCHOVER TO database-name;

Command Parameter

database-name

The name of the standby database you want to change to the primary database role.

Usage Notes

- If fast-start failover is enabled, you may switch over only to the fast-start failover target standby database.
- The broker verifies that the primary and standby databases are in the following states before starting the switchover:
	- The primary database must be enabled and in the `TRANSPORT-ON` state so redo transport services are started.
		- The standby database must be enabled and in the `APPLY-ON` state, with log apply services started.
- The broker allows the switchover to proceed as long as there are no redo transport services errors for the standby database that you selected to participate in the switchover. However, errors occurring for any other bystander standby database will not prevent the switchover from proceeding.
- Switchover to a logical standby database is not allowed when the configuration is operating in maximum protection mode.
- If the broker configuration is operating in either maximum protection mode or maximum availability mode, the switchover maintains the protection mode even after the operation (described in [Section 5.3.1](sofo.md)). The switchover will not be allowed if the mode cannot be maintained because the target standby database of the switchover was the only standby that satisfied the protection mode requirement.
- If the standby database that is assuming the primary role is a physical standby database, then the old primary database will be restarted after the switchover completes. If the standby database is a logical standby database, then neither the primary database nor the logical standby database is restarted.
- If the standby database that is assuming the primary role is a physical standby database, then the original primary becomes a physical standby database.
- If the standby database that is assuming the primary role is a logical standby database, then the original primary becomes a logical standby database.
- If an Oracle RAC primary database is becoming a physical standby database, all but one instance of the primary database will be shut down before performing the switchover. See [Section 5.3](sofo.md) for details.
- You cannot switchover to a snapshot standby database.
- If the standby database that is assuming the primary role is a logical standby database and there are physical standby databases in the configuration, after the switchover, the physical standby databases will be disabled.
	Caution:
	For this reason, Oracle generally recommends that you specify your physical standby database for switchover instead of your logical standby database. If you must switch over to your logical standby database, see [Section 5.4.3](sofo.md) to re-create your physical standby database.
	If you intend to switch back to the original primary database relatively soon, you may allow the physical and snapshot standbys to remain disabled. Once you have completed the switchover back to the original primary, you may then reenable the physical and snapshot standby databases since they are still viable standbys for the original primary database.

Command Examples

Example 1

The following example shows a successful switchover in which the physical standby database, `South_Sales`, transitions into the primary role.

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

Example 2

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