---
title: ALL_MVIEW_JOINS
book: Reference
doc_id: E40402-18
version: "11.2"
source: https://docs.oracle.com/cd/E11882_01/server.112/e40402/statviews_1149.htm
tags:
  - oracle
  - 11g
  - reference
---

`ALL_MVIEW_JOINS` describes joins between two columns in the `WHERE` clause of the subquery that defines a materialized view accessible to the current user.

Related Views

- `DBA_MVIEW_JOINS` describes all such joins for all materialized views in the database.
- `USER_MVIEW_JOINS` describes such joins for all materialized views owned by the current user.

Note:

All three views exclude materialized views that reference remote tables or that includes references to a nonstatic value such as `SYSDATE` or `USER`. These views also exclude materialized views that were created as "snapshots" prior to Oracle8i and that were never altered to enable query rewrite.

| Column | Datatype | NULL | Description |
| --- | --- | --- | --- |
| `OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the materialized view |
| `MVIEW_NAME` | `VARCHAR2(30)` | `NOT NULL` | Materialized view name |
| `DETAILOBJ1_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the first object in the join <sup>Foot 1</sup> |
| `DETAILOBJ1_RELATION` | `VARCHAR2(30)` | `NOT NULL` | Name of the first object in the join <sup>Footref 1</sup> |
| `DETAILOBJ1_COLUMN` | `VARCHAR2(30)` | `NOT NULL` | Join column of the first object in the join <sup>Footref 1</sup> |
| `OPERATOR` | `CHAR(1)` |  | Join operator <sup>Footref 1</sup> |
| `OPERATOR_TYPE` | `VARCHAR2(1)` |  | Indicates whether the join is an inner join (`I`) or the `DETAILOBJ1` table is the left side of an outer join (`L`) <sup>Footref 1</sup> |
| `DETAILOBJ2_OWNER` | `VARCHAR2(30)` | `NOT NULL` | Owner of the second object in the join <sup>Footref 1</sup> |
| `DETAILOBJ2_RELATION` | `VARCHAR2(30)` | `NOT NULL` | Name of the second object in the join <sup>Footref 1</sup> |
| `DETAILOBJ2_COLUMN` | `VARCHAR2(30)` | `NOT NULL` | Join column of the second object in the join <sup>Footref 1</sup> |

<sup>Footnote 1</sup> These rows relate only to materialized join views and materialized aggregate views. They describe the two detail objects of a materialized view join.