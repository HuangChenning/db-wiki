---
title: "MySQL :: MySQL 26.7 Reference Manual :: 15.1.42 DROP VIEW Statement"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/drop-view.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 15.1.42 DROP VIEW Statement

```sql
DROP VIEW [IF EXISTS]
    view_name [, view_name] ...
    [RESTRICT | CASCADE]
```

`DROP VIEW` removes one or more views. You must have the [`DROP`](privileges-provided.md) privilege for each view. `DROP VIEW` works with SQL views (see [Section 27.6, “Using Views”](views.md)) as well as with JSON duality views (see [Section 27.7, “JSON Duality Views”](json-duality-views.md)).

If any views named in the argument list do not exist, the statement fails with an error indicating by name which nonexisting views it was unable to drop, and no changes are made.

The `IF EXISTS` clause prevents an error from occurring for views that don't exist. When this clause is given, a `NOTE` is generated for each nonexistent view. See [Section 15.7.7.44, “SHOW WARNINGS Statement”](show-warnings.md).

`RESTRICT` and `CASCADE`, if given, are parsed and ignored.