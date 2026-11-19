---
title: POSITION
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702901.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
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
