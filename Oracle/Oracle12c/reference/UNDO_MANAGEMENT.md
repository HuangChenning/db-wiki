---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/UNDO_MANAGEMENT.html
tags:
  - oracle
  - 12c
  - reference
---

`UNDO_MANAGEMENT` specifies which undo space management mode the system should use.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `UNDO_MANAGEMENT = { MANUAL \| AUTO }` |
| Default value | `AUTO` |
| Modifiable | No |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | Multiple instances must have the same value. |

When `UNDO_MANAGEMENT` is set to `AUTO`, the instance starts in automatic undo management mode. In manual undo management mode, undo space is allocated externally as rollback segments.

Note:

In a CDB, the `UNDO_MANAGEMENT` initialization parameter must be set to `AUTO`, and an undo tablespace is required to be created to manage the undo data.

See Also:

- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ADMIN11110) for more information about this parameter
- [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ADMIN013) for more information about managing undo data