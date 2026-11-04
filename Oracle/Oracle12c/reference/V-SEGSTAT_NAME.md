---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/V-SEGSTAT_NAME.html
tags:
  - oracle
  - 12c
  - reference
---

`V$SEGSTAT_NAME` displays information about segment-level statistics properties.

| Column | Datatype | Description |
| --- | --- | --- |
| `STATISTIC#` | `NUMBER` | Statistic number |
| `NAME` | `VARCHAR2(64)` | Name of the statistic |
| `SAMPLED` | `VARCHAR2(3)` | Indicates whether the statistic was collected by sampling (`YES`) or not (`NO`) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |