---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-GCR_LOG.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.247 V$GCR\_LOG

`V$GCR_LOG` provides information on the last 30 significant events that have occurred in GCR in the recent past.

| Column | Datatype | Description |
| --- | --- | --- |
| `INST_ID` | `NUMBER` | Instance identier |
| `ITERATION` | `NUMBER` | GCR internal iteration count |
| `TIME` | `TIMESTAMP(6)` | Timestamp of record |
| `TYPE` | `VARCHAR2(14)` | Type of record: - `METRIC` - `METRIC ENABLE` - `METRIC DISABLE` - `GLOBAL METRIC` - `ACTION RAN` - `RESET RAN` |
| `DESCRIPTION` | `VARCHAR2(40)` | Description of function |
| `RESULT` | `VARCHAR2(7)` | Result: - `OK` - `FAIL` |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include: - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data. |