---
title: Broker
book: Data Guard Broker
doc_id: F31839-04
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/dgbkr/troubleshooting-oracle-data-guard-broker.html
tags:
  - oracle
  - 21c
  - data-guard-broker
---

### Sources of Diagnostic Information

The Oracle Data Guard broker provides information about its activities in several forms.

- Database status information (see [Database Status](managing-oracle-data-guard-broker-configuration-members.md))
- Oracle alert log files
	The broker records key information in the alert log file for each instance of each database in a broker configuration. You can check the alert log files for such information when troubleshooting Oracle Data Guard.
- Oracle Data Guard "broker log files"
	For each instance of each database in a broker configuration, the broker DMON process records important behavior and status information in a broker log file, useful in diagnosing Oracle Data Guard failures. The `TraceLevel` configuration property (see [TraceLevel](oracle-data-guard-broker-properties.md)) is used to specify the level of diagnostic information reported in the broker log files.
	The broker log file is created in the same directory as the alert log and is named `drc<$ORACLE_SID>.log`.

### General Problems and Solutions

These topics describe general problems and solutions when using Oracle Data Guard broker.

- ORA-16596: database not part of the Oracle Data Guard broker configuration
- Redo Accumulating on the Primary Is Not Sent to Some Standby Databases
- Many Log Files Are Received on a Standby Database But Not Applied
- The Request Timed Out or Cloud Control Performance Is Sluggish
- The Primary Database is Flashed Back
- Standby Fails to Automatically Start Up Due to Unknown Service (ORA-12514)

#### ORA-16596: database not part of the Oracle Data Guard broker configuration

A request was issued to the broker, but the database instance through which you have connected is no longer a part of the broker configuration.

Solution

Reconnect to the configuration through another database that you know is part of the broker configuration. Confirm that a database exists in the broker configuration that has a name that matches the `db_unique_name` value of the database that returned the ORA-16596 error.

This problem can also occur if you attempt to enable a configuration, but the broker configuration file for one of its databases was accidentally removed or is outdated. In this case, remove the database from the broker configuration, manually delete the configuration file for that standby database (not for the primary database), and try again to enable the configuration. After the configuration is enabled, you can either use the Cloud Control Add Standby Database wizard and choose the Add existing standby database option, or you can use the DGMGRL command-line interface and issue the `ADD DATABASE ` command.

#### Redo Accumulating on the Primary Is Not Sent to Some Standby Databases

By viewing the Log File Details page in Cloud Control, you have determined that log files are accumulating on the primary database and are not being archived to some of the standby databases in the broker configuration.

Solution

To narrow down the problem, do the following:

- Verify that the state of the primary database is in the `TRANSPORT-ON` state (not `TRANSPORT-OFF`).
- Verify that the value of the `LogShipping` database property of the standby database in question is `ON`.
- Check the status of the redo transport services on the primary database using the `LogXptStatus` monitorable property. If redo transport services have an error, then use the error message to determine further checking and resolution action. For example:
	- If the error indicates the standby database is not available, you need to restart the standby database.
		- If the error indicates no listener, you need to restart the listener.
		- If the error indicates the standby database has no local destination, you need to set up a standby location to store archived redo log files from the primary database.

#### Many Log Files Are Received on a Standby Database But Not Applied

By viewing the Performance page or Log File Details page in Cloud Control, you have determined that the standby database accumulates too many log files without applying them.

Solution

There are many possible reasons why archived redo log files might not be applied to the standby database. Investigate why the log files are building up and rule out the valid reasons.

If the current status of the standby database is not normal:

- Determine whether or not the log apply services might be unexpectedly stopped. See the ORA-16766 (for physical standby databases) or ORA-16768 (for logical standby databases) error description and solution statement for more help.
- If this is a logical standby database, check to see if a failed transaction has occurred.
- If you want to suppress the error while you investigate the problem, you can temporarily disable broker management of the database.
	See Also:
	[Oracle Data Guard Command-Line Interface Reference](oracle-data-guard-broker-commands.md) for additional information about disabling the database using the DGMGRL command-line interface

If the current status of the standby database is normal:

- Verify the state of the standby database is `APPLY-ON` (not in the `APPLY-OFF` state).
- Verify the state of the primary database is `TRANSPORT-ON` (not in the `TRANSPORT-OFF` state).
	See Also:
	[Oracle Data Guard Broker Properties](oracle-data-guard-broker-properties.md) for additional information about the `LogShipping` database property
- Check to see if log files are building up because the value of the `DelayMins` property is set too large. (Log apply services will delay applying the archived redo log files on the standby database for the number of minutes specified.)
	See Also:
	[Oracle Data Guard Broker Properties](oracle-data-guard-broker-properties.md) for additional information about the `DelayMins` database property
- If you cannot see any errors, compare the archive rate to the apply rate on the Performance page in Cloud Control to see if the apply rate is lower than the archive rate.

#### The Request Timed Out or Cloud Control Performance Is Sluggish

If the broker requests are not completing within the normal timeout parameters, try these actions to solve the problem.

1. Verify the network is operating appropriately.
2. Try to ping all of the nodes in the configuration.
3. Try reconnecting through another database to retry the operation.
4. Run the `VERIFY` command to determine on which database the broker is unable to process the requests.

#### The Primary Database is Flashed Back

If the primary database is flashed back, then the standby databases in the configuration must be also be flashed back or re-created to be viable targets for switchovers or failovers.

The broker will report errors for the standby databases if the primary database has been flashed back.

For more information about restoring the viability of a standby database that was disabled by the broker, see [Reenabling Disabled Databases After a Role Change](using-data-guard-broker-to-manage-switchovers-failovers.md).

#### Standby Fails to Automatically Start Up Due to Unknown Service (ORA-12514)

An `ORA-12514` error may be generated if the DGMGRL CLI fails to automatically start up an instance after a broker operation (for example, a switchover, reinstatement, or convert to physical standby).

The full error text is `ORA-12514: TNS:listener does not currently know of service requested in connect descriptor`. If you receive this error, and your database is not managed by Oracle Clusterware, then you must manually start the instance to complete or continue the broker operation.

Note:

The troubleshooting information in this section applicable only to databases that are not managed by Oracle Clusterware.

You can restart the instance before or after completing the following steps:

1. Issue the following DGMGRL CLI command to check the value of the `StaticConnectIdentifer` configurable property for the instance the DGMGRL CLI was unable to restart. (You will have to connect to another running instance to issue this command):
	```
	SHOW DATABASE db_unique_name StaticConnectIdentifier;
	```
2. The static service name specified in the value of the `StaticConnectIdentifer` instance property should be registered with the listener specified in the property value. The default value for the static service name is of the following form:
	```
	db_unique_name_DGMGRL.db_domain
	```
	See [Prerequisites](oracle-data-guard-broker-installation-requirements.md) for more information about this, and other prerequisites, for using the broker.
3. Confirm that the static service name is registered with the listener specified in the `StaticConnectIdentifer` configurable property value by using the Listener Control utility's status command. If the static service name is properly registered with the listener, it will be included in the output generated by the following command:
	```
	lsnrctl status
	```

### Troubleshooting Problems During a Switchover Operation

If the switchover fails due to problems with the configuration, then the broker reports any problems it encounters in the alert log files or in the broker log files.

See Sources of Diagnostic Information for more information about log files. If the reported problems can be corrected, you can retry the switchover operation and it will usually succeed. If the reported problems cannot be corrected or the switchover operation fails even after correcting the reported problems, then you can choose another database for the switchover or restore the configuration to its pre-switchover state and then retry the switchover.

If fast-start failover is enabled, the broker does not allow switchover to any standby database except to the target standby database. In addition, switchover to the target standby database is allowed only when the value of the `FS_FAILOVER_STATUS` column in the `V$DATABASE` view on the target standby database is either `READY` or `SUSPENDED`.

### Troubleshooting Problems During a Failover Operation

Although it is possible for a failover operation to fail, it is unlikely. If an error does occur there are guidelines you can follow to fix the problem and then retry the broker failover.

#### Failed Failovers to Physical Standby Databases

These steps describe how to recover from a failed broker failover to a physical standby database.

##### Failed Broker Complete Physical Failovers

Examine the alert log file and the broker log file (drc\*.log) on the target standby database to determine the cause of the failure and correct the problem.

If the reported problem can be corrected, then retry the failover operation. If the reported problem cannot be corrected or if the failover operation fails again after the reported problem has been corrected, then take the following steps:

1. Connect to the target standby database and disable fast-start failover using the `FORCE` option if it is enabled.
2. Then you can either:
	- Connect to another physical standby database and attempt a broker complete failover.
		- Perform a broker immediate failover to the target physical standby database.
3. Reinstate the original primary database and any bystander physical standby databases that are disabled with a status of reinstatement required (`ORA-16661`).
4. Reenable fast-start failover if it was disabled in step 1.

##### Failed Broker Immediate Physical Failovers

Examine the alert log file and the broker log file (drc\*.log) on the target standby database to determine the cause of the failure and correct the problem.

If the problem can be corrected, retry the broker immediate failover. Otherwise connect to another physical standby database and attempt either a broker complete or immediate failover.

#### Failed Failovers to Logical Standby Databases

These are the steps to follow if a failover to a logical standby database fails.

1. Examine the alert log file and the broker log file (drc\*.log) on the target standby database to determine the cause of the failure and correct the problem.
2. Connect to the target standby database and disable fast-start failover using the `FORCE` option if it is enabled.
3. Retry the broker failover.
4. Reinstate the old primary database. All bystander standby databases will be re-created from a copy of the new primary database.
5. Reenable fast-start failover if it was disabled in step 1.

If broker failover continues to fail, you should stop the broker on all databases in the Oracle Data Guard configuration (set the `DG_BROKER_START` initialization parameter to `FALSE`). Remove the Oracle Data Guard broker configuration files from all databases. Attempt a manual failover using the guidelines for role transitions in [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/dgbkr&id=SBYDB00635).

Note:

You can enable or disable the broker configuration using DGMGRL `ENABLE CONFIGURATION` and `DISABLE CONFIGURATION` commands. You cannot disable the configuration using Cloud Control. You can only enable the configuration using Cloud Control if it was previously disabled using DGMGRL.

### Troubleshooting Problems with the Observer

The observer continuously monitors the fast-start failover environment to ensure the primary database is available.

Installing and starting the observer is an integral part of using fast-start failover. The following sections describe techniques for troubleshooting the observer:

- Problems Because the Observer Has Stopped
- Capturing Observer Actions in the Observer Log File

#### Problems Because the Observer Has Stopped

If the observer host machine crashes, the broker configuration is no longer observed and fast-start failover is no longer possible.

In this case, you may have to move the observer to a new host if the original host machine cannot be repaired in a timely fashion.

1. Issue the DGMGRL `STOP OBSERVER` command to sever the link between the original observer and the broker configuration:
	```
	DGMGRL> STOP OBSERVER;
	Done.
	```
2. Issue the DGMGRL ` SHOW CONFIGURATION VERBOSE` command to verify that the configuration is no longer being observed:
	```
	DGMGRL> SHOW CONFIGURATION VERBOSE;
	 
	Configuration - DRSolution
	 
	  Protection Mode: MaxAvailability
	  Members:
	    North_Sales - Primary database
	    Warning: ORA-16819: fast-start failover observer not started
	 
	    South_Sales - (*) Physical standby database
	    Warning: ORA-16819: fast-start failover observer not started
	 
	(*) Fast-Start Failover target
	 
	Properties:
	  FastStartFailoverThreshold     = '30'
	  OperationTimeout               = '30'
	  TraceLevel                     = 'USER'
	  FastStartFailoverLagLimit      = '30'
	  CommunicationTimeout           = '180'
	  ObserverReconnect              = '0'
	  FastStartFailoverAutoReinstate = 'TRUE'
	  FastStartFailoverPmyShutdown   = 'TRUE'
	  BystandersFollowRoleChange     = 'ALL'
	  ObserverOverride               = 'FALSE'
	  ExternalDestination1           = ''
	  ExternalDestination2           = ''  
	  PrimaryLostWriteAction         = 'CONTINUE'
	  ConfigurationWideService       = 'North_Sales_CFG' 
	Fast-Start Failover: ENABLED
	 
	  Threshold: 30 seconds
	  Target: South_Sales
	  Observer: (none)
	  Lag Limit: 30 seconds (not in use)
	  Shutdown Primary: TRUE
	  Auto-reinstate: TRUE
	  Observer Reconnect: (none)
	  Observer Override: FALSE
	 
	Configuration Status:
	WARNING
	```
3. Note that you do not need to issue the DGMGRL `SHOW CONFIGURATION ` command to verify that the observer has actually stopped. Successful completion of the DGMGRL `STOP OBSERVER` command will allow a new observer to become associated with the configuration.

#### Capturing Observer Actions in the Observer Log File

You can use the `LOGFILE IS` option of the `START OBSERVER` command to capture the activity performed by the observer.

Start DGMGRL and issue the command:

```
DGMGRL> START OBSERVER observer1 IN BACKGROUND LOGFILE IS observer.log CONNECT IDENTIFIER IS North_Sales TRACE_LEVEL IS SUPPORT;
```

When the `LOGFILE IS` clause is used, then all observer output is recorded in the specified file. If a complete path, with file name, is provided, the file is stored in the specified path. If only a file name is provided and the `DG_ADMIN` environment variable is defined, the specified file is stored in the $ `DG_ADMIN/config_ConfigurationSimpleName/log` directory. If the `DG_ADMIN` environment variable is not defined, the file is stored in the current working directory. If `LOGFILE IS` clause is omitted, the log file is stored in the `$DG_ADMIN/config_ConfigurationSimpleName/log` directory using the name observer\_hostname.log. If the `DG_ADMIN` environment variable is not defined, the log file is stored as `observer_hostname.log` in the current working directory. `ConfigurationSimpleName` is the name of the broker configuration.