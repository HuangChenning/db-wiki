---
title: DB_LOST_WRITE_PROTECT
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams063.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `DB_LOST_WRITE_PROTECT = { NONE \| TYPICAL \| FULL }` |
| Default value | `NONE` |
| Modifiable | `ALTER SYSTEM` |
| Basic | No |
| Oracle RAC | In Oracle RAC instances, the parameter value is system-wide. |

`DB_LOST_WRITE_PROTECT` enables or disables lost write detection. A data block lost write occurs when an I/O subsystem acknowledges the completion of the block write, while in fact the write did not occur in the persistent storage.

When the parameter is set to `TYPICAL` on the primary database, the instance logs buffer cache reads for read-write tablespaces in the redo log, which is necessary for detection of lost writes.

When the parameter is set to `FULL` on the primary database, the instance logs reads for read-only tablespaces as well as read-write tablespaces.

When the parameter is set to `TYPICAL` or `FULL` on the standby database or on the primary database during media recovery, the instance performs lost write detection.

When the parameter is set to `NONE` on either the primary database or the standby database, no lost write detection functionality is enabled.