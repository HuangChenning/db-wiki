---
title: ALL_JAVA_COMPILER_OPTIONS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1117.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_JAVA_COMPILER_OPTIONS` displays information about the native compiler options accessible to the current user.

Related Views

- `DBA_JAVA_COMPILER_OPTIONS` displays information about all native compiler options in the database.
- `USER_JAVA_COMPILER_OPTIONS` displays information about the native compiler options owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the native compiler option |
| `OPTION_NAME` | `VARCHAR2(64)` |  | Name of the native compiler option |
| `VALUE` | `VARCHAR2(4000)` |  | Value of the native compiler option |

See Also:

- ["DBA\_JAVA\_COMPILER\_OPTIONS"](statviews_4090.md)
- ["USER\_JAVA\_COMPILER\_OPTIONS"](statviews_5331.md)