---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/FAST_START_PARALLEL_ROLLBACK.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.133 FAST\_START\_PARALLEL\_ROLLBACK

`FAST_START_PARALLEL_ROLLBACK` specifies the degree of parallelism used when recovering terminated transactions.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `FAST_START_PARALLEL_ROLLBACK = { HIGH \| LOW \| FALSE }` |
| Default value | `LOW` |
| Modifiable | `ALTER SYSTEM` |
| Modifiable in a PDB | No |
| Basic | No |

Terminated transactions are transactions that are active before a system failure. If a system fails when there are uncommitted parallel DML or DDL transactions, then you can speed up transaction recovery during startup by using this parameter.

Values

- `FALSE`
	Parallel rollback is disabled
- `LOW`
	Limits the maximum degree of parallelism to 2 \* `CPU_COUNT`
- `HIGH`
	Limits the maximum degree of parallelism to 4 \* `CPU_COUNT`

If you change the value of this parameter, then transaction recovery will be stopped and restarted with the new implied degree of parallelism.

See Also:

[Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=VLDBG1504) for more information about this parameter