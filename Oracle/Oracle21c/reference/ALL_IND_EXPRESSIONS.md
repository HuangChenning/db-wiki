---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_IND_EXPRESSIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.231 ALL\_IND\_EXPRESSIONS

`ALL_IND_EXPRESSIONS` describes the expressions of function-based indexes on tables accessible to the current user.

Related Views

- `DBA_IND_EXPRESSIONS` describes the expressions of all function-based indexes in the database.
- `USER_IND_EXPRESSIONS` describes the expressions of function-based indexes on tables owned by the current user. This view does not display the `INDEX_OWNER` or `TABLE_OWNER` columns.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `INDEX_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the index |
| `INDEX_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the index |
| `TABLE_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the table or cluster |
| `TABLE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the table or cluster |
| `COLUMN_EXPRESSION` | `LONG` |  | Function-based index expression defining the column |
| `COLUMN_POSITION` | `NUMBER` | `NOT NULL` | Position of the column or attribute within the index |

See Also:

- " [DBA\_IND\_EXPRESSIONS](DBA_IND_EXPRESSIONS.md) "
- " [USER\_IND\_EXPRESSIONS](USER_IND_EXPRESSIONS.md) "