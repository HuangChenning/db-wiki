---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/V-IO_CALIBRATION_STATUS.html
tags:
  - oracle
  - 19c
  - reference
---

## 8.12 V$IO\_CALIBRATION\_STATUS

`V$IO_CALIBRATION_STATUS` displays the status of I/O calibration in the instance.

| Column | Datatype | Description |
| --- | --- | --- |
| `STATUS` | `VARCHAR2(13)` | Calibration status:  - `IN PROGRESS` - Calibration in Progress (Results from a previous calibration run are displayed, if available) - `READY` Results are ready and available from an earlier run - `NOT AVAILABLE` Calibration results are not available |
| `CALIBRATION_TIME` | `TIMESTAMP(3)` | End time of the last calibration run |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |