---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ALL_FILE_GROUP_VERSIONS.html
tags:
  - oracle
  - 12c
  - reference
---

`ALL_FILE_GROUP_VERSIONS` shows top-level version information for the file groups accessible to the current user.

Related Views

- `DBA_FILE_GROUP_VERSIONS` shows top-level version information for all file groups in the database.
- `USER_FILE_GROUP_VERSIONS` shows top-level version information for all file groups owned by the current user. This view does not display the `FILE_GROUP_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `FILE_GROUP_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the file group |
| `FILE_GROUP_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the file group |
| `VERSION_NAME` | `VARCHAR2(128)` | `NOT NULL` | User-specified name for the version |
| `VERSION` | `NUMBER` | `NOT NULL` | Internal version number |
| `CREATOR` | `VARCHAR2(128)` | `NOT NULL` | User who created the version |
| `CREATED` | `TIMESTAMP(6) WITH TIME ZONE` | `NOT NULL` | Time at which the version was created |