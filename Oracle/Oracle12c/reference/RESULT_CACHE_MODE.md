---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/RESULT_CACHE_MODE.html
tags:
  - oracle
  - 12c
  - reference
---

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
	Note:
	`FORCE` mode is not recommended because the database and clients will attempt to cache all queries, which may create significant performance and latching overhead. Moreover, because queries that call non-deterministic PL/SQL functions are also cached, enabling the result cache in such a broad-based manner may cause material changes to the results.

For the `FORCE` setting, if the statement contains a `NO_RESULT_CACHE` hint, then the hint takes precedence over the parameter setting.

See Also:

- [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=TGSQL251) for more information on how the result cache handles PL/SQL functions before changing the value of this initialization parameter
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=SQLRF20005) for more information about the NO\_RESULT\_CACHE hint