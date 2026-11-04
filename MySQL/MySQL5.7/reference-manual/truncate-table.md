---
title: "13.1.34 TRUNCATE TABLE Statement"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/truncate-table.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 13.1.34 TRUNCATE TABLE Statement

```
TRUNCATE [TABLE] tbl_name
```

`TRUNCATE TABLE` empties a table completely. It requires the [`DROP`](privileges-provided.md) privilege.

Logically, `TRUNCATE TABLE` is similar to a [`DELETE`](delete.md) statement that deletes all rows, or a sequence of [`DROP       TABLE`](drop-table.md) and [`CREATE TABLE`](create-table.md) statements. To achieve high performance, it bypasses the DML method of deleting data. Thus, it cannot be rolled back, it does not cause `ON DELETE` triggers to fire, and it cannot be performed for `InnoDB` tables with parent-child foreign key relationships.

Although `TRUNCATE TABLE` is similar to [`DELETE`](delete.md), it is classified as a DDL statement rather than a DML statement. It differs from [`DELETE`](delete.md) in the following ways:

- Truncate operations drop and re-create the table, which is much faster than deleting rows one by one, particularly for large tables.
- Truncate operations cause an implicit commit, and so cannot be rolled back. See [Section 13.3.3, “Statements That Cause an Implicit Commit”](implicit-commit.md).
- Truncation operations cannot be performed if the session holds an active table lock.
- `TRUNCATE TABLE` fails for an `InnoDB` table or [`NDB`](mysql-cluster.md) table if there are any `FOREIGN KEY` constraints from other tables that reference the table. Foreign key constraints between columns of the same table are permitted.
- Truncation operations do not return a meaningful value for the number of deleted rows. The usual result is “0 rows affected,” which should be interpreted as “no information.”
- As long as the table format file ``*`tbl_name`*.frm`` is valid, the table can be re-created as an empty table with `TRUNCATE TABLE`, even if the data or index files have become corrupted.
- Any `AUTO_INCREMENT` value is reset to its start value. This is true even for `MyISAM` and `InnoDB`, which normally do not reuse sequence values.
- When used with partitioned tables, `TRUNCATE TABLE` preserves the partitioning; that is, the data and index files are dropped and re-created, while the partition definitions (`.par`) file is unaffected.
- The `TRUNCATE TABLE` statement does not invoke `ON DELETE` triggers.

`TRUNCATE TABLE` is treated for purposes of binary logging and replication as DDL rather than DML, and is always logged as a statement.

`TRUNCATE TABLE` for a table closes all handlers for the table that were opened with [`HANDLER OPEN`](handler.md).

On a system with a large `InnoDB` buffer pool and [`innodb_adaptive_hash_index`](innodb-parameters.md) enabled, `TRUNCATE TABLE` operations may cause a temporary drop in system performance due to an LRU scan that occurs when removing an `InnoDB` table's adaptive hash index entries. The problem was addressed for [`DROP TABLE`](drop-table.md) in MySQL 5.5.23 (Bug #13704145, Bug #64284) but remains a known issue for `TRUNCATE TABLE` (Bug #68184).

`TRUNCATE TABLE` can be used with Performance Schema summary tables, but the effect is to reset the summary columns to 0 or `NULL`, not to remove rows. See [Section 25.12.15, “Performance Schema Summary Tables”](performance-schema-summary-tables.md).