---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-CONTROLFILE.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.142 V$CONTROLFILE

`V$CONTROLFILE` displays the names of the control files.

| Column | Datatype | Description |
| --- | --- | --- |
| `STATUS` | `VARCHAR2(7)` | `INVALID` if the name cannot be determined (which should not occur); NULL if the name can be determined |
| `NAME` | `VARCHAR2(513)` | Name of the control file |
| `IS_RECOVERY_DEST_FILE` | `VARCHAR2(3)` | Indicates whether the file was created in the fast recovery area (`YES`) or not (`NO`) |
| `BLOCK_SIZE` | `NUMBER` | Control file block size |
| `FILE_SIZE_BLKS` | `NUMBER` | Control file size (in blocks) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |