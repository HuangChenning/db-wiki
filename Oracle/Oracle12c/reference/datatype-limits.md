---
title: Database Reference
book: Database Reference
doc_id: E85634-25
version: "12.2"
source: https://docs.oracle.com/en/database/oracle/oracle-database/12.2/refrn/datatype-limits.html
tags:
  - oracle
  - 12c
  - reference
---

This table documents the limits for datatypes, and includes comments about the datatypes.

| Datatypes | Limit | Comments |
| --- | --- | --- |
| `BFILE` | Maximum size: 4 GB  Maximum size of a file name: 255 characters  Maximum size of a directory name: 128 bytes  Maximum number of open BFILEs: see Comments | The maximum number of `BFILEs` is limited by the value of the `SESSION_MAX_OPEN_FILES` initialization parameter, which is itself limited by the maximum number of open files the operating system will allow. |
| `BLOB` | Maximum size: (4 GB - 1) \* `DB_BLOCK_SIZE` initialization parameter (8 TB to 128 TB) | The number of LOB columns per table is limited only by the maximum number of columns per table (that is, 1000 <sup>Foot 1</sup>). |
| `CHAR` | Maximum size: 2000 bytes | None |
| `CLOB` | Maximum size: (4 GB - 1) \* `DB_BLOCK_SIZE` initialization parameter (8 TB to 128 TB) | The number of LOB columns per table is limited only by the maximum number of columns per table (that is, 1000 <sup>Foot 1</sup>). |
| Literals (characters or numbers in SQL or PL/SQL) | Maximum size: 4000 characters | None |
| `LONG` | Maximum size: 2 GB - 1 | Only one `LONG` column is allowed per table. |
| `NCHAR` | Maximum size: 2000 bytes | None |
| `NCLOB` | Maximum size: (4 GB - 1) \* `DB_BLOCK_SIZE` initialization parameter (8 TB to 128 TB) | The number of LOB columns per table is limited only by the maximum number of columns per table (that is, 1000 <sup>Foot 1</sup>). |
| `NUMBER` | 999...(38 9's) x10 <sup>125</sup> maximum value  \-999...(38 9's) x10 <sup>125</sup> minimum value | Can be represented to full 38-digit precision (the mantissa)  Can be represented to full 38-digit precision (the mantissa) |
| `NVARCHAR2` | Maximum size: 4000 bytes, or 32767 bytes if the `MAX_STRING_SIZE` initialization parameter is set to `EXTENDED`  See Also: " [MAX\_STRING\_SIZE](MAX_STRING_SIZE.md) " initialization parameter for additional details | None |
| Precision | 38 significant digits | None |
| `RAW` | Maximum size: 2000 bytes, or 32767 bytes if the `MAX_STRING_SIZE` initialization parameter is set to `EXTENDED`  See Also: " [MAX\_STRING\_SIZE](MAX_STRING_SIZE.md) " initialization parameter for additional details | None |
| `VARCHAR2` | Maximum size: 4000 bytes, or 32767 bytes if the `MAX_STRING_SIZE` initialization parameter is set to `EXTENDED`  See Also: " [MAX\_STRING\_SIZE](MAX_STRING_SIZE.md) " initialization parameter for additional details | None |

<sup>Footnote 1</sup>

The absolute maximum number of columns in a table is 1000. However, when you create an object table (or a relational table with columns of object, nested table, varray, or `REF` type), Oracle maps the columns of the user-defined types to relational columns, creating in effect hidden columns that count toward the 1000-column limit. For details on how Oracle calculates the total number of columns in such a table, refer to [Oracle Database Administrator’s Guide](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=ADMIN11632).

See Also:

- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=SQLRF0021) for more information about datatypes
- [Oracle Database SQL Language Reference](https://docs.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/12.2/refrn&id=SQLRF00223) for more information on naming database objects