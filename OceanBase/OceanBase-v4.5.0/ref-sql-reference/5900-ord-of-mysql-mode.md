---
title: ORD
book: "SQL 参考"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004481372.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# ORD

## 声明

```sql
ORD(str)
```

## 说明

返回字符串最左侧字符的字符码。单字节编码如果最左侧字符是多字节编码字符，返回值计算规则如下：

```sql
(1st byte code)
+ (2nd byte code * 256)
+ (3rd byte code * 256^2) ...
```

如果最左边的字符不是多字节字符，则 `ORD()` 返回与 `ASCII()` 函数相同的值。

## 示例

```sql
obclient> SELECT ORD('中国');
+---------------+
| ORD('中国') |
+---------------+
|      14989485 |
+---------------+
1 row in set
```
