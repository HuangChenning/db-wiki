---
title: "MySQL :: MySQL 26.10 Reference Manual :: 15.1.25 CREATE TABLE Statement"
book: MySQL 26.10 Reference Manual
version: "26.10"
source: "https://dev.mysql.com/doc/refman/26.10/en/create-table.html"
tags:
  - mysql
  - mysql-26.10
  - reference-manual
---

### 15.1.25 CREATE TABLE Statement

```sql
CREATE [TEMPORARY] TABLE [IF NOT EXISTS] tbl_name
    (create_definition,...)
    [table_options]
    [partition_options]

CREATE [TEMPORARY] TABLE [IF NOT EXISTS] tbl_name
    [(create_definition,...)]
    [table_options]
    [partition_options]
    [IGNORE | REPLACE]
    [AS] query_expression

CREATE [TEMPORARY] TABLE [IF NOT EXISTS] tbl_name
    { LIKE old_tbl_name | (LIKE old_tbl_name) }

create_definition: {
    col_name column_definition
  | {INDEX | KEY} [index_name] [index_type] (key_part,...)
      [index_option] ...
  | {FULLTEXT | SPATIAL} [INDEX | KEY] [index_name] (key_part,...)
      [index_option] ...
  | [CONSTRAINT [symbol]] PRIMARY KEY
      [index_type] (key_part,...)
      [index_option] ...
  | [CONSTRAINT [symbol]] UNIQUE [INDEX | KEY]
      [index_name] [index_type] (key_part,...)
      [index_option] ...
  | [CONSTRAINT [symbol]] FOREIGN KEY
      [index_name] (col_name,...)
      reference_definition
  | check_constraint_definition
}

column_definition: {
    data_type [NOT NULL | NULL] [DEFAULT {literal | (expr)} ]
      [VISIBLE | INVISIBLE]
      [AUTO_INCREMENT] [UNIQUE [KEY]] [[PRIMARY] KEY]
      [COMMENT 'string']
      [COLLATE collation_name]
      [COLUMN_FORMAT {FIXED | DYNAMIC | DEFAULT}]
      [ENGINE_ATTRIBUTE [=] 'string']
      [SECONDARY_ENGINE_ATTRIBUTE [=] 'string']
      [STORAGE {DISK | MEMORY}]
      [reference_definition]
      [check_constraint_definition]
  | data_type
      [COLLATE collation_name]
      [GENERATED ALWAYS] AS (expr)
      [VIRTUAL | STORED] [NOT NULL | NULL]
      [VISIBLE | INVISIBLE]
      [UNIQUE [KEY]] [[PRIMARY] KEY]
      [COMMENT 'string']
      [reference_definition]
      [check_constraint_definition]
}

data_type:
    (see Chapter 13, Data Types)

key_part: {col_name [(length)] | (expr)} [ASC | DESC]

index_type:
    USING {BTREE | HASH}

index_option: {
    KEY_BLOCK_SIZE [=] value
  | index_type
  | WITH PARSER parser_name
  | COMMENT 'string'
  | {VISIBLE | INVISIBLE}
  |ENGINE_ATTRIBUTE [=] 'string'
  |SECONDARY_ENGINE_ATTRIBUTE [=] 'string'
}

check_constraint_definition:
    [CONSTRAINT [symbol]] CHECK (expr) [[NOT] ENFORCED]

reference_definition:
    REFERENCES tbl_name (key_part,...)
      [MATCH FULL | MATCH PARTIAL | MATCH SIMPLE]
      [ON DELETE reference_option]
      [ON UPDATE reference_option]

reference_option:
    RESTRICT | CASCADE | SET NULL | NO ACTION | SET DEFAULT

table_options:
    table_option [[,] table_option] ...

table_option: {
    AUTOEXTEND_SIZE [=] value
  | AUTO_INCREMENT [=] value
  | AVG_ROW_LENGTH [=] value
  | [DEFAULT] CHARACTER SET [=] charset_name
  | CHECKSUM [=] {0 | 1}
  | [DEFAULT] COLLATE [=] collation_name
  | COMMENT [=] 'string'
  | COMPRESSION [=] {'ZLIB' | 'LZ4' | 'NONE'}
  | CONNECTION [=] 'connect_string'
  | {DATA | INDEX} DIRECTORY [=] 'absolute path to directory'
  | DELAY_KEY_WRITE [=] {0 | 1}
  | ENCRYPTION [=] {'Y' | 'N'}
  | ENGINE [=] engine_name
  | ENGINE_ATTRIBUTE [=] 'string'
  | INSERT_METHOD [=] { NO | FIRST | LAST }
  | KEY_BLOCK_SIZE [=] value
  | MAX_ROWS [=] value
  | MIN_ROWS [=] value
  | PACK_KEYS [=] {0 | 1 | DEFAULT}
  | PASSWORD [=] 'string'
  | ROW_FORMAT [=] {DEFAULT | DYNAMIC | FIXED | COMPRESSED | REDUNDANT | COMPACT}
  | START TRANSACTION 
  | SECONDARY_ENGINE_ATTRIBUTE [=] 'string'
  | STATS_AUTO_RECALC [=] {DEFAULT | 0 | 1}
  | STATS_PERSISTENT [=] {DEFAULT | 0 | 1}
  | STATS_SAMPLE_PAGES [=] value
  | tablespace_option
  | UNION [=] (tbl_name[,tbl_name]...)
}

partition_options:
    PARTITION BY
        { [LINEAR] HASH(expr)
        | [LINEAR] KEY [ALGORITHM={1 | 2}] (column_list)
        | RANGE{(expr) | COLUMNS(column_list)}
        | LIST{(expr) | COLUMNS(column_list)} }
    [PARTITIONS num]
    [SUBPARTITION BY
        { [LINEAR] HASH(expr)
        | [LINEAR] KEY [ALGORITHM={1 | 2}] (column_list) }
      [SUBPARTITIONS num]
    ]
    [(partition_definition [, partition_definition] ...)]

partition_definition:
    PARTITION partition_name
        [VALUES
            {LESS THAN {(expr | value_list) | MAXVALUE}
            |
            IN (value_list)}]
        [[STORAGE] ENGINE [=] engine_name]
        [COMMENT [=] 'string' ]
        [DATA DIRECTORY [=] 'data_dir']
        [INDEX DIRECTORY [=] 'index_dir']
        [MAX_ROWS [=] max_number_of_rows]
        [MIN_ROWS [=] min_number_of_rows]
        [TABLESPACE [=] tablespace_name]
        [(subpartition_definition [, subpartition_definition] ...)]

subpartition_definition:
    SUBPARTITION logical_name
        [[STORAGE] ENGINE [=] engine_name]
        [COMMENT [=] 'string' ]
        [DATA DIRECTORY [=] 'data_dir']
        [INDEX DIRECTORY [=] 'index_dir']
        [MAX_ROWS [=] max_number_of_rows]
        [MIN_ROWS [=] min_number_of_rows]
        [TABLESPACE [=] tablespace_name]

tablespace_option:
    TABLESPACE tablespace_name [STORAGE DISK]
  | [TABLESPACE tablespace_name] STORAGE MEMORY

query_expression:
    SELECT ...   (Some valid select or union statement)
```

`CREATE TABLE` creates a table with the given name. You must have the [`CREATE`](privileges-provided.md) privilege for the table.

By default, tables are created in the default database, using the [`InnoDB`](innodb-storage-engine.md) storage engine. An error occurs if the table exists, if there is no default database, or if the database does not exist.

MySQL has no limit on the number of tables. The underlying file system may have a limit on the number of files that represent tables. Individual storage engines may impose engine-specific constraints. `InnoDB` permits up to 4 billion tables.

For information about the physical representation of a table, see [Section 15.1.25.1, “Files Created by CREATE TABLE”](create-table-files.md).

There are several aspects to the `CREATE       TABLE` statement, described under the following topics in this section:

#### Table Name

- ``*`tbl_name`*``
	The table name can be specified as *`db_name.tbl_name`* to create the table in a specific database. This works regardless of whether there is a default database, assuming that the database exists. If you use quoted identifiers, quote the database and table names separately. For example, write `` `mydb`.`mytbl` ``, not `` `mydb.mytbl` ``.
	Rules for permissible table names are given in [Section 11.2, “Schema Object Names”](identifiers.md).
- `IF NOT EXISTS`
	Prevents an error from occurring if the table exists. However, there is no verification that the existing table has a structure identical to that indicated by the `CREATE TABLE` statement.

#### Temporary Tables

You can use the `TEMPORARY` keyword when creating a table. A `TEMPORARY` table is visible only within the current session, and is dropped automatically when the session is closed. For more information, see [Section 15.1.25.2, “CREATE TEMPORARY TABLE Statement”](create-temporary-table.md).

#### Table Cloning and Copying

- `LIKE`
	Use `CREATE TABLE ... LIKE` to create an empty table based on the definition of another table, including any column attributes and indexes defined in the original table:
	```sql
	CREATE TABLE new_tbl LIKE orig_tbl;
	```
	For more information, see [Section 15.1.25.3, “CREATE TABLE... LIKE Statement”](create-table-like.md).
- ``[AS]           *`query_expression`*``
	To create one table from another, add a [`SELECT`](select.md) statement at the end of the `CREATE TABLE` statement:
	```sql
	CREATE TABLE new_tbl AS SELECT * FROM orig_tbl;
	```
	For more information, see [Section 15.1.25.4, “CREATE TABLE... SELECT Statement”](create-table-select.md).
- `IGNORE | REPLACE`
	The `IGNORE` and `REPLACE` options indicate how to handle rows that duplicate unique key values when copying a table using a [`SELECT`](select.md) statement.
	For more information, see [Section 15.1.25.4, “CREATE TABLE... SELECT Statement”](create-table-select.md).

#### Column Data Types and Attributes

There is a hard limit of 4096 columns per table, but the effective maximum may be less for a given table and depends on the factors discussed in [Section 10.4.7, “Limits on Table Column Count and Row Size”](column-count-limit.md).

- ``*`data_type`*``
	*`data_type`* represents the data type in a column definition. For a full description of the syntax available for specifying column data types, as well as information about the properties of each type, see [Chapter 13, *Data Types*](data-types.md).
	- `AUTO_INCREMENT` applies only to integer types.
	- Character data types ([`CHAR`](char.md), [`VARCHAR`](char.md), the [`TEXT`](blob.md) types, [`ENUM`](enum.md), [`SET`](set.md), and any synonyms) can include `CHARACTER SET` to specify the character set for the column. `CHARSET` is a synonym for `CHARACTER SET`. A collation for the character set can be specified with the `COLLATE` attribute, along with any other attributes. For details, see [Chapter 12, *Character Sets, Collations, Unicode*](charset.md). Example:
		```sql
		CREATE TABLE t (c CHAR(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin);
		```
		MySQL 26.10 interprets length specifications in character column definitions in characters. Lengths for [`BINARY`](binary-varbinary.md) and [`VARBINARY`](binary-varbinary.md) are in bytes.
	- For [`CHAR`](char.md), [`VARCHAR`](char.md), [`BINARY`](binary-varbinary.md), and [`VARBINARY`](binary-varbinary.md) columns, indexes can be created that use only the leading part of column values, using ``*`col_name`*(*`length`*)`` syntax to specify an index prefix length. [`BLOB`](blob.md) and [`TEXT`](blob.md) columns also can be indexed, but a prefix length *must* be given. Prefix lengths are given in characters for nonbinary string types and in bytes for binary string types. That is, index entries consist of the first *`length`* characters of each column value for [`CHAR`](char.md), [`VARCHAR`](char.md), and [`TEXT`](blob.md) columns, and the first *`length`* bytes of each column value for [`BINARY`](binary-varbinary.md), [`VARBINARY`](binary-varbinary.md), and [`BLOB`](blob.md) columns. Indexing only a prefix of column values like this can make the index file much smaller. For additional information about index prefixes, see [Section 15.1.18, “CREATE INDEX Statement”](create-index.md).
		Only the `InnoDB` and `MyISAM` storage engines support indexing on [`BLOB`](blob.md) and [`TEXT`](blob.md) columns. For example:
		```sql
		CREATE TABLE test (blob_col BLOB, INDEX(blob_col(10)));
		```
		If a specified index prefix exceeds the maximum column data type size, `CREATE               TABLE` handles the index as follows:
		- For a nonunique index, either an error occurs (if strict SQL mode is enabled), or the index length is reduced to lie within the maximum column data type size and a warning is produced (if strict SQL mode is not enabled).
		- For a unique index, an error occurs regardless of SQL mode because reducing the index length might enable insertion of nonunique entries that do not meet the specified uniqueness requirement.
	- [`JSON`](json.md) columns cannot be indexed. You can work around this restriction by creating an index on a generated column that extracts a scalar value from the `JSON` column. See [Indexing a Generated Column to Provide a JSON Column Index](create-table-secondary-indexes.md), for a detailed example.
- `NOT NULL | NULL`
	If neither `NULL` nor `NOT           NULL` is specified, the column is treated as though `NULL` had been specified.
	In MySQL 26.10, only the `InnoDB`, `MyISAM`, and `MEMORY` storage engines support indexes on columns that can have `NULL` values. In other cases, you must declare indexed columns as `NOT NULL` or an error results.
- `DEFAULT`
	Specifies a default value for a column. For more information about default value handling, including the case that a column definition includes no explicit `DEFAULT` value, see [Section 13.6, “Data Type Default Values”](data-type-defaults.md).
	If the [`NO_ZERO_DATE`](sql-mode.md) or [`NO_ZERO_IN_DATE`](sql-mode.md) SQL mode is enabled and a date-valued default is not correct according to that mode, `CREATE TABLE` produces a warning if strict SQL mode is not enabled and an error if strict mode is enabled. For example, with [`NO_ZERO_IN_DATE`](sql-mode.md) enabled, `c1 DATE DEFAULT '2010-00-00'` produces a warning.
- `VISIBLE`, `INVISIBLE`
	Specify column visibility. The default is `VISIBLE` if neither keyword is present. A table must have at least one visible column. Attempting to make all columns invisible produces an error. For more information, see [Section 15.1.25.10, “Invisible Columns”](invisible-columns.md).
- `AUTO_INCREMENT`
	An integer column can have the additional attribute `AUTO_INCREMENT`. When you insert a value of `NULL` (recommended) or `0` into an indexed `AUTO_INCREMENT` column, the column is set to the next sequence value. Typically this is ``*`value`*+1``, where *`value`* is the largest value for the column currently in the table. `AUTO_INCREMENT` sequences begin with `1`.
	To retrieve an `AUTO_INCREMENT` value after inserting a row, use the [`LAST_INSERT_ID()`](information-functions.md) SQL function or the [`mysql_insert_id()`](https://dev.mysql.com/doc/c-api/26.10/en/mysql-insert-id.html) C API function. See [Section 14.15, “Information Functions”](information-functions.md), and [mysql\_insert\_id()](https://dev.mysql.com/doc/c-api/26.10/en/mysql-insert-id.html).
	If the [`NO_AUTO_VALUE_ON_ZERO`](sql-mode.md) SQL mode is enabled, you can store `0` in `AUTO_INCREMENT` columns as `0` without generating a new sequence value. See [Section 7.1.11, “Server SQL Modes”](sql-mode.md).
	There can be only one `AUTO_INCREMENT` column per table, it must be indexed, and it cannot have a `DEFAULT` value. An `AUTO_INCREMENT` column works properly only if it contains only positive values. Inserting a negative number is regarded as inserting a very large positive number. This is done to avoid precision problems when numbers “wrap” over from positive to negative and also to ensure that you do not accidentally get an `AUTO_INCREMENT` column that contains `0`.
	For `MyISAM` tables, you can specify an `AUTO_INCREMENT` secondary column in a multiple-column key. See [Section 5.6.9, “Using AUTO\_INCREMENT”](example-auto-increment.md).
	To make MySQL compatible with some ODBC applications, you can find the `AUTO_INCREMENT` value for the last inserted row with the following query:
	```sql
	SELECT * FROM tbl_name WHERE auto_col IS NULL
	```
	This method requires that [`sql_auto_is_null`](server-system-variables.md) variable is not set to 0. See [Section 7.1.8, “Server System Variables”](server-system-variables.md).
	For information about `InnoDB` and `AUTO_INCREMENT`, see [Section 17.6.1.6, “AUTO\_INCREMENT Handling in InnoDB”](innodb-auto-increment-handling.md). For information about `AUTO_INCREMENT` and MySQL Replication, see [Section 19.5.1.1, “Replication and AUTO\_INCREMENT”](replication-features-auto-increment.md).