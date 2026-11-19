---
title: VERSION
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001701471.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# VERSION

## 声明

```sql
VERSION()
```

## 说明

返回当前 OceanBase 数据库与 MySQL 兼容的版本号，字符集为 utf8mb4。

## 示例

```sql
obclient> SELECT VERSION();
+---------------------------+
| VERSION()                 |
+---------------------------+
| 5.7.25-OceanBase-v4.1.0.0 |
+---------------------------+
1 row in set
```
