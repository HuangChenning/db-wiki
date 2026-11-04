---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DBA_ADVISOR_COMMANDS.html
tags:
  - oracle
  - 19c
  - reference
---

## 4.15 DBA\_ADVISOR\_COMMANDS

`DBA_ADVISOR_COMMANDS` displays information about the commands used by all advisors in the database for specifying recommendation actions.

In addition to the set of commands in the `COMMAND` column of `V$SESSION`, the following additional commands are defined:

- `RUN ADVISOR`
- `CHECK EXECUTION PLAN`
- `ALTER PARAMETER`
- `ENABLE TRACE`

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `COMMAND_ID` | `NUMBER` |  | Identifier of the command |
| `COMMAND_NAME` | `VARCHAR2(64)` |  | Name of the command |