---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-UNUSABLE_BACKUPFILE_DETAILS.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.127 V$UNUSABLE\_BACKUPFILE\_DETAILS

`V$UNUSABLE_BACKUPFILE_DETAILS` displays information about all backup files (backup pieces, proxy copies, or copies) that are marked unavailable and expired. You can select one of the rows and use `BTYPE_KEY` or `FILETYPE_KEY` to change the status of a backup file set or a specific file to available.

| Column | Datatype | Description |
| --- | --- | --- |
| `SESSION_KEY` | `NUMBER` | Session identifier |
| `SESSION_RECID` | `NUMBER` | Session record ID |
| `SESSION_STAMP` | `NUMBER` | Session stamp |
| `RMAN_STATUS_RECID` | `NUMBER` | Record ID of the corresponding row in the control file |
| `RMAN_STATUS_STAMP` | `NUMBER` | Timestamp of the row in the controlfile |
| `BTYPE` | `CHAR(9)` | Backup type container. Possible values are: `BACKUPSET`, `IMAGECOPY`, `PROXYCOPY`. |
| `BTYPE_KEY` | `NUMBER` | Unique identifier for the backup type, either `BS_KEY` or `COPY_KEY`. |
| `ID1` | `NUMBER` | If `BACKUPSET`, it contains `SET_STAMP`.  If `IMAGECOPY` or `PROXYCOPY`, it is `RECID` from the control file. |
| `ID2` | `NUMBER` | If `BACKUPSET`, it contains `SET_COUNT`.  If `IMAGECOPY` or `PROXYCOPY`, it is `STAMP`. |
| `FILETYPE` | `VARCHAR2(15)` | Type of file. Possible values are: `BACKUPPIECE`, `COPY`, `PROXYCOPY`. |
| `FILETYPE_KEY` | `NUMBER` | Backup piece key if the file is a backup piece; otherwise `COPY_KEY`. |
| `STATUS` | `VARCHAR2(1)` | Status of the backup file, either `U` (unavailable) or `X` (expired) |
| `FILESIZE` | `NUMBER` | Size of the file |
| `DEVICE_TYPE` | `VARCHAR2(17)` | Type of device on which the file resides |
| `FILENAME` | `VARCHAR2(513)` | Name of the file |
| `MEDIA` | `VARCHAR2(65)` | Name of the media on which the copy resides. This value is informational only. It is not needed for restore. |
| `MEDIA_POOL` | `NUMBER` | Media pool in which the copy resides. This is the same value that was entered in the `POOL` operand of the Recovery Manager `BACKUP` command. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |