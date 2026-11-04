---
title: ALL_METHOD_PARAMS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1138.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_METHOD_PARAMS` describes the method parameters of the object types accessible to the current user.

Related Views

- `DBA_METHOD_PARAMS` describes the method parameters of all object types in the database.
- `USER_METHOD_PARAMS` describes the method parameters of the object types owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the type |
| `TYPE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the type |
| `METHOD_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the method |
| `METHOD_NO` | `NUMBER` | `NOT NULL` | For an overloaded method, a number distinguishing this method from others of the same. Do not confuse this number with the object ID. |
| `PARAM_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the parameter |
| `PARAM_NO` | `NUMBER` | `NOT NULL` | Parameter number (position) |
| `PARAM_MODE` | `VARCHAR2(6)` |  | Mode of the parameter (`IN`, `OUT`, `IN OUT`) |
| `PARAM_TYPE_MOD` | `VARCHAR2(7)` |  | Whether this parameter is a `REF` to another object |
| `PARAM_TYPE_OWNER` | `VARCHAR2(30)` |  | Owner of the type of the parameter |
| `PARAM_TYPE_NAME` | `VARCHAR2(30)` |  | Name of the type of the parameter |
| `CHARACTER_SET_NAME` | `VARCHAR2(44)` |  | Whether the character set or the method is fixed-length character set (`CHAR_CS`) or fixed-length national character set (`NCHAR_CS`), or a particular character set specified by the user |

See Also:

- ["DBA\_METHOD\_PARAMS"](statviews_4132.md)
- ["USER\_METHOD\_PARAMS"](statviews_5353.md)