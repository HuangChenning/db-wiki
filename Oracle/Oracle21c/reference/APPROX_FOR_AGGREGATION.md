---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/APPROX_FOR_AGGREGATION.html
tags:
  - oracle
  - 21c
  - reference
---

## 2.13 APPROX\_FOR\_AGGREGATION

`APPROX_FOR_AGGREGATION` replaces exact query processing for aggregation queries with approximate query processing.

| Property | Description |
| --- | --- |
| Parameter type | Boolean |
| Default value | `false` |
| Modifiable | `ALTER SESSION`, `ALTER SYSTEM` |
| Modifiable in a PDB | Yes |
| Range of values | `true \| false` |
| Basic | No |
| Oracle RAC | Different instances can use different values. |

Data analysis applications heavily use aggregate function and analytic function queries. Aggregation functions and analytic functions require sorting of large volumes of data, and exact query answering requires lots of memory, and can be time consuming. With approximate query processing, the results of aggregate function and analytic function queries are returned much faster than with exact query processing. Approximate query processing is useful for situations where a tolerable amount of error is acceptable in order to obtain faster query results.

The values that can be set are:

- `false`:
	Approximate query processing is not used for aggregation queries and analytic queries.
- `true`: Approximate query processing is used for aggregation queries and analytic queries.

See Also:

- " [APPROX\_FOR\_COUNT\_DISTINCT](APPROX_FOR_COUNT_DISTINCT.md) "
- " [APPROX\_FOR\_PERCENTILE](APPROX_FOR_PERCENTILE.md) "