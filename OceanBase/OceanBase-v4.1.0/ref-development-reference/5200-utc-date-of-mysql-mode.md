---
title: UTC_DATE
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001701624.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# UTC_DATE

## 声明

```sql
UTC_DATE()
```

## 说明

将当前 UTC 日期以 `%Y-%m-%d` 格式返回。

## 示例

```sql
obclient> SELECT UTC_DATE(), UTC_DATE() + 0, UTC_DATE() + 6;
+------------+----------------+----------------+
| UTC_DATE() | UTC_DATE() + 0 | UTC_DATE() + 6 |
+------------+----------------+----------------+
| 2021-07-14 |       20210714 |       20210720 |
+------------+----------------+----------------+
1 row in set 
```
