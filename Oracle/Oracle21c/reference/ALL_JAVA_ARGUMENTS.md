---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_JAVA_ARGUMENTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.242 ALL\_JAVA\_ARGUMENTS

`ALL_JAVA_ARGUMENTS` displays argument information about the stored Java classes accessible to the current user.

Related Views

- `DBA_JAVA_ARGUMENTS` displays argument information about all stored Java classes in the database.
- `USER_JAVA_ARGUMENTS` displays argument information about the stored Java classes owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the Java class |
| `NAME` | `VARCHAR2(4000)` |  | Name of the Java class |
| `METHOD_INDEX` | `NUMBER` |  | Index of the hosting method of the argument |
| `METHOD_NAME` | `VARCHAR2(4000)` |  | Name of the hosting method of the argument |
| `ARGUMENT_POSITION` | `NUMBER` |  | Position of the argument, starting from 0 |
| `ARRAY_DEPTH` | `NUMBER` |  | Array depth of the type of the argument |
| `BASE_TYPE` | `VARCHAR2(7)` |  | Base type of the type of the argument:  - `int` - `long` - `float` - `double` - `boolean` - `byte` - `char` - `short` - `class` |
| `ARGUMENT_CLASS` | `VARCHAR2(4000)` |  | Actual class name of the argument if the base type is `class` |

See Also:

- " [DBA\_JAVA\_ARGUMENTS](DBA_JAVA_ARGUMENTS.md) "
- " [USER\_JAVA\_ARGUMENTS](USER_JAVA_ARGUMENTS.md) "