---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_PDB_SNAPSHOTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.239 DBA\_PDB\_SNAPSHOTS

`DBA_PDB_SNAPSHOTS` describes the snapshots taken of pluggable databases (PDBs).

Rows are added to this view when a snapshot of a PDB is taken by using the `ALTER` `PLUGGABLE` `DATABASE` `SNAPSHOT` SQL statement.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CON_ID` | `NUMBER` | `NOT NULL` | The ID of the PDB |
| `CON_UID` | `NUMBER` | `NOT NULL` | Unique ID assigned to the PDB at creation time |
| `CON_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the PDB |
| `SNAPSHOT_NAME` | `VARCHAR2(128)` | `NOT NULL` | Snapshot name of the PDB |
| `SNAPSHOT_SCN` | `NUMBER` | `NOT NULL` | SCN at which the snapshot was taken |
| `PREVIOUS_SNAPSHOT_SCN` | `NUMBER` | `NOT NULL` | SCN at which the previous snapshot for the PDB was taken |
| `SNAPSHOT_TIME` | `NUMBER` | `NOT NULL` | Timestamp at which the snapshot was taken |
| `PREVIOUS_SNAPSHOT_TIME` | `NUMBER` | `NOT NULL` | Timestamp of the previous snapshot for this PDB |
| `FULL_SNAPSHOT_PATH` | `VARCHAR2(4000)` | `NOT NULL` | Full path for the snapshot |

Note:

This view does not display snapshot copy PDBs, which are created by using the `CREATE` `PLUGGABLE` `DATABASE`... `SNAPSHOT` `COPY` SQL statement.

See Also:

" [DBA\_PDB\_SNAPSHOTFILE](DBA_PDB_SNAPSHOTFILE.md) " for information about the files associated with a particular PDB snapshot