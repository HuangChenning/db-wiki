---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ROLLING_PLAN.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.299 DBA\_ROLLING\_PLAN

`DBA_ROLLING_PLAN` displays the instructions which constitute the active upgrade plan.

Each row in `DBA_ROLLING_PLAN` identifies a specific instruction scheduled to execute at a specific database. Instructions are created as a result of successful calls to the `DBMS_ROLLING.BUILD_PLAN` procedure.

During execution, groups of instructions are scheduled in batches to execute at remote databases. Groups of instructions are guaranteed to complete in `BATCHID` order.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `REVISION` | `NUMBER` |  | Plan revision number associated with an instruction |
| `BATCHID` | `NUMBER` |  | Identifier for a batch of instructions which are requested together |
| `INSTID` | `NUMBER` |  | Identifier for a single instruction |
| `SOURCE` | `VARCHAR2(128)` |  | Database unique name where an instruction executes |
| `TARGET` | `VARCHAR2(128)` |  | The site where a given instruction will execute |
| `PHASE` | `VARCHAR2(14)` |  | rolling operation phase in which an instruction executes |
| `STATUS` | `VARCHAR2(7)` |  | Scheduling status of the instruction |
| `PROGRESS` | `VARCHAR2(10)` |  | Execution progress of the instruction |
| `DESCRIPTION` | `VARCHAR2(256)` |  | Description of the instruction |
| `EXEC_STATUS` | `NUMBER` |  | Status code returned from instruction execution |
| `EXEC_INFO` | `VARCHAR2(256)` |  | Supplemental information obtained during instruction execution |
| `EXEC_TIME` | `TIMESTAMP(6)` |  | Time of instruction execution |
| `FINISH_TIME` | `TIMESTAMP(6)` |  | Time of instruction completion |

See Also:

- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SBYDB5214) for more information about rolling operations.
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS73534) for more information about the `DBMS_ROLLING` package