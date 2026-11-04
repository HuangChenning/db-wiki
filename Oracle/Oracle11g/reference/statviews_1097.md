---
title: ALL_FILE_GROUP_VERSIONS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1097.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_FILE_GROUP_VERSIONS` shows top-level version information for the file groups accessible to the current user.

Related Views

- `DBA_FILE_GROUP_VERSIONS` shows top-level version information for all file groups in the database.
- `USER_FILE_GROUP_VERSIONS` shows top-level version information for all file groups owned by the current user. This view does not display the `FILE_GROUP_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `FILE_GROUP_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the file group |
| `FILE_GROUP_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the file group |
| `VERSION_NAME` | `VARCHAR2(30)` | `NOT NULL` | User-specified name for the version |
| `VERSION` | `NUMBER` | `NOT NULL` | Internal version number |
| `CREATOR` | `VARCHAR2(30)` | `NOT NULL` | User who created the version |
| `CREATED` | `TIMESTAMP(6) WITH TIME ZONE` | `NOT NULL` | Time at which the version was created |
| `COMMENTS` | `VARCHAR2(4000)` |  | Comments about the file group |
| `DEFAULT_DIRECTORY` | `VARCHAR2(30)` |  | Default directory object for this version, if specified |