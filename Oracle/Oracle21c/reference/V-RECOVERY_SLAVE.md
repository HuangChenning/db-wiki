---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-RECOVERY_SLAVE.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.162 V$RECOVERY\_SLAVE

`V$RECOVERY_SLAVE` is used to track database media recovery processes to monitor their performance statistics and analyze a media recovery session.

| Column | Datatype | Description |
| --- | --- | --- |
| `START_TIME` | `DATE` | Start time of the recovery process |
| `TYPE` | `VARCHAR2(64)` | Type of recovery process being performed:  - `MEDIA RECOVERY Apply SLAVE` - `MEDIA RECOVERY Merge Slave` - `SERIAL MEDIA RECOVERY` |
| `ITEM` | `VARCHAR2(32)` | Item being measured.  When `TYPE` is `MEDIA RECOVERY Apply SLAVE`, the possible values are:  - `Recovery ID` - `Process ID` - `Number of Redo Cache Full` - `Number of Redo Cache Copy` - `Number of CV Cached` - `CV Applied OK` - `CV Applied Stuck` - `CV Applied Repair` - `CV Applied Corrupt` - `CV Applied Ckpt` - `CV Applied Reapplied` - `Total CV Processed Size` - `Total CV Applied` - `Number of Buffer Cache Full` - `Number of Buffer Retries` - `Number of Max Reads Issued` - `Number of Unrcv Condition` - `Number of Influx Buffer Flushed` - `Number of Reap Request` - `Number of Reap Wait IO` - `Number of Reap No Buffer` - `Number of Wait All Read` - `Number of Buffer Pinged` - `Buffer Ping Time` - `Read Issue Time` - `Number of Read Request Issued`  When `TYPE` is `MEDIA RECOVERY Merge Slave`, the possible values are:  - `Recovery ID` - `Process ID` - `Number of Redo Cache Full` - `Number of Redo Cache Copy` - `Number of CV Cached` - `Total Redo Read Bytes` - `Total CV Parsed`  When `TYPE` is `SERIAL MEDIA RECOVERY`, the possible values include values from the other two `TYPE` s. |
| `UNITS` | `VARCHAR2(32)` | The units of measurement for each item |
| `SOFAR` | `NUMBER` | Amount of work done so far |
| `TOTAL` | `NUMBER` | Total amount of work expected |