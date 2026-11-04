---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_TABLESPACE_STAT.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.77 DBA\_HIST\_TABLESPACE\_STAT

`DBA_HIST_TABLESPACE_STAT` displays tablespace information from the control file.

This view contains snapshots of `V$TABLESPACE` and `DBA_TABLESPACES`.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | Unique snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID for the snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number for the snapshot |
| `TS#` | `NUMBER` | `NOT NULL` | Tablespace number |
| `TSNAME` | `VARCHAR2(30)` |  | Tablespace name |
| `CONTENTS` | `VARCHAR2(9)` |  | Tablespace contents:  - `PERMANENT` - `TEMPORARY` |
| `STATUS` | `VARCHAR2(9)` |  | Tablespace status:  - `ONLINE` - `OFFLINE` - `READ ONLY` |
| `SEGMENT_SPACE_MANAGEMENT` | `VARCHAR2(6)` |  | Indicates whether the free and used segment space in the tablespace is managed using free lists (`MANUAL`) or bitmaps (`AUTO`) |
| `EXTENT_MANAGEMENT` | `VARCHAR2(10)` |  | Indicates whether the extents in the tablespace are dictionary managed (`DICTIONARY`) or locally managed (`LOCAL`) |
| `IS_BACKUP` | `VARCHAR2(5)` |  | Indicates whether the tablespace is part of a backup |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

- " [V$TABLESPACE](V-TABLESPACE.md) "
- " [DBA\_TABLESPACES](DBA_TABLESPACES.md) "