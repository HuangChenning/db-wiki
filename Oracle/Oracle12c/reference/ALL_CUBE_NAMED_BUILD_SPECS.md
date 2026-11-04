---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_CUBE_NAMED_BUILD_SPECS.html
tags:
  - oracle
  - 12c
  - reference
---

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