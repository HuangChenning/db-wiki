---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/QUERY_REWRITE_INTEGRITY.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.297 QUERY\_REWRITE\_INTEGRITY

`QUERY_REWRITE_INTEGRITY` determines the degree to which Oracle must enforce query rewriting. At the safest level, Oracle does not use query rewrite transformations that rely on unenforced relationships.

| Property | Description |
| --- | --- |
| Parameter type | String |
| Syntax | `QUERY_REWRITE_INTEGRITY = { enforced \| trusted \| stale_tolerated }` |
| Default value | `enforced` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Basic | No |
| Oracle RAC | Multiple instances can have different values. |

`QUERY_REWRITE_INTEGRITY` is relevant for materialized views as well as for foreign key constraints in `NOVALIDATE` state.

Values

- `enforced`
	Oracle enforces and guarantees consistency and integrity.
- `trusted`
	Oracle allows rewrites using relationships that have been declared, but that are not enforced by Oracle.
- `stale_tolerated`
	Oracle allows rewrites using unenforced relationships. Materialized views are eligible for rewrite even if they are known to be inconsistent with the underlying detail data. You must set the `QUERY_REWRITE_INTEGRITY` initialization parameter to `stale_tolerated` before querying an external table in the In-Memory Column Store (IM column store).

If a foreign key constraint is in `NOVALIDATE` state, join elimination is not done when `QUERY_REWRITE_INTEGRITY=enforced`. This means that queries with joins over a foreign key constraint that is in `RELY NOVALIDATE` state can potentially take longer to parse and execute as the optimizer does not trust the `RELY`.

See Also:

- " [INMEMORY\_CLAUSE\_DEFAULT](INMEMORY_CLAUSE_DEFAULT.md) "
- [Oracle Database Data Warehousing Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DWHSG-GUID-D4CD7FA7-7E59-4114-A8A7-941FD7F1C07E) for more information about query rewrite for materialized views
- [Oracle Database Data Warehousing Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/21/refrn&id=DWHSG01821) for more information about the `QUERY_REWRITE_INTEGRITY` parameter