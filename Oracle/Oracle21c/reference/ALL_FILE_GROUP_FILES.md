---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_FILE_GROUP_FILES.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.192 ALL\_FILE\_GROUP\_FILES

`ALL_FILE_GROUP_FILES` shows the file set for each versioned file group accessible to the current user.

Related Views

- `DBA_FILE_GROUP_FILES` shows the file set for each versioned group in the database.
- `USER_FILE_GROUP_FILES` shows the file set for each versioned group owned by the current user. This view does not display the `FILE_GROUP_OWNER` column.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `FILE_GROUP_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the file group |
| `FILE_GROUP_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the file group |
| `VERSION_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the version to which the file belongs |
| `VERSION` | `NUMBER` | `NOT NULL` | Internal version number of the file group version to which the file belongs |
| `FILE_NAME` | `VARCHAR2(512)` | `NOT NULL` | Name of the file |
| `FILE_DIRECTORY` | `VARCHAR2(128)` | `NOT NULL` | Directory object for the directory where the file is stored |
| `FILE_TYPE` | `VARCHAR2(32)` |  | User-specified file type |
| `FILE_SIZE` | `NUMBER` |  | Size of the file |
| `FILE_BLOCK_SIZE` | `NUMBER` |  | Block size for the file |