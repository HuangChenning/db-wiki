---
title: PI
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001700065.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# PI

## 声明

```sql
PI()
```

## 说明

返回 `π` 的值（圆周率）。

## 示例

```sql
obclient> SELECT PI();
+----------+
| PI()     |
+----------+
| 3.141593 |
+----------+
1 row in set 

obclient> SELECT ROUND(2*PI(),2);
+----------------+
| ROUND(2*PI(),2)|
+----------------+
| 6.28           |
+----------------+
1 row in set
```
