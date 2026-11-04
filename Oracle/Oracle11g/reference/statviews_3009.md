---
title: DBA_ADVISOR_ACTIONS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3009.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_ADVISOR_ACTIONS` displays information about the actions associated with all recommendations in the database. Each action is specified by the `COMMAND` and `ATTR1` through `ATTR6` columns. Each command defines how the attribute columns will be used.

Related View

`USER_ADVISOR_ACTIONS` displays information about the actions associated with the recommendations owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the task |
| `TASK_ID` | `NUMBER` | `NOT NULL` | Identifier of the task |
| `TASK_NAME` | `VARCHAR2(30)` |  | Name of the task |
| `EXECUTION_NAME` | `VARCHAR2(30)` |  | The name of the task execution with which this entry (row) is associated |
| `REC_ID` | `NUMBER` | `NOT NULL` | Recommendation associated with the action |
| `ACTION_ID` | `NUMBER` | `NOT NULL` | Unique identifier for the action |
| `OBJECT_ID` | `NUMBER` |  | Object associated with the action |
| `COMMAND` | `VARCHAR2(64)` |  | Command to be executed  See Also: `DBA_ADVISOR_COMMANDS` for a list of commands |
| `COMMAND_ID` | `NUMBER` | `NOT NULL` | ID of the command to be executed  See Also: `DBA_ADVISOR_COMMANDS` for a list of commands |
| `FLAGS` | `NUMBER` |  | Advisor-specific flags |
| `ATTR1` | `VARCHAR2(4000)` |  | Parameters defining the command |
| `ATTR2` | `VARCHAR2(4000)` |  | Parameters defining the command |
| `ATTR3` | `VARCHAR2(4000)` |  | Parameters defining the command |
| `ATTR4` | `VARCHAR2(4000)` |  | Parameters defining the command |
| `ATTR5` | `CLOB` |  | Parameters defining the command; to be used if the text is significantly large (for example, a SQL statement defining a materialized view) |
| `ATTR6` | `CLOB` |  | Parameters defining the command; to be used if the text is significantly large (for example, a SQL statement defining a materialized view) |
| `NUM_ATTR1` | `NUMBER` |  | General numeric attribute |
| `NUM_ATTR2` | `NUMBER` |  | General numeric attribute |
| `NUM_ATTR3` | `NUMBER` |  | General numeric attribute |
| `NUM_ATTR4` | `NUMBER` |  | General numeric attribute |
| `NUM_ATTR5` | `NUMBER` |  | General numeric attribute |
| `MESSAGE` | `VARCHAR2(4000)` |  | Message associated with the action |
| `FILTERED` | `VARCHAR2(1)` |  | A value of `Y` means that the row in the view was filtered out by a directive (or a combination of directives). A value of `N` means that the row was not filtered. |

See Also:

["USER\_ADVISOR\_ACTIONS"](statviews_5199.md)