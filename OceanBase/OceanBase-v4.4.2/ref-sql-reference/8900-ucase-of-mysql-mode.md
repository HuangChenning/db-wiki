---
title: UCASE
book: "SQL 参考"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005288286.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# UCASE

## 声明

```sql
UCASE(str)
```

## 说明

将字符串 `str` 中的小写字母转化为大写字母。该函数是 `UPPER()` 函数的同义词。

## 示例

```sql
obclient> SELECT UCASE('obclient您好！');
+----------------------------+
| UCASE('obclient您好！')    |
+----------------------------+
| OBCLIENT您好！             |
+----------------------------+
1 row in set
```
