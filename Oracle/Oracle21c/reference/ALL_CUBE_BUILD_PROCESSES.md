---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_CUBE_BUILD_PROCESSES.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.145 ALL\_CUBE\_BUILD\_PROCESSES

`ALL_CUBE_BUILD_PROCESSES` describes the OLAP build processes and maintenance scripts accessible to the current user.

Related Views

- `DBA_CUBE_BUILD_PROCESSES` describes all OLAP build processes and maintenance scripts in the database.
- `USER_CUBE_BUILD_PROCESSES` describes the OLAP build processes and maintenance scripts owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the build process |
| `BUILD_PROCESS_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the build process |
| `BUILD_PROCESS_ID` | `NUMBER` | `NOT NULL` | ID of the build process |
| `BUILD_PROCESS` | `CLOB` |  | Syntax of the build process |
| `DESCRIPTION` | `NVARCHAR2(300)` |  | Description of the build process in the session language |

See Also:

- " [DBA\_CUBE\_BUILD\_PROCESSES](DBA_CUBE_BUILD_PROCESSES.md) "
- " [USER\_CUBE\_BUILD\_PROCESSES](USER_CUBE_BUILD_PROCESSES.md) "