---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-GCR_STATUS.html
tags:
  - oracle
  - 12c
  - reference
---

`V$GCR_STATUS` provides information on the current GCR status, what metrics ran and their result. It records the last 100 events.

| Column | Datatype | Description |
| --- | --- | --- |
| `INST_ID` | `NUMBER` | Instance identifier |
| `ITERATION` | `NUMBER` | GCR internal iteration count |
| `TIME` | `TIMESTAMP(6)` | Timestamp of record |
| `TYPE` | `VARCHAR2(14)` | Type of record: - `METRIC` - `GLOBAL METRIC` - `ACTION RAN` - `RESET RAN` |
| `DESCRIPTION` | `VARCHAR2(40)` | Description of function |
| `RESULT` | `VARCHAR2(7)` | Result: - `OK` - `FAIL` |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include: - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data. |

Note:

This view is available starting with Oracle Database 12c Release 2 (12.2.0.1).