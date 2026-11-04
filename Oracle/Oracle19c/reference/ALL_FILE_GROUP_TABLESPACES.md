---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/ALL_FILE_GROUP_TABLESPACES.html
tags:
  - oracle
  - 19c
  - reference
---

## 2.186 ALL\_FILE\_GROUP\_TABLESPACES

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