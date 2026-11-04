---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-BACKUP_COPY_SUMMARY.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.89 V$BACKUP\_COPY\_SUMMARY

`V$BACKUP_COPY_SUMMARY` provides summary information for the output data file and control file copy.

| Column | Datatype | Description |
| --- | --- | --- |
| `NUM_COPIES` | `NUMBER` | Number of copies created |
| `NUM_DISTINCT_COPIES` | `NUMBER` | Number of distinct copies (that contain data files with different checkpoints) |
| `MIN_CHECKPOINT_CHANGE#` | `NUMBER` | Minimum checkpoint change SCN |
| `MAX_CHECKPOINT_CHANGE#` | `NUMBER` | Maximum checkpoint change SCN |
| `MIN_CHECKPOINT_TIME` | `DATE` | Minimum checkpoint change time |
| `MAX_CHECKPOINT_TIME` | `DATE` | Maximum checkpoint change time |
| `OUTPUT_BYTES` | `NUMBER` | Total number of output bytes |
| `OUTPUT_BYTES_DISPLAY` | `VARCHAR2(4000)` | Displayable format for output bytes |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |