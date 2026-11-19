---
title: DROP PROFILE
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001701420.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
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
