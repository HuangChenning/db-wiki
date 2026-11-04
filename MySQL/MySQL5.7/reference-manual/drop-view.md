---
title: "13.1.32 DROP VIEW Statement"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/drop-view.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 13.1.32 DROP VIEW Statement

```
DROP VIEW [IF EXISTS]
    view_name [, view_name] ...
    [RESTRICT | CASCADE]
```

`DROP VIEW` removes one or more views. You must have the [`DROP`](privileges-provided.md) privilege for each view.

If any views named in the argument list do not exist, the statement returns an error indicating by name which nonexisting views it was unable to drop, but also drops all views in the list that do exist.

Note

In MySQL 8.0, `DROP VIEW` fails if any views named in the argument list do not exist. Due to the change in behavior, a partially completed `DROP VIEW` operation on a MySQL 5.7 source fails when replicated to a MySQL 8.0 replica. To avoid this failure scenario, use `IF EXISTS` syntax in `DROP         VIEW` statements to prevent an error from occurring for views that do not exist. For more information, see [Atomic Data Definition Statement Support](https://docs.oracle.com/cd/E17952_01/mysql-8.0-en/atomic-ddl.html).

The `IF EXISTS` clause prevents an error from occurring for views that don't exist. When this clause is given, a `NOTE` is generated for each nonexistent view. See [Section 13.7.5.40, “SHOW WARNINGS Statement”](show-warnings.md).

`RESTRICT` and `CASCADE`, if given, are parsed and ignored.