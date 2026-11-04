---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_PLSQL_TYPE_ATTRS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.11 ALL\_PLSQL\_TYPE\_ATTRS

`ALL_PLSQL_TYPE_ATTRS` describes the attributes of PL/SQL types accessible to the user.

Related Views

- `DBA_PLSQL_TYPE_ATTRS` describes the attributes of all PL/SQL types in the database.
- `USER_PLSQL_TYPE_ATTRS` describes the attributes of the user's own PL/SQL types. This view does not display the `OWNER` or `CHAR_USED` columns.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the type |
| `TYPE_NAME` | `VARCHAR2(136)` |  | Name of the type |
| `PACKAGE_NAME` | `VARCHAR2(128)` |  | Name of the package containing the type |
| `ATTR_NAME` | `VARCHAR2(128)` |  | Name of the attribute |
| `ATTR_TYPE_MOD` | `VARCHAR2(7)` |  | Type modifier of the attribute |
| `ATTR_TYPE_OWNER` | `VARCHAR2(128)` |  | Owner of the type of the attribute |
| `ATTR_TYPE_NAME` | `VARCHAR2(136)` |  | Name of the type of the attribute |
| `ATTR_TYPE_PACKAGE` | `VARCHAR2(128)` |  | Name of the package containing the attribute type |
| `LENGTH` | `NUMBER` |  | Length of the `CHAR` attribute or maximum length of the `VARCHAR` or `VARCHAR2` attribute |
| `PRECISION` | `NUMBER` |  | Decimal precision of the `NUMBER` or `DECIMAL` attribute or binary precision of the `FLOAT` attribute |
| `SCALE` | `NUMBER` |  | Scale of the `NUMBER` or `DECIMAL` attribute |
| `CHARACTER_SET_NAME` | `VARCHAR2(44)` |  | Character set name of the attribute |
| `ATTR_NO` | `NUMBER` |  | Syntactical order number or position of the attribute as specified in the type specification or `CREATE TYPE` statement (not to be used as ID number) |
| `CHAR_USED` | `VARCHAR2(1)` |  | `C` if the width was specified in characters, `B` if in bytes |

See Also:

- " [DBA\_PLSQL\_TYPE\_ATTRS](DBA_PLSQL_TYPE_ATTRS.md) "
- " [USER\_PLSQL\_TYPE\_ATTRS](USER_PLSQL_TYPE_ATTRS.md) "