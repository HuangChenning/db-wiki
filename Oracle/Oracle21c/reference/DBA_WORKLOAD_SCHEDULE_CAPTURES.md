---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_WORKLOAD_SCHEDULE_CAPTURES.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.128 DBA\_WORKLOAD\_SCHEDULE\_CAPTURES

`DBA_WORKLOAD_SCHEDULE_CAPTURES` displays the workload captures used by replay schedules.

Each row in the view contains information about one workload capture.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SCHEDULE_NAME` | `VARCHAR2(128)` | `NOT NULL` | The name of a schedule to be replayed |
| `SCHEDULE_CAP_ID` | `NUMBER` | `NOT NULL` | Identifies a workload capture added to a replay schedule. It starts with `1`. If the same capture is added multiple times to a schedule, there will be multiple rows with different `SCHEDULE_CAP_ID` columns and identical `CAPTURE_ID` columns. |
| `CAPTURE_ID` | `NUMBER` | `NOT NULL` | Points to the capture ID from `DBA_WORKLOAD_CAPTURES`. |
| `CAPTURE_DIR` | `VARCHAR2(128)` | `NOT NULL` | Name of the directory object for workload capture |
| `OS_SUBDIR` | `VARCHAR2(4000)` | `NOT NULL` | Name of the subdirectory under the replay directory for this workload capture |
| `MAX_CONCURRENT_SESSIONS` | `NUMBER` |  | The maximal number of concurrent sessions that was seen in this workload capture |
| `NUM_CLIENTS_ASSIGNED` | `NUMBER` |  | Number of clients assigned to this workload capture before replay starts |
| `NUM_CLIENTS` | `NUMBER` |  | Number of clients that are running for this workload capture during replay |
| `NUM_CLIENTS_DONE` | `NUMBER` |  | Number of clients that have finished the replay of this workload capture |
| `STOP_REPLAY` | `VARCHAR2(1)` | `NOT NULL` | Indicates whether the whole replay will stop once the replay of this workload capture is done (`Y`) or not (`N`) |
| `TAKE_BEGIN_SNAPSHOT` | `VARCHAR2(1)` | `NOT NULL` | Indicates whether an AWR snapshot will be taken when the replay of this capture starts (`Y`) or not (`N`) |
| `TAKE_END_SNAPSHOT` | `VARCHAR2(1)` | `NOT NULL` | Indicates whether an AWR snapshot will be taken when the replay of this capture finishes (`Y`) or not (`N`) |
| `QUERY_ONLY` | `VARCHAR2(1)` | `NOT NULL` | Indicates whether only the query-only workload from the current workload capture will be replayed, skipping all the DML/DDL that might update the database (`Y`) or not (`N`) |
| `START_DELAY_SECS` | `NUMBER` |  | Displays the wait time (in seconds) when the replay of a workload capture is ready to start. "Ready to start" means the capture does not wait for any other capture, or all the captures for which it should wait have already been replayed. The default value is 0. |
| `START_TIME` | `DATE` |  | Start time for the replay of this capture |
| `END_TIME` | `DATE` |  | Finish time for the replay of this capture |
| `AWR_DBID` | `NUMBER` |  | AWR database ID of the replay |
| `AWR_BEGIN_SNAP` | `NUMBER` |  | AWR snapshot ID when the replay starts |
| `AWR_END_SNAP` | `NUMBER` |  | AWR snapshot ID when the replay finishes |
| `NUM_CLIENTS_ABORTED` | `NUMBER` |  | Number of workload replay clients terminated during the replay |