---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-CLONEDFILE.html
tags:
  - oracle
  - 12c
  - reference
---

| Column | Datatype | Description |
| --- | --- | --- |
| `SNAPSHOTFILENAME` | `VARCHAR2(513)` | Snapshot/master file name. This file is the master file from the master database. The snapshot file is also sometimes referred to as the srcfile. |
| `CLONEFILENAME` | `VARCHAR2(513)` | CloneDB file name. This file is the cloned file (of master file) which resides in the current (cloned database). The cloned file is sometimes referred to as the destfile. |
| `SNAPSHOTBLKREAD` | `NUMBER` | Number of blocks reads to the snapshot file (master file) |
| `SNAPSHOTREQUEST` | `NUMBER` | Number of read requests to the snapshot file (master file) |
| `FILENUMBER` | `NUMBER` | File number of the cloned file |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `BLOCKS_ALLOCATED` | `NUMBER` | Amount of space allocated in blocks in the file system. This is less than or equal to the actual file size. |

Note:

When this view is queried in an Oracle Database environment, rows are returned for every opened file, even those without a parent file backing them (in those cases the column is empty/NULL).

In an Oracle ASM environement, rows are returned for files that an Oracle ASM instance has mounted in disk groups only if those files are children (a clonefile) of a parent snapshot file.