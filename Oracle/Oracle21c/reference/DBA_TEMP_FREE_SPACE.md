---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_TEMP_FREE_SPACE.html
tags:
  - oracle
  - 21c
  - reference
---

## 7.52 DBA\_TEMP\_FREE\_SPACE

`DBA_TEMP_FREE_SPACE` displays temporary space usage information at tablespace level.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `TABLESPACE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the tablespace |
| `TABLESPACE_SIZE` | `NUMBER` |  | Total size of the tablespace, in bytes |
| `ALLOCATED_SPACE` | `NUMBER` |  | Total allocated space, in bytes, including space that is currently allocated and used and space that is currently allocated and available for reuse |
| `FREE_SPACE` | `NUMBER` |  | Total free space available, in bytes, including space that is currently allocated and available for reuse and space that is currently unallocated |
| `SHARED` | `VARCHAR2(12)` |  | Type of tablespace this file belongs to:  - `SHARED`: For shared tablespace - `LOCAL_FOR_RIM`: Local temporary tablespace for RIM (read-only) instances - `LOCAL_FOR_ALL`: Local temporary tablespace for all instance types |
| `INST_ID` | `NUMBER` |  | Instance ID of the instance to which the tempfile belongs |