---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_ADVISOR_TEMPLATES.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_ADVISOR_TEMPLATES` displays information about all templates in the database.

Related View

`USER_ADVISOR_TEMPLATES` displays information about the templates owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the task |
| `TASK_ID` | `NUMBER` | `NOT NULL` | Unique identifier of the task |
| `TASK_NAME` | `VARCHAR2(128)` |  | Name of the task |
| `DESCRIPTION` | `VARCHAR2(256)` |  | User-supplied description of the task |
| `ADVISOR_NAME` | `VARCHAR2(128)` |  | Advisor associated with the task |
| `CREATED` | `DATE` | `NOT NULL` | Creation date of the task |
| `LAST_MODIFIED` | `DATE` | `NOT NULL` | Date on which the task was last modified |
| `SOURCE` | `VARCHAR2(128)` |  | Optional task or template on which the template was based |
| `READ_ONLY` | `VARCHAR2(5)` |  | Indicates whether the task can be modified or deleted (`TRUE`) or not (`FALSE`) |

See Also:

" [USER\_ADVISOR\_TEMPLATES](USER_ADVISOR_TEMPLATES.md) "