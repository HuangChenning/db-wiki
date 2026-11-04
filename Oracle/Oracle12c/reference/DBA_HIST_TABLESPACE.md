---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_HIST_TABLESPACE.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_HIST_TABLESPACE` displays tablespace information contained in the Workload Repository.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID |
| `TS#` | `NUMBER` | `NOT NULL` | Tablespace number |
| `TSNAME` | `VARCHAR2(30)` | `NOT NULL` | Tablespace name |
| `CONTENTS` | `VARCHAR2(30)` |  | Tablespace contents:  - `UNDO` - `PERMANENT` - `TEMPORARY` |
| `SEGMENT_SPACE_MANAGEMENT` | `VARCHAR2(30)` |  | Indicates whether the free and used space in the tablespace is managed using free lists (`MANUAL`) or bitmaps (`AUTO`) |
| `EXTENT_MANAGEMENT` | `VARCHAR2(30)` |  | Indicates whether the extents in the tablespace are dictionary managed (`DICTIONARY`) or locally managed (`LOCAL`) |
| `BLOCK_SIZE` | `NUMBER` |  | Block size of the tablespace |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |