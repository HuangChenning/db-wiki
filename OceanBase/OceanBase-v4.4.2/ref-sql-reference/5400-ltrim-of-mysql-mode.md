---
title: LTRIM
book: "SQL 参考"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005288319.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# LTRIM

## 声明

```sql
LTRIM(str)
```

## 说明

删除字符串左侧的空格。

## 示例

```sql
obclient> SELECT LTRIM('    obclient    ') AS ltrim;
+--------------+
| ltrim        |
+--------------+
| obclient     |
+--------------+
1 row in set
```
