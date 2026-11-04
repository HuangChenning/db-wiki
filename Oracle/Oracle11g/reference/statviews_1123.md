---
title: ALL_JAVA_METHODS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1123.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_JAVA_METHODS` displays method information about the stored Java classes accessible to the current user.

Related Views

- `DBA_JAVA_METHODS` displays method information about all stored Java classes in the database.
- `USER_JAVA_METHODS` displays method information about the stored Java classes owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the Java class |
| `NAME` | `VARCHAR2(4000)` |  | Name of the Java class |
| `METHOD_INDEX` | `NUMBER` |  | Index of the method |
| `METHOD_NAME` | `VARCHAR2(4000)` |  | Name of the method identified by the `METHOD_INDEX` column |
| `ACCESSIBILITY` | `VARCHAR2(9)` |  | Accessibility of the method: - `PUBLIC` - `PRIVATE` - `PROTECTED` |
| `IS_STATIC` | `VARCHAR2(3)` |  | Indicates whether the method is a static method (`YES`) or not (`NO`) |
| `IS_FINAL` | `VARCHAR2(3)` |  | Indicates whether the method is a final method (`YES`) or not (`NO`) |
| `IS_SYNCHRONIZED` | `VARCHAR2(3)` |  | Indicates whether the method is a synchronized method (`YES`) or not (`NO`) |
| `IS_NATIVE` | `VARCHAR2(3)` |  | Indicates whether the method is a native method (`YES`) or not (`NO`) |
| `IS_ABSTRACT` | `VARCHAR2(3)` |  | Indicates whether the method is an abstract method (`YES`) or not (`NO`) |
| `IS_STRICT` | `VARCHAR2(3)` |  | Indicates whether the method is a strict method (`YES`) or not (`NO`) |
| `ARGUMENTS` | `NUMBER` |  | Number of arguments of the method |
| `THROWS` | `NUMBER` |  | Number of exceptions thrown by the method |
| `ARRAY_DEPTH` | `NUMBER` |  | Array depth of the return type of the method |
| `BASE_TYPE` | `VARCHAR2(7)` |  | Base type of the return type of the method: - `int` - `long` - `float` - `double` - `boolean` - `byte` - `char` - `short` - `class` - `void` |
| `RETURN_CLASS` | `VARCHAR2(4000)` |  | Actual class name of the return value if the base type is `class` |
| `IS_COMPILED` | `VARCHAR2(3)` |  | Indicates whether the Java method has been natively compiled by the JIT compiler (`YES`) or not (`NO`) |

See Also:

- ["DBA\_JAVA\_METHODS"](statviews_4096.md)
- ["USER\_JAVA\_METHODS"](statviews_5337.md)