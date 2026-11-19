---
title: SESSIONTIMEZONE
book: "SQL 参考"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004481606.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
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
