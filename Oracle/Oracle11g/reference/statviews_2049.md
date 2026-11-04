---
title: ALL_SCHEDULER_PROGRAMS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2049.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_SCHEDULER_PROGRAMS` displays information about the Scheduler programs accessible to the current user.

Related Views

- `DBA_SCHEDULER_PROGRAMS` displays information about all Scheduler programs in the database.
- `USER_SCHEDULER_PROGRAMS` displays information about the Scheduler programs owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the Scheduler program |
| `PROGRAM_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the Scheduler program |
| `PROGRAM_TYPE` | `VARCHAR2(16)` |  | Type of the program action: - `PLSQL_BLOCK` - `STORED_PROCEDURE` - `EXECUTABLE` |
| `PROGRAM_ACTION` | `VARCHAR2(4000)` |  | String specifying the program action |
| `NUMBER_OF_ARGUMENTS` | `NUMBER` |  | Number of arguments accepted by the program |
| `ENABLED` | `VARCHAR2(5)` |  | Indicates whether the program is enabled (`TRUE`) or disabled (`FALSE`) |
| `DETACHED` | `VARCHAR2(5)` |  | This column is for internal use |
| `SCHEDULE_LIMIT` | `INTERVAL DAY(3) TO SECOND(0)` |  | Maximum delay in running the program after the scheduled start |
| `PRIORITY` | `NUMBER` |  | Priority of the program |
| `WEIGHT` | `NUMBER` |  | Weight of the program |
| `MAX_RUNS` | `NUMBER` |  | Maximum number of runs of any job based on this program |
| `MAX_FAILURES` | `NUMBER` |  | Maximum number of failures of any job based on this program |
| `MAX_RUN_DURATION` | `INTERVAL DAY(3) TO SECOND(0)` |  | Maximum amount of time this program can run |
| `NLS_ENV` | `VARCHAR2(4000)` |  | NLS environment in which the program was created |
| `COMMENTS` | `VARCHAR2(240)` |  | Comments on the program |

See Also:

- ["DBA\_SCHEDULER\_PROGRAMS"](statviews_4254.md)
- ["USER\_SCHEDULER\_PROGRAMS"](statviews_5438.md)