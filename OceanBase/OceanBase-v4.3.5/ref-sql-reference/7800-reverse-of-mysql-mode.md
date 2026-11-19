---
title: REVERSE
book: "SQL 参考"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002018285.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# REVERSE

## 声明

```sql
REVERSE(str)
```

## 说明

返回字符串 `str` 的倒序排列。

该函数是多字节安全的。

## 示例

```sql
obclient> SELECT REVERSE('oceanbase');
+----------------------+
| REVERSE('oceanbase') |
+----------------------+
| esabnaeco            |
+----------------------+
1 row in set

obclient> SELECT REVERSE(1000);
+---------------+
| REVERSE(1000) |
+---------------+
| 0001          |
+---------------+
1 row in set
```
