---
title: "24.4.21 The INFORMATION_SCHEMA INNODB_SYS_FOREIGN_COLS Table"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/information-schema-innodb-sys-foreign-cols-table.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 24.4.21 The INFORMATION\_SCHEMA INNODB\_SYS\_FOREIGN\_COLS Table

The `INNODB_SYS_FOREIGN_COLS` table provides status information about the columns of `InnoDB` foreign keys, equivalent to the information from the `SYS_FOREIGN_COLS` table in the `InnoDB` data dictionary.

For related usage information and examples, see [Section 14.16.3, “InnoDB INFORMATION\_SCHEMA System Tables”](innodb-information-schema-system-tables.md).

The `INNODB_SYS_FOREIGN_COLS` table has these columns:

- `ID`
	The foreign key index associated with this index key field, using the same value as `INNODB_SYS_FOREIGN.ID`.
- `FOR_COL_NAME`
	The name of the associated column in the child table.
- `REF_COL_NAME`
	The name of the associated column in the parent table.
- `POS`
	The ordinal position of this key field within the foreign key index, starting from 0.

#### Example

```
mysql> SELECT * FROM INFORMATION_SCHEMA.INNODB_SYS_FOREIGN_COLS WHERE ID = 'test/fk1'\G
*************************** 1. row ***************************
          ID: test/fk1
FOR_COL_NAME: parent_id
REF_COL_NAME: id
         POS: 0
```

#### Notes

- You must have the [`PROCESS`](privileges-provided.md) privilege to query this table.
- Use the `INFORMATION_SCHEMA` [`COLUMNS`](information-schema-columns-table.md) table or the [`SHOW COLUMNS`](show-columns.md) statement to view additional information about the columns of this table, including data types and default values.