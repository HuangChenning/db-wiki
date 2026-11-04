---
title: "MySQL :: MySQL 26.10 Reference Manual :: 15.1.32 DROP INDEX Statement"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/drop-index.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 15.1.32 DROP INDEX Statement

```sql
DROP INDEX index_name ON tbl_name
    [algorithm_option | lock_option] ...

algorithm_option:
    ALGORITHM [=] {DEFAULT | INPLACE | COPY}

lock_option:
    LOCK [=] {DEFAULT | NONE | SHARED | EXCLUSIVE}
```

`DROP INDEX` drops the index named *`index_name`* from the table *`tbl_name`*. This statement is mapped to an [`ALTER TABLE`](alter-table.md) statement to drop the index. See [Section 15.1.11, “ALTER TABLE Statement”](alter-table.md).

To drop a primary key, the index name is always `PRIMARY`, which must be specified as a quoted identifier because `PRIMARY` is a reserved word:

```sql
DROP INDEX \`PRIMARY\` ON t;
```

Indexes on variable-width columns of [`NDB`](mysql-cluster.md) tables are dropped online; that is, without any table copying. The table is not locked against access from other NDB Cluster API nodes, although it is locked against other operations on the *same* API node for the duration of the operation. This is done automatically by the server whenever it determines that it is possible to do so; you do not have to use any special SQL syntax or server options to cause it to happen.

`ALGORITHM` and `LOCK` clauses may be given to influence the table copying method and level of concurrency for reading and writing the table while its indexes are being modified. They have the same meaning as for the [`ALTER TABLE`](alter-table.md) statement. For more information, see [Section 15.1.11, “ALTER TABLE Statement”](alter-table.md)

MySQL NDB Cluster supports online operations using the same `ALGORITHM=INPLACE` syntax supported in the standard MySQL Server. See [Section 25.6.12, “Online Operations with ALTER TABLE in NDB Cluster”](mysql-cluster-online-operations.md), for more information.