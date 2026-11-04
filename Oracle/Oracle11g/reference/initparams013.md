---
title: ASM_PREFERRED_READ_FAILURE_GROUPS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams013.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `ASM_PREFERRED_READ_FAILURE_GROUPS = <diskgroup_name>.<failure_group_name>, ...` |
| Default value | NULL |
| Modifiable | `ALTER SYSTEM` |
| Basic | No |
| Oracle RAC | The value is different on different nodes |

`ASM_PREFERRED_READ_FAILURE_GROUPS` specifies the failure groups that contain preferred read disks. Preferred disks are instance specific. This parameter is only valid in ASM instances.