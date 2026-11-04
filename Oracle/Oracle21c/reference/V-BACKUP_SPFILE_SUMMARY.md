---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-BACKUP_SPFILE_SUMMARY.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.105 V$BACKUP\_SPFILE\_SUMMARY

`V$BACKUP_SPFILE_SUMMARY` provides summary information for input SP file, based on either a backup job or time range applicable to jobs.

| Column | Datatype | Description |
| --- | --- | --- |
| `NUM_FILES_BACKED` | `NUMBER` | Number of files backed up |
| `NUM_DISTINCT_FILES_BACKED` | `NUMBER` | Number of distinct SP files backed up (with modification timestamp) |
| `MIN_MODIFICATION_TIME` | `DATE` | Minimum modification time |
| `MAX_MODIFICATION_TIME` | `DATE` | Maximum modification time |
| `INPUT_BYTES` | `NUMBER` | Total input bytes for all SP files backed up |
| `INPUT_BYTES_DISPLAY` | `VARCHAR2(4000)` | Displayable format for all input bytes |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |