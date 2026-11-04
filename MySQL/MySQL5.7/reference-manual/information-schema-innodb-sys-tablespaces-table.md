---
title: "24.4.24 The INFORMATION_SCHEMA INNODB_SYS_TABLESPACES Table"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/information-schema-innodb-sys-tablespaces-table.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 24.4.24 The INFORMATION\_SCHEMA INNODB\_SYS\_TABLESPACES Table

The `INNODB_SYS_TABLESPACES` table provides metadata about `InnoDB` file-per-table and general tablespaces, equivalent to the information in the `SYS_TABLESPACES` table in the `InnoDB` data dictionary.

For related usage information and examples, see [Section 14.16.3, “InnoDB INFORMATION\_SCHEMA System Tables”](innodb-information-schema-system-tables.md).

Note

The `INFORMATION_SCHEMA` [`FILES`](information-schema-files-table.md) table reports metadata for all `InnoDB` tablespace types including file-per-table tablespaces, general tablespaces, the system tablespace, the temporary tablespace, and undo tablespaces, if present.

The `INNODB_SYS_TABLESPACES` table has these columns:

- `SPACE`
	The tablespace ID.
- `NAME`
	The schema (database) and table name.
- `FLAG`
	A numeric value that represents bit-level information about tablespace format and storage characteristics.
- `FILE_FORMAT`
	The tablespace file format. For example, [Antelope](glossary.md), [Barracuda](glossary.md), or `Any` ([general tablespaces](glossary.md) support any row format). The data in this field is interpreted from the tablespace flags information that resides in the [.ibd file](glossary.md). For more information about `InnoDB` file formats, see [Section 14.10, “InnoDB File-Format Management”](innodb-file-format.md).
- `ROW_FORMAT`
	The tablespace row format (`Compact or           Redundant`, `Dynamic`, or `Compressed`). The data in this column is interpreted from the tablespace flags information that resides in the [`.ibd` file](glossary.md).
- `PAGE_SIZE`
	The tablespace page size. The data in this column is interpreted from the tablespace flags information that resides in the [`.ibd` file](glossary.md).
- `ZIP_PAGE_SIZE`
	The tablespace zip page size. The data in this column is interpreted from the tablespace flags information that resides in the [`.ibd` file](glossary.md).
- `SPACE_TYPE`
	The type of tablespace. Possible values include `General` for general tablespaces and `Single` for file-per-table tablespaces.
- `FS_BLOCK_SIZE`
	The file system block size, which is the unit size used for hole punching. This column pertains to the `InnoDB` [transparent page compression](innodb-page-compression.md) feature.
- `FILE_SIZE`
	The apparent size of the file, which represents the maximum size of the file, uncompressed. This column pertains to the `InnoDB` [transparent page compression](innodb-page-compression.md) feature.
- `ALLOCATED_SIZE`
	The actual size of the file, which is the amount of space allocated on disk. This column pertains to the `InnoDB` [transparent page compression](innodb-page-compression.md) feature.

#### Example

```
mysql> SELECT * FROM INFORMATION_SCHEMA.INNODB_SYS_TABLESPACES WHERE SPACE = 26\G
*************************** 1. row ***************************
         SPACE: 26
          NAME: test/t1
          FLAG: 0
   FILE_FORMAT: Antelope
    ROW_FORMAT: Compact or Redundant
     PAGE_SIZE: 16384
 ZIP_PAGE_SIZE: 0
    SPACE_TYPE: Single
 FS_BLOCK_SIZE: 4096
     FILE_SIZE: 98304
ALLOCATED_SIZE: 65536
```

#### Notes

- You must have the [`PROCESS`](privileges-provided.md) privilege to query this table.
- Use the `INFORMATION_SCHEMA` [`COLUMNS`](information-schema-columns-table.md) table or the [`SHOW COLUMNS`](show-columns.md) statement to view additional information about the columns of this table, including data types and default values.
- Because tablespace flags are always zero for all Antelope file formats (unlike table flags), there is no way to determine from this flag integer if the tablespace row format is Redundant or Compact. As a result, the possible values for the `ROW_FORMAT` field are “Compact or Redundant”, “Compressed”, or “Dynamic.”
- With the introduction of general tablespaces, `InnoDB` system tablespace data (for SPACE 0) is exposed in `INNODB_SYS_TABLESPACES`.