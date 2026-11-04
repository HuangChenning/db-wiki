---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/APPROX_FOR_COUNT_DISTINCT.html
tags:
  - oracle
  - 12c
  - reference
---

`APPROX_FOR_COUNT_DISTINCT` automatically replaces `COUNT (DISTINCT expr)` queries with `APPROX_COUNT_DISTINCT` queries.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | `ALTER SESSION, ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `true \| false` |
| Basic | No |
| Oracle RAC | Different instances can use different values. |

Query results for `APPROX_COUNT_DISTINCT` queries are returned faster than the equivalent `COUNT (DISTINCT expr)` queries. `APPROX_COUNT_DISTINCT` queries are useful for situations where a tolerable amount of error is acceptable in order to obtain faster query results than with a `COUNT (DISTINCT expr)` query.

Note:

This initialization parameter is available starting with Oracle Database 12c Release 2 (12.2.0.1).

See Also:

- " [APPROX\_FOR\_AGGREGATION](APPROX_FOR_AGGREGATION.md) "
- " [APPROX\_FOR\_PERCENTILE](APPROX_FOR_PERCENTILE.md) "