---
title: "管理普通视图"
book: "数据库对象管理"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577893.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 管理普通视图

#### 说明

- OceanBase 数据库 Oracle 模式支持在创建视图时，通过 `--string` 给视图添加注释。此时，注释存储在视图定义中。
  - `--string` 可以注释在 `select_stmt` 的任意位置。

- `[NO] FORCE`：如果创建视图时，不希望考虑该视图是否存在基表或存在引用的对象类型，以及视图所在 Schema 的所有者是否具有权限时，则需要指定 `FORCE`。

  如果已确认基表存在且视图所在 Schema 的所有者具有权限，则可以指定 `NO FORCE`。默认为 `NO FORCE`。

- `column_name_list`：与基表一样，视图必须具有唯一的列名，不能重复。缺省情况下，由 `SELECT` 语句检索的列名将用作视图列名。

  如果想为视图列定义明确的名称，可使用可选的 `column_name_list` 子句，ID 之间使用逗号分隔。`column_name_list` 中的名称数目必须等于 `SELECT`语句检索的列数。

  `SELECT` 语句检索的列可以是对表列的简单引用。也可以是使用函数、常量值、运算符等的表达式。

**示例如下：**

- 选择表 `tbl1` 中的 `col1`、`col2` 列来创建视图 `view1`。

  ```
  obclient> CREATE OR REPLACE FORCE VIEW view1(vcol1, vcol2) AS SELECT col1, col2 FROM tbl1;
  ```

- 基于表 `tbl2` 的 `col1`、`col2` 列来创建视图 `view4`，并同时为视图 `view4` 添加注释。

  1.  创建表 `tbl2`。

      ```
      obclient [SYS]> CREATE TABLE tbl2 (col1 INT, col2 INT);
      ```

  2.  创建视图 `view4`。

      ```
      obclient [SYS]> CREATE VIEW view4
        AS SELECT col1, --col1 comment1
          col2 --col1 comment2
          FROM tbl2;
      ```

## 修改普通视图

您可以使用 `CREATE OR REPLACE VIEW` 语句来对普通视图进行修改。

示例：修改视图 `stock_item`。

``` sql
obclient> CREATE OR REPLACE VIEW stock_item
     AS
     SELECT /*+ leading(s) use_merge(i) */
     i_price, i_name, i_data, s_i_id, s_w_id, s_order_cnt, s_ytd, s_remote_cnt, s_quantity, s_data, s_dist_01, s_dist_02, s_dist_03, s_dist_04, s_dist_05, s_dist_06, s_dist_07, s_dist_08, s_dist_09, s_dist_10
     FROM stok s, item i
     WHERE s.s_i_id = i.i_id;
Query OK, 0 rows affected (0.02 sec)
```

## 删除视图

您可以使用 `DROP VIEW` 语句删除一个或多个视图，删除视图并不会删除视图所引用的表。

如果当前视图被其他视图所引用，则被依赖视图删除后将会导致依赖当前视图的其他视图的查询失败。

删除视图时，需确保当前用户具备该视图的 `DROP` 权限。

Oracle 模式下，删除视图的 SQL 语法如下：

``` sql
obclient>DROP VIEW view_name;
```

示例：删除视图 `v1`。

``` sql
obclient> DROP VIEW v1;
```

## 相关文档

- [CREATE VIEW](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002017454)

- [DROP VIEW](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002017435)
