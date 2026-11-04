---
title: DBA_WORKLOAD_REPLAYS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5096.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_WORKLOAD_REPLAYS` displays all the workload replays that have been performed in the current database. It also lists replays on which `DBMS_WORKLOAD_REPLAY.GET_REPLAY_INFO()` has been called. Each row contains information about one workload replay.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ID` | `NUMBER` | `NOT NULL` | Internal key for the workload replay |
| `NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the workload replay |
| `DBID` | `NUMBER` | `NOT NULL` | ID of the database in which the workload was replayed |
| `DBNAME` | `VARCHAR2(10)` | `NOT NULL` | Name of the database in which the workload was replayed |
| `DBVERSION` | `VARCHAR2(128)` | `NOT NULL` | Version of the database in which the workload was replayed |
| `PARALLEL` | `VARCHAR2(3)` |  | Indicates whether the database in which the workload was replayed was an Oracle RAC database (`YES`) or a single instance database (`NO`) |
| `DIRECTORY` | `VARCHAR2(128)` | `NOT NULL` | Name of the directory object for the workload replay |
| `CAPTURE_ID` | `NUMBER` |  | ID of the capture (`DBA_WORKLOAD_CAPTURES.ID`) that was replayed |
| `STATUS` | `VARCHAR2(40)` | `NOT NULL` | Current status of the workload replay: - `PREPARE` - Workload prepare has been started and is waiting for clients to join - `IN PROGRESS` - Workload replay is in progress - `COMPLETED` - Workload replay has successfully completed - `CANCELLED` - Workload replay or the workload prepare has been cancelled - `FAILED` - Workload replay was aborted due to errors encountered. See the `COMMENTS` column for further information. |
| `PREPARE_TIME` | `DATE` |  | Datetime at which the workload prepare started |
| `START_TIME` | `DATE` |  | Datetime when the replay began |
| `END_TIME` | `DATE` |  | Datetime when the replay completed or cancelled; NULL if the replay is still in progress |
| `DURATION_SECS` | `NUMBER` |  | Duration of the workload replay (in seconds) |
| `NUM_CLIENTS` | `NUMBER` | `NOT NULL` | Number of workload replay client processes that were used in this workload replay |
| `NUM_CLIENTS_DONE` | `NUMBER` | `NOT NULL` | Number of workload replay client processes that have finished replay |
| `FILTER_SET_NAME` <sup>Footref 1</sup> | `VARCHAR2(1000)` |  | Name of the filter set used for the replay |
| `DEFAULT_ACTION` | `VARCHAR2(30)` | `NOT NULL` | Reserved for future use |
| `SYNCHRONIZATION` | `VARCHAR2(9)` |  | Indicates whether recorded transaction semantics should be maintained (`TRUE`) or not (`FALSE`)  When synchronization is on, the commit order observed during the original workload capture will be preserved. Every action that is replayed will be executed only after all of its dependent commits have been executed. Dependent commits are commits that were issued before the given action in the original workload capture.  See Also: `DBMS_WORKLOAD_REPLAY.PREPARE_REPLAY()` in [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm) for a detailed explanation of this replay parameter |
| `CONNECT_TIME_SCALE` | `NUMBER` | `NOT NULL` | Connection time scaling factor for captured streams during replay. The value is interpreted as a percentage.The default value of 100 means 100 percent.  See Also: `DBMS_WORKLOAD_REPLAY.PREPARE_REPLAY()` in [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm) for a detailed explanation of this replay parameter |
| `THINK_TIME_SCALE` | `NUMBER` | `NOT NULL` | Think time scaling factor for captured streams during replay. It scales the thinking time elapsed between two successive user calls from the same captured stream. The input is interpreted as a percentage. The default value of 100 means 100 percent.  See Also: `DBMS_WORKLOAD_REPLAY.PREPARE_REPLAY()` in [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm) for a detailed explanation of this replay parameter |
| `THINK_TIME_AUTO_CORRECT` | `VARCHAR2(5)` |  | Indicates whether the think time should be automatically corrected between calls (`TRUE`) or not (`FALSE`)  A value of `TRUE` reduces think time if replay goes slower than capture.  A value of `FALSE` results in no action.  See Also: `DBMS_WORKLOAD_REPLAY.PREPARE_REPLAY()` in [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm) for a detailed explanation of this replay parameter |
| `SCALE_UP_MULTIPLIER` | `NUMBER` | `NOT NULL` | Before the multiple-capture replay, `SCALE_UP_MULTIPLIER` is used to scale up the query part of a workload capture. The queries from each captured session are replayed concurrently as many times as the value of `SCALE_UP_MULTIPLIER`. |
| `USER_CALLS` | `NUMBER` |  | Total number of user calls replayed |
| `DBTIME` | `NUMBER` |  | Accumulated database time for the replay |
| `NETWORK_TIME` | `NUMBER` |  | Accumulated network time for the replay |
| `THINK_TIME` | `NUMBER` |  | Accumulated think time for the replay |
| `PAUSE_TIME` | `NUMBER` |  | Time that the replay spent in the paused state |
| `ELAPSED_TIME_DIFF` | `NUMBER` |  | Reserved for future use |
| `AWR_DBID` | `NUMBER` |  | Database ID of the AWR snapshots that correspond to this workload replay. For replays that were performed in the current database, this value is equal to the current database's DBID. For replays that were performed in other databases, this value will either be NULL or will be populated by `DBMS_WORKLOAD_REPLAY.IMPORT_AWR()`. |
| `AWR_BEGIN_SNAP` | `NUMBER` |  | Begin snapshot ID of the AWR snapshots that correspond to this workload replay |
| `AWR_END_SNAP` | `NUMBER` |  | End snapshot ID of the AWR snapshots that correspond to this workload replay |
| `AWR_EXPORTED` | `VARCHAR2(12)` |  | Indicates whether the AWR snapshots that correspond to this workload replay have been exported using `DBMS_WORKLOAD_REPLAY.EXPORT_AWR()` (`YES`) or not (`NO`), or whether AWR snapshots cannot be exported because the replay is still in progress, has run to completion successfully, or was done in a different database from which it was not exported (`NOT POSSIBLE`) |
| `ERROR_CODE` | `NUMBER` |  | Error code for this workload replay |
| `ERROR_MESSAGE` | `VARCHAR2(300)` |  | Error message for this workload replay |
| `DIR_PATH` | `VARCHAR2(4000)` | `NOT NULL` | Full directory path for the replay directory object |
| `REPLAY_DIR_NUMBER` | `NUMBER` |  | A hash value computed based on the values of other columns in this view, such as the `NAME`, `DBID`, `DBNAME`, `PREPARE_TIME`, `START_TIME`, and `END_TIME` columns. It should be fairly unique for any replay. The value is used to create a subdirectory under the replay directory. |
| `SQLSET_OWNER` <sup>Foot 1</sup> | `VARCHAR2(128)` |  | User name of the SQL tuning set owner |
| `SQLSET_NAME` <sup>Footref 1</sup> | `VARCHAR2(128)` |  | Name of the SQL tuning set for this workload replay |
| `SCHEDULE_NAME` <sup>Foot 2</sup> | `VARCHAR2(128)` |  | The name of a schedule to be replayed. It defines one or multiple workload captures, and the order to start their replays.  If `SCHEDULE_NAME` is `NULL`, the replay is a regular replay introduced since Oracle Database 11g, done with existing APIs from `DBMS_WORKLOAD_REPLAY`: `INITIALIZE_REPLAY`, `PREPARE_REPLAY`, and `START_REPLAY`.  If `SCHEDULE_NAME` is not `NULL`, the replay is a new consolidated replay introduced at Oracle Database 11.2.0.4. That is, it is a replay of one or more workload captures done with new APIs at `DBMS_WORKLOAD_REPLAY`: `INITIALIZE_CONSOLIDATED_REPLAY`, `PREPARE_CONSOLIDATED_REPLAY`, and `START_CONSOLIDATED_REPLAY`.  See Also: `DBMS_WORKLOAD_REPLAY` in [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/d_workload_replay.htm#ARPLS208) |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.2).

<sup>Footnote 2</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.4)