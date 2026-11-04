---
title: "28.4.27 The INFORMATION_SCHEMA INNODB_TEMP_TABLE_INFO Table"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/information-schema-innodb-temp-table-info-table.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 28.4.27 The INFORMATION\_SCHEMA INNODB\_TEMP\_TABLE\_INFO Table

The `INNODB_TEMP_TABLE_INFO` table provides information about user-created `InnoDB` temporary tables that are active in an `InnoDB` instance. It does not provide information about internal `InnoDB` temporary tables used by the optimizer. The `INNODB_TEMP_TABLE_INFO` table is created when first queried, exists only in memory, and is not persisted to disk.

For usage information and examples, see [Section 17.15.7, “InnoDB INFORMATION\_SCHEMA Temporary Table Info Table”](innodb-information-schema-temp-table-info.md).

The `INNODB_TEMP_TABLE_INFO` table has these columns:

- `TABLE_ID`
	The table ID of the temporary table.
- `NAME`
	The name of the temporary table.
- `N_COLS`
	The number of columns in the temporary table. The number includes three hidden columns created by `InnoDB` (`DB_ROW_ID`, `DB_TRX_ID`, and `DB_ROLL_PTR`).
- `SPACE`
	The ID of the temporary tablespace where the temporary table resides.

#### Example

```
mysql> CREATE TEMPORARY TABLE t1 (c1 INT PRIMARY KEY) ENGINE=INNODB;

mysql> SELECT * FROM INFORMATION_SCHEMA.INNODB_TEMP_TABLE_INFO\G
*************************** 1. row ***************************
TABLE_ID: 97
    NAME: #sql8c88_43_0
  N_COLS: 4
   SPACE: 76
```

#### Notes

- This table is useful primarily for expert-level monitoring.
- You must have the [`PROCESS`](privileges-provided.md) privilege to query this table.
- Use the `INFORMATION_SCHEMA` [`COLUMNS`](information-schema-columns-table.md) table or the [`SHOW COLUMNS`](show-columns.md) statement to view additional information about the columns of this table, including data types and default values.