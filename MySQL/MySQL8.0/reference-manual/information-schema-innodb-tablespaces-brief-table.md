---
title: "28.4.25 The INFORMATION_SCHEMA INNODB_TABLESPACES_BRIEF Table"
book: MySQL 8.0 Reference Manual
version: "8.0"
source: "https://dev.mysql.com/doc/refman/8.0/en/information-schema-innodb-tablespaces-brief-table.html"
tags:
  - mysql
  - mysql-8.0
  - reference-manual
---

MySQL 8.0 Reference Manual Including MySQL NDB Cluster 8.0

### 28.4.25 The INFORMATION\_SCHEMA INNODB\_TABLESPACES\_BRIEF Table

The `INNODB_TABLESPACES_BRIEF` table provides space ID, name, path, flag, and space type metadata for file-per-table, general, undo, and system tablespaces.

[`INNODB_TABLESPACES`](information-schema-innodb-tablespaces-table.md) provides the same metadata but loads more slowly because other metadata provided by the table, such as `FS_BLOCK_SIZE`, `FILE_SIZE`, and `ALLOCATED_SIZE`, must be loaded dynamically.

Space and path metadata is also provided by the [`INNODB_DATAFILES`](information-schema-innodb-datafiles-table.md) table.

The `INNODB_TABLESPACES_BRIEF` table has these columns:

- `SPACE`
	The tablespace ID.
- `NAME`
	The tablespace name. For file-per-table tablespaces, the name is in the form of *`schema/table_name`*.
- `PATH`
	The tablespace data file path. If a [file-per-table](glossary.md) tablespace is created in a location outside the MySQL data directory, the path value is a fully qualified directory path. Otherwise, the path is relative to the data directory.
- `FLAG`
	A numeric value that represents bit-level information about tablespace format and storage characteristics.
- `SPACE_TYPE`
	The type of tablespace. Possible values include `General` for `InnoDB` general tablespaces, `Single` for `InnoDB` file-per-table tablespaces, and `System` for the `InnoDB` system tablespace.

#### Example

```
mysql> SELECT * FROM INFORMATION_SCHEMA.INNODB_TABLESPACES_BRIEF WHERE SPACE = 7;
+-------+---------+---------------+-------+------------+
| SPACE | NAME    | PATH          | FLAG  | SPACE_TYPE |
+-------+---------+---------------+-------+------------+
| 7     | test/t1 | ./test/t1.ibd | 16417 | Single     |
+-------+---------+---------------+-------+------------+
```

#### Notes

- You must have the [`PROCESS`](privileges-provided.md) privilege to query this table.
- Use the `INFORMATION_SCHEMA` [`COLUMNS`](information-schema-columns-table.md) table or the [`SHOW COLUMNS`](show-columns.md) statement to view additional information about the columns of this table, including data types and default values.