---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_SEG_STAT_OBJ.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.45 DBA\_HIST\_SEG\_STAT\_OBJ

`DBA_HIST_SEG_STAT_OBJ` displays all the names of the segments captured in the workload repository.

This view is used with the `DBA_HIST_SEG_STAT` view.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID |
| `TS#` | `NUMBER` | `NOT NULL` | Tablespace number |
| `OBJ#` | `NUMBER` | `NOT NULL` | Dictionary object number |
| `DATAOBJ#` | `NUMBER` | `NOT NULL` | Data object number |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the object |
| `OBJECT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the object |
| `SUBOBJECT_NAME` | `VARCHAR2(128)` |  | Name of the subobject (for example: partition) |
| `OBJECT_TYPE` | `VARCHAR2(18)` |  | Type of the object for example: table, tablespace) |
| `TABLESPACE_NAME` | `VARCHAR2(30)` |  | Tablespace Name for the object |
| `PARTITION_TYPE` | `VARCHAR2(8)` |  | Partition Type, if relevant |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

See Also:

" [DBA\_HIST\_SEG\_STAT](DBA_HIST_SEG_STAT.md) "