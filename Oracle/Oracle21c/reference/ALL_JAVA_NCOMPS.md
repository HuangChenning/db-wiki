---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_JAVA_NCOMPS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.251 ALL\_JAVA\_NCOMPS

`ALL_JAVA_NCOMPS` displays `ncomp` -related information about the Java classes accessible to the current user.

Related Views

- `DBA_JAVA_NCOMPS` displays `ncomp` -related information about all Java classes in the database.
- `USER_JAVA_NCOMPS` displays `ncomp` -related information about the Java classes owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the Java class object |
| `NAME` | `VARCHAR2(4000)` |  | Name of the Java class object |
| `SOURCE` | `VARCHAR2(4000)` |  | `ncomp` source shown in this row |
| `INITIALIZER` | `VARCHAR2(4000)` |  | `ncomp` initializer shown in this row |
| `LIBRARYFILE` | `VARCHAR2(4000)` |  | `ncomp` library file shown in this row |
| `LIBRARY` | `VARCHAR2(4000)` |  | `ncomp` library shown in this row |

See Also:

- " [DBA\_JAVA\_NCOMPS](DBA_JAVA_NCOMPS.md) "
- " [USER\_JAVA\_NCOMPS](USER_JAVA_NCOMPS.md) "