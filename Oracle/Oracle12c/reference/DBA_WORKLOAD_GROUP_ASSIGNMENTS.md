---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_WORKLOAD_GROUP_ASSIGNMENTS.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_WORKLOAD_GROUP_ASSIGNMENTS` displays all the workload capture groups and their assigned instances. A workload capture group is a subset of the captured workload. Each group accesses its own set of recorded database objects.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `REPLAY_DIR_NUMBER` | `NUMBER(38)` | `NOT NULL` | The value that is associated with the subdirectory under the replay directory. See `REPLAY_DIR_NUMBER` in `DBA_WORKLOAD_REPLAYS`. |
| `GROUP_ID` | `NUMBER(38)` | `NOT NULL` | The identifier of a workload capture group |
| `INSTANCE_NUMBER` | `NUMBER(38)` | `NOT NULL` | The instance a given group is assigned to |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

" [DBA\_WORKLOAD\_REPLAYS](DBA_WORKLOAD_REPLAYS.md) "