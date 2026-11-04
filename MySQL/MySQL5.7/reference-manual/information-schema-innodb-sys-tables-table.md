---
title: "24.4.23 The INFORMATION_SCHEMA INNODB_SYS_TABLES Table"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/information-schema-innodb-sys-tables-table.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 24.4.23 The INFORMATION\_SCHEMA INNODB\_SYS\_TABLES Table

The `INNODB_SYS_TABLES` table provides metadata about `InnoDB` tables, equivalent to the information from the `SYS_TABLES` table in the `InnoDB` data dictionary.

For related usage information and examples, see [Section 14.16.3, “InnoDB INFORMATION\_SCHEMA System Tables”](innodb-information-schema-system-tables.md).

The `INNODB_SYS_TABLES` table has these columns:

- `TABLE_ID`
	An identifier for the `InnoDB` table. This value is unique across all databases in the instance.
- `NAME`
	The name of the table, preceded by the schema (database) name where appropriate (for example, `test/t1`). Names of databases and user tables are in the same case as they were originally defined, possibly influenced by the [`lower_case_table_names`](server-system-variables.md) setting.
- `FLAG`
	A numeric value that represents bit-level information about table format and storage characteristics.
- `N_COLS`
	The number of columns in the table. The number reported includes three hidden columns that are created by `InnoDB` (`DB_ROW_ID`, `DB_TRX_ID`, and `DB_ROLL_PTR`). The number reported also includes [virtual generated columns](glossary.md), if present.
- `SPACE`
	An identifier for the tablespace where the table resides. 0 means the `InnoDB` [system tablespace](glossary.md). Any other number represents either a [file-per-table](glossary.md) tablespace or a general tablespace. This identifier stays the same after a [`TRUNCATE TABLE`](truncate-table.md) statement. For file-per-table tablespaces, this identifier is unique for tables across all databases in the instance.
- `FILE_FORMAT`
	The table's file format (`Antelope` or `Barracuda`).
- `ROW_FORMAT`
	The table's row format (`Compact`, `Redundant`, `Dynamic`, or `Compressed`).
- `ZIP_PAGE_SIZE`
	The zip page size. Applies only to tables with a row format of `Compressed`.
- `SPACE_TYPE`
	The type of tablespace to which the table belongs. Possible values include `System` for the system tablespace, `General` for general tablespaces, and `Single` for file-per-table tablespaces. Tables assigned to the system tablespace using [`CREATE TABLE`](create-table.md) or [`ALTER TABLE`](alter-table.md) `TABLESPACE=innodb_system` have a `SPACE_TYPE` of `General`. For more information, see [`CREATE           TABLESPACE`](create-tablespace.md).

#### Example

```
mysql> SELECT * FROM INFORMATION_SCHEMA.INNODB_SYS_TABLES WHERE TABLE_ID = 214\G
*************************** 1. row ***************************
     TABLE_ID: 214
         NAME: test/t1
         FLAG: 129
       N_COLS: 4
        SPACE: 233
  FILE_FORMAT: Antelope
   ROW_FORMAT: Compact
ZIP_PAGE_SIZE: 0
   SPACE_TYPE: General
```

#### Notes

- You must have the [`PROCESS`](privileges-provided.md) privilege to query this table.
- Use the `INFORMATION_SCHEMA` [`COLUMNS`](information-schema-columns-table.md) table or the [`SHOW COLUMNS`](show-columns.md) statement to view additional information about the columns of this table, including data types and default values.