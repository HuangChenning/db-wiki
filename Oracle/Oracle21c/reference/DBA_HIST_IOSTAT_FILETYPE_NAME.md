---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_IOSTAT_FILETYPE_NAME.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.415 DBA\_HIST\_IOSTAT\_FILETYPE\_NAME

`DBA_HIST_IOSTAT_FILETYPE_NAME` displays historical I/O statistics for file type names.

This view contains snapshots of `V$IOSTAT_FILE`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `FILETYPE_ID` | `NUMBER` | `NOT NULL` | Type of file (for example, log file, data file, and so on) |
| `FILETYPE_NAME` | `VARCHAR2(30)` | `NOT NULL` | Name of the file, in the case of a data file or temp file. For all other files, a corresponding string to be displayed (for example, `ARCHIVELOG`). |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [V$IOSTAT\_FILE](V-IOSTAT_FILE.md) "