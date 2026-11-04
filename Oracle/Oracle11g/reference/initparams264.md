---
title: UNDO_MANAGEMENT
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams264.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `UNDO_MANAGEMENT = { MANUAL \| AUTO }` |
| Default value | `AUTO` |
| Modifiable | No |
| Basic | No |
| Oracle RAC | Multiple instances must have the same value. |

`UNDO_MANAGEMENT` specifies which undo space management mode the system should use. When set to `AUTO`, the instance starts in automatic undo management mode. In manual undo management mode, undo space is allocated externally as rollback segments.