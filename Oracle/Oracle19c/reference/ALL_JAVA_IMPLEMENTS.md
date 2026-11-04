---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ALL_JAVA_IMPLEMENTS.html
tags:
  - oracle
  - 19c
  - reference
---

## 2.239 ALL\_JAVA\_IMPLEMENTS

`ALL_JAVA_IMPLEMENTS` describes interfaces implemented by the stored Java classes accessible to the current user.

Related Views

- `DBA_JAVA_IMPLEMENTS` describes interfaces implemented by all stored Java classes in the database.
- `USER_JAVA_IMPLEMENTS` describes interfaces implemented by the stored Java classes owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the Java class |
| `NAME` | `VARCHAR2(4000)` |  | Name of the Java class |
| `INTERFACE_INDEX` | `NUMBER` |  | Index of the interfaces implemented by the Java class |
| `INTERFACE_NAME` | `VARCHAR2(4000)` |  | Name of the interface identified by the `INTERFACE_INDEX` column |

See Also:

- " [DBA\_JAVA\_IMPLEMENTS](DBA_JAVA_IMPLEMENTS.md) "
- " [USER\_JAVA\_IMPLEMENTS](USER_JAVA_IMPLEMENTS.md) "