---
title: ALL_TYPE_METHODS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2125.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_TYPE_METHODS` describes the methods of the object types accessible to the current user.

Related Views

- `DBA_TYPE_METHODS` describes the methods of all object types in the database.
- `USER_TYPE_METHODS` describes the methods of the object types owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the type |
| `TYPE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the type |
| `METHOD_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the method |
| `METHOD_NO` | `NUMBER` | `NOT NULL` | Method number for distinguishing overloaded methods (not to be used as ID number) |
| `METHOD_TYPE` | `VARCHAR2(6)` |  | Type of the method: - `MAP` - `ORDER` - `PUBLIC` |
| `PARAMETERS` | `NUMBER` | `NOT NULL` | Number of parameters to the method |
| `RESULTS` | `NUMBER` | `NOT NULL` | Number of results returned by the method |
| `FINAL` | `VARCHAR2(3)` |  | Indicates whether the method is final (`YES`) or not (`NO`) |
| `INSTANTIABLE` | `VARCHAR2(3)` |  | Indicates whether the method is instantiable (`YES`) or not (`NO`) |
| `OVERRIDING` | `VARCHAR2(3)` |  | Indicates whether the method is overriding a supertype method (`YES`) or not (`NO`) |
| `INHERITED` | `VARCHAR2(3)` |  | Indicates whether the method is inherited from a supertype (`YES`) or not (`NO`) |

See Also:

- ["DBA\_TYPE\_METHODS"](statviews_5075.md)
- ["USER\_TYPE\_METHODS"](statviews_5501.md)