---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_RSRC_PLANS.html
tags:
  - oracle
  - 12c
  - reference
---

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