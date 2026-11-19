---
title: SECOND
book: "SQL 参考"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001504729.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# SECOND

## 声明

```sql
SECOND(time)
```

## 说明

返回时间 `time` 中的秒数。

## 示例

```sql
obclient> SELECT SECOND('18:20:17');
+--------------------+
| SECOND('18:20:17') |
+--------------------+
|                 17 |
+--------------------+
1 row in set
```
