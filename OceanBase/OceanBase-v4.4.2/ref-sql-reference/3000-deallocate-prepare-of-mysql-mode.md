---
title: DEALLOCATE PREPARE
book: "SQL 参考"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005286490.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# DEALLOCATE PREPARE

## 描述

该语句用于删除准备语句。

## 语法

```sql
{DEALLOCATE | DROP} PREPARE stmt_name
```

## 参数解释

|    参数     |    描述    |
|-----------|----------|
| stmt_name | 准备语句的名称。 |

## 示例

删除准备的语句。

```sql
obclient> PREPARE stmt1 FROM 'PURGE RECYCLEBIN';
Query OK, 0 rows affected

obclient> DROP PREPARE stmt1;
Query OK, 0 rows affected
```
