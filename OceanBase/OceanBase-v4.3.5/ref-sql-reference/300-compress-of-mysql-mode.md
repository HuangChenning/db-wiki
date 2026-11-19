---
title: COMPRESS
book: "SQL 参考"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002017660.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# COMPRESS

## 声明

```sql
COMPRESS(str)
```

## 说明

压缩字符串并将结果作为二进制字符串返回。可以使用 [UNCOMPRESS](../500.encryption-and-compression-functions-of-mysql-mode/1100.uncompress-of-mysql-mode.md) 函数对结果进行解压。

## 示例

```sql
obclient> SELECT COMPRESS('abc');
+-----------------+
| COMPRESS('abc') |
+-----------------+
|    x?KLJ M'  |
+-----------------+
1 row in set
```
