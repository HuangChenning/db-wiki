---
title: SESSIONTIMEZONE
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699975.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# SESSIONTIMEZONE

## 描述

该函数返回当前会话时区。

## 语法

```sql
SESSIONTIMEZONE
```

## 返回类型

返回 `VARCHAR2` 数据类型。

## 示例

返回数据库时区和当前会话时区。

```sql
obclient> SELECT DBTIMEZONE,SESSIONTIMEZONE FROM DUAL;
+------------+-----------------+
| DBTIMEZONE | SESSIONTIMEZONE |
+------------+-----------------+
| +00:00     | +08:00          |
+------------+-----------------+
1 row in set
```
