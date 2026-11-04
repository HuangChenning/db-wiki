---
title: ALL_JAVA_INNERS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1121.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_JAVA_INNERS` displays information about inner classes referred to by the stored Java classes accessible to the current user.

Related Views

- `DBA_JAVA_INNERS` displays information about inner classes referred to by all stored Java classes in the database.
- `USER_JAVA_INNERS` displays information about inner classes referred to by the stored Java classes owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the Java class |
| `NAME` | `VARCHAR2(4000)` |  | Name of the Java class |
| `INNER_INDEX` | `NUMBER` |  | Index of the referred inner class |
| `SIMPLE_NAME` | `VARCHAR2(4000)` |  | Simple name of the referred inner class |
| `FULL_NAME` | `VARCHAR2(4000)` |  | Full name of the referred inner class |
| `ACCESSIBILITY` | `VARCHAR2(9)` |  | Accessibility of the referred inner class: - `PUBLIC` - `PRIVATE` - `PROTECTED` |
| `IS_STATIC` | `VARCHAR2(3)` |  | Indicates whether the referred inner class is declared static in the source file (`YES`) or not (`NO`) |
| `IS_FINAL` | `VARCHAR2(3)` |  | Indicates whether the referred inner class is declared final in the source file (`YES`) or not (`NO`) |
| `IS_ABSTRACT` | `VARCHAR2(3)` |  | Indicates whether the referred inner class is declared abstract in the source file (`YES`) or not (`NO`) |
| `IS_INTERFACE` | `VARCHAR2(3)` |  | Indicates whether the referred inner class is declared interface in the source file (`YES`) or not (`NO`) |

See Also:

- ["DBA\_JAVA\_INNERS"](statviews_4094.md)
- ["USER\_JAVA\_INNERS"](statviews_5335.md)