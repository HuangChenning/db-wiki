---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_EDITION_COMMENTS.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_EDITION_COMMENTS` describes the comments on the editions accessible to the current user.

Related View

`DBA_EDITION_COMMENTS` describes the comments on all editions in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `EDITION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the edition |
| `COMMENTS` | `VARCHAR2(4000)` |  | Edition comments |

See Also:

" [DBA\_EDITION\_COMMENTS](DBA_EDITION_COMMENTS.md) "