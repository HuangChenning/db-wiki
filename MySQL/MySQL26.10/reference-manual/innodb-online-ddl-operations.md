---
title: "MySQL :: MySQL 26.10 Reference Manual :: 17.12.1 Online DDL Operations"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/innodb-online-ddl-operations.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 17.12.1 Online DDL Operations

Online support details, syntax examples, and usage notes for DDL operations are provided under the following topics in this section.

#### Index Operations

The following table provides an overview of online DDL support for index operations. An asterisk indicates additional information, an exception, or a dependency. For details, see Syntax and Usage Notes.

**Table 17.13 Online DDL Support for Index Operations**

| Operation | Instant | In Place | Rebuilds Table | Permits Concurrent DML | Only Modifies Metadata |
| --- | --- | --- | --- | --- | --- |
| Creating or adding a secondary index | No | Yes | No | Yes | No |
| Dropping an index | No | Yes | No | Yes | Yes |
| Renaming an index | No | Yes | No | Yes | Yes |
| Adding a `FULLTEXT` index | No | Yes\* | No\* | No | No |
| Adding a `SPATIAL` index | No | Yes | No | No | No |
| Changing the index type | Yes | Yes | No | Yes | Yes |

##### Syntax and Usage Notes

- Creating or adding a secondary index
	```sql
	CREATE INDEX name ON table (col_list);
	```
	```sql
	ALTER TABLE tbl_name ADD INDEX name (col_list);
	```
	The table remains available for read and write operations while the index is being created. The [`CREATE INDEX`](create-index.md) statement only finishes after all transactions that are accessing the table are completed, so that the initial state of the index reflects the most recent contents of the table.
	Online DDL support for adding secondary indexes means that you can generally speed the overall process of creating and loading a table and associated indexes by creating the table without secondary indexes, then adding secondary indexes after the data is loaded.
	A newly created secondary index contains only the committed data in the table at the time the [`CREATE INDEX`](create-index.md) or [`ALTER TABLE`](alter-table.md) statement finishes executing. It does not contain any uncommitted values, old versions of values, or values marked for deletion but not yet removed from the old index.
	Some factors affect the performance, space usage, and semantics of this operation. For details, see [Section 17.12.8, “Online DDL Limitations”](innodb-online-ddl-limitations.md).
- Dropping an index
	```sql
	DROP INDEX name ON table;
	```
	```sql
	ALTER TABLE tbl_name DROP INDEX name;
	```
	The table remains available for read and write operations while the index is being dropped. The [`DROP INDEX`](drop-index.md) statement only finishes after all transactions that are accessing the table are completed, so that the initial state of the index reflects the most recent contents of the table.
- Renaming an index
	```sql
	ALTER TABLE tbl_name RENAME INDEX old_index_name TO new_index_name, ALGORITHM=INPLACE, LOCK=NONE;
	```
- Adding a `FULLTEXT` index
	```sql
	CREATE FULLTEXT INDEX name ON table(column);
	```
	Adding the first `FULLTEXT` index rebuilds the table if there is no user-defined `FTS_DOC_ID` column. Additional `FULLTEXT` indexes may be added without rebuilding the table.
- Adding a `SPATIAL` index
	```sql
	CREATE TABLE geom (g GEOMETRY NOT NULL);
	ALTER TABLE geom ADD SPATIAL INDEX(g), ALGORITHM=INPLACE, LOCK=SHARED;
	```
- Changing the index type (`USING {BTREE |             HASH}`)
	```sql
	ALTER TABLE tbl_name DROP INDEX i1, ADD INDEX i1(key_part,...) USING BTREE, ALGORITHM=INSTANT;
	```

#### Primary Key Operations

The following table provides an overview of online DDL support for primary key operations. An asterisk indicates additional information, an exception, or a dependency. See Syntax and Usage Notes.

**Table 17.14 Online DDL Support for Primary Key Operations**

| Operation | Instant | In Place | Rebuilds Table | Permits Concurrent DML | Only Modifies Metadata |
| --- | --- | --- | --- | --- | --- |
| Adding a primary key | No | Yes\* | Yes\* | Yes | No |
| Dropping a primary key | No | No | Yes | No | No |
| Dropping a primary key and adding another | No | Yes | Yes | Yes | No |

##### Syntax and Usage Notes

- Adding a primary key
	```sql
	ALTER TABLE tbl_name ADD PRIMARY KEY (column), ALGORITHM=INPLACE, LOCK=NONE;
	```
	Rebuilds the table in place. Data is reorganized substantially, making it an expensive operation. `ALGORITHM=INPLACE` is not permitted under certain conditions if columns have to be converted to `NOT NULL`.
	Restructuring the [clustered index](glossary.md) always requires copying of table data. Thus, it is best to define the [primary key](glossary.md) when you create a table, rather than issuing `ALTER TABLE ... ADD PRIMARY KEY` later.
	When you create a `UNIQUE` or `PRIMARY KEY` index, MySQL must do some extra work. For `UNIQUE` indexes, MySQL checks that the table contains no duplicate values for the key. For a `PRIMARY KEY` index, MySQL also checks that none of the `PRIMARY KEY` columns contains a `NULL`.
	When you add a primary key using the `ALGORITHM=COPY` clause, MySQL converts `NULL` values in the associated columns to default values: 0 for numbers, an empty string for character-based columns and BLOBs, and 0000-00-00 00:00:00 for `DATETIME`. This is a non-standard behavior that Oracle recommends you not rely on. Adding a primary key using `ALGORITHM=INPLACE` is only permitted when the [`SQL_MODE`](server-system-variables.md) setting includes the `strict_trans_tables` or `strict_all_tables` flags; when the `SQL_MODE` setting is strict, `ALGORITHM=INPLACE` is permitted, but the statement can still fail if the requested primary key columns contain `NULL` values. The `ALGORITHM=INPLACE` behavior is more standard-compliant.
	If you create a table without a primary key, `InnoDB` chooses one for you, which can be the first `UNIQUE` key defined on `NOT NULL` columns, or a system-generated key. To avoid uncertainty and the potential space requirement for an extra hidden column, specify the `PRIMARY KEY` clause as part of the [`CREATE TABLE`](create-table.md) statement.
	MySQL creates a new clustered index by copying the existing data from the original table to a temporary table that has the desired index structure. Once the data is completely copied to the temporary table, the original table is renamed with a different temporary table name. The temporary table comprising the new clustered index is renamed with the name of the original table, and the original table is dropped from the database.
	The online performance enhancements that apply to operations on secondary indexes do not apply to the primary key index. The rows of an InnoDB table are stored in a [clustered index](glossary.md) organized based on the [primary key](glossary.md), forming what some database systems call an “index-organized table”. Because the table structure is closely tied to the primary key, redefining the primary key still requires copying the data.
	When an operation on the primary key uses `ALGORITHM=INPLACE`, even though the data is still copied, it is more efficient than using `ALGORITHM=COPY` because:
	- No undo logging or associated redo logging is required for `ALGORITHM=INPLACE`. These operations add overhead to DDL statements that use `ALGORITHM=COPY`.
	- The secondary index entries are pre-sorted, and so can be loaded in order.
	- The change buffer is not used, because there are no random-access inserts into the secondary indexes.
- Dropping a primary key
	```sql
	ALTER TABLE tbl_name DROP PRIMARY KEY, ALGORITHM=COPY;
	```
	Only `ALGORITHM=COPY` supports dropping a primary key without adding a new one in the same `ALTER TABLE` statement.
- Dropping a primary key and adding another
	```sql
	ALTER TABLE tbl_name DROP PRIMARY KEY, ADD PRIMARY KEY (column), ALGORITHM=INPLACE, LOCK=NONE;
	```
	Data is reorganized substantially, making it an expensive operation.

#### Column Operations

The following table provides an overview of online DDL support for column operations. An asterisk indicates additional information, an exception, or a dependency. For details, see Syntax and Usage Notes.

**Table 17.15 Online DDL Support for Column Operations**

| Operation | Instant | In Place | Rebuilds Table | Permits Concurrent DML | Only Modifies Metadata |
| --- | --- | --- | --- | --- | --- |
| Adding a column | Yes\* | Yes | No\* | Yes\* | Yes |
| Dropping a column | Yes\* | Yes | Yes | Yes | Yes |
| Renaming a column | Yes\* | Yes | No | Yes\* | Yes |
| Reordering columns | No | Yes | Yes | Yes | No |
| Setting a column default value | Yes | Yes | No | Yes | Yes |
| Changing the column data type | No | No | Yes | No | No |
| Extending `VARCHAR` column size | No | Yes | No | Yes | Yes |
| Dropping the column default value | Yes | Yes | No | Yes | Yes |
| Changing the auto-increment value | No | Yes | No | Yes | No\* |
| Making a column `NULL` | No | Yes | Yes\* | Yes | No |
| Making a column `NOT NULL` | No | Yes\* | Yes\* | Yes | No |
| Modifying the definition of an `ENUM` or `SET` column | Yes | Yes | No | Yes | Yes |

##### Syntax and Usage Notes

- Adding a column
	```sql
	ALTER TABLE tbl_name ADD COLUMN column_name column_definition, ALGORITHM=INSTANT;
	```
	`INSTANT` is the default algorithm in MySQL 26.10.
	The following limitations apply when the `INSTANT` algorithm adds a column:
	- A statement cannot combine the addition of a column with other `ALTER TABLE` actions that do not support the `INSTANT` algorithm.
	- The `INSTANT` algorithm can add a column at any position in the table.
	- Columns cannot be added to tables that use `ROW_FORMAT=COMPRESSED`, tables with a `FULLTEXT` index, tables that reside in the data dictionary tablespace, or temporary tables. Temporary tables only support `ALGORITHM=COPY`.
	- MySQL checks the row size when the `INSTANT` algorithm adds a column, and throws the following error if the addition exceeds the limit.
		ERROR 4092 (HY000): Column can't be added with ALGORITHM=INSTANT as after this max possible row size crosses max permissible row size. Try ALGORITHM=INPLACE/COPY.
	- The maximum number of columns in the internal representation of the table cannot exceed 1022 after column addition with the `INSTANT` algorithm. The error message is:
		ERROR 4158 (HY000): Column can't be added to *`tbl_name`* with ALGORITHM=INSTANT anymore. Please try ALGORITHM=INPLACE/COPY
	- The `INSTANT` algorithm can not add or drop columns to system schema tables, such as the internal `mysql` table.
	- A column with a functional index cannot be dropped using the `INSTANT` algorithm.
	Multiple columns may be added in the same [`ALTER TABLE`](alter-table.md) statement. For example:
	```sql
	ALTER TABLE t1 ADD COLUMN c2 INT, ADD COLUMN c3 INT, ALGORITHM=INSTANT;
	```
	A new row version is created after each [`ALTER TABLE ...             ALGORITHM=INSTANT`](alter-table.md) operation that adds one or more columns, drops one or more columns, or adds and drops one or more columns in the same operation. The `INFORMATION_SCHEMA.INNODB_TABLES.TOTAL_ROW_VERSIONS` column tracks the number of row versions for a table. The value is incremented each time a column is instantly added or dropped. The initial value is 0.
	```sql
	mysql>  SELECT NAME, TOTAL_ROW_VERSIONS FROM INFORMATION_SCHEMA.INNODB_TABLES 
	        WHERE NAME LIKE 'test/t1';
	+---------+--------------------+
	| NAME    | TOTAL_ROW_VERSIONS |
	+---------+--------------------+
	| test/t1 |                  0 |
	+---------+--------------------+
	```
	When a table with instantly added or dropped columns is rebuilt by table-rebuilding [`ALTER TABLE             `](alter-table.md) or [`OPTIMIZE TABLE`](optimize-table.md) operation, the `TOTAL_ROW_VERSIONS` value is reset to 0. The maximum number of row versions permitted is 255, as each row version requires additional space for table metadata. When the row version limit is reached, `ADD COLUMN` and `DROP             COLUMN` operations using `ALGORITHM=INSTANT` are rejected with an error message that recommends rebuilding the table using the `COPY` or `INPLACE` algorithm.
	ERROR 4092 (HY000): Maximum row versions reached for table test/t1. No more columns can be added or dropped instantly. Please use COPY/INPLACE.
	The following [`INFORMATION_SCHEMA`](information-schema.md) columns provide additional metadata for instantly added columns. Refer to the descriptions of those columns for more information. See [Section 28.4.9, “The INFORMATION\_SCHEMA INNODB\_COLUMNS Table”](information-schema-innodb-columns-table.md), and [Section 28.4.23, “The INFORMATION\_SCHEMA INNODB\_TABLES Table”](information-schema-innodb-tables-table.md).
	- `INNODB_COLUMNS.DEFAULT_VALUE`
	- `INNODB_COLUMNS.HAS_DEFAULT`
	- `INNODB_TABLES.INSTANT_COLS`
	Concurrent DML is not permitted when adding an [auto-increment](glossary.md) column. Data is reorganized substantially, making it an expensive operation. At a minimum, `ALGORITHM=INPLACE, LOCK=SHARED` is required.
	The table is rebuilt if `ALGORITHM=INPLACE` is used to add a column.
- Dropping a column
	```sql
	ALTER TABLE tbl_name DROP COLUMN column_name, ALGORITHM=INSTANT;
	```
	`INSTANT` is the default algorithm in MySQL 26.10.
	The following limitations apply when the `INSTANT` algorithm is used to drop a column:
	- Dropping a column cannot be combined in the same statement with other [`ALTER                 TABLE`](alter-table.md) actions that do not support `ALGORITHM=INSTANT`.
	- Columns cannot be dropped from tables that use `ROW_FORMAT=COMPRESSED`, tables with a `FULLTEXT` index, tables that reside in the data dictionary tablespace, or temporary tables. Temporary tables only support `ALGORITHM=COPY`.
	Multiple columns may be dropped in the same [`ALTER TABLE`](alter-table.md) statement; for example:
	```sql
	ALTER TABLE t1 DROP COLUMN c4, DROP COLUMN c5, ALGORITHM=INSTANT;
	```
	Each time a column is added or dropped using `ALGORITHM=INSTANT`, a new row version is created. The `INFORMATION_SCHEMA.INNODB_TABLES.TOTAL_ROW_VERSIONS` column tracks the number of row versions for a table. The value is incremented each time a column is instantly added or dropped. The initial value is 0.
	```sql
	mysql>  SELECT NAME, TOTAL_ROW_VERSIONS FROM INFORMATION_SCHEMA.INNODB_TABLES 
	        WHERE NAME LIKE 'test/t1';
	+---------+--------------------+
	| NAME    | TOTAL_ROW_VERSIONS |
	+---------+--------------------+
	| test/t1 |                  0 |
	+---------+--------------------+
	```
	When a table with instantly added or dropped columns is rebuilt by table-rebuilding [`ALTER TABLE             `](alter-table.md) or [`OPTIMIZE TABLE`](optimize-table.md) operation, the `TOTAL_ROW_VERSIONS` value is reset to 0. The maximum number of row versions permitted is 255, as each row version requires additional space for table metadata. When the row version limit is reached, `ADD COLUMN` and `DROP             COLUMN` operations using `ALGORITHM=INSTANT` are rejected with an error message that recommends rebuilding the table using the `COPY` or `INPLACE` algorithm.
	ERROR 4092 (HY000): Maximum row versions reached for table test/t1. No more columns can be added or dropped instantly. Please use COPY/INPLACE.
	If an algorithm other than `ALGORITHM=INSTANT` is used, data is reorganized substantially, making it an expensive operation.
- Renaming a column
	```sql
	ALTER TABLE tbl CHANGE old_col_name new_col_name data_type, ALGORITHM=INSTANT;
	```
	To permit concurrent DML, keep the same data type and only change the column name.
	When you keep the same data type and `[NOT]             NULL` attribute, only changing the column name, the operation can always be performed online.
	Renaming a column referenced from another table is only permitted with `ALGORITHM=INPLACE`. If you use `ALGORITHM=INSTANT`, `ALGORITHM=COPY`, or some other condition that causes the operation to use those algorithms, the `ALTER TABLE` statement fails.
	`ALGORITHM=INSTANT` supports renaming a virtual column; `ALGORITHM=INPLACE` does not.
	`ALGORITHM=INSTANT` and `ALGORITHM=INPLACE` do not support renaming a column when adding or dropping a virtual column in the same statement. In this case, only `ALGORITHM=COPY` is supported.
- Reordering columns
	To reorder columns, use `FIRST` or `AFTER` in `CHANGE` or `MODIFY` operations.
	```sql
	ALTER TABLE tbl_name MODIFY COLUMN col_name column_definition FIRST, ALGORITHM=INPLACE, LOCK=NONE;
	```
	Data is reorganized substantially, making it an expensive operation.
- Changing the column data type
	```sql
	ALTER TABLE tbl_name CHANGE c1 c1 BIGINT, ALGORITHM=COPY;
	```
	Changing the column data type is only supported with `ALGORITHM=COPY`.
- Extending `VARCHAR` column size
	```sql
	ALTER TABLE tbl_name CHANGE COLUMN c1 c1 VARCHAR(255), ALGORITHM=INPLACE, LOCK=NONE;
	```
	The number of length bytes required by a [`VARCHAR`](char.md) column must remain the same. For [`VARCHAR`](char.md) columns of 0 to 255 bytes in size, one length byte is required to encode the value. For [`VARCHAR`](char.md) columns of 256 bytes in size or more, two length bytes are required. As a result, in-place [`ALTER             TABLE`](alter-table.md) only supports increasing [`VARCHAR`](char.md) column size from 0 to 255 bytes, or from 256 bytes to a greater size. In-place [`ALTER TABLE`](alter-table.md) does not support increasing the size of a [`VARCHAR`](char.md) column from less than 256 bytes to a size equal to or greater than 256 bytes. In this case, the number of required length bytes changes from 1 to 2, which is only supported by a table copy (`ALGORITHM=COPY`). For example, attempting to change [`VARCHAR`](char.md) column size for a single byte character set from VARCHAR(255) to VARCHAR(256) using in-place [`ALTER             TABLE`](alter-table.md) returns this error:
	```sql
	ALTER TABLE tbl_name ALGORITHM=INPLACE, CHANGE COLUMN c1 c1 VARCHAR(256);
	ERROR 0A000: ALGORITHM=INPLACE is not supported. Reason: Cannot change
	column type INPLACE. Try ALGORITHM=COPY.
	```
	Note
	The byte length of a `VARCHAR` column is dependant on the byte length of the character set.
	Decreasing [`VARCHAR`](char.md) size using in-place [`ALTER TABLE`](alter-table.md) is not supported. Decreasing [`VARCHAR`](char.md) size requires a table copy (`ALGORITHM=COPY`).
- Setting a column default value
	```sql
	ALTER TABLE tbl_name ALTER COLUMN col SET DEFAULT literal, ALGORITHM=INSTANT;
	```
	Only modifies table metadata. Default column values are stored in the [data dictionary](https://dev.mysql.com/doc/refman/8.4/en/glossary.html#glos_data_dictionary).
- Dropping a column default value
	```sql
	ALTER TABLE tbl ALTER COLUMN col DROP DEFAULT, ALGORITHM=INSTANT;
	```
- Changing the auto-increment value
	```sql
	ALTER TABLE table AUTO_INCREMENT=next_value, ALGORITHM=INPLACE, LOCK=NONE;
	```
	Modifies a value stored in memory, not the data file.
	In a distributed system using replication or sharding, you sometimes reset the auto-increment counter for a table to a specific value. The next row inserted into the table uses the specified value for its auto-increment column. You might also use this technique in a data warehousing environment where you periodically empty all the tables and reload them, and restart the auto-increment sequence from 1.
- Making a column `NULL`
	```sql
	ALTER TABLE tbl_name MODIFY COLUMN column_name data_type NULL, ALGORITHM=INPLACE, LOCK=NONE;
	```
	Rebuilds the table in place. Data is reorganized substantially, making it an expensive operation.
- Making a column `NOT NULL`
	```sql
	ALTER TABLE tbl_name MODIFY COLUMN column_name data_type NOT NULL, ALGORITHM=INPLACE, LOCK=NONE;
	```
	Rebuilds the table in place. `STRICT_ALL_TABLES` or `STRICT_TRANS_TABLES` [`SQL_MODE`](server-system-variables.md) is required for the operation to succeed. The operation fails if the column contains NULL values. The server prohibits changes to foreign key columns that have the potential to cause loss of referential integrity. See [Section 15.1.11, “ALTER TABLE Statement”](alter-table.md). Data is reorganized substantially, making it an expensive operation.
- Modifying the definition of an `ENUM` or `SET` column
	```sql
	CREATE TABLE t1 (c1 ENUM('a', 'b', 'c'));
	ALTER TABLE t1 MODIFY COLUMN c1 ENUM('a', 'b', 'c', 'd'), ALGORITHM=INSTANT;
	```
	Modifying the definition of an [`ENUM`](enum.md) or [`SET`](set.md) column by adding new enumeration or set members to the *end* of the list of valid member values may be performed instantly or in place, as long as the storage size of the data type does not change. For example, adding a member to a [`SET`](set.md) column that has 8 members changes the required storage per value from 1 byte to 2 bytes; this requires a table copy. Adding members in the middle of the list causes renumbering of existing members, which requires a table copy.

#### Generated Column Operations

The following table provides an overview of online DDL support for generated column operations. For details, see Syntax and Usage Notes.

**Table 17.16 Online DDL Support for Generated Column Operations**

| Operation | Instant | In Place | Rebuilds Table | Permits Concurrent DML | Only Modifies Metadata |
| --- | --- | --- | --- | --- | --- |
| Adding a `STORED` column | No | No | Yes | No | No |
| Modifying `STORED` column order | No | No | Yes | No | No |
| Dropping a `STORED` column | No | Yes | Yes | Yes | No |
| Adding a `VIRTUAL` column | Yes | Yes | No | Yes | Yes |
| Modifying `VIRTUAL` column order | No | No | Yes | No | No |
| Dropping a `VIRTUAL` column | Yes | Yes | No | Yes | Yes |

##### Syntax and Usage Notes

- Adding a `STORED` column
	```sql
	ALTER TABLE t1 ADD COLUMN (c2 INT GENERATED ALWAYS AS (c1 + 1) STORED), ALGORITHM=COPY;
	```
	`ADD COLUMN` is not an in-place operation for stored columns (done without using a temporary table) because the expression must be evaluated by the server.
- Modifying `STORED` column order
	```sql
	ALTER TABLE t1 MODIFY COLUMN c2 INT GENERATED ALWAYS AS (c1 + 1) STORED FIRST, ALGORITHM=COPY;
	```
	Rebuilds the table in place.
- Dropping a `STORED` column
	```sql
	ALTER TABLE t1 DROP COLUMN c2, ALGORITHM=INPLACE, LOCK=NONE;
	```
	Rebuilds the table in place.
- Adding a `VIRTUAL` column
	```sql
	ALTER TABLE t1 ADD COLUMN (c2 INT GENERATED ALWAYS AS (c1 + 1) VIRTUAL), ALGORITHM=INSTANT;
	```
	Adding a virtual column can be performed instantly or in place for non-partitioned tables.
	Adding a `VIRTUAL` is not an in-place operation for partitioned tables.
- Modifying `VIRTUAL` column order
	```sql
	ALTER TABLE t1 MODIFY COLUMN c2 INT GENERATED ALWAYS AS (c1 + 1) VIRTUAL FIRST, ALGORITHM=COPY;
	```
- Dropping a `VIRTUAL` column
	```sql
	ALTER TABLE t1 DROP COLUMN c2, ALGORITHM=INSTANT;
	```
	Dropping a `VIRTUAL` column can be performed instantly or in place for non-partitioned tables.

#### Foreign Key Operations

The following table provides an overview of online DDL support for foreign key operations. An asterisk indicates additional information, an exception, or a dependency. For details, see Syntax and Usage Notes.

**Table 17.17 Online DDL Support for Foreign Key Operations**

| Operation | Instant | In Place | Rebuilds Table | Permits Concurrent DML | Only Modifies Metadata |
| --- | --- | --- | --- | --- | --- |
| Adding a foreign key constraint | No | Yes\* | No | Yes | Yes |
| Dropping a foreign key constraint | No | Yes | No | Yes | Yes |

##### Syntax and Usage Notes

- Adding a foreign key constraint
	The `INPLACE` algorithm is supported when [`foreign_key_checks`](server-system-variables.md) is disabled. Otherwise, only the `COPY` algorithm is supported.
	```sql
	ALTER TABLE tbl1 ADD CONSTRAINT fk_name FOREIGN KEY index (col1)
	  REFERENCES tbl2(col2) referential_actions;
	```
- Dropping a foreign key constraint
	```sql
	ALTER TABLE tbl DROP FOREIGN KEY fk_name;
	```
	Dropping a foreign key can be performed online with the [`foreign_key_checks`](server-system-variables.md) option enabled or disabled.
	If you do not know the names of the foreign key constraints on a particular table, issue the following statement and find the constraint name in the `CONSTRAINT` clause for each foreign key:
	```sql
	SHOW CREATE TABLE table\G
	```
	Or, query the Information Schema [`TABLE_CONSTRAINTS`](information-schema-table-constraints-table.md) table and use the `CONSTRAINT_NAME` and `CONSTRAINT_TYPE` columns to identify the foreign key names.
	You can also drop a foreign key and its associated index in a single statement:
	```sql
	ALTER TABLE table DROP FOREIGN KEY constraint, DROP INDEX index;
	```

Note

If [foreign keys](glossary.md) are already present in the table being altered (that is, it is a [child table](glossary.md) containing a `FOREIGN KEY ... REFERENCE` clause), additional restrictions apply to online DDL operations, even those not directly involving the foreign key columns:

- An [`ALTER TABLE`](alter-table.md) on the child table could wait for another transaction to commit, if a change to the parent table causes associated changes in the child table through an `ON UPDATE` or `ON DELETE` clause using the `CASCADE` or `SET NULL` parameters.
- In the same way, if a table is the [parent table](glossary.md) in a foreign key relationship, even though it does not contain any `FOREIGN KEY` clauses, it could wait for the [`ALTER TABLE`](alter-table.md) to complete if an [`INSERT`](insert.md), [`UPDATE`](update.md), or [`DELETE`](delete.md) statement causes an `ON UPDATE` or `ON               DELETE` action in the child table.

#### Table Operations

The following table provides an overview of online DDL support for table operations. An asterisk indicates additional information, an exception, or a dependency. For details, see Syntax and Usage Notes.

**Table 17.18 Online DDL Support for Table Operations**

| Operation | Instant | In Place | Rebuilds Table | Permits Concurrent DML | Only Modifies Metadata |
| --- | --- | --- | --- | --- | --- |
| Changing the `ROW_FORMAT` | No | Yes | Yes | Yes | No |
| Changing the `KEY_BLOCK_SIZE` | No | Yes | Yes | Yes | No |
| Setting persistent table statistics | No | Yes | No | Yes | Yes |
| Specifying a character set | No | Yes | Yes\* | Yes | No |
| Converting a character set | No | Yes | Yes\* | No | No |
| Optimizing a table | No | Yes\* | Yes | Yes | No |
| Rebuilding with the `FORCE` option | No | Yes\* | Yes | Yes | No |
| Performing a null rebuild | No | Yes\* | Yes | Yes | No |
| Renaming a table | Yes | Yes | No | Yes | Yes |

##### Syntax and Usage Notes

- Changing the `ROW_FORMAT`
	```sql
	ALTER TABLE tbl_name ROW_FORMAT = row_format, ALGORITHM=INPLACE, LOCK=NONE;
	```
	Data is reorganized substantially, making it an expensive operation.
	For additional information about the `ROW_FORMAT` option, see [Table Options](create-table.md).
- Changing the `KEY_BLOCK_SIZE`
	```sql
	ALTER TABLE tbl_name KEY_BLOCK_SIZE = value, ALGORITHM=INPLACE, LOCK=NONE;
	```
	Data is reorganized substantially, making it an expensive operation.
	For additional information about the `KEY_BLOCK_SIZE` option, see [Table Options](create-table.md).
- Setting persistent table statistics options
	```sql
	ALTER TABLE tbl_name STATS_PERSISTENT=0, STATS_SAMPLE_PAGES=20, STATS_AUTO_RECALC=1, ALGORITHM=INPLACE, LOCK=NONE;
	```
	Only modifies table metadata.
	Persistent statistics include `STATS_PERSISTENT`, `STATS_AUTO_RECALC`, and `STATS_SAMPLE_PAGES`. For more information, see [Section 17.8.10.1, “Configuring Persistent Optimizer Statistics Parameters”](innodb-persistent-stats.md).
- Specifying a character set
	```sql
	ALTER TABLE tbl_name CHARACTER SET = charset_name, ALGORITHM=INPLACE, LOCK=NONE;
	```
	Rebuilds the table if the new character encoding is different.
- Converting a character set
	```sql
	ALTER TABLE tbl_name CONVERT TO CHARACTER SET charset_name, ALGORITHM=INPLACE, LOCK=NONE;
	```
	Rebuilds the table if the new character encoding is different.
- Optimizing a table
	```sql
	OPTIMIZE TABLE tbl_name;
	```
	In-place operation is not supported for tables with `FULLTEXT` indexes. The operation uses the `INPLACE` algorithm, but `ALGORITHM` and `LOCK` syntax is not permitted.
- Rebuilding a table with the `FORCE` option
	```sql
	ALTER TABLE tbl_name FORCE, ALGORITHM=INPLACE, LOCK=NONE;
	```
	Uses `ALGORITHM=INPLACE` as of MySQL 5.6.17. `ALGORITHM=INPLACE` is not supported for tables with `FULLTEXT` indexes.
- Performing a "null" rebuild
	```sql
	ALTER TABLE tbl_name ENGINE=InnoDB, ALGORITHM=INPLACE, LOCK=NONE;
	```
	Uses `ALGORITHM=INPLACE` as of MySQL 5.6.17. `ALGORITHM=INPLACE` is not supported for tables with `FULLTEXT` indexes.
- Renaming a table
	```sql
	ALTER TABLE old_tbl_name RENAME TO new_tbl_name, ALGORITHM=INSTANT;
	```
	Renaming a table can be performed instantly or in place. MySQL renames files that correspond to the table *`tbl_name`* without making a copy. (You can also use the [`RENAME             TABLE`](rename-table.md) statement to rename tables. See [Section 15.1.43, “RENAME TABLE Statement”](rename-table.md).) Privileges granted specifically for the renamed table are not migrated to the new name. They must be changed manually.

#### Tablespace Operations

The following table provides an overview of online DDL support for tablespace operations. For details, see Syntax and Usage Notes.

**Table 17.19 Online DDL Support for Tablespace Operations**

| Operation | Instant | In Place | Rebuilds Table | Permits Concurrent DML | Only Modifies Metadata |
| --- | --- | --- | --- | --- | --- |
| Renaming a general tablespace | No | Yes | No | Yes | Yes |
| Enabling or disabling general tablespace encryption | No | Yes | No | Yes | No |
| Enabling or disabling file-per-table tablespace encryption | No | No | Yes | No | No |

##### Syntax and Usage Notes

- Renaming a general tablespace
	```sql
	ALTER TABLESPACE tablespace_name RENAME TO new_tablespace_name;
	```
	[`ALTER             TABLESPACE ... RENAME TO`](alter-tablespace.md) uses the `INPLACE` algorithm but does not support the `ALGORITHM` clause.
- Enabling or disabling general tablespace encryption
	```sql
	ALTER TABLESPACE tablespace_name ENCRYPTION='Y';
	```
	[`ALTER             TABLESPACE ... ENCRYPTION`](alter-tablespace.md) uses the `INPLACE` algorithm but does not support the `ALGORITHM` clause.
	For related information, see [Section 17.13, “InnoDB Data-at-Rest Encryption”](innodb-data-encryption.md).
- Enabling or disabling file-per-table tablespace encryption
	```sql
	ALTER TABLE tbl_name ENCRYPTION='Y', ALGORITHM=COPY;
	```
	For related information, see [Section 17.13, “InnoDB Data-at-Rest Encryption”](innodb-data-encryption.md).

#### Partitioning Operations

With the exception of some [`ALTER         TABLE`](alter-table.md) partitioning clauses, online DDL operations for partitioned `InnoDB` tables follow the same rules that apply to regular `InnoDB` tables.

Some [`ALTER TABLE`](alter-table.md) partitioning clauses do not go through the same internal online DDL API as regular non-partitioned `InnoDB` tables. As a result, online support for [`ALTER         TABLE`](alter-table.md) partitioning clauses varies.

The following table shows the online status for each `ALTER TABLE` partitioning statement. Regardless of the online DDL API that is used, MySQL attempts to minimize data copying and locking where possible.

[`ALTER TABLE`](alter-table.md) partitioning options that use `ALGORITHM=COPY` or that only permit “ `ALGORITHM=DEFAULT,         LOCK=DEFAULT` ”, repartition the table using the `COPY` algorithm. In other words, a new partitioned table is created with the new partitioning scheme. The newly created table includes any changes applied by the [`ALTER TABLE`](alter-table.md) statement, and table data is copied into the new table structure.

**Table 17.20 Online DDL Support for Partitioning Operations**

| Partitioning Clause | Instant | In Place | Permits DML | Notes |
| --- | --- | --- | --- | --- |
| [`PARTITION BY`](alter-table.md) | No | No | No | Permits `ALGORITHM=COPY`, `LOCK={DEFAULT\|SHARED\|EXCLUSIVE}` |
| [`ADD PARTITION`](alter-table.md) | No | Yes\* | Yes\* | `ALGORITHM=INPLACE,               LOCK={DEFAULT\|NONE\|SHARED\|EXCLUSISVE}` is supported for `RANGE` and `LIST` partitions, `ALGORITHM=INPLACE,               LOCK={DEFAULT\|SHARED\|EXCLUSISVE}` for `HASH` and `KEY` partitions, and `ALGORITHM=COPY,               LOCK={SHARED\|EXCLUSIVE}` for all partition types. Does not copy existing data for tables partitioned by `RANGE` or `LIST`. Concurrent queries are permitted with `ALGORITHM=COPY` for tables partitioned by `HASH` or `LIST`, as MySQL copies the data while holding a shared lock. |
| [`DROP PARTITION`](alter-table.md) | No | Yes\* | Yes\* | `ALGORITHM=INPLACE,                 LOCK={DEFAULT\|NONE\|SHARED\|EXCLUSIVE}` is supported. Does not copy data for tables partitioned by `RANGE` or `LIST`.  `DROP PARTITION` with `ALGORITHM=INPLACE` deletes data stored in the partition and drops the partition. However, `DROP PARTITION` with `ALGORITHM=COPY` or [`old_alter_table=ON`](server-system-variables.md) rebuilds the partitioned table and attempts to move data from the dropped partition to another partition with a compatible `PARTITION ... VALUES` definition. Data that cannot be moved to another partition is deleted. |
| [`DISCARD PARTITION`](alter-table.md) | No | No | No | Only permits `ALGORITHM=DEFAULT`, `LOCK=DEFAULT` |
| [`IMPORT PARTITION`](alter-table.md) | No | No | No | Only permits `ALGORITHM=DEFAULT`, `LOCK=DEFAULT` |
| [`TRUNCATE               PARTITION`](alter-table.md) | No | Yes | Yes | Does not copy existing data. It merely deletes rows; it does not alter the definition of the table itself, or of any of its partitions. |
| [`COALESCE               PARTITION`](alter-table.md) | No | Yes\* | No | `ALGORITHM=INPLACE, LOCK={DEFAULT\|SHARED\|EXCLUSIVE}` is supported. |
| [`REORGANIZE               PARTITION`](alter-table.md) | No | Yes\* | No | `ALGORITHM=INPLACE, LOCK={DEFAULT\|SHARED\|EXCLUSIVE}` is supported. |
| [`EXCHANGE               PARTITION`](alter-table.md) | No | Yes | Yes |  |
| [`ANALYZE PARTITION`](alter-table.md) | No | Yes | Yes |  |
| [`CHECK PARTITION`](alter-table.md) | No | Yes | Yes |  |
| [`OPTIMIZE               PARTITION`](alter-table.md) | No | No | No | `ALGORITHM` and `LOCK` clauses are ignored. Rebuilds the entire table. See [Section 26.3.4, “Maintenance of Partitions”](partitioning-maintenance.md). |
| [`REBUILD PARTITION`](alter-table.md) | No | Yes\* | No | `ALGORITHM=INPLACE, LOCK={DEFAULT\|SHARED\|EXCLUSIVE}` is supported. |
| [`REPAIR PARTITION`](alter-table.md) | No | Yes | Yes |  |
| [`REMOVE               PARTITIONING`](alter-table.md) | No | No | No | Permits `ALGORITHM=COPY`, `LOCK={DEFAULT\|SHARED\|EXCLUSIVE}` |

Non-partitioning online [`ALTER         TABLE`](alter-table.md) operations on partitioned tables follow the same rules that apply to regular tables. However, [`ALTER TABLE`](alter-table.md) performs online operations on each table partition, which causes increased demand on system resources due to operations being performed on multiple partitions.

For additional information about [`ALTER         TABLE`](alter-table.md) partitioning clauses, see [Partitioning Options](alter-table.md), and [Section 15.1.11.1, “ALTER TABLE Partition Operations”](alter-table-partition-operations.md). For information about partitioning in general, see [Chapter 26, *Partitioning*](partitioning.md).