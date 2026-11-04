---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ILMEVALUATIONDETAILS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.98 DBA\_ILMEVALUATIONDETAILS

`DBA_ILMEVALUATIONDETAILS` displays details on evaluation of Automatic Data Optimization policies considered for Automatic Data Optimization tasks.

It also shows the job name that executes the policy, in case the policy was selected for execution. If the policy was not selected for execution, this view provides a reason.

Related View

`USER_ILMEVALUATIONDETAILS` displays details on evaluation of Automatic Data Optimization policies considered for Automatic Data Optimization tasks for a user. It also shows the job name that executes the policy, in case the policy was selected for execution. If the policy was not selected for execution, this view provides a reason.

Note:

Automatic Data Optimization is supported in Oracle Database 12c Release 2 multitenant environments.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TASK_ID` | `NUMBER` |  | Number that uniquely identifies a specific Automatic Data Optimization task |
| `POLICY_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the Automatic Data Optimization policy |
| `OBJECT_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the object associated with the Automatic Data Optimization policy |
| `OBJECT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the object associated with the Automatic Data Optimization policy |
| `SUBOBJECT_NAME` | `VARCHAR2(128)` |  | Name of the subobject associated with the Automatic Data Optimization policy |
| `OBJECT_TYPE` | `VARCHAR2(18)` |  | Object type. Valid values include `TABLE`, `TABLE PARTITION`, and `TABLE SUBPARTITION`. |
| `SELECTED_FOR_EXECUTION` | `VARCHAR2(42)` |  | Indicates whether the policy has been selected for execution on the object. If not, the reason for not being selected is listed. Possible values:  - `POLICY DISABLED` - `SELECTED FOR EXECUTION` - `POLICY OVERRULED` - `INHERITED POLICY OVERRULED` - `PRECONDITION NOT SATISFIED` - `JOB ALREADY EXISTS` - `NO OPERATION SINCE LAST ILM ACTION` - `TABLE HAS MATERIALIZED VIEW` - `TARGET COMPRESSION NOT HIGHER THAN CURRENT` - `STATISTICS NOT AVAILABLE`  The value `SELECTED FOR EXECUTION` means a job was created for this policy on the object. The other values state the reason why the policy on the object was selected for execution. |
| `JOB_NAME` | `VARCHAR2(128)` |  | Name of the job in the case where the policy is selected for execution on this object |