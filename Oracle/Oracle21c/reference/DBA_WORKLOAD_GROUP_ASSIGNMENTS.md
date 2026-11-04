---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_WORKLOAD_GROUP_ASSIGNMENTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.122 DBA\_WORKLOAD\_GROUP\_ASSIGNMENTS

`DBA_WORKLOAD_GROUP_ASSIGNMENTS` displays all the workload capture groups and their assigned instances. A workload capture group is a subset of the captured workload. Each group accesses its own set of recorded database objects.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `REPLAY_DIR_NUMBER` | `NUMBER(38)` | `NOT NULL` | The value that is associated with the subdirectory under the replay directory. See `REPLAY_DIR_NUMBER` in `DBA_WORKLOAD_REPLAYS`. |
| `GROUP_ID` | `NUMBER(38)` | `NOT NULL` | The identifier of a workload capture group |
| `INSTANCE_NUMBER` | `NUMBER(38)` | `NOT NULL` | The instance a given group is assigned to |

See Also:

" [DBA\_WORKLOAD\_REPLAYS](DBA_WORKLOAD_REPLAYS.md) "