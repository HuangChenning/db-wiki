---
title: BIT_COUNT
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001700049.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# BIT_COUNT

## 声明

```sql
BIT_COUNT(N)
```

## 说明

返回 `N` 转换为二进制后 `1` 的数量。如果 `N` 为 `NULL`，则返回 `NULL`。

## 示例

```sql
obclient> SELECT BIT_COUNT(42), BIT_COUNT(b'1010');
+---------------+--------------------+
| BIT_COUNT(42) | BIT_COUNT(b'1010') |
+---------------+--------------------+
|             3 |                  2 |
+---------------+--------------------+
1 row in set 
```
