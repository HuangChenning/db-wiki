---
title: POSITION
book: "SQL 参考"
version: V4.6.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005687984.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# POSITION

## 声明

```sql
POSITION(substr IN str)
```

## 说明

回字符串 `str` 中子字符串 `substr` 的第一个出现位置。

## 示例

```sql
obclient> SELECT POSITION('bar' IN 'foobarbar');
+--------------------------------+
| POSITION('bar' IN 'foobarbar') |
+--------------------------------+
|                              4 |
+--------------------------------+
1 row in set
```
