---
title: FROM_BASE64
book: "SQL 参考"
version: V4.6.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005688037.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# FROM_BASE64

## 声明

```sql
FROM_BASE64(str)
```

## 说明

解码一个 base-64 编码的字符串，并以二进制字符串的形式返回。通常用来对 `TO_BASE64()` 编码的字符串进行解码，详细信息请参见 [TO_BASE64()](../200.string-functions-of-mysql-mode/9300.to-base64-mysql-mode.md)。

## 示例

```sql
obclient> SELECT FROM_BASE64('T0I=');
+---------------------+
| FROM_BASE64('T0I=') |
+---------------------+
| OB                  |
+---------------------+
1 row in set
```
