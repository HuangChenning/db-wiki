---
title: UPPER
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001701587.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
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
