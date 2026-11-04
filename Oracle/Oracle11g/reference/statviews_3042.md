---
title: DBA_ADVISOR_TEMPLATES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3042.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_ADVISOR_TEMPLATES` displays information about all templates in the database.

Related View

`USER_ADVISOR_TEMPLATES` displays information about the templates owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` |  | Owner of the task |
| `TASK_ID` | `NUMBER` | `NOT NULL` | Unique identifier of the task |
| `TASK_NAME` | `VARCHAR2(30)` |  | Name of the task |
| `DESCRIPTION` | `VARCHAR2(256)` |  | User-supplied description of the task |
| `ADVISOR_NAME` | `VARCHAR2(30)` |  | Advisor associated with the task |
| `CREATED` | `DATE` | `NOT NULL` | Creation date of the task |
| `LAST_MODIFIED` | `DATE` | `NOT NULL` | Date on which the task was last modified |
| `SOURCE` | `VARCHAR2(30)` |  | Optional task or template on which the template was based |
| `READ_ONLY` | `VARCHAR2(5)` |  | Indicates whether the task can be modified or deleted (`TRUE`) or not (`FALSE`) |

See Also:

["USER\_ADVISOR\_TEMPLATES"](statviews_5224.md)