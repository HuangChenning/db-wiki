---
title: "10.6.2 Bulk Data Loading for MyISAM Tables"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/optimizing-myisam-bulk-data-loading.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 10.6.2 Bulk Data Loading for MyISAM Tables

These performance tips supplement the general guidelines for fast inserts in [Section 10.2.5.1, “Optimizing INSERT Statements”](insert-optimization.md).

- For a `MyISAM` table, you can use concurrent inserts to add rows at the same time that [`SELECT`](select.md) statements are running, if there are no deleted rows in middle of the data file. See [Section 10.11.3, “Concurrent Inserts”](concurrent-inserts.md).
- With some extra work, it is possible to make [`LOAD DATA`](load-data.md) run even faster for a `MyISAM` table when the table has many indexes. Use the following procedure:
	1. Execute a [`FLUSH TABLES`](flush.md) statement or a [**mysqladmin flush-tables**](mysqladmin.md) command.
	2. Use [**myisamchk --keys-used=0 -rq *`/path/to/db/tbl_name`***](myisamchk.md) to remove all use of indexes for the table.
	3. Insert data into the table with [`LOAD DATA`](load-data.md). This does not update any indexes and therefore is very fast.
	4. If you intend only to read from the table in the future, use [**myisampack**](myisampack.md) to compress it. See [Section 18.2.3.3, “Compressed Table Characteristics”](compressed-format.md).
	5. Re-create the indexes with [**myisamchk -rq *`/path/to/db/tbl_name`***](myisamchk.md). This creates the index tree in memory before writing it to disk, which is much faster than updating the index during [`LOAD DATA`](load-data.md) because it avoids lots of disk seeks. The resulting index tree is also perfectly balanced.
	6. Execute a [`FLUSH TABLES`](flush.md) statement or a [**mysqladmin flush-tables**](mysqladmin.md) command.
	[`LOAD DATA`](load-data.md) performs the preceding optimization automatically if the `MyISAM` table into which you insert data is empty. The main difference between automatic optimization and using the procedure explicitly is that you can let [**myisamchk**](myisamchk.md) allocate much more temporary memory for the index creation than you might want the server to allocate for index re-creation when it executes the [`LOAD DATA`](load-data.md) statement.
	You can also disable or enable the nonunique indexes for a `MyISAM` table by using the following statements rather than [**myisamchk**](myisamchk.md). If you use these statements, you can skip the [`FLUSH TABLES`](flush.md) operations:
	```
	ALTER TABLE tbl_name DISABLE KEYS;
	ALTER TABLE tbl_name ENABLE KEYS;
	```
- To speed up [`INSERT`](insert.md) operations that are performed with multiple statements for nontransactional tables, lock your tables:
	```
	LOCK TABLES a WRITE;
	INSERT INTO a VALUES (1,23),(2,34),(4,33);
	INSERT INTO a VALUES (8,26),(6,29);
	...
	UNLOCK TABLES;
	```
	This benefits performance because the index buffer is flushed to disk only once, after all [`INSERT`](insert.md) statements have completed. Normally, there would be as many index buffer flushes as there are [`INSERT`](insert.md) statements. Explicit locking statements are not needed if you can insert all rows with a single [`INSERT`](insert.md).
	Locking also lowers the total time for multiple-connection tests, although the maximum wait time for individual connections might go up because they wait for locks. Suppose that five clients attempt to perform inserts simultaneously as follows:
	- Connection 1 does 1000 inserts
	- Connections 2, 3, and 4 do 1 insert
	- Connection 5 does 1000 inserts
	If you do not use locking, connections 2, 3, and 4 finish before 1 and 5. If you use locking, connections 2, 3, and 4 probably do not finish before 1 or 5, but the total time should be about 40% faster.
	[`INSERT`](insert.md), [`UPDATE`](update.md), and [`DELETE`](delete.md) operations are very fast in MySQL, but you can obtain better overall performance by adding locks around everything that does more than about five successive inserts or updates. If you do very many successive inserts, you could do a [`LOCK             TABLES`](lock-tables.md) followed by an [`UNLOCK             TABLES`](lock-tables.md) once in a while (each 1,000 rows or so) to permit other threads to access table. This would still result in a nice performance gain.
	[`INSERT`](insert.md) is still much slower for loading data than [`LOAD             DATA`](load-data.md), even when using the strategies just outlined.
- To increase performance for `MyISAM` tables, for both [`LOAD DATA`](load-data.md) and [`INSERT`](insert.md), enlarge the key cache by increasing the [`key_buffer_size`](server-system-variables.md) system variable. See [Section 7.1.1, “Configuring the Server”](server-configuration.md).