---
title: "10.3.1 How MySQL Uses Indexes"
book: MySQL 8.4 Reference Manual
version: "8.4"
source: "https://dev.mysql.com/doc/refman/8.4/en/mysql-indexes.html"
tags:
  - mysql
  - mysql-8.4
  - reference-manual
---

MySQL 8.4 Reference Manual Including MySQL NDB Cluster 8.4

### 10.3.1 How MySQL Uses Indexes

Indexes are used to find rows with specific column values quickly. Without an index, MySQL must begin with the first row and then read through the entire table to find the relevant rows. The larger the table, the more this costs. If the table has an index for the columns in question, MySQL can quickly determine the position to seek to in the middle of the data file without having to look at all the data. This is much faster than reading every row sequentially.

Most MySQL indexes (`PRIMARY KEY`, `UNIQUE`, `INDEX`, and `FULLTEXT`) are stored in [B-trees](glossary.md). Exceptions: Indexes on spatial data types use R-trees; `MEMORY` tables also support [hash indexes](glossary.md); `InnoDB` uses inverted lists for `FULLTEXT` indexes.

In general, indexes are used as described in the following discussion. Characteristics specific to hash indexes (as used in `MEMORY` tables) are described in [Section 10.3.9, “Comparison of B-Tree and Hash Indexes”](index-btree-hash.md).

MySQL uses indexes for these operations:

- To find the rows matching a `WHERE` clause quickly.
- To eliminate rows from consideration. If there is a choice between multiple indexes, MySQL normally uses the index that finds the smallest number of rows (the most [selective](glossary.md) index).
- If the table has a multiple-column index, any leftmost prefix of the index can be used by the optimizer to look up rows. For example, if you have a three-column index on `(col1, col2, col3)`, you have indexed search capabilities on `(col1)`, `(col1, col2)`, and `(col1, col2,             col3)`. For more information, see [Section 10.3.6, “Multiple-Column Indexes”](multiple-column-indexes.md).
- To retrieve rows from other tables when performing joins. MySQL can use indexes on columns more efficiently if they are declared as the same type and size. In this context, [`VARCHAR`](char.md) and [`CHAR`](char.md) are considered the same if they are declared as the same size. For example, `VARCHAR(10)` and `CHAR(10)` are the same size, but `VARCHAR(10)` and `CHAR(15)` are not.
	For comparisons between nonbinary string columns, both columns should use the same character set. For example, comparing a `utf8mb4` column with a `latin1` column precludes use of an index.
	Comparison of dissimilar columns (comparing a string column to a temporal or numeric column, for example) may prevent use of indexes if values cannot be compared directly without conversion. For a given value such as `1` in the numeric column, it might compare equal to any number of values in the string column such as `'1'`, `' 1'`, `'00001'`, or `'01.e1'`. This rules out use of any indexes for the string column.
- To find the [`MIN()`](aggregate-functions.md) or [`MAX()`](aggregate-functions.md) value for a specific indexed column *`key_col`*. This is optimized by a preprocessor that checks whether you are using ``WHERE *`key_part_N`* =             *`constant`*`` on all key parts that occur before *`key_col`* in the index. In this case, MySQL does a single key lookup for each [`MIN()`](aggregate-functions.md) or [`MAX()`](aggregate-functions.md) expression and replaces it with a constant. If all expressions are replaced with constants, the query returns at once. For example:
	```
	SELECT MIN(key_part2),MAX(key_part2)
	  FROM tbl_name WHERE key_part1=10;
	```
- To sort or group a table if the sorting or grouping is done on a leftmost prefix of a usable index (for example, ``ORDER BY *`key_part1`*,             *`key_part2`*``). If all key parts are followed by `DESC`, the key is read in reverse order. (Or, if the index is a descending index, the key is read in forward order.) See [Section 10.2.1.16, “ORDER BY Optimization”](order-by-optimization.md), [Section 10.2.1.17, “GROUP BY Optimization”](group-by-optimization.md), and [Section 10.3.13, “Descending Indexes”](descending-indexes.md).
- In some cases, a query can be optimized to retrieve values without consulting the data rows. (An index that provides all the necessary results for a query is called a [covering index](glossary.md).) If a query uses from a table only columns that are included in some index, the selected values can be retrieved from the index tree for greater speed:
	```
	SELECT key_part3 FROM tbl_name
	  WHERE key_part1=1
	```

Indexes are less important for queries on small tables, or big tables where report queries process most or all of the rows. When a query needs to access most of the rows, reading sequentially is faster than working through an index. Sequential reads minimize disk seeks, even if not all the rows are needed for the query. See [Section 10.2.1.23, “Avoiding Full Table Scans”](table-scan-avoidance.md) for details.