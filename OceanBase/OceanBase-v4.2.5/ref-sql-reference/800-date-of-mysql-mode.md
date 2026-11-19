---
title: DATE
book: "SQL 参考"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001504748.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# DATE

## 声明

```sql
DATE(expr)
```

## 说明

返回时间或时间日期表达式 `expr` 的日期。

## 示例

```sql
obclient> SELECT DATE('2021-07-14 19:12:03');
+-----------------------------+
| DATE('2021-07-14 19:12:03') |
+-----------------------------+
| 2021-07-14                  |
+-----------------------------+
1 row in set
```
