---
title: "V$BACKUP_ARCHIVELOG_SUMMARY"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1046.htm
tags:
  - oracle
  - 11g
  - reference
---

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