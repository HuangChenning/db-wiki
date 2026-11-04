---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ILMTASKS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.103 DBA\_ILMTASKS

`DBA_ILMTASKS` displays information on Automatic Data Optimization execution.

Related View

`USER_ILMTASKS` displays information on Automatic Data Optimization tasks created by a user.

Note:

Automatic Data Optimization is supported in Oracle Database 12c Release 2 multitenant environments.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TASK_ID` | `NUMBER` |  | Number that uniquely identifies a specific Automatic Data Optimization task |
| `TASK_OWNER` | `VARCHAR2(128)` | `NOT NULL` | User who initiates the task |
| `STATE` | `VARCHAR2(9)` |  | Possible values:  - `INACTIVE`: Indicates that the task was created for previewing - `ACTIVE`: Indicates that jobs have been created for the qualifying policies in the task - `COMPLETE`: Indicates that the task has completed |
| `CREATION_TIME` | `TIMESTAMP(6)` |  | The time that the task was created |
| `START_TIME` | `TIMESTAMP(6)` |  | Start time of a specific task |
| `COMPLETION_TIME` | `TIMESTAMP(6)` |  | Completion time of a specific task |

See Also:

" [USER\_ILMTASKS](USER_ILMTASKS.md) "