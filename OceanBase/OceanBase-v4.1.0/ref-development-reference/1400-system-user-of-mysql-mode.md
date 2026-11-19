---
title: SYSTEM_USER
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702769.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# SYSTEM_USER

## 声明

```sql
SYSTEM_USER()
```

## 说明

返回当前的用户名与主机名，该函数是 `USER()` 的同义词。

## 示例

```sql
obclient> SELECT SYSTEM_USER();
+---------------------+
| SYSTEM_USER()       |
+---------------------+
| root@xxx.xx.xxx.xxx |
+---------------------+
1 row in set 
```
