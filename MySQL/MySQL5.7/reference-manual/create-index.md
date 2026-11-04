---
title: "13.1.14 CREATE INDEX Statement"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/create-index.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 13.1.14 CREATE INDEX Statement

```
CREATE [UNIQUE | FULLTEXT | SPATIAL] INDEX index_name
    [index_type]
    ON tbl_name (key_part,...)
    [index_option]
    [algorithm_option | lock_option] ...

key_part:
    col_name [(length)] [ASC | DESC]

index_option: {
    KEY_BLOCK_SIZE [=] value
  | index_type
  | WITH PARSER parser_name
  | COMMENT 'string'
}

index_type:
    USING {BTREE | HASH}

algorithm_option:
    ALGORITHM [=] {DEFAULT | INPLACE | COPY}

lock_option:
    LOCK [=] {DEFAULT | NONE | SHARED | EXCLUSIVE}
```

Normally, you create all indexes on a table at the time the table itself is created with [`CREATE       TABLE`](create-table.md). See [Section 13.1.18, “CREATE TABLE Statement”](create-table.md). This guideline is especially important for [`InnoDB`](innodb-storage-engine.md) tables, where the primary key determines the physical layout of rows in the data file. `CREATE INDEX` enables you to add indexes to existing tables.

`CREATE INDEX` is mapped to an [`ALTER TABLE`](alter-table.md) statement to create indexes. See [Section 13.1.8, “ALTER TABLE Statement”](alter-table.md). `CREATE INDEX` cannot be used to create a `PRIMARY KEY`; use [`ALTER TABLE`](alter-table.md) instead. For more information about indexes, see [Section 8.3.1, “How MySQL Uses Indexes”](mysql-indexes.md).

[`InnoDB`](innodb-storage-engine.md) supports secondary indexes on virtual columns. For more information, see [Section 13.1.18.8, “Secondary Indexes and Generated Columns”](create-table-secondary-indexes.md).

When the [`innodb_stats_persistent`](innodb-parameters.md) setting is enabled, run the [`ANALYZE       TABLE`](analyze-table.md) statement for an [`InnoDB`](innodb-storage-engine.md) table after creating an index on that table.

An index specification of the form ``(*`key_part1`*,       *`key_part2`*, ...)`` creates an index with multiple key parts. Index key values are formed by concatenating the values of the given key parts. For example `(col1, col2, col3)` specifies a multiple-column index with index keys consisting of values from `col1`, `col2`, and `col3`.

A *`key_part`* specification can end with `ASC` or `DESC`. These keywords are permitted for future extensions for specifying ascending or descending index value storage. Currently, they are parsed but ignored; index values are always stored in ascending order.

The following sections describe different aspects of the `CREATE INDEX` statement:

#### Column Prefix Key Parts

For string columns, indexes can be created that use only the leading part of column values, using ``*`col_name`*(*`length`*)`` syntax to specify an index prefix length:

- Prefixes can be specified for [`CHAR`](char.md), [`VARCHAR`](char.md), [`BINARY`](binary-varbinary.md), and [`VARBINARY`](binary-varbinary.md) key parts.
- Prefixes *must* be specified for [`BLOB`](blob.md) and [`TEXT`](blob.md) key parts. Additionally, [`BLOB`](blob.md) and [`TEXT`](blob.md) columns can be indexed only for `InnoDB`, `MyISAM`, and `BLACKHOLE` tables.
- Prefix *limits* are measured in bytes. However, prefix *lengths* for index specifications in [`CREATE             TABLE`](create-table.md), [`ALTER TABLE`](alter-table.md), and `CREATE INDEX` statements are interpreted as number of characters for nonbinary string types ([`CHAR`](char.md), [`VARCHAR`](char.md), [`TEXT`](blob.md)) and number of bytes for binary string types ([`BINARY`](binary-varbinary.md), [`VARBINARY`](binary-varbinary.md), [`BLOB`](blob.md)). Take this into account when specifying a prefix length for a nonbinary string column that uses a multibyte character set.
	Prefix support and lengths of prefixes (where supported) are storage engine dependent. For example, a prefix can be up to 767 bytes long for [`InnoDB`](innodb-storage-engine.md) tables or 3072 bytes if the [`innodb_large_prefix`](innodb-parameters.md) option is enabled. For [`MyISAM`](myisam-storage-engine.md) tables, the prefix length limit is 1000 bytes. The [`NDB`](mysql-cluster.md) storage engine does not support prefixes (see [Section 21.2.7.6, “Unsupported or Missing Features in NDB Cluster”](mysql-cluster-limitations-unsupported.md)).

As of MySQL 5.7.17, if a specified index prefix exceeds the maximum column data type size, `CREATE         INDEX` handles the index as follows:

- For a nonunique index, either an error occurs (if strict SQL mode is enabled), or the index length is reduced to lie within the maximum column data type size and a warning is produced (if strict SQL mode is not enabled).
- For a unique index, an error occurs regardless of SQL mode because reducing the index length might enable insertion of nonunique entries that do not meet the specified uniqueness requirement.

The statement shown here creates an index using the first 10 characters of the `name` column (assuming that `name` has a nonbinary string type):

```
CREATE INDEX part_of_name ON customer (name(10));
```

If names in the column usually differ in the first 10 characters, lookups performed using this index should not be much slower than using an index created from the entire `name` column. Also, using column prefixes for indexes can make the index file much smaller, which could save a lot of disk space and might also speed up [`INSERT`](insert.md) operations.

#### Unique Indexes

A `UNIQUE` index creates a constraint such that all values in the index must be distinct. An error occurs if you try to add a new row with a key value that matches an existing row. If you specify a prefix value for a column in a `UNIQUE` index, the column values must be unique within the prefix length. A `UNIQUE` index permits multiple `NULL` values for columns that can contain `NULL`.

If a table has a `PRIMARY KEY` or `UNIQUE NOT NULL` index that consists of a single column that has an integer type, you can use `_rowid` to refer to the indexed column in [`SELECT`](select.md) statements, as follows:

- `_rowid` refers to the `PRIMARY             KEY` column if there is a `PRIMARY             KEY` consisting of a single integer column. If there is a `PRIMARY KEY` but it does not consist of a single integer column, `_rowid` cannot be used.
- Otherwise, `_rowid` refers to the column in the first `UNIQUE NOT NULL` index if that index consists of a single integer column. If the first `UNIQUE NOT NULL` index does not consist of a single integer column, `_rowid` cannot be used.

#### Full-Text Indexes

`FULLTEXT` indexes are supported only for [`InnoDB`](innodb-storage-engine.md) and [`MyISAM`](myisam-storage-engine.md) tables and can include only [`CHAR`](char.md), [`VARCHAR`](char.md), and [`TEXT`](blob.md) columns. Indexing always happens over the entire column; column prefix indexing is not supported and any prefix length is ignored if specified. See [Section 12.9, “Full-Text Search Functions”](fulltext-search.md), for details of operation.

#### Spatial Indexes

The [`MyISAM`](myisam-storage-engine.md), [`InnoDB`](innodb-storage-engine.md), [`NDB`](mysql-cluster.md), and [`ARCHIVE`](archive-storage-engine.md) storage engines support spatial columns such as [`POINT`](spatial-type-overview.md) and [`GEOMETRY`](spatial-type-overview.md). ([Section 11.4, “Spatial Data Types”](spatial-types.md), describes the spatial data types.) However, support for spatial column indexing varies among engines. Spatial and nonspatial indexes on spatial columns are available according to the following rules.

Spatial indexes on spatial columns (created using `SPATIAL INDEX`) have these characteristics:

- Available only for [`MyISAM`](myisam-storage-engine.md) and [`InnoDB`](innodb-storage-engine.md) tables. Specifying `SPATIAL INDEX` for other storage engines results in an error.
- Indexed columns must be `NOT NULL`.
- Column prefix lengths are prohibited. The full width of each column is indexed.

Nonspatial indexes on spatial columns (created with `INDEX`, `UNIQUE`, or `PRIMARY KEY`) have these characteristics:

- Permitted for any storage engine that supports spatial columns except [`ARCHIVE`](archive-storage-engine.md).
- Columns can be `NULL` unless the index is a primary key.
- For each spatial column in a non- `SPATIAL` index except [`POINT`](spatial-type-overview.md) columns, a column prefix length must be specified. (This is the same requirement as for indexed [`BLOB`](blob.md) columns.) The prefix length is given in bytes.
- The index type for a non- `SPATIAL` index depends on the storage engine. Currently, B-tree is used.
- Permitted for a column that can have `NULL` values only for [`InnoDB`](innodb-storage-engine.md), [`MyISAM`](myisam-storage-engine.md), and [`MEMORY`](memory-storage-engine.md) tables.

#### Index Options

Following the key part list, index options can be given. An *`index_option`* value can be any of the following:

- ``KEY_BLOCK_SIZE [=]             *`value`*``
	For [`MyISAM`](myisam-storage-engine.md) tables, `KEY_BLOCK_SIZE` optionally specifies the size in bytes to use for index key blocks. The value is treated as a hint; a different size could be used if necessary. A `KEY_BLOCK_SIZE` value specified for an individual index definition overrides a table-level `KEY_BLOCK_SIZE` value.
	`KEY_BLOCK_SIZE` is not supported at the index level for [`InnoDB`](innodb-storage-engine.md) tables. See [Section 13.1.18, “CREATE TABLE Statement”](create-table.md).
- *`index_type`*
	Some storage engines permit you to specify an index type when creating an index. For example:
	```
	CREATE TABLE lookup (id INT) ENGINE = MEMORY;
	CREATE INDEX id_index ON lookup (id) USING BTREE;
	```
	Table 13.1, “Index Types Per Storage Engine” shows the permissible index type values supported by different storage engines. Where multiple index types are listed, the first one is the default when no index type specifier is given. Storage engines not listed in the table do not support an *`index_type`* clause in index definitions.
	**Table 13.1 Index Types Per Storage Engine**
	| Storage Engine | Permissible Index Types |
	| --- | --- |
	| [`InnoDB`](innodb-storage-engine.md) | `BTREE` |
	| [`MyISAM`](myisam-storage-engine.md) | `BTREE` |
	| [`MEMORY`](memory-storage-engine.md) / `HEAP` | `HASH`, `BTREE` |
	| [`NDB`](mysql-cluster.md) | `HASH`, `BTREE` (see note in text) |
	The *`index_type`* clause cannot be used for `FULLTEXT INDEX` or `SPATIAL INDEX` specifications. Full-text index implementation is storage engine dependent. Spatial indexes are implemented as R-tree indexes.
	`BTREE` indexes are implemented by the [`NDB`](mysql-cluster.md) storage engine as T-tree indexes.
	Note
	For indexes on [`NDB`](mysql-cluster.md) table columns, the `USING` option can be specified only for a unique index or primary key. `USING HASH` prevents the creation of an ordered index; otherwise, creating a unique index or primary key on an [`NDB`](mysql-cluster.md) table automatically results in the creation of both an ordered index and a hash index, each of which indexes the same set of columns.
	For unique indexes that include one or more `NULL` columns of an [`NDB`](mysql-cluster.md) table, the hash index can be used only to look up literal values, which means that `IS [NOT] NULL` conditions require a full scan of the table. One workaround is to make sure that a unique index using one or more `NULL` columns on such a table is always created in such a way that it includes the ordered index; that is, avoid employing `USING HASH` when creating the index.
	If you specify an index type that is not valid for a given storage engine, but another index type is available that the engine can use without affecting query results, the engine uses the available type. The parser recognizes `RTREE` as a type name, but currently this cannot be specified for any storage engine.
	Note
	Use of the *`index_type`* option before the ``ON               *`tbl_name`*`` clause is deprecated; you should expect support for use of the option in this position to be removed in a future MySQL release. If an *`index_type`* option is given in both the earlier and later positions, the final option applies.
	``TYPE *`type_name`*`` is recognized as a synonym for ``USING             *`type_name`*``. However, `USING` is the preferred form.
	The following tables show index characteristics for the storage engines that support the *`index_type`* option.
	**Table 13.2 InnoDB Storage Engine Index Characteristics**
	| Index Class | Index Type | Stores NULL VALUES | Permits Multiple NULL Values | IS NULL Scan Type | IS NOT NULL Scan Type |
	| --- | --- | --- | --- | --- | --- |
	| Primary key | `BTREE` | No | No | N/A | N/A |
	| Unique | `BTREE` | Yes | Yes | Index | Index |
	| Key | `BTREE` | Yes | Yes | Index | Index |
	| `FULLTEXT` | N/A | Yes | Yes | Table | Table |
	| `SPATIAL` | N/A | No | No | N/A | N/A |
	**Table 13.3 MyISAM Storage Engine Index Characteristics**
	| Index Class | Index Type | Stores NULL VALUES | Permits Multiple NULL Values | IS NULL Scan Type | IS NOT NULL Scan Type |
	| --- | --- | --- | --- | --- | --- |
	| Primary key | `BTREE` | No | No | N/A | N/A |
	| Unique | `BTREE` | Yes | Yes | Index | Index |
	| Key | `BTREE` | Yes | Yes | Index | Index |
	| `FULLTEXT` | N/A | Yes | Yes | Table | Table |
	| `SPATIAL` | N/A | No | No | N/A | N/A |
	**Table 13.4 MEMORY Storage Engine Index Characteristics**
	| Index Class | Index Type | Stores NULL VALUES | Permits Multiple NULL Values | IS NULL Scan Type | IS NOT NULL Scan Type |
	| --- | --- | --- | --- | --- | --- |
	| Primary key | `BTREE` | No | No | N/A | N/A |
	| Unique | `BTREE` | Yes | Yes | Index | Index |
	| Key | `BTREE` | Yes | Yes | Index | Index |
	| Primary key | `HASH` | No | No | N/A | N/A |
	| Unique | `HASH` | Yes | Yes | Index | Index |
	| Key | `HASH` | Yes | Yes | Index | Index |
	**Table 13.5 NDB Storage Engine Index Characteristics**
	| Index Class | Index Type | Stores NULL VALUES | Permits Multiple NULL Values | IS NULL Scan Type | IS NOT NULL Scan Type |
	| --- | --- | --- | --- | --- | --- |
	| Primary key | `BTREE` | No | No | Index | Index |
	| Unique | `BTREE` | Yes | Yes | Index | Index |
	| Key | `BTREE` | Yes | Yes | Index | Index |
	| Primary key | `HASH` | No | No | Table (see note 1) | Table (see note 1) |
	| Unique | `HASH` | Yes | Yes | Table (see note 1) | Table (see note 1) |
	| Key | `HASH` | Yes | Yes | Table (see note 1) | Table (see note 1) |
	Table note:
	1\. If `USING HASH` is specified that prevents creation of an implicit ordered index.
- ``WITH PARSER             *`parser_name`*``
	This option can be used only with `FULLTEXT` indexes. It associates a parser plugin with the index if full-text indexing and searching operations need special handling. [`InnoDB`](innodb-storage-engine.md) and [`MyISAM`](myisam-storage-engine.md) support full-text parser plugins. If you have a [`MyISAM`](myisam-storage-engine.md) table with an associated full-text parser plugin, you can convert the table to `InnoDB` using `ALTER TABLE`. See [Full-Text Parser Plugins](https://dev.mysql.com/doc/extending-mysql/5.7/en/plugin-types.html#full-text-plugin-type) and [Writing Full-Text Parser Plugins](https://dev.mysql.com/doc/extending-mysql/5.7/en/writing-full-text-plugins.html) for more information.
- ``COMMENT             '*`string`*'``
	Index definitions can include an optional comment of up to 1024 characters.
	The [`MERGE_THRESHOLD`](index-page-merge-threshold.md) for index pages can be configured for individual indexes using the *`index_option`* `COMMENT` clause of the `CREATE INDEX` statement. For example:
	```
	CREATE TABLE t1 (id INT);
	CREATE INDEX id_index ON t1 (id) COMMENT 'MERGE_THRESHOLD=40';
	```
	If the page-full percentage for an index page falls below the `MERGE_THRESHOLD` value when a row is deleted or when a row is shortened by an update operation, [`InnoDB`](innodb-storage-engine.md) attempts to merge the index page with a neighboring index page. The default `MERGE_THRESHOLD` value is 50, which is the previously hardcoded value.
	`MERGE_THRESHOLD` can also be defined at the index level and table level using [`CREATE TABLE`](create-table.md) and [`ALTER TABLE`](alter-table.md) statements. For more information, see [Section 14.8.12, “Configuring the Merge Threshold for Index Pages”](index-page-merge-threshold.md).

#### Table Copying and Locking Options

`ALGORITHM` and `LOCK` clauses may be given to influence the table copying method and level of concurrency for reading and writing the table while its indexes are being modified. They have the same meaning as for the [`ALTER TABLE`](alter-table.md) statement. For more information, see [Section 13.1.8, “ALTER TABLE Statement”](alter-table.md)

NDB Cluster formerly supported online `CREATE         INDEX` operations using an alternative syntax that is no longer supported. NDB Cluster now supports online operations using the same `ALGORITHM=INPLACE` syntax used with the standard MySQL Server. See [Section 21.6.12, “Online Operations with ALTER TABLE in NDB Cluster”](mysql-cluster-online-operations.md), for more information.