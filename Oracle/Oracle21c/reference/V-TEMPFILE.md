---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-TEMPFILE.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.110 V$TEMPFILE

| Column | Datatype | Description |
| --- | --- | --- |
| `FILE#` | `NUMBER` | Absolute file number |
| `CREATION_CHANGE#` | `NUMBER` | Creation System Change Number (SCN) |
| `CREATION_TIME` | `DATE` | Creation time |
| `TS#` | `NUMBER` | Tablespace number |
| `RFILE#` | `NUMBER` | Relative file number in the tablespace |
| `STATUS` | `VARCHAR2(7)` | Status of the file (`OFFLINE` \| `ONLINE`) |
| `ENABLED` | `VARCHAR2(10)` | Enabled for read and/or write |
| `BYTES` | `NUMBER` | Size of the file in bytes (from the file header) |
| `BLOCKS` | `NUMBER` | Size of the file in blocks (from the file header) |
| `CREATE_BYTES` | `NUMBER` | Creation size of the file (in bytes) |
| `BLOCK_SIZE` | `NUMBER` | Block size for the file |
| `NAME` | `VARCHAR2(513)` | Name of the file |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |