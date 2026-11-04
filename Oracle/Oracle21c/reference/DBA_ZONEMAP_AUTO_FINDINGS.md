---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ZONEMAP_AUTO_FINDINGS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.170 DBA\_ZONEMAP\_AUTO\_FINDINGS

`DBA_ZONEMAP_AUTO_FINDINGS` provides information about automatic zone map findings.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TASK_ID` | `NUMBER` | `NOT NULL` | Zone map task identifier |
| `MSG_ID` | `NUMBER` | `NOT NULL` | Zone map message identifier |
| `EXEC_NAME` | `VARCHAR2(128)` |  | Zone map execution name |
| `MESSAGE` | `VARCHAR2(4000)` |  | Execution message text |
| `TIME_STAMP` | `TIMESTAMP(9)` |  | Finding timestamp |
| `OBJECT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the object for which the finding was observed, typically a table name or a zone map name |
| `FINDING_REASON` | `VARCHAR2(9)` |  | Finding reason code |
| `FINDING_TYPE` | `VARCHAR2(9)` |  | Finding type. Possible values:  - `BLACKLIST`: The table is no longer a candidate for automatic zone maps - `ERROR`: An error occurred - `EVICT`: The table does not meet automatic zone map creation criteria - `OTHER`  Refer to the `MESSAGE` column for additional information about the reasoning behind the finding type. |

Automatic zone map findings contain information that the database learned when performing automatic zone map executions. The database uses these findings to optimize subsequent automatic zone maps executions, which saves on execution time and resources.

The `TASK_ID`, `MSG_ID`, and `EXEC_NAME` columns in this view correspond to the same columns in the `DBA_ZONEMAP_AUTO_ACTIONS` view. This allows you to correlate the findings in `DBA_ZONEMAP_AUTO_FINDINGS` with their corresponding actions in `DBA_ZONEMAP_AUTO_ACTIONS`.

Note:

This view is available starting with Oracle Database 21c.

See Also:

" [DBA\_ZONEMAP\_AUTO\_ACTIONS](DBA_ZONEMAP_AUTO_ACTIONS.md) "