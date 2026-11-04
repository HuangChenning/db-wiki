---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/ASM_DISKGROUPS.html
tags:
  - oracle
  - 12c
  - reference
---

`ASM_DISKGROUPS` specifies a list of disk group names that an Oracle ASM instance mounts when the `ALTER DISKGROUP ALL MOUNT` statement is issued.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `ASM_DISKGROUPS = ` `diskgroup` `  [,  ``diskgroup` ` ] ...` |
| Default value | There is no default value. |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | Comma-separated list of strings, up to 30 characters |
| Oracle RAC | Multiple instances can have different values. |

Note:

This parameter may only be specified in an Oracle Automatic Storage Management (Oracle ASM) instance.

The Oracle ASM instance startup process executes `ALTER DISKGROUP ALL MOUNT` unless the `NOMOUNT` startup option is specified.

Oracle ASM automatically adds a disk group to this parameter when the disk group is successfully created or mounted, and automatically removes a disk group from this parameter when the disk group is dropped or dismounted.

Issuing the `ALTER DISKGROUP...ALL MOUNT` or `ALTER DISKGROUP...ALL DISMOUNT` command does not affect the value of this parameter.

Supporting Up to 511 Disk Groups for an Oracle ASM Instance

In Oracle Database 12c Release 1 or later, Oracle ASM configurations support up to 511 disk groups. Oracle ASM configurations with Oracle Database releases before 12c Release 1 can only support up to 63 disk groups.