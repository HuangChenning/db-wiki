---
title: "24.4.22 The INFORMATION_SCHEMA INNODB_SYS_INDEXES Table"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/information-schema-innodb-sys-indexes-table.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 24.4.22 The INFORMATION\_SCHEMA INNODB\_SYS\_INDEXES Table

The `INNODB_SYS_INDEXES` table provides metadata about `InnoDB` indexes, equivalent to the information in the internal `SYS_INDEXES` table in the `InnoDB` data dictionary.

For related usage information and examples, see [Section 14.16.3, “InnoDB INFORMATION\_SCHEMA System Tables”](innodb-information-schema-system-tables.md).

The `INNODB_SYS_INDEXES` table has these columns:

- `INDEX_ID`
	An identifier for the index. Index identifiers are unique across all the databases in an instance.
- `NAME`
	The name of the index. Most indexes created implicitly by `InnoDB` have consistent names but the index names are not necessarily unique. Examples: `PRIMARY` for a primary key index, `GEN_CLUST_INDEX` for the index representing a primary key when one is not specified, and `ID_IND`, `FOR_IND`, and `REF_IND` for foreign key constraints.
- `TABLE_ID`
	An identifier representing the table associated with the index; the same value as `INNODB_SYS_TABLES.TABLE_ID`.
- `TYPE`
	A numeric value derived from bit-level information that identifies the index type. 0 = nonunique secondary index; 1 = automatically generated clustered index (`GEN_CLUST_INDEX`); 2 = unique nonclustered index; 3 = clustered index; 32 = full-text index; 64 = spatial index; 128 = secondary index on a [virtual generated column](glossary.md).
- `N_FIELDS`
	The number of columns in the index key. For `GEN_CLUST_INDEX` indexes, this value is 0 because the index is created using an artificial value rather than a real table column.
- `PAGE_NO`
	The root page number of the index B-tree. For full-text indexes, the `PAGE_NO` column is unused and set to -1 (`FIL_NULL`) because the full-text index is laid out in several B-trees (auxiliary tables).
- `SPACE`
	An identifier for the tablespace where the index resides. 0 means the `InnoDB` [system tablespace](glossary.md). Any other number represents a table created with a separate `.ibd` file in [file-per-table](glossary.md) mode. This identifier stays the same after a [`TRUNCATE TABLE`](truncate-table.md) statement. Because all indexes for a table reside in the same tablespace as the table, this value is not necessarily unique.
- `MERGE_THRESHOLD`
	The merge threshold value for index pages. If the amount of data in an index page falls below the [`MERGE_THRESHOLD`](index-page-merge-threshold.md) value when a row is deleted or when a row is shortened by an update operation, `InnoDB` attempts to merge the index page with the neighboring index page. The default threshold value is 50%. For more information, see [Section 14.8.12, “Configuring the Merge Threshold for Index Pages”](index-page-merge-threshold.md).

#### Example

```
mysql> SELECT * FROM INFORMATION_SCHEMA.INNODB_SYS_INDEXES WHERE TABLE_ID = 34\G
*************************** 1. row ***************************
       INDEX_ID: 39
           NAME: GEN_CLUST_INDEX
       TABLE_ID: 34
           TYPE: 1
       N_FIELDS: 0
        PAGE_NO: 3
          SPACE: 23
MERGE_THRESHOLD: 50
*************************** 2. row ***************************
       INDEX_ID: 40
           NAME: i1
       TABLE_ID: 34
           TYPE: 0
       N_FIELDS: 1
        PAGE_NO: 4
          SPACE: 23
MERGE_THRESHOLD: 50
```

#### Notes

- You must have the [`PROCESS`](privileges-provided.md) privilege to query this table.
- Use the `INFORMATION_SCHEMA` [`COLUMNS`](information-schema-columns-table.md) table or the [`SHOW COLUMNS`](show-columns.md) statement to view additional information about the columns of this table, including data types and default values.