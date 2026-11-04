---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_IM_SEG_STAT.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.408 DBA\_HIST\_IM\_SEG\_STAT

`DBA_HIST_IM_SEG_STAT` displays information about historical in-memory segment statistics.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `TS#` | `NUMBER` | `NOT NULL` | Tablespace number |
| `OBJ#` | `NUMBER` | `NOT NULL` | Dictionary object number |
| `DATAOBJ#` | `NUMBER` | `NOT NULL` | Data object number |
| `MEMBYTES` | `NUMBER` |  | Size of in-memory version of the segment in bytes |
| `SCANS` | `NUMBER` |  | Count of segment statistics |
| `SCANS_DELTA` | `NUMBER` |  | Delta values for in-memory scans |
| `DB_BLOCK_CHANGES` | `NUMBER` |  | The total number of changes that were part of an update or delete operation that were made to segment blocks |
| `DB_BLOCK_CHANGES_DELTA` | `NUMBER` |  | Delta value for database block changes |
| `POPULATE_CUS` | `NUMBER` |  | Count of compression units (CUs) populated per segment |
| `POPULATE_CUS_DELTA` | `NUMBER` |  | Delta value for compression unit (CU) populate operations |
| `REPOPULATE_CUS` | `NUMBER` |  | Count of CUs repopulated per segment |
| `REPOPULATE_CUS_DELTA` | `NUMBER` |  | Delta value for compression unit (CU) repopulate operations |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |