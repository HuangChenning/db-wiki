---
title: SHRINK
book: "SQL 参考"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001504070.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# SHRINK

## 描述

该语句会将表的数据重写。

## 语法

```sql
ALTER TABLE table_name SHRINK SPACE;
```

## 参数解释

|     参数     | 描述  |
|------------|-----|
| table_name | 表名。 |

## 示例

将表 `tbl1` 的数据重写。

```sql
obclient> ALTER TABLE tbl1 SHRINK SPACE;
Query OK, 0 rows affected
```
