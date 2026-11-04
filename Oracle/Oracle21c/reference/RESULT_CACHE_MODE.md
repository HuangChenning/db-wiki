---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/RESULT_CACHE_MODE.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.318 RESULT\_CACHE\_MODE

`RESULT_CACHE_MODE` specifies which queries are eligible to store result sets in the result cache. Only query execution plans with the result cache operator will attempt to read from or write to the result cache.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `RESULT_CACHE_MODE = { MANUAL \| MANUAL_TEMP \| FORCE \| FORCE_TEMP }` |
| Default value | `MANUAL` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |

Values

- `MANUAL`
	Query results can only be stored in the result cache by using a query hint or table annotation.
- `MANUAL_TEMP`
	Query results can only be stored in the result cache by using a query hint or table annotation. All hinted queries are allowed to leverage temporary segments on disk unless explicitly prohibited by using the `/*+ RESULT_CACHE (TEMP=FALSE) */` hint.
- `FORCE`
	All query results are stored in the result cache. If a query result is not in the cache, then the database executes the query and stores the result in the cache. Subsequent executions of the same SQL statement that include the `/*+ RESULT_CACHE */` hint will retrieve data from the cache. Sessions will use these results, if possible. To exclude query results from the cache, use the `/*+ NO_RESULT_CACHE */` hint.
- `FORCE_TEMP`
	All query results are stored in the result cache. All queries are allowed to leverage temporary segments on disk unless explicitly prohibited by a hint.

Note:

The `FORCE` and `FORCE_TEMP` modes are not generally recommended because queries that call non-deterministic PL/SQL functions are cached, potentially causing material changes to the results. Enabling the result cache in such a broad-based manner can also impact performance in mixed workload environments, where the same tables are continuously updated and retrieved.

See Also:

- [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGSQL251) for more information on how the result cache handles PL/SQL functions before changing the value of this initialization parameter
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=SQLRF20005) for more information about the `NO_RESULT_CACHE` hint