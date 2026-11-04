---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_OBJECT_SIZE.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.210 DBA\_OBJECT\_SIZE

`DBA_OBJECT_SIZE` lists the sizes, in bytes, of various PL/SQL objects.

Related View

- `USER_OBJECT_SIZE` lists the size of PL/SQL objects owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the object |
| `NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the object |
| `TYPE` | `VARCHAR2(18)` |  | Type of the object: `TYPE, TYPE BODY, TABLE, VIEW, SYNONYM, SEQUENCE, PROCEDURE, FUNCTION, PACKAGE, PACKAGE BODY, JAVA SOURCE, JAVA CLASS` or `JAVA RESOURCE` |
| `SOURCE_SIZE` | `NUMBER` |  | Size of the source in bytes. Must be in memory during compilation, or dynamic recompilation. |
| `PARSED_SIZE ` | `NUMBER` |  | Size of the parsed form of the object, in bytes. Must be in memory when an object is being compiled that references this object. |
| `CODE_SIZE` | `NUMBER` |  | Code size, in bytes. Must be in memory when this object is executing. |
| `ERROR_SIZE ` | `NUMBER` |  | Size of error messages, in bytes. In memory during the compilation of the object when there are compilation errors. |

See Also:

" [USER\_OBJECT\_SIZE](USER_OBJECT_SIZE.md) "