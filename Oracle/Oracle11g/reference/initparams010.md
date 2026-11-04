---
title: ASM_DISKGROUPS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams010.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `ASM_DISKGROUPS =` `diskgroup` `[,` `diskgroup` `] ...` |
| Default value | There is no default value. |
| Modifiable | `ALTER SYSTEM` |
| Range of values | Comma-separated list of strings, up to 30 characters |
| Oracle RAC | Multiple instances can have different values. |

Note:

This parameter may only be specified in an Automatic Storage Management instance.

`ASM_DISKGROUPS` specifies a list of names of disk groups to be mounted by an Automatic Storage Management instance at instance startup. Oracle ignores the value that you set for `ASM_DISKGROUPS` when you specify the `NOMOUNT` option at startup or when a `ALTER DISKGROUP ALL MOUNT` statement is issued.

Automatic Storage Management (ASM) automatically adds a disk group to this parameter when the disk group is successfully created or mounted, and automatically removes a disk group from this parameter when the disk group is dropped or dismounted.

Issuing the `ALTER DISKGROUP...ALL MOUNT` or `ALTER DISKGROUP...ALL DISMOUNT` command does not affect the value of this parameter.