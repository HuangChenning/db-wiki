---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-BACKUP_PIECE.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.97 V$BACKUP\_PIECE

`V$BACKUP_PIECE` displays information about backup pieces from the control file. Each backup set consists of one or more backup pieces.

| Column | Datatype | Description |
| --- | --- | --- |
| `RECID` | `NUMBER` | Backup piece record ID |
| `STAMP` | `NUMBER` | Backup piece record stamp |
| `SET_STAMP` | `NUMBER` | Backup set stamp |
| `SET_COUNT` | `NUMBER` | Backup set count |
| `PIECE#` | `NUMBER` | Backup piece number (1-N) |
| `COPY#` | `NUMBER` | Indicates the copy number for backup pieces created with duplex enabled. 1 if the backup piece is not duplexed. |
| `DEVICE_TYPE` | `VARCHAR2(17)` | Type of the device on which the backup piece resides. Set to DISK for backup sets on disk.  See Also: `V$BACKUP_DEVICE` |
| `HANDLE` | `VARCHAR2(513)` | Backup piece handle identifies the backup piece on restore |