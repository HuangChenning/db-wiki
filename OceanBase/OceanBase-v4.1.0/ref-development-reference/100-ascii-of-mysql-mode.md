---
title: ASCII
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702871.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# ASCII

## 声明

```sql
ASCII(str)
```

## 说明

返回字符串 `str` 最左侧字符的 ASCII 码。

如果 `str` 为空字符串，则该函数返回 `0`。如果 `str` 为 `NULL`，则该函数返回 `NULL`。

## 示例

```sql
obclient> SELECT ASCII('');
+-----------+
| ASCII('') |
+-----------+
|         0 |
+-----------+
1 row in set 

obclient> SELECT ASCII('oceanbase');
+--------------------+
| ASCII('oceanbase') |
+--------------------+
|                111 |
+--------------------+
1 row in set 

obclient> SELECT ASCII('Oceanbase');
+--------------------+
| ASCII('Oceanbase') |
+--------------------+
|                 79 |
+--------------------+
1 row in set 
```
