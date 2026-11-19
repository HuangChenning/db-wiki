---
title: NEG
book: "SQL 参考"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005288174.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# NEG

## 声明

```sql
NEG(expr)
```

## 说明

求补函数，对操作数执行求补运算，即用零减去操作数，然后结果返回操作数。

支持比较运算，结果为 BOOL 值，被转化为数字类型处理，产生的结果为 `1`(`TRUE`)、`0` (`FALSE`)，再对结果求补。

## 示例

```sql
obclient> SELECT NEG(1), NEG(1+1), NEG(2*3), NEG(1=1), NEG(5<1);
+--------+----------+----------+----------+----------+
| NEG(1) | NEG(1+1) | NEG(2*3) | NEG(1=1) | NEG(5<1) |
+--------+----------+----------+----------+----------+
|     -1 |       -2 |       -6 |       -1 |        0 |
+--------+----------+----------+----------+----------+
1 row in set
```
