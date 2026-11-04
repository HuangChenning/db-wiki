---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-BACKUP_SET_SUMMARY.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.102 V$BACKUP\_SET\_SUMMARY

`V$BACKUP_SET_SUMMARY` provides summary information for a backup set.

| Column | Datatype | Description |
| --- | --- | --- |
| `NUM_BACKUPSETS` | `NUMBER` | Total number of backup sets created |
| `OLDEST_BACKUP_TIME` | `DATE` | Oldest backup start time |
| `NEWEST_BACKUP_TIME` | `DATE` | Newest backup start time |
| `OUTPUT_BYTES` | `NUMBER` | Number of output bytes (not including multiple copies) |
| `ORIGINAL_INPUT_BYTES` | `NUMBER` | Number of input bytes when backup sets were created |
| `ORIGINAL_INPRATE_BYTES` | `NUMBER` | Average input rate |
| `OUTPUT_RATE_BYTES` | `NUMBER` | Average output rate |
| `COMPRESSION_RATIO` | `NUMBER` | The ratio between the total blocks in the datafile and the blocks that RMAN backed up. This is not the the ratio from the `AS COMPRESSED BACKUPSET` clause of the `BACKUP` command. |
| `ORIGINAL_INPUT_BYTES_DISPLAY` | `VARCHAR2(4000)` | Displayable format for input bytes |
| `OUTPUT_BYTES_DISPLAY` | `VARCHAR2(4000)` | Displayable format for output bytes |
| `ORIGINAL_INPRATE_BYTES_DISPLAY` | `VARCHAR2(4000)` | Displayable format for input rate |
| `OUTPUT_RATE_BYTES_DISPLAY` | `VARCHAR2(4000)` | Displayable format for output rate |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |