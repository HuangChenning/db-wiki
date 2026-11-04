---
title: DBA_RSRC_PLAN_DIRECTIVES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4229.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_RSRC_PLAN_DIRECTIVES` displays information about all resource plan directives in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `PLAN` | `VARCHAR2(30)` |  | Name of the plan to which the directive belongs |
| `GROUP_OR_SUBPLAN` | `VARCHAR2(30)` |  | Name of the consumer group or subplan referred to |
| `TYPE` | `VARCHAR2(14)` |  | Indicates whether `GROUP_OR_SUBPLAN` refers to a consumer group (`CONSUMER_GROUP`) or a plan (`PLAN`) |
| `CPU_P1` | `NUMBER` |  | First parameter for the CPU resource allocation method |
| `CPU_P2` | `NUMBER` |  | Second parameter for the CPU resource allocation method |
| `CPU_P3` | `NUMBER` |  | Third parameter for the CPU resource allocation method |
| `CPU_P4` | `NUMBER` |  | Fourth parameter for the CPU resource allocation method |
| `CPU_P5` | `NUMBER` |  | Fifth parameter for the CPU resource allocation method |
| `CPU_P6` | `NUMBER` |  | Sixth parameter for the CPU resource allocation method |
| `CPU_P7` | `NUMBER` |  | Seventh parameter for the CPU resource allocation method |
| `CPU_P8` | `NUMBER` |  | Eighth parameter for the CPU resource allocation method |
| `MGMT_P1` | `NUMBER` |  | First parameter for the resource allocation method |
| `MGMT_P2` | `NUMBER` |  | Second parameter for the resource allocation method |
| `MGMT_P3` | `NUMBER` |  | Third parameter for the resource allocation method |
| `MGMT_P4` | `NUMBER` |  | Fourth parameter for the resource allocation method |
| `MGMT_P5` | `NUMBER` |  | Fifth parameter for the resource allocation method |
| `MGMT_P6` | `NUMBER` |  | Sixth parameter for the resource allocation method |
| `MGMT_P7` | `NUMBER` |  | Seventh parameter for the resource allocation method |
| `MGMT_P8` | `NUMBER` |  | Eighth parameter for the resource allocation method |
| `ACTIVE_SESS_POOL_P1` | `NUMBER` |  | First parameter for the active session pool resource allocation method |
| `QUEUEING_P1` | `NUMBER` |  | First parameter for the queuing resource allocation method |
| `PARALLEL_TARGET_PERCENTAGE` <sup>Foot 1</sup> | `NUMBER` |  | Maximum percentage of the target number of parallel servers that the consumer group can use |
| `PARALLEL_DEGREE_LIMIT_P1` | `NUMBER` |  | First parameter for the parallel degree limit resource allocation method |
| `SWITCH_GROUP` | `VARCHAR2(30)` |  | Group to switch to once the switch time is reached |
| `SWITCH_FOR_CALL` | `VARCHAR2(5)` |  | Indicates whether to switch back to the initial consumer group once the top call has completed (`TRUE`) or not (`FALSE`) |
| `SWITCH_TIME` | `NUMBER` |  | Amount of run time before the session is automatically switched |
| `SWITCH_IO_MEGABYTES` | `NUMBER` |  | Maximum megabytes of I/O within a group |
| `SWITCH_IO_REQS` | `NUMBER` |  | Maximum I/O requests within a group |
| `SWITCH_ESTIMATE` | `VARCHAR2(5)` |  | Indicates whether estimated execution time should be used for switch criteria (`TRUE`) or not (`FALSE`) |
| `MAX_EST_EXEC_TIME` | `NUMBER` |  | Maximum estimated execution time |
| `UNDO_POOL` | `NUMBER` |  | Undo pool size for the consumer group |
| `MAX_IDLE_TIME` | `NUMBER` |  | Maximum idle time for the session |
| `MAX_IDLE_BLOCKER_TIME` | `NUMBER` |  | Maximum idle time for the session when blocking other sessions |
| `MAX_UTILIZATION_LIMIT` | `NUMBER` |  | Maximum percentage of CPU that the consumer group or subplan can utilize |
| `PARALLEL_QUEUE_TIMEOUT` <sup>Footref 1</sup> | `NUMBER` |  | Time (in seconds) that a query may remain in the parallel statement queue for the consumer group before it is removed and terminated with error `ORA-07454` |
| `SWITCH_TIME_IN_CALL` | `NUMBER` |  | Call switch time limit for execution in a group |
| `COMMENTS` | `VARCHAR2(2000)` |  | Text comment on the plan directive |
| `STATUS` | `VARCHAR2(30)` |  | Indicates whether the plan directive is part of the pending area (`PENDING`) or not (NULL) |
| `MANDATORY` | `VARCHAR2(3)` |  | Indicates whether the plan directive is mandatory (`YES`) or not (`NO`) |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.2).

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/toc.htm) for information on resource plans in general
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/cd/E11882_01/appdev.112/e40758/toc.htm) for more information on creating resource plans with the `DBMS_RESOURCE_MANAGER` package