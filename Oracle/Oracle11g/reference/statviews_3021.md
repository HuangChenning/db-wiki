---
title: DBA_ADVISOR_FINDINGS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3021.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_ADVISOR_FINDINGS` displays the findings discovered by all advisors in the database.

Related View

`USER_ADVISOR_FINDINGS` displays the findings discovered by the advisors owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the task |
| `TASK_ID` | `NUMBER` | `NOT NULL` | Identifier of the task |
| `TASK_NAME` | `VARCHAR2(30)` |  | Name of the task |
| `EXECUTION_NAME` | `VARCHAR2(30)` |  | The name of the task execution with which this entry (row) is associated |
| `FINDING_ID` | `NUMBER` | `NOT NULL` | Identifier of the finding |
| `FINDING_NAME` | `VARCHAR2(4000)` |  | Name of the finding |
| `TYPE` | `VARCHAR2(11)` |  | Type of the finding: - `PROBLEM` - `SYMPTOM` - `ERROR` - `INFORMATION` |
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

["USER\_ADVISOR\_FINDINGS"](statviews_5204.md)