---
title: ALL_OPBINDINGS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1162.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_OPBINDINGS` describes the binding functions and methods on the operators accessible to the current user.

Related Views

- `DBA_OPBINDINGS` describes the binding functions and methods on all operators in the database.
- `USER_OPBINDINGS` describes the binding functions and methods on the operators owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the operator |
| `OPERATOR_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the operator |
| `BINDING#` | `NUMBER` | `NOT NULL` | Binding number of the operator |
| `FUNCTION_NAME` | `VARCHAR2(92)` |  | Name of the binding function or method as specified by the user |
| `RETURN_SCHEMA` | `VARCHAR2(30)` |  | Name of the schema of the return type if the return type of the binding is an object type |
| `RETURN_TYPE` | `VARCHAR2(30)` |  | Name of the return type |
| `IMPLEMENTATION_TYPE_SCHEMA` | `VARCHAR2(30)` |  | If the operator was created `WITH INDEX CONTEXT` or `SCAN CONTEXT`, then this column displays the schema of the implementation type used by the functional implementation of the operator as a scan context (null if the operator was created without this syntax).  See Also: the `CREATE OPERATOR` statement in [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_6004.htm#SQLRF01304) |
| `IMPLEMENTATION_TYPE` | `VARCHAR2(30)` |  | If the operator was created `WITH INDEX CONTEXT` or `SCAN CONTEXT`, then this column displays the name of the implementation type used by the functional implementation of the operator as a scan context (null if the operator was created without this syntax).  See Also: the `CREATE OPERATOR` statement in [Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/statements_6004.htm#SQLRF01304) |
| `PROPERTY` | `VARCHAR2(43)` |  | Property of the operator binding: |

See Also:

- ["DBA\_OPBINDINGS"](statviews_4162.md)
- ["USER\_OPBINDINGS"](statviews_5380.md)