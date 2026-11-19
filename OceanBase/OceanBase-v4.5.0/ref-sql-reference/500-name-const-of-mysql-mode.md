---
title: NAME_CONST
book: "SQL 参考"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004480697.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# NAME_CONST

## 声明

```sql
NAME_CONST(name,value)
```

## 说明

该函数返回值定的值。参数 `value`应该是常量。

`NAME_CONST()` 使所生成结果集的列具有指定的名称。

## 示例

```sql
obclient> SELECT NAME_CONST('my_id', 101);
+-------+
| my_id |
+-------+
|   101 |
+-------+
1 row in set
```

您也可以通过设置简单的别名，获得与上述示例完全相同的结果，如下所示：

```sql
SELECT 101 AS my_id;
```
