---
title: OCT
book: "SQL 参考"
version: V4.6.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005687979.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# OCT

## 声明

```sql
OCT(N)
```

## 描述

返回 `N` 的八进制值，该函数等价于 `CONV(N,10,8)`。

如果 `N` 为 `NULL`，则该函数返回 `NULL`。

## 示例

```sql
obclient> SELECT OCT(12);
+---------+
| OCT(12) |
+---------+
| 14      |
+---------+
1 row in set
```
