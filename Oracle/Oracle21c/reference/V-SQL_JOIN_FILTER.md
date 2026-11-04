---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/V-SQL_JOIN_FILTER.html
tags:
  - oracle
  - 21c
  - reference
---

## 10.54 V$SQL\_JOIN\_FILTER

`V$SQL_JOIN_FILTER` displays performance information about the characteristics of join filters when they are used for a parallel cursor. (A join filter is a bitmap filter applied to table rows before a join operation in order to avoid parallel communication.)

| Column | Datatype | Description |
| --- | --- | --- |
| `QC_SESSION_ID` | `NUMBER` | QC (Query Coordinator) session ID of the given cursor for the given parallel query |
| `QC_INSTANCE_ID` | `NUMBER` | QC (Query Coordinator) instance ID of the given cursor for the given parallel query |
| `SQL_PLAN_HASH_VALUE` | `NUMBER` | SQL plan hash value of the given cursor for the given parallel query |
| `FILTER_ID` | `NUMBER` | An ID that identifies the join filter in the given cursor and corresponds to the filter ID in the execution plan |
| `LENGTH` | `NUMBER` | Total size of the join filter field |
| `BITS_SET` | `NUMBER` | Number of bits set in this filter |
| `FILTERED` | `NUMBER` | Number of rows seen by the join filter |
| `PROBED` | `NUMBER` | Number of rows of the right table that have been tested against the bitmap filter. This is the sum of the filtered rows plus the non-filtered rows. |
| `ACTIVE` | `NUMBER` | Whether the filter is active (Yes) or not (No) |
| `CON_ID` | `NUMBER` | The ID of the container to which the data pertains. Possible values include:  - `0`: This value is used for rows containing data that pertain to the entire CDB. This value is also used for rows in non-CDBs. - `1`: This value is used for rows containing data that pertain to only the root - n: Where n is the applicable container ID for the rows containing data |