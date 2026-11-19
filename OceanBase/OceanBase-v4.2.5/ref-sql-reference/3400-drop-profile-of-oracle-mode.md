---
title: DROP PROFILE
book: "SQL 参考"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001504106.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# DROP PROFILE

## 描述

该语句用于删除配置文件。

## 语法

```sql
DROP PROFILE "profile_name";
```

## 参数解释

|      参数      |       描述       |
|--------------|----------------|
| profile_name | 指定要删除的配置文件的名称。 |

## 示例

删除配置文件 `profile1`。

```sql
obclient> DROP PROFILE "profile1";
Query OK, 0 rows affected
```
