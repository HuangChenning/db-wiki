---
title: COS
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001700053.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# COS

## 声明

```sql
COS(X)
```

## 说明

返回给定弧度 `X` 的余弦值。

## 示例

```sql
obclient> SELECT COS(PI());
+-----------+
| COS(PI()) |
+-----------+
|        -1 |
+-----------+
1 row in set 
```
