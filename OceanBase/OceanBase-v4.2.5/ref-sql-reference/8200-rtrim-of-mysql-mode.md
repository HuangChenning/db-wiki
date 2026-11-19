---
title: RTRIM
book: "SQL 参考"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001504802.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# RTRIM

## 声明

```sql
RTRIM(str)
```

## 说明

删除字符串 `str` 右侧的空格。

## 示例

```sql
obclient> SELECT RTRIM('    obclient    ') AS rtrim;
+--------------+
| rtrim        |
+--------------+
|     obclient |
+--------------+
1 row in set
```
