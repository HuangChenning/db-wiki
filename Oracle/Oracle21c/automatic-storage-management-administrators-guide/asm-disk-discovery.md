---
title: "Administrator's Guide"
book: "Automatic Storage Management Administrator's Guide"
doc_id: F30296-05
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/ostmg/asm-disk-discovery.html
tags:
  - oracle
  - 21c
  - automatic-storage-management-administrators-guide
---

Disk discovery is the mechanism used to find the operating system names for disks Oracle ASM can access.

This mechanism finds all the disks that comprise a disk group to be mounted, the disks an administrator wants to add to a disk group, or the disks the administrator might consider adding to a disk group. This section contains the following topics:

See Also:

[ASM\_DISKSTRING](init-params-asm-instance.md) for additional information about disk discovery and the `ASM_DISKSTRING` initialization parameter

### How A Disk is Discovered

When an Oracle ASM instance is initialized, Oracle ASM discovers and examines the contents of all of the disks that are in the paths that you designated with values in the `ASM_DISKSTRING` initialization parameter.

Disk discovery also occurs when you:

- Run the following SQL statements
	- Mount a disk group with `ALTER` `DISKGROUP` `MOUNT`
		- Online a disk with `ALTER` `DISKGROUP` `ONLINE` `DISK`
		- Add a disk to a disk group with `CREATE` or `ALTER` `DISKGROUP`...`ADD` `DISK`
		- Resize a disk in a disk group with `ALTER` `DISKGROUP`...`RESIZE` `DISK`
		- Query with `SELECT` `FROM` `V$ASM_DISKGROUP` or `V$ASM_DISK` views
- Run Oracle ASM Configuration Assistant (ASMCA) operations or ASMCMD commands that perform the same operations as the SQL statements previously listed

After Oracle ASM successfully discovers a disk, the disk appears in the `V$ASM_DISK` view. Disks that belong to a disk group, that is, disks that have a disk group name in the disk header, show a header status of `MEMBER`. Disks that were discovered, but that have not yet been assigned to a disk group, have a status of either `CANDIDATE` or `PROVISIONED`. Disks that previously belonged to a disk group and were dropped cleanly from the disk group have a status of `FORMER`.

The `PROVISIONED` status implies that an additional platform-specific action has been taken by an administrator to make the disk available for Oracle ASM. For example, on Windows computers, the administrator might have used `asmtool` or `asmtoolg` to stamp the disk with a header. For example, on Linux computers, the administrator might have used Oracle ASM Filter Driver or ASMLIB to prepare the disk for Oracle ASM.

Example 4-10 shows a SQL query on `V$ASM_DISK` that displays the header status of a group of disks.

Example 4-10 Querying V$ASM\_DISK for header status

```
SQL> SELECT name, header_status, path FROM V$ASM_DISK 
     WHERE path LIKE '/devices/disk0%';

NAME      HEADER_STATUS PATH
--------- ------------- ---------------------
          FORMER        /devices/disk02
          FORMER        /devices/disk01
          CANDIDATE     /devices/disk07
DISK06    MEMBER        /devices/disk06
DISK05    MEMBER        /devices/disk05
DISK04    MEMBER        /devices/disk04
DISK03    MEMBER        /devices/disk03
7 rows selected.
```

### Disk Discovery Rules

The rules for discovering Oracle ASM disks are as follows:

- Oracle ASM can discover up to 10,000 disks. That is, if more than 10,000 disks match the `ASM_DISKSTRING` initialization parameter, then Oracle ASM discovers only the first 10,000.
- Oracle ASM only discovers disk partitions. Oracle ASM does not discover partitions that include the partition table.
- From the perspective of the installation, candidate disks are those that have the `CANDIDATE`, `PROVISIONED`, or `FORMER` header status. These disks with a `CANDIDATE`, `PROVISIONED`, or `FORMER` status can be added to Oracle ASM disk groups without using the `FORCE` flag.
- When adding a disk, the `FORCE` option must be used if Oracle ASM recognizes that the disk was managed by Oracle. Such a disk appears in the `V$ASM_DISK` view with a status of `FOREIGN`. In this case, you can only add the disk to a disk group by using the `FORCE` keyword.
- `MEMBER` disks can usually be added to a disk group by specifying the `FORCE` flag, if the disks are not part of a currently mounted disk group.

In addition, Oracle ASM identifies the following configuration errors during discovery:

- Multiple paths to the same disk
	In this case, if the disk is part of a disk group, then disk group mount fails. If the disk is being added to a disk group with the `ADD DISK` or `CREATE DISKGROUP` command, then the command fails. To correct the error, adjust the `ASM_DISKSTRING` value so that Oracle ASM does not discover multiple paths to the same disk. Or if you are using multipathing software, then ensure that you include only the pseudo-device name in the `ASM_DISKSTRING` value. See [Oracle ASM and Multipathing](considerations-asm-storage.md).
- Multiple Oracle ASM disks with the same disk header
	This can be caused by having copied one disk onto another. In this case, the disk group mount operation fails.

### Improving Disk Discovery Time

The value for the `ASM_DISKSTRING` initialization parameter is an operating system–dependent value that Oracle ASM uses to limit the set of paths that the discovery process uses to search for disks. When a new disk is added to a disk group, each Oracle ASM instance that has the disk group mounted must be able to discover the new disk using its `ASM_DISKSTRING`.

In many cases, the default value (`NULL`) is sufficient. Using a more restrictive value might reduce the time required for Oracle ASM to perform discovery, and thus improve disk group mount time or the time for adding a disk to a disk group. Oracle may dynamically change the `ASM_DISKSTRING` before adding a disk so that the new disk is discovered through this parameter.

The default value of `ASM_DISKSTRING` might not find all disks in all situations. If your site is using Oracle ASM Filter Driver or a third-party vendor, then you may have discovery string conventions that you must use for `ASM_DISKSTRING`.

In addition, if your installation uses multipathing software, then the software might place pseudo-devices in a path that is different from the operating system default.

See Also:

- [Administering Oracle ASM Filter Driver](administer-filter-driver.md) for information about Oracle ASM Filter Driver
- [Oracle ASM and Multipathing](considerations-asm-storage.md) and your multipathing vendor documentation for information about multipathing