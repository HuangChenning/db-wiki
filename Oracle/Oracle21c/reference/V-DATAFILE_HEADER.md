---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-DATAFILE_HEADER.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.159 V$DATAFILE\_HEADER

`V$DATAFILE_HEADER` displays data file information from the data file headers.

| Column | Datatype | Description |
| --- | --- | --- |
| `FILE#` | `NUMBER` | Data file number (from control file) |
| `STATUS` | `VARCHAR2(7)` | `ONLINE` \| `OFFLINE` (from control file) |
| `ERROR` | `VARCHAR2(18)` | NULL if the data file header read and validation were successful. If the read failed then the rest of the columns are NULL. If the validation failed then the rest of columns may display invalid data. If there is an error then usually the data file must be restored from a backup before it can be recovered or used. |
| `FORMAT` | `NUMBER` | Indicates the format for the header block. The possible values are `6,` `7`, `8`, `10` or `0`.  `6` - indicates Oracle Version 6  `7` - indicates Oracle Version 7  `8` - indicates Oracle Version 8  `10` - indicates Oracle Version 10  `0` - indicates the format could not be determined (for example, the header could not be read) |
| `RECOVER` | `VARCHAR2(3)` | File needs media recovery (`YES` \| `NO`) |
| `FUZZY` | `VARCHAR2(3)` | File is fuzzy (`YES` \| `NO`) |
| `CREATION_CHANGE#` | `NUMBER` | Data file creation change# |
| `CREATION_TIME` | `DATE` | Data file creation timestamp |
| `TABLESPACE_NAME` | `VARCHAR2(30)` | Tablespace name |
| `TS#` | `NUMBER` | Tablespace number |
| `RFILE#` | `NUMBER` | Tablespace relative data file number |
| `RESETLOGS_CHANGE#` | `NUMBER` | Resetlogs change# |
| `RESETLOGS_TIME` | `DATE` | Resetlogs timestamp |
| `CHECKPOINT_CHANGE#` | `NUMBER` | Data file checkpoint change# |
| `CHECKPOINT_TIME` | `DATE` | Data file checkpoint timestamp |
| `CHECKPOINT_COUNT` | `NUMBER` | Data file checkpoint count |
| `BYTES` | `NUMBER` | Current data file size in bytes |
| `BLOCKS` | `NUMBER` | Current data file size in blocks |
| `NAME` | `VARCHAR2(513)` | Data file name |
| `SPACE_HEADER` | `VARCHAR2(40)` | Represents the block address of a space file header block of a locally managed data file |
| `LAST_DEALLOC_CHANGE#` | `VARCHAR2(16)` | Last deallocated SCN |
| `UNDO_OPT_CURRENT_CHANGE#` | `VARCHAR2(40)` | For internal use only |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `IS_SPARSE` | `VARCHAR2(3)` | Indicates whether the file is sparse (`YES`) or not (`NO`) |
| `ENCRYPTED` | `VARCHAR2(3)` | After file encryption is completed, this column indicates whether the file is encrypted (`YES`) or not (`NO`).  When file encryption is still in progress, this column has a value of `NO`. |