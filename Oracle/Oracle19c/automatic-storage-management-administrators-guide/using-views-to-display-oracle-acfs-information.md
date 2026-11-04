---
title: "Oracle Automatic Storage Management Administrator's Guide"
book: "Oracle Automatic Storage Management Administrator's Guide"
doc_id: F34287-08
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/part-iii-oracle-automatic-storage-management-cluster-file-system/using-views-to-display-oracle-acfs-information.html
tags:
  - oracle
  - 19c
  - automatic-storage-management-administrators-guide
---

## Using Views to Display Oracle ACFS Information

Dynamic views display important information about Oracle Automatic Storage Management Cluster File System (Oracle ACFS) and Oracle ASM Dynamic Volume Manager (Oracle ADVM).

This chapter contains information about using dynamic views to display Oracle Automatic Storage Management Cluster File System (Oracle ACFS) and Oracle ASM Dynamic Volume Manager (Oracle ADVM) information.

- Views Containing Oracle ACFS Information
- Oracle ACFS Support for Oracle Database File Mapping Views

See also

- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19&id=REFRN-GUID-8C5690B0-DE10-4460-86DF-80111869CF4C) for information about all of the `V$ASM_ACFS*` dynamic performance views
- [Oracle ACFS Command-Line Utilities](managing-oracle-acfs-with-command-line-tools.md) for `acfsutil` `info` commands that display Oracle ACFS information

## Views Containing Oracle ACFS Information

You can use the views in the following table to obtain information about Oracle Automatic Storage Management Cluster File System (Oracle ACFS). These views are accessible from the Oracle ASM instance.

Note:

- To display information about Oracle ACFS file systems or volumes that are located on nodes in an Oracle Flex ASM configuration, you must connect to the Oracle ASM proxy instance instead of the local Oracle ASM instance.
- When viewing space usage values in Oracle ACFS views on Windows systems, the values may differ from sizes in Windows folders. The mechanism used by **Folder** **Properties** on Windows systems only accounts for files and should be considered an approximate value.

Table: Oracle ASM dynamic views for Oracle ACFS information

| View | Description |
| --- | --- |
| `V$ASM_ACFS_ENCRYPTION_INFO` | Contains encryption information for each Oracle ACFS file system. |
| `V$ASM_ACFS_SECURITY_INFO` | Contains security realm information for each Oracle ACFS file system. |
| `V$ASM_ACFS_SEC_ADMIN` | Contains information about Oracle ACFS security administrator in the cluster. |
| `V$ASM_ACFS_SEC_CMDRULE` | Contains information about Oracle ACFS security command rules for each Oracle ACFS file system. |
| `V$ASM_ACFS_SEC_REALM` | Contains information about every realm in the Oracle ACFS security realm for each Oracle ACFS file system. |
| `V$ASM_ACFS_SEC_REALM_FILTER` | Contains information about every filter in the Oracle ACFS security realm for each Oracle ACFS file system. A filter is a defined as `commandrule` / `ruleset` pair in a realm. |
| `V$ASM_ACFS_SEC_REALM_GROUP` | Contains information about every group in the Oracle ACFS security realm for each Oracle ACFS file system. |
| `V$ASM_ACFS_SEC_REALM_USER` | Contains information about every user in the Oracle ACFS security realm for each Oracle ACFS file system. |
| `V$ASM_ACFS_SEC_RULE` | Contains information about every Oracle ACFS security rule for each Oracle ACFS file system. |
| `V$ASM_ACFS_SEC_RULESET` | Contains information about every Oracle ACFS security ruleset for each Oracle ACFS file system. |
| `V$ASM_ACFS_SEC_RULESET_RULE` | Contains information about every rule in Oracle ACFS security ruleset for each Oracle ACFS file system. |
| `V$ASM_ACFSREPL` | Contains information for Oracle ACFS file systems that are initialized for replication.  This view only contains records for Oracle ASM releases prior to 12.2. To display Oracle ACFS replication information for Oracle ASM releases 12.2 or higher, use the `acfsutil repl info` command. |
| `V$ASM_ACFSREPLTAG` | Contains replicated tag information for Oracle ACFS file systems that are initialized for replication.  This view only contains records for Oracle ASM releases prior to 12.2. To display Oracle ACFS replication information for Oracle ASM releases 12.2 or higher, use the `acfsutil repl info` command. |
| `V$ASM_ACFSSNAPSHOTS` | Contains snapshot information about every mounted Oracle ACFS file system. |
| `V$ASM_ACFSTAG` | Contains all tag name information about files on all mounted Oracle ACFS file systems |
| `V$ASM_ACFSVOLUMES` | Contains information about mounted Oracle ADVM volumes, correlated with `V$ASM_FILESYSTEM`. |
| `V$ASM_FILESYSTEM` | Contains information about every mounted Oracle ACFS file system. |
| `V$ASM_VOLUME` | Contains information about each Oracle ADVM volume that is a member of an Oracle ASM instance. |
| `V$ASM_VOLUME_STAT` | Contains information about statistics for each Oracle ADVM volume. |

Example: Viewing encryption information in V$ASM\_ACFS\_ENCRYPTION\_INFO

This example shows information displayed from the `V$ASM_ACFS_ENCRYPTION_INFO` view. The `FS_NAME` column contains the mount point. The `VOL_DEVICE` contains the name of the Oracle ADVM device.

```
SELECT SUBSTR(fs_name,1,24) FILESYSTEM, SUBSTR(vol_device,1,20) DEVICE, set_status,
   enabled_status, algorithm, key_length, last_rekey_time FROM V$ASM_ACFS_ENCRYPTION_INFO;

FILESYSTEM               DEVICE                 SET_STA ENABLED_ ALGORIT KEY_LEN LAST_REKE
------------ ----------- ---------------------- ------- -------- ------- ------- ---------
/acfsmounts/acfs1        /dev/asm/volume1-228   YES     ENABLED  AES     192
```

Example: Viewing security information in V$ASM\_ACFS\_SECURITY\_INFO

This example shows information displayed from the `V$ASM_ACFS_SECURITY_INFO` view. The `FS_NAME` column contains the mount point. The `VOL_DEVICE` contains the name of the Oracle ADVM device.

```
SELECT SUBSTR(fs_name,1,24) FILESYSTEM, SUBSTR(vol_device,1,20) DEVICE, prepared_status,
     enabled_status FROM V$ASM_ACFS_SECURITY_INFO;

FILESYSTEM                DEVICE                 PREPARE ENABLED_
------------------------- ---------------------- ------- --------
/acfsmounts/acfs1        /dev/asm/volume1-228    YES     ENABLED
```

Example: Viewing security rules information in V$ASM\_ACFS\_SEC\_RULE

This example shows information displayed from the `V$ASM_ACFS_SEC_RULE` view. The `FS_NAME` column contains the mount point.

```
SELECT SUBSTR(rule_name,1,24) rule, SUBSTR(rule_type,1,12) type,
    SUBSTR(rule_value,1,16) value, SUBSTR(fs_name,1,24) filesystem
    FROM V$ASM_ACFS_SEC_RULE;

RULE                     TYPE         VALUE            FILESYSTEM
------------------------ ------------ ---------------- ------------------------
medHistRule1a            TIME         22:00:00         /acfsmounts/acfs1
medHistRule1c            TIME         08:00:00         /acfsmounts/acfs1
medHistRule1b            USERNAME     medMaintenance   /acfsmounts/acfs1
medHistRule1d            USERNAME     medBrowse        /acfsmounts/acfs1
SYSTEM_RULE_Auditor      GROUPNAME    myaudit_mgr_grp  /acfsmounts/acfs1
SYSTEM_RULE_AuditManager GROUPNAME    myauditor_grp    /acfsmounts/acfs1
SYSTEM_RULE_Always       TIME         00:00:00         /acfsmounts/acfs1
```

Example: Viewing security ruleset information in V$ASM\_ACFS\_SEC\_RULESET

This example shows information displayed from the `V$ASM_ACFS_SEC_RULESET` view. The `FS_NAME` column contains the mount point.

```
SELECT SUBSTR(ruleset_name,1,36) ruleset, ruleset_option r_option, SUBSTR(fs_name,1,24) filesystem
    FROM V$ASM_ACFS_SEC_RULESET;

RULESET                              R_OPTION FILESYSTEM
------------------------------------ -------- -----------------
medRuleSet1                          ALL_TRUE /acfsmounts/acfs1
medRuleSet2                          ALL_TRUE /acfsmounts/acfs1
SYSTEM_RULESET_Auditor               ALL_TRUE /acfsmounts/acfs1
SYSTEM_RULESET_AuditManager          ALL_TRUE /acfsmounts/acfs1
SYSTEM_RULESET_AuditMgr_Auditor      ANY_TRUE /acfsmounts/acfs1
SYSTEM_RULESET_AlwaysDeny            ANY_TRUE /acfsmounts/acfs1
```

Example: Viewing security ruleset information in V$ASM\_ACFS\_SEC\_RULESET\_RULE

This example shows information displayed from the `V$ASM_ACFS_SEC_RULESET_RULE` view.

```
SELECT SUBSTR(ruleset_name,1,36) ruleset, substr(rule_name,1,24) rule,
    SUBSTR(fs_name,1,36) filesystem FROM V$ASM_ACFS_SEC_RULESET_RULE;

RULESET                              RULE                     FILESYSTEM
------------------------------------ ------------------------ ------------------
medRuleSet1                          medHistRule1a            /acfsmounts/acfs1
medRuleSet1                          medHistRule1b            /acfsmounts/acfs1
medRuleSet2                          medHistRule1c            /acfsmounts/acfs1
medRuleSet2                          medHistRule1d            /acfsmounts/acfs1
SYSTEM_RULESET_Auditor               SYSTEM_RULE_Auditor      /acfsmounts/acfs1
SYSTEM_RULESET_AuditManager          SYSTEM_RULE_AuditManager /acfsmounts/acfs1
SYSTEM_RULESET_AuditMgr_Auditor      SYSTEM_RULE_Auditor      /acfsmounts/acfs1
SYSTEM_RULESET_AuditMgr_Auditor      SYSTEM_RULE_AuditManager /acfsmounts/acfs1
SYSTEM_RULESET_AlwaysDeny            SYSTEM_RULE_Always       /acfsmounts/acfs1
```

Example: Viewing snapshot information in V$ASM\_ACFSSNAPSHOTS

This examle shows information displayed from the `V$ASM_ACFSSNAPSHOTS` view. The `FS_NAME` column contains the mount point. The `VOL_DEVICE` contains the name of the Oracle ADVM device.

```
SELECT SUBSTR(FS_NAME,1,24) FILESYSTEM, SUBSTR(VOL_DEVICE,1,22) DEVICE,
  SUBSTR(SNAP_NAME,1,12) SNAPSHOT, CREATE_TIME TIME, SUBSTR(PARENT,1,10) PARENT,
  SUBSTR(TYPE,1,4) TYPE FROM V$ASM_ACFSSNAPSHOTS;

FILESYSTEM               DEVICE                 SNAPSHOT     TIME      PARENT     TY
------------------------ ---------------------- ------------ --------- ---------- --
/acfsmounts/acfs1        /dev/asm/volume1-229   snaprw       13-MAR-12 NULL       RW
/acfsmounts/acfs1        /dev/asm/volume1-229   snaprw_child 13-MAR-12 snaprw     RW
/acfsmounts/acfs2        /dev/asm/volume2-321   snapro       13-MAR-12 NULL       RO
```

Example: Viewing volume information with V$ASM\_ACFSVOLUMES

This example shows information displayed from the `V$ASM_ACFSVOLUMES` view. The `PRIMARY_VOL` column contains `TRUE` if the volume is the primary volume for the file system.

```
SELECT fs_name, vol_device, primary_vol, total_mb, free_mb FROM V$ASM_ACFSVOLUMES;

FS_NAME            VOL_DEVICE             PRIMARY_VOL   TOTAL_MB  FREE_MB
------------------ ---------------------- -----------   --------- ----------
/acfsmounts/acfs1  /dev/asm/volume1-228   TRUE            1024000 578626.522
/acfsmounts/acfs2  /dev/asm/volume2-375   TRUE            1024000 685761.463
...
```

Example: Viewing volume information with V$ASM\_FILESYSTEM

This example shows information displayed from the `V$ASM_FILESYSTEM` view.

The `STATE` column contains the status of the file system, either `AVAILABLE` or `OFFLINE`. An offline file system can only be dismounted; other attempts at access result in errors. Offline means that either the Oracle ASM instance is down, the disk group has been forced dismounted, or less commonly, a metadata I/O failure occurred or serious metadata corruption was detected. With a metadata I/O failure, the file system is also marked as corrupt.

The `CORRUPT` column indicates whether the file system needs the `fsck` or `acfschkdsk` command run on it.

```
SELECT fs_name, available_time, block_size, state, corrupt FROM V$ASM_FILESYSTEM;

FS_NAME                    AVAILABLE BLOCK_SIZE STATE         CORRUPT
-------------------------- --------- ---------- ------------- -------
/acfsmounts/acfs1          19-JUL-09          4 AVAILABLE     FALSE
/acfsmounts/acfs2          19-JUL-09          4 AVAILABLE     FALSE
```

Example: Viewing volume information with V$ASM\_VOLUME

This example shows information displayed from the `V$ASM_VOLUME` view for volumes contained in the `DATA` disk group.

```
SELECT dg.name AS diskgroup, v.volume_name, v.volume_device, v.mountpath
    FROM V$ASM_DISKGROUP dg, V$ASM_VOLUME v
    WHERE dg.group_number = v.group_number and dg.name = 'DATA';

DISKGROUP        VOLUME_NAME       VOLUME_DEVICE           MOUNTPATH
---------------- ----------------- ----------------------- ------------------
DATA             VOLUME1           /dev/asm/volume1-228    /acfsmounts/acfs1
DATA             VOLUME2           /dev/asm/volume2-375    /acfsmounts/acfs2
```

Example: Viewing volume information with V$ASM\_VOLUME\_STAT

This example shows information displayed from the `V$ASM_VOLUME_STAT` view for volumes contained in the `DATA` disk group. The `BYTES_READ` column contains the total number of bytes read for the volume. The `BYTES_WRITTEN` column contains the total number of bytes written for the volume.

```
SELECT dg.name AS diskgroup, v.volume_name, v.bytes_read, v.bytes_written
    FROM V$ASM_DISKGROUP dg, V$ASM_VOLUME_STAT v
    WHERE dg.group_number = v.group_number and dg.name = 'DATA';

DISKGROUP                      VOLUME_NAME                    BYTES_READ  BYTES_WRITTEN
------------------------------ ------------------------------ ----------- -------------
DATA                           VOLUME1                        12370105856      43510272
DATA                           VOLUME2                            2685728      32201504
```

Example: Viewing tag name information with V$ASM\_ACFSTAG

This example shows tag names for the `/acfsmounts/acfs1` file system displayed from the `V$ASM_ACFSTAG` view.

```
SELECT SUBSTR(TAG_NAME,1,8) TAG_NAME, SUBSTR(FS_NAME,1,20) FS_NAME,
     SUBSTR(PATH_NAME,1,42) PATH_NAME FROM V$ASM_ACFSTAG WHERE TAG_NAME='tag5';

TAG_NAME FS_NAME               PATH_NAME
-------- --------------------- --------------------------------------
tag5     /acfsmounts/acfs1     /acfsmounts/acfs1/d1/d2/d3/d4/d5/f6
tag5     /acfsmounts/acfs1     /acfsmounts/acfs1/d1/d2/d3/d4/d5
tag5     /acfsmounts/acfs1     /acfsmounts/acfs1/d1/d2/d3/d4
tag5     /acfsmounts/acfs1     /acfsmounts/acfs1/d1/d2/d3
tag5     /acfsmounts/acfs1     /acfsmounts/acfs1/d1/d2
tag5     /acfsmounts/acfs1     /acfsmounts/acfs1/d1
tag5     /acfsmounts/acfs1     /acfsmounts/acfs1/f1
tag5     /acfsmounts/acfs1     /acfsmounts/acfs1
```

See also

[Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19&id=REFRN-GUID-8C5690B0-DE10-4460-86DF-80111869CF4C) for information about the Oracle ACFS dynamic views

## Oracle ACFS Support for Oracle Database File Mapping Views

Oracle ACFS supports Oracle Database file mapping views to the Oracle ASM device level.

Note:

This feature is available starting with Oracle Database 12c Release 1 (12.1.0.2).

The following database mapping views are supported by Oracle ACFS:

- `V$MAP_FILE`
- `V$MAP_FILE_EXTENT`
- `V$MAP_ELEMENT`
- `V$MAP_FILE_IO_STACK`

These `V$MAP` views are only refreshed by executing the procedure `DBMS_STORAGE_MAP.MAP_ALL`. The Oracle ACFS file mapping interface does not utilize the external `fmputl` process or its supporting libraries.

Note:

- Oracle ACFS does not provide support for Oracle Database file mapping on Windows.
- Oracle ACFS does not provide support for the `V$MAP_SUBELEMENT` view.

Before running any queries on the `V$MAP` views, ensure that the `FILE_MAPPING` initialization is set to `TRUE`, then run the `DBMS_STORAGE_MAP.MAP_ALL` procedure to build the mapping information for the entire I/O subsystem associated with the database. For example, connect as `SYSDBA` to the database instance and run the following:

```
SQL> ALTER SYSTEM SET file_mapping=true;

SQL> EXEC DBMS_STORAGE_MAP.MAP_ALL(10000);
```

The SQL examples for `V$MAP_ELEMENT`, `V$MAP_FILE`, `V$MAP_FILE_EXTENT`, and `V$MAP_FILE_IO_STACK` are run from the Oracle Database instance.

Example: Viewing Oracle ASM information with V$MAP\_ELEMENT

This example displays information from the `V$MAP_ELEMENT` view.

```
SQL> SELECT ELEM_NAME, ELEM_IDX, ELEM_TYPE, ELEM_SIZE, ELEM_DESCR
       FROM V$MAP_ELEMENT;

ELEM_NAME      ELEM_IDX ELEM_TYPE   ELEM_SIZE ELEM_DESCR
------------ ---------- ---------- ---------- -----------------
+/dev/xvdd1           0 ASMDISK     117184512 TEST_0001
+/dev/xvdc1           1 ASMDISK     117184512 TEST_0000
```

Example: Viewing Oracle ACFS Data File Information with V$MAP\_FILE

This example displays information from the `V$MAP_FILE` view.

```
SQL> SELECT FILE_NAME, FILE_MAP_IDX, FILE_TYPE, FILE_STRUCTURE, FILE_SIZE,
      FILE_NEXTS FROM V$MAP_FILE WHERE REGEXP_LIKE(FILE_NAME, '*users01.dbf');

FILE_NAME                 FILE_MAP_IDX FILE_TYPE FILE_STRU FILE_SIZE FILE_NEXTS
------------------------- ------------ --------- --------- --------- ----------
/dbdata1/orcl/users01.dbf            4 DATAFILE  FILE          10256         41
```

Example: Viewing Element and File Offset Information with V$MAP\_FILE\_EXTENT

This example displays the element offset versus file offset information for each extent with `V$MAP_FILE_EXTENT`, specifying `FILE_MAP_IDX` equal to `4`, which is the file map index of the `/dbdata/orcl/users01.dbf` file.

```
SQL> SELECT FILE_MAP_IDX, EXT_NUM, EXT_ELEM_OFF, EXT_SIZE, EXT_FILE_OFF,
       EXT_TYPE, ELEM_IDX FROM V$MAP_FILE_EXTENT WHERE FILE_MAP_IDX=4;

FILE_MAP_IDX    EXT_NUM EXT_ELEM_OFF   EXT_SIZE EXT_FILE_OFF EXT_TY   ELEM_IDX
------------ ---------- ------------ ---------- ------------ ------ ----------
           4          0     58105664        192            0 DATA            0
           4          1     58154752        256          192 DATA            1
           4          2     58089472        256          448 DATA            0
...
           4         39     58140928        256         9920 DATA            1
           4         40     58108160         88        10176 DATA            0
41 rows selected.
```

Example: Viewing Extent Information With V$MAP\_FILE\_IO\_STACK

This example displays information from `V$MAP_FILE_IO_STACK` specifying `FILE_MAP_IDX` equal to `4`. The `V$MAP_FILE_IO_STACK` view is similar to `V$MAP_FILE_EXTENT`, but the display groups contiguous extents which are on the same device or element and of the same size.

```
SQL> SELECT FILE_MAP_IDX, ELEM_IDX, CU_SIZE,STRIDE, NUM_CU,ELEM_OFFSET,
       FILE_OFFSET FROM V$MAP_FILE_IO_STACK WHERE FILE_MAP_IDX=4;

FILE_MAP_IDX   ELEM_IDX    CU_SIZE     STRIDE     NUM_CU ELEM_OFFSET FILE_OFFSET
------------ ---------- ---------- ---------- ---------- ----------- -----------
           4          0        256       1024         10    58089472 448
           4          0        192          0          1    58105664 0
           4          0        256       1024          9    58105856 960
           4          0         88          0          1    58108160 10176
           4          1        256       1024         10    58138624 704
           4          1        256       1024         10    58154752 192

6 rows selected.
```

See also

- [Oracle Database File Mapping for Oracle ASM Files](administering-oracle-asm-files-directories-and-templates.md) for information about file mapping to Oracle ASM files
- [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19&id=ADMIN-GUID-3348410C-246D-4100-A41E-814E1BD9C541) for information about the Oracle Database File Mapping Interface
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19&id=REFRN-GUID-B200B2D6-08D4-49B0-9FD9-8AF6AED37202) for details about the `V$MAP` views