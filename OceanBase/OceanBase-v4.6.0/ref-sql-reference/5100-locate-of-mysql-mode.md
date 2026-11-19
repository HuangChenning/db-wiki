---
title: LOCATE
book: "SQL 参考"
version: V4.6.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005688018.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# LOCATE

## 声明

```sql
LOCATE(substr,str)
LOCATE(substr,str,pos)
```

## 说明

第一个语法返回字符串 `str` 中子字符串 `substr` 的第一个出现位置。第二个语法返回字符串 `str` 中子字符串 `substr` 的第一个出现位置，起始位置在 `pos`。如果 `substr` 不在 `str` 中，则返回值为 `0`。

## 示例

```sql
obclient> SELECT LOCATE('bar', 'foobarbar'), LOCATE('xbar', 'foobar'), LOCATE('bar', 'foobarbar',5);
+----------------------------+--------------------------+------------------------------+
| LOCATE('bar', 'foobarbar') | LOCATE('xbar', 'foobar') | LOCATE('bar', 'foobarbar',5) |
+----------------------------+--------------------------+------------------------------+
|                          4 |                        0 |                            7 |
+----------------------------+--------------------------+------------------------------+
1 row in set
```
