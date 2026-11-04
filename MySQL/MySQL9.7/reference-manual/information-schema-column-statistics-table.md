---
title: "28.3.11 The INFORMATION_SCHEMA COLUMN_STATISTICS Table"
book: MySQL 9.7 Reference Manual
version: "9.7"
source: "https://dev.mysql.com/doc/refman/9.7/en/information-schema-column-statistics-table.html"
tags:
  - mysql
  - mysql-9.7
  - reference-manual
---

MySQL 9.7 Reference Manual Including MySQL NDB Cluster 9.7

### 28.3.11 The INFORMATION\_SCHEMA COLUMN\_STATISTICS Table

The `COLUMN_STATISTICS` table provides access to histogram statistics for column values.

For information about histogram statistics, see [Section 10.9.6, “Optimizer Statistics”](optimizer-statistics.md), and [Section 15.7.3.1, “ANALYZE TABLE Statement”](analyze-table.md).

You can see information only for columns for which you have some privilege.

The `COLUMN_STATISTICS` table has these columns:

- `SCHEMA_NAME`
	The names of the schema for which the statistics apply.
- `TABLE_NAME`
	The names of the column for which the statistics apply.
- `COLUMN_NAME`
	The names of the column for which the statistics apply.
- `HISTOGRAM`
	A [`JSON`](json.md) object describing the column statistics, stored as a histogram.