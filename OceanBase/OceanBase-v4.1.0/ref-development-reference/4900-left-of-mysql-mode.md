---
title: LEFT
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702890.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# LEFT

## 声明

```sql
LEFT(str,len)
```

## 说明

返回字符串 `str` 从左侧起的 `len` 个字符，如果 `str` 或 `len` 为 `NULL`，则返回 `NULL`。

该函数是多字节安全的。

## 示例

```sql
obclient> SELECT LEFT('oceanbase', 5);
+----------------------+
| LEFT('oceanbase', 5) |
+----------------------+
| ocean                |
+----------------------+
1 row in set 
```
