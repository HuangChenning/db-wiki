---
title: MD5
book: "SQL 参考"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004480641.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# MD5

## 声明

```javascript
MD5(str)
```

## 说明

返回字符串的 MD5 128 位校验和。

返回值为 32 位十六进制数字组成的字符串，如果 `str` 为 `NULL` 则返回 `NULL`。

## 示例

```javascript
obclient> SELECT MD5(1);
+----------------------------------+
| MD5(1)                           |
+----------------------------------+
| c4ca4238a0b923820dcc509a6f75849b |
+----------------------------------+
1 row in set
```
