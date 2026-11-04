---
title: "24.3.24 The INFORMATION_SCHEMA STATISTICS Table"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/information-schema-statistics-table.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 24.3.24 The INFORMATION\_SCHEMA STATISTICS Table

The `STATISTICS` table provides information about table indexes.

The `STATISTICS` table has these columns:

- `TABLE_CATALOG`
	The name of the catalog to which the table containing the index belongs. This value is always `def`.
- `TABLE_SCHEMA`
	The name of the schema (database) to which the table containing the index belongs.
- `TABLE_NAME`
	The name of the table containing the index.
- `NON_UNIQUE`
	0 if the index cannot contain duplicates, 1 if it can.
- `INDEX_SCHEMA`
	The name of the schema (database) to which the index belongs.
- `INDEX_NAME`
	The name of the index. If the index is the primary key, the name is always `PRIMARY`.
- `SEQ_IN_INDEX`
	The column sequence number in the index, starting with 1.
- `COLUMN_NAME`
	The column name. See also the description for the `EXPRESSION` column.
- `COLLATION`
	How the column is sorted in the index. This can have values `A` (ascending), `D` (descending), or `NULL` (not sorted).
- `CARDINALITY`
	An estimate of the number of unique values in the index. To update this number, run [`ANALYZE           TABLE`](analyze-table.md) or (for `MyISAM` tables) [**myisamchk -a**](myisamchk.md).
	`CARDINALITY` is counted based on statistics stored as integers, so the value is not necessarily exact even for small tables. The higher the cardinality, the greater the chance that MySQL uses the index when doing joins.
- `SUB_PART`
	The index prefix. That is, the number of indexed characters if the column is only partly indexed, `NULL` if the entire column is indexed.
	Note
	Prefix *limits* are measured in bytes. However, prefix *lengths* for index specifications in [`CREATE             TABLE`](create-table.md), [`ALTER TABLE`](alter-table.md), and [`CREATE INDEX`](create-index.md) statements are interpreted as number of characters for nonbinary string types ([`CHAR`](char.md), [`VARCHAR`](char.md), [`TEXT`](blob.md)) and number of bytes for binary string types ([`BINARY`](binary-varbinary.md), [`VARBINARY`](binary-varbinary.md), [`BLOB`](blob.md)). Take this into account when specifying a prefix length for a nonbinary string column that uses a multibyte character set.
	For additional information about index prefixes, see [Section 8.3.4, “Column Indexes”](column-indexes.md), and [Section 13.1.14, “CREATE INDEX Statement”](create-index.md).
- `PACKED`
	Indicates how the key is packed. `NULL` if it is not.
- `NULLABLE`
	Contains `YES` if the column may contain `NULL` values and `''` if not.
- `INDEX_TYPE`
	The index method used (`BTREE`, `FULLTEXT`, `HASH`, `RTREE`).