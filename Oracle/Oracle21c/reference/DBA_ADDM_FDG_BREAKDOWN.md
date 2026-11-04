---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ADDM_FDG_BREAKDOWN.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.12 DBA\_ADDM\_FDG\_BREAKDOWN

`DBA_ADDM_FDG_BREAKDOWN` describes the contribution for each finding from the different instances.

There is one row for each finding and for each instance participating in the analysis. Rows are omitted if the impact from that instance is not sufficient to register a finding in a local ADDM analysis.

Related View

`USER_ADDM_FDG_BREAKDOWN` describes the contribution for each finding from the different instances owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TASK_ID` | `NUMBER` | `NOT NULL` | Identifies the task to which this finding belongs (see `DBA_ADVISOR_TASKS)` |
| `FINDING_ID` | `NUMBER` | `NOT NULL` | Identifies the finding (see `DBA_ADVISOR_FINDINGS`) |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | The number of the instance contributing to the finding |
| `DATABASE_TIME` | `NUMBER` |  | The database time, in microseconds, accumulated by this instance during the analysis period |
| `ACTIVE_SESSIONS` | `NUMBER` |  | The average number of active sessions of the finding in this instance |
| `PERC_ACTIVE_SESSIONS` | `NUMBER` |  | The percentage of contribution from this instance compared to the total impact of the finding |

See Also:

" [USER\_ADDM\_FDG\_BREAKDOWN](USER_ADDM_FDG_BREAKDOWN.md) "