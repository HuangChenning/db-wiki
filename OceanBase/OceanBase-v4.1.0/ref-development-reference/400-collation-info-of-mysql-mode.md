---
title: COLLATION
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000001967394.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# COLLATION

## 声明

```sql
COLLATION(str)
```

## 说明

返回字符串 `str` 的字符序。

您可以通过 `SHOW COLLATION` 语句查看 OceanBase 数据库支持的字符序。

## 示例

```sql
obclient> SELECT COLLATION("oceanbase");
+------------------------+
| COLLATION("oceanbase") |
+------------------------+
| utf8mb4_general_ci     |
+------------------------+
1 row in set 

obclient> SELECT COLLATION("oceanbase" COLLATE utf8mb4_bin);
+--------------------------------------------+
| COLLATION("oceanbase" COLLATE utf8mb4_bin) |
+--------------------------------------------+
| utf8mb4_bin                                |
+--------------------------------------------+
1 row in set 
```
