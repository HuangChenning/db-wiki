---
title: "MySQL :: MySQL 26.7 Reference Manual :: 15.1.13 ALTER VIEW Statement"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/alter-view.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 15.1.13 ALTER VIEW Statement

```sql
ALTER
    [ALGORITHM = {UNDEFINED | MERGE | TEMPTABLE}]
    [MATERIALIZED] ...
    [DEFINER = user]
    [SQL SECURITY { DEFINER | INVOKER }]
    VIEW view_name [(column_list)]
    AS select_statement
    [WITH [CASCADED | LOCAL] CHECK OPTION]
```

This statement changes the definition of a view, which must exist. The syntax is similar to that for [`CREATE       VIEW`](create-view.md) see [Section 15.1.28, “CREATE VIEW Statement”](create-view.md)). This statement requires the [`CREATE VIEW`](privileges-provided.md) and [`DROP`](privileges-provided.md) privileges for the view, and some privilege for each column referred to in the [`SELECT`](select.md) statement. `ALTER VIEW` is permitted only to the definer or users with the [`SET_ANY_DEFINER`](privileges-provided.md) or [`ALLOW_NONEXISTENT_DEFINER`](privileges-provided.md) privilege.

Materialized views is only supported on MySQL HeatWave. See [Query Materalized Views](https://dev.mysql.com/doc/heatwave/en/mys-hw-materialized-views.html) to learn more.