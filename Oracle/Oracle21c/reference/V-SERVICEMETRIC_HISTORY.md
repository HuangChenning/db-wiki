---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SERVICEMETRIC_HISTORY.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.12 V$SERVICEMETRIC\_HISTORY

`V$SERVICEMETRIC_HISTORY` displays a recent history of the metric values measured in predefined time interval periods for services executing inside the database. Service metrics are measured in 5-second and 1-minute intervals.

| Column | Datatype | Description |
| --- | --- | --- |
| `BEGIN_TIME` | `DATE` | Begin timestamp for the interval period |
| `END_TIME` | `DATE` | End timestamp for the interval period |
| `INTSIZE_CSEC` | `NUMBER` | Interval size (in hundredths of a second) |
| `GROUP_ID` | `NUMBER` | Group ID for the service metric group |
| `SERVICE_NAME_HASH` | `NUMBER` | Service name hash |
| `SERVICE_NAME` | `VARCHAR2(64)` | Service name |
| `CTMHASH` | `NUMBER` | Service create timestamp hash value |
| `ELAPSEDPERCALL` | `NUMBER` | Elapsed time per call (in microseconds). This column is deprecated in favor of the `DBTIMEPERCALL` column. |
| `CPUPERCALL` | `NUMBER` | CPU time per call (in microseconds) |
| `DBTIMEPERCALL` | `NUMBER` | Elapsed time per call (in microseconds) |
| `CALLSPERSEC` | `NUMBER` | Number of user calls per second |
| `DBTIMEPERSEC` | `NUMBER` | Database time per second |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |