---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/monitor-oracle-data-guard-configuration.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## 18 Monitor an Oracle Data Guard Configuration

### Monitoring Oracle Data Guard Configuration Health Using the Broker

The Oracle data Guard broker issues a health check once a minute and updates the configuration status. To force a health check to occur immediately, run the command `show configuration verbose`.

On a primary database, the health check determines if the following conditions are met.

- Database is in the state specified by the user, as recorded in the broker configuration file
- Database is in the correct data protection mode
- Database is using a server parameter file(`SPFILE`)
- Database is in the `ARCHIVELOG` mode
- Redo transport services do not have any errors
- Database settings match those specified by the broker configurable properties
- Redo transport settings match those specified by the redo transport-related properties of the standby databases
- Current data protection level is consistent with configured data protection mode
- Primary database is able to resolve all gaps for all standby databases

On a standby database, the health check determines whether the following conditions are met.

- Database is in the state specified by the user, as recorded in the broker configuration file
- Database is using a server parameter file (`SPFILE`)
- Database settings match those specified by the broker configurable properties
- Primary and target standby databases are synchronized or within lag limits if fast-start failover is enabled

To identify any warnings on the overall configuration, show the status using the `SHOW CONFIGURATION` command.

```
DGMGRL> show configuration;

Configuration – dg

  Protection Mode: MaxPerformance
  Members:
  tin - Primary database
    can - Physical standby database 

Fast-Start Failover: DISABLED

Configuration Status:
SUCCESS   (status updated 18 seconds ago)
```

If the configuration status is `SUCCESS`, everything in the broker configuration is working properly.

However, if you see a status of `WARNING` or `ERROR`, then something is wrong in the configuration. Additional error messages will accompany the `WARNING` or `ERROR` status that should be used to identify current issues.

The next step is to examine each database in the configuration to narrow down what the specific error is related to.

To identify the warnings on the primary database, get its status using the `SHOW                 DATABASE` command.

```
DGMGRL> show database tin

Database – tin

  Role:               PRIMARY
  Intended State:     TRANSPORT-ON
  Instance(s):
    tin1
    tin2

Database Status:
SUCCESS
```

If the database status is `SUCCESS` then the database is working properly.

However, if you see a status of `WARNING` or `ERROR`, then something is wrong in the database. Additional error messages will accompany the `WARNING` or `ERROR` status that should be used to identify current issues.

Repeat the same `SHOW DATABASE` command on the standby database and assess any error messages.

In addition to the above commands, the broker features a `VALIDATE                 DATABASE` command.

```
DGMGRL> validate database tin

  Database Role:    Primary database
  Ready for Switchover:  Yes

DGMGRL> validate database can;

  Database Role:     Physical standby database
  Primary Database:  tin

  Ready for Switchover:  No
  Ready for Failover:    Yes (Primary Running)

  Capacity Information:
    Database  Instances        Threads        
    tin       2                2              
    can       1                2              
    Warning: the target standby has fewer instances than the
    primary database, this may impact application performance

  Standby Apply-Related Information:
    Apply State:      Not Running
    Apply Lag:        Unknown
    Apply Delay:      0 minutes
```

The `VALIDATE DATABASE` does not provide a `SUCCESS` or `WARNING` status and must be examined to determine if any action needs to be taken.

It is recommended that you run the `VALIDATE DATABASE` command after creating the broker configuration, and before and after any role transition operation.

The `VALIDATE DATABASE` command performs the following checks.

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

#### Detecting Transport or Apply Lag Using the Oracle Data Guard Broker

Given enough resources, in particular network bandwidth, an Oracle Data Guard standby can maintain pace with very high workloads. In cases where resources are constrained, the standby can begin to fall behind, resulting in a transport or apply lag.

A **transport lag** is the amount of data, measured in time, that the standby has not received from the primary.

An **apply lag** is the difference, in elapsed time, between when the last applied change became visible on the standby and when that same change was first visible on the primary.

When using the Data Guard broker, the transport or apply lag can be viewed by using the `SHOW DATABASE` command and referencing the standby database, as shown here.

```
DGMGRL> show database orclsb

Database – orclsb

  Role:               PHYSICAL STANDBY
  Intended State:     APPLY-ON
  Transport Lag:      0 seconds (computed 0 seconds ago)
  Apply Lag:          0 seconds (computed 1 second ago)
  Average Apply Rate: 792.00 KByte/s
  Real Time Query:    ON
  Instance(s):
    orclsb1 (apply instance)
    orclsb2

Database Status:
SUCCESS
```

The broker `TransportDisconnectedThreshold` database property (default of 0 in Oracle Database 11.2, and 30 seconds for Oracle Database 12.1 and later releases) can be used to generate a warning status for a standby when the last communication from the primary database exceeds the value specified by the property. The property value is expressed in seconds.

The following is an example of the warning when a disconnection has occurred.

```
DGMGRL> show database orclsb;

Database – orclsb

  Role:               PHYSICAL STANDBY
  Intended State:     APPLY-ON
  Transport Lag:      0 seconds (computed 981 seconds ago)
  Apply Lag:          0 seconds (computed 981 seconds ago)
  Average Apply Rate: 12.00 KByte/s
  Real Time Query:    OFF
  Instance(s):
    orclsb1 (apply instance)
    orclsb2

  Database Warning(s):
    ORA-16857: member disconnected from redo source for longer than specified threshold
```

The broker also has the following configurable database properties that you can use to generate warnings when a transport or apply lag exceed a user defined value.

- The `ApplyLagThreshold` property generates a warning status for a logical or physical standby when the database's apply lag exceeds the value specified by the property.
	The property value is expressed in seconds. A value of 0 seconds results in no warnings being generated when an apply lag exists. As a best practice, Oracle recommends setting `ApplyLagThreshold` to at least 15 minutes.
- The `TransportLagThreshold` property can be used to generate a warning status for a logical, physical, or snapshot standby when the database's transport lag exceeds the value specified by the property.
	The property value is expressed in seconds. A value of 0 seconds results in no warnings being generated when a transport lag exists. As a best practice, Oracle recommends setting `TransportLagThreshold` to at least 15 minutes.

### Monitoring Oracle Data Guard Configuration Health Using SQL

You can use the queries in the following tables to assess the overall Data Guard configuration health on the primary database and the standby database.

Table 18-1 Primary Database Queries

| Goal | Query | Expected Results |
| --- | --- | --- |
| Check if any remote standby archive destination is getting errors  Check if all remote standby archive destinations is enabled or `VALID` | ``` select sysdate,status,error  from gv$archive_dest_status  where type='PHYSICAL'  and status!='VALID'  or error is not null; ``` | Good health = no rows returned  If the query returns rows, then raise an alert with the returned data. |
| Check if any `NOLOGGING` activity occurred on the primary database in the last day | ``` select file#, name, unrecoverable_change#, unrecoverable_time  from v$datafile  where unrecoverable_time > (sysdate - 1); ``` | Good health = no rows returned  If the query returns rows, then the standby database is vulnerable, and the files listed in the output must be refreshed on the standby. |
| Detect gaps on the standby database | ``` select sysdate,database_mode,recovery_mode, gap_status  from v$archive_dest_status  where type='PHYSICAL'  and gap_status !='NO GAP'; ``` | Good health = no rows returned  If the query returns rows, then there's an existing gap between the primary and the standby database, and you must run the same query on the standby database.  If the output from the primary and standby is identical, then no action is required.  If the output on the standby does not match the output from the primary, then the datafile on the standby should be refreshed. |
| Assess whether any severe Data Guard event occurred in the last day | ``` select *  from v$dataguard_status  where severity in ('Error','Fatal')  and timestamp > (sysdate -1); ``` | Good health = no rows returned  If the query returns rows, then raise an alert with the returned output. |
| FOR SYNC ENVIRONMENTS ONLY:  Assess if running in Maximum Availability mode and configuration is in sync | ``` select sysdate,protection_mode, synchronized, synchronization_status  from v$archive_dest_status  where type='PHYSICAL'  and synchronization_status !='OK'; ``` | Good health = no rows returned  If the query returns rows, then raise an alert with the returned output. |

Table 18-2 Physical Standby Database Queries

| Goal | Query | Expected Results |
| --- | --- | --- |
| Determine if there is a transport lag | ``` select name,value,time_computed,datum_time  from v$dataguard_stats  where name='transport lag'  and value > '+00 00:01:00'; ``` | Good health = no rows returned  If no rows are returned, then this implies that there is no transport lag |
| Determine if there is an apply lag | ``` select name,value,time_computed,datum_time  from v$dataguard_stats  where name='apply lag'  and value > '+00 00:01:00'; ``` | Good health = no rows returned  If no rows are returned, then this implies that there is no apply lag |
| Standby data file check (offline files or files that are not accessible) | ``` select *  from v$datafile_header  where status ='OFFLINE'  or ERROR is not null; ``` | Good health = no rows returned  Any rows returned list the files that have I/O or recovery issues |
| Verify that the Media Recovery Process is currently running | ``` select *  from v$managed_standby  where process like 'MRP%'; ``` | Good health = rows returned  If no rows are returned, then the MRP process is not running |
| Assess whether any severe Data Guard event occurred in the last day | ``` select *  from v$dataguard_status  where severity in ('Error','Fatal')  and timestamp > (sysdate -1); ``` | Good health = no rows returned  If the query returns rows, then raise an alert with the returned output |

### Oracle Data Guard Broker Diagnostic Information

The Oracle Data Guard broker provides information about its activities in several forms.

- Database status information
- Oracle alert log files
	The broker records key information in the alert log file for each instance of each database in a broker configuration.
- Oracle Data Guard broker log files
	For each instance of each database in a broker configuration, the broker DMON process records important behavior and status information in a broker log file, which are useful for diagnosing Oracle Data Guard failures. The Set the `TraceLevel` configuration property to specify the level of diagnostic information reported in the broker log files. The broker log file is created in the same directory as the alert log and is named `drc<$ORACLE_SID>.log`.
- Oracle Data Guard command line (DGMGRL) `logfile` option
	If the DGMGRL command-line interface was started with the `-logfile` optional parameter, then the resulting log file may contain a useful record of past operations and error conditions.

### Detecting and Monitoring Data Corruption

If corrupt data is written to disk, or if a component failure causes good data to become corrupt after it is written, then it is critical that you detect the corrupted blocks as soon as possible.

To monitor the database for errors and alerts:

- Query the `V$DATABASE_BLOCK_CORRUPTION` view that is automatically updated when block corruption is detected or repaired.
- Configure Data Recovery Advisor to automatically diagnose data failures, determine and present appropriate repair options, and perform repair operations at your request.
	Note that Data Recovery Advisor integrates with the Oracle Enterprise Manager Support Workbench (Support Workbench), the Health Monitor, and RMAN.
- Use Data Guard to detect physical corruptions and to detect lost writes.
	Data Guard can detect physical corruptions when the apply process stops due to a corrupted block in the redo steam or when it detects a lost write.
	Use Enterprise Manager to manage and monitor your Data Guard configuration.
	By taking advantage of Automatic Block Media Recovery, a corrupt block found on either a primary database or a physical standby database can be fixed automatically when the Active Data Guard option is used.
- Use SQL\*Plus to detect data file corruptions and inter-block corruptions.
	Run this SQL\*Plus statement:
	```
	sqlplus> ANALYZE TABLE table_name VALIDATE STRUCTURE CASCADE;
	```
	After finding the corruptions, the table can be re-created or another action can be taken.
- An Recovery Manager (RMAN) backup and recovery strategy can detect physical block corruptions.
	A more intensive RMAN check using the following command can detect logical block corruptions.
	```
	RMAN> BACKUP VALIDATE CHECK LOGICAL;
	```