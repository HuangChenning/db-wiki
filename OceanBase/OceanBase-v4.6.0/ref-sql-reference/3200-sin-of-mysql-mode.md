---
title: SIN
book: "SQL 参考"
version: V4.6.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005687905.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# SIN

## 声明

```sql
SIN(X)
```

## 说明

返回给定弧度 `X` 的正弦值。

## 示例

```sql
obclient> SELECT SIN(PI());
+------------------------+
| SIN(PI())              |
+------------------------+
| 1.2246467991473532e-16 |
+------------------------+
1 row in set
```
