---
title: UID
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702828.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# UID

## 描述

该函数返回当前登录用户的用户 ID。

## 语法

```sql
UID
```

## 返回类型

返回一个整数。

## 示例

创建表 `tbl1`，并把当前用户的 ID 数据插入表 `tbl1` 中。

```sql
obclient> CREATE TABLE tbl1(col1 INT,user_id INT);
Query OK, 0 rows affected

obclient> INSERT INTO tbl1 VALUES(1,UID),(2,UID),(3,UID);
Query OK, 3 rows affected
Records: 3  Duplicates: 0  Warnings: 0

obclient> SELECT * FROM tbl1;
+------+------------------+
| COL1 | USER_ID          |
+------+------------------+
|    1 | 1101710651031555 |
|    2 | 1101710651031555 |
|    3 | 1101710651031555 |
+------+------------------+
3 rows in set
```
