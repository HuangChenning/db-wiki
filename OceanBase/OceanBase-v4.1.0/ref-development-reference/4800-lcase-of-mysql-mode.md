---
title: LCASE
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702889.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# LCASE

## 声明

```sql
LCASE(str)
```

## 说明

将字符串中的大写字母转化为小写字母。

该函数是 `LOWER()` 的同义词。

## 示例

```sql
obclient> SELECT LCASE('OBCLIENT您好！');
+----------------------------+
| LCASE('OBCLIENT您好！')    |
+----------------------------+
| obclient您好！             |
+----------------------------+
1 row in set 
```
