---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-BACKUP_PIECE_DETAILS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.98 V$BACKUP\_PIECE\_DETAILS

`V$BACKUP_PIECE_DETAILS` displays information about all available backup pieces.

| Column | Datatype | Description |
| --- | --- | --- |
| `SESSION_KEY` | `NUMBER` | Session identifier |
| `SESSION_RECID` | `NUMBER` | Session recid |
| `SESSION_STAMP` | `NUMBER` | Session stamp |
| `BS_KEY` | `NUMBER` | Backup set identifier |
| `BP_KEY` | `NUMBER` | Backup piece key |
| `RECID` | `NUMBER` | Backup piece record ID |
| `STAMP` | `NUMBER` | Backup piece record stamp |
| `SET_STAMP` | `NUMBER` | Backup set stamp |
| `SET_COUNT` | `NUMBER` | Backup set count |
| `PIECE#` | `NUMBER` | Backup piece number (1-N) |
| `COPY#` | `NUMBER` | Indicates the copy number for backup pieces created with duplex enabled. The value is 1 if the backup piece is not duplexed. |
| `DEVICE_TYPE` | `VARCHAR2(17)` | Type of device on which the backup piece resides. Set to DISK for backup sets on disk. |
| `HANDLE` | `VARCHAR2(513)` | Backup piece handle identifies the backup piece on restore |