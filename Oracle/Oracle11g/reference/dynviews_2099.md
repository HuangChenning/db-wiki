---
title: "V$PQ_SYSSTAT"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_2099.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$PQ_SYSSTAT` lists system statistics for parallel queries. After you have run a query or DML operation, you can use the information derived from `V$PQ_SYSSTAT` to view the number of slave processes used, and other information for the system.

| Column | Datatype | Description |
| --- | --- | --- |
| `STATISTIC` | `VARCHAR2(30)` | Name of the statistic: - `Servers Busy` - Number of currently busy servers on this instance - `Servers Idle` - Number of currently idle servers on this instance - `Servers Highwater` - Number of active servers on this instance that have partaken in >= 1 operation so far - `Server Sessions` - Total number of operations executed in all servers on this instance - `Servers Started` - Total number of servers started on this instance - `Servers Shutdown` - Total number of servers shutdown on this instance - `Servers Cleaned Up` - Total number of servers on this instance cleaned up due to process death - `Queries Initiated` - Total number of parallel queries initiated on this instance - `DDL Initiated` - Total number of parallel DDL operations that were initiated - `DML Initiated` - Total number of parallel DML operations that were initiated - `DFO Trees` - Total number of DFO trees executed on this instance - `Local Msgs Sent` - Total number of local (intra-instance) messages sent on this instance - `Distr Msgs Sent` - Total number of remote (inter-instance) messages sent on this instance - `Local Msgs Recv'd` - Total number of remote (inter-instance) messages received on this instance - `Distr Msgs Recv'd` - Total number of remote (inter-instance) messages received on this instance |
| `VALUE` | `NUMBER` | Value of the statistic |