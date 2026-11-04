---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/DB_LOST_WRITE_PROTECT.html
tags:
  - oracle
  - 19c
  - reference
---

## 1.90 DB\_LOST\_WRITE\_PROTECT

`DB_LOST_WRITE_PROTECT` enables or disables lost write detection.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `DB_LOST_WRITE_PROTECT = { AUTO \| TYPICAL \| FULL                                     \| NONE }` |
| Default value | Starting with Oracle Database 19c, Release Update 19.26: `AUTO`  Oracle Database 19c, Release Update 19.25 or earlier: `NONE` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Basic | No |
| Oracle RAC | In Oracle RAC instances, the parameter value is systemwide. |

A data block lost write occurs when an I/O subsystem acknowledges the completion of the block write, while in fact the write did not occur in the persistent storage.

- `AUTO`
	This setting is available starting with Oracle Database 19c, Release Update 19.26. When this parameter is set to `AUTO` on a primary database, the instance automatically decides whether it logs buffer cache reads in the redo log or not, depending on the status of the standby databases. Specifically, the primary database only logs buffer cache reads if physical standby databases with real time redo apply exist.
	When this parameter is set to `AUTO` on a standby database, the instance will automatically decide whether it incurs additional performance overhead to perform lost write detection or not, depending on whether apply is keeping up. If apply lag is beyond the reasonable threshold, the standby database will skip lost write protection temporarily until redo apply catches up with primary again, to ensure the lowest Data Guard role transition timings.
	The reasonable threshold is determined as follows:
	- If Fast Start Failover (FSFO) is configured through Data Guard Broker, based on apply lag threshold, then the threshold is the lesser of 60 seconds and two-thirds of the FSFO apply lag threshold.
		- Otherwise, the threshold is 60 seconds.
- `TYPICAL`
	When this parameter is set to `TYPICAL` on a primary database, the instance logs buffer cache reads for read/write tablespaces in the redo log, which is necessary for detection of lost writes.
	When this parameter is set to `TYPICAL` on a standby database, or on a primary database during media recovery, the instance performs lost write detection, regardless of higher redo apply lags that may impact Data Guard role transition timings.
- `FULL`
	When this parameter is set to `FULL` on a primary database, the instance logs reads for read-only tablespaces and read/write tablespaces.
	When this parameter is set to `FULL` on a standby database, or on a primary database during media recovery, the instance performs lost write detection.
- `NONE`
	When this parameter is set to `NONE` on either a primary database or a standby database, no lost write detection functionality is enabled.