---
title: COS
book: "SQL 参考"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005288204.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# COS

## 声明

```sql
COS(X)
```

## 说明

返回给定弧度 `X` 的余弦值。

## 示例

```sql
obclient> SELECT COS(PI());
+-----------+
| COS(PI()) |
+-----------+
|        -1 |
+-----------+
1 row in set
```
