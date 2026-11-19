---
title: UPPER
book: "SQL 参考"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005288287.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# UPPER

## 声明

```sql
UPPER(str)
```

## 说明

将字符串 `str` 中的小写字母转化为大写字母。

## 示例

```sql
obclient> obclient> SELECT UPPER('obclient您好！');
+----------------------------+
| UPPER('obclient您好！')    |
+----------------------------+
| OBCLIENT您好！             |
+----------------------------+
1 row in set
```
