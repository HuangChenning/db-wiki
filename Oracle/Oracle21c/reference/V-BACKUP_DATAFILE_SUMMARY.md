---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-BACKUP_DATAFILE_SUMMARY.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.93 V$BACKUP\_DATAFILE\_SUMMARY

`V$BACKUP_DATAFILE_SUMMARY` provides summary information for a specific criteria set, based on a backup job, a time range applicable to jobs, or a specific data file).

| Column | Datatype | Description |
| --- | --- | --- |
| `NUM_FILES_BACKED` | `NUMBER` | Number of files backed up for specified criteria |
| `NUM_DISTINCT_FILES_BACKED` | `NUMBER` | Number of distinct files backed up |
| `NUM_DISTINCT_TS_BACKED` | `NUMBER` | Number of distinct tablespaces backed up |
| `MIN_CHECKPOINT_CHANGE#` | `NUMBER` | Minimum checkpoint change number of the data file for specified criteria |
| `MAX_CHECKPOINT_CHANGE#` | `NUMBER` | Maximum checkpoint change number of the data file for specified criteria |
| `MIN_CHECKPOINT_TIME` | `DATE` | Minimum checkpoint time of the data file for specified criteria |
| `MAX_CHECKPOINT_TIME` | `DATE` | Maximum checkpoint time of the data file for specified criteria |
| `INPUT_BYTES` | `NUMBER` | Total input bytes of files read |
| `OUTPUT_BYTES` | `NUMBER` | Total output bytes written |
| `COMPRESSION_RATIO` | `NUMBER` | The ratio between the total blocks in the datafile and the blocks that RMAN backed up. This is not the the ratio from the `AS COMPRESSED BACKUPSET` clause of the `BACKUP` command. |
| `INPUT_BYTES_DISPLAY` | `VARCHAR2(4000)` | Displayable format for input bytes |
| `OUTPUT_BYTES_DISPLAY` | `VARCHAR2(4000)` | Displayable format for output bytes |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |