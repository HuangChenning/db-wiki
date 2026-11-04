---
title: DBA_OBJECT_SIZE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_4156.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_OBJECT_SIZE` lists the sizes, in bytes, of various PL/SQL objects.

Related View

- `USER_OBJECT_SIZE` lists the size of PL/SQL objects owned by the current user.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the object |
| `NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the object |
| `TYPE` | `VARCHAR2(12)` |  | Type of the object: `TYPE, TYPE BODY, TABLE, VIEW, SYNONYM, SEQUENCE, PROCEDURE, FUNCTION, PACKAGE, PACKAGE BODY, JAVA SOURCE, JAVA CLASS` or `JAVA RESOURCE` |
| `SOURCE_SIZE` | `NUMBER` |  | Size of the source in bytes. Must be in memory during compilation, or dynamic recompilation. |
| `PARSED_SIZE` | `NUMBER` |  | Size of the parsed form of the object, in bytes. Must be in memory when an object is being compiled that references this object. |
| `CODE_SIZE` | `NUMBER` |  | Code size, in bytes. Must be in memory when this object is executing. |
| `ERROR_SIZE` | `NUMBER` |  | Size of error messages, in bytes. In memory during the compilation of the object when there are compilation errors. |