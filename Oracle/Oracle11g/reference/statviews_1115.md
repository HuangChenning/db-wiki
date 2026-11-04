---
title: ALL_JAVA_ARGUMENTS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1115.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_JAVA_ARGUMENTS` displays argument information about the stored Java classes accessible to the current user.

Related Views

- `DBA_JAVA_ARGUMENTS` displays argument information about all stored Java classes in the database.
- `USER_JAVA_ARGUMENTS` displays argument information about the stored Java classes owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the Java class |
| `NAME` | `VARCHAR2(4000)` |  | Name of the Java class |
| `METHOD_INDEX` | `NUMBER` |  | Index of the hosting method of the argument |
| `METHOD_NAME` | `VARCHAR2(4000)` |  | Name of the hosting method of the argument |
| `ARGUMENT_POSITION` | `NUMBER` |  | Position of the argument, starting from 0 |
| `ARRAY_DEPTH` | `NUMBER` |  | Array depth of the type of the argument |
| `BASE_TYPE` | `VARCHAR2(7)` |  | Base type of the type of the argument: - `int` - `long` - `float` - `double` - `boolean` - `byte` - `char` - `short` - `class` |
| `ARGUMENT_CLASS` | `VARCHAR2(4000)` |  | Actual class name of the argument if the base type is `class` |

See Also:

- ["DBA\_JAVA\_ARGUMENTS"](statviews_4088.md)
- ["USER\_JAVA\_ARGUMENTS"](statviews_5329.md)