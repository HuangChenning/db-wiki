---
title: MINUTE
book: "SQL 参考"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002018197.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# MINUTE

## 声明

```sql
MINUTE(time)
```

## 说明

返回时间 `time` 中的分钟数。

## 示例

```sql
obclient> SELECT MINUTE('18:20:17');
+--------------------+
| MINUTE('18:20:17') |
+--------------------+
|                 20 |
+--------------------+
1 row in set
```
