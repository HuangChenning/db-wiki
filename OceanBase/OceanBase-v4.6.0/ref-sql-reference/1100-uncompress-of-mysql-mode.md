---
title: UNCOMPRESS
book: "SQL 参考"
version: V4.6.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005687256.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# UNCOMPRESS

## 声明

```sql
UNCOMPRESS(str)
```

## 说明

解压缩由 [COMPRESS()](../500.encryption-and-compression-functions-of-mysql-mode/300.compress-of-mysql-mode.md) 函数压缩的字符串。

## 示例

```sql
obclient [test]> SELECT UNCOMPRESS(COMPRESS('abc'));
+-----------------------------+
| UNCOMPRESS(COMPRESS('abc')) |
+-----------------------------+
| abc                         |
+-----------------------------+
1 row in set
```
