---
title: "15.1.11 ALTER VIEW Statement"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/alter-view.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 15.1.11 ALTER VIEW Statement

```
ALTER
    [ALGORITHM = {UNDEFINED | MERGE | TEMPTABLE}]
    [DEFINER = user]
    [SQL SECURITY { DEFINER | INVOKER }]
    VIEW view_name [(column_list)]
    AS select_statement
    [WITH [CASCADED | LOCAL] CHECK OPTION]
```

This statement changes the definition of a view, which must exist. The syntax is similar to that for [`CREATE       VIEW`](create-view.md) see [Section 15.1.23, “CREATE VIEW Statement”](create-view.md)). This statement requires the [`CREATE VIEW`](privileges-provided.md) and [`DROP`](privileges-provided.md) privileges for the view, and some privilege for each column referred to in the [`SELECT`](select.md) statement. `ALTER VIEW` is permitted only to the definer or users with the [`SET_USER_ID`](privileges-provided.md) privilege (or the deprecated [`SUPER`](privileges-provided.md) privilege).