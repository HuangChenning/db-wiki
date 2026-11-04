---
title: "17.12.6 Simplifying DDL Statements with Online DDL"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/innodb-online-ddl-single-multi.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 17.12.6 Simplifying DDL Statements with Online DDL

Before the introduction of [online DDL](glossary.md), it was common practice to combine many DDL operations into a single [`ALTER TABLE`](alter-table.md) statement. Because each [`ALTER TABLE`](alter-table.md) statement involved copying and rebuilding the table, it was more efficient to make several changes to the same table at once, since those changes could all be done with a single rebuild operation for the table. The downside was that SQL code involving DDL operations was harder to maintain and to reuse in different scripts. If the specific changes were different each time, you might have to construct a new complex [`ALTER       TABLE`](alter-table.md) for each slightly different scenario.

For DDL operations that can be done online, you can separate them into individual [`ALTER TABLE`](alter-table.md) statements for easier scripting and maintenance, without sacrificing efficiency. For example, you might take a complicated statement such as:

```
ALTER TABLE t1 ADD INDEX i1(c1), ADD UNIQUE INDEX i2(c2),
  CHANGE c4_old_name c4_new_name INTEGER UNSIGNED;
```

and break it down into simpler parts that can be tested and performed independently, such as:

```
ALTER TABLE t1 ADD INDEX i1(c1);
ALTER TABLE t1 ADD UNIQUE INDEX i2(c2);
ALTER TABLE t1 CHANGE c4_old_name c4_new_name INTEGER UNSIGNED NOT NULL;
```

You might still use multi-part [`ALTER       TABLE`](alter-table.md) statements for:

- Operations that must be performed in a specific sequence, such as creating an index followed by a foreign key constraint that uses that index.
- Operations all using the same specific `LOCK` clause, that you want to either succeed or fail as a group.
- Operations that cannot be performed online, that is, that still use the table-copy method.
- Operations for which you specify `ALGORITHM=COPY` or [`old_alter_table=1`](server-system-variables.md), to force the table-copying behavior if needed for precise backward-compatibility in specialized scenarios.