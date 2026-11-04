---
title: ALL_CUBE_BUILD_PROCESSES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1051.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_CUBE_BUILD_PROCESSES` describes the OLAP build processes and maintenance scripts accessible to the current user.

Related Views

- `DBA_CUBE_BUILD_PROCESSES` describes all OLAP build processes and maintenance scripts in the database.
- `USER_CUBE_BUILD_PROCESSES` describes the OLAP build processes and maintenance scripts owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the build process |
| `BUILD_PROCESS_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the build process |
| `BUILD_PROCESS` | `CLOB` |  | Syntax of the build process |
| `DESCRIPTION` | `NVARCHAR2(300)` |  | Description of the build process in the session language |

See Also:

- ["DBA\_CUBE\_BUILD\_PROCESSES"](statviews_3127.md)
- ["USER\_CUBE\_BUILD\_PROCESSES"](statviews_5263.md)