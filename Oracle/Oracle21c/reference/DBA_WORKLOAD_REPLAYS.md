---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_WORKLOAD_REPLAYS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.127 DBA\_WORKLOAD\_REPLAYS

`DBA_WORKLOAD_REPLAYS` displays all the workload replays that have been performed in the current database.

It also lists replays on which `DBMS_WORKLOAD_REPLAY.GET_REPLAY_INFO()` has been called. Each row contains information about one workload replay.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ID` | `NUMBER` | `NOT NULL` | Internal key for the workload replay |
| `NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the workload replay |
| `DBID` | `NUMBER` | `NOT NULL` | ID of the database in which the workload was replayed |
| `DBNAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the database in which the workload was replayed |
| `DBVERSION` | `VARCHAR2(17)` | `NOT NULL` | Version of the database in which the workload was replayed |
| `PARALLEL` | `VARCHAR2(3)` |  | Indicates whether the database in which the workload was replayed was an Oracle RAC database (`YES`) or a single instance database (`NO`) |
| `DIRECTORY` | `VARCHAR2(128)` | `NOT NULL` | Name of the directory object for the workload replay |
| `CAPTURE_ID` | `NUMBER` |  | ID of the capture (`DBA_WORKLOAD_CAPTURES.ID`) that was replayed. If the replay involves a replay schedule, the `CAPTURE_ID` will be null. |
| `STATUS` | `VARCHAR2(40)` | `NOT NULL` | Current status of the workload replay:  - `PREPARE` - Workload prepare has been started and is waiting for clients to join - `IN PROGRESS` - Workload replay is in progress - `COMPLETED` - Workload replay has successfully completed - `CANCELLED` - Workload replay or the workload prepare has been cancelled - `FAILED` - Workload replay was terminated due to errors encountered. See the `COMMENTS` column for further information. |
| `PREPARE_TIME` | `DATE` |  | Datetime at which the workload prepare started |
| `START_TIME` | `DATE` |  | Datetime when the replay began |
| `END_TIME` | `DATE` |  | Datetime when the replay completed or cancelled; NULL if the replay is still in progress |
| `DURATION_SECS` | `NUMBER` |  | Duration of the workload replay (in seconds) |
| `NUM_CLIENTS` | `NUMBER` | `NOT NULL` | Number of workload replay client processes that were used in this workload replay |
| `NUM_CLIENTS_DONE` | `NUMBER` | `NOT NULL` | Number of workload replay client processes that have finished replay |
| `FILTER_SET_NAME` | `VARCHAR2(128)` |  | Name of the filter set used for the replay |
| `DEFAULT_ACTION` | `VARCHAR2(30)` | `NOT NULL` | Reserved for future use |
| `SYNCHRONIZATION` | `VARCHAR2(9)` |  | Indicates whether recorded transaction semantics should be maintained (`TRUE`) or not (`FALSE`)  When synchronization is on, the commit order observed during the original workload capture will be preserved. Every action that is replayed will be executed only after all of its dependent commits have been executed. Dependent commits are commits that were issued before the given action in the original workload capture.  See Also: `DBMS_WORKLOAD_REPLAY.PREPARE_REPLAY()` in [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS69086) for a detailed explanation of this replay parameter |
| `CONNECT_TIME_SCALE` | `NUMBER` | `NOT NULL` | Connection time scaling factor for captured streams during replay. The value is interpreted as a percentage.The default value of 100 means 100 percent.  See Also: `DBMS_WORKLOAD_REPLAY.PREPARE_REPLAY()` in [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS69086) for a detailed explanation of this replay parameter |
| `THINK_TIME_SCALE` | `NUMBER` | `NOT NULL` | Think time scaling factor for captured streams during replay. It scales the thinking time elapsed between two successive user calls from the same captured stream. The input is interpreted as a percentage. The default value of 100 means 100 percent.  See Also: `DBMS_WORKLOAD_REPLAY.PREPARE_REPLAY()` in [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS69086) for a detailed explanation of this replay parameter |
| `THINK_TIME_AUTO_CORRECT` | `VARCHAR2(5)` |  | Indicates whether the think time should be automatically corrected between calls (`TRUE`) or not (`FALSE`)  A value of `TRUE` reduces think time if replay goes slower than capture.  A value of `FALSE` results in no action.  See Also: `DBMS_WORKLOAD_REPLAY.PREPARE_REPLAY()` in [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS69086) for a detailed explanation of this replay parameter |
| `SCALE_UP_MULTIPLIER` | `NUMBER` | `NOT NULL` | Before the multiple-capture replay, `SCALE_UP_MULTIPLIER` is used to scale up the query part of a workload capture. The queries from each captured session are replayed concurrently as many times as the value of `SCALE_UP_MULTIPLIER`. |
| `USER_CALLS` | `NUMBER` |  | Total number of user calls replayed |
| `DBTIME` | `NUMBER` |  | Accumulated database time (in microseconds) for the replay |
| `NETWORK_TIME` | `NUMBER` |  | Accumulated network time for the replay (in microseconds) |
| `THINK_TIME` | `NUMBER` |  | Accumulated think time (in microseconds) for the replay |
| `PAUSE_TIME` | `NUMBER` |  | The total time (in seconds) that the replay has been paused (by calling the PAUSE\_REPLAY procedure) |
| `PLSQL_CALLS` | `NUMBER` |  | Total number of replayed top-level PL/SQL calls |
| `PLSQL_SUBCALLS` | `NUMBER` |  | Total number of replayed calls for SQL executed from PL/SQL |
| `PLSQL_DBTIME` | `NUMBER` |  | Total amount of database time (in microseconds) from PL/SQL calls |
| `ELAPSED_TIME_DIFF` | `NUMBER` |  | Reserved for future use |
| `REPLAY_DEADLOCKS` | `NUMBER` |  | A workload replay uses either the timing information from the capture files or the commit-based synchronization.  With commit-based synchronization, the capture-time commit order is preserved during replay, and sessions normally wait on the session that is to do the next commit; such waits are classified as “WCR: replay clock” waits.  A replay deadlock occurs if the session that is to do the next commit is itself blocked by a session that is waiting on “WCR: replay clock.” Replay deadlocks are resolved by allowing the blocker to go ahead and commit out of order.  Replay deadlocks are not detected as database deadlocks since “WCR: replay clock” is an idle wait, introduced specifically for DB Replay.  See Also: " [WCR: replay clock](descriptions-of-wait-events.md) " |
| `AWR_DBID` | `NUMBER` |  | Database ID of the AWR snapshots that correspond to this workload replay. For replays that were performed in the current database, this value is equal to the current database's DBID. For replays that were performed in other databases, this value will either be NULL or will be populated by `DBMS_WORKLOAD_REPLAY.IMPORT_AWR()`.  See Also: DBMS\_WORKLOAD\_REPLAY.IMPORT\_AWR() in [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS69081) |
| `AWR_BEGIN_SNAP` | `NUMBER` |  | Begin snapshot ID of the AWR snapshots that correspond to this workload replay |
| `AWR_END_SNAP` | `NUMBER` |  | End snapshot ID of the AWR snapshots that correspond to this workload replay |
| `AWR_EXPORTED` | `VARCHAR2(12)` |  | Indicates whether the AWR snapshots that correspond to this workload replay have been exported using `DBMS_WORKLOAD_REPLAY.EXPORT_AWR()` (`YES`) or not (`NO`), or whether AWR snapshots cannot be exported because the replay is still in progress, has run to completion successfully, or was done in a different database from which it was not exported (`NOT POSSIBLE`)  See Also: DBMS\_WORKLOAD\_REPLAY.EXPORT\_AWR() in [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS69077) |
| `ERROR_CODE` | `NUMBER` |  | Error code for this workload replay |
| `ERROR_MESSAGE` | `VARCHAR2(512)` |  | Error message for this workload replay |
| `DIR_PATH` | `VARCHAR2(4000)` | `NOT NULL` | Full directory path for the replay directory object |
| `REPLAY_DIR_NUMBER` | `NUMBER` |  | A hash value computed based on the values of other columns in this view, such as the `NAME`, `DBID`, `DBNAME`, `PREPARE_TIME`, `START_TIME`, and `END_TIME` columns. It should be fairly unique for any replay. The value is used to create a subdirectory under the replay directory. |
| `SQLSET_OWNER` | `VARCHAR2(128)` |  | User name of the SQL tuning set owner |
| `SQLSET_NAME` | `VARCHAR2(128)` |  | Name of the SQL tuning set for this workload replay |
| `SCHEDULE_NAME` | `VARCHAR2(128)` |  | The name of a schedule to be replayed. It defines one or multiple workload captures, and the order to start their replays.  If `SCHEDULE_NAME` is `NULL`, the replay is a regular replay introduced since Oracle Database 11g, done with existing APIs from `DBMS_WORKLOAD_REPLAY`: `INITIALIZE_REPLAY`, `PREPARE_REPLAY`, and `START_REPLAY`.  If `SCHEDULE_NAME` is not `NULL`, the replay is a new consolidated replay introduced in Oracle Database 12c. That is, it is a replay of one or more workload captures done with new APIs at `DBMS_WORKLOAD_REPLAY`: `INITIALIZE_CONSOLIDATED_REPLAY`, `PREPARE_CONSOLIDATED_REPLAY`, and `START_CONSOLIDATED_REPLAY`.  See Also: `DBMS_WORKLOAD_REPLAY` in [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS208) |
| `DIVERGENCE_LOAD_STATUS` | `VARCHAR2(5)` |  | Indicates whether replay divergence data have been loaded (`TRUE`) or not (`FALSE`) |
| `PLSQL_MODE` | `VARCHAR2(12)` |  | Replay options for PL/SQL calls. Possible values:  - `TOP_LEVEL`: Top-level PL/SQL only - `EXTENDED`: SQL executed from PL/SQL or top-level PL/SQL if there is no SQL recorded inside the PL/SQL |
| `CONNECT_TIME_AUTO_CORRECT` | `VARCHAR2(12)` |  | Indicates whether the waiting time for a new session to be connected is automatically reduced when the replay proceeds faster than its capture. The reduced amount is determined by the elapsed-time difference between the replay and the capture of the slowest session. The default value is true.  There is no impact when the replay proceeds slower than the capture. |
| `RAC_MODE` | `VARCHAR2(19)` |  | Replay options in an Oracle RAC environment:  - `GLOBAL_SYNC`: Synchronization is across all instances. This is the default. 	Database connections from workload replay client (wrc) are done based on connection remapping. - `PER_INSTANCE_CLIENT`: Synchronization is across all instances. 	All database connections from one wrc are connected to only one instance. - `PER_INSTANCE_SYNC`: Synchronization is within one instance. 	All database connections from one wrc are connected to only one instance. |
| `QUERY_ONLY` | `VARCHAR2(1)` |  | Indicates whether only the query-only workload from the current workload capture will be replayed, skipping all the DML/DDL that might update the database (`Y`) or not (`N`) |
| `PDB_LEVEL` | `VARCHAR2(1)` |  | Indicates whether the replay is a PDB-level replay (`Y`) or not (`N`) |
| `NUM_CLIENTS_ABORTED` | `NUMBER` |  | Number of workload replay clients terminated during the replay |
| `PATCH_NAME` | `VARCHAR2(128)` |  | Database workload capture and replay patch name  This column is only populated for backports to Oracle Database 12c Release 1 (12.1) and earlier releases. |
| `DURATION_LIMIT` | `NUMBER(38)` |  | Replay duration limit (in seconds)  If the replay duration limit has not been set, then the value of this column is null. |
| `STATUS_DETAILS` | `VARCHAR2(128)` |  | Provides additional details about the replay status  If additional details are not available, then the value of this column is null. |

See Also:

[Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS208) for more information about the `DBMS_WORKLOAD_REPLAY` package