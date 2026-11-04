---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ROLLBACK_SEGMENTS.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.321 ROLLBACK\_SEGMENTS

`ROLLBACK_SEGMENTS` allocates one or more rollback segments by name to this instance.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `ROLLBACK_SEGMENTS =`  `   (segment_name [, segment_name] ... )` |
| Default value | If you do not specify this parameter, the instance uses public rollback segments by default, unless the `UNDO_MANAGEMENT` initialization parameter is set to `AUTO`. In that case, the `ROLLBACK_SEGMENTS` parameter is ignored and automatic undo management is used. |
| Modifiable | No |
| Modifiable in a PDB | Yes |
| Range of values | Any rollback segment names listed in `DBA_ROLLBACK_SEGS` except `SYSTEM` |
| Basic | No |
| Oracle RAC | Multiple instances must have different values. |

If you set this parameter, the instance acquires all of the rollback segments named in this parameter, even if the number of rollback segments exceeds the minimum number required by the instance (calculated as `TRANSACTIONS / TRANSACTIONS_PER_ROLLBACK_SEGMENT`).

You cannot change the value of this parameter dynamically, but you can change its value and then restart the instance. Although this parameter usually specifies private rollback segments, it can also specify public rollback segments if they are not already in use.

To find the name, segment ID number, and status of each rollback segment in the database, query the data dictionary view `DBA_ROLLBACK_SEGS`.

When `UNDO_MANAGEMENT` is set to `AUTO`, `ROLLBACK_SEGMENTS` is ignored.

See Also:

- [Oracle Real Application Clusters Administration and Deployment Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=RACAD817) for information on setting this parameter in an Oracle RAC environment
- " [DBA\_ROLLBACK\_SEGS](DBA_ROLLBACK_SEGS.md) "