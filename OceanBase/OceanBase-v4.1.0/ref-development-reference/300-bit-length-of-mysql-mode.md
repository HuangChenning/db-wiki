---
title: BIT_LENGTH
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702873.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
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
