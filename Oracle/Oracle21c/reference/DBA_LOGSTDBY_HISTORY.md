---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_LOGSTDBY_HISTORY.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.161 DBA\_LOGSTDBY\_HISTORY

`DBA_LOGSTDBY_HISTORY` displays the history of switchovers and failovers in a Data Guard configuration.

It does this by showing the complete sequence of redo log streams processed or created on the local system, across all role transitions. (After a role transition, a new log stream is started and the log stream sequence number is incremented by the new primary database.). This view is for logical standby databases only.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `STREAM_SEQUENCE#` | `NUMBER` |  | Lists the sequence numbers for all log streams created or applied on the local system.  Note: A value of 0 indicates an unknown sequence order; this is reserved for future log streams. |
| `STATUS` | `VARCHAR2(16)` |  | Description of the log stream processing:  - `Past` - The log stream has already been processed - `Immediate Past` - This is the most recently processed log stream; its status is transitioning from `Current` to `Past` - `Current` - The log stream is currently being processed - `Immediate Future` - This is the next log stream to be processed; its status is transitioning from `Future` to `Current` - `Future` - The log stream will be processed |
| `SOURCE` | `VARCHAR2(5)` |  | Describes how the log stream was started:  - `RFS` - The RFS process created the log stream - `User` - A user registered the initial log file for the log stream - `Synch` - A user issued the `ALTER DATABASE START LOGICAL STANDBY APPLY NEW PRIMARY DDL` statement - `Redo` - The log stream information was recorded in the redo log |
| `DBID` | `NUMBER` |  | Database identifier of the primary database that created the log stream |
| `FIRST_CHANGE#` | `NUMBER` |  | Lowest system change number (SCN) in the current log file |
| `LAST_CHANGE#` | `NUMBER` |  | Highest system change number (SCN) in the current log file |
| `FIRST_TIME` | `DATE` |  | Time of the first SCN entry (`FIRST_CHANGE#`) in the current log file |
| `LAST_TIME` | `DATE` |  | Time of the last SCN entry (`LAST_CHANGE#`) in the current log file |
| `DGNAME` | `VARCHAR2(255)` |  | Unique database name (`DB_UNIQUE_NAME`) of the primary database that produced the log stream. See `V$DATAGUARD_CONFIG` to display all database `DB_UNIQUE_NAME` values defined in the Data Guard configuration. |
| `MERGE_CHANGE#` | `NUMBER` |  | SCN that should be used to flashback a failed primary (that created the log stream) or to flashback a bystander logical standby database following a failover, in the context of the associated redo log stream. It is the SCN up to which redo for the associated log stream can be merged safely in all databases using local copies of archived logs received from the primary database. In order to apply changes beyond this following a failover, you will need to fetch and mine the redo logs from the failover target. |
| `PROCESSED_CHANGE#` | `NUMBER` |  | Strict upper bound on the SCN up to which SQL Apply has applied redo records before it switched to a new log stream (either because it was activated and became the primary database, or in the case of a bystander logical standby database where it switched to a new log stream to accommodate a new primary database). |

Note:

In a CDB, this view shows data only when queried in the root.