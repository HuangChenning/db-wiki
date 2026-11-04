---
title: "24.4.20 The INFORMATION_SCHEMA INNODB_SYS_FOREIGN Table"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/information-schema-innodb-sys-foreign-table.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 24.4.20 The INFORMATION\_SCHEMA INNODB\_SYS\_FOREIGN Table

The `INNODB_SYS_FOREIGN` table provides metadata about `InnoDB` [foreign keys](glossary.md), equivalent to the information from the `SYS_FOREIGN` table in the `InnoDB` data dictionary.

For related usage information and examples, see [Section 14.16.3, “InnoDB INFORMATION\_SCHEMA System Tables”](innodb-information-schema-system-tables.md).

The `INNODB_SYS_FOREIGN` table has these columns:

- `ID`
	The name (not a numeric value) of the foreign key index, preceded by the schema (database) name (for example, `test/products_fk`).
- `FOR_NAME`
	The name of the [child table](glossary.md) in this foreign key relationship.
- `REF_NAME`
	The name of the [parent table](glossary.md) in this foreign key relationship.
- `N_COLS`
	The number of columns in the foreign key index.
- `TYPE`
	A collection of bit flags with information about the foreign key column, ORed together. 0 = `ON DELETE/UPDATE           RESTRICT`, 1 = `ON DELETE CASCADE`, 2 = `ON DELETE SET NULL`, 4 = `ON           UPDATE CASCADE`, 8 = `ON UPDATE SET           NULL`, 16 = `ON DELETE NO ACTION`, 32 = `ON UPDATE NO ACTION`.

#### Example

```
mysql> SELECT * FROM INFORMATION_SCHEMA.INNODB_SYS_FOREIGN\G
*************************** 1. row ***************************
      ID: test/fk1
FOR_NAME: test/child
REF_NAME: test/parent
  N_COLS: 1
    TYPE: 1
```

#### Notes

- You must have the [`PROCESS`](privileges-provided.md) privilege to query this table.
- Use the `INFORMATION_SCHEMA` [`COLUMNS`](information-schema-columns-table.md) table or the [`SHOW COLUMNS`](show-columns.md) statement to view additional information about the columns of this table, including data types and default values.