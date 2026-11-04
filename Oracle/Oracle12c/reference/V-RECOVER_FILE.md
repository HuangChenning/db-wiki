---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-RECOVER_FILE.html
tags:
  - oracle
  - 12c
  - reference
---

`V$RECOVER_FILE` displays the status of files needing media recovery.

| Column | Datatype | Description |
| --- | --- | --- |
| `FILE#` | `NUMBER` | File identifier number |
| `ONLINE` | `VARCHAR2(7)` | This column is obsolete and maintained for backward compatibility. The value of this column is always equal to the value in `ONLINE_STATUS`. |
| `ONLINE_STATUS` | `VARCHAR2(7)` | Online status (`ONLINE`, `OFFLINE`) |
| `ERROR` | `VARCHAR2(18)` | Why the file must be recovered: NULL if reason unknown, or `OFFLINE NORMAL` if recovery not needed |
| `CHANGE#` | `NUMBER` | SCN where recovery must start |
| `TIME` | `DATE` | Time of SCN when recovery must start |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |