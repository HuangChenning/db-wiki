---
title: DBA_DATA_FILES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_3143.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_DATA_FILES` describes database files.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `FILE_NAME` | `VARCHAR2(513)` |  | Name of the database file |
| `FILE_ID` | `NUMBER` | `NOT NULL` | File identifier number of the database file |
| `TABLESPACE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the tablespace to which the file belongs |
| `BYTES` | `NUMBER` |  | Size of the file in bytes |
| `BLOCKS` | `NUMBER` | `NOT NULL` | Size of the file in Oracle blocks |
| `STATUS` | `VARCHAR2(9)` |  | File status: `AVAILABLE` or `INVALID` (`INVALID` means that the file number is not in use, for example, a file in a tablespace that was dropped) |
| `RELATIVE_FNO` | `NUMBER` |  | Relative file number |
| `AUTOEXTENSIBLE` | `VARCHAR2(3)` |  | Autoextensible indicator |
| `MAXBYTES` | `NUMBER` |  | Maximum file size in bytes |
| `MAXBLOCKS` | `NUMBER` |  | Maximum file size in blocks |
| `INCREMENT_BY` | `NUMBER` |  | Number of Oracle blocks used as autoextension increment |
| `USER_BYTES` | `NUMBER` |  | The size of the file available for user data. The actual size of the file minus the `USER_BYTES` value is used to store file related metadata. |
| `USER_BLOCKS` | `NUMBER` |  | Number of blocks which can be used by the data |
| `ONLINE_STATUS` | `VARCHAR2(7)` |  | Online status of the file: |