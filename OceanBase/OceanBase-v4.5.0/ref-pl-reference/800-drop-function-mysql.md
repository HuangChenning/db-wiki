---
title: DROP FUNCTION
book: "PL 参考"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004478388.html"
tags:
  - oceanbase
  - distributed
  - ref-pl-reference
---

# DROP FUNCTION

`DROP FUNCTION` 语句用于删除存储函数。

## 语法

```sql
DROP FUNCTION [IF EXISTS] sp_name
```

## 参数解释

| **参数名称** | **说明** |
|--------------|----------|
| IF EXISTS | 可选，如果函数不存在，则不报错，只生成告警。 |
| sp_name | 要删除的存储函数名称。可以使用 `database_name.sp_name` 指定数据库。 |

要删除存储的例程，用户必须对其具有 `ALTER ROUTINE` 权限。

如果存储函数不存在，使用 `IF EXISTS` 子句可以防止发生错误，并生成一个告警，可以使用 `SHOW WARNINGS` 查看该告警。

## 示例

删除存储函数。

```sql
obclient> DROP FUNCTION IF EXISTS my_func;
```

删除指定数据库中的存储函数：

```sql
obclient> DROP FUNCTION IF EXISTS test_db.calculate_sum;
```
