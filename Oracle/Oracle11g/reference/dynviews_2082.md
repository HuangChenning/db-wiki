---
title: "V$OFFLINE_RANGE"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2082.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$OFFLINE_RANGE` displays datafile offline information from the control file. Note that the last offline range of each datafile is kept in the `DATAFILE` record.

An offline range is created for a datafile when its tablespace is first altered to be `OFFLINE NORMAL` or `READ ONLY`, and then subsequently altered to be `ONLINE` or read/write. Note that no offline range is created if the datafile itself is altered to be `OFFLINE` or if the tablespace is altered to be `OFFLINE IMMEDIATE`.

See Also:

["V$DATAFILE"](dynviews_1100.md)

| Column | Datatype | Description |
| --- | --- | --- |
| `RECID` | `NUMBER` | Record ID |
| `STAMP` | `NUMBER` | Record stamp |
| `FILE#` | `NUMBER` | Datafile number |
| `OFFLINE_CHANGE#` | `NUMBER` | SCN at which offlined |
| `ONLINE_CHANGE#` | `NUMBER` | SCN at which onlined |
| `ONLINE_TIME` | `DATE` | Time of offline SCN |
| `RESETLOGS_CHANGE#` | `NUMBER` | Resetlogs change number of the record |
| `RESETLOGS_TIME` | `DATE` | Resetlogs timestamp of the record |