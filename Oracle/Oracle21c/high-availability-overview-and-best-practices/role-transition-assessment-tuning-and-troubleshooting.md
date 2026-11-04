---
title: High Availability Overview and Best Practices
book: High Availability Overview and Best Practices
doc_id: F46646-49
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/haovw/role-transition-assessment-tuning-and-troubleshooting.html
tags:
  - oracle
  - 21c
  - high-availability-overview-and-best-practices
---

## Role Transition, Assessment, and Tuning

With thorough planning, configuration, and tuning, Oracle Data Guard role transitions can effectively minimize downtime and ensure that the database environment is restored with minimal impact on the business.

Using a physical standby database, Oracle MAA testing has determined that switchover and failover times with Oracle Data Guard have been reduced to seconds. This section describes best practices for both switchover and failover. While following best practices, switchover times of approximately 30 seconds for Oracle RAC and less 10 seconds for a single instance database have been observed. Detection time is separate.

### Prerequisite Data Guard Health Check Before Role Transition

Complete the following prerequisites before performing a switchover operation.

#### Every Quarter

Perform the following steps every quarter.

1. Ensure that your Oracle Data Guard configuration is MAA compliant.
	1. Refer to [Oracle Database Configuration Best Practices](oracle-ai-database-configuration-best-practices.md) and [Oracle Data Guard Configuration Best Practices](configure-and-deploy-oracle-data-guard.md) to ensure that all recommended Data Guard configuration practices are in place.
		2. Refer to [Overview of Oracle Multitenant Best Practices](overview-multitenant-best-practices.md) for PDB service recommendations.
2. Run a simple application test, which includes:
	1. Convert existing the standby database to a snapshot standby.
		2. Validate the application connection to the read-write test database as if this was a disaster recovery test. See [Configuring Continuous Availability for Applications](configuring-continuous-availability-applications1.md) for configuration guidance.
3. Test your end-to-end application failover after a Data Guard role transition.
	1. Issue a Data Guard switchover.
		2. Orchestrate the entire application failover.
		3. Switch back is optional.

#### One Month Before Switchover

One month before performing a switchover operation, consult the MOS note “Oracle Database 19c Important Recommended One-off Patches (Doc ID 555.1)” to identify any critical issues that might affect your release.

Also consider suspending or shutting down long running reporting or jobs including monitoring, auditing, and database backups that create persistent connections during the target planned maintenance window that contains the Data Guard switchover operation.

Common configuration issues that impact application service availability while performing a Data Guard role transition with Oracle Multitenant database are:

- PDB saved state or triggers are used and fail during Data Guard role transition
- PDB default service is leveraged instead of using Oracle clusterware-managed distinct services for each PDB for your application service
- Wallet/security settings are not the same on the standby

To ensure application service and application failover readiness:

1. Never use PDB default services, nor `SAVED STATE` (except during relocate operations), nor database triggers to manage role-based services.
2. Use clusterware-managed distinct services on each PDB for your application service, and leverage that application service to connect to the database.
3. When defining a clusterware-managed application service, define which PDB and services will be started, and in which Oracle RAC instance and database role.
4. For Data Guard, always use role-based services by assigning a role to each clusterware-managed service.

Validate Database Switchover and Failover Readiness

You can use the `VALIDATE` command to perform a comprehensive set of database checks before performing a role change. The command checks the following items:

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

The three main `VALIDATE` commands that should be issued prior to switchover are:

1. `VALIDATE DATABASE VERBOSE standby` - The `VALIDATE DATABASE` command shows a brief summary of the database, and reports any errors or warnings that were detected. `VALIDATE DATABASE VERBOSE` shows everything in the brief summary plus all items that were validated.
2. `VALIDATE DATABASE standby SPFILE` - The `VALIDATE DATABASE SPFILE` command reports any parameter differences between primary and the specified standby databases.
3. `VALIDATE NETWORK CONFIGURATION FOR ALL` - The `VALIDATE                         NETWORK CONFIGURATION` command performs network connectivity checks between members of a configuration.

To summarize how to evaluate Role Transition readiness, review the following:

- `PRIMARY DATABASE` Section:
	- ```
		DGMGRL> VALIDATE DATABASE VERBOSE 'Primary_DBName';
		```
		- Check if there are PDB saved states in the primary database.
		- ```
			SELECT * FROM dba_pdb_saved_states;
			```
		- Evaluate health with `exachk` or `orachk`.
- For each `STANDBY DATABASE                             STANDBY_DB_UNIQUE_NAME` Section:
	- ```
		DGMGRL> VALIDATE DATABASE VERBOSE 'Standby_DBName';
		```
		- ```
		DGMGRL> VALIDATE DATABASE 'Standby_DBName' SPFILE;
		```
		- Evaluate health with `exachk` or `orachk`.
		- Evaluate if the standby cluster and database are symmetric with the primary cluster and database. This ensures identical or similar performance after role transition.
		- Evaluate whether the cluster shape and system resources are the same, spfile memory settings are the same, and number of databases sharing the cluster resources are the same. If not, highlight the differences and evaluate if system resources are available by reviewing `exawatcher` or `oswatcher` graphs.
- Network Section:
	- ```
		DGMGRL> VALIDATE NETWORK CONFIGURATION FOR ALL;
		```
- Redo Rate History Section:
	- ```
		SQL> SELECT thread#,sequence#,blocks*block_size/1024/1024 MB,(next_time-first_time)*86400 sec,
		 blocks*block_size/1024/1024)/((next_time-first_time)*86400) "MB/s"
		 FROM v$archived_log
		 WHERE ((next_time-first_time)*86400<>0) and first_time
		 between to_date('2015/01/15 08:00:00','YYYY/MM/DD HH24:MI:SS')
		 and to_date('2015/01/15 11:00:00','YYYY/MM/DD HH24:MI:SS') and dest_id=1
		 order by first_time;
		```

Example:

The Oracle Data Guard broker `VALIDATE DATABASE` command gathers information related to switchover and failover readiness.

The validation verifies that the standby and primary database are reachable and the apply lag is less than `ApplyLagThreshold` for the target database. If these data points are favorable, the command output displays "Ready for Failover: Yes" as shown below. In addition, if redo transport is running, the command output displays "Ready for Switchover: Yes".

```
DGMGRL> validate database [verbose] database_name

Database Role: Physical standby database
 Primary Database: standby_db_unique_name

Ready for Switchover: Yes
 Ready for Failover: Yes (Primary Running)
```

`VALIDATE DATABASE` checks additional information that can impact switchover time and database performance, such as whether the online redo logs have been cleared, number of temporary tablespaces, parameter mismatches between primary and standby, and the status of flashback databases.

In most failover cases the primary database has crashed or become unavailable. The Ready for Failover output indicates if the primary database is running when `VALIDATE DATABASE` was issued. This state does not prevent a failover, but it is recommended that you stop the primary database before issuing a failover to avoid a split-brain scenario where the configuration has two primary databases. The broker only guarantees split-brain avoidance on failover when Fast-Start Failover is used.

You should also run `VALIDATE DATABASE VERBOSE                     standby`, `VALIDATE DATABASE                         standby SPFILE`, and `VALIDATE NETWORK                     CONFIGURATION FOR ALL` periodically as a configuration monitoring tool.

#### Days Before Switchover

Perform the following steps days before performing a Data Guard switchover.

1. Set the Data Guard broker trace level.
	The Data Guard broker `TraceLevel` configuration property is used to control the amount of tracing performed by the broker for every member in the configuration. Setting the property to `USER` limits the tracing to completed operations and to any warning or error messages resulting from an operation or health check. Setting the property to `SUPPORT` increases the amount of tracing to include lower-level information needed to troubleshoot any issues.
	```
	DGMGRL> EDIT CONFIGURATION SET PROPERTY TraceLevel = SUPPORT;
	```
2. Enable role transition metrics.
	The Time Management Interface (TMI) event is a low overhead event which adds a line to the alert log whenever certain calls are executed in Oracle.
	These entries in the alert log, or tags, delineate the beginning and end of a call. The tables in the topics below depict the delineation of key switchover and failover operations. This method is the most accurate for determining where time is being spent.
	Set the database level event 16453 trace name context forever, level 15 on all databases. There are two methods of enabling this trace, either using the `EVENT` database parameter or setting the `EVENTS` at the system level. The difference is that the `EVENT` parameter is not dynamic but is persistent across restarts. `SET EVENTS` is dynamic but NOT persistent across database restarts. See the following examples.
	```
	ALTER SYSTEM SET EVENT=‘16453 trace name contextforever, level 15’ scope=spfile sid=’*’;
	```
	```
	ALTER SYSTEM SET EVENTS ‘16453 trace name context forever, level 15’;
	```

### Data Guard Role Transition

Always use Oracle Data Guard broker or any Oracle UI or utility that ultimately calls the Data Guard broker command.

Suspend or shut down any long running reports or batch jobs including monitoring, auditing, and database backups that have persistent connections.

Use the Oracle Data Guard broker `SWITCHOVER` command to initiate switchover, and the `FAILOVER` command to initiate failover.

As part of a switchover or failover operation the broker does the following.

- Configures redo transport from the new primary database
- Starts redo apply on the new standby database
- Ensures that other standby databases in the broker configuration are viable and receiving redo from the new primary
- Integrates Oracle Clusterware and Global Data Services to ensure that the role-based services are started

Before issuing the Data Guard switchover, suspend or shut down long running reporting or jobs including monitoring, auditing, and database backups that create persistent connections.

To configure broker to initiate switchover, log in as SYS or SYSDBA and issue:

```
DGMGRL> SWITCHOVER TO database_name;
```

To configure broker to initiate failover, run:

```
DGMGRL> FAILOVER TO database_name [IMMEDIATE];
```

By default `FAILOVER` applies all redo that was received before failing over. The `IMMEDIATE` clause skips the pending redo and fails over immediately.

The `SWITCHOVER` and `FAILOVER` commands are idempotent and can be re-issued in the unlikely event of a failed transition.

### Monitor Data Guard Role Transitions

Refer to the Data Guard Broker messages while the Data Guard role transition is happening. To extract detailed role transition status, refer to the primary and standby alert logs and broker logs for Data Guard switchover and failover messages and tags.

#### Key Switchover Operations and Alert Log Tags

Switchover is broken down into four main steps as follows.

1. `Convert to Standby` - terminate any existing production sessions, convert the control file into a standby control file, and send a message to the standby to continue the switchover.
	The `Convert to Standby` - these steps are found in the alert log of the original primary. All remaining steps are found in the original standby alert log.
2. `Cancel Recovery` - apply remaining redo and stop recovery.
3. `Convert to Primary` - a two-step close (to the mounted state) of instances (one instance, then all others), clear online redo logs, convert control file to primary control file, and data Guard Broker bookkeeping.
4. `Open New Primary` - parallel open of all instances.

Table 17-8 Alert Log Tags Defining the Steps with Time Management Interface Event Enabled

| Step | Stage | Time Management Interface Event Enabled |
| --- | --- | --- |
| Convert To Standby(primary alert log) | BEGIN | TMI: dbsdrv switchover to target BEGIN \<DATE> \<TIMESTAMP> |
| Convert To Standby(primary alert log) | END | TMI: kcv\_switchover\_to\_target send 'switchover to primary' msg BEGIN \<DATE> \<TIMESTAMP> |
| Cancel Recovery(standby alert log) | BEGIN | TMI: kcv\_commit\_to\_so\_to\_primary wait for MRP to die BEGIN \<DATE> \<TIMESTAMP> |
| Cancel Recovery(standby alert log) | END | TMI: kcv\_commit\_to\_so\_to\_primary wait for MRP to die END \<DATE> \<TIMESTAMP> |
| Convert to Primary (standby alert log) | BEGIN | TMI: kcv\_commit\_to\_so\_to\_primary BEGIN CTSO to primary \<DATE> \<TIMESTAMP> |
| Convert to Primary (standby alert log) | END | TMI: adbdrv BEGIN 10 \<DATE> \<TIMESTAMP> |
| Open Primary(standby alert log) | BEGIN | TMI: adbdrv BEGIN 10 \<DATE> \<TIMESTAMP> |
| Open Primary(standby alert log) | END | TMI: adbdrv END 10 \<DATE> \<TIMESTAMP> |

#### Key Failover Operations and Alert Log Tags

All failover steps are documented in the alert log of the target standby where the failover was performed.

1. Cancel Recovery - Stop recovery and close all instances (to mounted) in parallel.
2. Terminal Recovery - Archive standby redo logs and recover any unapplied redo.
3. Convert to Primary - Clear online redo logs and convert control file to standby control file.
4. Open Primary - Open all instances in parallel.

Table 17-9 Failover Alert Log Tags Defining the Steps with Time Management Interface Event Enabled

| Step | Stage | Time Management Interface Event Enabled |
| --- | --- | --- |
| Cancel Recovery | BEGIN | TMI: adbdrv termRecovery BEGIN \<DATE> \<TIMESTAMP> |
| Cancel Recovery | END | TMI: adbdrv termRecovery END \<DATE> \<TIMESTAMP> |
| Terminal Recovery | BEGIN | TMI: krdsmr full BEGIN Starting media recovery \<DATE> \<TIMESTAMP> |
| Terminal Recovery | END | TMI: krdemr full END end media recovery \<DATE> \<TIMESTAMP> |
| Convert to Primary | BEGIN | TMI: kcv\_commit\_to\_so\_to\_primary BEGIN CTSO to primary \<DATE> \<TIMESTAMP> |
| Convert to Primary | END | TMI: adbdrv BEGIN 10 \<DATE> \<TIMESTAMP> |
| Open Primary | BEGIN | TMI: adbdrv BEGIN 10 \<DATE> \<TIMESTAMP> |
| Open Primary | END | TMI: adbdrv END 10 \<DATE> \<TIMESTAMP> |

### Post Role Transition Validation

Use the `SHOW CONFIGURATION VERBOSE` command to verify that the switchover or failover and standby reinstate was successful.

```
DGMGRL> SHOW CONFIGURATION VERBOSE;
Configuration - DRSolution   
Protection Mode: MaxAvailability 
Members:   
         South_Sales  - Primary database     
         North_Sales - Physical standby database
         Fast-Start Failover: DISABLED
         Configuration Status:
          SUCCESS
```

### Troubleshooting Problems During a Switchover Operation

The most important goal after a failed Data Guard switchover or failover operation is to resume database and application availability as soon as possible.

#### Sources of Diagnostic Information

The Oracle Data Guard broker provides information about its activities in several forms.

- Database status information - You can use the `SHOW DATABASE VERBOSE                         db_unique_name` command to get a brief description of the database (name, role, and so on), database status, and information about any health check problems.
	```
	DGMGRL> SHOW DATABASE VERBOSE db_unique_name
	```
- Oracle alert log files - The broker records key information in the alert log file for each instance of each database in a broker configuration. You can check the alert log files for such information when troubleshooting Oracle Data Guard.
- Oracle Data Guard "broker log files" - For each instance of each database in a broker configuration, the broker DMON process records important behavior and status information in a broker log file, useful in diagnosing Oracle Data Guard failures. The `TraceLevel` configuration property is used to specify the level of diagnostic information reported in the broker log files. The broker log file is created in the same directory as the alert log and is named `drc<$ORACLE_SID>.log`.

#### Retry Switchover After Correcting the Initial Problem

If the reported problems can be corrected quickly, you can retry the switchover operation.

If the reported problems cannot be corrected or the switchover operation fails even after correcting the reported problems, then you can choose another database for the switchover or restore the configuration to its pre-switchover state and then retry the switchover or refer to Rolling Back After Unsuccessful Switchover to Maximize Uptime.

```
DGMGRL> SWITCHOVER TO database_name;
```

#### Rolling Back After Unsuccessful Switchover to Maximize Uptime

For physical standby databases in situations where an error occurred, and it is not possible to continue with the switchover in a timely fashion, revert the new physical standby database back to the primary role to minimize database downtime.

Take the following steps.

1. Shut down and mount the new standby database (old primary).
2. Start Redo Apply on the new standby database.
3. Verify that the new standby database is ready to be switched back to the primary role.
	Query the `SWITCHOVER_STATUS` column of the `V$DATABASE` view on the new standby database. A value of `TO PRIMARY` or `SESSIONS ACTIVE` indicates that the new standby database is ready to be switched to the primary role. Continue to query this column until the value returned is either `TO                         PRIMARY` or `SESSIONS ACTIVE`.
4. Issue the following statement to convert the new standby database back to the primary role:
	```
	SQL> ALTER DATABASE SWITCHOVER TO target_db_name;
	```
	If step 4 fails, see [Roll Back After Unsuccessful Switchover and Start Over](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/haovw&id=SBYDB-GUID-97282862-4EA0-42D9-97EF-34E75A29F87F) in