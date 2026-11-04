---
title: "17.11.4 Defragmenting a Table"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/innodb-file-defragmenting.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 17.11.4 Defragmenting a Table

Random insertions into or deletions from a secondary index can cause the index to become fragmented. Fragmentation means that the physical ordering of the index pages on the disk is not close to the index ordering of the records on the pages, or that there are many unused pages in the 64-page blocks that were allocated to the index.

One symptom of fragmentation is that a table takes more space than it “should” take. How much that is exactly, is difficult to determine. All `InnoDB` data and indexes are stored in [B-trees](glossary.md), and their [fill factor](glossary.md) may vary from 50% to 100%. Another symptom of fragmentation is that a table scan such as this takes more time than it “should” take:

```
SELECT COUNT(*) FROM t WHERE non_indexed_column <> 12345;
```

The preceding query requires MySQL to perform a full table scan, the slowest type of query for a large table.

To speed up index scans, you can periodically perform a “null” [`ALTER TABLE`](alter-table.md) operation, which causes MySQL to rebuild the table:

```
ALTER TABLE tbl_name ENGINE=INNODB
```

You can also use [``ALTER TABLE       *`tbl_name`* FORCE``](alter-table.md) to perform a “null” alter operation that rebuilds the table.

Both [``ALTER TABLE       *`tbl_name`* ENGINE=INNODB``](alter-table.md) and [``ALTER TABLE       *`tbl_name`* FORCE``](alter-table.md) use [online DDL](innodb-online-ddl.md). For more information, see [Section 17.12, “InnoDB and Online DDL”](innodb-online-ddl.md).

Another way to perform a defragmentation operation is to use [**mysqldump**](mysqldump.md) to dump the table to a text file, drop the table, and reload it from the dump file.

If the insertions into an index are always ascending and records are deleted only from the end, the `InnoDB` filespace management algorithm guarantees that fragmentation in the index does not occur.