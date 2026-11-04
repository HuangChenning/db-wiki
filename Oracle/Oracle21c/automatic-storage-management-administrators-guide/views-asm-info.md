---
title: "Administrator's Guide"
book: "Automatic Storage Management Administrator's Guide"
doc_id: F30296-05
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/ostmg/views-asm-info.html
tags:
  - oracle
  - 21c
  - automatic-storage-management-administrators-guide
---

Dynamic views display important information about Oracle ASM.

This chapter contains information about using dynamic views to display Oracle Automatic Storage Management (Oracle ASM) information.

See Also:

- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=REFRN-GUID-8C5690B0-DE10-4460-86DF-80111869CF4C) for information about all dynamic performance views
- [Managing Oracle ASM with ASMCMD](manage-asm-asmcmd.md) for ASMCMD `ls*` commands that display Oracle ASM information.

### Views Containing Oracle ASM Information

The views listed in Table 6-1 provide information about Oracle ASM.

For information about all dynamic performance views that display information about Oracle ASM, refer to [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=REFRN003)

Note:

The `REDUNDANCY_LOWERED` column in the `V$ASM_FILE` view no longer provides information about files with reduced redundancy. This column is deprecated, and it always displays a value of `U`.

Table 6-1 Oracle ASM dynamic views

| View | Description |
| --- | --- |
| `V$ASM_ALIAS` | Contains one row for every alias present in every disk group mounted by the Oracle ASM instance. |
| `V$ASM_ATTRIBUTE` | Displays one row for each attribute defined. In addition to attributes specified by `CREATE` `DISKGROUP` and `ALTER` `DISKGROUP` statements, the view may show other attributes that are created automatically. Attributes are only displayed for disk groups where `COMPATIBLE.ASM` is set to `11.1` or higher. |
| `V$ASM_AUDIT_CLEANUP_JOBS` | Displays information about the configured audit trail purge jobs. |
| `V$ASM_AUDIT_CONFIG_PARAMS` | Displays information about the currently configured audit trail properties. |
| `V$ASM_AUDIT_LAST_ARCH_TS` | Displays information about the last archive timestamps set for audit trail cleanup or purges. |
| `V$ASM_CLIENT` | In an Oracle ASM instance, identifies databases using disk groups managed by the Oracle ASM instance.  In an Oracle Database instance, contains information about the Oracle ASM instance if the database has any open Oracle ASM files. |
| `V$ASM_DBCLONE_INFO` | In an Oracle ASM instance, shows the relationship between the source database, the cloned database, and their file groups. |
| `V$ASM_DISK` | Contains one row for every disk discovered by the Oracle ASM instance, including disks that are not part of any disk group.  This view performs disk discovery every time it is queried. Because performing a discovery is very resource intensive, this view is not recommended for monitoring scripts. |
| `V$ASM_DISK_IOSTAT` | Displays information about disk I/O statistics for each Oracle ASM client.  In an Oracle Database instance, only the rows for that instance are shown. |
| `V$ASM_DISK_STAT` | Contains the same columns as `V$ASM_DISK`, but to reduce overhead, does not perform a discovery when it is queried. `V$ASM_DISK_STAT` only returns information about any disks that are part of mounted disk groups in the storage system.  The `V$ASM_DISK_STAT` view is recommended for monitoring scripts.  To display information about all disks, use `V$ASM_DISK` instead. |
| `V$ASM_DISKGROUP` | Describes a disk group (number, name, size related info, state, and redundancy type).  This view performs disk discovery every time it is queried. Because performing a discovery is very resource intensive, this view is not recommended for monitoring scripts. |
| `V$ASM_DISKGROUP_STAT` | Contains the same columns as `V$ASM_DISKGROUP`, but to reduce overhead, `V$ASM_DISKGROUP_STAT` does not perform a discovery when it is queried.  The `V$ASM_DISKGROUP_STAT` view is recommended for monitoring scripts.  To display more complete information about all disks, use `V$ASM_DISKGROUP`. |
| `V$ASM_ESTIMATE` | Displays an estimate of the work involved in execution plans for Oracle ASM disk group rebalance and resync operations. |
| `V$ASM_FILE` | Contains one row for every Oracle ASM file in every disk group mounted by the Oracle ASM instance. |
| `V$ASM_FILEGROUP` | Contains one row for every file group in every disk group mounted by the Oracle ASM instance. |
| `V$ASM_FILEGROUP_FILE` | Contains one row for each file associated with a file group in every disk group mounted by the Oracle ASM instance. |
| `V$ASM_FILEGROUP_PROPERTY` | Contains one row for every property associated with the file group or each file type of every file group in every disk group mounted by the Oracle ASM instance. |
| `V$ASM_OPERATION` | In an Oracle ASM instance, contains one row for every active Oracle ASM long running operation executing in the Oracle ASM instance.  In an Oracle Database instance, contains no rows. |
| `V$ASM_QUOTAGROUP` | Contains one row for every Oracle Automatic Storage Management (Oracle ASM) quota group discovered by the Oracle ASM instance on the node. |
| `V$ASM_TEMPLATE` | Contains one row for every template present in every disk group mounted by the Oracle ASM instance. |
| `V$ASM_USER` | Contains the effective operating system user names of connected database instances and names of file owners. |
| `V$ASM_USERGROUP` | Contains the creator for each Oracle ASM File Access Control group. |
| `V$ASM_USERGROUP_MEMBER` | Contains the members for each Oracle ASM File Access Control group. |

When querying `V$ASM` views, the value of the disk group number is not a static value. When a disk group is mounted, a disk group number is chosen. This number may change across disk group mounts. A disk group number is not recorded in any persistent structure, but the current value can be viewed in the `GROUP_NUMBER` column of the `V$ASM` views.

Example 6-1 Viewing disk group attributes with V$ASM\_ATTRIBUTE

This is an example of the use of the `V$ASM_ATTRIBUTE` and `V$ASM_DISKGROUP` views. The `COMPATIBLE.ASM` value must be set to `11.1` or higher for the disk group to display in the `V$ASM_ATTRIBUTE` view output. Attributes that are designated as read-only (`Y`) can only be set during disk group creation.

```
SELECT SUBSTR(dg.name,1,12) AS diskgroup, SUBSTR(a.name,1,24) AS name,
     SUBSTR(a.value,1,24) AS value, read_only FROM V$ASM_DISKGROUP dg, 
     V$ASM_ATTRIBUTE a WHERE dg.name = 'DATA' AND dg.group_number = a.group_number
     AND a.name NOT LIKE '%template%';

DISKGROUP    NAME                     VALUE                    READ_ON
------------ ------------------------ ------------------------ -------
DATA         idp.type                 dynamic                  N
DATA         idp.boundary             auto                     N
DATA         vam_migration_done       false                    Y
DATA         scrub_metadata.enabled   TRUE                     N
DATA         scrub_async_limit        1                        N
DATA         content_hardcheck.enable FALSE                    N
DATA         access_control.umask     066                      N
DATA         access_control.enabled   FALSE                    N
DATA         cell.sparse_dg           allnonsparse             N
DATA         cell.smart_scan_capable  FALSE                    N
DATA         compatible.advm          19.0.0.0.0               N
DATA         compatible.rdbms         19.0.0.0.0               N
DATA         compatible.asm           19.0.0.0.0               N
DATA         appliance._partnering_ty GENERIC                  Y
DATA         au_size                  1048576                  Y
DATA         content.check            FALSE                    N
DATA         content.type             data                     N
DATA         logical_sector_size      512                      N
DATA         sector_size              512                      N
DATA         ate_conversion_done      true                     Y
DATA         preferred_read.enabled   FALSE                    N
DATA         thin_provisioned         FALSE                    N
DATA         failgroup_repair_time    24.0h                    N
DATA         phys_meta_replicated     true                     Y
DATA         disk_repair_time         12.0h                    N
```

Example 6-2 Viewing the compatibility of a disk group with V$ASM\_DISKGROUP

This is an example of displaying the compatibility for a disk group with the `V$ASM_DISKGROUP` view.

```
SELECT name AS diskgroup, substr(compatibility,1,12) AS asm_compat,
     substr(database_compatibility,1,12) AS db_compat FROM V$ASM_DISKGROUP;

DISKGROUP                      ASM_COMPAT   DB_COMPAT
------------------------------ ------------ ------------
DATA                           19.0.0.0.0   19.0.0.0.0
FRA                            19.0.0.0.0   19.0.0.0.0
```

Example 6-3 Viewing disks in disk groups with V$ASM\_DISK

This is an example of the use of the `V$ASM_DISK` and `V$ASM_DISKGROUP` views run on an Oracle ASM instance. The example displays the disks associated with a disk group, plus the mount status, state, and failure group of the disks.

```
SELECT SUBSTR(dg.name,1,16) AS diskgroup, SUBSTR(d.name,1,16) AS asmdisk,
     d.mount_status, d.state, SUBSTR(d.failgroup,1,16) AS failgroup 
     FROM V$ASM_DISKGROUP dg, V$ASM_DISK d WHERE dg.group_number = d.group_number;

DISKGROUP        ASMDISK          MOUNT_S STATE    FAILGROUP
---------------- ---------------- ------- -------- ----------------
DATA             DATA_0008        CACHED  NORMAL   DATA_0008
DATA             DATA_0000        CACHED  NORMAL   DATA_0000
DATA             DATA_0004        CACHED  NORMAL   DATA_0004
DATA             DATA_0015        CACHED  NORMAL   DATA_0015
DATA             DATA_0003        CACHED  NORMAL   DATA_0003
DATA             DATA_0012        CACHED  NORMAL   DATA_0012
DATA             DATA_0017        CACHED  NORMAL   DATA_0017
DATA             DATA_0013        CACHED  NORMAL   DATA_0013
DATA             DATA_0007        CACHED  NORMAL   DATA_0007
DATA             DATA_0014        CACHED  NORMAL   DATA_0014
DATA             DATA_0009        CACHED  NORMAL   DATA_0009
DATA             DATA_0001        CACHED  NORMAL   DATA_0001
DATA             DATA_0016        CACHED  NORMAL   DATA_0016
DATA             DATA_0011        CACHED  NORMAL   DATA_0011
DATA             DATA_0005        CACHED  NORMAL   DATA_0005
DATA             DATA_0010        CACHED  NORMAL   DATA_0010
DATA             DATA_0002        CACHED  NORMAL   DATA_0002
DATA             DATA_0006        CACHED  NORMAL   DATA_0006
FRA              FRA_0012         CACHED  NORMAL   FRA_0012
FRA              FRA_0013         CACHED  NORMAL   FRA_0013
FRA              FRA_0007         CACHED  NORMAL   FRA_0007
FRA              FRA_0006         CACHED  NORMAL   FRA_0006
FRA              FRA_0010         CACHED  NORMAL   FRA_0010
FRA              FRA_0000         CACHED  NORMAL   FRA_0000
FRA              FRA_0003         CACHED  NORMAL   FRA_0003
...
```

Example 6-4 Viewing disks in disk groups with V$ASM\_DISK\_STAT

This is an example of the use of the `V$ASM_DISK_STAT` and `V$ASM_DISKGROUP_STAT` views run on an Oracle ASM instance. The example displays the disks associated with a specific disk group along with the mount status, state, and various read and write statistics.

```
SELECT SUBSTR(dgs.name,1,10) AS diskgroup, SUBSTR(ds.name,1,10) AS asmdisk, 
       ds.mount_status, ds.state, ds.reads, ds.writes, ds.read_time, ds.write_time, 
       bytes_read, bytes_written 
       FROM V$ASM_DISKGROUP_STAT dgs, V$ASM_DISK_STAT ds 
       WHERE dgs.group_number = ds.group_number AND dgs.name = 'DATA';

DISKGROUP  ASMDISK    MOUNT_S STATE    READS WRITES READ_TIME WRITE_TIME BYTES_READ BYTES_WRITTEN
---------- ---------- ------- ------- ------ ------ --------- ---------- ---------- -------------
DATA       DATA_0000  CACHED  NORMAL     841  10407  1.212218   3.511977   23818240     178369024
DATA       DATA_0008  CACHED  NORMAL   26065   1319  1.592524    .297728  436203520      38358528
DATA       DATA_0010  CACHED  NORMAL     561    868   .794849    .337575   18631680      22584320
DATA       DATA_0004  CACHED  NORMAL     695  10512  1.282711   3.351801   23240704     177246208
DATA       DATA_0006  CACHED  NORMAL     484   1642  1.506733     .45724   19857408      30191616
DATA       DATA_0016  CACHED  NORMAL     583   1028  2.283268    .263629   21012480      17682432
DATA       DATA_0007  CACHED  NORMAL     724   2316  1.259379    .546318   26017792      42283008
DATA       DATA_0009  CACHED  NORMAL     537    757  1.146663    .241434   19893248      20633088
DATA       DATA_0014  CACHED  NORMAL    1049   1464  7.346259    .677313   25378816      27578368
DATA       DATA_0017  CACHED  NORMAL    1440   1326  1.132886   2.541013   25899008      26537984
DATA       DATA_0013  CACHED  NORMAL     714   1391  1.527926    .371432   18169856      22814720
DATA       DATA_0001  CACHED  NORMAL     713    807   .790505    .219565   20406272      28561408
DATA       DATA_0012  CACHED  NORMAL     617   1206  1.016893    3.60425   24477696      25391104
DATA       DATA_0003  CACHED  NORMAL   15567  11500  5.642053   3.328861  266956800     183625728
DATA       DATA_0015  CACHED  NORMAL     642   1357  2.545441    .403455   22179840      24973312
DATA       DATA_0011  CACHED  NORMAL    7585   1685  1.121678    .359123  135217152      37572608
DATA       DATA_0005  CACHED  NORMAL     513   1431  1.007476     .47202   26427392      21344256
DATA       DATA_0002  CACHED  NORMAL   11368   2196  1.209433    .861601  199213056      32090624
```

Example 6-5 Viewing disk group clients with V$ASM\_CLIENT

This is an example of the use of the `V$ASM_CLIENT` and `V$ASM_DISKGROUP` views on an Oracle ASM instance. The example displays disk groups with information about the connected database client instances.

```
SELECT dg.name AS diskgroup, SUBSTR(c.instance_name,1,12) AS instance,
    SUBSTR(c.db_name,1,12) AS dbname, SUBSTR(c.SOFTWARE_VERSION,1,12) AS software,
    SUBSTR(c.COMPATIBLE_VERSION,1,12) AS compatible 
    FROM V$ASM_DISKGROUP dg, V$ASM_CLIENT c  
    WHERE dg.group_number = c.group_number;
 
DISKGROUP                      INSTANCE     DBNAME   SOFTWARE     COMPATIBLE
------------------------------ ------------ -------- ------------ ------------
DATA                           +ASM         +ASM     19.0.0.0.0   19.0.0.0.0
DATA                           orcl         orcl     19.0.0.0.0   19.0.0.0.0
DATA                           +ASM         asmvol   19.0.0.0.0   19.0.0.0.0
FRA                            orcl         orcl     19.0.0.0.0   19.0.0.0.0
...
```

### Viewing Oracle ASM File Access Control Information

You can view information about Oracle ASM File Access Control in the columns of the `V$ASM_USER`, `V$ASM_USERGROUP`, `V$ASM_USERGROUP_MEMBER`, and `V$ASM_FILE` views.

For more information about Oracle ASM File Access Control, see [Managing Oracle ASM File Access Control for Disk Groups](asm-access-control-diskgroups.md).

Example 6-6 Viewing Oracle ASM File Access Control information with V$ASM\_USER

This example shows information about Oracle ASM File Access Control users displayed in the `V$ASM_USER` view.

```
SELECT dg.name AS diskgroup, u.group_number, u.user_number, u.os_id, u.os_name 
     FROM V$ASM_DISKGROUP dg, V$ASM_USER u 
     WHERE dg.group_number = u.group_number AND dg.name = 'DATA';

DISKGROUP       GROUP_NUMBER USER_NUMBER OS_ID OS_NAME
--------------- ------------ ----------- ----- -------
DATA                       1           1 1001  oracle1
DATA                       1           2 1002  oracle2
DATA                       1           3 1003  grid
```

Example 6-7 Viewing File Access Control information with V$ASM\_USERGROUP

This example shows information about Oracle ASM File Access Control user groups displayed in the `V$ASM_USERGROUP` view.

```
SELECT dg.name AS diskgroup, ug.group_number, ug.owner_number, u.os_name,
     ug.usergroup_number, ug.name FROM V$ASM_DISKGROUP dg, V$ASM_USER u, V$ASM_USERGROUP ug 
     WHERE dg.group_number = ug.group_number AND dg.name = 'DATA' 
     AND ug.owner_number = u.user_number;

DISKGROUP         GROUP_NUMBER OWNER_NUMBER OS_NAME         USERGROUP_NUMBER NAME
----------------- ------------ ------------ --------------- ---------------- --------
DATA                         1            3 grid                           1 asm_data
```

Example 6-8 Viewing File Access Control information with V$ASM\_USERGROUP\_MEMBER

This example shows information about Oracle ASM File Access Control user groups and members displayed in the `V$ASM_USERGROUP_MEMBER` view.

```
SELECT dg.name AS diskgroup, um.group_number, um.member_number, u.os_name, 
     um.usergroup_number, ug.name FROM V$ASM_DISKGROUP dg, V$ASM_USER u, V$ASM_USERGROUP_MEMBER um, 
     V$ASM_USERGROUP ug WHERE dg.group_number = um.group_number AND 
     dg.group_number = ug.group_number AND dg.group_number = u.group_number AND dg.name = 'DATA' 
     AND um.member_number = u.user_number AND um.usergroup_number = ug.usergroup_number;

DISKGROUP       GROUP_NUMBER MEMBER_NUMBER OS_NAME            USERGROUP_NUMBER NAME
--------------- ------------ ------------- ------------------ ---------------- --------
DATA                       1             1 oracle1                           1 asm_data
DATA                       1             2 oracle2                           1 asm_data
```

Example 6-9 Viewing Oracle ASM File Access Control information with V$ASM\_FILE

This example shows information about Oracle ASM File Access Control file permissions displayed in the `V$ASM_FILE` view.

```
SELECT dg.name AS diskgroup, a.name, f.permissions, f.user_number, u.os_name,
       f.usergroup_number, ug.name 
     FROM V$ASM_DISKGROUP dg, V$ASM_USER u, V$ASM_USERGROUP ug, V$ASM_FILE f, V$ASM_ALIAS a 
     WHERE dg.name = 'FRA' AND dg.group_number = u.group_number AND 
       u.group_number = ug.group_number AND ug.group_number = f.group_number AND 
       f.group_number = a.group_number AND 
       f.usergroup_number = ug.usergroup_number AND f.user_number = u.user_number AND 
       f.file_number = a.file_number;

DISKGROUP NAME                   PERMISSIONS USER_NUMBER OS_NAME USERGROUP_NUMBER NAME
--------- ---------------------- ----------- ----------- ------- ---------------- -------
DATA      USERS.259.685366091    rw-r-----             3 grid                   1 asm_fra 
DATA      TEMP.264.685366227     rw-r-----             3 grid                   1 asm_fra 
...
```