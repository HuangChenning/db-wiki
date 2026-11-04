---
title: "V$BACKUP_DATAFILE_SUMMARY"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1055.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$BACKUP_DATAFILE_SUMMARY` provides summary information for a specific criteria set, based on a backup job, a time range applicable to jobs, or a specific datafile).

| Column | Datatype | Description |
| --- | --- | --- |
| `NUM_FILES_BACKED` | `NUMBER` | Number of files backed up for specified criteria |
| `NUM_DISTINCT_FILES_BACKED` | `NUMBER` | Number of distinct files backed up |
| `NUM_DISTINCT_TS_BACKED` | `NUMBER` | Number of distinct tablespaces backed up |
| `MIN_CHECKPOINT_CHANGE#` | `NUMBER` | Minimum checkpoint change number of the datafile for specified criteria |
| `MAX_CHECKPOINT_CHANGE#` | `NUMBER` | Maximum checkpoint change number of the datafile for specified criteria |
| `MIN_CHECKPOINT_TIME` | `DATE` | Minimum checkpoint time of the datafile for specified criteria |
| `MAX_CHECKPOINT_TIME` | `DATE` | Maximum checkpoint time of the datafile for specified criteria |
| `INPUT_BYTES` | `NUMBER` | Total input bytes of files read |
| `OUTPUT_BYTES` | `NUMBER` | Total output bytes written |
| `COMPRESSION_RATIO` | `NUMBER` | The ratio between the total blocks in the datafile and the blocks that RMAN backed up. This is not the the ratio from the `AS COMPRESSED BACKUPSET` clause of the `BACKUP` command. |
| `INPUT_BYTES_DISPLAY` | `VARCHAR2(4000)` | Displayable format for input bytes |
| `OUTPUT_BYTES_DISPLAY` | `VARCHAR2(4000)` | Displayable format for output bytes |