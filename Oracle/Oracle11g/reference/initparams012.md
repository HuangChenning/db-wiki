---
title: ASM_POWER_LIMIT
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams012.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `1` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Range of values | `0` to `11` <sup>Foot 1</sup> |
| Oracle RAC | Multiple instances can have different values. |

<sup>Footnote 1</sup> Beginning with Oracle Database 11g Release 2 (11.2.0.2), if the `COMPATIBLE`.`ASM` disk group attribute is set to 11.2.0.2 or higher, then the range of values is 0 to 1024.

Note:

This parameter may only be specified in an Automatic Storage Management instance.

`ASM_POWER_LIMIT` specifies the maximum power on an Automatic Storage Management instance for disk rebalancing. The higher the limit, the faster rebalancing will complete. Lower values will take longer, but consume fewer processing and I/O resources.

If the `POWER` clause of a rebalance operation is not specified, then the default power will be the value of `ASM_POWER_LIMIT`.