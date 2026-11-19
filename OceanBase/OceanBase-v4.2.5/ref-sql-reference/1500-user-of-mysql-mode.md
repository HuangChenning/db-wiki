---
title: USER
book: "SQL 参考"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001504294.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# USER

## 声明

```sql
USER()
```

## 说明

返回当前的用户名与主机名，返回值使用的字符集为 utf8mb4。

## 示例

```sql
obclient> SELECT USER();
+---------------------+
| USER()              |
+---------------------+
| root@xxx.xx.xxx.xxx |
+---------------------+
1 row in set
```
