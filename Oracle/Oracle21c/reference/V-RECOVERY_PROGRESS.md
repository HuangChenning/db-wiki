---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-RECOVERY_PROGRESS.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.161 V$RECOVERY\_PROGRESS

`V$RECOVERY_PROGRESS` can be used to track database recovery operations to ensure that they are not stalled, and also to estimate the time required to complete the operation in progress.

On non-coordinator instances, `V$RECOVERY_PROGRESS` is not populated.

On the coordinator instance (the instance where MRP0 was started to start recovery), `V$RECOVERY_PROGRESS` has the same set of rows as before, except the following rows in the `ITEM` column are always 0 (not used) with Multi-Instance Redo Apply:

- Active Apply
- Maximum Apply Rate
- Apply Time per Log
- Checkpoint Time per Log
- Recovery ID

`V$RECOVERY_PROGRESS` is a subview of `V$SESSION_LONGOPS`.

Note:

This view is populated on the instance where the MRP0 process is started if recovery is running in Multi-Instance Redo Apply mode. Not all the columns will be populated.

| Column | Datatype | Description |
| --- | --- | --- |
| `START_TIME` | `DATE` | Start time of the recovery operation |
| `TYPE` | `VARCHAR2(64)` | Type of recovery operation being performed:  - `CRASH RECOVERY` - `INSTANCE RECOVERY` - `MEDIA RECOVERY` |
| `ITEM` | `VARCHAR2(32)` | Item being measured.  When TYPE is CRASH RECOVERY or INSTANCE RECOVERY, the possible values are:  - `Log Files` - `Redo Blocks`  When TYPE is MEDIA RECOVERY, the possible values are:  - `Active Apply Rate` - `Average Apply Rate` - `Maximum Apply Rate` - `Redo Applied` - `Log Files` - `Last Applied Redo` - `Active Time` - `Elapsed Time` - `Apply Time per Log` - `Checkpoint Time per Log` - `Standby Apply Lag` - `Recovery ID` |
| `UNITS` | `VARCHAR2(32)` | The units of measurement for each item |
| `SOFAR` | `NUMBER` | Amount of work done so far |
| `TOTAL` | `NUMBER` | Total amount of work expected |
| `TIMESTAMP` | `DATE` | Timestamp of the last redo record applied |