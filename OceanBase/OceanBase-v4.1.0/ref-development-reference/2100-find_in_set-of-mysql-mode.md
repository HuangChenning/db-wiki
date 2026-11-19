---
title: FIND_IN_SET
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702882.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# FIND_IN_SET

## 声明

```sql
FIND_IN_SET(str,strlist)
```

## 说明

返回字符串集合 `strlist` 中指定字符串 `str` 的位置，从 `1` 开始。如果 `str` 不存在于 `strlist`，则返回 `0`。如果 `str` 或 `strlist` 为 `NULL`，则返回 `NULL`。

`str` 字符串中不能包含逗号（,）。

## 示例

```sql
obclient> SELECT FIND_IN_SET('b','a,b,c,d');
+----------------------------+
| FIND_IN_SET('b','a,b,c,d') |
+----------------------------+
|                          2 |
+----------------------------+
1 row in set 
```
