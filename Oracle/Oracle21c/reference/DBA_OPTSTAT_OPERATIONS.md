---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_OPTSTAT_OPERATIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.222 DBA\_OPTSTAT\_OPERATIONS

`DBA_OPTSTAT_OPERATIONS` contains a history of statistics operations performed at the schema and database level using the `DBMS_STATS` package.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ID` | `NUMBER` |  | Internal ID of the statistics operation |
| `OPERATION` | `VARCHAR2(64)` |  | Operation name |
| `TARGET` | `VARCHAR2(64)` |  | Target on which the operation was performed |
| `START_TIME` | `TIMESTAMP(6) WITH TIME ZONE` |  | Time at which the operation started |
| `END_TIME` | `TIMESTAMP(6) WITH TIME ZONE` |  | Time at which the operation ended |
| `STATUS` | `VARCHAR2(49)` |  | Current operation status. Possible values are:  - `IN PROGRESS`: Operation is currently running - `COMPLETED`: Operation has completed successfully - `FAILED`: Operation has failed - `TIMED OUT`: Maintenance window was not enough to complete this operation (applies only to automatic statistics gathering) |
| `JOB_NAME` | `VARCHAR2(32)` |  | Name of the scheduler job that executes this operation (for example, a user scheduled statistics gathering job) |
| `SESSION_ID` | `NUMBER` |  | ID of the session in which this operation is invoked |
| `NOTES` | `VARCHAR2(4000)` |  | Notes about the operation, such as a failure message for operations with status FAILED |

See Also:

- " [DBA\_OPTSTAT\_OPERATION\_TASKS](DBA_OPTSTAT_OPERATION_TASKS.md) "
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS059) for more information about the `DBMS_STATS` package
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS67547) for more information about the `DBMS_REPAIR.ADMIN_TABLES` procedure
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS67551) for more information about the `DBMS_REPAIR.DUMP_ORPHAN_KEYS` procedure