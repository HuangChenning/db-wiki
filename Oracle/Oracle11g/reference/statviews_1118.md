---
title: ALL_JAVA_DERIVATIONS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1118.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_JAVA_DERIVATIONS` displays mapping information about Java source objects and their derived Java class objects and Java resource objects for the Java classes accessible to the current user.

Related Views

- `DBA_JAVA_DERIVATIONS` displays mapping information about Java source objects and their derived Java class objects and Java resource objects for all Java classes in the database.
- `USER_JAVA_DERIVATIONS` displays mapping information about Java source objects and their derived Java class objects and Java resource objects for the Java classes owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the Java source object |
| `SOURCE_NAME` | `VARCHAR2(4000)` |  | Name of the Java source object |
| `CLASS_INDEX` | `NUMBER` |  | Index of the derived Java class object |
| `CLASS_NAME` | `VARCHAR2(4000)` |  | Name of the derived Java class object |

See Also:

- ["DBA\_JAVA\_DERIVATIONS"](statviews_4091.md)
- ["USER\_JAVA\_DERIVATIONS"](statviews_5332.md)