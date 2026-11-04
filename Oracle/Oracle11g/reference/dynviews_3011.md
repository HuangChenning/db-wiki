---
title: "V$SERVICEMETRIC_HISTORY"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3011.htm
tags:
  - oracle
  - 11g
  - reference
---

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