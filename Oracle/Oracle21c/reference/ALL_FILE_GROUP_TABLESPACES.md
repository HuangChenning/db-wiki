---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_FILE_GROUP_TABLESPACES.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.194 ALL\_FILE\_GROUP\_TABLESPACES

`ALL_FILE_GROUP_TABLESPACES` shows information about the transportable tablespaces present (partially or completely) in the file groups accessible to the current user (when the file groups contain dump files).

Related Views

- `DBA_FILE_GROUP_TABLESPACES` shows information about the transportable tablespaces present (partially or completely) in all file groups in the database (when the file groups contain dump files).
- `USER_FILE_GROUP_TABLESPACES` shows information about the transportable tablespaces present (partially or completely) in the file groups owned by the current user (when the file groups contain dump files). This view does not display the `FILE_GROUP_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `FILE_GROUP_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the file group |
| `FILE_GROUP_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the file group |
| `VERSION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Version of the file group that contains the tablespace |
| `VERSION` | `NUMBER` | `NOT NULL` | Internal version number |
| `TABLESPACE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the tablespace |

See Also:

- " [DBA\_FILE\_GROUP\_TABLESPACES](DBA_FILE_GROUP_TABLESPACES.md) "
- " [USER\_FILE\_GROUP\_TABLESPACES](USER_FILE_GROUP_TABLESPACES.md) "