---
title: "Administrator's Guide"
book: "Advanced Cluster File System Administrator's Guide"
doc_id: F30297-04
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/acfsg/views-contain-acfs-info.html
tags:
  - oracle
  - 21c
  - advanced-cluster-file-system-administrators-guide
---

You can use the views in Table 2-1 to obtain information about Oracle Advanced Cluster File System (Oracle ACFS). These views are accessible from the Oracle ASM instance.

Note:

To display information about Oracle ACFS file systems or volumes that are located on nodes in an Oracle Flex ASM configuration, you must connect to the Oracle ASM proxy instance instead of the local Oracle ASM instance.

Table 2-1 Oracle ASM dynamic views for Oracle ACFS information

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
| `V$ASM_ACFSREPL` | Contains information for Oracle ACFS file systems that are initialized for replication.  For Oracle ASM releases 12.2 or higher, this view contains records just for storage locations that are file systems (and not for ones that are snapshots) |
| `V$ASM_ACFSREPLTAG` | Contains replicated tag information for Oracle ACFS file systems that are initialized for replication.  This view only contains records for Oracle ASM releases prior to 12.2. To display Oracle ACFS replication information for Oracle ASM releases 12.2 or higher, use the `acfsutil repl info` command. |
| `V$ASM_ACFSSNAPSHOTS` | Contains snapshot information about every mounted Oracle ACFS file system. |
| `V$ASM_ACFSTAG` | Contains all tag name information about files on all mounted Oracle ACFS file systems |
| `V$ASM_ACFSVOLUMES` | Contains information about mounted Oracle ADVM volumes, correlated with `V$ASM_FILESYSTEM`. |
| `V$ASM_FILESYSTEM` | Contains information about every mounted Oracle ACFS file system. |
| `V$ASM_VOLUME` | Contains information about each Oracle ADVM volume that is a member of an Oracle ASM instance. |
| `V$ASM_VOLUME_STAT` | Contains information about statistics for each Oracle ADVM volume. |

Example 2-1 Viewing encryption information in V$ASM\_ACFS\_ENCRYPTION\_INFO

This example shows information displayed from the `V$ASM_ACFS_ENCRYPTION_INFO` view. The `FS_NAME` column contains the mount point. The `VOL_DEVICE` contains the name of the Oracle ADVM device.

```
SELECT SUBSTR(fs_name,1,24) FILESYSTEM, SUBSTR(vol_device,1,20) DEVICE, set_status, 
   enabled_status, algorithm, key_length, last_rekey_time FROM V$ASM_ACFS_ENCRYPTION_INFO;

FILESYSTEM               DEVICE                 SET_STA ENABLED_ ALGORIT KEY_LEN LAST_REKE
------------ ----------- ---------------------- ------- -------- ------- ------- ---------
/acfsmounts/acfs1        /dev/asm/volume1-228   YES     ENABLED  AES     192
```

Example 2-2 Viewing security information in V$ASM\_ACFS\_SECURITY\_INFO

This example shows information displayed from the `V$ASM_ACFS_SECURITY_INFO` view. The `FS_NAME` column contains the mount point. The `VOL_DEVICE` contains the name of the Oracle ADVM device.

```
SELECT SUBSTR(fs_name,1,24) FILESYSTEM, SUBSTR(vol_device,1,20) DEVICE, prepared_status, 
     enabled_status FROM V$ASM_ACFS_SECURITY_INFO;

FILESYSTEM                DEVICE                 PREPARE ENABLED_
------------------------- ---------------------- ------- --------
/acfsmounts/acfs1        /dev/asm/volume1-228    YES     ENABLED
```

Example 2-3 Viewing security rules information in V$ASM\_ACFS\_SEC\_RULE

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

Example 2-4 Viewing security ruleset information in V$ASM\_ACFS\_SEC\_RULESET

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

Example 2-5 Viewing security ruleset information in V$ASM\_ACFS\_SEC\_RULESET\_RULE

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

Example 2-6 Viewing snapshot information in V$ASM\_ACFSSNAPSHOTS

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

Example 2-7 Viewing volume information with V$ASM\_ACFSVOLUMES

This example shows information displayed from the `V$ASM_ACFSVOLUMES` view. The `PRIMARY_VOL` column contains `TRUE` if the volume is the primary volume for the file system.

```
SELECT fs_name, vol_device, primary_vol, total_mb, free_mb FROM V$ASM_ACFSVOLUMES;

FS_NAME            VOL_DEVICE             PRIMARY_VOL   TOTAL_MB  FREE_MB
------------------ ---------------------- -----------   --------- ----------
/acfsmounts/acfs1  /dev/asm/volume1-228   TRUE            1024000 578626.522
/acfsmounts/acfs2  /dev/asm/volume2-375   TRUE            1024000 685761.463
...
```

Example 2-8 Viewing volume information with V$ASM\_FILESYSTEM

This example shows information displayed from the `V$ASM_FILESYSTEM` view.

The `STATE` column contains the status of the file system, either `AVAILABLE` or `OFFLINE`. An offline file system can only be dismounted; other attempts at access result in errors. Offline means that either the Oracle ASM instance is down, the disk group has been forced dismounted, or less commonly, a metadata I/O failure occurred or serious metadata corruption was detected. With a metadata I/O failure, the file system is also marked as corrupt.

The `CORRUPT` column indicates whether the file system needs the `fsck` command run on it.

```
SELECT fs_name, available_time, block_size, state, corrupt FROM V$ASM_FILESYSTEM;

FS_NAME                    AVAILABLE BLOCK_SIZE STATE         CORRUPT
-------------------------- --------- ---------- ------------- -------
/acfsmounts/acfs1          19-JUL-09          4 AVAILABLE     FALSE
/acfsmounts/acfs2          19-JUL-09          4 AVAILABLE     FALSE
```

Example 2-9 Viewing volume information with V$ASM\_VOLUME

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

Example 2-10 Viewing volume information with V$ASM\_VOLUME\_STAT

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

Example 2-11 Viewing tag name information with V$ASM\_ACFSTAG

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

See Also:

[Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/acfsg&id=REFRN-GUID-8C5690B0-DE10-4460-86DF-80111869CF4C) for information about the Oracle ACFS dynamic views