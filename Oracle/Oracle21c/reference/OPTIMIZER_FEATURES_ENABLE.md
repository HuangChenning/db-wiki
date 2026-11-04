---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/OPTIMIZER_FEATURES_ENABLE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.247 OPTIMIZER\_FEATURES\_ENABLE

`OPTIMIZER_FEATURES_ENABLE` acts as an umbrella parameter for enabling a series of optimizer features based on an Oracle release number.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `OPTIMIZER_FEATURES_ENABLE = { 8.0.0 \| 8.0.3 \| 8.0.4 \| 8.0.5 \| 8.0.6 \| 8.0.7 \| 8.1.0 \| 8.1.3 \| 8.1.4 \| 8.1.5 \| 8.1.6 \| 8.1.7 \| 9.0.0 \| 9.0.1 \| 9.2.0 \| 9.2.0.8 \| 10.1.0 \| 10.1.0.3 \| 10.1.0.4 \| 10.1.0.5 \| 10.2.0.1 \| 10.2.0.2 \| 10.2.0.3 \| 10.2.0.4 \| 10.2.0.5 \| 11.1.0.6 \| 11.1.0.7 \| 11.2.0.1 \| 11.2.0.2 \| 11.2.0.3 \| 11.2.0.4 \| 12.1.0.1 \| 12.1.0.2 \| 12.2.0.1 \| 18.1.0 \| 19.1.0 \| 21.1.0 }` |
| Default value | `21.1.0` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |

For example, if you upgrade your database from release 11.1 to release 12.1, but you want to keep the release 11.1 optimizer behavior, you can do so by setting this parameter to `11.1.0.6`. At a later time, you can try the enhancements introduced in releases up to and including release 12.1 by setting the parameter to `12.1.0.2`.

Note:

When setting this parameter to a value representing Oracle Database 18c or later, you must specify three numeric values separated by periods, such as `18.1.0` or `19.1.0`.

Table 2-6 describes some of the optimizer features that are enabled when you set the `OPTIMIZER_FEATURES_ENABLE` parameter to an 11.1 or 11.2 release.

Table 2-7 describes some of the optimizer features that are enabled when you set the `OPTIMIZER_FEATURES_ENABLE` parameter to a 12.1 or later release.

See Also:

[Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGSQL112) for more information about the optimizer and for information about the features listed in the following tables

Table 2-6 Optimizer Features for Oracle Database 11g Releases

| Features | 11.1.0.6 | 11.1.0.7 | 11.2.0.1 | 11.2.0.2 | 11.2.0.3 | 11.2.0.4 |
| --- | --- | --- | --- | --- | --- | --- |
| Adaptive cursor sharing | X | X | X | X | X | X |
| Join predicate pushdown | X | X | X | X | X | X |
| Use extended statistics to estimate selectivity | X | X | X | X | X | X |
| Use native implementation for full outer joins | X | X | X | X | X | X |
| Partition pruning using join filtering | X | X | X | X | X | X |
| Group by placement optimization | X | X | X | X | X | X |
| Null aware antijoins | X | X | X | X | X | X |
| Join predicate pushdown | X | X | X | X | X | X |
| Join Factorization |  |  | X | X | X | X |
| Cardinality Feedback |  |  | X | X | X | X |
| Subquery Unnesting |  |  | X | X | X | X |
| Subquery Coalescing |  |  | X | X | X | X |
| Table Expansion |  |  | X | X | X | X |
| Filtering Join Elimination |  |  | X | X | X | X |
| Dynamic statistics enhancements |  |  |  |  |  | X |

Table 2-7 Optimizer Features for Oracle Database 12c and Later Releases

| Features | 12.1.0.1 | 12.1.0.2 | 12.2.0.1 | 18c | 19c | 21c |
| --- | --- | --- | --- | --- | --- | --- |
| All optimizer features listed in Table 2-6 | X | X | X | X | X | X |
| Adaptive Query Optimization | X | X | X | X | X | X |
| Online statistics gathering for bulk loads | X | X | X | X | X | X |
| Session level statistics for Global Temporary Tables | X | X | X | X | X | X |
| Multi-table left outer joins | X | X | X | X | X | X |
| Lateral views | X | X | X | X | X | X |
| Batch table access by rowid | X | X | X | X | X | X |
| Null accepting semi joins | X | X | X | X | X | X |
| Scalar subquery unnesting | X | X | X | X | X | X |
| Conversion of joins that produce unnecessary duplicates to semi-joins | X | X | X | X | X | X |
| Parallel Union and Parallel Union All operations | X | X | X | X | X | X |
| Enhance Auto DOP | X | X | X | X | X | X |
| Approximate count distinct |  | X | X | X | X | X |
| Support for Oracle Database In-Memory |  | X | X | X | X | X |
| Group-by and aggregation elimination |  | X | X | X | X | X |
| Query rewrite for approximate query processing |  |  | X | X | X | X |
| Statistics advisor |  |  | X | X | X | X |
| Support for sharded databases |  |  | X | X | X | X |
| Expression tracking |  |  | X | X | X | X |
| Space-saving algorithm for partition synopses |  |  | X | X | X | X |
| Oracle In-Memory Database statistics |  |  | X | X | X | X |
| Support for sharding |  |  | X | X | X | X |
| Cost-based OR expansion |  |  | X | X | X | X |
| Sub-query elimination |  |  | X | X | X | X |
| Multi-column key join elimination |  |  | X | X | X | X |
| SQL Quarantine |  |  |  |  | X | X |
| Gathering and use of real-time statistics |  |  |  |  | X | X |
| Use of automatic indexes |  |  |  |  | X | X |
| `WITH` clause filter predicate pushdown |  |  |  |  |  | X |
| Number of distinct value (NDV) modeling for real time statistics |  |  |  |  |  | X |