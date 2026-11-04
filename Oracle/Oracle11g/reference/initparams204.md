---
title: QUERY_REWRITE_INTEGRITY
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/initparams204.htm
tags:
  - oracle
  - 11g
  - reference
---

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `QUERY_REWRITE_INTEGRITY = { enforced \| trusted \| stale_tolerated }` |
| Default value | `enforced` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Oracle RAC | Multiple instances can have different values. |

`QUERY_REWRITE_INTEGRITY` determines the degree to which Oracle must enforce query rewriting. At the safest level, Oracle does not use query rewrite transformations that rely on unenforced relationships.

`QUERY_REWRITE_INTEGRITY` is relevant for materialized views as well as for foreign key constraints in `NOVALIDATE` state.

Values:

- `enforced`
	Oracle enforces and guarantees consistency and integrity.
- `trusted`
	Oracle allows rewrites using relationships that have been declared, but that are not enforced by Oracle.
- `stale_tolerated`
	Oracle allows rewrites using unenforced relationships. Materialized views are eligible for rewrite even if they are known to be inconsistent with the underlying detail data.

If a foreign key constraint is in `NOVALIDATE` state, join elimination is not done when `QUERY_REWRITE_INTEGRITY=enforced`. This means that queries with joins over a foreign key constraint that is in `RELY NOVALIDATE` state can potentially take longer to parse and execute as the optimizer does not trust the `RELY`.

See Also:

- [Oracle Database Data Warehousing Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25554/qrbasic.htm#DWHSG018) for more information about using query rewrite for materialized views and using the optional `QUERY_REWRITE_INTEGRITY` parameter
- [Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/cd/E11882_01/server.112/e25523/part_warehouse.htm#VLDBG1363) for information about materialized view refresh strategies