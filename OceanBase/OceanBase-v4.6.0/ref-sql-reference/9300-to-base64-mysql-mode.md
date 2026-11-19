---
title: TO_BASE64
book: "SQL 参考"
version: V4.6.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005688015.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# TO_BASE64

## 声明

```sql
TO_BASE64(str)
```

## 说明

将字符串参数转换为 base-64 编码形式。可以使用 `FROM_BASE64` 函数对 Base-64 编码的字符串进行解码，详细信息请参见 [FROM_BASE64()](../200.string-functions-of-mysql-mode/9400.from-base64-of-mysql-mode.md)。

## 示例

```sql
obclient> SELECT TO_BASE64('OB');
+-----------------+
| TO_BASE64('OB')
+-----------------+
| T0I=            |
+-----------------+
1 row in set
```
