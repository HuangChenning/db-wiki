---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-HANG_STATISTICS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.275 V$HANG\_STATISTICS

`V$HANG_STATISTICS` displays statistics about hangs found on the cluster.

| Column | Datatype | Description |
| --- | --- | --- |
| `STATISTIC#` | `NUMBER` | Statistic number |
| `NAME` | `VARCHAR2(45)` | Name of the statistic |
| `VALUE` | `NUMBER` | Value associated with the statistic |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |