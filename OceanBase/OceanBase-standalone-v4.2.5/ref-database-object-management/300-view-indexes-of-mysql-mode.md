---
title: "查看索引"
book: "数据库对象管理"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003150315.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 查看索引

可以使用 `SHOW INDEX/INDEXES/KEYS` 语句查看表的索引。

语句如下：

``` sql
SHOW [EXTENDED] {INDEX | INDEXES | KEYS}
    {FROM | IN} table_name
    [{FROM | IN} database_name];
```

语句中：

- `EXTENDED`：展示隐藏的索引。

- `table_name`：待查询的索引表。

- `database_name`：待查询表所属的数据库。

示例如下：

- 查看表 `test` 的索引。

  ``` sql
  obclient [test]> SHOW INDEX FROM test;
  ```

  查询结果如下：

  ```
  +-------+------------+-----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+-----------+---------------+---------+------------+
  | Table | Non_unique | Key_name  | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment   | Index_comment | Visible | Expression |
  +-------+------------+-----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+-----------+---------------+---------+------------+
  | test  |          0 | PRIMARY   |            1 | id          | A         |        NULL | NULL     | NULL   |      | BTREE      | available |               | YES     | NULL       |
  | test  |          1 | tbl1_idx1 |            1 | date        | A         |        NULL | NULL     | NULL   | YES  | BTREE      | available |               | YES     | NULL       |
  +-------+------------+-----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+-----------+---------------+---------+------------+
  2 rows in set
  ```

  相关字段说明如下：

  - `Non_unique`：如果索引不能包括重复值则为 `0`，如果可以则为 `1`。也就是通常所说的唯一索引。

  - `Key_name`：索引名。

  - `Seq_in_index`：索引中的列序列号，`1` 或者 `2`，用于表明该索引在联合索引中的顺序。

  - `Column_name`：索引的列名。

  - `Collation`：表示列以什么方式存储在索引中。

  - `Cardinality`：基数的意思，表示索引中唯一值的数目的估计值。

  - `Sub_part`：前缀索引，如果列只是被部分地编入索引，则为被编入索引的字符的数目。如果整列被编入索引，则为 `NULL`。

  - `Packed`：指示关键字如何被压缩。如果没有被压缩，则为 `NULL`。

  - `Null`：表示索引值是否可以为空。

  - `Index_type`：表示索引类型。当前仅支持 `BTREE` 类型。

  - `Comment`：表示该索引是否可用。

  - `Index_comment`：该索引的注释信息。

  - `Visible`：表示该索引是否可见。

- 查看表 `test` 中包括隐藏索引在内的所有索引。

  ``` sql
  obclient [test]> SHOW EXTENDED INDEX FROM test;
  ```

  查询结果如下：

  ```
  +-------+------------+-----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+-----------+---------------+---------+------------+
  | Table | Non_unique | Key_name  | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment   | Index_comment | Visible | Expression |
  +-------+------------+-----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+-----------+---------------+---------+------------+
  | test  |          0 | PRIMARY   |            1 | id          | A         |        NULL | NULL     | NULL   |      | BTREE      | available |               | YES     | NULL       |
  | test  |          0 | PRIMARY   |            2 | name        | A         |        NULL | NULL     | NULL   |      | BTREE      | available |               | YES     | NULL       |
  | test  |          0 | PRIMARY   |            3 | date        | A         |        NULL | NULL     | NULL   |      | BTREE      | available |               | YES     | NULL       |
  | test  |          1 | tbl1_idx1 |            1 | date        | A         |        NULL | NULL     | NULL   | YES  | BTREE      | available |               | YES     | NULL       |
  | test  |          1 | tbl1_idx1 |            2 | id          | A         |        NULL | NULL     | NULL   |      | BTREE      | available |               | YES     | NULL       |
  +-------+------------+-----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+-----------+---------------+---------+------------+
  5 rows in set
  ```

更多 `SHOW INDEX` 语句的介绍，请参见 [SHOW](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001503274)。

## 使用视图查看索引信息

- 可以使用视图 [information_schema.STATISTICS](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001501714) 查看表索引信息，包含表名、是否是唯一索引、索引名、索引编号、列名等。

- 可以使用视图 [oceanbase.DBA_OB_TABLE_LOCATIONS](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001501743) 查看索引是全局索引（`GLOBAL`）还是局部索引（`LOCAL`）。

**示例如下：**

1.  查看表 `tbl1` 下有哪些视图。

    ``` sql
    SELECT TABLE_SCHEMA, TABLE_NAME, SEQ_IN_INDEX, INDEX_NAME, COLUMN_NAME
    FROM information_schema.STATISTICS
    WHERE TABLE_NAME = 'tbl1';
    ```

    返回结果如下：

    ```
    +--------------+------------+--------------+------------+-------------+
    | TABLE_SCHEMA | TABLE_NAME | SEQ_IN_INDEX | INDEX_NAME | COLUMN_NAME |
    +--------------+------------+--------------+------------+-------------+
    | test         | tbl1       |            1 | tbl1_idx1  | date        |
    | test         | tbl1       |            1 | PRIMARY    | id          |
    +--------------+------------+--------------+------------+-------------+
    2 rows in set
    ```

2.  查看索引 `tbl1_idx1` 是全局索引（`GLOBAL`）还是局部索引（`LOCAL`）。

    ``` sql
    SELECT DATABASE_NAME, INDEX_NAME, INDEX_TYPE
    FROM oceanbase.DBA_OB_TABLE_LOCATIONS
    WHERE INDEX_NAME = 'tbl1_idx1';
    ```

    返回结果如下：

    ```
    +---------------+------------+------------+
    | DATABASE_NAME | INDEX_NAME | INDEX_TYPE |
    +---------------+------------+------------+
    | test          | tbl1_idx1  | LOCAL      |
    +---------------+------------+------------+
    1 row in set
    ```

3.  从视图 `information_schema.STATISTICS` 和 `oceanbase.DBA_OB_TABLE_LOCATIONS` 中获取表 `tbl1` 的索引信息。

    ``` sql
    SELECT ss.TABLE_SCHEMA, ss.TABLE_NAME, ss.SEQ_IN_INDEX, ss.INDEX_NAME, ss.COLUMN_NAME, ls.INDEX_TYPE
    FROM information_schema.STATISTICS ss, oceanbase.DBA_OB_TABLE_LOCATIONS ls
    WHERE ss.TABLE_SCHEMA = ls.DATABASE_NAME
      AND ss.INDEX_NAME = ls.INDEX_NAME
      AND ss.TABLE_NAME = 'tbl1';
    ```

    返回结果如下：

    ```
    +--------------+------------+--------------+------------+-------------+------------+
    | TABLE_SCHEMA | TABLE_NAME | SEQ_IN_INDEX | INDEX_NAME | COLUMN_NAME | INDEX_TYPE |
    +--------------+------------+--------------+------------+-------------+------------+
    | test         | tbl1       |            1 | tbl1_idx1  | date        | LOCAL      |
    +--------------+------------+--------------+------------+-------------+------------+
    1 row in set
    ```

## 相关文档

更多 MySQL 模式下索引相关的内容，参见以下信息：

- [索引简介](../ref-oceanbase-database-concepts/100-index-overview-of-mysql-mode.md)

- [创建索引](100-about-indexes-of-mysql-mode.md)

- [在分区表上建立索引](200-local-index-of-mysql-mode.md)

- [删除索引](400-delete-an-index-of-mysql-mode.md)
