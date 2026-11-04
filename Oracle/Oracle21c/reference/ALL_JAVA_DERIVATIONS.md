---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_JAVA_DERIVATIONS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.245 ALL\_JAVA\_DERIVATIONS

`ALL_JAVA_DERIVATIONS` displays mapping information about Java source objects and their derived Java class objects and Java resource objects for the Java classes accessible to the current user.

Related Views

- `DBA_JAVA_DERIVATIONS` displays mapping information about Java source objects and their derived Java class objects and Java resource objects for all Java classes in the database.
- `USER_JAVA_DERIVATIONS` displays mapping information about Java source objects and their derived Java class objects and Java resource objects for the Java classes owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the Java source object |
| `SOURCE_NAME` | `VARCHAR2(4000)` |  | Name of the Java source object |
| `CLASS_INDEX` | `NUMBER` |  | Index of the derived Java class object |
| `CLASS_NAME` | `VARCHAR2(4000)` |  | Name of the derived Java class object |

See Also:

- " [DBA\_JAVA\_DERIVATIONS](DBA_JAVA_DERIVATIONS.md) "
- " [USER\_JAVA\_DERIVATIONS](USER_JAVA_DERIVATIONS.md) "