---
title: ALL_REWRITE_EQUIVALENCES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2026.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_REWRITE_EQUIVALENCES` describes the rewrite equivalences accessible to the current user.

Related Views

- `DBA_REWRITE_EQUIVALENCES` describes all rewrite equivalences in the database.
- `USER_REWRITE_EQUIVALENCES` describes the rewrite equivalences owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the rewrite equivalence |
| `NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the rewrite equivalence |
| `SOURCE_STMT` | `CLOB` |  | Source statement of the rewrite equivalence |
| `DESTINATION_STMT` | `CLOB` |  | Destination of the rewrite equivalence |
| `REWRITE_MODE` | `VARCHAR2(10)` |  | Rewrite mode of the rewrite equivalence: |

See Also:

- ["DBA\_REWRITE\_EQUIVALENCES"](statviews_4217.md)
- ["USER\_REWRITE\_EQUIVALENCES"](statviews_5415.md)