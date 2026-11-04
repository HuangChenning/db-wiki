---
title: DBA_TUNE_MVIEW
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5073.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_TUNE_MVIEW` displays the result of executing the `DBMS_ADVISOR.TUNE_MVIEW` procedure.

Related View

`USER_TUNE_MVIEW` displays the result of executing the `DBMS_ADVISOR.TUNE_MVIEW` procedure. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the task |
| `TASK_NAME` | `VARCHAR2(30)` |  | Name of the task |
| `ACTION_ID` | `NUMBER` | `NOT NULL` | Identifier of the action |
| `SCRIPT_TYPE` | `VARCHAR2(14)` |  | Type of the script: |
| `STATEMENT` | `CLOB` |  | Action statement |

See Also:

["USER\_TUNE\_MVIEW"](statviews_5499.md)