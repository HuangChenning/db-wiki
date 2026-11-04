---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_SCHEDULER_JOB_ARGS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.49 ALL\_SCHEDULER\_JOB\_ARGS

`ALL_SCHEDULER_JOB_ARGS` displays information about the arguments of the Scheduler jobs accessible to the current user.

Related Views

- `DBA_SCHEDULER_JOB_ARGS` displays information about the arguments of all Scheduler jobs in the database.
- `USER_SCHEDULER_JOB_ARGS` displays information about the arguments of the Scheduler jobs owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the job to which the argument belongs |
| `JOB_NAME` | `VARCHAR2(128)` |  | Name of the job to which the argument belongs |
| `ARGUMENT_NAME` | `VARCHAR2(128)` |  | Optional name of the argument |
| `ARGUMENT_POSITION` | `NUMBER` |  | Position of the argument in the argument list |
| `ARGUMENT_TYPE` | `VARCHAR2(257)` |  | Data type of the argument |
| `VALUE` | `VARCHAR2(4000)` |  | Value of the argument (in string format) if the argument is a string |
| `ANYDATA_VALUE` | `ANYDATA` |  | Value of the argument (in AnyData format) |
| `OUT_ARGUMENT` | `VARCHAR2(5)` |  | Reserved for future use |

See Also:

- " [DBA\_SCHEDULER\_JOB\_ARGS](DBA_SCHEDULER_JOB_ARGS.md) "
- " [USER\_SCHEDULER\_JOB\_ARGS](USER_SCHEDULER_JOB_ARGS.md) "