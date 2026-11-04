---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_SQLJ_TYPE_METHODS.html
tags:
  - oracle
  - 21c
  - reference
---

## 4.79 ALL\_SQLJ\_TYPE\_METHODS

`ALL_SQLJ_TYPE_METHODS` describes the methods of the SQLJ object types accessible to the current user.

Related Views

- `DBA_SQLJ_TYPE_METHODS` describes the methods of all SQLJ object types in the database.
- `USER_SQLJ_TYPE_METHODS` describes the methods of the SQLJ object types owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the type |
| `TYPE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the type |
| `METHOD_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the method |
| `EXTERNAL_VAR_NAME` | `VARCHAR2(4000)` |  | Name of the external variable |
| `METHOD_NO` | `NUMBER` | `NOT NULL` | Method number that distinguishes overloaded methods (not to be used as an ID number) |
| `METHOD_TYPE` | `VARCHAR2(6)` |  | Type of the method:  - `MAP` - `ORDER` - `PUBLIC` |
| `PARAMETERS` | `NUMBER` | `NOT NULL` | Number of parameters to the method |
| `RESULTS` | `NUMBER` | `NOT NULL` | Number of results returned by the method |
| `FINAL` | `VARCHAR2(3)` |  | Indicates whether the method is final (`YES`) or not (`NO`) |
| `INSTANTIABLE` | `VARCHAR2(3)` |  | Indicates whether the method is instantiable (`YES`) or not (`NO`) |
| `OVERRIDING` | `VARCHAR2(3)` |  | Indicates whether the method is overriding a supertype method (`YES`) or not (`NO`) |
| `INHERITED` | `VARCHAR2(3)` |  | Indicates whether the method is inherited from a supertype (`YES`) or not (`NO`) |

See Also:

- " [DBA\_SQLJ\_TYPE\_METHODS](DBA_SQLJ_TYPE_METHODS.md) "
- " [USER\_SQLJ\_TYPE\_METHODS](USER_SQLJ_TYPE_METHODS.md) "