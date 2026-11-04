---
title: "V$CLONEDFILE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1083.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$CLONEDFILE` provides CloneDB file information.

| Column | Datatype | Description |
| --- | --- | --- |
| `SNAPSHOTFILENAME` | `VARCHAR2(513)` | Snapshot/master file name. This file is the master file from the master database. The snapshot file is also sometimes referred to as the srcfile. |
| `CLONEFILENAME` | `VARCHAR2(513)` | CloneDB file name. This file is the cloned file (of master file) which resides in the current (cloned database). The cloned file is sometimes referred to as the destfile. |
| `SNAPSHOTBLKREAD` | `NUMBER` | Number of blocks reads to the snapshot file (master file) |
| `SNAPSHOTREQUEST` | `NUMBER` | Number of read requests to the snapshot file (master file) |
| `FILENUMBER` | `NUMBER` | File number of the cloned file |
| `BLOCKS_ALLOCATED` | `NUMBER` | Amount of space allocated in blocks in the file system. This is less than or equal to the actual file size. |

Note:

The `V$CLONEDFILE` view is is available starting with Oracle Database 11g Release 2 (11.2.0.4).

See Also:

[Oracle Database Administrator's Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25494/create.htm#ADMIN14023) for more information about cloning a database with CloneDB