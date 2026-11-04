---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/OPTIMIZER_MODE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.253 OPTIMIZER\_MODE

`OPTIMIZER_MODE` establishes the default behavior for choosing an optimization approach for the instance.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `OPTIMIZER_MODE =`  `   { FIRST_ROWS_[1 \| 10 \| 100 \| 1000] \| FIRST_ROWS \| ALL_ROWS }` |
| Default value | `ALL_ROWS` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |

Values

- `FIRST_ROWS_` `n`
	The optimizer uses a cost-based approach and optimizes with a goal of best response time to return the first `n` rows (where `n` = 1, 10, 100, 1000).
- `FIRST_ROWS`
	The optimizer uses a mix of costs and heuristics to find a best plan for fast delivery of the first few rows.
	`FIRST_ROWS` is available for backward compatibility and plan stability; use `FIRST_ROWS_` n instead.
- `ALL_ROWS`
	The optimizer uses a cost-based approach for all SQL statements in the session and optimizes with a goal of best throughput (minimum resource use to complete the entire statement).

See Also:

- [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGSQL255) for more information on setting this parameter
- [Oracle Database Concepts](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=CNCPT316) and [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGSQL192) for more information about the optimizer