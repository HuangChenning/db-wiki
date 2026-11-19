---
title: CHARACTER_LENGTH
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702876.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
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
