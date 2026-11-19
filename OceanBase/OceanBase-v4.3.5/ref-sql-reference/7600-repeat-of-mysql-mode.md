---
title: REPEAT
book: "SQL 参考"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002018296.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# REPEAT

## 声明

```sql
REPEAT(str, count)
```

## 说明

返回 `str` 重复 `count` 次组成的字符串。`count` 小于等于 0 时，返回空字符串。参数中包含 `NULL` 时，返回 `NULL`。

## 示例

```javascript
obclient> SELECT
     REPEAT('1', -1),
     REPEAT(null, null),
     REPEAT('Abc', 4)
     \G
*************************** 1. row ***************************
   REPEAT('1', -1):
REPEAT(null, null): NULL
  REPEAT('Abc', 4): AbcAbcAbcAbc
1 row in set
```
