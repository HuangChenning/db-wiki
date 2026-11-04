---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_WORKLOAD_TRACKED_COMMITS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.131 DBA\_WORKLOAD\_TRACKED\_COMMITS

`DBA_WORKLOAD_TRACKED_COMMITS` displays the commits tracked every second during a database replay.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `REPLAY_DIR_NUMBER` | `NUMBER` | `NOT NULL` | The numerical value that is associated with the subdirectory under the replay directory.  See `REPLAY_DIR_NUMBER` in `DBA_WORKLOAD_REPLAYS` |
| `INSTANCE_NUMBER` | `NUMBER(38)` |  | The instance where the commit is executed |
| `FILE_ID` | `NUMBER(38)` | `NOT NULL` | The file ID |
| `CALL_CTR` | `NUMBER(38)` | `NOT NULL` | The call counter of the commit |
| `COMMIT_SCN` | `NUMBER(38)` |  | The recorded commit SCN value |
| `PREV_GLOBAL_COMMIT_FILE_ID` | `NUMBER(38)` |  | The file ID of the latest commit across all sessions |
| `PREV_GLOBAL_COMMIT_SCN` | `NUMBER(38)` |  | The recorded SCN of the latest commit across all sessions |
| `PREV_LOCAL_COMMIT_CALL_CTR` | `NUMBER(38)` |  | The call counter of the latest commit in the same session |
| `CAPTURE_COMMIT_TIME` | `NUMBER(38)` |  | The time in seconds since the capture started |
| `CAPTURE_COMMIT_TIME_DELTA` | `NUMBER(38)` |  | The elapsed time in seconds since the previous commit across all sessions during capture |
| `REPLAY_COMMIT_TIME` | `NUMBER(38)` |  | The time in seconds since the replay started |
| `REPLAY_COMMIT_TIME_DELTA` | `NUMBER(38)` |  | The elapsed time in seconds since the previous commit across all sessions during the replay |

See Also:

[DBA\_WORKLOAD\_REPLAYS](DBA_WORKLOAD_REPLAYS.md)