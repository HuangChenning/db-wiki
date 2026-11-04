---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DBA_PDB_SNAPSHOTFILE.html
tags:
  - oracle
  - 21c
  - reference
---

## 6.238 DBA\_PDB\_SNAPSHOTFILE

`DBA_PDB_SNAPSHOTFILE` displays the files associated with snapshots taken of pluggable databases (PDBs).

You can use this view in conjunction with the `DBA_PDB_SNAPSHOT` view. Join the `SNAPSHOT_SCN` column in this view with the `SNAPSHOT_SCN` column in `DBA_PDB_SNAPSHOT` to determine the files associated with a particular PDB snapshot. A PDB snapshot consists of an archive log file, one or more data files, and one or more XML files. A row is added to this view for each file associated with a PDB snapshot.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `CON_ID` | `NUMBER` | `NOT NULL` | The ID of the PDB |
| `SNAPSHOT_SCN` | `NUMBER` | `NOT NULL` | SCN at which the snapshot was taken |
| `SNAPSHOT_FILENAME` | `VARCHAR2(513)` | `NOT NULL` | Snapshot file name |
| `SNAPSHOT_FILETYPE` | `VARCHAR2(8)` | `NOT NULL` | Snapshot file type. Possible values:  - `ARCH`: Archive log file - `DATA`: Data file - `XML`: XML file |

See Also:

" [DBA\_PDB\_SNAPSHOTS](DBA_PDB_SNAPSHOTS.md) "