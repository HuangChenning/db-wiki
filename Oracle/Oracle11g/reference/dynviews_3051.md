---
title: "V$SQL_JOIN_FILTER"
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/dynviews_3051.htm
tags:
  - oracle
  - 11g
  - reference
---

`V$SQL_JOIN_FILTER` displays performance information about the characteristics of join filters when they are used for a parallel cursor. (A join filter is a bitmap filter applied to table rows prior to a join operation in order to avoid parallel communication.)

| Column | Datatype | Description |
| --- | --- | --- |
| `QC_SESSION_ID` | `NUMBER` | QC (Query Coordinator) session ID of the given cursor for the given parallel query |
| `QC_INSTANCE_ID` | `NUMBER` | QC (Query Coordinator) instance ID of the given cursor for the given parallel query |
| `SQL_PLAN_HASH_VALUE` | `NUMBER` | SQL plan hash value of the given cursor for the given parallel query |
| `LENGTH` | `NUMBER` | Total size of the join filter field |
| `BITS_SET` | `NUMBER` | Number of bits set in this filter |
| `FILTERED` | `NUMBER` | Number of rows seen by the join filter |
| `PROBED` | `NUMBER` | Number of rows of the right table that have be tested against the bitmap filter. This is the sum of the filtered rows plus the non-filtered rows. |
| `ACTIVE` | `NUMBER` | Whether the filter is active (Yes) or not (No) |