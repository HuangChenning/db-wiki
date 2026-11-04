---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/DB_LOST_WRITE_PROTECT.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.89 DB\_LOST\_WRITE\_PROTECT

`DB_LOST_WRITE_PROTECT` enables or disables lost write detection.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `DB_LOST_WRITE_PROTECT = { NONE \| TYPICAL \| FULL }` |
| Default value | `NONE` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Basic | No |
| Oracle RAC | In Oracle RAC instances, the parameter value is systemwide. |

A data block lost write occurs when an I/O subsystem acknowledges the completion of the block write, while in fact the write did not occur in the persistent storage.

When the parameter is set to `TYPICAL` on the primary database, the instance logs buffer cache reads for read/write tablespaces in the redo log, which is necessary for detection of lost writes.

When the parameter is set to `FULL` on the primary database, the instance logs reads for read-only tablespaces and read/write tablespaces.

When the parameter is set to `TYPICAL` or `FULL` on the standby database or on the primary database during media recovery, the instance performs lost write detection.

When the parameter is set to `NONE` on either the primary database or the standby database, no lost write detection functionality is enabled.