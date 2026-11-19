---
title: TAN
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001700074.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# TAN

## 声明

```sql
TAN(X)
```

## 说明

返回给定弧度 X 的正切值。

## 示例

```sql
obclient> SELECT TAN(PI());
+-------------------------+
| TAN(PI())               |
+-------------------------+
| -1.2246467991473532e-16 |
+-------------------------+
1 row in set 
```
