---
title: Concepts and Administration
book: Data Guard Concepts and Administration
doc_id: F31838-07
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/sbydb/sql-statements-used-by-oracle-data-guard.html
tags:
  - oracle
  - 21c
  - data-guard-concepts-and-administration
---

There are many SQL and SQL\*Plus statements that are useful for performing operations on standby databases in an Oracle Data Guard environment.

See the following topics:

Refer to the [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sbydb&id=SQLRF008) for complete syntax and descriptions of all SQL statements.

See [Initialization Parameters](oracle-initialization-parameters-used-by-oracle-data-guard.md) for a list of initialization parameters that you can set and dynamically update using the `ALTER SYSTEM SET` statement.

### ALTER DATABASE Statements

This table describes `ALTER DATABASE` statements that are relevant to Oracle Data Guard.

Table 18-1 ALTER DATABASE Statements Used in Data Guard Environments

| ALTER DATABASE Statement | Description |
| --- | --- |
| `ACTIVATE [PHYSICAL\|LOGICAL] STANDBY DATABASE FINISH APPLY]` | Performs a failover. The standby database must be mounted before it can be activated with this statement.  Note: Do not use the `ALTER DATABASE ACTIVATE STANDBY DATABASE` statement to failover because it causes data loss. Instead, use the following best practices:  - For physical standby databases, use the `ALTER DATABASE RECOVER MANAGED STANDBY DATABASE` statement with the `FINISH` keyword to perform the role transition as quickly as possible with little or no data loss and without rendering other standby databases unusable. - For logical standby databases, use the `ALTER DATABASE PREPARE TO SWITCHOVER` and `ALTER DATABASE COMMIT TO SWITCHOVER` statements. |
| `ADD` `[STANDBY`\] `LOGFILE  [THREAD ` integer`]  [GROUP ` integer`] ` `filespec` | Adds one or more online redo log file groups or standby redo log file groups to the specified thread, making the log files available to the instance to which the thread is assigned.  See [Add or Drop a Redo Log File Group](managing-oracle-data-guard-physical-standby-databases.md) for an example of this statement. |
| `ADD [STANDBY`\] `LOGFILE` `MEMBER` 'filename' `[REUSE]` `TO` logfile-descriptor | Adds new members to existing online redo log file groups or standby redo log file groups. |
| `[ADD` \| `DROP`\] `SUPPLEMENTAL` `LOG` `DATA {PRIMARY KEY\|UNIQUE INDEX}` `COLUMNS` | This statement is for logical standby databases only.  Use it to enable full supplemental logging before you create a logical standby database. This is necessary because supplemental logging is the source of change to a logical standby database. To implement full supplemental logging, you must specify either the `PRIMARY KEY COLUMNS` or the `UNIQUE INDEX COLUMNS` keyword on this statement. |
| `COMMIT TO SWITCHOVER` | Performs a switchover to:  - Change the current primary database to the standby database role - Change one standby database to the primary database role.  When switching over to a physical standby database, as of Oracle Database 12c Release 1 (12.1), the `COMMIT TO SWITCHOVER` statement has been replaced with the `SWITCHOVER TO` statement. The `COMMIT TO SWITCHOVER` statement is still supported, but Oracle recommends that you use the new `SWITCHOVER TO` statement.  Note: On logical standby databases, you issue the `ALTER DATABASE PREPARE TO SWITCHOVER` statement to prepare the database for the switchover before you issue the `ALTER DATABASE COMMIT TO SWITCHOVER` statement.  See [Performing a Switchover to a Physical Standby Database Using Old Syntax](performing-oracle-data-guard-role-transitions.md) and [Performing a Failover to a Physical Standby Database Using Old Syntax](performing-oracle-data-guard-role-transitions.md) for examples of this statement. |
| `CONVERT TO [[PHYSICAL\|SNAPSHOT] STANDBY] DATABASE` | Converts a physical standby database into a snapshot standby database and vice versa. |
| `CREATE [PHYSICAL\|LOGICAL] STANDBY CONTROLFILE AS '` filename `' [REUSE]` | Creates a control file to be used to maintain a physical or a logical standby database. Issue this statement on the primary database.  See [Create a Control File for the Standby Database](creating-oracle-data-guard-physical-standby.md) for an example of this statement. |
| `DROP [STANDBY] LOGFILE ` logfile\_descriptor | Drops all members of an online redo log file group or standby redo log file group.  See [Add or Drop a Redo Log File Group](managing-oracle-data-guard-physical-standby-databases.md) for an example of this statement. |
| `DROP [STANDBY] LOGFILE MEMBER ` 'filename' | Drops one or more online redo log file members or standby redo log file members. |
| `FAILOVER TO` `target_db_name` | This statement is for physical standby databases only.  It initiates a failover to the specified host database. |
| `[NO]FORCE LOGGING` | Controls whether or not the Oracle database logs all changes in the database except for changes to temporary tablespaces and temporary segments. The `[NO]FORCE LOGGING` clause is required to prevent inconsistent standby databases.  The primary database must at least be mounted (and it can also be open) when you issue this statement. See [Enable Forced Logging](creating-oracle-data-guard-physical-standby.md) for an example of this statement. |
| `GUARD` | Controls user access to tables in a logical standby database. Possible values are `ALL`, `STANDBY`, and `NONE`. See [Controlling User Access to Tables in a Logical Standby Database](managing-oracle-data-guard-logical-standby-databases.md) for more information. |
| `MOUNT` \[`STANDBY DATABASE`\] | Mounts a standby database, allowing the standby instance to receive redo data from the primary instance. |
| `OPEN` | Opens a previously started and mounted database:  - Physical standby databases are opened in read-only mode, restricting users to read-only transactions and preventing the generating of redo data. - Logical standby database are opened in read/write mode. |
| `PREPARE` `TO` `SWITCHOVER` | This statement is for logical standby databases only.  It prepares the primary database and the logical standby database for a switchover by building the LogMiner dictionary before the switchover takes place. After the dictionary build has completed, issue the `ALTER DATABASE COMMIT TO SWITCHOVER` statement to switch the roles of the primary and logical standby databases.  See [Performing a Switchover to a Logical Standby Database](managing-oracle-data-guard-role-transitions.md) for examples of this statement. |
| `RECOVER MANAGED STANDBY DATABASE [ {  DISCONNECT [FROM SESSION] \| PARALLEL n\| NODELAY \| UNTIL CHANGE integer }...]` | This statement starts and controls Redo Apply on physical standby databases. You can use the `RECOVER MANAGED STANDBY DATABASE` clause on a physical standby database that is mounted, open, or closed. See Step 3 in [Start the Physical Standby Database](creating-oracle-data-guard-physical-standby.md) and [Applying Redo Data to Physical Standby Databases](oracle-data-guard-redo-apply-services.md) for examples.  Note: Several clauses and keywords were deprecated and are supported for backward compatibility only. See [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sbydb&id=SQLRF52467) for more information about these deprecated clauses. |
| `RECOVER` `MANAGED` `STANDBY` `DATABASE` `CANCEL` | The `CANCEL` clause cancels Redo Apply on a physical standby database after applying the current archived redo log file.  Note: Several clauses and keywords were deprecated and are supported for backward compatibility only. See [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sbydb&id=SQLRF52467) for more information about these clauses. |
| `RECOVER` `MANAGED` `STANDBY` `DATABASE` `FINISH` | The `FINISH` clause initiates failover on the target physical standby database and recovers the current standby redo log files. Use the `FINISH` clause only in the event of the failure of the primary database. This clause overrides any delay intervals specified.  Note: Several clauses and keywords were deprecated and are supported for backward compatibility only. See [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/sbydb&id=SQLRF52467) for more information about these clauses. |
| `REGISTER [OR REPLACE]  [PHYSICAL\|LOGICAL] LOGFILE ` `filespec` | Allows the registration of manually copied archived redo log files.  Note: Issue this command only after manually copying the corresponding archived redo log file to the standby database. Issuing this command while the log file is in the process of being copied or when the log file does not exist may result in errors on the standby database at a later time. |
| `RECOVER TO LOGICAL STANDBY` new\_database\_name | Instructs apply services to continue applying changes to the physical standby database until you issue the command to convert the database to a logical standby database. See [Convert to a Logical Standby Database](creating-oracle-data-guard-logical-standby.md) for more information. |
| `RESET DATABASE TO INCARNATION ` integer | Resets the target recovery incarnation for the database from the current incarnation to a different incarnation. |
| `SET` `STANDBY` `DATABASE` `TO` `MAXIMIZE ` { `PROTECTION` \| `AVAILABILITY` \| `PERFORMANCE` } | Use this clause to specify the level of protection for the data in your Oracle Data Guard configuration. You specify this clause from the primary database. |
| `START LOGICAL STANDBY APPLY INITIAL` \[scn-value\] \] \[`NEW PRIMARY` dblink\] | This statement is for logical standby databases only.  It starts SQL Apply on a logical standby database. See [Starting SQL Apply](oracle-data-guard-redo-apply-services.md) for examples of this statement. |
| `{STOP\|ABORT} LOGICAL STANDBY APPLY` | This statement is for logical standby databases only.  Use the `STOP` clause to stop SQL Apply on a logical standby database in an orderly fashion. Use the `ABORT` clause to stop SQL Apply abruptly. See [Performing a Failover to a Logical Standby Database](managing-oracle-data-guard-role-transitions.md) for an example of this statement. |
| `SWITCHOVER TO` `target_db_name` | This statement is for physical standby databases only.  It initiates a switchover on the primary database to the specified physical standby database. |

### ALTER SESSION Statements

This table describes the `ALTER SESSION` statements that are relevant to Oracle Data Guard.

Table 18-2 ALTER SESSION Statements Used in Oracle Data Guard Environments

| ALTER SESSION Statement | Description |
| --- | --- |
| `ALTER` `SESSION` \[`ENABLE` \| `DISABLE`\] `GUARD` | This statement is for logical standby databases only.  This statement allows privileged users to turn the database guard on and off for the current session.  See [Modifying a Logical Standby Database](managing-oracle-data-guard-logical-standby-databases.md) for more information. |
| `ALTER SESSION SYNC WITH PRIMARY` | This statement is for physical standby databases only.  This statement synchronizes a physical standby database with the primary database, by blocking until all redo data received by the physical standby at the time of statement invocation has been applied.  See [Forcing Redo Apply Synchronization in a Real-time Query Environment](managing-oracle-data-guard-physical-standby-databases.md) for more information. |

### ALTER SYSTEM Statements

This table describes the `ALTER SYSTEM` statements that are relevant to Oracle Data Guard.

Table 18-3 ALTER SYSTEM Statements Used in Oracle Data Guard Environments

| ALTER SYSTEM Statement | Description |
| --- | --- |
| `ALTER SYSTEM FLUSH REDO TO target_db_name [[NO] CONFIRM APPLY]` | This statement flushes redo data from a primary database to a standby database and optionally waits for the flushed redo data to be applied to a physical or logical standby database.  This statement must be issued on a mounted, but not open, primary database. |