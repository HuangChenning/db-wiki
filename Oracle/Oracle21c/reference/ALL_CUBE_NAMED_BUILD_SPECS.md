---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_CUBE_NAMED_BUILD_SPECS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.158 ALL\_CUBE\_NAMED\_BUILD\_SPECS

`ALL_CUBE_NAMED_BUILD_SPECS` describes the OLAP cube named build specifications in the database that are accessible by the user.

Related Views

- `DBA_CUBE_NAMED_BUILD_SPECS` describes the OLAP cube named build specifications in the database.
- `USER_CUBE_NAMED_BUILD_SPECS` describes the OLAP cube named build specifications in the database that are owned by the current user. This view does not display the `OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the OLAP named build specification |
| `CUBE_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the OLAP cube |
| `NAMED_BUILD_SPEC` | `CLOB` |  | Name of the OLAP cube named build specification |

See Also:

- " [DBA\_CUBE\_NAMED\_BUILD\_SPECS](DBA_CUBE_NAMED_BUILD_SPECS.md) "
- " [USER\_CUBE\_NAMED\_BUILD\_SPECS](USER_CUBE_NAMED_BUILD_SPECS.md) "