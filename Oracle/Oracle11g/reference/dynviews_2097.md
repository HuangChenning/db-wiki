---
title: "V$PQ_SESSTAT"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2097.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$PQ_SESSTAT` lists session statistics for parallel queries. After you have run a query or DML operation, you can use the information derived from `V$PQ_SESSTAT` to view the number of slave processes used, and other information for the session and system.

| Column | Datatype | Description |
| --- | --- | --- |
| `STATISTIC` | `VARCHAR2(30)` | Name of the statistic: - `Queries Parallelized` - Number of queries run in parallel - `DDL Parallelized` - Number of DDL operations run in parallel - `DML Parallelized` - Number of DML operations run in parallel - `DFO Trees` - Number of executed DFO trees - `Server Threads` - Number of PX servers used - `Allocation Height` - Requested number of servers per instance - `Allocation Width` - Requested number of instances - `Local Msgs Sent` - Number of local (intra-instance) messages sent - `Distr Msgs Sent` - Number of remote (inter-instance) messages sent - `Local Msgs Recv'd` - Number of local (intra-instance) messages received - `Distr Msgs Recv'd` - Number of remote (inter-instance) messages received |
| `LAST_QUERY` | `NUMBER` | Value of the statistic for the last operation |
| `SESSION_TOTAL` | `NUMBER` | Value of the statistic for the entire session to this point in time |