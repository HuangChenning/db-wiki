---
title: ABS
book: "SQL 参考"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005288184.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# ABS

## 声明

```sql
ABS(expr)
```

## 说明

绝对值函数，求表达式绝对值，函数返回值类型与数值表达式的数据类型相同。

支持比较运算，结果为 BOOL 值，被转化为数字类型处理，产生的结果为 `1`(`TRUE`)、`0` (`FALSE`)。

如果输入 `NULL`，返回值为 `NULL`。

如果输入纯数字的字符串，支持自动转换成数字类型。返回值会被转化为一个 `BIGINT`。

## 示例

```javascript
obclient> SELECT ABS(5), ABS(-5.777), ABS(0), ABS(1/2), ABS(1-5);
+--------+-------------+--------+----------+----------+
| ABS(5) | ABS(-5.777) | ABS(0) | ABS(1/2) | ABS(1-5) |
+--------+-------------+--------+----------+----------+
|      5 |       5.777 |      0 |   0.5000 |        4 |
+--------+-------------+--------+----------+----------+
1 row in set
```
