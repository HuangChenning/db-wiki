---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-OFSMOUNT.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.101 V$OFSMOUNT

`V$OFSMOUNT` provides information about the file systems that are mounted by Oracle File System.

| Column | Datatype | Description |
| --- | --- | --- |
| `OFS_MNTPATH` | `VARCHAR2(1024)` | Mount path where the file system is mounted |
| `OFS_FSPATH` | `VARCHAR2(1024)` | File system path |
| `OFS_MNTOPTS` | `VARCHAR2(1024)` | Mount options used to mount the file system |
| `OFS_MNTFLAGS` | `VARCHAR2(7)` | Flags to specify if the file system is mounted. A value of 1 indicates that the file system is mounted. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |
| `OFS_NODENM` | `VARCHAR2(255)` | Node name |
| `OFS_FSID` | `NUMBER` | Unique ID that identifies the mounted file system |
| `OFS_FSTYPE` | `VARCHAR2(255)` | Oracle file system type. This is the value that is passed to the `dbms_fs.mount_oracle_fs()` procedure. Some of the expected values are `dbfs` and `ofs`. |

Note:

This database view is supported only on the Linux operating system.

See Also:

- " [V$OFS\_STATS](V-OFS_STATS.md) "
- [Oracle Database PL/SQL Packages and Types Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=ARPLS-GUID-DFB3DF98-30CF-4ECE-89FC-A73E66449991) for more information about the `DBMS_FS.MOUNT_ORACLE_FS` procedure