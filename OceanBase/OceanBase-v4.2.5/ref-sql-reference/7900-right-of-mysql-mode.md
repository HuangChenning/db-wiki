---
title: RIGHT
book: "SQL 参考"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001504789.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# RIGHT

## 声明

```sql
RIGHT(str,len)
```

## 说明

返回字符串 `str` 从右侧起的 `len` 个字符，如果 `str` 或 `len` 为 `NULL`，则返回 `NULL`。

该函数是多字节安全的。

## 示例

```sql
obclient> SELECT RIGHT('oceanbase',4);
+----------------------+
| RIGHT('oceanbase',4) |
+----------------------+
| base                 |
+----------------------+
1 row in set
```
