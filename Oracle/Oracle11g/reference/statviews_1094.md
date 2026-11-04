---
title: ALL_FILE_GROUP_FILES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1094.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_FILE_GROUP_FILES` shows the file set for each versioned file group accessible to the current user.

Related Views

- `DBA_FILE_GROUP_FILES` shows the file set for each versioned group in the database.
- `USER_FILE_GROUP_FILES` shows the file set for each versioned group owned by the current user. This view does not display the `FILE_GROUP_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `FILE_GROUP_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the file group |
| `FILE_GROUP_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the file group |
| `VERSION_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the version to which the file belongs |
| `VERSION` | `NUMBER` | `NOT NULL` | Internal version number of the file group version to which the file belongs |
| `FILE_NAME` | `VARCHAR2(512)` | `NOT NULL` | Name of the file |
| `FILE_DIRECTORY` | `VARCHAR2(30)` | `NOT NULL` | Directory object for the directory where the file is stored |
| `FILE_TYPE` | `VARCHAR2(32)` |  | User-specified file type |
| `FILE_SIZE` | `NUMBER` |  | Size of the file |
| `FILE_BLOCK_SIZE` | `NUMBER` |  | Block size for the file |
| `COMMENTS` | `VARCHAR2(4000)` |  | Comments about the file group |