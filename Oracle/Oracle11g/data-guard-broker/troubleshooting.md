---
title: Troubleshooting Data Guard
book: Data Guard Broker
doc_id: E40771-07
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40771/troubleshooting.htm
tags:
  - oracle
  - 11g
  - data-guard-broker
---

## 9 Troubleshooting Data Guard

This chapter describes various errors and how to solve them. It contains the following topics:

## 9.1 Sources of Diagnostic Information

The Data Guard broker provides information about its activities in several forms:

- Database status information (see [Section 4.9](dbresource.md))
- Oracle alert log files
	The broker records key information in the alert log file for each instance of each database in a broker configuration. You can check the alert log files for such information when troubleshooting Data Guard.
- Data Guard "broker log files"
	For each instance of each database in a broker configuration, the broker DMON process records important behavior and status information in a "broker log file," useful in diagnosing Data Guard failures.
	The broker log file is created in the same directory as the alert log and is named `drc<$ORACLE_SID>.log`.

## 9.2 General Problems and Solutions

This section describes general problems and solutions. This section contains the following topics:

- ORA-16596: database not part of the Data Guard broker configuration
- Redo Accumulating on the Primary Is Not Sent to Some Standby Databases
- Many Log Files Are Received on a Standby Database But Not Applied
- The Request Timed Out or Enterprise Manager Performance Is Sluggish
- The Primary Database is Flashed Back
- Standby Fails to Automatically Start Up Due to Unknown Service (ORA-12514)

### 9.2.1 ORA-16596: database not part of the Data Guard broker configuration

A request was issued to the broker, but the database instance through which you have connected is no longer a part of the broker configuration. You may see this error when the broker fails to locate a broker configuration profile for the database upon which it is running.

Solution Reconnect to the configuration through another database that you know is part of the broker configuration. Confirm that a database exists in the broker configuration that has a name that matches the `db_unique_name` value of the database that returned the ORA-16596 error.

This problem can also occur if you attempt to enable a configuration, but the broker configuration file for one of its databases was accidentally removed or is outdated. In this case, remove the database from the broker configuration, manually delete the configuration file for that standby database (not for the primary database), and try again to enable the configuration. After the configuration is enabled, to create a new database profile for the previously deleted standby database, you can either use the Enterprise Manager Add Standby Database wizard and choose the Add existing standby database option, or you can use the DGMGRL command-line interface and issue the `ADD DATABASE` command.

### 9.2.2 Redo Accumulating on the Primary Is Not Sent to Some Standby Databases

By viewing the Log File Details page in Enterprise Manager, you have determined that log files are accumulating on the primary database and are not being archived to some of the standby databases in the broker configuration.

Solution To narrow down the problem, do the following:

- Verify that the state of the primary database is in the `TRANSPORT-ON` state (not `TRANSPORT-OFF`).
- Verify that the value of the `LogShipping` database property of the standby database in question is `ON`.
- Check the status of the redo transport services on the primary database using the `LogXptStatus` monitorable database property. If redo transport services have an error, then use the error message to determine further checking and resolution action. For example:
	- If the error indicates the standby database is not available, you need to restart the standby database.
		- If the error indicates no listener, you need to restart the listener.
		- If the error indicates the standby database has no local destination, you need to set up a standby location to store archived redo log files from the primary database.

### 9.2.3 Many Log Files Are Received on a Standby Database But Not Applied

By viewing the Performance page or Log File Details page in Enterprise Manager, you have determined that the standby database accumulates too many log files without applying them.

Solution There are many possible reasons why archived redo log files might not be applied to the standby database. Investigate why the log files are building up and rule out the valid reasons.

If the current status of the standby database is not normal:

- Determine whether or not the log apply services might be unexpectedly stopped. See the ORA-16766 (for physical standby databases) or ORA-16768 (for logical standby databases) error description and solution statement for more help.
- If this is a logical standby database, check to see if a failed transaction has occurred.
- If you want to suppress the error while you investigate the problem, you can temporarily disable broker management of the database.
	See Also:
	[Chapter 7](dgmgrl.md) for additional information about disabling the database using the DGMGRL command-line interface

If the current status of the standby database is normal:

- Verify the state of the standby database is `APPLY-ON` (not in the `APPLY-OFF` state).
- Verify the state of the primary database is `TRANSPORT-ON` (not in the `TRANSPORT-OFF` state).
	See Also:
	[Chapter 8](dbpropref.md) for additional information about the `LogShipping` database property
- Check to see if log files are building up because the value of the `DelayMins` property is set too large. (Log apply services will delay applying the archived redo log files on the standby database for the number of minutes specified.)
	See Also:
	[Chapter 8](dbpropref.md) for additional information about the `DelayMins` database property
- If you cannot see any errors, compare the archive rate to the apply rate on the Performance page in Enterprise Manager to see if the apply rate is lower than the archive rate.

### 9.2.4 The Request Timed Out or Enterprise Manager Performance Is Sluggish

If the broker requests are not completing within the normal timeout parameters, try the following actions to solve the problem:

1. Verify the network is operating appropriately.
2. Try to ping all of the nodes in the configuration.
3. Try reconnecting through another database to retry the operation.
4. Run the `VERIFY` command to determine on which database the broker is unable to process the requests.

### 9.2.5 The Primary Database is Flashed Back

If the primary database is flashed back, the standby databases in the configuration must be also be flashed back or re-created to be viable targets for switchovers or failovers. The broker will report errors for the standby databases if the primary database has been flashed back.

For more information about restoring the viability of a standby database that was disabled by the broker, see [Section 5.4.3](sofo.md).

### 9.2.6 Standby Fails to Automatically Start Up Due to Unknown Service (ORA-12514)

If the DGMGRL CLI fails to automatically start up an instance after a broker operation (for example, a switchover, reinstatement, convert to physical standby, or upgrade of protection mode to maximum protection mode), and you receive an `ORA-12514: TNS:listener does not currently know of service requested in connect descriptor` error, then you must manually start the instance to complete or continue the broker operation.

You can restart the instance before or after completing the following steps:

1. Issue the following DGMGRL CLI command to check the value of the `StaticConnectIdentifer` configurable property for the instance the DGMGRL CLI was unable to restart. (You will have to connect to another running instance to issue this command):
	```
	DGMGRL> SHOW INSTANCE VERBOSE 'instance_name' ON DATABASE db_unique_name;
	```
2. The static service name specified in the value of the `StaticConnectIdentifer` instance property should be registered with the listener specified in the property value. The default value for the static service name is of the following form:
	```
	db_unique_name_DGMGRL.db_domain
	```
	See [Section 2.2](install.md) for more information about this, and other prerequisites, for using the broker.
3. Confirm that the static service name is registered with the listener specified in the `StaticConnectIdentifer` configurable property value by using the Listener Control utility's status command. If the static service name is properly registered with the listener, it will be included in the output generated by the following command:
	```
	lsnrctl status
	```
4. If you are working in an Oracle RAC environment, you may want to repeat steps 1 and 2 for each instance to ensure that a static service name is properly registered with its respective listener.

## 9.3 Troubleshooting Problems During a Switchover Operation

If the switchover fails due to problems with the configuration, the broker reports any problems it encounters in the alert log files or in the broker log files (see Section 9.1). In general, you can choose another database for the switchover or restore the configuration to its pre-switchover state and then retry the switchover. The following subsections describe how to recover from the most common problems.

If fast-start failover is enabled, the broker does not allow switchover to any standby database except to the target standby database. In addition, switchover to the target standby database is allowed only when the value of the `FS_FAILOVER_STATUS` column in the `V$DATABASE` view on the target standby database is either `READY` or `SUSPENDED`.

See Also:

[Section 5.5.2.1, "When Fast-Start Failover Is Enabled and the Observer Is Running"](sofo.md)

### 9.3.1 Failed Switchovers to Physical Standby Databases

Examine the alert and DRC log files on the original primary and the target standby databases to determine the cause of the failure. The following sections describe the steps necessary to recover from a failed switchover to a physical standby, based on the types of errors contained in the log files:

- Failure to Convert the Original Primary Database
- Failure to Convert Target Physical Standby Database
- Failure to Open New Primary Database

#### 9.3.1.1 Failure to Convert the Original Primary Database

If the broker switchover failed and the `DATABASE_ROLE` column of the `V$DATABASE` view contains a value of `PRIMARY`, take the following steps:

1. Disable fast-start failover if it is enabled.
2. If the old primary database has been closed, open it.
3. Correct the errors reported in the alert and DRC log files.
4. Retry the broker switchover.
5. Reenable fast-start failover if it was disabled in Step 1.

If the `DATABASE_ROLE` column of `V$DATABASE` contains a value of `PHYSICAL STANDBY`, then you can perform either one of the following procedures:

1. Disable fast-start failover if it is enabled.
2. Connect to the new physical standby database (original primary database) and disable the broker configuration.
3. Restart the new physical standby database.
4. Use the `ALTER DATABASE COMMIT TO SWITCHOVER TO PRIMARY DATABASE` SQL statement to convert the new physical standby database back into a primary database.
5. Open the new primary database.
6. Reenable the broker configuration.
7. Reenable fast-start failover if it was disabled in step 1.
8. Reattempt the broker switchover.

OR

1. Disable fast-start failover if it is enabled.
2. Connect to the new physical standby database (original primary database) and remove the broker configuration.
3. Connect to target standby database.
4. Use the `ALTER DATABASE COMMIT TO SWITCHOVER TO PRIMARY DATABASE` SQL statement to complete the switchover to the target physical standby.
5. Open the new primary database.
6. Shut down and restart the new physical standby database.
7. Connect to the new primary database and re-create the broker configuration.
8. Enable the broker configuration.
9. Reenable fast-start failover if it was disabled in step 1.

#### 9.3.1.2 Failure to Convert Target Physical Standby Database

If the broker switchover failed and the `DATABASE_ROLE` column of the `V$DATABASE` view on the target physical standby database contains a value of `PHYSICAL STANDBY`, take the following steps:

1. Disable fast-start failover if it is enabled.
2. Check the alert and DRC log files to see what caused the switchover to fail and correct it. Once the problem has been corrected you can perform either one of the following procedures:
	1. Connect to the new physical standby database and disable the configuration.
		2. Shut down and restart the new physical standby.
		3. Use the `ALTER DATABASE COMMIT TO SWITCHOVER TO PRIMARY DATABASE` SQL statement to convert the new physical standby database back into a primary database.
		4. Reenable the configuration.
		5. Reattempt the switchover.
	OR
	1. Connect to the new physical standby database (original primary database) and remove the broker configuration.
		2. Use the `ALTER DATABASE COMMIT TO SWITCHOVER TO PRIMARY DATABASE` SQL statement to complete the switchover to the target physical standby database. Open the new primary database.
		3. Shut down and restart the new physical standby database.
		4. Connect to the new primary database and re-create the broker configuration.
		5. Enable the broker configuration.
3. Reenable fast-start failover if it was disabled in Step 1.

#### 9.3.1.3 Failure to Open New Primary Database

If the broker switchover failed because the new primary database could not be opened, follow these steps:

1. Disable fast-start failover if it is enabled.
2. Connect to the new physical standby database (original primary database) and remove the broker configuration.
3. Check the new primary database's alert log file to see what prevented the database from opening and correct it, and then open the database.
4. Shut down and restart the new physical standby database.
5. Connect to the new primary database and re-create the broker configuration.
6. Enable the broker configuration.
7. Reenable fast-start failover if it was disabled in Step 1.

### 9.3.2 Failed Switchovers to Logical Standby Databases

Examine the alert and DRC log files on the original primary and the target standby databases to determine the cause of the failure. The following sections describe the steps necessary to recover from a failed switchover to a logical standby, based on the types of errors contained in the log files:

- Failure to Convert Original Primary Database
- Failure to Convert Target Logical Standby Database

#### 9.3.2.1 Failure to Convert Original Primary Database

If the broker switchover failed because there was an error converting the primary database, take the following steps:

1. Disable fast-start failover if it is enabled.
2. Disable the broker configuration.
3. Take the corrective actions described in [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/troubleshooting.htm#SBYDB01415).
	If after taking corrective action, you have:
	- Restored the original primary database to the primary role, take the following steps:
		1. Reenable the broker configuration.
				2. Retry the broker switchover.
	- Manually switched over the target logical standby to a primary database, take the following steps:
		1. Connect to the original primary database and remove the broker configuration.
				2. Connect to the target logical standby database and convert it to a primary database using the `ALTER DATABASE COMMIT TO SWITCHOVER TO PRIMARY` SQL statement.
				3. Connect to the new primary database and re-create the broker configuration.
				4. Enable the broker configuration.
4. Enable fast-start failover if it was disabled in step 1.

#### 9.3.2.2 Failure to Convert Target Logical Standby Database

If the broker switchover failed and the `DATABASE_ROLE` column of the `V$DATABASE` view contains a value of `PRIMARY`, or if the column contains a value of `LOGICAL STANDBY` and you intend to complete the switchover, follow these steps:

1. Disable fast-start failover if it is enabled.
2. Connect to the target logical standby database and disable the broker configuration.
3. Take the corrective actions described in [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/troubleshooting.htm#SBYDB01420).
4. Reenable the broker configuration.
5. Enable fast-start failover if it was disabled in step 1.

### 9.3.3 Additional Problems That May Occur During a Switchover Operation

Problem: The broker switchover fails due to problems with redo transport services.

Solution: Verify the state and status of the primary and standby database by viewing its information on the Enterprise Manager Data Guard Overview page or through the DGMGRL client `SHOW DATABASE` commands.

If using Enterprise Manager, then run the Verify operation after the switchover completes to examine the alert log file of the new primary database and to verify the status of the configuration.

Problem: The switchover may fail during verification checks done by Data Guard broker (for example, redo transport services might return errors on a database that is involved in the switchover).

Solution: Choose another database for the switchover or fix the problem by transporting the archived redo log files.

## 9.4 Troubleshooting Problems During a Failover Operation

Although it is possible for a failover to stop, it is unlikely. If an error occurs, it is likely to happen when the standby database is transitioning to the primary role. Use these guidelines to fix the problem and continue the broker failover.

### 9.4.1 Failed Failovers to Physical Standby Databases

Use the steps below to recover from a failed broker failover to a physical standby database.

#### 9.4.1.1 Failed Broker Complete Physical Failovers

Examine the alert and DRC log files on the target standby database to determine the cause of the failure and correct the problem. If the `ALTER DATABASE RECOVER MANAGED STANDBY DATABASE FINISH` SQL statement returned an error, or if the statement completes successfully but the database could not be converted to a primary database, follow these steps:

1. Connect to the target standby database and disable fast-start failover using the `FORCE` option if it is enabled.
2. Then you can either:
	- Connect to another physical standby database and attempt a broker complete failover.
		- Perform a broker immediate failover to the target physical standby database.
3. Reinstate the original primary database and any bystander physical standby databases that are disabled with a status of reinstatement required (`ORA-16661`).
4. Reenable fast-start failover if it was disabled in step 1.

#### 9.4.1.2 Failed Broker Immediate Physical Failovers

Examine the alert and DRC log files on the target standby database to determine the cause of the failure and correct the problem. If the problem can be corrected, retry the broker immediate failover. Otherwise connect to another physical standby database and attempt either a broker complete or immediate failover.

### 9.4.2 Failed Failovers to Logical Standby Databases

1. Examine the alert and DRC log files on the target standby database to determine the cause of the failure and correct the problem.
2. Connect to the target standby database and disable fast-start failover using the `FORCE` option if it is enabled.
3. Retry the broker failover.
4. Reinstate the old primary database. All bystander standby databases will be re-created from a copy of the new primary database.
5. Reenable fast-start failover if it was disabled in step 1.

If broker failover continues to fail, you should stop the broker on all databases in the Data Guard configuration (set the `DG_BROKER_START` initialization parameter to `FALSE`). Remove the Data Guard broker configuration files from all databases. Attempt a manual failover using the guidelines for role transitions in [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/cd/E11882_01/server.112/e41134/role_management.htm#SBYDB00635).

Note:

You can enable or disable the broker configuration using DGMGRL `ENABLE CONFIGURATION` and `DISABLE CONFIGURATION` commands. You cannot disable the configuration using the Enterprise Manager. You can only enable the configuration using Enterprise Manager if it was previously disabled using DGMGRL.

## 9.5 Troubleshooting Problems with the Observer

The observer continuously monitors the fast-start failover environment to ensure the primary database is available. Installing and starting the observer is an integral part of using fast-start failover. The following sections describe techniques for troubleshooting the observer:

- Problems Starting the Observer
- Problems Because the Observer Has Stopped
- Capturing Observer Actions in the Observer Log File

### 9.5.1 Problems Starting the Observer

Only one observer can be observing the broker configuration at any given time. If you attempt to start a second observer, one of the following errors is returned:

```
ORA-16647: could not start more than one observer
DGM-16954: Unable to open and lock the Observer configuration file
```

Use the DGMGRL `SHOW CONFIGURATION VERBOSE` command to determine the location of the observer that is currently associated with the broker configuration.

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

### 9.5.2 Problems Because the Observer Has Stopped

If the observer host machine crashes, the broker configuration is no longer observed and fast-start failover is no longer possible. In this case, you may have to move the observer to a new host if the original host machine cannot be repaired in a timely fashion. To move the observer, you must stop allowing the first observer to observe this broker configuration, and then start a new observer on another host.

1. Issue the DGMGRL `STOP OBSERVER` command to sever the link between the original observer and the broker configuration:
	```
	DGMGRL> STOP OBSERVER;
	Done.
	```
2. Issue the DGMGRL `SHOW CONFIGURATION VERBOSE` command to verify that the configuration is no longer being observed:
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
	  Observer:         (none)
	  Lag Limit:        30 seconds (not in use)
	  Shutdown Primary: TRUE
	  Auto-reinstate:   TRUE
	 
	Configuration Status:
	SUCCESS
	```
3. Note that you do not need to issue the DGMGRL `SHOW CONFIGURATION` command to verify that the observer has actually stopped. Successful completion of the DGMGRL `STOP OBSERVER` command will allow a new observer to become associated with the configuration.

### 9.5.3 Capturing Observer Actions in the Observer Log File

You can use the DGMGRL `-logfile` option to start the observer, so that all of the troubleshooting actions performed in Section 9.5.1 can be captured in a file. For example:

```
% dgmgrl -logfile observer.log / "start observer"
```

All the observer output is then recorded in a file named `observer.log` in the current working directory where you issued the DGMGRL command. If the specified log file is not accessible, then the observer output is sent to standard output as though a log file had not been specified.

Note that this is not only useful for troubleshooting problems with the observer, but also for troubleshooting problems with fast-start failover in general.