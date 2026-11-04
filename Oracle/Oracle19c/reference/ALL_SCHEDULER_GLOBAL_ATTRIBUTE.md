---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ALL_SCHEDULER_GLOBAL_ATTRIBUTE.html
tags:
  - oracle
  - 19c
  - reference
---

## 3.43 ALL\_SCHEDULER\_GLOBAL\_ATTRIBUTE

`ALL_SCHEDULER_GLOBAL_ATTRIBUTE` displays the values of all scheduler attributes (for example, `DEFAULT_TIMEZONE` and `CURRENT_OPEN_WINDOW`).

Related View

`DBA_SCHEDULER_GLOBAL_ATTRIBUTE` displays the values of all scheduler attributes in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ATTRIBUTE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the Scheduler attribute |
| `VALUE` | `VARCHAR2(256)` |  | Value of the Scheduler attribute |

See Also:

" [DBA\_SCHEDULER\_GLOBAL\_ATTRIBUTE](DBA_SCHEDULER_GLOBAL_ATTRIBUTE.md) "