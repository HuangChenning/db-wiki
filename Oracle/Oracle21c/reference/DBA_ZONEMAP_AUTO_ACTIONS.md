---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ZONEMAP_AUTO_ACTIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.169 DBA\_ZONEMAP\_AUTO\_ACTIONS

`DBA_ZONEMAP_AUTO_ACTIONS` provides information about automatic zone map tasks and executions.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TASK_ID` | `NUMBER` | `NOT NULL` | Zone map task identifier |
| `MSG_ID` | `NUMBER` | `NOT NULL` | Zone map message identifier |
| `EXEC_NAME` | `VARCHAR2(128)` |  | Zone map execution name |
| `ACTION_MSG` | `VARCHAR2(4000)` |  | Execution message text |
| `TIME_STAMP` | `TIMESTAMP(9)` |  | Execution timestamp |

The `TASK_ID`, `MSG_ID`, and `EXEC_NAME` columns in this view correspond to the same columns in the `DBA_ZONEMAP_AUTO_FINDINGS` view. This allows you to correlate the actions in `DBA_ZONEMAP_AUTO_ACTIONS` with their corresponding findings in `DBA_ZONEMAP_AUTO_FINDINGS`.

Note:

This view is available starting with Oracle Database 21c.

See Also:

" [DBA\_ZONEMAP\_AUTO\_FINDINGS](DBA_ZONEMAP_AUTO_FINDINGS.md) "