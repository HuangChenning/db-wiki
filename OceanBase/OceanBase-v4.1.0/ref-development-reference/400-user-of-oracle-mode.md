---
title: USER
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702829.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# USER

## 描述

该函数返回当前登录用户的名称。

## 语法

```sql
USER
```

## 返回类型

返回 `VARCHAR2` 数据类型。

## 示例

返回当前用户的名称。

```sql
obclient> SELECT USER FROM DUAL;
+------+
| USER |
+------+
| SYS  |
+------+
1 row in set
```
