---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/V-MYSTAT.html
tags:
  - oracle
  - 19c
  - reference
---

## 8.87 V$MYSTAT

`V$MYSTAT` contains statistics on the current session.

| Column | Datatype | Description |
| --- | --- | --- |
| `SID` | `NUMBER` | ID of the current session |
| `STATISTIC#` | `NUMBER` | Number of the statistic |
| `VALUE` | `NUMBER` | Value of the statistic |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |