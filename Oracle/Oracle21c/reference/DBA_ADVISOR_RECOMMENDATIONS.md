---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ADVISOR_RECOMMENDATIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.37 DBA\_ADVISOR\_RECOMMENDATIONS

`DBA_ADVISOR_RECOMMENDATIONS` displays the results of an analysis of all recommendations in the database.

A recommendation can have multiple actions associated with it. Actions are described in the `DBA_ADVISOR_ACTIONS` view. A recommendation also points to a set of rationales that present a justification/reasoning for that recommendation. These rationales are in the `DBA_ADVISOR_RATIONALE` view.

Related View

`USER_ADVISOR_RECOMMENDATIONS` displays the results of an analysis of the recommendations owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the task |
| `REC_ID` | `NUMBER` | `NOT NULL` | Unique identifier of the recommendation |
| `TASK_ID` | `NUMBER` | `NOT NULL` | Task that owns the recommendation |
| `TASK_NAME` | `VARCHAR2(128)` |  | Name of the task |
| `EXECUTION_NAME` | `VARCHAR2(128)` |  | The name of the task execution with which this entry (row) is associated |
| `FINDING_ID` | `NUMBER` |  | Unique identifier of the finding |
| `TYPE` | `VARCHAR2(30)` |  | Type of the recommendation |
| `RANK` | `NUMBER` |  | Ranking, in terms of importance, within the set of recommendations generated for the task |
| `PARENT_REC_IDS` | `VARCHAR2(4000)` |  | Comma-separated list of the recommendation IDs of the parent recommendations. If this column is nonzero, then the recommendation depends on the parents, and cannot be accepted if the parents are not accepted. |
| `BENEFIT_TYPE` | `VARCHAR2(4000)` |  | Describes the benefit obtained by carrying out the recommendation  If there is a set of parents for the recommendation, then the benefit is the cumulative benefit (the improvement in system performance when this and all prior parent recommendations are accepted).  If there are no parents, then this is the improvement when the recommendation is accepted, independent of other recommendations. |
| `BENEFIT` | `NUMBER` |  | Calculated benefit value  This column displays an estimate of the savings in total activity (or load) on the system if all actions of the recommendation are implemented.  Recommendations are not additive, that is, the benefit from one recommendation may overlap with the benefit from another. For example, Oracle might recommend increasing the shared pool size, or reducing hard parses (by not using literals), and both recommendations might reduce the same part of the workload related to parsing.  The benefit is given in both pure active sessions and as a percent of the average active sessions of the analysis time period. Therefore, if the benefit is 20% of active sessions, Oracle estimates that if you apply the actions on the same workload, the average active sessions on the server will be reduced by 20%. The `DBA_ADDM_TASKS` view displays the average active sessions for an ADDM task. |
| `ANNOTATION_STATUS` | `VARCHAR2(11)` |  | When a task is complete, the recommendations are marked `ACCEPT`. The status can be changed later using the `MARK_RECOMMENDATION` procedure:  - `ACCEPT` - Current recommendation is ready to implement. This recommendation can also be used as advice for future analysis operations. - `REJECT` - Current recommendation is not acceptable to the user, and therefore will be excluded from any implementation scripts. This recommendation can also be used as advice for future analysis operations. - `IGNORE` - Though not rejected, the current recommendation will be ignored when generating scripts and will never be used as advice to future analysis operations. |
| `FLAGS` | `NUMBER` |  | Advisor-specific flags |
| `FILTERED` | `VARCHAR2(1)` |  | A value of `Y` means that the row in the view was filtered out by a directive (or a combination of directives). A value of `N` means that the row was not filtered. |
| `REC_TYPE_ID` | `NUMBER` |  | Recommendation type ID |

See Also:

- " [USER\_ADVISOR\_RECOMMENDATIONS](USER_ADVISOR_RECOMMENDATIONS.md) "
- " [DBA\_ADDM\_TASKS](DBA_ADDM_TASKS.md) "