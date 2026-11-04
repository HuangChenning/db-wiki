---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ARCHIVE.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.36 V$ARCHIVE

`V$ARCHIVE` displays information about redo log files in need of archiving.

Each row displays information for one thread. This information is also available in `V$LOG`. Oracle recommends that you use `V$LOG`.

See Also:

" [V$LOG](V-LOG.md) "

| Column | Datatype | Description |
| --- | --- | --- |
| `GROUP#` | `NUMBER` | Log file group number |
| `THREAD#` | `NUMBER` | Log file thread number |
| `SEQUENCE#` | `NUMBER` | Log file sequence number |
| `ISCURRENT` | `VARCHAR2(3)` | This is the current online redo log |
| `CURRENT` | `VARCHAR2(3)` | This column is obsolete and maintained for backward compatibility. The value of this column is always equal to the value in `ISCURRENT`. |
| `FIRST_CHANGE#` | `NUMBER` | First SCN stored in the current log |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |