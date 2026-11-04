---
title: ALL_JAVA_NCOMPS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1124.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_JAVA_NCOMPS` displays `ncomp` -related information about the Java classes accessible to the current user.

Related Views

- `DBA_JAVA_NCOMPS` displays `ncomp` -related information about all Java classes in the database.
- `USER_JAVA_NCOMPS` displays `ncomp` -related information about the Java classes owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the Java class object |
| `NAME` | `VARCHAR2(4000)` |  | Name of the Java class object |
| `SOURCE` | `VARCHAR2(4000)` |  | `ncomp` source shown in this row |
| `INITIALIZER` | `VARCHAR2(4000)` |  | `ncomp` initializer shown in this row |
| `LIBRARYFILE` | `VARCHAR2(4000)` |  | `ncomp` library file shown in this row |
| `LIBRARY` | `VARCHAR2(4000)` |  | `ncomp` library shown in this row |

See Also:

- ["DBA\_JAVA\_NCOMPS"](statviews_4097.md)
- ["USER\_JAVA\_NCOMPS"](statviews_5338.md)