---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_JAVA_LAYOUTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.249 ALL\_JAVA\_LAYOUTS

`ALL_JAVA_LAYOUTS` displays class layout information about the stored Java classes accessible to the current user.

Related Views

- `DBA_JAVA_LAYOUTS` displays class layout information about all stored Java classes in the database.
- `USER_JAVA_LAYOUTS` displays class layout information about the stored Java classes owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the Java class |
| `NAME` | `VARCHAR2(4000)` |  | Name of the Java class |
| `INTERFACES` | `NUMBER` |  | Number of interfaces that this Java class implements |
| `INNER_CLASSES` | `NUMBER` |  | Number of inner classes that this Java class contains |
| `FIELDS` | `NUMBER` |  | Number of locally declared fields that this Java class contains |
| `STATIC_FIELDS` | `NUMBER` |  | Number of locally declared static fields that this Java class contains |
| `METHODS` | `NUMBER` |  | Number of locally declared methods that this Java class contains |
| `STATIC_METHODS` | `NUMBER` |  | Number of locally declared static methods that this Java class contains |
| `NATIVE_METHODS` | `NUMBER` |  | Number of locally declared native methods that this Java class contains |

See Also:

- " [DBA\_JAVA\_LAYOUTS](DBA_JAVA_LAYOUTS.md) "
- " [USER\_JAVA\_LAYOUTS](USER_JAVA_LAYOUTS.md) "