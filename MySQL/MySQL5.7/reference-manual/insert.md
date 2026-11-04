---
title: "13.2.5 INSERT Statement"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/insert.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 13.2.5 INSERT Statement

```
INSERT [LOW_PRIORITY | DELAYED | HIGH_PRIORITY] [IGNORE]
    [INTO] tbl_name
    [PARTITION (partition_name [, partition_name] ...)]
    [(col_name [, col_name] ...)]
    {VALUES | VALUE} (value_list) [, (value_list)] ...
    [ON DUPLICATE KEY UPDATE assignment_list]

INSERT [LOW_PRIORITY | DELAYED | HIGH_PRIORITY] [IGNORE]
    [INTO] tbl_name
    [PARTITION (partition_name [, partition_name] ...)]
    SET assignment_list
    [ON DUPLICATE KEY UPDATE assignment_list]

INSERT [LOW_PRIORITY | HIGH_PRIORITY] [IGNORE]
    [INTO] tbl_name
    [PARTITION (partition_name [, partition_name] ...)]
    [(col_name [, col_name] ...)]
    SELECT ...
    [ON DUPLICATE KEY UPDATE assignment_list]

value:
    {expr | DEFAULT}

value_list:
    value [, value] ...

assignment:
    col_name = value

assignment_list:
    assignment [, assignment] ...
```

`INSERT` inserts new rows into an existing table. The `INSERT       ... VALUES` and `INSERT ... SET` forms of the statement insert rows based on explicitly specified values. The [`INSERT       ... SELECT`](insert-select.md) form inserts rows selected from another table or tables. `INSERT` with an `ON DUPLICATE KEY UPDATE` clause enables existing rows to be updated if a row to be inserted would cause a duplicate value in a `UNIQUE` index or `PRIMARY       KEY`.

For additional information about [`INSERT ...       SELECT`](insert-select.md) and [`INSERT ... ON       DUPLICATE KEY UPDATE`](insert-on-duplicate.md), see [Section 13.2.5.1, “INSERT... SELECT Statement”](insert-select.md), and [Section 13.2.5.2, “INSERT... ON DUPLICATE KEY UPDATE Statement”](insert-on-duplicate.md).

In MySQL 5.7, the `DELAYED` keyword is accepted but ignored by the server. For the reasons for this, see [Section 13.2.5.3, “INSERT DELAYED Statement”](insert-delayed.md),

Inserting into a table requires the [`INSERT`](privileges-provided.md) privilege for the table. If the `ON DUPLICATE KEY UPDATE` clause is used and a duplicate key causes an [`UPDATE`](update.md) to be performed instead, the statement requires the [`UPDATE`](privileges-provided.md) privilege for the columns to be updated. For columns that are read but not modified you need only the [`SELECT`](privileges-provided.md) privilege (such as for a column referenced only on the right hand side of an *`col_name`* = *`expr`* assignment in an `ON DUPLICATE KEY UPDATE` clause).

When inserting into a partitioned table, you can control which partitions and subpartitions accept new rows. The `PARTITION` clause takes a list of the comma-separated names of one or more partitions or subpartitions (or both) of the table. If any of the rows to be inserted by a given `INSERT` statement do not match one of the partitions listed, the `INSERT` statement fails with the error Found a row not matching the given partition set. For more information and examples, see [Section 22.5, “Partition Selection”](partitioning-selection.md).

*`tbl_name`* is the table into which rows should be inserted. Specify the columns for which the statement provides values as follows:

- Provide a parenthesized list of comma-separated column names following the table name. In this case, a value for each named column must be provided by the `VALUES` list or the [`SELECT`](select.md) statement.
- If you do not specify a list of column names for `INSERT ...           VALUES` or [`INSERT ...           SELECT`](insert-select.md), values for every column in the table must be provided by the `VALUES` list or the [`SELECT`](select.md) statement. If you do not know the order of the columns in the table, use ``DESCRIBE           *`tbl_name`*`` to find out.
- A `SET` clause indicates columns explicitly by name, together with the value to assign each one.

Column values can be given in several ways:

- If strict SQL mode is not enabled, any column not explicitly given a value is set to its default (explicit or implicit) value. For example, if you specify a column list that does not name all the columns in the table, unnamed columns are set to their default values. Default value assignment is described in [Section 11.6, “Data Type Default Values”](data-type-defaults.md). See also [Section 1.6.3.3, “Constraints on Invalid Data”](constraint-invalid-data.md).
	If strict SQL mode is enabled, an `INSERT` statement generates an error if it does not specify an explicit value for every column that has no default value. See [Section 5.1.10, “Server SQL Modes”](sql-mode.md).
- If both the column list and the `VALUES` list are empty, `INSERT` creates a row with each column set to its default value:
	```
	INSERT INTO tbl_name () VALUES();
	```
	If strict mode is not enabled, MySQL uses the implicit default value for any column that has no explicitly defined default. If strict mode is enabled, an error occurs if any column has no default value.
- Use the keyword `DEFAULT` to set a column explicitly to its default value. This makes it easier to write `INSERT` statements that assign values to all but a few columns, because it enables you to avoid writing an incomplete `VALUES` list that does not include a value for each column in the table. Otherwise, you must provide the list of column names corresponding to each value in the `VALUES` list.
- If a generated column is inserted into explicitly, the only permitted value is `DEFAULT`. For information about generated columns, see [Section 13.1.18.7, “CREATE TABLE and Generated Columns”](create-table-generated-columns.md).
- In expressions, you can use [``DEFAULT(*`col_name`*)``](miscellaneous-functions.md) to produce the default value for column *`col_name`*.
- Type conversion of an expression *`expr`* that provides a column value might occur if the expression data type does not match the column data type. Conversion of a given value can result in different inserted values depending on the column type. For example, inserting the string `'1999.0e-2'` into an [`INT`](integer-types.md), [`FLOAT`](floating-point-types.md), [`DECIMAL(10,6)`](fixed-point-types.md), or [`YEAR`](year.md) column inserts the value `1999`, `19.9921`, `19.992100`, or `1999`, respectively. The value stored in the [`INT`](integer-types.md) and [`YEAR`](year.md) columns is `1999` because the string-to-number conversion looks only at as much of the initial part of the string as may be considered a valid integer or year. For the [`FLOAT`](floating-point-types.md) and [`DECIMAL`](fixed-point-types.md) columns, the string-to-number conversion considers the entire string a valid numeric value.
- An expression *`expr`* can refer to any column that was set earlier in a value list. For example, you can do this because the value for `col2` refers to `col1`, which has previously been assigned:
	```
	INSERT INTO tbl_name (col1,col2) VALUES(15,col1*2);
	```
	But the following is not legal, because the value for `col1` refers to `col2`, which is assigned after `col1`:
	```
	INSERT INTO tbl_name (col1,col2) VALUES(col2*2,15);
	```
	An exception occurs for columns that contain `AUTO_INCREMENT` values. Because `AUTO_INCREMENT` values are generated after other value assignments, any reference to an `AUTO_INCREMENT` column in the assignment returns a `0`.

`INSERT` statements that use `VALUES` syntax can insert multiple rows. To do this, include multiple lists of comma-separated column values, with lists enclosed within parentheses and separated by commas. Example:

```
INSERT INTO tbl_name (a,b,c) VALUES(1,2,3),(4,5,6),(7,8,9);
```

Each values list must contain exactly as many values as are to be inserted per row. The following statement is invalid because it contains one list of nine values, rather than three lists of three values each:

```
INSERT INTO tbl_name (a,b,c) VALUES(1,2,3,4,5,6,7,8,9);
```

`VALUE` is a synonym for `VALUES` in this context. Neither implies anything about the number of values lists, nor about the number of values per list. Either may be used whether there is a single values list or multiple lists, and regardless of the number of values per list.

The affected-rows value for an `INSERT` can be obtained using the [`ROW_COUNT()`](information-functions.md) SQL function or the [`mysql_affected_rows()`](https://docs.oracle.com/cd/E17952_01/c-api-5.7-en/mysql-affected-rows.html) C API function. See [Section 12.15, “Information Functions”](information-functions.md), and [mysql\_affected\_rows()](https://docs.oracle.com/cd/E17952_01/c-api-5.7-en/mysql-affected-rows.html).

If you use an `INSERT ...       VALUES` statement with multiple value lists or [`INSERT ...       SELECT`](insert-select.md), the statement returns an information string in this format:

```
Records: N1 Duplicates: N2 Warnings: N3
```

If you are using the C API, the information string can be obtained by invoking the [`mysql_info()`](https://docs.oracle.com/cd/E17952_01/c-api-5.7-en/mysql-info.html) function. See [mysql\_info()](https://docs.oracle.com/cd/E17952_01/c-api-5.7-en/mysql-info.html).

`Records` indicates the number of rows processed by the statement. (This is not necessarily the number of rows actually inserted because `Duplicates` can be nonzero.) `Duplicates` indicates the number of rows that could not be inserted because they would duplicate some existing unique index value. `Warnings` indicates the number of attempts to insert column values that were problematic in some way. Warnings can occur under any of the following conditions:

- Inserting `NULL` into a column that has been declared `NOT NULL`. For multiple-row `INSERT` statements or [`INSERT INTO ...           SELECT`](insert-select.md) statements, the column is set to the implicit default value for the column data type. This is `0` for numeric types, the empty string (`''`) for string types, and the “zero” value for date and time types. [`INSERT INTO ...           SELECT`](insert-select.md) statements are handled the same way as multiple-row inserts because the server does not examine the result set from the [`SELECT`](select.md) to see whether it returns a single row. (For a single-row `INSERT`, no warning occurs when `NULL` is inserted into a `NOT           NULL` column. Instead, the statement fails with an error.)
- Setting a numeric column to a value that lies outside the column range. The value is clipped to the closest endpoint of the range.
- Assigning a value such as `'10.34 a'` to a numeric column. The trailing nonnumeric text is stripped off and the remaining numeric part is inserted. If the string value has no leading numeric part, the column is set to `0`.
- Inserting a string into a string column ([`CHAR`](char.md), [`VARCHAR`](char.md), [`TEXT`](blob.md), or [`BLOB`](blob.md)) that exceeds the column maximum length. The value is truncated to the column maximum length.
- Inserting a value into a date or time column that is illegal for the data type. The column is set to the appropriate zero value for the type.
- For `INSERT` examples involving `AUTO_INCREMENT` column values, see [Section 3.6.9, “Using AUTO\_INCREMENT”](example-auto-increment.md).
	If `INSERT` inserts a row into a table that has an `AUTO_INCREMENT` column, you can find the value used for that column by using the [`LAST_INSERT_ID()`](information-functions.md) SQL function or the [`mysql_insert_id()`](https://docs.oracle.com/cd/E17952_01/c-api-5.7-en/mysql-insert-id.html) C API function.
	Note
	These two functions do not always behave identically. The behavior of `INSERT` statements with respect to `AUTO_INCREMENT` columns is discussed further in [Section 12.15, “Information Functions”](information-functions.md), and [mysql\_insert\_id()](https://docs.oracle.com/cd/E17952_01/c-api-5.7-en/mysql-insert-id.html).

The `INSERT` statement supports the following modifiers:

- If you use the `LOW_PRIORITY` modifier, execution of the `INSERT` is delayed until no other clients are reading from the table. This includes other clients that began reading while existing clients are reading, and while the `INSERT           LOW_PRIORITY` statement is waiting. It is possible, therefore, for a client that issues an `INSERT           LOW_PRIORITY` statement to wait for a very long time.
	`LOW_PRIORITY` affects only storage engines that use only table-level locking (such as `MyISAM`, `MEMORY`, and `MERGE`).
	Note
	`LOW_PRIORITY` should normally not be used with `MyISAM` tables because doing so disables concurrent inserts. See [Section 8.11.3, “Concurrent Inserts”](concurrent-inserts.md).
- If you specify `HIGH_PRIORITY`, it overrides the effect of the [`--low-priority-updates`](server-system-variables.md) option if the server was started with that option. It also causes concurrent inserts not to be used. See [Section 8.11.3, “Concurrent Inserts”](concurrent-inserts.md).
	`HIGH_PRIORITY` affects only storage engines that use only table-level locking (such as `MyISAM`, `MEMORY`, and `MERGE`).
- If you use the `IGNORE` modifier, ignorable errors that occur while executing the `INSERT` statement are ignored. For example, without `IGNORE`, a row that duplicates an existing `UNIQUE` index or `PRIMARY KEY` value in the table causes a duplicate-key error and the statement is aborted. With `IGNORE`, the row is discarded and no error occurs. Ignored errors generate warnings instead.
	`IGNORE` has a similar effect on inserts into partitioned tables where no partition matching a given value is found. Without `IGNORE`, such `INSERT` statements are aborted with an error. When `INSERT           IGNORE` is used, the insert operation fails silently for rows containing the unmatched value, but inserts rows that are matched. For an example, see [Section 22.2.2, “LIST Partitioning”](partitioning-list.md).
	Data conversions that would trigger errors abort the statement if `IGNORE` is not specified. With `IGNORE`, invalid values are adjusted to the closest values and inserted; warnings are produced but the statement does not abort. You can determine with the [`mysql_info()`](https://docs.oracle.com/cd/E17952_01/c-api-5.7-en/mysql-info.html) C API function how many rows were actually inserted into the table.
	For more information, see [The Effect of IGNORE on Statement Execution](sql-mode.md).
	You can use [`REPLACE`](replace.md) instead of `INSERT` to overwrite old rows. [`REPLACE`](replace.md) is the counterpart to `INSERT           IGNORE` in the treatment of new rows that contain unique key values that duplicate old rows: The new rows replace the old rows rather than being discarded. See [Section 13.2.8, “REPLACE Statement”](replace.md).
- If you specify `ON DUPLICATE KEY UPDATE`, and a row is inserted that would cause a duplicate value in a `UNIQUE` index or `PRIMARY           KEY`, an [`UPDATE`](update.md) of the old row occurs. The affected-rows value per row is 1 if the row is inserted as a new row, 2 if an existing row is updated, and 0 if an existing row is set to its current values. If you specify the `CLIENT_FOUND_ROWS` flag to the [`mysql_real_connect()`](https://docs.oracle.com/cd/E17952_01/c-api-5.7-en/mysql-real-connect.html) C API function when connecting to [**mysqld**](mysqld.md), the affected-rows value is 1 (not 0) if an existing row is set to its current values. See [Section 13.2.5.2, “INSERT... ON DUPLICATE KEY UPDATE Statement”](insert-on-duplicate.md).
- [`INSERT DELAYED`](insert-delayed.md) was deprecated in MySQL 5.6, and is scheduled for eventual removal. In MySQL 5.7, the `DELAYED` modifier is accepted but ignored. Use `INSERT` (without `DELAYED`) instead. See [Section 13.2.5.3, “INSERT DELAYED Statement”](insert-delayed.md).

An `INSERT` statement affecting a partitioned table using a storage engine such as [`MyISAM`](myisam-storage-engine.md) that employs table-level locks locks only those partitions into which rows are actually inserted. (For storage engines such as [`InnoDB`](innodb-storage-engine.md) that employ row-level locking, no locking of partitions takes place.) For more information, see [Section 22.6.4, “Partitioning and Locking”](partitioning-limitations-locking.md).