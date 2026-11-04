---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_EDITIONS.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_EDITIONS` describes the editions accessible to the current user.

Related View

`DBA_EDITIONS` describes all editions in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `EDITION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the edition |
| `PARENT_EDITION_NAME` | `VARCHAR2(128)` |  | Name of the parent edition for this edition |
| `USABLE` | `VARCHAR2(3)` |  | Indicates whether the edition is usable (`YES`) or unusable (`NO`) |

See Also:

- " [DBA\_EDITIONS](DBA_EDITIONS.md) "
- [Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ADFNS99923) for more information about editions