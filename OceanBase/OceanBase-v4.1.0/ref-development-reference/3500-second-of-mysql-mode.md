---
title: SECOND
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001701607.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
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
