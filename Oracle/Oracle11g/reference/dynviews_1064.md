---
title: "V$BACKUP_SPFILE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1064.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$BACKUP_SPFILE` displays information about server parameter files in backup sets from the control file.

| Column | Datatype | Description |
| --- | --- | --- |
| `RECID` | `NUMBER` | Backup SPFILE record ID |
| `STAMP` | `NUMBER` | Backup SPFILE record stamp |
| `SET_STAMP` | `NUMBER` | Backup set stamp (of the set which contains this SPFILE backup) |
| `SET_COUNT` | `NUMBER` | Backup set count (of the set which contains this SPFILE backup) |
| `MODIFICATION_TIME` | `DATE` | Time when the SPFILE was last modified (this also includes creation time) |
| `BYTES` | `NUMBER` | Size of the SPFILE (in bytes) |
| `COMPLETION_TIME` | `DATE` | Time when the backup of the SPFILE completed |
| `DB_UNIQUE_NAME` | `VARCHAR2(30)` | Unique database name |