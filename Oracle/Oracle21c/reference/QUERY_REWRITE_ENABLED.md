---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/QUERY_REWRITE_ENABLED.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.296 QUERY\_REWRITE\_ENABLED

Use `QUERY_REWRITE_ENABLED` to enable or disable query rewriting globally for the database.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `QUERY_REWRITE_ENABLED = { false \| true \| force }` |
| Default value | If `OPTIMIZER_FEATURES_ENABLE` is set to `10.0.0` or higher, then `true`  If `OPTIMIZER_FEATURES_ENABLE` is set to `9.2.0` or lower, then `false` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |

Values

- `false`
	Oracle does not use rewrite.
- `true`
	Oracle costs the query with rewrite and without rewrite and chooses the method with the lower cost.
- `force`
	Oracle always uses rewrite and does not evaluate the cost before doing so. Use `force` when you know that the query will always benefit from rewrite and when reduction in compile time is important.

To take advantage of query rewrite for a particular materialized view, you must enable query rewrite for that materialized view, and you must enable cost-based optimization.

See Also:

- [Oracle Database Data Warehousing Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DWHSG-GUID-D4CD7FA7-7E59-4114-A8A7-941FD7F1C07E) for information on query rewrite of materialized views
- [Oracle Database SQL Tuning Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=TGSQL195) and " [OPTIMIZER\_MODE](OPTIMIZER_MODE.md) " for information on cost-based optimization