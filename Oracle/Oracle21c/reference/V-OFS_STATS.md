---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-OFS_STATS.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.100 V$OFS\_STATS

`V$OFS_STATS` displays performance statistics for various Oracle File System operations. These statistics are maintained at per mount level.

| Column | Datatype | Description |
| --- | --- | --- |
| `OFS_MNTPNT` | `VARCHAR2(4096)` | Mount point |
| `OFS_LOOKUP` | `NUMBER` | Number of lookup operations performed |
| `OFS_FORGET` | `NUMBER` | Number of forget operations performed |
| `OFS_GETATTR` | `NUMBER` | Number of getattr operations |
| `OFS_SETATTR` | `NUMBER` | Number of setattr operations |
| `OFS_READLINK` | `NUMBER` | Number of readlink operations |
| `OFS_SYMLINK` | `NUMBER` | Number of symlink operations |
| `OFS_MKNOD` | `NUMBER` | Number of mknod operations |
| `OFS_MKDIR` | `NUMBER` | Number of mkdir operations |
| `OFS_UNLINK` | `NUMBER` | Number of remove file operations |
| `OFS_RMDIR` | `NUMBER` | Number of remove directory operations |
| `OFS_RENAME` | `NUMBER` | Number of file rename operations |
| `OFS_LINK` | `NUMBER` | Number of hard link operations |
| `OFS_OPEN` | `NUMBER` | Number of file open operations |
| `OFS_READ` | `NUMBER` | Number of file read operations |
| `OFS_WRITE` | `NUMBER` | Number of file write operations |
| `OFS_STATFS` | `NUMBER` | Number of statfs operations performed |
| `OFS_RELEASE` | `NUMBER` | Number of release operations |
| `OFS_FSYNC` | `NUMBER` | Number of file sync operations |
| `OFS_SETXATTR` | `NUMBER` | Number of set extended attributes operations |
| `OFS_GETXATTR` | `NUMBER` | Number of get extended attributes |
| `OFS_LISTXATTR` | `NUMBER` | Number of list extended attributes |
| `OFS_REMOVEXATTR` | `NUMBER` | Number of remove extended attributes |
| `OFS_FLUSH` | `NUMBER` | Number of flush operations |
| `OFS_INIT` | `NUMBER` | Number of init operations |
| `OFS_OPENDIR` | `NUMBER` | Number of opendir operations |
| `OFS_READDIR` | `NUMBER` | Number of readdir operations |
| `OFS_RELEASEDIR` | `NUMBER` | Number of releasedir operations |
| `OFS_FSYNCDIR` | `NUMBER` | Number of directory sync operations |
| `OFS_GETLK` | `NUMBER` | Number of file get lock operations |
| `OFS_SETLK` | `NUMBER` | Number of file lock operations |
| `OFS_SETLKW` | `NUMBER` | Number of file lock operation with wait option |
| `OFS_ACCESS` | `NUMBER` | Number of access operations |
| `OFS_CREATE` | `NUMBER` | Number of create operations |
| `OFS_INTERRUPT` | `NUMBER` | Number of interrupt operations received on the mount |
| `OFS_BMAP` | `NUMBER` | Number of block map operations received |
| `OFS_DESTROY` | `NUMBER` | Number of destroy operations |
| `OFS_BYTES_READ` | `NUMBER` | Total number of bytes read on the mount point |
| `OFS_BYTES_WRITTEN` | `NUMBER` | Total number of bytes written to the mount point |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |

Note:

This database view is supported only on the Linux operating system.

See Also:

" [V$OFSMOUNT](V-OFSMOUNT.md) "