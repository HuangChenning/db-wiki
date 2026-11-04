---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_AUTOTASK_SETTINGS.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.200 DBA\_AUTOTASK\_SETTINGS

`DBA_AUTOTASK_SETTINGS` displays the settings for automated tasks.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Identifier of the database used by the task |
| `TASK_ID` | `NUMBER` | `NOT NULL` | Identifier of the task |
| `TASK_NAME` | `VARCHAR2(64)` |  | Name of the task |
| `INTERVAL` | `NUMBER` |  | The time interval between task invocations (in seconds) |
| `MAX_RUN_TIME` | `NUMBER` |  | Maximum run time allowed for the task before it is stopped (in seconds) |
| `ENABLED` | `VARCHAR2(5)` |  | Indicates whether the task is enabled (`TRUE`) or not (`FALSE`) |

Note:

This view is available starting with Oracle Database 21c.