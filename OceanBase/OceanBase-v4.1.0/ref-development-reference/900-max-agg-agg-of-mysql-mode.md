---
title: MAX
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000001967393.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# MAX

## 声明

```sql
MAX([DISTINCT | ALL] expr)
```

## 说明

返回指定数据中的最大值。

`MAX()` 的取值可以是一个字符串参数，在这些情况下，它们返回最大字符串值。`DISTINCT` 关键字表示只计算不同值，缺省为 `ALL`。

## 示例

假设表 `a` 有三行数据：`id=1,num=10`、`id=2,num=20` 与 `id=3,num=30`，选取其中 `num` 的最大值。

```sql
obclient> SELECT MAX(num) FROM a;
+-----------------+
| MAX(num)        |
+-----------------+
|              30 |
+-----------------+
1 row in set 
```
