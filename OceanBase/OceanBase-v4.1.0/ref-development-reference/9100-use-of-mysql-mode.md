---
title: USE
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702362.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# USE

## 描述

该语句用于切换使用的数据库。

## 语法

```sql
USE database_name
```

## 参数解释

|      参数       |    描述     |
|---------------|-----------|
| database_name | 使用的数据库名称。 |

## 示例

切换当前的数据库。

```sql
obclient> USE test
Database changed
```
