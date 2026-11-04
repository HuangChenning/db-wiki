---
title: "V$DNFS_STATS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1120.htm
tags:
  - oracle
  - 11g
  - reference
---

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
| `NFS_READBYTES` <sup>Foot 1</sup> | `NUMBER` | Number of bytes read from NFS server |
| `NFS_WRITEBYTES` <sup>Footref 1</sup> | `NUMBER` | Number of bytes written to NFS server |

<sup>Footnote 1</sup> This column is available starting with Oracle Database 11g Release 2 (11.2.0.4)