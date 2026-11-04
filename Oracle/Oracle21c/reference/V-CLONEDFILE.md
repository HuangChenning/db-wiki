---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-CLONEDFILE.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.127 V$CLONEDFILE

| Column | Datatype | Description |
| --- | --- | --- |
| `SNAPSHOTFILENAME` | `VARCHAR2(513)` | Snapshot file name. This file is the snapshot file from the snapshot database. The snapshot file is also sometimes referred to as the srcfile. |
| `CLONEFILENAME` | `VARCHAR2(513)` | CloneDB file name. This file is the cloned file (of the snapshot file) which resides in the current (cloned database). The cloned file is sometimes referred to as the destfile. |
| `SNAPSHOTBLKREAD` | `NUMBER` | Number of blocks reads to the snapshot file |
| `SNAPSHOTREQUEST` | `NUMBER` | Number of read requests to the snapshot file |
| `FILENUMBER` | `NUMBER` | File number of the cloned file |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `BLOCKS_ALLOCATED` | `NUMBER` | Amount of space allocated in blocks in the file system. This is less than or equal to the actual file size. |

Note:

When this view is queried in an Oracle Database environment, rows are returned for every opened file, even those without a parent file backing them (in those cases the column is empty/NULL).

In an Oracle ASM environement, rows are returned for files that an Oracle ASM instance has mounted in disk groups only if those files are children (a clonefile) of a parent snapshot file.