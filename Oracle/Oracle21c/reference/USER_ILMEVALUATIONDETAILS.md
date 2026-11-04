---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/USER_ILMEVALUATIONDETAILS.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.509 USER\_ILMEVALUATIONDETAILS

`USER_ILMEVALUATIONDETAILS` displays details on evaluation of Automatic Data Optimization policies considered for Automatic Data Optimization tasks for a user.

It also shows the job name that executes the policy, in case the policy was selected for execution. If the policy was not selected for execution, this view provides a reason. Its columns are the same as those in `DBA_ILMEVALUATIONDETAILS`.

Note:

Automatic Data Optimization is supported in Oracle Database 12c Release 2 multitenant environments.

See Also:

" [DBA\_ILMEVALUATIONDETAILS](DBA_ILMEVALUATIONDETAILS.md) "