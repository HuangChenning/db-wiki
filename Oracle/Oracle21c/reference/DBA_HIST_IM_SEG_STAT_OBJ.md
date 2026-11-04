---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_HIST_IM_SEG_STAT_OBJ.html
tags:
  - oracle
  - 21c
  - reference
---

## 5.409 DBA\_HIST\_IM\_SEG\_STAT\_OBJ

`DBA_HIST_IM_SEG_STAT_OBJ` displays information about object metadata for historical in-memory segments.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `DBID` | `NUMBER` | `NOT NULL` | Database id for the snapshot |
| `TS#` | `NUMBER` | `NOT NULL` | Tablespace number |
| `OBJ#` | `NUMBER` | `NOT NULL` | Dictionary object number |
| `DATAOBJ#` | `NUMBER` | `NOT NULL` | Data object number |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the object |
| `OBJECT_NAME` | `VARCHAR2(128)` |  | Name of the object |
| `SUBOBJECT_NAME` | `VARCHAR2(128)` |  | Name of the subobject |
| `OBJECT_TYPE` | `VARCHAR2(128)` |  | Type of the object |
| `TABLESPACE_NAME` | `VARCHAR2(128)` |  | Tablespace name for the object |
| `CON_DBID` | `NUMBER` |  | The database ID of the PDB for the sampled session |
| `CON_ID` | `NUMBER` |  | The ID of the container that `CON_DBID` identifies. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |