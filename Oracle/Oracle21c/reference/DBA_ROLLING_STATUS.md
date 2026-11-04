---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_ROLLING_STATUS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.301 DBA\_ROLLING\_STATUS

`DBA_ROLLING_STATUS` displays the overall status of the rolling operation.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `REVISION` | `NUMBER` |  | Revision number of the current upgrade plan |
| `STATUS` | `VARCHAR2(12)` |  | Readiness of the facility to begin or resume the rolling operation |
| `PHASE` | `VARCHAR2(14)` |  | Current phase of the plan |
| `NEXT_INSTRUCTION` | `NUMBER` |  | Instruction ID of the next pending instruction |
| `REMAINING_INSTRUCTIONS` | `NUMBER` |  | Number of remaining instructions to execute in the plan |
| `COORDINATOR_INSTANCE` | `NUMBER` |  | Instance number from which the rolling operation is being coordinated |
| `COORDINATOR_PID` | `NUMBER` |  | Process PID in which the rolling operation is being coordinated |
| `ORIGINAL_PRIMARY` | `VARCHAR2(128)` |  | Database unique name of the original primary |
| `FUTURE_PRIMARY` | `VARCHAR2(128)` |  | Database unique name of the future primary |
| `TOTAL_DATABASES` | `NUMBER` |  | Number of total databases eligible to participate in the rolling operation |
| `PARTICIPATING_DATABASES` | `NUMBER` |  | Number of databases configured to participate in the rolling operation |
| `INIT_TIME` | `TIMESTAMP(6)` |  | Time of the last call to `DBMS_ROLLING`.`INIT_PLAN` |
| `BUILD_TIME` | `TIMESTAMP(6)` |  | Time of the last call to `DBMS_ROLLING`.`BUILD` |
| `START_TIME` | `TIMESTAMP(6)` |  | Time of the last call to `DBMS_ROLLING`.`START_UPGRADE` |
| `SWITCH_TIME` | `TIMESTAMP(6)` |  | Time of the last call to `DBMS_ROLLING`.`SWITCHOVER` |
| `FINISH_TIME` | `TIMESTAMP(6)` |  | Time of the last call to `DBMS_ROLLING`.`FINISH` |

See Also:

- [Oracle Data Guard Concepts and Administration](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SBYDB5214) for more information about rolling operations.
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS73534) for more information about the `DBMS_ROLLING` package