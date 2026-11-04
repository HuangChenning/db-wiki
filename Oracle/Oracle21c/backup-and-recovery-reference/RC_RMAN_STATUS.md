---
title: Backup and Recovery Reference
book: Database Backup and Recovery Reference
doc_id: F31837-09
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/rcmrf/RC_RMAN_STATUS.html
tags:
  - oracle
  - 21c
  - backup-and-recovery-reference
---

This view contains information about the history of RMAN operations on all databases associated with this recovery catalog. It contains essentially the same information as `V$RMAN_STATUS`, except that it does not contain information about current sessions.

All RMAN operations such as backups, restores, deletion of backups, and so on are logged in this table. The table is organized to show the status of each RMAN session (the invocation of an RMAN client, including all actions taken until the RMAN client exits), operations executed during the session, and recursive operations.

`RC_RMAN_STATUS` also contains the `RSR_KEY`, `PARENT_KEY` and `SESSION_KEY` columns, which do not appear in `V$RMAN_STATUS`.

| Column | Data Type | Description |
| --- | --- | --- |
| `DB_KEY` | `NUMBER` | The primary key for the database. Use this column to join with almost any other catalog view. |
| `DBINC_KEY` | `NUMBER` | The primary key for the database incarnation. |
| `DB_NAME` | `VARCHAR2(8)` | The `DB_NAME` of the database incarnation to which this record belongs. |
| `RECID` | `NUMBER` | The recid of the corresponding row in the control file. |
| `STAMP` | `NUMBER` | The timestamp of the row in the control file. (Because control file records are reused, you must combine the timestamp and recid to get a value unique across all records in `RC_RMAN_STATUS`.) |
| `RSR_KEY` | `NUMBER` | Unique key for this row. |
| `PARENT_KEY` | `NUMBER` | The value of `RSR_KEY` for the parent row of this row. |
| `SESSION_KEY` | `NUMBER` | The value of `RSR_KEY` for the session row associated with this row. Use in joins with `RC_RMAN_BACKUP_JOB_DETAILS`. |
| `ROW_TYPE` | `VARCHAR2(33)` | This is the type of operation represented by this row. Possible values are:  - `SESSION` for rows at level 0 - `COMMAND` for rows at level 1 - `RECURSIVE OPERATION` for rows at level >1 |
| `ROW_LEVEL` | `NUMBER` | The level of this row.  - If `0` then this is a session row, that is, `ROW_TYPE=SESSION` and the row represents an invocation of the RMAN client. - If `1` then this row represents a command entered in the RMAN client and executed. `ROW_TYPE=COMMAND` for rows at level 1. - If `>1` then this row represents a recursive operation, which is a suboperation of an RMAN command such as a control file autobackup performed with a database backup. `ROW_TYPE=RECURSIVE OPERATION` for rows at levels >1. |
| `OPERATION` | `VARCHAR2(33)` | The name of the operation presented by this row. For `SESSION` operations, this column is set to `RMAN`. For `COMMAND` operations, it describes the command executed, such as `BACKUP`, `RESTORE`, `CONFIGURE`, `REPORT` and so on. |
| `STATUS` | `VARCHAR2(33)` | The status of the operation described by this row. Possible values are:  - `COMPLETED` - Job completed successfully - no warnings or errors during execution. - `COMPLETED WITH WARNINGS` - Job completed successfully, but there were some warning messages during execution. For example, a warning message like the following: 	``` 	RMAN-05019: WARNING: no channel of required type allocated to recover copy of datafile1 	``` - `COMPLETED WITH ERRORS` - Job completed successfully, but there were some errors which were overcome using failover features. For example, `RESTORE FAILOVER` or `BACKUP FAILOVER ` was used to schedule the job on another channel. - `FAILED` - Job failed. - `RUNNING` - Job is executing and there are no errors or warnings during execution so far. - `RUNNING WITH ERRORS` - Job is executing with error messages. - `RUNNING WITH WARNINGS` - Job is executing with warning messages. |
| `COMMAND_ID` | `VARCHAR2(33)` | The user-specified ID of the operation. The user can change this using the `SET COMMAND ID` syntax in RMAN. By default, the command ID is set to the time at which RMAN is invoked, in ISO standard format. |
| `MBYTES_PROCESSED` | `NUMBER` | If the operation represented by this row performed some data transfer (such as backing up or restoring data), then this column contains the number of megabytes processed in the operation. Otherwise, this row contains `NULL`. |
| `START_TIME` | `DATE` | The start time for the operation represented by this row. |
| `END_TIME` | `DATE` | The end time for the operation represented by this row. |
| `JOB_KEY` | `NUMBER` | The key of the RMAN session. Identical to `SESSION_KEY`. |
| `INPUT_BYTES` | `NUMBER` | Number of input bytes read. |
| `OUTPUT_BYTES` | `NUMBER` | Number of input bytes written. |
| `OPTIMIZED` | `VARCHAR2(3)` | `YES` if backup optimization was applied during the backup job. Otherwise, `NO`. |
| `OBJECT_TYPE` | `VARCHAR2(80)` | Contains one of the following values: `DATABASE FULL`, `RECOVERY AREA`, `DATABASE INCR`, `DATAFILE FULL`, `DATAFILE INCR`, `ARCHIVELOG`, `CONTROLFILE`, `SPFILE`. |
| `SESSION_RECID` | `NUMBER` | If `ROW_TYPE=SESSION`, that is, this row has no parents and represents an RMAN session, then this column contains `NULL`. Otherwise, it contains the recid of the row representing the session associated with this row. |
| `SESSION_STAMP` | `NUMBER` | If `ROW_TYPE=SESSION`, that is, this row has no parents and represents an RMAN session, then this column contains `NULL`. Otherwise, it contains the timestamp of the row representing the session associated with this row. |
| `OUTPUT_DEVICE_TYPE` | `VARCHAR2(17)` | The type of output device: `DISK`, `SBT_TAPE`, or `*`. An asterisk (`*`) indicates that output was written to multiple device types. |
| `SITE_KEY` | `NUMBER` | Primary key of the Data Guard database associated with the RMAN status information. Each database in a Data Guard environment has a unique `SITE_KEY` value. You can use `SITE_KEY` in a join with the `RC_SITE` view to obtain the `DB_UNIQUE_NAME` of the database. |
| `OSB_ALLOCATED` | `VARCHAR2(3)` | `YES` if this session allocated an SBT channel for Oracle Secure Backup; otherwise, `NO`. |