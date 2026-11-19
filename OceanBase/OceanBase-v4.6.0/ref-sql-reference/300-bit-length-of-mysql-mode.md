---
title: BIT_LENGTH
book: "SQL 参考"
version: V4.6.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005688036.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# BIT_LENGTH

## 声明

```sql
BIT_LENGTH(str)
```

## 说明

返回字符串 `str` 的比特位长度。

## 示例

```sql
obclient> SELECT BIT_LENGTH('oceanbase');
+-------------------------+
| BIT_LENGTH('oceanbase') |
+-------------------------+
|                      72 |
+-------------------------+
1 row in set
```
