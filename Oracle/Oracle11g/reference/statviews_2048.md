---
title: ALL_SCHEDULER_PROGRAM_ARGS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2048.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_SCHEDULER_PROGRAM_ARGS` displays information about the arguments of the Scheduler programs accessible to the current user.

Related Views

- `DBA_SCHEDULER_PROGRAM_ARGS` displays information about the arguments of all Scheduler programs in the database.
- `USER_SCHEDULER_PROGRAM_ARGS` displays information about the arguments of the Scheduler programs owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the program to which the argument belongs |
| `PROGRAM_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the program to which the argument belongs |
| `ARGUMENT_NAME` | `VARCHAR2(30)` |  | Optional name of the argument |
| `ARGUMENT_POSITION` | `NUMBER` | `NOT NULL` | Position of the argument in the argument list |
| `ARGUMENT_TYPE` | `VARCHAR2(61)` |  | Datatype of the argument |
| `METADATA_ATTRIBUTE` | `VARCHAR2(19)` |  | Metadata attribute: |
| `DEFAULT_VALUE` | `VARCHAR2(4000)` |  | Default value taken by the argument (in string format) if the argument is a string |
| `DEFAULT_ANYDATA_VALUE` | `ANYDATA` |  | Default value taken by the argument (in AnyData format) |
| `OUT_ARGUMENT` | `VARCHAR2(5)` |  | Reserved for future use |

See Also:

- ["DBA\_SCHEDULER\_PROGRAM\_ARGS"](statviews_4253.md)
- ["USER\_SCHEDULER\_PROGRAM\_ARGS"](statviews_5437.md)