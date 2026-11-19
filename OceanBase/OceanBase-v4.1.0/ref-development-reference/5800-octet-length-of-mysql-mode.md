---
title: OCTET_LENGTH
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702899.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
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
