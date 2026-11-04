---
title: "V$BACKUP_SET_SUMMARY"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1063.htm
tags:
  - oracle
  - 11g
  - reference
---

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