---
title: CHARACTER_LENGTH
book: "SQL 参考"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005288283.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# CHARACTER_LENGTH

## 声明

```sql
CHARACTER_LENGTH(str)
```

## 说明

`CHARACTER_LENGTH()` 是 `CHAR_LENGTH()` 的同义词。

## 示例

```sql
obclient> SELECT CHARACTER_LENGTH('中国'), LENGTH('中国'),CHARACTER_LENGTH('hello');
+----------------------------+------------------+---------------------------+
| CHARACTER_LENGTH('中国')   | LENGTH('中国')   | CHARACTER_LENGTH('hello') |
+----------------------------+------------------+---------------------------+
|                          2 |                6 |                         5 |
+----------------------------+------------------+---------------------------+
1 row in set
```
