---
title: "Administrator's Guide"
book: "Automatic Storage Management Administrator's Guide"
doc_id: F30296-05
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/ostmg/asm-access-control-diskgroups.html
tags:
  - oracle
  - 21c
  - automatic-storage-management-administrators-guide
---

Oracle ASM File Access Control provides optional protection for the content of Oracle ASM disk groups from accidental access by unauthorized Oracle ASM clients, such as an unauthorized database.

To set up Oracle ASM File Access Control, you must designate separate operating system group. You can manage Oracle ASM file access control with ASMCMD commands and SQL statements.

This section contains these topics:

See Also:

- [Using Separate Operating System Groups for Oracle ASM Users](authenticate-access-asm-instance.md) for information about designating separate operating system groups
- [ASMCMD File Access Control Commands](asmcmd-accesscontrol-commands.md) for information about managing Oracle ASM File Access Control with ASMCMD commands
- [Viewing Oracle ASM File Access Control Information](views-asm-info.md) for information about views that provide details about Oracle ASM file access control
- [Authentication for Accessing Oracle ASM Instances](authenticate-access-asm-instance.md) for information about controlling accessing to Oracle ASM instances

### About Oracle ASM File Access Control

Oracle ASM File Access Control restricts the access of files to specific Oracle ASM clients that connect as SYSDBA.

An Oracle ASM client is typically a database, which is identified as the user that owns the database instance home. Oracle ASM File Access Control uses this user name to identify a database. Oracle ASM File Access Control restricts access based on the operating system effective user identification number of a database owner. For example, in [Table 3-2](authenticate-access-asm-instance.md) the databases are identified as `oracle1` and `oracle2`.

Oracle ASM uses file access control to determine the additional privileges that are given to a database that has been authenticated AS SYSDBA on the Oracle ASM instance. These additional privileges include the ability to modify and delete certain files, aliases, and user groups.

You can set up user groups to specify the list of databases that share the same access permissions to Oracle ASM files. User groups are lists of databases and any database that authenticates AS SYSDBA can create a user group. However, only the creator of a group can delete it or modify its membership list.

Each Oracle ASM file has three categories of privileges: owner, group, and other. Each category can have no permission, read-only permission, or read-write permission.

The file owner is usually the creator of the file and can assign permissions for the file in any of the owner, group, or other categories. The owner can also change the group associated with the file.

When you create a file, a group is not automatically associated with the file. You must use the `asmcmd` `chgrp` command to set the group manually because Oracle ASM File Access Control does not have the concept of the primary group of a user.

When administering Oracle ASM File Access Control, Oracle recommends that you connect as SYSDBA to the database instance that is the owner, or planned owner, of the files in the disk group.

To set up Oracle ASM File Access Control for files in a disk group, perform the following steps:

1. Alter a new or existing disk group to set the Oracle ASM File Access Control disk group attributes.
	For a newly-created disk group, you should set the disk group attributes before creating any files in the disk group.
2. For files that exist in a disk group before setting the Oracle ASM File Access Control disk group attributes, you must explicitly set the permissions and ownership on those existing files.
	Ensure that the user exists before setting ownership or permissions on a file. The file must be closed before setting the ownership or permissions.
3. Optionally, you can create user groups that are groups of database users that share the same access permissions to Oracle ASM files.

See Also:

- Setting Disk Group Attributes for Oracle ASM File Access Control for information about setting disk group attributes
- Using SQL Statements to Manage Oracle ASM File Access Control for information about using `ALTER` `DISKGROUP` `SET` `PERMISSION` and `ALTER` `DISKGROUP` `SET` `OWNERSHIP` for managing Oracle ASM File Access Control with SQL statements
- Using SQL Statements to Manage Oracle ASM File Access Control for information about using `ALTER` `DISKGROUP` `ADD` `USERGROUP`

### Setting Disk Group Attributes for Oracle ASM File Access Control

To manage Oracle ASM File Access Control for a disk group, you must set the `ACCESS_CONTROL.ENABLED` and `ACCESS_CONTROL.UMASK` disk group attributes. You can set the attributes by altering the disk group with the `ALTER` `DISKGROUP` SQL statement or you can set the attributes with the ASMCMD `setattr` command.

When you set up file access control on an existing disk group, the files previously created remain accessible by everyone, unless you run the `ALTER` `DISKGROUP` `SET` `PERMISSION` SQL statement or the ASMCMD `chmod` command to restrict the permissions.

The `COMPATIBLE.ASM` and `COMPATIBLE.RDBMS` disk group attributes must be set to `11.2` or higher to enable Oracle ASM File Access Control.

The disk group attributes that control Oracle ASM File Access Control are the following:

- `ACCESS_CONTROL.ENABLED`
	This attribute determines whether Oracle ASM File Access Control is enabled for a disk group.
	The value can be `true` or `false`. The default is `false`.
	If the attribute is set to `true`, accessing Oracle ASM files is subject to access control. If `false`, any user can access every file in the disk group. All other operations behave independently of this attribute.
- `ACCESS_CONTROL.UMASK`
	This attribute determines which permissions are masked out on the creation of an Oracle ASM file for the user that owns the file, users in the same user group, and others not in the user group. This attribute applies to all files on a disk group.
	The values can be combinations of three digits { `0` | `2` | `6` } { `0` | `2` | `6` } { `0` | `2` | `6` }. The default is `066`.
	Setting to `0` masks out nothing. Setting to `2` masks out write permission. Setting to `6` masks out both read and write permissions.
	Before setting the `ACCESS_CONTROL.UMASK` disk group attribute, you must set the `ACCESS_CONTROL.ENABLED` attribute to `true` to enable Oracle ASM File Access Control.

Example 4-11 shows how to enable Oracle ASM File Access Control for a disk group using SQL\*Plus. In this example, the `umask` permissions setting is `026` which enables read-write access for the owner (masks out nothing with `0`), read access for users in the group (masks out write permission with `2`), and no access to others (masks out all access with `6`) not in the group.

Example 4-11 Setting up Oracle ASM File Access Control

```
ALTER DISKGROUP data1 SET ATTRIBUTE 'access_control.enabled' = 'true';
ALTER DISKGROUP data1 SET ATTRIBUTE 'access_control.umask' = '026';
```

See Also:

- [setattr](asmcmd-diskgroup-commands.md) for information about the ASMCMD `setattr` command
- [chmod](asmcmd-accesscontrol-commands.md) for information about the ASMCMD `chmod` command
- [Disk Group Compatibility](diskgroup-compatibility.md) for information about disk group compatibility attributes

### Using SQL Statements to Manage Oracle ASM File Access Control

You can use the `ALTER` `DISKGROUP` SQL statement to manage file access control for Oracle ASM disk groups. These SQL statements are available for both database and Oracle ASM instances.

When administering users with SQL\*Plus, the users must be existing operating system users and their user names must have corresponding operating system user IDs. However, only users in the same cluster as the Oracle ASM instance can be validated.

Note:

When modifying ownership of files, the previous owner of a file cannot be dropped while the file is still open even after the ownership of the file has changed.

The SQL statements that support disk group access control are:

- `ALTER` `DISKGROUP` `ADD` `USERGROUP` `WITH` `MEMBER`
	Adds an Oracle ASM user group to a disk group. The maximum length of a user group name is 63 bytes. If you specify the user name, then it must be in the OS password file and its length cannot exceed 32 characters.
	The operating system users of the databases identified in the `MEMBER` clause must be in the disk group, as shown by `V$ASM_USER`, or the command returns an error. Any users authenticated as `SYSASM` or `SYSDBA` can create new user groups. For example:
	```
	SQL> SELECT group_number, os_name FROM V$ASM_USER;
	GROUP_NUMBER OS_NAME
	------------ ----------------------------------------------------------------
	           1 oracle1
	           1 oracle2
	...
	SQL> ALTER DISKGROUP data ADD USERGROUP 'test_grp1' 
	     WITH MEMBER 'oracle1','oracle2';
	```
- `ALTER` `DISKGROUP` `DROP` `USERGROUP`
	Drops an Oracle ASM user group from a disk group. Dropping a group might leave some files without a valid group. For those files to have a valid group, you must manually update the group associated with those files to a valid group.
	```
	SQL> ALTER DISKGROUP data DROP USERGROUP 'test_grp1';
	```
- `ALTER` `DISKGROUP` `MODIFY` `USERGROUP` `ADD` `MEMBER`
	Adds users to the specified user group. The users must be in the disk group, as shown by `V$ASM_USER`, or the command returns an error. Only the creator of the group or the Oracle ASM administrator can modify group membership.
	```
	SQL> ALTER DISKGROUP data MODIFY USERGROUP 'test_grp2' ADD MEMBER 'oracle2';
	```
- `ALTER` `DISKGROUP` `MODIFY` `USERGROUP` `DROP` `MEMBER`
	Removes users from the specified user group. If a member is not in the user group, then an error is returned. Only the creator of the group or the Oracle ASM administrator can modify group membership.
	```
	SQL> ALTER DISKGROUP data MODIFY USERGROUP 'test_grp2' DROP MEMBER 'oracle2';
	```
- `ALTER` `DISKGROUP` `ADD` `USER`
	Adds operating system (OS) users to an Oracle ASM disk group, so that these users can have access privileges on the disk group. If a user exists in the disk group, as shown by `V$ASM_USER`, then the command records an error and continues to add other users, if any.
	The operating system user of a running database instance is automatically added to a disk group when the database instance accesses that disk group and creates files. However, for a database instance to read files in a disk group without creating any files, then you must use the `ADD` `USER` clause to add the operating system user associated with that database to the disk group. Also, you can use this clause to add the operating system user associated with a database to an existing disk group immediately after setting the Oracle ASM File Access Control disk group attributes and before creating new files.
	```
	SQL>  ALTER DISKGROUP data ADD USER 'oracle1';
	```
- `ALTER` `DISKGROUP` `DROP` `USER`
	Drops operating system users from an Oracle ASM disk group. If a user is not in the disk group, then this command records an error and continues to drop other users, if any.
	If the user owns any files on the same Oracle ASM disk group, then this command fails with an error, unless the `CASCADE` keyword is specified. If the latter case, then the user is deleted, along with all the files that the user owns.
	If any files owned by the user are currently open, then the `DROP` `USER` command fails, and no files are deleted.
	```
	SQL>  ALTER DISKGROUP data DROP USER 'oracle1';
	```
- `ALTER` `DISKGROUP` `REPLACE` `USER`
	Replaces one operating system user with another in an Oracle ASM disk group. The replacement user must not be a user currently in the disk group user list.
	If the command succeeds, all files that were previously owned by current user are now owned by the replacement user. The current user is automatically removed from the user list of the disk group. Adding the current user back to the disk group is possible, but this user does not own any files.
	When changing the owner of an open file, the new owner cannot be dropped with the owner's files until all instances within a cluster are restarted.
	Only an Oracle ASM administrator can run this command.
	```
	SQL> ALTER DISKGROUP data REPLACE USER 'oracle1' WITH 'oracle2';
	```
- `ALTER` `DISKGROUP` `SET` `PERMISSION`
	Modifies permissions of an Oracle ASM file. Setting `read` `only` permission to a file that has `read` `write` permission revokes the `write` permission. Only the file owner or the Oracle ASM administrator can change the permissions of a file.
	```
	SQL> ALTER DISKGROUP data SET PERMISSION OWNER=read write, GROUP=read only,
	     OTHER=none FOR FILE '+data/controlfile.f';
	```
- `ALTER` `DISKGROUP` `SET` `OWNERSHIP`
	Changes the owner or group of a file to the specified user or user group name, respectively. If the specified user or user group name does not exist, this command fails with an error. Only the owner of the file or the Oracle ASM administrator can run this command, and only the Oracle ASM administrator can change the owner. Also, the user group name must exist, and the owner of the file must be a member of that group.
	```
	SQL> ALTER DISKGROUP data SET OWNERSHIP OWNER='oracle1', GROUP='test_grp1'
	     FOR FILE '+data/controlfile.f';
	```

See Also:

The [`ALTER DISKGROUP`](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=SQLRF01113) SQL statement in the [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=SQLRF01113)