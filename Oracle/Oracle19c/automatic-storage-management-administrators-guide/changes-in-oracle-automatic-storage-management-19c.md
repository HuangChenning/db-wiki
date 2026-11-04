---
title: "Oracle Automatic Storage Management Administrator's Guide"
book: "Oracle Automatic Storage Management Administrator's Guide"
doc_id: F34287-08
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/ostmg/changes-in-this-release-for-oracle-automatic-storage-management-administrators-guide/changes-in-oracle-automatic-storage-management-19c.html
tags:
  - oracle
  - 19c
  - automatic-storage-management-administrators-guide
---

## Changes in Oracle Automatic Storage Management 19c

The following are changes in Oracle Automatic Storage Management 19c.

## New Features

These are the new features for Oracle Automatic Storage Management 19c.

- New Permission Requirements for Oracle ASM File Group Operations
	Moving a file group to a new quota group now requires only the `SYSASM` privilege. File group template usage now requires an Oracle ASM File Access Control check. Moving a file between file groups now requires an Oracle ASM File Access Control check.
	The new permission requirements provide enhanced security, as well as quota management.
- SRVCTL command enhancements
	SRVCTL provides enhanced commands to manage Oracle ASM network resources.
	See also
	- [About Administering Oracle ASM Instances with Server Control Utility](administering-oracle-asm-instances.md) for a summary of Oracle ASM and Oracle ACFS tasks that can be performed with SRVCTL
	- [SRVCTL and CRSCTL Commands to Administer Oracle Flex ASM](managing-oracle-flex-asm.md) for information about SRVCTL commands to manage Oracle Flex ASM resources
	- [Oracle Clusterware Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19&id=CWADD-GUID-1DCA9E3F-B929-4555-B673-921FF3588AC3) and [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19&id=RACAD-GUID-3ED4DBCE-A148-462B-8A79-534A3F0D6E7D) for information about SRVCTL commands
- Flushing the password file metadata
	After a change has been made to the location of the password file, the following SQL statement should be run to flush the password file metadata cache:
	```
	SQL> ALTER SYSTEM FLUSH PASSWORDFILE_METADATA_CACHE
	```
	Changes to the location of the password file could be introduced by running `orapwd`, or the ASMCMD `pwcopy`, `pwcreate`, `pwdelete`, `pwmove`, or `pwset` command. If the `V$PASSWORDFILE_INFO` does not display the correct password file location after a change, then flush the password file metadata cache to force a refresh of the password file location.
	See also
	- [Managing a Shared Password File in a Disk Group](administering-oracle-asm-instances.md) for information about managing a password file in a disk group.
	- [ASMCMD Instance Management Commands](managing-oracle-asm-with-asmcmd.md) for information about the ASMCMD commands for managing the password file.
- New and updated ASMCMD commands
	- The `password` option with the ASMCMD `pwcreate` command is now optional.
		New options have been added for to force a delete of the old password file and create a new password file (`-f`) and to specify the format of the password file (`--format`).
		- The new ASMCMD `setsparseparent` command sets the parent for a sparse child file.
		- The new ASMCMD `mvfile` command moves a file to the specified file group in the same disk group where the file is stored.
	See also
	- [pwcreate](managing-oracle-asm-with-asmcmd.md)
	- [setsparseparent](managing-oracle-asm-with-asmcmd.md)
	- [mvfile](managing-oracle-asm-with-asmcmd.md)
- Support for Parity Protected Files
	The `REDUNDANCY` file type property specifies the redundancy for a file group. The `PARITY` value specifies single parity and the `DOUBLE` value specifies double parity. Parity settings are intended for write-once files, such as archive logs and backup sets.
	See also
	- [About Oracle ASM File Group Properties](administering-oracle-asm-disk-groups.md) for information about the Oracle ASM file group `REDUNDANCY` property

## Deprecated Features

These are the deprecated features for Oracle ASM 19c.

- Deprecation of the `password` option with the ASMCMD `pwcreate` command

## Desupported Features

These are the desupported features for Oracle ASM 19c.

- Starting with Oracle Database 19c, leaf nodes are desupported as part of Oracle Flex Cluster architecture.
	See also
	- [Oracle Database Upgrade Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/ostmg&id=UPGRD)