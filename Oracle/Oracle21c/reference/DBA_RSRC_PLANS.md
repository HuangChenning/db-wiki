---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_RSRC_PLANS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.312 DBA\_RSRC\_PLANS

`DBA_RSRC_PLANS` displays information about all resource plans in the database.

For a list of currently active plans, see " [V$RSRC\_PLAN](V-RSRC_PLAN.md) ".

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PLAN_ID` | `NUMBER` | `NOT NULL` | ID number of the resource plan |
| `PLAN` | `VARCHAR2(128)` |  | Name of the resource plan |
| `NUM_PLAN_DIRECTIVES` | `NUMBER` |  | Number of plan directives for the plan |
| `CPU_METHOD` | `VARCHAR2(128)` |  | CPU resource allocation method for the plan |
| `MGMT_METHOD` | `VARCHAR2(128)` |  | Resource allocation method for the plan |
| `ACTIVE_SESS_POOL_MTH` | `VARCHAR2(128)` |  | Active session pool resource allocation method for the plan |
| `PARALLEL_DEGREE_LIMIT_MTH` | `VARCHAR2(128)` |  | Parallel degree limit resource allocation method for the plan |
| `QUEUING_MTH` | `VARCHAR2(128)` |  | Queuing resource allocation method for the plan |
| `SUB_PLAN` | `VARCHAR2(3)` |  | Indicates whether the plan is a subplan (`YES`) or not (`NO`) |