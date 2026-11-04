---
title: OPTIMIZER_MODE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams171.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `OPTIMIZER_MODE =`  `{ first_rows_[1 \| 10 \| 100 \| 1000] \| first_rows \| all_rows }` |
| Default value | `all_rows` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |

`OPTIMIZER_MODE` establishes the default behavior for choosing an optimization approach for the instance.

Values:

- `first_rows_` `n`
	The optimizer uses a cost-based approach and optimizes with a goal of best response time to return the first `n` rows (where `n` = 1, 10, 100, 1000).
- `first_rows`
	The optimizer uses a mix of costs and heuristics to find a best plan for fast delivery of the first few rows.
- `all_rows`
	The optimizer uses a cost-based approach for all SQL statements in the session and optimizes with a goal of best throughput (minimum resource use to complete the entire statement).

See Also:

- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm) for more information on setting this parameter
- [Oracle Database Concepts](https://docs.oracle.com/cd/E11882_01/server.112/e40540/toc.htm) and [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm) for more information about the optimizer