---
title: "MySQL :: MySQL 26.7 Reference Manual :: 28.4.10 The INFORMATION_SCHEMA INNODB_DATAFILES Table"
book: MySQL 26.7 Reference Manual
version: "26.7"
source: "https://dev.mysql.com/doc/refman/26.7/en/information-schema-innodb-datafiles-table.html"
tags:
  - mysql
  - mysql-26.7
  - reference-manual
---

### 28.4.10 The INFORMATION\_SCHEMA INNODB\_DATAFILES Table

The `INNODB_DATAFILES` table provides data file path information for `InnoDB` file-per-table and general tablespaces.

For related usage information and examples, see [Section 17.15.3, “InnoDB INFORMATION\_SCHEMA Schema Object Tables”](innodb-information-schema-system-tables.md).

Note

The `INFORMATION_SCHEMA` [`FILES`](information-schema-files-table.md) table reports metadata for `InnoDB` tablespace types including file-per-table tablespaces, general tablespaces, the system tablespace, the global temporary tablespace, and undo tablespaces.

The `INNODB_DATAFILES` table has these columns:

- `SPACE`
	The tablespace ID.
- `PATH`
	The tablespace data file path. If a [file-per-table](glossary.md) tablespace is created in a location outside the MySQL data directory, the path value is a fully qualified directory path. Otherwise, the path is relative to the data directory.

#### Example

```sql
mysql> SELECT * FROM INFORMATION_SCHEMA.INNODB_DATAFILES WHERE SPACE = 57\G
*************************** 1. row ***************************
SPACE: 57
 PATH: ./test/t1.ibd
```

#### Notes

- You must have the [`PROCESS`](privileges-provided.md) privilege to query this table.
- Use the `INFORMATION_SCHEMA` [`COLUMNS`](information-schema-columns-table.md) table or the [`SHOW COLUMNS`](show-columns.md) statement to view additional information about the columns of this table, including data types and default values.