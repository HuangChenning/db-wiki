---
title: DAYOFYEAR
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702918.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# DAYOFYEAR

## 声明

```sql
DAYOFYEAR(date)
```

## 说明

返回日期或时间日期 `date` 在一年中的位置。

## 示例

```sql
obclient> SELECT DAYOFYEAR('2021-07-15');
+-------------------------+
| DAYOFYEAR('2021-07-15') |
+-------------------------+
|                     196 |
+-------------------------+
1 row in set 
```
