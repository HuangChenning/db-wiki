---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-PQ_SYSSTAT.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.127 V$PQ\_SYSSTAT

`V$PQ_SYSSTAT` lists system statistics for parallel queries.

After you have run a query or DML operation, you can use the information derived from `V$PQ_SYSSTAT` to view the number of PX (Parallel Execution) servers used, and other information for the system.

| Column | Datatype | Description |
| --- | --- | --- |
| `STATISTIC` | `VARCHAR2(30)` | Name of the statistic:  - `DDL Initiated` - Total number of parallel DDL operations that were initiated - `DFO Trees` - Total number of DFO trees executed on this instance - `DML Initiated` - Total number of parallel DML operations that were initiated - `Distr Msgs Recv'd` - Total number of remote (inter-instance) messages received on this instance - `Distr Msgs Sent` - Total number of remote (inter-instance) messages sent on this instance - `Local Msgs Recv'd` - Total number of remote (inter-instance) messages received on this instance - `Local Msgs Sent` - Total number of local (intra-instance) messages sent on this instance - `Queries Initiated` - Total number of parallel queries initiated on this instance - `Queries Queued` - Total number of queued queries on this instance - `Server Sessions` - Total number of operations executed in all PX servers on this instance - `Servers Busy` - Number of currently busy PX servers on this instance - `Servers Cleaned Up` - Total number of PX servers on this instance cleaned up due to process death - `Servers Highwater` - Number of active PX servers on this instance that have partaken in >= 1 operation so far - `Servers Idle` - Number of currently idle PX servers on this instance - `Servers Shutdown` - Total number of PX servers shutdown on this instance - `Servers Started` - Total number of PX servers started on this instance - `Sessions Active` - Total number of active sessions on this instance |
| `VALUE` | `NUMBER` | Value of the statistic |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |