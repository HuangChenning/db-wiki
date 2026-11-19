---
title: POW
book: "SQL 参考"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004481273.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# POW

## 声明

```sql
POW(X,Y)
```

## 说明

返回 `X` 的 `Y` 次方。

`X` 与 `Y` 中任何一个参数为 `NULL`，返回值都为 `NULL`。

## 示例

```sql
obclient> SELECT POW(4,2), POW(4,-2), POW(1,NULL);
+----------+-----------+-------------+
| POW(4,2) | POW(4,-2) | POW(1,NULL) |
+----------+-----------+-------------+
|       16 |    0.0625 |        NULL |
+----------+-----------+-------------+
1 row in set
```
