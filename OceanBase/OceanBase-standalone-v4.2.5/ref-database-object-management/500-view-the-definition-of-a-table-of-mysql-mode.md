---
title: "查看表"
book: "数据库对象管理"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003150290.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 查看表

表创建成功后，您可以通过 SQL 语句查看数据库中的所有表，以及指定表的定义和表结构等。

## 查看数据库中的表

表创建成功后，可以使用 `SHOW TABLES` 语句查看数据库的所有表。语句如下：

``` sql
SHOW [EXTENDED] [FULL] TABLES [{FROM | IN} database_name];
```

语句中：

- `EXTENDED`：展示隐藏的表。由于 OceanBase 数据库当前版本不会产生隐藏表，该参数无实际作用。

- `FULL`：展示表类型。

- `database_name`：待查询的数据库。

查看数据库 `test` 中所有表的示例如下：

``` sql
SHOW TABLES FROM test;
```

查询结果如下：

```
+----------------+
| Tables_in_test |
+----------------+
| t1             |
+----------------+
1 row in set
```

更多 `SHOW TABLES` 语句的介绍，请参见 [SHOW](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001503274)。

## 查看表的定义

表创建成功后，您可以使用 `SHOW CREATE TABLE` 语句查看表的定义。

查看表 `test` 的定义的示例如下：

``` sql
obclient [test]> SHOW CREATE TABLE tbl1;
```

结果如下：

```
+-------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                                                                                                                                               |
+-------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| tbl1  | CREATE TABLE `tbl1` (
  `col1` int(11) NOT NULL,
  `col2` int(11) DEFAULT NULL
) DEFAULT CHARSET = utf8mb4 ROW_FORMAT = DYNAMIC COMPRESSION = 'zstd_1.3.8' REPLICA_NUM = 1 BLOCK_SIZE = 16384 USE_BLOOM_FILTER = FALSE TABLET_SIZE = 134217728 PCTFREE = 0 |
+-------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
1 row in set
```

部分字段说明如下：

- `DEFAULT CHARSET = utf8mb4`：指定默认字符集为 `utf8mb4`。

- `ROW_FORMAT = DYNAMIC`：表示打开数据编码。

- `COMPRESSION`：表的压缩方式。

- `PCTFREE`：表示留给更新该块数据的使用空间。

## 查看表结构

表创建成功后，您可以使用 `SHOW COLUMNS/FIELDS` 语句查看表结构。语句如下：

``` sql
SHOW [EXTENDED] [FULL] {COLUMNS | FIELDS}
    {FROM | IN} table_name
    [{FROM | IN} database_name];
```

语句中：

- `EXTENDED`：展示隐藏的列。

- `FULL`：展示列的字符序、权限与注释。

- `table_name`：待查询的表。

- `database_name`：待查询的表所属的数据库。

示例如下：

- 查看表 `test` 的表结构。

  ``` sql
  obclient [test]> SHOW COLUMNS FROM tbl1;
  ```

  查询结果如下：

  ```
  +-------+---------+------+------+---------+-------+
  | Field | Type    | Null | Key  | Default | Extra |
  +-------+---------+------+------+---------+-------+
  | col1  | int(11) | NO   |      | NULL    |       |
  | col2  | int(11) | YES  |      | NULL    |       |
  +-------+---------+------+------+---------+-------+
  2 rows in set
  ```

- 查看表 `test` 中包括隐藏的列在内的所有列。

  ``` sql
  obclient [test]> SHOW EXTENDED COLUMNS FROM tbl1;
  ```

  查询结果如下：

  ```
  +----------------+-----------------+------+------+---------+-------+
  | Field          | Type            | Null | Key  | Default | Extra |
  +----------------+-----------------+------+------+---------+-------+
  | col1           | int(11)         | NO   |      | NULL    |       |
  | col2           | int(11)         | YES  |      | NULL    |       |
  | __pk_increment | bigint unsigned | NO   | PRI  | NULL    |       |
  +----------------+-----------------+------+------+---------+-------+
  3 rows in set
  ```

更多 `SHOW COLUMNS/FIELDS` 语句的介绍，请参见 [SHOW](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001503274)。

## 检查表

可以使用 `CHECK TABLE` 语句检查数据库中的表是否存在。

有关 `CHECK TABLE` 语句的详细信息，参见 [CHECK TABLE](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001503313)。

**示例如下：**

1.  当表 `tbl3` 不存在时，查看检查表 `tbl3` 的返回信息。

    ```
    obclient [test]> CHECK TABLE tbl3;
    ```

    返回结果如下：

    ```
    +-----------+-------+----------+---------------------------------+
    | Table     | Op    | Msg_type | Msg_text                        |
    +-----------+-------+----------+---------------------------------+
    | test.tbl3 | check | Error    | Table 'test.tbl3' doesn't exist |
    | test.tbl3 | check | status   | Operation failed                |
    +-----------+-------+----------+---------------------------------+
    2 rows in set
    ```

2.  创建表 `tbl3`。

    ```
    obclient [test]> CREATE TABLE tbl3(col1 INT, col2 VARCHAR(18));
    ```

3.  再次检查表 `tbl3`，查看返回信息。

    ```
    obclient [test]> CHECK TABLE tbl3;
    ```

    返回结果如下：

    ```
    +-----------+-------+----------+----------+
    | Table     | Op    | Msg_type | Msg_text |
    +-----------+-------+----------+----------+
    | test.tbl3 | check | status   | OK       |
    +-----------+-------+----------+----------+
    1 row in set
    ```
