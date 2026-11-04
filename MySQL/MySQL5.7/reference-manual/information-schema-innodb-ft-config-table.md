---
title: "24.4.9 The INFORMATION_SCHEMA INNODB_FT_CONFIG Table"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/information-schema-innodb-ft-config-table.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 24.4.9 The INFORMATION\_SCHEMA INNODB\_FT\_CONFIG Table

The `INNODB_FT_CONFIG` table provides metadata about the `FULLTEXT` index and associated processing for an `InnoDB` table.

This table is empty initially. Before querying it, set the value of the [`innodb_ft_aux_table`](innodb-parameters.md) system variable to the name (including the database name) of the table that contains the `FULLTEXT` index; for example `test/articles`.

For related usage information and examples, see [Section 14.16.4, “InnoDB INFORMATION\_SCHEMA FULLTEXT Index Tables”](innodb-information-schema-fulltext_index-tables.md).

The `INNODB_FT_CONFIG` table has these columns:

- `KEY`
	The name designating an item of metadata for an `InnoDB` table containing a `FULLTEXT` index.
	The values for this column might change, depending on the needs for performance tuning and debugging for `InnoDB` full-text processing. The key names and their meanings include:
	- `optimize_checkpoint_limit`: The number of seconds after which an [`OPTIMIZE               TABLE`](optimize-table.md) run stops.
	- `synced_doc_id`: The next `DOC_ID` to be issued.
	- `stopword_table_name`: The *`database/table`* name for a user-defined stopword table. The `VALUE` column is empty if there is no user-defined stopword table.
	- `use_stopword`: Indicates whether a stopword table is used, which is defined when the `FULLTEXT` index is created.
- `VALUE`
	The value associated with the corresponding `KEY` column, reflecting some limit or current value for an aspect of a `FULLTEXT` index for an `InnoDB` table.

#### Example

```
mysql> SELECT * FROM INFORMATION_SCHEMA.INNODB_FT_CONFIG;
+---------------------------+-------------------+
| KEY                       | VALUE             |
+---------------------------+-------------------+
| optimize_checkpoint_limit | 180               |
| synced_doc_id             | 0                 |
| stopword_table_name       | test/my_stopwords |
| use_stopword              | 1                 |
+---------------------------+-------------------+
```

#### Notes

- This table is intended only for internal configuration. It is not intended for statistical information purposes.
- You must have the [`PROCESS`](privileges-provided.md) privilege to query this table.
- Use the `INFORMATION_SCHEMA` [`COLUMNS`](information-schema-columns-table.md) table or the [`SHOW COLUMNS`](show-columns.md) statement to view additional information about the columns of this table, including data types and default values.
- For more information about `InnoDB` `FULLTEXT` search, see [Section 14.6.2.4, “InnoDB Full-Text Indexes”](innodb-fulltext-index.md), and [Section 12.9, “Full-Text Search Functions”](fulltext-search.md).