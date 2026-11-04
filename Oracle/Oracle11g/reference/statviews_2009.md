---
title: ALL_PLSQL_OBJECT_SETTINGS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_2009.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_PLSQL_OBJECT_SETTINGS` displays information about the compiler settings for the stored objects accessible to the current user.

Related Views

- `DBA_PLSQL_OBJECT_SETTINGS` displays information about the compiler settings for all stored objects in the database.
- `USER_PLSQL_OBJECT_SETTINGS` displays information about the compiler settings for the stored objects owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the object |
| `NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the object |
| `TYPE` | `VARCHAR2(12)` |  | Type of the object: - `PROCEDURE` - `FUNCTION` - `PACKAGE` - `PACKAGE BODY` - `TRIGGER` - `TYPE` - `TYPE BODY` |
| `PLSQL_OPTIMIZE_LEVEL` | `NUMBER` |  | Optimization level that was used to compile the object |
| `PLSQL_CODE_TYPE` | `VARCHAR2(4000)` |  | Compilation mode for the object |
| `PLSQL_DEBUG` | `VARCHAR2(4000)` |  | Indicates whether the object was compiled with debug information or not |
| `PLSQL_WARNINGS` | `VARCHAR2(4000)` |  | Compiler warning settings that were used to compile the object |
| `NLS_LENGTH_SEMANTICS` | `VARCHAR2(4000)` |  | NLS length semantics that were used to compile the object |
| `PLSQL_CCFLAGS` | `VARCHAR2(4000)` |  | Conditional compilation flag settings that were used to compile the object |
| `PLSCOPE_SETTINGS` | `VARCHAR2(4000)` |  | Settings for using PL/Scope |

See Also:

- ["DBA\_PLSQL\_OBJECT\_SETTINGS"](statviews_4181.md)
- ["USER\_PLSQL\_OBJECT\_SETTINGS"](statviews_5396.md)