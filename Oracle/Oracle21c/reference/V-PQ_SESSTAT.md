---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-PQ_SESSTAT.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.125 V$PQ\_SESSTAT

After you have run a query or DML operation, you can use the information derived from `V$PQ_SESSTAT` to view the number of worker processes used, and other information for the session and system.

| Column | Datatype | Description |
| --- | --- | --- |
| `STATISTIC` | `VARCHAR2(30)` | Name of the statistic:  - `Allocation Height` - Requested number of servers per instance - `Allocation Width` - Requested number of instances - `DDL Parallelized` - Number of DDL operations run in parallel - `DFO Trees` - Number of executed DFO trees - `DML Parallelized` - Number of DML operations run in parallel - `DOP` - Degree of parallelism used for the last statement - `Distr Msgs Recv'd` - Number of remote (inter-instance) messages received - `Distr Msgs Sent` - Number of remote (inter-instance) messages sent - `Local Msgs Recv'd` - Number of local (intra-instance) messages received - `Local Msgs Sent` - Number of local (intra-instance) messages sent - `Queries Parallelized` - Number of queries run in parallel - `Server Threads` - Number of PX servers used - `Slave Sets` - Total number of worker sets used for the last statement. For multiple parallelizers in the parallel plan, it is the cumulative count. |
| `LAST_QUERY` | `NUMBER` | Value of the statistic for the last operation |
| `SESSION_TOTAL` | `NUMBER` | Value of the statistic for the entire session to this point in time.  The value of the statistic for the entire session to this point in time is not maintained for the `DOP`, `Server Threads`, `Allocation Height`, `Allocation Width`, and `Slave Set` statistics. |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |