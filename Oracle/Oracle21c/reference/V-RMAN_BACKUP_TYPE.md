---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-RMAN_BACKUP_TYPE.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.177 V$RMAN\_BACKUP\_TYPE

`V$RMAN_BACKUP_TYPE` displays information about RMAN backup types.

| Column | Datatype | Description |
| --- | --- | --- |
| `WEIGHT` | `NUMBER` | Used to set precedence order of different backup types in reports. |
| `INPUT_TYPE` | `VARCHAR2(13)` | Used to represent possible filters used in creating various reporting screens. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |