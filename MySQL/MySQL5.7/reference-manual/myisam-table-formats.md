---
title: "15.2.3 MyISAM Table Storage Formats"
book: MySQL 5.7 Reference Manual
version: "5.7"
source: "https://dev.mysql.com/doc/refman/5.7/en/myisam-table-formats.html"
tags:
  - mysql
  - mysql-5.7
  - reference-manual
---

MySQL 5.7 Reference Manual Including MySQL NDB Cluster 7.5 and NDB Cluster 7.6

### 15.2.3 MyISAM Table Storage Formats

`MyISAM` supports three different storage formats. Two of them, fixed and dynamic format, are chosen automatically depending on the type of columns you are using. The third, compressed format, can be created only with the [**myisampack**](myisampack.md) utility (see [Section 4.6.5, “myisampack — Generate Compressed, Read-Only MyISAM Tables”](myisampack.md)).

When you use [`CREATE TABLE`](create-table.md) or [`ALTER TABLE`](alter-table.md) for a table that has no [`BLOB`](blob.md) or [`TEXT`](blob.md) columns, you can force the table format to `FIXED` or `DYNAMIC` with the `ROW_FORMAT` table option.

See [Section 13.1.18, “CREATE TABLE Statement”](create-table.md), for information about `ROW_FORMAT`.

You can decompress (unpack) compressed `MyISAM` tables using [**myisamchk**](myisamchk.md) [`--unpack`](myisamchk-repair-options.md); see [Section 4.6.3, “myisamchk — MyISAM Table-Maintenance Utility”](myisamchk.md), for more information.