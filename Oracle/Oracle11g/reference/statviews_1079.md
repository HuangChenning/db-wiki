---
title: ALL_EDITION_COMMENTS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1079.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_EDITION_COMMENTS` describes the comments on the editions accessible to the current user.

Related View

`DBA_EDITION_COMMENTS` describes the comments on all editions in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `EDITION_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the edition |
| `COMMENTS` | `VARCHAR2(4000)` |  | Edition comments |

See Also:

["DBA\_EDITION\_COMMENTS"](statviews_3160.md)