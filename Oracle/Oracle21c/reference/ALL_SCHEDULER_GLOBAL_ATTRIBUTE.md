---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_SCHEDULER_GLOBAL_ATTRIBUTE.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.44 ALL\_SCHEDULER\_GLOBAL\_ATTRIBUTE

`ALL_SCHEDULER_GLOBAL_ATTRIBUTE` displays the values of all scheduler attributes (for example, `DEFAULT_TIMEZONE` and `CURRENT_OPEN_WINDOW`).

Related View

`DBA_SCHEDULER_GLOBAL_ATTRIBUTE` displays the values of all scheduler attributes in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `ATTRIBUTE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the Scheduler attribute |
| `VALUE` | `VARCHAR2(256)` |  | Value of the Scheduler attribute |

See Also:

" [DBA\_SCHEDULER\_GLOBAL\_ATTRIBUTE](DBA_SCHEDULER_GLOBAL_ATTRIBUTE.md) "