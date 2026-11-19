---
title: SHA1
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699910.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# SHA1

## 声明

```sql
SHA1(str)
```

## 说明

计算并返回给定字符串的 SHA-1 160 位校验和，该值以 40 个十六进制数字的字符串形式返回。等效于 `SHA()` 函数。

## 示例

```sql
obclient [test]> SELECT SHA1('OB');
+------------------------------------------+
| SHA1('OB')                               |
+------------------------------------------+
| 29a6de2fd8618f31afb281a608c57995b7eb105d |
+------------------------------------------+
1 row in set
```
