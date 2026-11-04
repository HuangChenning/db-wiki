---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SEGSTAT.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.4 V$SEGSTAT

| Column | Datatype | Description |
| --- | --- | --- |
| `TS#` | `NUMBER` | Tablespace number |
| `OBJ#` | `NUMBER` | Dictionary object number |
| `DATAOBJ#` | `NUMBER` | Data object number |
| `STATISTIC_NAME` | `VARCHAR2(64)` | Name of the statistic |
| `STATISTIC#` | `NUMBER` | Statistic number |
| `VALUE` | `NUMBER` | Statistic value |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |