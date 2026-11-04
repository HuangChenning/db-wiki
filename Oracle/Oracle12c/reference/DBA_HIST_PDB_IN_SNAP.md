---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/DBA_HIST_PDB_IN_SNAP.html
tags:
  - oracle
  - 12c
  - reference
---

`DBA_HIST_PDB_IN_SNAP` captures a list of open pluggable databases (PDBs) at the time of the Automatic Workload Repository (AWR) snapshot. This view can be used with other DBA\_HIST\_ views to construct the number of opened PDBs at the time of the snapshot.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `SNAP_ID` | `NUMBER` | `NOT NULL` | AWR snapshot ID |
| `DBID` | `NUMBER` | `NOT NULL` | Database ID of the database that took this snapshot |
| `INSTANCE_NUMBER` | `NUMBER` | `NOT NULL` | Instance number of the instance that took this snapshot |
| `CON_DBID` | `NUMBER` |  | DBID of an open PDB at the time of the snapshot |
| `FLAG` | `NUMBER` |  | Flag field in capture properties of the PDB. Not used at this time. |
| `CON_ID` | `NUMBER` |  | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |