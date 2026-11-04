---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ASM_DISKGROUPS.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.18 ASM\_DISKGROUPS

`ASM_DISKGROUPS` specifies a list of disk group names that an Oracle ASM instance mounts at startup when the `ALTER DISKGROUP ALL MOUNT` statement is issued.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `ASM_DISKGROUPS = ` `diskgroup` `  [,  ``diskgroup` ` ] ...` |
| Default value | There is no default value. |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | Comma-separated list of strings, up to 30 characters |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |

Note:

This parameter may only be specified in an Oracle Automatic Storage Management (Oracle ASM) instance.

The Oracle ASM instance startup process executes `ALTER DISKGROUP ALL MOUNT` unless the `NOMOUNT` startup option is specified.

The `ASM_DISKGROUPS` parameter is dynamic. If you are using a server parameter file (SPFILE), then you do not have to manually alter the value of `ASM_DISKGROUPS` in most situations. Oracle ASM automatically adds a disk group to the parameter when the disk group is successfully created or mounted. Oracle ASM also automatically removes a disk group from the parameter when the disk group is dropped. However, the SPFILE is not updated on a manual dismount.

Issuing the `ALTER DISKGROUP...ALL MOUNT` or `ALTER DISKGROUP...ALL DISMOUNT` command does not affect the value of this parameter.

Supporting Up to 511 Disk Groups for an Oracle ASM Instance

In Oracle Database 12c Release 1 or later, Oracle ASM configurations support up to 511 disk groups. Oracle ASM configurations with Oracle Database releases before 12c Release 1 can only support up to 63 disk groups.