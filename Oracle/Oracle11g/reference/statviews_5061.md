---
title: DBA_TEMP_FILES
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_5061.htm
tags:
  - oracle
  - 11g
  - reference
---

`DBA_TEMP_FILES` describes all temporary files (tempfiles) in the database.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `FILE_NAME` | `VARCHAR2(513)` |  | Name of the database temp file |
| `FILE_ID` | `NUMBER` |  | File identifier number of the database temp file |
| `TABLESPACE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the tablespace to which the file belongs |
| `BYTES` | `NUMBER` |  | Size of the file (in bytes) |
| `BLOCKS` | `NUMBER` |  | Size of the file (in Oracle blocks) |
| `STATUS` | `CHAR(9)` |  | File status: - `OFFLINE` - `ONLINE` - `UNKNOWN` |
| `RELATIVE_FNO` | `NUMBER` |  | Tablespace-relative file number |
| `AUTOEXTENSIBLE` | `VARCHAR2(3)` |  | Indicates whether the file is autoextensible (`YES`) or not (`NO`) |
| `MAXBYTES` | `NUMBER` |  | maximum size of the file (in bytes) |
| `MAXBLOCKS` | `NUMBER` |  | Maximum size of the file (in Oracle blocks) |
| `INCREMENT_BY` | `NUMBER` |  | Default increment for autoextension (in Oracle blocks) |
| `USER_BYTES` | `NUMBER` |  | Size of the useful portion of the file (in bytes) |
| `USER_BLOCKS` | `NUMBER` |  | Size of the useful portion of the file (in Oracle blocks) |