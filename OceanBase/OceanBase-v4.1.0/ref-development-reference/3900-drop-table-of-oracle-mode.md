---
title: DROP TABLE
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001701424.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# DROP TABLE

## 描述

该语句用于删除 OceanBase 数据库中的表。

## 语法

```sql
DROP TABLE table_name [CASCADE CONSTRAINTS] [PURGE];
```

## 参数解释

|         参数          |            描述             |
|---------------------|---------------------------|
| table_name          | 指定要删除的表名。                 |
| CASCADE CONSTRAINTS | 级联删除跟 `table_name` 关联的约束。 |
| PURGE               | 彻底删除表 (不进回收站)。            |

## 示例

删除表 `tbl1`。

```sql
obclient> DROP TABLE tbl1;
Query OK, 0 rows affected
```
