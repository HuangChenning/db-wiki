---
title: LOG10
book: "SQL 参考"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005288188.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# LOG10

## 声明

```sql
LOG10(X)
```

## 说明

返回以 10 为底的 `X` 的指数。

## 示例

```sql
obclient> SELECT LOG10(1000);
+-------------+
| LOG10(1000) |
+-------------+
|           3 |
+-------------+
1 row in set

obclient> SELECT LOG10(-1000);
+--------------+
| LOG10(-1000) |
+--------------+
|         NULL |
+--------------+
1 row in set, 1 warning
```
