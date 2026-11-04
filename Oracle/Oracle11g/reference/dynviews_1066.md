---
title: "V$BACKUP_SPFILE_SUMMARY"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1066.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$BACKUP_SPFILE_SUMMARY` provides summary information for input SP file, based on either a backup job or time range applicable to jobs.

| Column | Datatype | Description |
| --- | --- | --- |
| `NUM_FILES_BACKED` | `NUMBER` | Number of files backed up |
| `NUM_DISTINCT_FILES_BACKED` | `NUMBER` | Number of distinct SP files backed up (with modification timestamp) |
| `MIN_MODIFICATION_TIME` | `DATE` | Minimum modification time |
| `MAX_MODIFICATION_TIME` | `DATE` | Maximum modification time |
| `INPUT_BYTES` | `NUMBER` | Total input bytes for all SP files backed up |
| `INPUT_BYTES_DISPLAY` | `VARCHAR2(4000)` | Displayable format for all input bytes |