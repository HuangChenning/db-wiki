---
title: HEX
book: "SQL 参考"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005288320.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# HEX

## 声明

```sql
HEX(str)
```

## 说明

将数字或字符串 `str` 转化为十六进制字符串，其中 `str` 中的每个字符的每个字节都转换为两个十六进制数字。

对于数字类型的参数 `N`，`UNHEX(N)` 并不是 `HEX(N)` 的逆运算，对于这种情况，您可以使用 `CONV(HEX(N),16,10)` 替代。

## 示例

```sql
obclient> SELECT HEX(255), HEX('abc');
+----------+------------+
| HEX(255) | HEX('abc') |
+----------+------------+
| FF       | 616263     |
+----------+------------+
1 row in set
```
