---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_MVIEW_AGGREGATES.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.279 ALL\_MVIEW\_AGGREGATES

`ALL_MVIEW_AGGREGATES` describes the grouping functions (aggregate operations) that appear in the `SELECT` list of materialized aggregate views accessible to the current user.

Related Views

- `DBA_MVIEW_AGGREGATES` describes all such grouping functions defined for all materialized views in the database.
- `USER_MVIEW_AGGREGATES` describes all such grouping functions defined for all materialized views owned by the current user.

Note:

All three views exclude materialized views that reference remote tables or that include references to a nonstatic value such as `SYSDATE` or `USER`. These views also exclude materialized views that were created as "snapshots" before Oracle8i and that were never altered to enable query rewrite.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the materialized view |
| `MVIEW_NAME` | `VARCHAR2(128)` | `NOT NULL` | Name of the materialized view |
| `POSITION_IN_SELECT` | `NUMBER` | `NOT NULL` | Ordinal position of this aggregation within the `SELECT` list. For the position of nonaggregate elements of the select list, see " [ALL\_MVIEW\_KEYS](ALL_MVIEW_KEYS.md) ". |
| `CONTAINER_COLUMN` | `VARCHAR2(128)` | `NOT NULL` | Name of this column in the container table |
| `AGG_FUNCTION` | `VARCHAR2(8)` |  | Aggregation function |
| `DISTINCTFLAG` | `VARCHAR2(1)` |  | Indicates whether this aggregation is distinct (`Y`) or not (`N`) |
| `MEASURE` | `LONG` |  | SQL text of the measure, excluding the aggregation function. Equal to `*` for `COUNT(*)`. |

See Also:

- " [DBA\_MVIEW\_AGGREGATES](DBA_MVIEW_AGGREGATES.md) "
- " [USER\_MVIEW\_AGGREGATES](USER_MVIEW_AGGREGATES.md) "