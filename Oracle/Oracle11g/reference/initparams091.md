---
title: FAST_START_PARALLEL_ROLLBACK
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams091.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `FAST_START_PARALLEL_ROLLBACK = { HIGH \| LOW \| FALSE }` |
| Default value | `LOW` |
| Modifiable | `ALTER SYSTEM` |
| Basic | No |

`FAST_START_PARALLEL_ROLLBACK` specifies the degree of parallelism used when recovering terminated transactions. Terminated transactions are transactions that are active before a system failure. If a system fails when there are uncommitted parallel DML or DDL transactions, then you can speed up transaction recovery during startup by using this parameter.

Values:

- `FALSE`
	Parallel rollback is disabled
- `LOW`
	Limits the maximum degree of parallelism to 2 \* `CPU_COUNT`
- `HIGH`
	Limits the maximum degree of parallelism to 4 \* `CPU_COUNT`

If you change the value of this parameter, then transaction recovery will be stopped and restarted with the new implied degree of parallelism.