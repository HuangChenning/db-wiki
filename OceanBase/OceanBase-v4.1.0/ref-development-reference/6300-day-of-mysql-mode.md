---
title: DAY
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001700084.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# DAY

## 声明

```sql
DAY(date)
```

## 说明

返回 `date` 中月份的日期，范围为 1 到 31。`DAY()` 是 `DAYOFMONTH()` 的同义词。

## 示例

```sql
obclient> SELECT DAY('2008-12-31');
+--------------------------+
| DAY('2008-12-31') |
+--------------------------+
|                       31 |
+--------------------------+
```
