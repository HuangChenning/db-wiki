---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_FILE_GROUPS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.196 ALL\_FILE\_GROUPS

`ALL_FILE_GROUPS` shows top-level metadata about the file groups accessible to the current user.

Related Views

- `DBA_FILE_GROUPS` shows top-level metadata about all file groups in the database.
- `USER_FILE_GROUPS` shows top-level metadata about file groups owned by the current user. This view does not display the `FILE_GROUP_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `FILE_GROUP_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the file group |
| `FILE_GROUP_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the file group |
| `KEEP_FILES` | `VARCHAR2(1)` | `NOT NULL` | A value of Y or N to indicate whether or not files should be deleted when a version is purged |
| `MIN_VERSIONS` | `NUMBER` | `NOT NULL` | Autopurge should not drop a version if this condition will become violated |
| `MAX_VERSIONS` | `NUMBER` | `NOT NULL` | Autopurge will drop the oldest version when this condition is violated |
| `RETENTION_DAYS` | `NUMBER` | `NOT NULL` | Autopurge will drop versions older than this if doing so does not violate `MIN_VERSIONS` |
| `CREATED` | `TIMESTAMP(6) WITH TIME ZONE` | `NOT NULL` | Time at which the file group was created |