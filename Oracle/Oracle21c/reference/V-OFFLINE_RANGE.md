---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-OFFLINE_RANGE.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.99 V$OFFLINE\_RANGE

`V$OFFLINE_RANGE` displays datafile offline information from the control file.

Note that the last offline range of each datafile is kept in the `DATAFILE` record.

An offline range is created for a datafile when its tablespace is first altered to be `OFFLINE NORMAL` or `READ ONLY`, and then subsequently altered to be `ONLINE` or read/write. Note that no offline range is created if the datafile itself is altered to be `OFFLINE` or if the tablespace is altered to be `OFFLINE IMMEDIATE`.

See Also:

" [V$DATAFILE](V-DATAFILE.md) "

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
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |