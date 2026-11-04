---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ASM_POWER_LIMIT.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.21 ASM\_POWER\_LIMIT

`ASM_POWER_LIMIT` specifies the maximum power on an Oracle ASM instance for disk rebalancing.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `1` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Range of values | `0` to `11` <sup>Foot 1</sup> |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |

<sup>Footnote 1</sup>

Beginning with Oracle Database 11g Release 2 (11.2.0.2), if the `COMPATIBLE`.`ASM` disk group attribute is set to 11.2.0.2 or higher, then the range of values is 0 to 1024.

Note:

- This parameter may only be specified in an Oracle Automatic Storage Management (Oracle ASM) instance.
- In an Oracle Exadata or Oracle Data Appliance environment, you cannot set this parameter to 0.

The higher the limit, the faster rebalancing will complete. Lower values will take longer, but consume fewer processing and I/O resources.

If the `POWER` clause of a rebalance operation is not specified, then the default power will be the value of `ASM_POWER_LIMIT`.

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=OSTMG10144) for more information about using this parameter