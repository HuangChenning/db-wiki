---
title: "V$RSRC_PLAN"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2159.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$RSRC_PLAN` displays the names of all currently active resource plans.

| Column | Datatype | Description |
| --- | --- | --- |
| `ID` | `NUMBER` | Resource plan ID (a unique number, consistent across database shutdowns and startups). This is also the data dictionary object ID. |
| `NAME` | `VARCHAR2(32)` | Name of the resource plan |
| `IS_TOP_PLAN` | `VARCHAR2(5)` | Indicates whether the resource plan is the current top plan (`TRUE`) or whether the resource plan is a subplan of the current top plan (`FALSE`) |
| `CPU_MANAGED` | `VARCHAR2(3)` | Indicates whether the resource plan has parameters that specify a policy for how the Resource Manager should schedule sessions to manage CPU usage (`ON`) or whether Resource Manager is not managing CPU usage (`OFF`) |
| `INSTANCE_CAGING` <sup>Foot 1</sup> | `VARCHAR2(3)` | Indicates whether instance caging is enabled (`ON`) or disabled (`OFF`). Instance caging is enabled if the `CPU_COUNT` initialization parameter is set to a value other than `0` and Resource Manager is enabled. |
| `PARALLEL_SERVERS_ACTIVE` <sup>Footref 1</sup> | `NUMBER` | Total number of active parallel servers on the instance |
| `PARALLEL_SERVERS_TOTAL` <sup>Footref 1</sup> | `NUMBER` | The value of `PARALLEL_SERVERS_TARGET` for the instance. Parallel statements are queued if the total number of active parallel servers exceeds this value. |
| `PARALLEL_EXECUTION_MANAGED` <sup>Footref 1</sup> | `VARCHAR2(32)` | State of parallel statement queuing: - `OFF` - Parallel statement queuing is disabled - `STARTUP` - Parallel statement queuing is enabled. This is a temporary state that can occur when an Oracle RAC database is undergoing configuration changes - `FIFO` - Parallel statement queuing is enabled. All parallel statements are managed in a single Oracle RAC FIFO queue - `FULL` - Parallel statement queuing is enabled. All parallel statements are managed in per-consumer group queues according to the current resource plan. This state is used when a resource plan that contains resource allocation directives (`MGMT_P*`) is enabled. |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.2).

See Also:

- ["DBA\_RSRC\_PLANS"](statviews_4230.md) for a listing of all plans in the database
- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for information on resource plans
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm) for information on defining resource allocation methods for consumer groups with the `DBMS_RESOURCE_MANAGER` package