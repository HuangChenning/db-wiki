---
title: SHRINK
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001701438.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
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
