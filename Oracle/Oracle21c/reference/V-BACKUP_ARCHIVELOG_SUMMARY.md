---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-BACKUP_ARCHIVELOG_SUMMARY.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.84 V$BACKUP\_ARCHIVELOG\_SUMMARY

`V$BACKUP_ARCHIVELOG_SUMMARY` provides archive log summary information based on archive logs in the backup set or on proxy copies.

| Column | Datatype | Description |
| --- | --- | --- |
| `NUM_FILES_BACKED` | `NUMBER` | Number of files backed up |
| `NUM_DISTINCT_FILES_BACKED` | `NUMBER` | Number of distinct archive log files backed up |
| `MIN_FIRST_CHANGE#` | `NUMBER` | Lowest SCN range value |
| `MAX_NEXT_CHANGE#` | `NUMBER` | Highest SCN range value |
| `MIN_FIRST_TIME` | `DATE` | Lowest SCN range time |
| `MAX_NEXT_TIME` | `DATE` | Highest SCN range time |
| `INPUT_BYTES` | `NUMBER` | Total input bytes read |
| `OUTPUT_BYTES` | `NUMBER` | Output size of backups |
| `COMPRESSION_RATIO` | `NUMBER` | The ratio between the total blocks in the archive log and the blocks that RMAN backed up. This is not the ratio from the `AS COMPRESSED BACKUPSET` clause of the `BACKUP` command. |
| `INPUT_BYTES_DISPLAY` | `VARCHAR2(4000)` | Displayable format for input bytes |
| `OUTPUT_BYTES_DISPLAY` | `VARCHAR2(4000)` | Displayable format for output bytes |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |