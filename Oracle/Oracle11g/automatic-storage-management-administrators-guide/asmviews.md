---
title: Using Views to Display Information
book: "Automatic Storage Management Administrator's Guide"
doc_id: E18951-03
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e18951/asmviews.htm
tags:
  - oracle
  - 11g
  - automatic-storage-management-administrators-guide
---

## 6 Using Views to Display Information

This chapter contains information about using dynamic views to display Oracle Automatic Storage Management (Oracle ASM), Oracle Automatic Storage Management Cluster File System (Oracle ACFS), and Oracle ASM Dynamic Volume Manager (Oracle ADVM) information.

See Also:

[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_part.htm#REFRN003) for information about all of the `V$ASM*` dynamic performance views

## Views Containing Oracle ASM Disk Group Information

You can use the views in Table 6-1 to obtain information about Oracle ASM disk groups.

The `V$ASM_ALIAS`, `V$ASM_CLIENT`, `V$ASM_DISK`, `V$ASM_DISK_IOSTAT`, `V$ASM_DISK_STAT`, `V$ASM_DISKGROUP`, `V$ASM_DISKGROUP_STAT`, `V$ASM_FILE`, `V$ASM_TEMPLATE`, `V$ASM_USER`, `V$ASM_USERGROUP`, and `V$ASM_USERGROUP_MEMBER` are accessible from both the Oracle ASM and database instances.

Table 6-1 Oracle ASM dynamic views for disk group information

| View | Description |
| --- | --- |
| `V$ASM_ALIAS` | Contains one row for every alias present in every disk group mounted by the Oracle ASM instance. |
| `V$ASM_ATTRIBUTE` | Displays one row for each attribute defined. In addition to attributes specified by `CREATE` `DISKGROUP` and `ALTER` `DISKGROUP` statements, the view may show other attributes that are created automatically. Attributes are only displayed for disk groups where `COMPATIBLE.ASM` is set to 11.1 or higher. |
| `V$ASM_CLIENT` | In an Oracle ASM instance, identifies databases using disk groups managed by the Oracle ASM instance.  In an Oracle Database instance, contains information about the Oracle ASM instance if the database has any open Oracle ASM files. |
| `V$ASM_DISK` | Contains one row for every disk discovered by the Oracle ASM instance, including disks that are not part of any disk group.  This view performs disk discovery every time it is queried. |
| `V$ASM_DISK_IOSTAT` | Displays information about disk I/O statistics for each Oracle ASM client.  In an Oracle Database instance, only the rows for that instance are shown. |
| `V$ASM_DISK_STAT` | Contains the same columns as `V$ASM_DISK`, but to reduce overhead, does not perform a discovery when it is queried. It only returns information about any disks that are part of mounted disk groups in the storage system. To see all disks, use `V$ASM_DISK` instead. |
| `V$ASM_DISKGROUP` | Describes a disk group (number, name, size related info, state, and redundancy type).  This view performs disk discovery every time it is queried. |
| `V$ASM_DISKGROUP_STAT` | Contains the same columns as `V$ASM_DISKGROUP`, but to reduce overhead, does not perform a discovery when it is queried. It does not return information about any disks that are part of mounted disk groups in the storage system. To see all disks, use `V$ASM_DISKGROUP` instead. |
| `V$ASM_FILE` | Contains one row for every Oracle ASM file in every disk group mounted by the Oracle ASM instance. |
| `V$ASM_OPERATION` | In an Oracle ASM instance, contains one row for every active Oracle ASM long running operation executing in the Oracle ASM instance.  In an Oracle Database instance, contains no rows. |
| `V$ASM_TEMPLATE` | Contains one row for every template present in every disk group mounted by the Oracle ASM instance. |
| `V$ASM_USER` | Contains the effective operating system user names of connected database instances and names of file owners. |
| `V$ASM_USERGROUP` | Contains the creator for each Oracle ASM File Access Control group. |
| `V$ASM_USERGROUP_MEMBER` | Contains the members for each Oracle ASM File Access Control group. |

When querying V$ASM views, note that the value of the disk group number is not a static value. When a disk group is mounted, a disk group number is chosen. This number may change across disk group mounts. A disk group number is not recorded in any persistent structure, but the current value can be viewed in the `GROUP_NUMBER` column of the V$ASM views.

An example of the use of the `V$ASM_ATTRIBUTE` and `V$ASM_DISKGROUP` views is shown in Example 6-1. The `COMPATIBLE.ASM` value must be set to 11.1 or higher for the disk group to display in the `V$ASM_ATTRIBUTE` view output. Attributes that are designated as read-only (`Y`) can only be set during disk group creation.

Example 6-1 Viewing disk group attributes with V$ASM\_ATTRIBUTE

```
SQL> SELECT dg.name AS diskgroup, SUBSTR(a.name,1,18) AS name,
     SUBSTR(a.value,1,24) AS value, read_only FROM V$ASM_DISKGROUP dg, 
     V$ASM_ATTRIBUTE a WHERE dg.name = 'DATA'
     AND dg.group_number = a.group_number;

DISKGROUP                NAME                     VALUE                 READ_ONLY
------------------------ ------------------------ --------------------- ---------
DATA                     disk_repair_time         3.6h                  N
DATA                     au_size                  4194304               Y
DATA                     sector_size              512                   Y
DATA                     compatible.asm           11.2.0.0.0            N
DATA                     compatible.rdbms         11.2.0.0.0            N
DATA                     compatible.advm          11.2.0.0.0            N
DATA                     cell.smart_scan_capable  FALSE                 N
DATA                     access_control.enabled   TRUE                  N
DATA                     access_control.umask     002                   N
...
```

You can view the compatibility for a disk group with the `V$ASM_DISKGROUP` view, as shown in Example 6-2.

Example 6-2 Viewing the compatibility of a disk group with V$ASM\_DISKGROUP

```
SQL> SELECT name AS diskgroup, compatibility AS asm_compat, 
     database_compatibility AS db_compat FROM V$ASM_DISKGROUP;

DISKGROUP         ASM_COMPAT   DB_COMPAT
----------------- ------------ ----------
DATA              11.2.0.0.0   11.2.0.0.0
FRA               10.1.0.0.0   10.1.0.0.0
```

An example of the use of the `V$ASM_DISK` and `V$ASM_DISKGROUP` views is shown in Example 6-3. This example displays the disks associated with a disk group, plus the mount status and state of the disks.

Example 6-3 Viewing disks in disk groups with V$ASM\_DISK

```
SQL> SELECT SUBSTR(d.name,1,16) AS asmdisk, d.mount_status, d.state, 
     dg.name AS diskgroup FROM V$ASM_DISKGROUP dg, V$ASM_DISK d 
     WHERE dg.group_number = d.group_number;

ASMDISK          MOUNT_S STATE    DISKGROUP
---------------- ------- -------- -------------
DATA_0001        CACHED  NORMAL   DATA
DATA_0007        CACHED  NORMAL   DATA
DATA_0000        CACHED  NORMAL   DATA
DATA_0008        CACHED  NORMAL   DATA
DATA_0005        CACHED  NORMAL   DATA
DATA_0002        CACHED  NORMAL   DATA
DATA_0004        CACHED  NORMAL   DATA
DATA_0006        CACHED  NORMAL   DATA
DATA_0003        CACHED  NORMAL   DATA
FRA_0005         CACHED  NORMAL   FRA
FRA_0004         CACHED  NORMAL   FRA
FRA_0000         CACHED  NORMAL   FRA
FRA_0009         CACHED  NORMAL   FRA
FRA_0011         CACHED  NORMAL   FRA
...
```

An example of the use of the `V$ASM_CLIENT` and `V$ASM_DISKGROUP` views on an Oracle ASM instance is shown in Example 6-4. This example displays disk groups with information about the connected database client instances.

Example 6-4 Viewing disk group clients with V$ASM\_CLIENT

```
SQL> SELECT dg.name AS diskgroup, SUBSTR(c.instance_name,1,12) AS instance,
    SUBSTR(c.db_name,1,12) AS dbname, SUBSTR(c.SOFTWARE_VERSION,1,12) AS software,
    SUBSTR(c.COMPATIBLE_VERSION,1,12) AS compatible 
    FROM V$ASM_DISKGROUP dg, V$ASM_CLIENT c  
    WHERE dg.group_number = c.group_number;
 
DISKGROUP                      INSTANCE     DBNAME   SOFTWARE     COMPATIBLE
------------------------------ ------------ -------- ------------ ------------
DATA                           +ASM         +ASM     11.2.0.0.0   11.2.0.0.0
DATA                           orcl         orcl     11.2.0.0.0   11.2.0.0.0
DATA                           +ASM         asmvol   11.2.0.0.0   11.2.0.0.0
FRA                            orcl         orcl     11.2.0.0.0   11.2.0.0.0
...
```

### Viewing Oracle ASM File Access Control Information

You can view information about Oracle ASM File Access Control in the columns of the `V$ASM_USER`, `V$ASM_USERGROUP`, `V$ASM_USERGROUP_MEMBER`, and `V$ASM_FILE` views.

Example 6-5 shows information about Oracle ASM File Access Control users displayed in the `V$ASM_USER` view.

Example 6-5 Viewing Oracle ASM File Access Control information with V$ASM\_USER

```
SQL> SELECT dg.name AS diskgroup, u.group_number, u.user_number, u.os_id, u.os_name 
     FROM V$ASM_DISKGROUP dg, V$ASM_USER u 
     WHERE dg.group_number = u.group_number AND dg.name = 'DATA';

DISKGROUP       GROUP_NUMBER USER_NUMBER OS_ID OS_NAME
--------------- ------------ ----------- ----- -------
DATA                       1           1 1001  oracle1
DATA                       1           2 1002  oracle2
DATA                       1           3 1003  grid
```

Example 6-6 shows information about Oracle ASM File Access Control user groups displayed in the `V$ASM_USERGROUP` view.

Example 6-6 Viewing Oracle ASM File Access Control information with V$ASM\_USERGROUP

```
SQL>  SELECT dg.name AS diskgroup, ug.group_number, ug.owner_number, u.os_name,
      ug.usergroup_number, ug.name FROM V$ASM_DISKGROUP dg, V$ASM_USER u, V$ASM_USERGROUP ug 
      WHERE dg.group_number = ug.group_number AND dg.name = 'DATA' 
      AND ug.owner_number = u.user_number;

DISKGROUP         GROUP_NUMBER OWNER_NUMBER OS_NAME         USERGROUP_NUMBER NAME
----------------- ------------ ------------ --------------- ---------------- ------------------
DATA                         1            3 grid                           1 asm_data
```

Example 6-7 shows information about Oracle ASM File Access Control user groups and members displayed in the `V$ASM_USERGROUP_MEMBER` view.

Example 6-7 Viewing Oracle ASM File Access Control information with V$ASM\_USERGROUP\_MEMBER

```
SQL> SELECT dg.name AS diskgroup, um.group_number, um.member_number, u.os_name, 
     um.usergroup_number, ug.name FROM V$ASM_DISKGROUP dg, V$ASM_USER u, V$ASM_USERGROUP_MEMBER um, 
     V$ASM_USERGROUP ug WHERE dg.group_number = um.group_number AND 
     dg.group_number = ug.group_number AND dg.group_number = u.group_number AND dg.name = 'DATA' 
     AND um.member_number = u.user_number AND um.usergroup_number = ug.usergroup_number;

DISKGROUP       GROUP_NUMBER MEMBER_NUMBER OS_NAME            USERGROUP_NUMBER NAME
--------------- ------------ ------------- ------------------ ---------------- ------------------
DATA                       1             1 oracle1                           1 asm_data
DATA                       1             2 oracle2                           1 asm_data
```

Example 6-8 shows information about Oracle ASM File Access Control file permissions displayed in the `V$ASM_FILE` view.

Example 6-8 Viewing Oracle ASM File Access Control information with V$ASM\_FILE

```
SQL> SELECT dg.name AS diskgroup, a.name, f.permissions, f.user_number, u.os_name,
     f.usergroup_number, ug.NAME FROM V$ASM_DISKGROUP dg, V$ASM_USER u, V$ASM_USERGROUP ug, 
     V$ASM_FILE f, V$ASM_ALIAS a WHERE dg.group_number = f.group_number AND 
     dg.group_number = u.group_number AND dg.group_number = ug.group_number AND 
     dg.name = 'FRA' AND f.usergroup_number = ug.usergroup_number AND f.user_number = u.user_number
     AND f.file_number = a.file_number;

DISKGROUP NAME                   PERMISSIONS USER_NUMBER OS_NAME USERGROUP_NUMBER NAME
--------- ---------------------- ----------- ----------- ------- ---------------- -------------
DATA      USERS.259.685366091    rw-r-----             3 grid                   1 asm_fra 
DATA      TEMP.264.685366227     rw-r-----             3 grid                   1 asm_fra 
...
```

For more information about Oracle ASM File Access Control, see ["Managing Oracle ASM File Access Control for Disk Groups"](asmdiskgrps.md).

### Viewing Disk Region Information

Information about Intelligent Data Placement is displayed in the columns of the `V$ASM_DISK`, `V$ASM_DISK_IOSTAT`, `V$ASM_FILE`, and `V$ASM_TEMPLATE` views.

Example 6-9 shows queries for Intelligent Data Placement information in the `PRIMARY_REGION` and `MIRROR_REGION` columns of the `V$ASM_FILE` view.

Example 6-9 Viewing Intelligent Data Placement information with V$ASM\_FILE

```
SQL> SELECT dg.name AS diskgroup, f.file_number, f.primary_region, f.mirror_region, f.hot_reads,
       f.hot_writes,  f.cold_reads, f.cold_writes
       FROM V$ASM_DISKGROUP dg, V$ASM_FILE f 
       WHERE dg.group_number = f.group_number and dg.name = 'DATA';
 
DISKGROUP                      FILE_NUMBER PRIM MIRR  HOT_READS HOT_WRITES COLD_READS COLD_WRITES
------------------------------ ----------- ---- ---- ---------- ---------- ---------- -----------
DATA                                   257 COLD COLD          0          0     119770      886575
DATA                                   258 COLD COLD          0          0       1396      222282
DATA                                   259 COLD COLD          0          0       2056         199
DATA                                   260 COLD COLD          0          0      42377     1331016
DATA                                   261 COLD COLD          0          0    4336300     1331027
...
```

Example 6-10 displays Intelligent Data Placement information in the `PRIMARY_REGION` and `MIRROR_REGION` columns of the `V$ASM_TEMPLATE` view.

Example 6-10 Viewing Intelligent Data Placement information with V$ASM\_TEMPLATE

```
SQL> SELECT dg.name AS diskgroup, t.name, t.stripe, t.redundancy, t.primary_region, t.mirror_region 
       FROM V$ASM_DISKGROUP dg, V$ASM_TEMPLATE t 
       WHERE dg.group_number = t.group_number and dg.name = 'DATA' ORDER BY t.name;

DISKGROUP                      NAME                           STRIPE REDUND PRIM MIRR
------------------------------ ------------------------------ ------ ------ ---- ----
DATA                           ARCHIVELOG                     COARSE MIRROR COLD COLD
DATA                           ASMPARAMETERFILE               COARSE MIRROR COLD COLD
DATA                           AUTOBACKUP                     COARSE MIRROR COLD COLD
DATA                           BACKUPSET                      COARSE MIRROR COLD COLD
DATA                           CHANGETRACKING                 COARSE MIRROR COLD COLD
DATA                           CONTROLFILE                    FINE   HIGH   COLD COLD
DATA                           DATAFILE                       COARSE MIRROR COLD COLD
DATA                           DATAGUARDCONFIG                COARSE MIRROR COLD COLD
DATA                           DUMPSET                        COARSE MIRROR COLD COLD
DATA                           FLASHBACK                      COARSE MIRROR COLD COLD
DATA                           FLASHFILE                      COARSE MIRROR COLD COLD
DATA                           OCRFILE                        COARSE MIRROR COLD COLD
DATA                           ONLINELOG                      COARSE MIRROR COLD COLD
DATA                           PARAMETERFILE                  COARSE MIRROR COLD COLD
DATA                           TEMPFILE                       COARSE MIRROR COLD COLD
DATA                           XTRANSPORT                     COARSE MIRROR COLD COLD
15 rows selected.
```

For information about setting Intelligent Data Placement, see ["Intelligent Data Placement"](asmdiskgrps.md).

## Views Containing Oracle ACFS Information

You can use the views in Table 6-2 to obtain information about Oracle Automatic Storage Management Cluster File System (Oracle ACFS). These views are accessible from the Oracle ASM instance.

Table 6-2 Oracle ASM dynamic views for Oracle ACFS information

| View | Description |
| --- | --- |
| `V$ASM_ACFS_ENCRYPTION_INFO` | Contains encryption information for each Oracle ACFS file system. |
| `V$ASM_ACFS_SECURITY_INFO` | Contains security realm information for each Oracle ACFS file system. |
| `V$ASM_ACFSSNAPSHOTS` | Contains snapshot information for every mounted Oracle ACFS file system. |
| `V$ASM_ACFSVOLUMES` | Contains information about mounted Oracle ACFS volumes, correlated with `V$ASM_FILESYSTEM`. |
| `V$ASM_FILESYSTEM` | Contains columns that display information for every mounted Oracle ACFS file system. |
| `V$ASM_VOLUME` | Contains information about each Oracle ADVM volume that is a member of an Oracle ASM instance. |
| `V$ASM_VOLUME_STAT` | Contains information about statistics for each Oracle ADVM volume. |

Example 6-11 shows information displayed from the `V$ASM_ACFS_ENCRYPTION_INFO` view. The `FS_NAME` column contains the mount point. The `VOL_DEVICE` contains the name of the Oracle ADVM device.

Example 6-11 Viewing encryption information in V$ASM\_ACFS\_ENCRYPTION\_INFO

```
SELECT SUBSTR(fs_name,1,32) FILESYSTEM, SUBSTR(vol_device,1,20) DEVICE, set_status, enabled_status, 
     algorithm, key_length, last_rekey_time FROM V$ASM_ACFS_ENCRYPTION_INFO;

FILESYSTEM                        DEVICE                 SET_STA ENABLED_ ALGORIT KEY_LEN LAST_REKE
--------------------------------- ---------------------- ------- -------- ------- ------- ---------
/u01/app/acfsmounts/acfs1         /dev/asm/volume1-228   YES     ENABLED  AES     192
```

See Also:

[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1017.htm#REFRN30636) for information about the `V$ASM_ACFS_ENCRYPTION_INFO` view

Example 6-12 shows information displayed from the `V$ASM_ACFS_SECURITY_INFO` view. The `FS_NAME` column contains the mount point. The `VOL_DEVICE` contains the name of the Oracle ADVM device.

Example 6-12 Viewing security information in V$ASM\_ACFS\_SECURITY\_INFO

```
SELECT SUBSTR(fs_name,1,32) FILESYSTEM, SUBSTR(vol_device,1,20) DEVICE, prepared_status, 
     enabled_status FROM V$ASM_ACFS_SECURITY_INFO;

FILESYSTEM                        DEVICE                 PREPARE ENABLED_
--------------------------------- ---------------------- ------- --------
/u01/app/acfsmounts/acfs1        /dev/asm/volume1-228    YES     ENABLED
```

See Also:

[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1018.htm#REFRN30637) for information about the `V$ASM_ACFS_SECURITY_INFO` view

Example 6-13 shows information displayed from the `V$ASM_ACFSSNAPSHOTS` view. The `FS_NAME` column contains the mount point. The `VOL_DEVICE` contains the name of the Oracle ADVM device.

Example 6-13 Viewing snapshot information in V$ASM\_ACFSSNAPSHOTS

```
SELECT SUBSTR(fs_name,1,32) FILESYSTEM, SUBSTR(vol_device,1,24) DEVICE, 
  SUBSTR(snap_name,1,28) SNAPSHOT, create_time TIME FROM V$ASM_ACFSSNAPSHOTS;

FILESYSTEM                       DEVICE                   SNAPSHOT                     TIME
-------------------------------- ------------------------ ---------------------------- ---------
/u01/app/acfsmounts/acfs1        /dev/asm/volume1-228     mysnapshot_0900609a          09-JUL-09
/u01/app/acfsmounts/acfs1        /dev/asm/volume1-228     mysnapshot_0900610a          10-JUL-09
/u01/app/acfsmounts/acfs1        /dev/asm/volume1-228     mysnapshot_0900609c          09-JUL-09
/u01/app/acfsmounts/acfs1        /dev/asm/volume1-228     mysnapshot_0900610b          10-JUL-09
```

See Also:

[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1019.htm#REFRN30617) for information about the `V$ASM_ACFSSNAPSHOTS` view

Example 6-14 shows information displayed from the `V$ASM_VACFSOLUMES` view. The `PRIMARY_VOL` column contains `TRUE` if the volume is the primary volume for the file system.

Example 6-14 Viewing volume information with V$ASM\_ACFSVOLUMES

```
SELECT fs_name, vol_device, primary_vol, total_mb, free_mb FROM V$ASM_ACFSVOLUMES;

FS_NAME                    VOL_DEVICE             PRIMARY_VOL   TOTAL_MB  FREE_MB
-------------------------- ---------------------- -----------   --------- ----------
/u01/app/acfsmounts/acfs1  /dev/asm/volume1-228   TRUE            1024000 578626.522
/u01/app/acfsmounts/acfs2  /dev/asm/volume2-375   TRUE            1024000 685761.463
...
```

See Also:

[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1019.htm#REFRN30617) for information about the `V$ASM_ACFSVOLUMES` view

Example 6-15 shows information displayed from the `V$ASM_FILESYSTEM` view.

The `STATE` column contains the status of the file system, either `AVAILABLE` or `OFFLINE`. An offline file system can only be dismounted; other attempts at access result in errors. Offline means that either the Oracle ASM instance is down, the disk group has been forced dismounted, or less commonly, a metadata I/O failure occurred or serious metadata corruption was detected. With a metadata I/O failure, the file system is also marked as corrupt.

The `CORRUPT` column indicates whether the file system needs the `fsck` or `acfschkdsk` command run on it. See ["fsck"](asmfs_util002.md) and ["acfschkdsk"](asmfs_util005.md).

Example 6-15 Viewing volume information with V$ASM\_FILESYSTEM

```
SQL> SELECT fs_name, available_time, block_size, state, corrupt FROM V$ASM_FILESYSTEM;

FS_NAME                            AVAILABLE BLOCK_SIZE STATE         CORRUPT
---------------------------------- --------- ---------- ------------- -------
/u01/app/acfsmounts/acfs1          19-JUL-09          4 AVAILABLE     FALSE
/u01/app/acfsmounts/acfs2          19-JUL-09          4 AVAILABLE     FALSE
```

See Also:

[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1030.htm#REFRN30619) for information about the `V$ASM_FILESYSTEM` view

Example 6-16 shows information displayed from the `V$ASM_VOLUME` view for volumes contained in the `DATA` disk group.

Example 6-16 Viewing volume information with V$ASM\_VOLUME

```
SELECT dg.name AS diskgroup, v.volume_name, v.volume_device, v.mountpath 
    FROM V$ASM_DISKGROUP dg, V$ASM_VOLUME v 
    WHERE dg.group_number = v.group_number and dg.name = 'DATA';

DISKGROUP        VOLUME_NAME       VOLUME_DEVICE           MOUNTPATH
---------------- ----------------- ----------------------- ---------------------------------
DATA             VOLUME1           /dev/asm/volume1-228    /u01/app/acfsmounts/acfs1
DATA             VOLUME2           /dev/asm/volume2-375    /u01/app/acfsmounts/acfs2
```

See Also:

[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1036.htm#REFRN30625) for information about the `V$ASM_VOLUME` view

Example 6-16 shows information displayed from the `V$ASM_VOLUME_STAT` view for volumes contained in the `DATA` disk group. The `BYTES_READ` column contains the total number of bytes read for the volume. The `BYTES_WRITTEN` column contains the total number of bytes written for the volume.

Example 6-17 Viewing volume information with V$ASM\_VOLUME\_STAT

```
SELECT dg.name AS diskgroup, v.volume_name, v.bytes_read, v.bytes_written
    FROM V$ASM_DISKGROUP dg, V$ASM_VOLUME_STAT v 
    WHERE dg.group_number = v.group_number and dg.name = 'DATA';

DISKGROUP                      VOLUME_NAME                    BYTES_READ  BYTES_WRITTEN
------------------------------ ------------------------------ ----------- -------------
DATA                           VOLUME1                        12370105856      43510272
DATA                           VOLUME2                            2685728      32201504
```

See Also:

[Oracle Database Reference](https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_1037.htm#REFRN30626) for information about the `V$ASM_VOLUME_STAT` view