---
title: Database Reference
book: Database Reference
doc_id: F31274-35
version: "21c"
source: https://docs.oracle.com/en/database/oracle/oracle-database/21/refrn/ALL_MVIEW_JOINS.html
tags:
  - oracle
  - 21c
  - reference
---

## 3.285 ALL\_MVIEW\_JOINS

`ALL_MVIEW_JOINS` describes joins between two columns in the `WHERE` clause of the subquery that defines a materialized view accessible to the current user.

Related Views

- `DBA_MVIEW_JOINS` describes all such joins for all materialized views in the database.
- `USER_MVIEW_JOINS` describes such joins for all materialized views owned by the current user.

Note:

All three views exclude materialized views that reference remote tables or that includes references to a nonstatic value such as `SYSDATE` or `USER`. These views also exclude materialized views that were created as "snapshots" before Oracle8i and that were never altered to enable query rewrite.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the materialized view |
| `MVIEW_NAME` | `VARCHAR2(128)` | `NOT NULL` | Materialized view name |
| `DETAILOBJ1_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the first object in the join <sup>Foot 1</sup> |
| `DETAILOBJ1_RELATION` | `VARCHAR2(128)` | `NOT NULL` | Name of the first object in the join <sup>Foot 1</sup> |
| `DETAILOBJ1_COLUMN` | `VARCHAR2(128)` | `NOT NULL` | Join column of the first object in the join <sup>Foot 1</sup> |
| `OPERATOR` | `CHAR(1)` |  | Join operator <sup>Foot 1</sup> |
| `OPERATOR_TYPE` | `VARCHAR2(1)` |  | Indicates whether the join is an inner join (`I`) or the `DETAILOBJ1` table is the left side of an outer join (`L`) <sup>Foot 1</sup> |
| `DETAILOBJ2_OWNER` | `VARCHAR2(128)` | `NOT NULL` | Owner of the second object in the join <sup>Foot 1</sup> |
| `DETAILOBJ2_RELATION` | `VARCHAR2(128)` | `NOT NULL` | Name of the second object in the join <sup>Foot 1</sup> |
| `DETAILOBJ2_COLUMN` | `VARCHAR2(128)` | `NOT NULL` | Join column of the second object in the join <sup>Foot 1</sup> |

<sup>Footnote 1</sup>

These rows relate only to materialized join views and materialized aggregate views. They describe the two detail objects of a materialized view join.

See Also:

- " [DBA\_MVIEW\_JOINS](DBA_MVIEW_JOINS.md) "
- " [USER\_MVIEW\_JOINS](USER_MVIEW_JOINS.md) "