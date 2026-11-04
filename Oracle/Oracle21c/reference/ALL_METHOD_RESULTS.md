---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_METHOD_RESULTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.271 ALL\_METHOD\_RESULTS

`ALL_METHOD_RESULTS` describes the method results of the object types accessible to the current user.

Related Views

- `DBA_METHOD_RESULTS` describes the method results of all object types in the database.
- `USER_METHOD_RESULTS` describes the method results of the object types owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the type |
| `TYPE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the type |
| `METHOD_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the method |
| `METHOD_NO` | `NUMBER` | `NOT NULL` | For an overloaded method, a number distinguishing this method from others of the same. Do not confuse this number with the object ID. |
| `RESULT_TYPE_MOD` | `VARCHAR2(7)` |  | Whether this result is a `REF` to another object |
| `RESULT_TYPE_OWNER` | `VARCHAR2(128)` |  | Owner of the type of the result |
| `RESULT_TYPE_NAME` | `VARCHAR2(128)` |  | Name of the type of the result |
| `CHARACTER_SET_NAME` | `VARCHAR2(44)` |  | Whether the character set or the method is fixed-length character set (`CHAR_CS`) or fixed-length national character set (`NCHAR_CS`), or a particular character set specified by the user |

See Also:

- " [DBA\_METHOD\_RESULTS](DBA_METHOD_RESULTS.md) "
- " [USER\_METHOD\_RESULTS](USER_METHOD_RESULTS.md) "