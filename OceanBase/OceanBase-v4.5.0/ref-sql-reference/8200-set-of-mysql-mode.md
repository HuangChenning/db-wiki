---
title: SET
book: "SQL 参考"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004479614.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# SET

## 描述

该语句用于设置变量。

## 语法

```sql
SET [SESSION | GLOBAL] var_and_val_list

var_and_val_list:
  var_and_val [,var_and_val ...]

var_and_val:
   var_value {TO | =} set_expr_or_default
 | var_value = (simple_select)
```

## 参数解释

|        参数         |         描述          |
|-------------------|---------------------|
| SESSION \| GLOBAL | 设置会话或全局变量，默认为会话级变量。 |
| var_value         | 变量名。                |

## 示例

1. 设置用户变量 `a`。

   ```sql
   obclient> SET @a = 1;
   ```

2. 设置全局系统变量 `secure_file_priv`，该变量用于控制导入或导出到文件时可以访问的路径。

   ```sql
   obclient> SET GLOBAL secure_file_priv = '';
   ```

3. 设置用户变量 `proxy_route_policy`，该用户变量用于配置路由策略。

   ```sql
   obclient> SET @proxy_route_policy = 'follower_first';
   ```

4. 通过 `SELECT` 语句设置变量值。

   ```sql
   obclient> CREATE TABLE tbl1(col INT);
   obclient> INSERT into tbl1 VALUES('1'),('2'),('3'),('4'),('5');
   obclient> SET @var1=(SELECT COUNT(*) FROM tbl1);
   ```

   查询变量值：

   ```sql
   obclient> SELECT @var1;
   ```

   查询结果如下：

   ```sql
   +-------+
   | @var1 |
   +-------+
   |     5 |
   +-------+
   1 row in set
   ```
