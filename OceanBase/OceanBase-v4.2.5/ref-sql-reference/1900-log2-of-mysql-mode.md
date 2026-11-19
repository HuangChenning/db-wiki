---
title: LOG2
book: "SQL 参考"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001504666.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# LOG2

## 声明

```sql
LOG2(X)
```

## 说明

返回以 2 为底的 `X` 的对数。`X` 是一个正实数，即你想要计算其以 2 为底的对数的数值。

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
