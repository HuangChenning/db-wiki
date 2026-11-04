---
title: ALL_JAVA_CLASSES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1116.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_JAVA_CLASSES` displays class level information about the stored Java classes accessible to the current user.

Related Views

- `DBA_JAVA_CLASSES` displays class level information about all stored Java classes in the database.
- `USER_JAVA_CLASSES` displays class level information about the stored Java classes owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the Java class |
| `NAME` | `VARCHAR2(4000)` |  | Name of the Java class |
| `MAJOR` | `NUMBER` |  | Major version number of the Java class, as defined in the JVM specification |
| `MINOR` | `NUMBER` |  | Minor version number of the Java class, as defined in the JVM specification |
| `KIND` | `VARCHAR2(9)` |  | Indicates whether the stored object is a Java class (`CLASS`) or a Java interface (`INTERFACE`) |
| `ACCESSIBILITY` | `VARCHAR2(6)` |  | Accessibility of the Java class |
| `IS_INNER` | `VARCHAR2(3)` |  | Indicates whether this Java class is an inner class (`YES`) or not (`NO`) |
| `IS_ABSTRACT` | `VARCHAR2(3)` |  | Indicates whether this Java class is an abstract class (`YES`) or not (`NO`) |
| `IS_FINAL` | `VARCHAR2(3)` |  | Indicates whether this Java class is a final class (`YES`) or not (`NO`) |
| `IS_DEBUG` | `VARCHAR2(3)` |  | Indicates whether this Java class contains debug information (`YES`) or not (`NO`) |
| `SOURCE` | `VARCHAR2(4000)` |  | Source designation of the Java class |
| `SUPER` | `VARCHAR2(4000)` |  | Super class of this Java class |
| `OUTER` | `VARCHAR2(4000)` |  | Outer class of this Java class if this Java class is an inner class |

See Also:

- ["DBA\_JAVA\_CLASSES"](statviews_4089.md)
- ["USER\_JAVA\_CLASSES"](statviews_5330.md)