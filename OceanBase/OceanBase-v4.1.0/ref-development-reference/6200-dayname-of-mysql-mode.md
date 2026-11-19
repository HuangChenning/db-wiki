---
title: DAYNAME
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001700083.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# DAYNAME

## 声明

```sql
DAYNAME(date)
```

## 说明

返回日期所对应的工作日名称。

## 示例

```sql
obclient> SELECT DAYNAME('2022-09-08');
+-----------------------+
| DAYNAME('2022-09-08') |
+-----------------------+
| Thursday              |
+-----------------------+
1 row in set
```
