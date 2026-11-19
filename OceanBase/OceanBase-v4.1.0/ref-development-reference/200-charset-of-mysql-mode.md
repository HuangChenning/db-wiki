---
title: CHARSET
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702757.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# CHARSET

## 声明

```sql
CHARSET(str)
```

## 说明

返回字符串 `str` 使用的字符集。

## 示例

```sql
obclient> SELECT CHARSET("oceanbaase");
+-----------------------+
| CHARSET("oceanbaase") |
+-----------------------+
| utf8mb4               |
+-----------------------+
1 row in set 

obclient> SELECT CHARSET(CONVERT("oceanbase" USING binary));
+--------------------------------------------+
| CHARSET(CONVERT("oceanbase" USING binary)) |
+--------------------------------------------+
| binary                                     |
+--------------------------------------------+
1 row in set 
```
