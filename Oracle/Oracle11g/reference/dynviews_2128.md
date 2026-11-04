---
title: "V$RECOVERY_PROGRESS"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2128.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$RECOVERY_PROGRESS` can be used to track database recovery operations to ensure that they are not stalled, and also to estimate the time required to complete the operation in progress.

`V$RECOVERY_PROGRESS` is a subview of `V$SESSION_LONGOPS`.

| Column | Datatype | Description |
| --- | --- | --- |
| `START_TIME` | `DATE` | Start time of the recovery operation |
| `TYPE` | `VARCHAR2(64)` | Type of recovery operation being performed: |
| `ITEM` | `VARCHAR2(32)` | Item being measured.  When `TYPE` is `CRASH RECOVERY` or `INSTANCE RECOVERY`, the possible values are:  - `Log files` - `Redo blocks`  When `TYPE` is `MEDIA RECOVERY`, the possible values are:  - `Active Apply Rate` - `Average Apply Rate` - `Maximum Apply Rate` - `Redo Applied` - `Log Files` - `Last Applied Redo` - `Active Time` - `Elapsed Time` - `Apply Time per Log` - `Checkpoint Time per Log` - `Standby Apply Lag` |
| `UNITS` | `VARCHAR2(32)` | The units of measurement for each item |
| `SOFAR` | `NUMBER` | Amount of work done so far |
| `TOTAL` | `NUMBER` | Total amount of work expected |
| `TIMESTAMP` | `DATE` | Timestamp of the last redo record applied |
| `COMMENTS` | `VARCHAR2(208)` | Miscellaneous notes; currently displays the SCN for the last applied redo |