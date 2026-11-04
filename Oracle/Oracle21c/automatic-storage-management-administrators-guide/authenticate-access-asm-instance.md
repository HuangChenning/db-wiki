---
title: "Administrator's Guide"
book: "Automatic Storage Management Administrator's Guide"
doc_id: F30296-05
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/ostmg/authenticate-access-asm-instance.html
tags:
  - oracle
  - 21c
  - automatic-storage-management-administrators-guide
---

An Oracle ASM instance does not have a data dictionary, so the only way to connect to an Oracle ASM instance is by using one of three system privileges, `SYSASM`, `SYSDBA`, or `SYSOPER`. There are three modes of connecting to Oracle ASM instances:

- Local connection using operating system authentication
- Local connection using password authentication
- Remote connection by way of Oracle Net Services using password authentication

This section describes the following topics:

The Oracle ASM and database instances must have read/write operating system access rights to disk groups. For example, the Oracle ASM instance and the database instance must have identical read and write permissions for the disks that comprise the related Oracle ASM disk group. For Linux and UNIX systems, this is typically provided through shared Linux and UNIX group membership (OSASM group). On Windows systems, the Oracle ASM service must be run as Administrator.

See Also:

- [Managing Oracle ASM File Access Control for Disk Groups](asm-access-control-diskgroups.md) for information about file permissions and Oracle ASM File Access Control
- [Oracle Grid Infrastructure Installation and Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=CWGEN) for your operating system-specific information about how to ensure that the Oracle ASM and database instances have member disk access
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=DBSEG009) for information about maintaining database security, including assigning passwords

### About Privileges for Oracle ASM

During Oracle ASM installation, you can use one operating system group for all users or divide system privileges so that database administrators, storage administrators, and database operators each have distinct operating system privilege groups.

Whether you create separate operating system privilege groups or use one group to provide operating system authentication for all system privileges, you should use SYSASM to administer an Oracle ASM instance. The SYSDBA privilege cannot be used to administer an Oracle ASM instance. If you use the SYSDBA privilege to run administrative commands on an Oracle ASM instance, the operation results in an error. The SYSDBA privilege is intended to be used by the database to access disk groups.

Oracle also recommends the use of a less privileged user, such as ASMSNMP with SYSDBA privileges that is created during installation, for monitoring the Oracle ASM instance.

Operating system authentication using membership in the group or groups designated as OSDBA, OSOPER, and OSASM is valid on all Oracle platforms. Connecting to an Oracle ASM instance as SYSASM grants you full access to all of the available Oracle ASM disk groups and management functions.

This section contains these topics:

- Using One Operating System Group for Oracle ASM Users
- Using Separate Operating System Groups for Oracle ASM Users
- The SYSASM Privilege for Administering Oracle ASM
- The SYSDBA Privilege for Managing Oracle ASM Components

See Also:

[Oracle Automatic Storage Management Cluster File System Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ACFSG-GUID-EC577A31-256E-4FD2-9E9F-749D78B378D0) for information about privileges and Oracle ACFS

#### Using One Operating System Group for Oracle ASM Users

If you do not want to divide the privileges for system access into separate operating system groups, then you can designate one operating system group as the group whose members are granted access as OSDBA, OSOPER, and OSASM for Oracle ASM privileges. The default operating system group name for all of these is usually `dba` and that group is typically chosen for the default configuration.

Table 3-1 shows an example of a Linux deployment without separated privileges for Oracle ASM users.

Table 3-1 One operating system group and one set of privileges for all Oracle ASM users

| Role/Software Owner | User | Group/Privilege |
| --- | --- | --- |
| Oracle ASM administrator/Oracle Grid Infrastructure home | oracle | dba/SYSASM, SYSDBA, SYSOPER |
| Database administrator 1/Database home 1 | oracle | dba/SYSASM, SYSDBA, SYSOPER |
| Database administrator 2/Database home 2 | oracle | dba/SYSASM, SYSDBA, SYSOPER |
| Operating system disk device owner | oracle | dba |

#### Using Separate Operating System Groups for Oracle ASM Users

You can designate separate operating system groups as the operating system authentication groups for privileges on Oracle ASM. The following list describes the separate operating system authentication groups for Oracle ASM and the privileges that their members are granted.

- OSASM group (for example: `asmadmin`)
	This group is granted the SYSASM privilege, which provides full administrative privileges for the Oracle ASM instance.
- OSDBA for Oracle ASM group (for example: `asmdba`)
	This group is granted the SYSDBA privilege on the Oracle ASM instance, which grants access to data stored on Oracle ASM. This group has a subset of the privileges of the OSASM group.
	When you implement separate administrator privileges, choose an OSDBA group for the Oracle ASM instance that is different than the group that you select for the database instance (`dba`).
- OSOPER for Oracle ASM group (for example: `asmoper`)
	This group is granted the SYSOPER privilege on the Oracle ASM instance, which provides operations such as startup, shutdown, mount, dismount, and check disk group. This group has a subset of the privileges of the OSASM group.

When you implement separate Oracle ASM and database administrator duties, this configuration requires different group and different software owners. Implicitly this implementation requires that the OSASM and OSDBA are different groups. For this configuration, you must create an OSDBA for Oracle ASM group and a database instance must be a member of that group to access the Oracle ASM instance.

In an installation that has been configured as Oracle Grid Infrastructure, the Oracle ASM user, such as `grid`, does not have to be a member of the Oracle Database OSDBA group, such as `dba1` or `dba2`, because the Oracle Clusterware database agent runs as the database owner and can use SYSDBA to connect to the database.

However, in an Oracle Restart configuration, the Oracle ASM user (`grid`) must be a member of the OSDBA group (`dba1`, `dba2`,...) of every database. This requirement is necessary because Oracle Restart software runs as the Oracle ASM user (`grid`) and this user must be able to start and stop the databases using the `CONNECT` `/` `AS` `SYSDBA` authentication.

Additionally, the owner of the operating system disk devices should be the same as the owner of the Oracle ASM software.

Table 3-2 shows an example of a Linux deployment using separate operating system privilege groups for Oracle ASM users.

Table 3-2 Separated operating system groups and privileges for Oracle ASM users

| Role/Software Owner | User | Group/Privilege |
| --- | --- | --- |
| Oracle ASM administrator/Oracle Grid Infrastructure home | grid | asmadmin (OSASM)/SYSASM  asmdba (OSDBA for ASM)/SYSDBA  asmoper (OSOPER for ASM)/SYSOPER  dba1, dba2,... (OSDBA for the databases when in an Oracle Restart configuration) |
| Database administrator 1/Database home 1 | oracle1 | asmdba (OSDBA for ASM)/SYSDBA  oper1 (OSOPER for database 1)/SYSOPER  dba1 (OSDBA for database 1)/SYSDBA |
| Database administrator 2/Database home 2 | oracle2 | asmdba (OSDBA for ASM)/SYSDBA  oper2 (OSOPER for database 2)/SYSOPER  dba2 (OSDBA for database 2)/SYSDBA |
| Operating system disk device owner | grid | asmadmin (OSASM) |

#### The SYSASM Privilege for Administering Oracle ASM

SYSASM is a system privilege that enables the separation of the SYSDBA database administration privilege from the Oracle ASM storage administration privilege. Access to the SYSASM privilege is granted by membership in an operating system group that is designated as the OSASM group. This is similar to SYSDBA and SYSOPER privileges, which are system privileges granted through membership in the groups designated as the OSDBA and OSOPER operating system groups. You can designate one group for all of these system privileges, or you can designate separate groups for each operating system privilege.

You can also grant the SYSASM privilege with password file authentication, as discussed in Password File Authentication for Oracle ASM.

To connect locally as SYSASM using password authentication with SQL\*Plus, use the following statement:

```
sqlplus SYS AS SYSASM
...
Enter password:
```

To connect remotely as SYSASM using password authentication with SQL\*Plus, use the following statement:

```
sqlplus sys@\"myhost.mydomain.com:1521/+ASM\" AS SYSASM
...
Enter password:
```

In the previous example, `+ASM` is the service name of the Oracle ASM instance.

To connect locally as SYSASM to an Oracle ASM instance using operating system authentication with SQL\*Plus, use the following statement:

```
sqlplus / AS SYSASM
```

#### The SYSDBA Privilege for Managing Oracle ASM Components

You can connect as SYSDBA to use SQL\*Plus or ASMCMD commands to manage Oracle ASM components associated with the database. When running SQL or ASMCMD operations with the SYSDBA privilege, connect to the database instance rather than the Oracle ASM instance.

Connecting as SYSDBA to the database instance has a limited set of Oracle ASM privileges. For example, you cannot create a disk group when connected with the SYSDBA privilege.

When connected as SYSDBA to the database instance, the Oracle ASM operations are limited to:

- Create and delete files, aliases, directories, and templates
- Examine various Oracle ASM instance views
- Operate on files that were created by this user or only access files to which another user had explicitly granted access
- Granting Oracle ASM File Access Control to other users

### Creating Users with the SYSASM Privilege

When you are logged in to an Oracle ASM instance as SYSASM, you can use the combination of `CREATE` `USER` and `GRANT` SQL statements to create a user who has the SYSASM privilege.

You also can revoke the SYSASM privilege from a user using the `REVOKE` command, and you can drop a user from the password file using the `DROP` `USER` command.

Note:

- These commands update the password file for the local Oracle ASM instance only.
- Oracle ASM does not support the creation of external and global users.

The following example describes how to perform these SQL operations for the user identified as `new_user`:

```
REM create a new user, then grant the SYSASM privilege
SQL> CREATE USER new_user IDENTIFIED by new_user_passwd;
SQL> GRANT SYSASM TO new_user;

REM connect the user to the ASM instance
SQL> CONNECT new_user AS SYSASM;
Enter password:

REM revoke the SYSASM privilege, then drop the user
SQL> REVOKE SYSASM FROM new_user;
SQL> DROP USER new_user;
```

When you revoke the last privilege of a user in an Oracle ASM password file, the user is not automatically deleted as is done in the Oracle Database password file. You must run `DROP` `USER` to delete a user with no privileges in an Oracle ASM password file.

See Also:

- [orapwusr](asmcmd-instance-commands.md) for information about creating a user with Oracle ASM command-line utility (ASMCMD)
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=SQLRF01503) for information about the `CREATE` `USER` and `GRANT` commands
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ADMIN10241) for information about creating and maintaining a password file

### Operating System Authentication for Oracle ASM

Membership in the operating system group designated as the OSASM group provides operating system authentication for the SYSASM system privilege. OSASM is provided exclusively for Oracle ASM. Initially, only the user that installs ASM is a member of the OSASM group, if you use a separate operating system group for that privilege. However, you can add other users. Members of the OSASM group are authorized to connect using the SYSASM privilege and have full access to Oracle ASM, including administrative access to all disk groups that are managed by that Oracle ASM instance.

On Linux and UNIX systems, `dba` is the default operating system group designated as `OSASM`, `OSOPER`, and `OSDBA` for Oracle ASM.

On Windows systems, `ORA_ASMADMIN`, `ORA_ASMDBA`, and `ORA_ASMOPER` are the operating system groups designated for `OSASM`, `OSDBA` and `OSOPER` respectively for Oracle ASM.

SQL\*Plus commands, ASMCMD commands, and ASMCA use operating system authentication.

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ADMIN001) for more information about using operating system authentication
- [Oracle Grid Infrastructure Installation and Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=CWGEN) for information about installation of the Oracle Grid Infrastructure
- [Oracle Database Installation Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=GINST) for your specific operating system for information about default operating system groups

### Password File Authentication for Oracle ASM

Password file authentication for Oracle ASM can work both locally and remotely. To enable password file authentication, you must create a password file for Oracle ASM.

If you select the Oracle ASM storage option, then ASMCA creates a password file for Oracle ASM with initial users (SYS and ASMSNMP) when ASMCA configures the Oracle ASM disk groups. To add other users to the password file, you can use the `CREATE` `USER` and `GRANT` commands.

If you configure an Oracle ASM instance without using ASMCA, then you must manually create a password file and grant the SYSASM privilege to user SYS.

SQL\*Plus commands use password file authentication.

See Also:

- About Privileges for Oracle ASM for information about privileges for Oracle ASM
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ADMIN10241) for information about creating and maintaining a password file
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=SQLRF01503) for information about the `CREATE` `USER` and `GRANT` commands
- [Oracle Database Security Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=DBSEG001) for information about database security
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=REFRN30189) for information about the `V$PWFILE_USERS` view which lists users who have been granted `SYSASM`, `SYSDBA`, and `SYSOPER` privileges as derived from the password file.

### Managing a Shared Password File in a Disk Group

You can manage a shared password file on a disk group enabling access to the single file across the cluster system.

This sections contains these topics:

- About a Shared Password File in a Disk Group
- Creating a Password File in a Disk Group
- Backing Up and Restoring an Oracle ASM Password File in a Disk Group

Note:

After a change has been made to the location of the password file, the following SQL statement should be executed to flush the password file metadata cache.

```
SQL> ALTER SYSTEM FLUSH PASSWORDFILE_METADATA_CACHE
```

The location of the password file can be changed by running `orapwd`, or the ASMCMD `pwcopy`, `pwcreate`, `pwdelete`, `pwmove`, or `pwset` command.

For information about ASMCMD commands to manage an Oracle ASM or database instance password file in a disk group, refer to [ASMCMD Instance Management Commands](asmcmd-instance-commands.md).

See Also:

- [Oracle Database Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=ADMIN10241) for information about maintaining a password file
- [Oracle Database Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=REFRN10184) for information about the `REMOTE_LOGIN_PASSWORDFILE` initialization parameter
- [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=CWADD-GUID-1DCA9E3F-B929-4555-B673-921FF3588AC3) and [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/ostmg&id=RACAD826) for information about SRVCTL commands

#### About a Shared Password File in a Disk Group

An individual password file for Oracle Database or Oracle ASM can reside on a designated Oracle ASM disk group. Having the password files reside on a single location accessible across the cluster reduces maintenance costs and situations where passwords become out of sync.

You can use a password file located on a disk group for authentication only if the Oracle ASM instance is running and the designated disk group is mounted. Otherwise, operating system authentication must be used to bootstrap the startup of the Oracle ASM instance and stack.

The `COMPATIBLE.ASM` disk group attribute must be set to `12.1` or higher for the disk group where the password is to be located. The `SYSASM` privilege is required to manage the Oracle ASM password file. The `SYSDBA` privilege on Oracle ASM is required to manage the database password file.

The shared password file in a disk group is managed by ASMCMD commands, the `ORAPWD` tool, and SRVCTL commands. `ORAPWD` supports the creation of password files on an Oracle ASM disk group. All other password file manipulation is performed with ASMCMD or SRVCTL commands.

Before running commands, such as `ORAPWD`, to create a password file, ensure that the `ORACLE_SID` and `ORACLE_HOME` environmental variables have been set properly. For example, before setting the password file for Oracle ASM, set the `ORACLE_SID` and `ORACLE_HOME` environmental variables to ensure that you can connect to the local Oracle ASM instance. For information about environmental variables and connecting to an Oracle ASM instance, refer to [Connecting To and Starting Up an Oracle ASM Instance](admin-asm-instance.md).

SRVCTL provides commands to manage a password file in a disk group, such as the following commands for updating and displaying the location of the password file:

```
$ srvctl modify asm -pwfile location
$ srvctl modify database -db dbname -pwfile location
$ srvctl config asm
```

#### Creating a Password File in a Disk Group

Note:

Do not use `orapwd` to create a new Oracle ASM password file when Oracle ASM is configured in a cluster. If the Oracle ASM password file is inaccessible in a cluster configuration, you must restore the password file using an available backup rather than create a new file. For articles about recreating a shared Oracle ASM password file in a cluster, such as document 1929673.1, refer to articles at [My Oracle Support](https://support.oracle.com/) ([`https://support.oracle.com`](https://support.oracle.com/)).

You can use `orapwd` to create a password file in a specified Oracle ASM disk group.

- To create an Oracle Database password file in a disk group from the existing password file on the file system, run `orapwd` with the `dbuniquename` switch. The `dbuniquename` switch specifies to create an Oracle Database password file for the database instance identified by `orcl`.
	1. Determine that the Oracle Database password file is currently located on the file system.
		```
		SQL>  SELECT file_name FROM V$PASSWORDFILE_INFO; 
		FILE_NAME 
		---------------------------------------------------------------------- 
		 /u01/app/oracle/product/19.1.0/db_home1/dbs/orapworcl
		```
		2. Run `orapwd` to move the password file to an Oracle ASM disk group.
		```
		$ orapwd file='+data/ORCL/orapwdb' dbuniquename='orcl'
		Enter password for SYS:
		```
		3. After the password file has been moved, update the password metadata cache with the `ALTER` `SYSTEM` statement and then confirm the new password file location.
		```
		SQL>  ALTER SYSTEM FLUSH PASSWORDFILE_METADATA_CACHE;
		System altered.
		SQL>  SELECT file_name FROM v$passwordfile_info; 
		FILE_NAME 
		---------------------------------------------------------------------- 
		+DATA/ORCL/orapwdb
		```
- To create an Oracle ASM password file in a disk group, run `orapwd` with the `asm` switch set to `y`.
	```
	$ orapwd file='+data/ASM/orapwasm' asm=y
	Enter password for SYS:
	```
- To create an Oracle ASM password file in an Oracle ASM disk group from an existing password file, run `orapwd` with the `input_file` switch and the `asm` switch set to `y`.
	```
	$ orapwd input_file='/oraclegrid/dbs/orapwasm' file='+data/ASM/orapwasm' asm=y
	Enter password for SYS:
	```

#### Backing Up and Restoring an Oracle ASM Password File in a Disk Group

You can make a backup of the Oracle ASM password file, and if the Oracle ASM password file is lost or the disk group becomes inaccessible, then you can restore the backup password file.

This section describes the steps to back up the Oracle ASM password file to a disk group and the steps to restore the Oracle ASM password file.

The source and target disk groups must have the disk group attribute `COMPATIBLE.ASM` set to `12.1` or higher.

1. Locate the password file using the ASMCMD `pwget` command.
	For example:
	```
	ASMCMD [+] > pwget --asm
	+DATA/orapwasm
	```
2. Back up the password file to another disk group with the `pwcopy` command.
	For example:
	```
	ASMCMD [+] > pwcopy +DATA/orapwasm +FRA/my_pwfile_backup
	```
	Using `pwcopy` without the `--asm` or `--dbuniquename` option does not change the current location of the password file. If necessary after the copy is made, you can set the current password file location with the `pwset` command.
3. Verify which password file is in the current location after making a backup with the `pwcopy` command.
	For example:
	```
	ASMCMD [+] > pwget --asm
	+DATA/orapwasm
	```
4. Verify the backup password file was created.
	For example:
	```
	ASMCMD [+] > ls +fra/my_pwfile_backup
	my_pwfile_backup
	```
5. To restore the Oracle ASM password file, you can use `pwset` or `pwcopy`.
	To restore the Oracle ASM password file from the backup and use the existing location, use the `pwset` command with the `--asm` option.
	For example:
	```
	ASMCMD [+] > pwset --asm +FRA/my_pwfile_backup
	```
	To restore the Oracle ASM password file from the backup to another disk group, use the `pwcopy` command with the `--asm` option.
	For example:
	```
	ASMCMD [+] > pwcopy --asm +FRA/my_pwfile_backup +DATA2/my_orapwasm
	```
	The `--asm` option with the `pwset` and `pwcopy` command sets the password location for the Oracle ASM instance.
6. Verify the location of the current password file with the `pwget` command if you have changed the location.
	For example:
	```
	ASMCMD [+] > pwget --asm
	+DATA2/my_orapwasm
	```
	If the location of the current password file displayed is not the expected location, then flush the password metadata cache to refresh the password file information.
	```
	SQL>  ALTER SYSTEM FLUSH PASSWORDFILE_METADATA_CACHE;
	System altered.
	```