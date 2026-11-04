---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/USABLE_EDITIONS.html
tags:
  - oracle
  - 19c
  - reference
---

## 6.262 USABLE\_EDITIONS

`USABLE_EDITIONS` describes the usable editions of the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `EDITION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the edition |
| `PARENT_EDITION_NAME` | `VARCHAR2(128)` |  | Name of the parent edition for this edition |

See Also:

[Oracle Database Development Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=ADFNS99923) for more information about editions