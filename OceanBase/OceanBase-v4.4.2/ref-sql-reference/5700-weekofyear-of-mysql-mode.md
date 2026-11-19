---
title: WEEKOFYEAR
book: "SQL 参考"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005288263.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# WEEKOFYEAR

## 声明

```sql
WEEKOFYEAR(date)
```

## 说明

返回日期或时间日期类型 `date` 所指定的周在一年中的位置。

## 示例

```sql
obclient> SELECT WEEKOFYEAR('2020-07-16');
+--------------------------+
| WEEKOFYEAR('2020-07-16') |
+--------------------------+
|                       29 |
+--------------------------+
1 row in set
```
