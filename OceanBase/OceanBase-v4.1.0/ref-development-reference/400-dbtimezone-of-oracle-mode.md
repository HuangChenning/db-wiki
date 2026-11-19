---
title: DBTIMEZONE
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699965.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# DBTIMEZONE

## 描述

该函数返回当前数据库实例的时区，OceanBase 数据库的时区恒为+00:00，且不支持修改。

## 语法

```sql
DBTIMEZONE
```

## 返回类型

返回 `VARCHAR2` 数据类型。

## 示例

返回当前数据库实例的时区。

```sql
obclient> SELECT DBTIMEZONE FROM DUAL;
+------------+
| DBTIMEZONE |
+------------+
| +00:00     |
+------------+
1 row in set
```
