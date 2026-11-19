---
title: REGEXP
book: "SQL 参考"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001504772.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# REGEXP

## 声明

```sql
str [NOT] REGEXP | RLIKE pat
```

## 说明

正则匹配。参数中包含 `NULL` 时，返回 `NULL`。

## 示例

```sql
obclient> SELECT
     1234 REGEXP 1,
     'hello' RLIKE 'h%'
     \G
*************************** 1. row ***************************
     1234 REGEXP 1: 1
'hello' RLIKE 'h%': 0
1 row in set
```
