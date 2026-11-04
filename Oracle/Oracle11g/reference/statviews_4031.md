---
title: DBA_HIST_RULE_SET
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4031.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_HIST_RULE_SET` displays historical information about rule set statistics.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the rule set |
| `NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the rule set |
| `STARTUP_TIME` | `DATE` | `NOT NULL` | Startup time of the instance |
| `CPU_TIME` | `NUMBER` |  | Total CPU time (in hundredths of a second) spent in evaluation of the rule set |
| `ELAPSED_TIME` | `NUMBER` |  | Total elapsed time (in hundredths of a second) spent in evaluation of the rule set |
| `EVALUATIONS` | `NUMBER` |  | Number of evaluations on the rule set |
| `SQL_FREE_EVALUATIONS` | `NUMBER` |  | Number of evaluations on the rule set which did not internally issue SQL to evaluate rules |
| `SQL_EXECUTIONS` | `NUMBER` |  | Total number of SQL statements executed during evaluation of the rule set |
| `RELOADS` | `NUMBER` |  | Number of times the rule set object was reloaded in shared memory |