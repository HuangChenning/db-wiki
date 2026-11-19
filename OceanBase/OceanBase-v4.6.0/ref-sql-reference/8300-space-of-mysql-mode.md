---
title: SPACE
book: "SQL 参考"
version: V4.6.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005687988.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# SPACE

## 声明

```sql
SPACE(N)
```

## 说明

返回包含 `N` 个空格的字符串。

## 示例

返回包含 5 个空格的字符串。

```sql
obclient> SELECT SPACE(5);
+----------+
| SPACE(5) |
+----------+
|          |
+----------+
1 row in set
```
