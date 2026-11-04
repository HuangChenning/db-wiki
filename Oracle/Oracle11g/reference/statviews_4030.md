---
title: DBA_HIST_RSRC_PLAN
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4030.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_RSRC_PLAN` displays historical information about resource plans. This view contains snapshots of `V$RSRC_PLAN_HISTORY`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `SEQUENCE#` | `NUMBER` | `NOT NULL` | A sequential counter that uniquely describes a row. When the instance is restarted, this value is reset to zero. |
| `START_TIME` | `DATE` | `NOT NULL` | Time that the resource plan was enabled |
| `END_TIME` | `DATE` | `NOT NULL` | Time that the resource plan was disabled; NULL if the row contains the current resource plan information |
| `PLAN_ID` | `NUMBER` | `NOT NULL` | Resource plan ID; NULL if the Resource Manager was disabled |
| `PLAN_NAME` | `VARCHAR2(30)` | `NOT NULL` | Resource plan name; NULL if the Resource Manager was disabled |
| `CPU_MANAGED` | `VARCHAR2(4)` | `NOT NULL` | Indicates whether the resource plan has parameters that specify a policy for how the Resource Manager should schedule sessions to manage CPU usage (`ON`) or whether Resource Manager is not managing CPU usage (`OFF`) |
| `PARALLEL_EXECUTION_MANAGED` <sup>Foot 1</sup> | `VARCHAR2(4)` |  | State of parallel statement queuing: - `OFF` - Parallel statement queuing is disabled - `STARTUP` - Parallel statement queuing is enabled. This is a temporary state that can occur when an Oracle RAC database is undergoing configuration changes - `FIFO` - Parallel statement queuing is enabled. All parallel statements are managed in a single Oracle RAC FIFO queue - `FULL` - Parallel statement queuing is enabled. All parallel statements are managed in per-consumer group queues according to the current resource plan. This state is used when a resource plan that contains resource allocation directives (`MGMT_P*`) is enabled. |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.2).