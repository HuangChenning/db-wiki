---
title: OCTET_LENGTH
book: "SQL 参考"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005288275.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# OCTET_LENGTH

## 声明

```sql
OCTET_LENGTH(str)
```

## 说明

`OCTET_LENGTH()` 是 `LENGTH()` 的同义词。

## 示例

```sql
obclient> SELECT OCTET_LENGTH('中国'), OCTET_LENGTH('hello');
+------------------------+-----------------------+
| OCTET_LENGTH('中国')   | OCTET_LENGTH('hello') |
+------------------------+-----------------------+
|                      6 |                     5 |
+------------------------+-----------------------+
1 row in set
```
