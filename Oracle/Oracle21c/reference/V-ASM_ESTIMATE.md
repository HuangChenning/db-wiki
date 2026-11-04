---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-ASM_ESTIMATE.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.61 V$ASM\_ESTIMATE

`V$ASM_ESTIMATE` displays an estimate of the work involved in execution plans for Oracle Automatic Storage Management (Oracle ASM) disk group rebalance and resync operations.

| Column | Datatype | Description |
| --- | --- | --- |
| `GROUP_NUMBER` | `NUMBER` | Oracle ASM disk group number |
| `STATEMENT_ID` | `VARCHAR2(30)` | Value of the optional STATEMENT\_ID parameter specified in the EXPLAIN WORK statement |
| `TIMESTAMP` | `DATE` | Date and time when the EXPLAIN WORK statement was issued |
| `EST_WORK` | `NUMBER` | Estimated number of Allocation Units that have to be moved by the operation |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data  For this view, the value is always `0`. |

See Also:

[Oracle Automatic Storage Management Administrator's Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=OSTMG10030) for additional information about using views to display Oracle ASM information