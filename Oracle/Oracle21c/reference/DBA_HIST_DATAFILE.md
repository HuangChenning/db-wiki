---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_DATAFILE.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.396 DBA\_HIST\_DATAFILE

`DBA_HIST_DATAFILE` displays a history of the data file information from the control file.

This view contains snapshots of `V$DATAFILE`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID |
| `FILE#` | `NUMBER` | `NOT NULL` | File identification number |
| `CREATION_CHANGE#` | `NUMBER` | `NOT NULL` | Change number at which the data file was created |
| `FILENAME` | `VARCHAR2(513)` | `NOT NULL` | Name of the data file |
| `TS#` | `NUMBER` | `NOT NULL` | Tablespace number |
| `TSNAME` | `VARCHAR2(30)` |  | Name of the tablespace |
| `BLOCK_SIZE` | `NUMBER` |  | Block size of the data file |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$DATAFILE](V-DATAFILE.md) "