---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_OPBINDINGS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.298 ALL\_OPBINDINGS

`ALL_OPBINDINGS` describes the binding functions and methods on the operators accessible to the current user.

Related Views

- `DBA_OPBINDINGS` describes the binding functions and methods on all operators in the database.
- `USER_OPBINDINGS` describes the binding functions and methods on the operators owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the operator |
| `OPERATOR_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the operator |
| `BINDING#` | `NUMBER` | `NOT NULL` | Binding number of the operator |
| `FUNCTION_NAME` | `VARCHAR2(92)` |  | Name of the binding function or method as specified by the user |
| `RETURN_SCHEMA` | `VARCHAR2(128)` |  | Name of the schema of the return type if the return type of the binding is an object type |
| `RETURN_TYPE` | `VARCHAR2(128)` |  | Name of the return type |
| `IMPLEMENTATION_TYPE_SCHEMA` | `VARCHAR2(128)` |  | If the operator was created `WITH INDEX CONTEXT` or `SCAN CONTEXT`, then this column displays the schema of the implementation type used by the functional implementation of the operator as a scan context (null if the operator was created without this syntax).  See Also: the `CREATE OPERATOR` statement in [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SQLRF01304) |
| `IMPLEMENTATION_TYPE` | `VARCHAR2(128)` |  | If the operator was created `WITH INDEX CONTEXT` or `SCAN CONTEXT`, then this column displays the name of the implementation type used by the functional implementation of the operator as a scan context (null if the operator was created without this syntax).  See Also: the `CREATE OPERATOR` statement in [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SQLRF01304) |
| `PROPERTY` | `VARCHAR2(43)` |  | Property of the operator binding:  - `WITH INDEX CONTEXT` - `COMPUTE ANCILLARY DATA` - `ANCILLARY TO` - `WITH COLUMN CONTEXT` - `WITH INDEX, COLUMN CONTEXT` - `COMPUTE ANCILLARY DATA, WITH COLUMN CONTEXT` |

See Also:

- " [DBA\_OPBINDINGS](DBA_OPBINDINGS.md) "
- " [USER\_OPBINDINGS](USER_OPBINDINGS.md) "