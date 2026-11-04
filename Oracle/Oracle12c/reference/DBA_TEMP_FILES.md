---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_TEMP_FILES.html
tags:
  - oracle
  - 12c
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
| `STATUS` | `VARCHAR2(7)` |  | File status:  - `OFFLINE` - `ONLINE` - `UNKNOWN` |
| `RELATIVE_FNO` | `NUMBER` |  | Tablespace-relative file number |
| `AUTOEXTENSIBLE` | `VARCHAR2(3)` |  | Indicates whether the file is autoextensible (`YES`) or not (`NO`) |
| `MAXBYTES` | `NUMBER` |  | maximum size of the file (in bytes) |
| `MAXBLOCKS` | `NUMBER` |  | Maximum size of the file (in Oracle blocks) |
| `INCREMENT_BY` | `NUMBER` |  | Default increment for autoextension (in Oracle blocks) |
| `USER_BYTES` | `NUMBER` |  | Size of the useful portion of the file (in bytes) |
| `USER_BLOCKS` | `NUMBER` |  | Size of the useful portion of the file (in Oracle blocks) |
| `SHARED` | `VARCHAR2(12)` |  | Type of tablespace this file belongs to:  - `SHARED`: For shared tablespace - `LOCAL_FOR_RIM`: Local temporary tablespace for RIM (read-only) instances - `LOCAL_FOR_ALL`: Local temporary tablespace for all instance types  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |
| `INST_ID` | `NUMBER` |  | Instance ID of the instance to which the temp file belongs. This column has a NULL value for temp files that belong to shared tablespaces.  This column is available starting with Oracle Database 12c Release 2 (12.2.0.1). |