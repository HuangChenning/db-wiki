---
title: LOG2
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001700062.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# LOG2

## 声明

```sql
LOG2(X)
```

## 说明

返回以 2 为底的 `X` 的指数。

## 示例

```sql
obclient> SELECT LOG2(65536);
+-------------+
| LOG2(65536) |
+-------------+
|          16 |
+-------------+
1 row in set

obclient> SELECT LOG2(-65536);
+--------------+
| LOG2(-65536) |
+--------------+
|         NULL |
+--------------+
1 row in set, 1 warning 
```
