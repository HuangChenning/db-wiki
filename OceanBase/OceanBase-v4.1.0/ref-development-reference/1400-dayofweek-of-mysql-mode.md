---
title: DAYOFWEEK
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702917.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# DAYOFWEEK

## 声明

```sql
DAYOFWEEK(date)
```

## 说明

返回日期或时间日期 `date` 在一周中的位置，从周日开始计算。

## 示例

```sql
obclient> SELECT DAYOFWEEK('2021-07-15');
+-------------------------+
| DAYOFWEEK('2021-07-15') |
+-------------------------+
|                       5 |
+-------------------------+
1 row in set 
```
