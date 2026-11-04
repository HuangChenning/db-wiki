---
title: "24.4.18 The INFORMATION_SCHEMA INNODB_SYS_DATAFILES Table"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/information-schema-innodb-sys-datafiles-table.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 24.4.18 The INFORMATION\_SCHEMA INNODB\_SYS\_DATAFILES Table

The `INNODB_SYS_DATAFILES` table provides data file path information for `InnoDB` file-per-table and general tablespaces, equivalent to the information in the `SYS_DATAFILES` table in the `InnoDB` data dictionary.

For related usage information and examples, see [Section 14.16.3, “InnoDB INFORMATION\_SCHEMA System Tables”](innodb-information-schema-system-tables.md).

Note

The `INFORMATION_SCHEMA` [`FILES`](information-schema-files-table.md) table reports metadata for all `InnoDB` tablespace types including file-per-table tablespaces, general tablespaces, the system tablespace, the temporary tablespace, and undo tablespaces, if present.

The `INNODB_SYS_DATAFILES` table has these columns:

- `SPACE`
	The tablespace ID.
- `PATH`
	The tablespace data file path. If a [file-per-table](glossary.md) tablespace is created in a location outside the MySQL data directory, the path value is a fully qualified directory path. Otherwise, the path is relative to the data directory.

#### Example

```
mysql> SELECT * FROM INFORMATION_SCHEMA.INNODB_SYS_DATAFILES WHERE SPACE = 57\G
*************************** 1. row ***************************
SPACE: 57
 PATH: ./test/t1.ibd
```

#### Notes

- You must have the [`PROCESS`](privileges-provided.md) privilege to query this table.
- Use the `INFORMATION_SCHEMA` [`COLUMNS`](information-schema-columns-table.md) table or the [`SHOW COLUMNS`](show-columns.md) statement to view additional information about the columns of this table, including data types and default values.