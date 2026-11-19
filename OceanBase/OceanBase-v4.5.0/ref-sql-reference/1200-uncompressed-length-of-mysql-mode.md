---
title: UNCOMPRESSED_LENGTH
book: "SQL 参考"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004480648.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# UNCOMPRESSED_LENGTH

## 声明

```sql
UNCOMPRESSED_LENGTH(str)
```

## 说明

返回压缩字符串在 [COMPRESS()](../500.encryption-and-compression-functions-of-mysql-mode/300.compress-of-mysql-mode.md) 函数压缩前的长度。

## 示例

```sql
obclient [test]> SELECT UNCOMPRESSED_LENGTH(COMPRESS('abc'));
+--------------------------------------+
| UNCOMPRESSED_LENGTH(COMPRESS('abc')) |
+--------------------------------------+
|                                    3 |
+--------------------------------------+
1 row in set
```
