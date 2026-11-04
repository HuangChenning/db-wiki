---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ADVISOR_FINDINGS.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.30 DBA\_ADVISOR\_FINDINGS

`DBA_ADVISOR_FINDINGS` displays the findings discovered by all advisors in the database.

Related View

`USER_ADVISOR_FINDINGS` displays the findings discovered by the advisors owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the task |
| `TASK_ID` | `NUMBER` | `NOT NULL` | Identifier of the task |
| `TASK_NAME` | `VARCHAR2(128)` |  | Name of the task |
| `EXECUTION_NAME` | `VARCHAR2(128)` |  | The name of the task execution with which this entry (row) is associated |
| `FINDING_ID` | `NUMBER` | `NOT NULL` | Identifier of the finding |
| `FINDING_NAME` | `VARCHAR2(4000)` |  | Name of the finding |
| `TYPE` | `VARCHAR2(11)` |  | Type of the finding:  - `PROBLEM` - `SYMPTOM` - `ERROR` - `INFORMATION` |
| `TYPE_ID` | `NUMBER` | `NOT NULL` | Numeric ID for the value in column `TYPE` |
| `PARENT` | `NUMBER` | `NOT NULL` | Identifier of the parent finding |
| `OBJECT_ID` | `NUMBER` |  | Identifier of the associated object, if any |
| `IMPACT_TYPE` | `VARCHAR2(4000)` |  | Impact of the finding on the system |
| `IMPACT` | `NUMBER` |  | Impact value |
| `MESSAGE` | `VARCHAR2(4000)` |  | Message describing the finding |
| `MORE_INFO` | `VARCHAR2(4000)` |  | Additional info associated with the finding |
| `FILTERED` | `VARCHAR2(1)` |  | A value of `Y` means that the row in the view was filtered out by a directive (or a combination of directives). A value of `N` means that the row was not filtered. |
| `FLAGS` | `NUMBER` |  | For internal use only by advisor framework clients |

See Also:

" [USER\_ADVISOR\_FINDINGS](USER_ADVISOR_FINDINGS.md) "