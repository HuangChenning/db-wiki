---
title: ALL_JAVA_FIELDS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1119.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_JAVA_FIELDS` displays field information about the stored Java classes accessible to the current user.

Related Views

- `DBA_JAVA_FIELDS` displays field information about all stored Java classes in the database.
- `USER_JAVA_FIELDS` displays field information about the stored Java classes owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the Java class |
| `NAME` | `VARCHAR2(4000)` |  | Name of the Java class |
| `FIELD_INDEX` | `NUMBER` |  | Index of the field |
| `FIELD_NAME` | `VARCHAR2(4000)` |  | Name of the field identified by the `FIELD_INDEX` column |
| `ACCESSIBILITY` | `VARCHAR2(9)` |  | Accessibility of the field: - `PUBLIC` - `PRIVATE` - `PROTECTED` |
| `IS_STATIC` | `VARCHAR2(3)` |  | Indicates whether the field is a static field (`YES`) or not (`NO`) |
| `IS_FINAL` | `VARCHAR2(3)` |  | Indicates whether the field is a final field (`YES`) or not (`NO`) |
| `IS_VOLATILE` | `VARCHAR2(3)` |  | Indicates whether the field is volatile (`YES`) or not (`NO`) |
| `IS_TRANSIENT` | `VARCHAR2(3)` |  | Indicates whether the field is transient (`YES`) or not (`NO`) |
| `ARRAY_DEPTH` | `NUMBER` |  | Array depth of the type of the field |
| `BASE_TYPE` | `VARCHAR2(7)` |  | Base type of the type of the field: - `int` - `long` - `float` - `double` - `boolean` - `byte` - `char` - `short` - `class` |
| `FIELD_CLASS` | `VARCHAR2(4000)` |  | Actual class name of the base object if the base type is `class` |

See Also:

- ["DBA\_JAVA\_FIELDS"](statviews_4092.md)
- ["USER\_JAVA\_FIELDS"](statviews_5333.md)