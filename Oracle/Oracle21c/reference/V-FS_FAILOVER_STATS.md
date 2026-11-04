---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-FS_FAILOVER_STATS.html
tags:
  - oracle
  - 21c
  - reference
---

## 8.242 V$FS\_FAILOVER\_STATS

`V$FS_FAILOVER_STATS` displays statistics about fast-start failovers occurring on the system.

| Column | Datatype | Description |
| --- | --- | --- |
| `LAST_FAILOVER_TIME` | `VARCHAR2(20)` | Timestamp of the last fast-start failover |
| `LAST_FAILOVER_REASON` | `VARCHAR2(255)` | Reason for the last fast-start failover |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |