---
title: ALL_SCHEDULER_JOB_ARGS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2041.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_SCHEDULER_JOB_ARGS` displays information about the arguments of the Scheduler jobs accessible to the current user.

Related Views

- `DBA_SCHEDULER_JOB_ARGS` displays information about the arguments of all Scheduler jobs in the database.
- `USER_SCHEDULER_JOB_ARGS` displays information about the arguments of the Scheduler jobs owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the job to which the argument belongs |
| `JOB_NAME` | `VARCHAR2(30)` |  | Name of the job to which the argument belongs |
| `ARGUMENT_NAME` | `VARCHAR2(30)` |  | Optional name of the argument |
| `ARGUMENT_POSITION` | `NUMBER` |  | Position of the argument in the argument list |
| `ARGUMENT_TYPE` | `VARCHAR2(61)` |  | Datatype of the argument |
| `VALUE` | `VARCHAR2(4000)` |  | Value of the argument (in string format) if the argument is a string |
| `ANYDATA_VALUE` | `ANYDATA` |  | Value of the argument (in AnyData format) |
| `OUT_ARGUMENT` | `VARCHAR2(5)` |  | Reserved for future use |

See Also:

- ["DBA\_SCHEDULER\_JOB\_ARGS"](statviews_4245.md)
- ["USER\_SCHEDULER\_JOB\_ARGS"](statviews_5431.md)