---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_TYPE_ATTRS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.130 ALL\_TYPE\_ATTRS

`ALL_TYPE_ATTRS` describes the attributes of the object types accessible to the current user.

Related Views

- `DBA_TYPE_ATTRS` describes the attributes of all object types in the database. This view does not include the `CHAR_USED` column.
- `USER_TYPE_ATTRS` describes the attributes of the object types owned by the current user. This view does not display the `OWNER` or `CHAR_USED` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` |  | Owner of the type |
| `TYPE_NAME` | `VARCHAR2(128)` |  | Name of the type |
| `ATTR_NAME` | `VARCHAR2(128)` |  | Name of the attribute |
| `ATTR_TYPE_MOD` | `VARCHAR2(7)` |  | Type modifier of the attribute:  - `REF` - `POINTER` |
| `ATTR_TYPE_OWNER` | `VARCHAR2(128)` |  | Owner of the type of the attribute |
| `ATTR_TYPE_NAME` | `VARCHAR2(128)` |  | Name of the type of the attribute |
| `LENGTH` | `NUMBER` |  | Length of the `CHAR` attribute, or maximum length of the `VARCHAR` or `VARCHAR2` attribute. |
| `PRECISION` | `NUMBER` |  | Decimal precision of the `NUMBER` or `DECIMAL` attribute, or binary precision of the `FLOAT` attribute. |
| `SCALE` | `NUMBER` |  | Scale of the `NUMBER` or `DECIMAL` attribute |
| `CHARACTER_SET _NAME` | `VARCHAR2(44)` |  | Character set name of the attribute (`CHAR_CS` or `NCHAR_CS`) |
| `ATTR_NO` | `NUMBER` |  | Syntactical order number or position of the attribute as specified in the type specification or ` CREATE TYPE` statement (not to be used as an ID number) |
| `INHERITED` | `VARCHAR2(3)` |  | Indicates whether the attribute is inherited from a supertype (`YES`) or not (`NO`) |
| `CHAR_USED` | `VARCHAR2(1)` |  | Indicates whether the attribute uses `BYTE` length semantics (`B`) or `CHAR` length semantics (`C`). For `NCHAR` and `NVARCHAR2` attribute types, this value is always `C`. |

See Also:

- " [DBA\_TYPE\_ATTRS](DBA_TYPE_ATTRS.md) "
- " [USER\_TYPE\_ATTRS](USER_TYPE_ATTRS.md) "