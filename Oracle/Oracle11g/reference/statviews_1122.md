---
title: ALL_JAVA_LAYOUTS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1122.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_JAVA_LAYOUTS` displays class layout information about the stored Java classes accessible to the current user.

Related Views

- `DBA_JAVA_LAYOUTS` displays class layout information about all stored Java classes in the database.
- `USER_JAVA_LAYOUTS` displays class layout information about the stored Java classes owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the Java class |
| `NAME` | `VARCHAR2(4000)` |  | Name of the Java class |
| `INTERFACES` | `NUMBER` |  | Number of interfaces that this Java class implements |
| `INNER_CLASSES` | `NUMBER` |  | Number of inner classes that this Java class contains |
| `FIELDS` | `NUMBER` |  | Number of locally declared fields that this Java class contains |
| `STATIC_FIELDS` | `NUMBER` |  | Number of locally declared static fields that this Java class contains |
| `METHODS` | `NUMBER` |  | Number of locally declared methods that this Java class contains |
| `STATIC_METHODS` | `NUMBER` |  | Number of locally declared static methods that this Java class contains |
| `NATIVE_METHODS` | `NUMBER` |  | Number of locally declared native methods that this Java class contains |

See Also:

- ["DBA\_JAVA\_LAYOUTS"](statviews_4095.md)
- ["USER\_JAVA\_LAYOUTS"](statviews_5336.md)