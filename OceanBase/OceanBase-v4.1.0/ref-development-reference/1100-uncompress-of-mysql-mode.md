---
title: UNCOMPRESS
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699906.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
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
