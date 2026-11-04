---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/PARALLEL_MIN_TIME_THRESHOLD.html
tags:
  - oracle
  - 12c
  - reference
---

`PARALLEL_MIN_TIME_THRESHOLD` specifies the minimum execution time a statement should have before the statement is considered for automatic degree of parallelism.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `PARALLEL_MIN_TIME_THRESHOLD = { AUTO \| ` `integer` ` }` |
| Default value | `AUTO` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |

By default, this parameter is set to 10 seconds. Automatic degree of parallelism is only enabled if `PARALLEL_DEGREE_POLICY` is set to `ADAPTIVE`, `AUTO`, or `LIMITED`.

If all tables referenced by a SQL statement use In-Memory Column Store (IM column store), then `PARALLEL_MIN_TIME_THRESHOLD` defaults to 1.

See Also:

[Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=VLDBG13911) for information about automatic degree of parallelism