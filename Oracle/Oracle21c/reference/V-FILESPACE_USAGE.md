---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-FILESPACE_USAGE.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.230 V$FILESPACE\_USAGE

`V$FILESPACE_USAGE` summarizes space allocation information of each data file and temp file.

| Column | Datatype | Description |
| --- | --- | --- |
| `TABLESPACE_ID` | `NUMBER` | ID of the tablespace to which the file belongs |
| `RFNO` | `NUMBER` | Relative file number of the file |
| `ALLOCATED_SPACE` | `NUMBER` | Total allocated space in the file |
| `FILE_SIZE` | `NUMBER` | Current file size |
| `FILE_MAXSIZE` | `NUMBER` | Maximum file size |
| `CHANGESCN_BASE` | `NUMBER` | SCN base of the last change to the file |
| `CHANGESCN_WRAP` | `NUMBER` | SCN wrap of the last change to the file |
| `CHANGESCN8` | `NUMBER` | The 8–byte representation of the SCN at which the last change happened to the file |
| `FLAG` | `NUMBER` | Flags for file attributes |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |