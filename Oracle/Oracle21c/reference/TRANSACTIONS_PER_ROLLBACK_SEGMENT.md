---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/TRANSACTIONS_PER_ROLLBACK_SEGMENT.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.370 TRANSACTIONS\_PER\_ROLLBACK\_SEGMENT

`TRANSACTIONS_PER_ROLLBACK_SEGMENT` specifies the number of concurrent transactions you expect each rollback segment to have to handle.

| Property | Description |
| --- | --- |
| Parameter type | Integer |
| Default value | `5` |
| Modifiable | No |
| Modifiable in a PDB | No |
| Range of values | 1 to operating system-dependent |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |

The minimum number of rollback segments acquired at startup is `TRANSACTIONS` divided by the value for this parameter. For example, if `TRANSACTIONS` is 101 and this parameter is 10, then the minimum number of rollback segments acquired would be the ratio 101/10, rounded up to 11.

You can acquire more rollback segments by naming them in the parameter `ROLLBACK_SEGMENTS`.

See Also:

Your operating system-specific Oracle documentation for the range of values for this parameter.