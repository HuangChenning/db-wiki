---
title: DAYNAME
book: "SQL 参考"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004481311.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# DAYNAME

## 声明

```sql
DAYNAME(date)
```

## 说明

返回日期所对应的工作日名称。

## 示例

```sql
obclient> SELECT DAYNAME('2022-09-08');
+-----------------------+
| DAYNAME('2022-09-08') |
+-----------------------+
| Thursday              |
+-----------------------+
1 row in set
```
