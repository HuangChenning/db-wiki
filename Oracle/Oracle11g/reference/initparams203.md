---
title: QUERY_REWRITE_ENABLED
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams203.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `QUERY_REWRITE_ENABLED = { false \| true \| force }` |
| Default value | If `OPTIMIZER_FEATURES_ENABLE` is set to `10.0.0` or higher, then `true`  If `OPTIMIZER_FEATURES_ENABLE` is set to `9.2.0` or lower, then `false` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Oracle RAC | Multiple instances can have different values. |

`QUERY_REWRITE_ENABLED` allows you to enable or disable query rewriting globally for the database.

Values:

- `false`
	Oracle does not use rewrite.
- `true`
	Oracle costs the query with rewrite and without rewrite and chooses the method with the lower cost.
- `force`
	Oracle always uses rewrite and does not evaluate the cost before doing so. Use `force` when you know that the query will always benefit from rewrite and when reduction in compile time is important.

To take advantage of query rewrite for a particular materialized view, you must enable query rewrite for that materialized view, and you must enable cost-based optimization.

See Also:

- [Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/toc.htm) for information on query rewrite of materialized views
- [Oracle Database Performance Tuning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e41573/toc.htm) and ["OPTIMIZER\_MODE"](initparams171.md) for information on cost-based optimization