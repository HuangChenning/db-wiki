---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-LOGMNR_STATS.html
tags:
  - oracle
  - 21c
  - reference
---

## 9.58 V$LOGMNR\_STATS

`V$LOGMNR_STATS` displays the activity currently being performed by the active LogMiner persistent sessions.

| Column | Datatype | Description |
| --- | --- | --- |
| `SESSION_ID` | `NUMBER` | Unique identifier for the LogMiner persistent sessions |
| `NAME` | `VARCHAR2(64)` | Name of the LogMiner statistic, state, or status, including:  - Bytes of Redo Processed - Cumulative count of bytes processed by SQL Apply - Redo Records Processed - Count of redo records processed by SQL Apply - Txns Delivered to Client - Count of SQL transactions processed by SQL Apply - DML txns delivered - Count of DML transactions processed by SQL Apply - DDL txns delivered - Count of DDL transactions processed by SQL Apply - CTAS txns delivered - Count of `CREATE TABLE AS SELECT` (CTAS) transactions processed by SQL Apply - Recursive txns delivered - Count of recursive transactions processed by SQL Apply - Rolled back txns seen - LCRs delivered to client - Number of logical change records (LCRs) processed by SQL Apply - Bytes paged out - Cumulative count of bytes that have been paged out. LogMiner pages out memory from the LCR cache to accommodate certain ill-behaved workloads or under-configured systems. The ratio of bytes paged out to bytes of redo processed should be low. If this ratio is high (10% or higher), try increasing the `MAX_SGA` allocated to SQL Apply. - Microsecs spent in pageout - Time spent by LogMiner paging out memory from the LCR cache - Bytes checkpointed - Keeps track of the amount of bytes checkpointed. The mining engine takes periodic checkpoints, whereby it writes out logical change records (LCRs) pertaining to long-running transactions. The ratio of `Bytes Checkpointed` to `Bytes of Redo Processed` should be low. A high ratio (10% or higher) indicates an ill-behaved workload. - Microsecs spent in checkpoint - Time spent by the mining engine taking checkpoints, whereby it writes out logical change records (LCRs) pertaining to long-running transactions. - Bytes rolled back - Cumulative value of the number of bytes rolled back by LogMiner. There are times that LogMiner needs to backtrack and reprocess a section of the redo stream. In this case, it will roll back work it has already done. The ratio of `Bytes Rolled Back` to `Bytes of Redo Processed` should be low. If this ratio is high (10% or higher), reduce the number of `PREPARER` processes allocated to SQL Apply. - Microsecs spent in rollback - Time spent rolling back transactions already applied to the logical standby database |
| `VALUE` | `VARCHAR2(64)` | The corresponding metric value |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |