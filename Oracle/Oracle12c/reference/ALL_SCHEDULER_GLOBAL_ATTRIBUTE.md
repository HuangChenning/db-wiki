---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_SCHEDULER_GLOBAL_ATTRIBUTE.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_SCHEDULER_GLOBAL_ATTRIBUTE` displays the values of all scheduler attributes (for example, `DEFAULT_TIMEZONE` and `CURRENT_OPEN_WINDOW`).

Related View

`DBA_SCHEDULER_GLOBAL_ATTRIBUTE` displays the values of all scheduler attributes in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ATTRIBUTE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the Scheduler attribute |
| `VALUE` | `VARCHAR2(128)` |  | Value of the Scheduler attribute |

See Also:

" [DBA\_SCHEDULER\_GLOBAL\_ATTRIBUTE](DBA_SCHEDULER_GLOBAL_ATTRIBUTE.md) "