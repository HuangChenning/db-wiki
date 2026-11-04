---
title: "13.1.10 ALTER VIEW Statement"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/alter-view.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 13.1.10 ALTER VIEW Statement

```
ALTER
    [ALGORITHM = {UNDEFINED | MERGE | TEMPTABLE}]
    [DEFINER = user]
    [SQL SECURITY { DEFINER | INVOKER }]
    VIEW view_name [(column_list)]
    AS select_statement
    [WITH [CASCADED | LOCAL] CHECK OPTION]
```

This statement changes the definition of a view, which must exist. The syntax is similar to that for [`CREATE       VIEW`](create-view.md) see [Section 13.1.21, “CREATE VIEW Statement”](create-view.md)). This statement requires the [`CREATE VIEW`](privileges-provided.md) and [`DROP`](privileges-provided.md) privileges for the view, and some privilege for each column referred to in the [`SELECT`](select.md) statement. `ALTER VIEW` is permitted only to the definer or users with the [`SUPER`](privileges-provided.md) privilege.