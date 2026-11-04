---
title: RESULT_CACHE_MODE
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams221.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `RESULT_CACHE_MODE = { MANUAL \| FORCE }` |
| Default value | `MANUAL` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Basic | No |

`RESULT_CACHE_MODE` specifies when a `ResultCache` operator is spliced into a query's execution plan.

Values:

- `MANUAL`
	The `ResultCache` operator is added only when the query is annotated (that is, hints).
- `FORCE`
	The `ResultCache` operator is added to the root of all `SELECT` statements (provided that it is valid to do so).
	Note:
	`FORCE` mode is not recommended because the database and clients will attempt to cache all queries, which may create significant performance and latching overhead. Moreover, because queries that call non-deterministic PL/SQL functions are also cached, enabling the result cache in such a broad-based manner may cause material changes to the results.

For the `FORCE` setting, if the statement contains a `NO_RESULT_CACHE` hint, then the hint takes precedence over the parameter setting.

See Also:

[Oracle Database SQL Language Reference](https://docs.oracle.com/cd/E11882_01/server.112/e41084/sql_elements006.htm#SQLRF20005) for more information about the NO\_RESULT\_CACHE hint