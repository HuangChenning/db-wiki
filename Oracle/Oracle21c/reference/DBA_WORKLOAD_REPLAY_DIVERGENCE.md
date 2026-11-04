---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_WORKLOAD_REPLAY_DIVERGENCE.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.125 DBA\_WORKLOAD\_REPLAY\_DIVERGENCE

`DBA_WORKLOAD_REPLAY_DIVERGENCE` displays information about data/error divergence for a user call that has been replayed.

`DBA_WORKLOAD_DIV_SUMMARY` displays a summary of the replay divergence information in the `DBA_WORKLOAD_REPLAY_DIVERGENCE` view. `DBA_WORKLOAD_REPLAY_DIVERGENCE` may have duplicate entries, while `DBA_WORKLOAD_DIV_SUMMARY` keeps only one entry and tracks the number of occurrences of each duplicate entry.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `REPLAY_ID` | `NUMBER` | `NOT NULL` | ID (key) for the workload replay |
| `TIMESTAMP` | `TIMESTAMP(6) WITH TIME ZONE` |  | Time that the divergence occurred |
| `DIVERGENCE_TYPE` | `NUMBER` | `NOT NULL` | Reserved for future use |
| `IS_QUERY_DATA_DIVERGENCE` | `VARCHAR2(1)` |  | Indicates whether the data divergence is from the number of rows fetched by `SELECT` queries (`Y`) or not (`N`) |
| `IS_DML_DATA_DIVERGENCE` | `VARCHAR2(1)` |  | Indicates whether the divergence is from the number of rows affected by `INSERT`, `UPDATE`, or `DELETE` SQL statements (`Y`) or not (`N`) |
| `IS_ERROR_DIVERGENCE` | `VARCHAR2(1)` |  | Indicates whether the divergence is from errors seen during capture or replay (`Y`) or not (`N`) |
| `IS_THREAD_FAILURE` | `VARCHAR2(1)` |  | Indicates whether the divergence is from sessions that failed during replay (`Y`) or not (`N`) |
| `IS_DATA_MASKED` | `VARCHAR2(1)` |  | Indicates whether the SQL call contains masked bind data (Y) or not (N).  If data masking technology is used at the replay database, the workload capture files need to be masked. Otherwise, SQL statements generated from capture files that contain sensitive bind data will not match the database. When the replay client sends masked bind data to the server, it turns on the `IS_DATA_MASKED` flag for the current SQL call. |
| `IS_CLIENT_FAILURE` | `VARCHAR2(1)` |  | Indicates whether the workload replay client failed during replay (`Y`) or not (`N`) |
| `EXPECTED_ROW_COUNT` | `NUMBER` |  | Number of rows fetched for `SELECT` queries or rows affected for `INSERT`, `UPDATE`, or `DELETE` SQL statements during capture |
| `OBSERVED_ROW_COUNT` | `NUMBER` |  | Actual number of rows fetched for `SELECT` queries or rows affected for `INSERT`, `UPDATE`, or `DELETE` SQL statements during replay |
| `EXPECTED_ERROR#` | `NUMBER` |  | Error number that was seen during capture (`0` if the capture ran successfully) |
| `EXPECTED_ERROR_MESSAGE` | `VARCHAR2(4000)` |  | Text of the error message whose number appears in the `EXPECTED_ERROR#` column |
| `OBSERVED_ERROR#` | `NUMBER` |  | Actual error number seen during replay (`0` if the replay ran successfully, `15566` (corresponding to `ORA-15566`) if the captured call could not be replayed) |
| `OBSERVED_ERROR_MESSAGE` | `VARCHAR2(4000)` |  | Text of the error message whose number appears in the `OBSERVED_ERROR#` column |
| `STREAM_ID` | `NUMBER` | `NOT NULL` | Stream ID of the session that reported the divergence |
| `CALL_COUNTER` | `NUMBER` | `NOT NULL` | Call counter of the user call that reported the divergence |
| `CAPTURE_STREAM_ID` | `NUMBER` |  | Internal ID of the capture file whose replay produced the divergence |
| `SQL_ID` | `VARCHAR2(13)` |  | SQL ID of the SQL that reported the divergence |
| `SESSION_ID` | `NUMBER` | `NOT NULL` | Session ID of the session that reported the divergence |
| `SESSION_SERIAL#` | `NUMBER` | `NOT NULL` | Captured session serial number of the session that reported the divergence |
| `SERVICE` | `VARCHAR2(64)` |  | Service name of the session that reported the divergence |
| `MODULE` | `VARCHAR2(64)` |  | Module name of the session that reported the divergence |
| `ACTION` | `VARCHAR2(64)` |  | Action name of the session that reported the divergence |
| `INSTANCE_NUMBER` | `NUMBER` |  | The number of the instance that reported the divergence |
| `WRC_ID` | `NUMBER` |  | The identifier of the workload replay client |

See Also:

" [DBA\_WORKLOAD\_DIV\_SUMMARY](DBA_WORKLOAD_DIV_SUMMARY.md) "