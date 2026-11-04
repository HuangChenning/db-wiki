---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_PLSQL_TYPES.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.12 ALL\_PLSQL\_TYPES

`ALL_PLSQL_TYPES` describes the PL/SQL types accessible to the user.

Related Views

- `DBA_PLSQL_TYPES` describes all the PL/SQL types in the database.
- `USER_PLSQL_TYPES` describes the user's own PL/SQL types. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the type |
| `TYPE_NAME` | `VARCHAR2(136)` |  | Name of the type |
| `PACKAGE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the package containing the type |
| `TYPE_OID` | `RAW(16)` | `NOT NULL` | Object identifier (OID) of the type |
| `TYPECODE` | `VARCHAR2(58)` |  | Typecode of the type |
| `ATTRIBUTES` | `NUMBER` |  | Number of attributes in the type |
| `CONTAINS_PLSQL` | `VARCHAR2(3)` |  | Indicates whether the type contains PL/SQL-specific data types (`YES`) or not (`NO`) |

See Also:

- " [DBA\_PLSQL\_TYPES](DBA_PLSQL_TYPES.md) "
- " [USER\_PLSQL\_TYPES](USER_PLSQL_TYPES.md) "