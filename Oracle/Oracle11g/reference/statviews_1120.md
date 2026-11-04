---
title: ALL_JAVA_IMPLEMENTS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1120.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_JAVA_IMPLEMENTS` describes interfaces implemented by the stored Java classes accessible to the current user.

Related Views

- `DBA_JAVA_IMPLEMENTS` describes interfaces implemented by all stored Java classes in the database.
- `USER_JAVA_IMPLEMENTS` describes interfaces implemented by the stored Java classes owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the Java class |
| `NAME` | `VARCHAR2(4000)` |  | Name of the Java class |
| `INTERFACE_INDEX` | `NUMBER` |  | Index of the interfaces implemented by the Java class |
| `INTERFACE_NAME` | `VARCHAR2(4000)` |  | Name of the interface identified by the `INTERFACE_INDEX` column |

See Also:

- ["DBA\_JAVA\_IMPLEMENTS"](statviews_4093.md)
- ["USER\_JAVA\_IMPLEMENTS"](statviews_5334.md)