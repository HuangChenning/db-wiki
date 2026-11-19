---
title: LOG2
book: "SQL 参考"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005288202.html"
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
