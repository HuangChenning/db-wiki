---
title: Database Reference
book: Database Reference
doc_id: E96196-45
version: "19c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/RESULT_CACHE_MODE.html
tags:
  - oracle
  - 19c
  - reference
---

## 1.317 RESULT\_CACHE\_MODE

`RESULT_CACHE_MODE` specifies when a `ResultCache` operator is spliced into a query's execution plan.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `RESULT_CACHE_MODE = { MANUAL \| FORCE }` |
| Default value | `MANUAL` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |

Values

- `MANUAL`
	The `ResultCache` operator is added only when the query is annotated (that is, hints).
- `FORCE`
	The `ResultCache` operator is added to the root of all `SELECT` statements (when it is valid to do so).
	For the `FORCE` setting, if the statement contains a `NO_RESULT_CACHE` hint, then the hint takes precedence over the parameter setting.
	Note:
	`FORCE` mode is not generally recommended because queries that call non-deterministic PL/SQL functions are cached, potentially causing material changes to the results. Enabling the result cache in such a broad-based manner can also impact performance in mixed workload environments, where the same tables are continuously updated and retrieved.

See Also:

- [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=TGSQL251) for more information on how the result cache handles PL/SQL functions before changing the value of this initialization parameter
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19/refrn&id=SQLRF20005) for more information about the NO\_RESULT\_CACHE hint