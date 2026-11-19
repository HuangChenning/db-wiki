---
title: DATABASE
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702762.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# DATABASE

## 声明

```sql
DATABASE()
```

## 说明

返回当前数据库名称，字符集为 utf8mb4。

如果没有通过 `USE` 语句指定数据库，则返回 `NULL`。

## 示例

返回当前的数据库名称。

```sql
obclient> SELECT DATABASE();
+------------+
| DATABASE() |
+------------+
| oceanbase  |
+------------+
1 row in set 
```
