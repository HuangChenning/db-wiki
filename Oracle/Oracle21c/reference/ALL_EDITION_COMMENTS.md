---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_EDITION_COMMENTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.175 ALL\_EDITION\_COMMENTS

`ALL_EDITION_COMMENTS` describes the comments on the editions accessible to the current user.

Related View

`DBA_EDITION_COMMENTS` describes the comments on all editions in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `EDITION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the edition |
| `COMMENTS` | `VARCHAR2(4000)` |  | Edition comments |

See Also:

" [DBA\_EDITION\_COMMENTS](DBA_EDITION_COMMENTS.md) "