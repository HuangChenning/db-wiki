---
title: TO_BASE64
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001701589.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# TO_BASE64

## 声明

```sql
TO_BASE64(str)
```

## 说明

将字符串参数转换为 base-64 编码形式。可以使用 [FROM_BASE64()](../200.string-functions-of-mysql-mode/9400.from-base64-of-mysql-mode.md) 函数对 Base-64 编码的字符串进行解码。

## 示例

```sql
obclient [test]> SELECT TO_BASE64('OB');
+-----------------+
| TO_BASE64('OB') |
+-----------------+
| T0I=            |
+-----------------+
1 row in set
```
