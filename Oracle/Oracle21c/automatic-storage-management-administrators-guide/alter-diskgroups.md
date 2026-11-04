---
title: "Administrator's Guide"
book: "Automatic Storage Management Administrator's Guide"
doc_id: F30296-05
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/ostmg/alter-diskgroups.html
tags:
  - oracle
  - 21c
  - automatic-storage-management-administrators-guide
---

You can alter a disk group with SQL\*Plus, ASMCA, or ASMCMD commands.

You can use the `ALTER` `DISKGROUP` SQL statement to alter a disk group configuration. You can also alter a disk group configuration with Oracle ASM Configuration Assistant (ASMCA) and the ASMCMD `chdg` command.

You can add, resize, or drop disks while the database remains online. Whenever possible, multiple operations in a single `ALTER` `DISKGROUP` statement are recommended. Grouping operations in a single `ALTER` `DISKGROUP` statement can reduce rebalancing operations.

Oracle ASM automatically rebalances when the configuration of a disk group changes. By default, the `ALTER` `DISKGROUP` statement does not wait until the operation is complete before returning. Query the `V$ASM_OPERATION` view to monitor the status of this operation.

Use the `REBALANCE` `WAIT` clause to cause the `ALTER` `DISKGROUP` statement processing to wait until the rebalance operation is complete before returning. This is especially useful in scripts. The statement also accepts a `REBALANCE` `NOWAIT` clause that invokes the default behavior of conducting the rebalance operation asynchronously in the background.

You can interrupt a rebalance running in wait mode by typing `CTRL+C` on most platforms. This causes the statement to return immediately with the message `ORA-01013: user requested cancel of current operation`, and then to continue the operation asynchronously. Typing `CTRL+C` does not cancel the rebalance operation or any disk add, drop, or resize operations.

To control the speed and resource consumption of the rebalance operation, you can include the `REBALANCE` `POWER` clause in statements that add, drop, or resize disks.

The following topics are discussed:

See Also:

- [Managing Disk Groups with ASMCA](manage-asm-asmca.md) for information about altering a disk group configuration with Oracle ASM Configuration Assistant (ASMCA)
- [chdg](asmcmd-diskgroup-commands.md) for information about altering a disk group configuration with ASMCMD `chdg`
- Manually Rebalancing Disk Groups for more information about the `REBALANCE` `POWER` clause
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=SQLRF-GUID-22D73AB6-7063-4627-A2ED-18D521ED2557) for information about the `ALTER` `DISKGROUP` SQL statement
- [Oracle Automatic Storage Management Cluster File System Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ACFSG-GUID-7783FE8B-3BAD-4C4F-83C5-DF1426340290) for more information about Oracle ACFS and Oracle ADVM

### Adding Disks to a Disk Group

You can use the `ADD` clause of the `ALTER` `DISKGROUP` statement to add a disk or a failure group to a disk group.

You can add a disk or failure group with the `ALTER DISKGROUP` SQL statement. The syntax used is similar to the `CREATE` `DISKGROUP` statement. After you add new disks, the new disks gradually begin to accommodate their share of the workload as rebalancing progresses.

When adding a disk, the disk must be the same size as the other disks in the disk group.

See Also:

- Using the ALTER DISKGROUP SQL Statement to Add Disks to a Disk Group for an example using SQL statements to add disks to a disk group
- [Example 4-1](create-diskgroups.md) for an example of the `CREATE` `DISKGROUP` SQL statement
- [Mirroring, Redundancy, and Failure Group Options](mirroring-diskgroup-redundancy.md) and [Understanding Oracle ASM Concepts](asm-intro.md) for information about redundancy levels and failure groups
- [Managing Disk Groups with ASMCA](manage-asm-asmca.md) for information about adding disks to a disk group with ASMCA
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=SQLRF01113) for information about the `ALTER` `DISKGROUP` SQL statement

#### Using the ALTER DISKGROUP SQL Statement to Add Disks to a Disk Group

The SQL examples in this topic demonstrate the interactions of disk discovery with the `ADD` `DISK` operation. Assume that disk discovery identifies the following disks in `/devices` directory:

```
/devices/diska1 -- member of data1
/devices/diska2 -- member of data1
/devices/diska3 -- member of data1
/devices/diska4 -- member of data1
/devices/diska5 -- candidate disk
/devices/diska6 -- candidate disk
/devices/diska7 -- candidate disk
/devices/diska8 -- candidate disk

/devices/diskb1 -- member of data1
/devices/diskb2 -- member of data1
/devices/diskb3 -- member of data1
/devices/diskb4 -- member of data2

/devices/diskc1 -- member of data2
/devices/diskc2 -- member of data2
/devices/diskc3 -- member of data3
/devices/diskc4 -- candidate disk

/devices/diskd1 -- candidate disk
/devices/diskd2 -- candidate disk
/devices/diskd3 -- candidate disk
/devices/diskd4 -- candidate disk
/devices/diskd5 -- candidate disk
/devices/diskd6 -- candidate disk
/devices/diskd7 -- candidate disk
/devices/diskd8 -- candidate disk
```

You can query the `V$ASM_DISK` view to display the status of Oracle ASM disks. See [Views Containing Oracle ASM Information](views-asm-info.md).

The following statement would fail because `/devices/diska1` through `/devices/diska4` currently belong to the disk group `data1`.

```
ALTER DISKGROUP data1 ADD DISK
     '/devices/diska*';
```

The following statement successfully adds disks `/devices/diska5` and `/devices/diska6` to `data1`. Because no `FAILGROUP` clauses are included in the `ALTER DISKGROUP` statement, each disk is assigned to its own failure group. The `NAME` clauses assign names to the disks, otherwise they would have been assigned system-generated names.

```
ALTER DISKGROUP data1 ADD DISK
     '/devices/diska5' NAME diska5,
     '/devices/diska6' NAME diska6;
```

When specifying a failure group, you can specify the type (regular or quorum) as well as the name. The failure group type value defaults to regular. You must include `QUORUM` `FAILGROUP` clause to specify a quorum failure group. The following statement successfully adds disks `/devices/diska7` and `/devices/diska8` to `data1` using the `FAILGROUP` clause to specify a failure group.

```
ALTER DISKGROUP data1 ADD FAILGROUP fg_diska78 DISK
     '/devices/diska7' NAME diska7,
     '/devices/diska8' NAME diska8;
```

The following statement would fail because the search string matches disks that are contained in other disk groups. Specifically, `/devices/diska4` belongs to disk group `data1` and `/devices/diskb4` belongs to disk group `data2`.

```
ALTER DISKGROUP data1 ADD DISK
     '/devices/disk*4';
```

The following statement would successfully add `/devices/diskd1` through `/devices/diskd8` to disk group `data1`. This statement runs with a rebalance power of 5, and does not return until the rebalance operation is complete.

```
ALTER DISKGROUP data1 ADD DISK
      '/devices/diskd*'
       REBALANCE POWER 5 WAIT;
```

If `/devices/diskc3` was previously a member of a disk group that no longer exists, then you could use the `FORCE` option to add the disk as a member of another disk group. For example, the following use of the `FORCE` clause enables `/devices/diskc3` to be added to `data2`, even though it is a current member of `data3`. For this statement to succeed, `data3` cannot be mounted.

```
ALTER DISKGROUP data2 ADD DISK
     '/devices/diskc3' FORCE;
```

### Replacing Disks in Disk Groups

A disk or multiple disks in a disk group can be replaced, rather than dropped and added back.

The single replace operation is more efficient than dropping and adding disks. This operation is especially useful when disks are missing or damaged.

For example, you can issue the following statement to replace the `diskc7` disk with another disk identified by the `/devices/diskc18` path.

```
SQL> ALTER DISKGROUP data2 REPLACE DISK diskc7 WITH '/devices/diskc18' POWER 3;
```

The power option operates the same as the power option for the `ALTER` `DISKGROUP` `REBALANCE` statement, except that the power option cannot be set to `0`.

The `ALTER` `DISKGROUP` SQL statement with the `REPLACE` clause includes a `WAIT` or `NOWAIT` option, plus the `FORCE` option.

Note:

- Manually Rebalancing Disk Groups for information about the power option in rebalancing a disk group
- [ASM\_POWER\_LIMIT](init-params-asm-instance.md) for information about the `ASM_POWER_LIMIT` initialization parameter

### Renaming Disks in Disk Groups

You can rename a disk in a disk group with the `ALTER` `DISKGROUP` `RENAME` `DISK` SQL statement.

Note:

You can only use the `RENAME` `DISK` operation when the disk group that contains the disk is in the `MOUNT` `RESTRICTED` state. If any disks in the disk group are offline, then the `RENAME` operation fails. If the new disk name exists, then the `RENAME` operation fails. You must have `SYSASM` privileges to rename a disk.

In one SQL statement, you can rename one or multiple disks, or rename all disks in a disk group using the `RENAME` `DISKS` `ALL` clause.

For example, you can rename disks as follows:

```
SQL> ALTER DISKGROUP fra2 MOUNT RESTRICTED;

SQL> ALTER DISKGROUP fra2 RENAME DISK 'FRA1_0001' TO 'FRA2_0001', 
       'FRA1_0002' TO 'FRA2_0002';
```

For `NORMAL`, `HIGH`, and `FLEX` redundancy disk groups, you can associate a site name using `ALTER` `DISKGROUP` `RENAME` `DISK` with the `SITE` clause. For example:

```
SQL> ALTER DISKGROUP data1 RENAME DISK 'DATA1_0001' SITE SITE1;
```

For information about data sites, extended disk groups, and preferred read for disks, refer to [About Oracle ASM Extended Disk Groups](asm-filegroups.md) and [PREFERRED\_READ.ENABLED](manage-diskgroup-attributes.md). For information about the ASMCMD `stamp` command, refer to [stamp](asmcmd-diskgroup-commands.md).

For an `EXTERNAL` redundancy disk group, you can use `ALTER` `DISKGROUP` `RENAME` `DISK` with the `FAILGROUP` clause to specify a failure group for a disk. For example:

```
SQL> ALTER DISKGROUP external1 RENAME DISK 'EXTERNAL1_0001' FAILGROUP FG_EXT1_0001;
```

The `SITE` and `FAILGROUP` clauses cannot be used together in the same SQL `ALTER` `DISKGROUP` `RENAME` statement.

The `ALTER` `DISKGROUP` `diskgroupname` `RENAME` `DISKS` `ALL` statement can be run after the `renamedg` utility to change the names of the disks in the renamed disk group. For information about `renamedg`, refer to [Renaming Disks Groups](maintain-diskgroups.md).

When you run the `ALTER` `DISKGROUP` `diskgroupname` `RENAME` `DISKS` `ALL` statement, any disk name that is not in the format `diskgroupname` `_` `number` is renamed to that format. Disk names that are already in the `diskgroupname` `_` `number` format are not changed.

Note:

If a disk is labeled by any subsystem; such as ASMLIB, ASMFD, EXADATA, or ASMTOOL; then that label becomes the disk name by design. The `ALTER` `DISKGROUP` `RENAME` `DISKS` SQL statement on these subsystems has no effect and the disk is not renamed.

### Dropping Disks from Disk Groups

You can drop disks from a disk group with the `DROP` `DISK` clause of the `ALTER` `DISKGROUP` statement.

You can also drop all of the disks in specified failure groups using the `DROP` `DISKS` `IN` `FAILGROUP` clause.

When a disk is dropped, the disk group is rebalanced by moving all of the file extents from the dropped disk to other disks in the disk group. A drop disk operation might fail if not enough space is available on the other disks. The best approach is to perform both the add and drop operation with the same `ALTER` `DISKGROUP` statement. This has the benefit of rebalancing data extents only one time and ensuring that there is enough space for the rebalance operation to succeed.

Caution:

The `ALTER` `DISKGROUP``...``DROP` `DISK` SQL statement returns to SQL prompt before the drop and rebalance operations are complete. Do not reuse, remove, or disconnect the dropped disk until the `HEADER_STATUS` column for this disk in the `V$ASM_DISK` view changes to `FORMER`. You can query the `V$ASM_OPERATION` view to determine the amount of time remaining for the drop/rebalance operation to complete.

If you specify the `FORCE` clause for the drop operation, the disk is dropped even if Oracle ASM cannot read or write to the disk. You cannot use the `FORCE` flag when dropping a disk from an external redundancy disk group.

Caution:

A `DROP` `FORCE` operation leaves data at reduced redundancy until the subsequent rebalance operation completes. This increases your exposure to data loss if there is a subsequent disk failure during rebalancing. Use `DROP` `FORCE` with caution.

The statements in Example 4-5 demonstrate how to drop disks from the disk group `data1`. The first example drops `diska5` from disk group `data1`. The second example drops `diska5` from disk group `data1`, and also illustrates how multiple actions are possible with one `ALTER DISKGROUP` statement.

Example 4-5 Dropping disks from disk groups

```
ALTER DISKGROUP data1 DROP DISK diska5;

ALTER DISKGROUP data1 DROP DISK diska5
     ADD FAILGROUP failgrp1 DISK '/devices/diska9' NAME diska9;
```

See Also:

- [Managing Disk Groups with ASMCA](manage-asm-asmca.md) for information about dropping disks from a disk group with ASMCA
- Using the ALTER DISKGROUP SQL Statement to Add Disks to a Disk Group for an example of the `ALTER` `DISKGROUP` statement
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=REFRN30173) for information about the `V$ASM_OPERATION` view
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=SQLRF01113) for information about the `ALTER` `DISKGROUP` SQL statement

### Resizing Disks in Disk Groups

The `RESIZE` clause of `ALTER` `DISKGROUP` enables you to resize disks in a disk group.

When resizing disks in a disk group, all the disks must be of equal size.

If you do not specify a new size in the `SIZE` clause, then Oracle ASM uses the size of the disks as returned by the operating system. The new size is written to the Oracle ASM disk header and if the size is increasing, then the new space is immediately available for allocation. If the size is decreasing, rebalancing must relocate file extents beyond the new size limit to available space below the limit. If the rebalance operation can successfully relocate all extents, then the new size is made permanent, otherwise the rebalance fails.

The following example resizes all of the disks in the disk group `data1`. If the new size is greater than the capacity of a disk, then the statement fails.

Example 4-6 Resizing disks in disk groups

```
ALTER DISKGROUP data1 RESIZE ALL SIZE 100G;
```

### Undropping Disks in Disk Groups

The `UNDROP DISKS` clause of the `ALTER` `DISKGROUP` statement enables you to cancel all pending drops of disks within disk groups.

If a drop disk operation has completed, then this statement cannot be used to restore it. This statement cannot be used to restore disks that are being dropped as the result of a `DROP` `DISKGROUP` statement, or for disks that are being dropped using the `FORCE` clause.

The following example cancels the dropping of disks from disk group `data1`:

Example 4-7 Undropping disks in disk groups

```
ALTER DISKGROUP data1 UNDROP DISKS;
```

Note:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=SQLRF01517) for information about the `DROP` `DISKGROUP` SQL statement
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=SQLRF01113) for information about the `ALTER` `DISKGROUP` SQL statement

### Manually Rebalancing Disk Groups

You can manually rebalance the files in a disk group using the `REBALANCE` clause of the `ALTER` `DISKGROUP` statement.

Manual rebalancing would normally not be required because Oracle ASM automatically rebalances disk groups when their configuration changes, including changes to file groups. However, you might want to do a manual rebalance operation to control the speed of what would otherwise be an automatic rebalance operation.

The `POWER` clause of the `ALTER` `DISKGROUP` `REBALANCE` statement specifies the degree of parallelism, and the speed of the rebalance operation. A higher value increases the speed of the rebalance operation. It can be set to a minimum value of `0` which stops a rebalancing operation until the statement is either implicitly or explicitly rerun.

The default rebalance power is set by the `ASM_POWER_LIMIT` initialization parameter. The range of values for the `POWER` clause is the same for the `ASM_POWER_LIMIT` initialization parameter.

The power level of an ongoing rebalance operation can be changed by entering the rebalance statement using the `MODIFY` `POWER` clause. For example, the following SQL statement modifies the power setting to `10` of an ongoing rebalance.

```
ALTER DISKGROUP data2 REBALANCE MODIFY POWER 10;
```

The the following SQL statement modifies the power setting to the default value.

```
ALTER DISKGROUP data2 REBALANCE MODIFY POWER;
```

When you rebalance a disk group, you have the option choosing the following phase options using the `WITH` or `WITHOUT` keywords, except where noted:

- `RESTORE`
	The `RESTORE` phase includes `RESYNC`, `RESILVER`, and `REBUILD` operations. The `RESTORE` phase is always run by default and cannot be excluded.
	- `RESYNC`
		This operation synchronizes the stale extents on the disks that are being brought online.
		- `RESILVER`
		This operation is specific only to Exadata systems. During this phase, data is copied from one mirror to the mirror with stale data.
		- `REBUILD`
		This operation restores the redundancy of forcing disks only. Forcing disks are those disks that have been dropped with the force option.
- `BALANCE`
	This phase restores redundancy of all the disks in the disk group, including file groups, and also balances extents on Oracle ASM disks.
- `PREPARE`
	This phase completes the work corresponding to the prepare SQL operation. This phase is enabled only for `FLEX` or `EXTENDED` redundancy disk groups. `COMPATIBLE.ASM` must be set to `12.2` or higher.
- `COMPACT`
	This phase defragments and compacts extents across Oracle ASM disks.

The rebalance operation executes the phases in the optimal order. If none of the phases are specified with the `ALTER DISKGROUP...REBALANCE` SQL statement, then the behavior remains the same as the rebalance operation previous to the Oracle ASM 12.2 release during which all rebalance phases are run.

The following examples show the use of the phase options with `ALTER DISKGROUP...REBALANCE`:

```
ALTER DISKGROUP data2 REBALANCE WITH BALANCE COMPACT;

ALTER DISKGROUP data3 REBALANCE WITHOUT BALANCE;
```

The `ALTER DISKGROUP...REBALANCE` command returns immediately by default so that you can run other commands while the rebalance operation takes place asynchronously in the background. You can query the `V$ASM_OPERATION` view for the status of the rebalance operation. When not all rebalance phases are run, the `V$ASM_OPERATION` view displays an `ORA-59000` error at the end of the rebalance.

To cause the `ALTER DISKGROUP...REBALANCE` command to wait until the rebalance operation is complete before returning, add the `WAIT` keyword to the `REBALANCE` clause. The wait functionality is especially useful in scripts. The command also accepts a `NOWAIT` keyword, which invokes the default behavior of conducting the rebalance operation asynchronously. You can interrupt a rebalance running in wait mode by typing `CTRL+C` on most platforms. This causes the command to return immediately with the message `ORA-01013: user requested cancel of current operation`, and then continues the rebalance operation asynchronously.

Additional rules for the rebalance operation include the following:

- An ongoing rebalance command is restarted if the storage configuration changes either when you alter the configuration, or if the configuration changes due to a failure or an outage. Furthermore, if the new rebalance fails because of a user error, then a manual rebalance may be required.
- The `ALTER DISKGROUP...REBALANCE` statement runs on a single node even if you are using Oracle Real Application Clusters (Oracle RAC).
- Oracle ASM can perform one disk group rebalance at a time on a given instance. If you have initiated multiple rebalances on different disk groups on a single node, then Oracle processes these operations in parallel on additional nodes if available; otherwise the rebalances are performed serially on the single node. You can explicitly initiate rebalances on different disk groups on different nodes in parallel.
- Rebalancing continues across a failure of the Oracle ASM instance performing the rebalance.
- The `REBALANCE` clause (with its associated `POWER` and `WAIT/NOWAIT` keywords) can also be used in `ALTER DISKGROUP` commands that add, drop, or resize disks.
	Note:
	Oracle restarts the processing of an ongoing rebalance operation if the storage configuration changes. If the next rebalance operation fails because of a user error, then a manual rebalance may be required.

The following example manually rebalances the disk group `data2`. The command does not return until the rebalance operation is complete. All supported phases of the rebalance operation are executed. Note that specifying `RESTORE` is not necessary as that phase is always run during a rebalance.

Example 4-8 Manually rebalancing a disk group

```
ALTER DISKGROUP data2 REBALANCE RESTORE POWER 5 WAIT;
```

See Also:

- [ASM\_POWER\_LIMIT](init-params-asm-instance.md) for information about the `ASM_POWER_LIMIT` initialization parameter
- Tuning Rebalance Operations for information about rebalancing operations
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=SQLRF01113) for information about the `ALTER` `DISKGROUP` SQL statement

### Tuning Rebalance Operations

If the `POWER` clause is not specified in an `ALTER` `DISKGROUP` statement, or when rebalance is implicitly run by adding or dropping a disk, then the rebalance power defaults to the value of the `ASM_POWER_LIMIT` initialization parameter. You can adjust the value of this parameter dynamically. The range of values for the `POWER` clause is the same for the `ASM_POWER_LIMIT` initialization parameter.

The higher the power limit, the more quickly a rebalance operation can complete. Rebalancing takes longer with lower power values, but consumes fewer processing and I/O resources which are shared by other applications, such as the database.

Oracle ASM tries to keep a rebalance I/O for each unit of power. Each I/O requires PGA memory for the extent involved in the relocation.

The default value of `1` minimizes disruption to other applications. The appropriate value is dependent on your hardware configuration, performance requirements, and availability requirements. Oracle ASM always adjusts the power to fit available memory.

When the `COMPATIBLE.ASM` disk group is set to `11.2.0.2` or higher, the rebalance operation may be run as one process using asynchronous I/O. You can check the Oracle ASM alert log for details on the rebalance process.

If a rebalance is in progress because a disk is manually or automatically dropped, then increasing the power of the rebalance shortens the time frame during which redundant copies of that data on the dropped disk are reconstructed on other disks.

You can also affect rebalance behavior with the `CONTENT.CHECK` and `THIN_PROVISIONED` disk group attributes.

The `EXPLAIN` `WORK` SQL statement determines the amount of work for a rebalance operation and the resulting calculations are displayed in the `V$ASM_ESTIMATE` view.

For example:

```
EXPLAIN WORK FOR ALTER DISKGROUP data DROP DISK data_0000;
Explained.

SELECT est_work FROM V$ASM_ESTIMATE;
EST_WORK
--------
    4211

EXPLAIN WORK SET STATEMENT_ID='online' FOR ALTER DISKGROUP data 
  ONLINE disk data_000;
Explained.

SELECT est_work FROM V$ASM_ESTIMATE WHERE STATEMENT_ID='online';
EST_WORK
--------
     421
```

The `V$ASM_ESTIMATE` view provides information for adjusting `ASM_POWER_LIMIT` and the resulting power of rebalance operations. The `EST_WORK` column provides an estimate of the number of allocation units that have to be moved by the rebalance operation to complete.

The `PASS` column of `V$ASM_OPERATION` is updated for resync and rebalance operations. The contents of the column can be `RESYNC`, `REBALANCE`, or `COMPACT`. For example, the following SQL query shows values in the `PASS` column during a rebalance operation.

```
SQL> SELECT GROUP_NUMBER, PASS, STATE FROM V$ASM_OPERATION;

GROUP_NUMBER PASS      STAT
------------ --------- ----
           2 RESYNC    WAIT
           2 REBALANCE WAIT
           2 COMPACT   WAIT
```

See Also:

- [ASM\_POWER\_LIMIT](init-params-asm-instance.md) for information about the `ASM_POWER_LIMIT` initialization parameter
- [Summary of Disk Group Attributes](manage-diskgroup-attributes.md) for information about disk group attributes
- Manually Rebalancing Disk Groups for more information about rebalancing disk groups

### Scrubbing Disk Groups

Oracle ASM disk scrubbing improves availability and reliability by searching for data that may be less likely to be read. Disk scrubbing checks logical data corruptions and repairs them automatically in normal and high redundancy disks groups. The scrubbing process repairs logical corruptions using the mirror disks. Disk scrubbing can be combined with disk group rebalancing to reduce I/O resources. The disk scrubbing process has minimal impact to the regular I/O in production systems.

You can perform scrubbing on a disk group, a specified disk, or a specified file of a disk group with the `ALTER` `DISKGROUP` SQL statement. For example, the following SQL statements show various options used when running the `ALTER` `DISKGROUP` `disk_group` `SCRUB` SQL statement.

```
SQL> ALTER DISKGROUP data SCRUB POWER LOW;

SQL> ALTER DISKGROUP data SCRUB FILE '+DATA/ORCL/DATAFILE/example.266.806582193' 
       REPAIR POWER HIGH FORCE;

SQL> ALTER DISKGROUP data SCRUB DISK DATA_0005 REPAIR POWER HIGH FORCE;
```

You can stop an ongoing scrub operation with the `STOP` option.

```
SQL> ALTER DISKGROUP data SCRUB STOP;
```

When using `ALTER` `DISKGROUP` with the `SCRUB` option, the following items apply:

- The optional `REPAIR` option automatically repairs disk corruptions. If the `REPAIR` option is not specified, then the `SCRUB` option only checks and reports logical corruptions of the specified target.
- The optional `POWER` value can be set to `AUTO`, `LOW`, `HIGH`, or `MAX`. If the `POWER` option is not specified, the power value defaults to `AUTO` and the power adjusts to the optimum level for the system.
- If the optional `WAIT` option is specified, the command returns after the scrubbing operation has completed. If the `WAIT` option is not specified, the scrubbing operation is added into the scrubbing queue and the command returns immediately.
- If the optional `FORCE` option is specified, the command is processed even if the system I/O load is high or scrubbing has been disabled internally at the system level.

The scrubbing process is visible in the fields of the `V$ASM_OPERATION` view while the scrubbing process is running.

### Managing Oracle ADVM Volumes in a Disk Group

You can create an Oracle ASM Dynamic Volume Manager (Oracle ADVM) volume in a disk group.

The volume device associated with the dynamic volume can be used to host an Oracle ACFS file system.

The compatibility attributes `COMPATIBLE.ASM` and `COMPATIBLE.ADVM` must be set to `11.2` or higher for the disk group.

The `ALTER` `DISKGROUP` `VOLUME` SQL statements enable you to manage Oracle ADVM volumes, including the functionality to add, modify, resize, disable, enable, and drop volumes.

If the Oracle ADVM volume is on a flex disk group, then you can change the redundancy of the Oracle ADVM volume online with the `ALTER` `DISKGROUP` `MODIFY` `FILEGROUP` `volume_name` SQL statement.

Note:

If the volume is hosting an Oracle ACFS file system, then you cannot resize that volume with the SQL `ALTER` `DISKGROUP` statement. You must use the `acfsutil` `size` command instead.

The following are examples of the `ALTER` `DISKGROUP` `VOLUME` statement.

Example 4-9 Managing volumes with ALTER DISKGROUP VOLUME statements

```
SQL> ALTER DISKGROUP data ADD VOLUME volume1 SIZE 10G;
Diskgroup altered.

SQL> ALTER DISKGROUP data RESIZE VOLUME volume1 SIZE 15G;
Diskgroup altered.

SQL> ALTER DISKGROUP data DISABLE VOLUME volume1;
Diskgroup altered.

SQL> ALTER DISKGROUP data ENABLE VOLUME volume1;
Diskgroup altered.

SQL> ALTER DISKGROUP ALL DISABLE VOLUME ALL;
Diskgroup altered.

SQL> ALTER DISKGROUP data DROP VOLUME volume1;
Diskgroup altered.
```

See Also:

- [Disk Group Compatibility Attributes](diskgroup-compatibility.md) for information about disk group compatibility attributes
- [About Oracle ASM File Group Properties](asm-filegroups.md) for information about file group properties
- [Oracle Automatic Storage Management Cluster File System Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ACFSG-GUID-7783FE8B-3BAD-4C4F-83C5-DF1426340290) for more information about managing Oracle ACFS and Oracle ADVM with ASMCMD and ASMCA tools
- [Oracle Automatic Storage Management Cluster File System Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ACFSG-GUID-79A8333D-4E1C-4788-944D-EC86E4278C00) for information about the resizing a volume with `acfsutil` `size`
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=SQLRF-GUID-22D73AB6-7063-4627-A2ED-18D521ED2557) for information about the `ALTER` `DISKGROUP` SQL statement