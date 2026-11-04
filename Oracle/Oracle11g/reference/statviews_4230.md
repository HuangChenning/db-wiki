---
title: DBA_RSRC_PLANS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4230.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_RSRC_PLANS` displays information about all resource plans in the database. For a list of currently active plans, see ["V$RSRC\_PLAN"](dynviews_2159.md).

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PLAN_ID` | `NUMBER` | `NOT NULL` | ID number of the resource plan |
| `PLAN` | `VARCHAR2(30)` |  | Name of the resource plan |
| `NUM_PLAN_DIRECTIVES` | `NUMBER` |  | Number of plan directives for the plan |
| `CPU_METHOD` | `VARCHAR2(30)` |  | CPU resource allocation method for the plan |
| `MGMT_METHOD` | `VARCHAR2(30)` |  | Resource allocation method for the plan |
| `ACTIVE_SESS_POOL_MTH` | `VARCHAR2(30)` |  | Active session pool resource allocation method for the plan |
| `PARALLEL_DEGREE_LIMIT_MTH` | `VARCHAR2(30)` |  | Parallel degree limit resource allocation method for the plan |
| `QUEUING_MTH` | `VARCHAR2(30)` |  | Queuing resource allocation method for the plan |
| `SUB_PLAN` | `VARCHAR2(3)` |  | Indicates whether the plan is a subplan (`YES`) or not (`NO`) |
| `COMMENTS` | `VARCHAR2(2000)` |  | Text comment on the plan |
| `STATUS` | `VARCHAR2(30)` |  | Indicates whether the plan is part of the pending area (`PENDING`) or not (NULL) |
| `MANDATORY` | `VARCHAR2(3)` |  | Indicates whether the plan is mandatory (`YES`) or not (`NO`) |

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for information on resource plans in general
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm) for more information on creating resource plans with the `DBMS_RESOURCE_MANAGER` package