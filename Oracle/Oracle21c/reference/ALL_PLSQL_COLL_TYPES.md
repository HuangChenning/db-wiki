---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_PLSQL_COLL_TYPES.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.9 ALL\_PLSQL\_COLL\_TYPES

`ALL_PLSQL_COLL_TYPES` describes named PL/SQL collection types accessible to the user.

Related Views

- `DBA_PLSQL_COLL_TYPES` describes all named PL/SQL collection types in the database. This view does not display the `CHAR_USED` column.
- `USER_PLSQL_COLL_TYPES` describes the user's own named PL/SQL collection types. This view does not display the `OWNER` or `CHAR_USED` columns.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the type |
| `TYPE_NAME` | `VARCHAR2(128)` |  | Name of the type |
| `PACKAGE_NAME` | `VARCHAR2(128)` |  | Name of the package containing the collection |
| `COLL_TYPE` | `VARCHAR2(128)` |  | Collection type |
| `UPPER_BOUND` | `NUMBER` |  | The upper bound of a varray or length constraint of an index by `VARCHAR2` table |
| `ELEM_TYPE_OWNER` | `VARCHAR2(128)` |  | Owner of the type of the element |
| `ELEM_TYPE_NAME` | `VARCHAR2(136)` |  | Name of the type of the element |
| `ELEM_TYPE_PACKAGE` | `VARCHAR2(128)` |  | Name of the package containing the element |
| `LENGTH` | `NUMBER` |  | Length of the `CHAR` element or maximum length of the `VARCHAR` or `VARCHAR2` element |
| `PRECISION` | `NUMBER` |  | Decimal precision of the `NUMBER` or `DECIMAL` element or binary precision of the `FLOAT` element |
| `SCALE` | `NUMBER` |  | Scale of the `NUMBER` or `DECIMAL` element |
| `CHARACTER_SET_NAME` | `VARCHAR2(44)` |  | Character set name of the element |
| `ELEM_STORAGE` | `VARCHAR2(7)` |  | Storage optimization specification for VARRAY of numeric elements |
| `NULLS_STORED` | `VARCHAR2(3)` |  | Indicates whether null information is stored with each `VARRAY` element (`YES`) or not (`NO`) |
| `CHAR_USED` | `VARCHAR2(1)` |  | `C` if the width was specified in characters, `B` if in bytes |
| `INDEX_BY` | `VARCHAR2(14)` |  | Index by `BINARY_INTEGER` or `VARCHAR2` |
| `ELEM_TYPE_MOD` | `VARCHAR2(7)` |  | Type modifier of the element |

See Also:

- " [DBA\_PLSQL\_COLL\_TYPES](DBA_PLSQL_COLL_TYPES.md) "
- " [USER\_PLSQL\_COLL\_TYPES](USER_PLSQL_COLL_TYPES.md) "