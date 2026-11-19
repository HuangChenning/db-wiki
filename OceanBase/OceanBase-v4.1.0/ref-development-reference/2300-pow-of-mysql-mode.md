---
title: POW
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001700066.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
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
