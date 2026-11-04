---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_MVREF_RUN_STATS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.199 DBA\_MVREF\_RUN\_STATS

`DBA_MVREF_RUN_STATS` has information about each refresh run for all the materialized views for the database, with each run being identified by the `REFRESH_ID`. The information includes timing statistics related to the run and the parameters specified in that run.

Related View

`USER_MVREF_RUN_STATS` has information about each refresh run for the materialized views accessible for the current database user, with each run being identified by the `REFRESH_ID`. The information includes timing statistics related to the run and the parameters specified in that run. This view does not display the `RUN_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `RUN_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the refresh operation (the user who launched the operation) |
| `REFRESH_ID` | `NUMBER` | `NOT NULL` | The refresh ID of the refresh run |
| `NUM_MVS` | `NUMBER` | `NOT NULL` | The number of materialized views being refreshed in the run |
| `MVIEWS` | `VARCHAR2(4000)` |  | Shows the list of comma separated parameters specified in the API for the materialized view refresh operation |
| `BASE_TABLES` | `VARCHAR2(4000)` |  | For internal use only |
| `METHOD` | `VARCHAR2(4000)` |  | The `METHOD` parameter specified by the API |
| `ROLLBACK_SEG` | `VARCHAR2(4000)` |  | The `ROLLBACK_SEG` parameter specified by the API |
| `PUSH_DEFERRED_RPC` | `CHAR(1)` |  | The `PUSH_DEFERRED_RPC` parameter specified by the API |
| `REFRESH_AFTER_ERRORS` | `CHAR(1)` |  | The `REFRESH_AFTER_ERRORS` parameter specified by the API |
| `PURGE_OPTION` | `NUMBER` |  | The `PURGE_OPTION` parameter specified by the API |
| `PARALLELISM` | `NUMBER` |  | The `PARALLELISM` parameter specified by the API |
| `HEAP_SIZE` | `NUMBER` |  | The `HEAP_SIZE` parameter specified by the API |
| `ATOMIC_REFRESH` | `CHAR(1)` |  | The `ATOMIC_REFRESH` parameter specified by the API |
| `NESTED` | `CHAR(1)` |  | The `NESTED` parameter specified by the API |
| `OUT_OF_PLACE` | `CHAR(1)` |  | The `OUT_OF_PLACE` parameter specified by the API |
| `NUMBER_OF_FAILURES` | `NUMBER` |  | The number of failures that occurred in processing the API |
| `START_TIME` | `TIMESTAMP(6)` |  | Start time of the refresh run |
| `END_TIME` | `TIMESTAMP(6)` |  | End time of the refresh run |
| `ELAPSED TIME` | `NUMBER` |  | The length of time for the refresh run, in seconds |
| `LOG_SETUP_TIME` | `NUMBER` |  | Log setup time (in seconds) for the materialized view for a non-atomic refresh; `NULL` for an atomic refresh |
| `LOG_PURGE_TIME` | `NUMBER` |  | Log purge time (in seconds) for the materialized view in the case of atomic refresh; `NULL` in the case of non-atomic refresh |
| `COMPLETE_STATS_AVAILABLE` | `CHAR(1)` |  | Indicates whether all the complete refresh statistics are available for this run:  - `Y`: All the statistics are available - `N`: All the statistics are not available |

See Also:

" [USER\_MVREF\_RUN\_STATS](USER_MVREF_RUN_STATS.md) "