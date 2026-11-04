---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ASM_DISKSTRING.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.19 ASM\_DISKSTRING

`ASM_DISKSTRING` specifies an operating system-dependent value used by Oracle ASM to limit the set of disks considered for discovery.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `ASM_DISKSTRING = ` `discovery_string` `  [,  ``discovery_string` ` ] ...` |
| Default value | The null string; Oracle Automatic Storage Management discovery finds all disks in an operating system-specific location to which the Oracle Automatic Storage Management instance has read/write access. |
| Modifiable | `ALTER SESSION, ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. Different nodes might see the same disks under different names; however, each instance must be able to use its `ASM_DISKSTRING` to discover the same physical media as the other nodes in the cluster. |

Note:

This parameter may only be specified in an Oracle Automatic Storage Management (Oracle ASM) instance.

When a new disk is added to a disk group, each Oracle ASM instance that has the disk group mounted must be able to discover the new disk using the value of `ASM_DISKSTRING`.

In most cases, the default value will be sufficient. Using a more restrictive value may reduce the time required for Oracle ASM to perform discovery, and thus improve disk group mount time or the time for adding a disk to a disk group. A "?" at the beginning of the string gets expanded to the Oracle home directory. Depending on the operating system, wildcard characters can be used. It may be necessary to dynamically change `ASM_DISKSTRING` before adding a disk so that the new disk will be discovered.

An attempt to dynamically modify `ASM_DISKSTRING` will be rejected and the old value retained if the new value cannot be used to discover a disk that is in a disk group that is already mounted.

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=OSTMG10142) for more information and examples of using this parameter