---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_COLL_TYPES.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.137 ALL\_COLL\_TYPES

`ALL_COLL_TYPES` describes all named collection types (varrays and nested tables) accessible to the current user.

Related Views

- `DBA_COLL_TYPES` describes all named collection types in the database.
- `USER_COLL_TYPES` describes all named collection types owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the collection |
| `TYPE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the collection |
| `COLL_TYPE` | `VARCHAR2(128)` | `NOT NULL` | Description of the collection, such as `VARYING` `ARRAY`, \[nested\] `TABLE` |
| `UPPER_BOUND` | `NUMBER` |  | For varrays only, maximum size |
| `ELEM_TYPE_MOD` | `VARCHAR2(7)` |  | Type modifier of the element |
| `ELEM_TYPE_OWNER` | `VARCHAR2(128)` |  | Owner of the type upon which the collection is based. This value is useful primarily for a user-defined type. |
| `ELEM_TYPE_NAME` | `VARCHAR2(128)` |  | Name of the data type or user-defined type upon which the collection is based |
| `LENGTH` | `NUMBER` |  | Length of `CHAR` elements or maximum length of `VARCHAR` or `VARCHAR2` elements |
| `PRECISION` | `NUMBER` |  | Decimal precision of `NUMBER` or `DECIMAL` elements; binary precision of `FLOAT` elements |
| `SCALE` | `NUMBER` |  | Scale of `NUMBER` or `DECIMAL` elements |
| `CHARACTER_SET_NAME` | `VARCHAR2(44)` |  | Name of the character set (`CHAR_CS` \| `NCHAR_CS`) |
| `ELEM_STORAGE` | `VARCHAR2(7)` |  | Obsolete column |
| `NULLS_STORED` | `VARCHAR2(3)` |  | Obsolete column |
| `CHAR_USED` | `VARCHAR2(1)` |  | Indicates whether the attribute uses `BYTE` length semantics (`B`) or `CHAR` length semantics (`C`). For `NCHAR` and `NVARCHAR2` attribute types, this value is always `C`. |

See Also:

- " [DBA\_COLL\_TYPES](DBA_COLL_TYPES.md) "
- " [USER\_COLL\_TYPES](USER_COLL_TYPES.md) "