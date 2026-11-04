---
title: ALL_FILE_GROUPS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1098.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_FILE_GROUPS` shows top-level metadata about the file groups accessible to the current user.

Related Views

- `DBA_FILE_GROUPS` shows top-level metadata about all file groups in the database.
- `USER_FILE_GROUPS` shows top-level metadata about file groups owned by the current user. This view does not display the `FILE_GROUP_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `FILE_GROUP_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the file group |
| `FILE_GROUP_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the file group |
| `KEEP_FILES` | `VARCHAR2(1)` | `NOT NULL` | A value of Y or N to indicate whether or not files should be deleted when a version is purged |
| `MIN_VERSIONS` | `NUMBER` | `NOT NULL` | Autopurge should not drop a version if this condition will become violated |
| `MAX_VERSIONS` | `NUMBER` | `NOT NULL` | Autopurge will drop the oldest version when this condition is violated |
| `RETENTION_DAYS` | `NUMBER` | `NOT NULL` | Autopurge will drop versions older than this if doing so does not violate `MIN_VERSIONS` |
| `CREATED` | `TIMESTAMP(6) WITH TIME ZONE` | `NOT NULL` | Time at which the file group was created |
| `COMMENTS` | `VARCHAR2(4000)` |  | Comments about the file group |
| `DEFAULT_DIRECTORY` | `VARCHAR2(30)` |  | Name of the default directory object |