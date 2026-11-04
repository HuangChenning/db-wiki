---
title: "V$BACKUP"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1044.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$BACKUP` displays the backup status of all online datafiles.

| Column | Datatype | Description |
| --- | --- | --- |
| `FILE#` | `NUMBER` | File identifier |
| `STATUS` | `VARCHAR2(18)` | File status: `NOT ACTIVE`, `ACTIVE` (backup in progress), `OFFLINE NORMAL`, or description of an error.  `NOT ACTIVE` indicates that the file is not currently in backup mode (that is, an `ALTER TABLESPACE ... BEGIN BACKUP` or `ALTER DATABASE BEGIN BACKUP` statement has not been issued), whereas `ACTIVE` indicates that the file is currently in backup mode. |
| `CHANGE#` | `NUMBER` | System change number when backup started |
| `TIME` | `DATE` | Time the backup started |