---
title: OB_VERSION
book: "SQL 参考"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004480738.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# OB_VERSION

## 声明

```sql
OB_VERSION()
```

## 说明

返回当前 OceanBase 数据库的版本信息，字符集为 utf8mb4。

## 示例

```sql
obclient> SELECT OB_VERSION();
+--------------+
| OB_VERSION() |
+--------------+
| 4.1.0.0      |
+--------------+
1 row in set
```
