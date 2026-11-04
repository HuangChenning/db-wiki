---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_REWRITE_EQUIVALENCES.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.32 ALL\_REWRITE\_EQUIVALENCES

`ALL_REWRITE_EQUIVALENCES` describes the rewrite equivalences accessible to the current user.

Related Views

- `DBA_REWRITE_EQUIVALENCES` describes all rewrite equivalences in the database.
- `USER_REWRITE_EQUIVALENCES` describes the rewrite equivalences owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the rewrite equivalence |
| `NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the rewrite equivalence |
| `SOURCE_STMT` | `CLOB` |  | Source statement of the rewrite equivalence |
| `DESTINATION_STMT` | `CLOB` |  | Destination of the rewrite equivalence |
| `REWRITE_MODE` | `VARCHAR2(10)` |  | Rewrite mode of the rewrite equivalence:  - `DISABLED` - `TEXT_MATCH` - `GENERAL` - `RECURSIVE` |

See Also:

- " [DBA\_REWRITE\_EQUIVALENCES](DBA_REWRITE_EQUIVALENCES.md) "
- " [USER\_REWRITE\_EQUIVALENCES](USER_REWRITE_EQUIVALENCES.md) "