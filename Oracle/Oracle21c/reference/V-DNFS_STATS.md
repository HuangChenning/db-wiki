---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-DNFS_STATS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.191 V$DNFS\_STATS

`V$DNFS_STATS` displays information about the Oracle process NFS operation statistics issued by Direct NFS.

| Column | Datatype | Description |
| --- | --- | --- |
| `PNUM` | `NUMBER` | Oracle process number that statistics are relevant to |
| `NFS_NULL` | `NUMBER` | Null |
| `NFS_GETATTR` | `NUMBER` | Get attributes |
| `NFS_SETATTR` | `NUMBER` | Set attributes |
| `NFS_LOOKUP` | `NUMBER` | Lookup object |
| `NFS_ACCESS` | `NUMBER` | Access object |
| `NFS_READLINK` | `NUMBER` | Read link |
| `NFS_READ` | `NUMBER` | Read file |
| `NFS_WRITE` | `NUMBER` | Write file |
| `NFS_CREATE` | `NUMBER` | Create file |
| `NFS_MKDIR` | `NUMBER` | Make directory |
| `NFS_SYMLINK` | `NUMBER` | Symbolic link |
| `NFS_MKNOD` | `NUMBER` | Make node |
| `NFS_REMOVE` | `NUMBER` | Remove file |
| `NFS_RMDIR` | `NUMBER` | Remove directory |
| `NFS_RENAME` | `NUMBER` | Rename |
| `NFS_LINK` | `NUMBER` | Link |
| `NFS_READDIR` | `NUMBER` | Read directory |
| `NFS_READDIRPLUS` | `NUMBER` | Read directory plus |
| `NFS_FSSTAT` | `NUMBER` | File system status |
| `NFS_FSINFO` | `NUMBER` | File system information |
| `NFS_PATHCONF` | `NUMBER` | Path configuration |
| `NFS_COMMIT` | `NUMBER` | Commit |
| `NFS_MOUNT` | `NUMBER` | Mount |
| `NFS_READBYTES` | `NUMBER` | Number of bytes read from NFS server |
| `NFS_WRITEBYTES` | `NUMBER` | Number of bytes written to NFS server |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |