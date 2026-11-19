---
title: SEC_TO_TIME
book: "SQL 参考"
version: V4.6.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005687960.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# SEC_TO_TIME

## 声明

```sql
SEC_TO_TIME(seconds)
```

## 说明

返回 `seconds` 转换为的时间类型。结果的范围仅限于 `TIME` 数据类型的范围。

## 示例

```sql
obclient> SELECT SEC_TO_TIME(2378);
+-------------------+
| SEC_TO_TIME(2378) |
+-------------------+
| 00:39:38          |
+-------------------+
1 row in set

obclient> SELECT SEC_TO_TIME(2378) + 0;
+-----------------------+
| SEC_TO_TIME(2378) + 0 |
+-----------------------+
|                  3938 |
+-----------------------+
1 row in set
```
