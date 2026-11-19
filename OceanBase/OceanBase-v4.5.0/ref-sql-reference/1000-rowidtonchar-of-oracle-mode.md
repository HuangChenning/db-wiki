---
title: ROWIDTONCHAR
book: "SQL 参考"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004481534.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# ROWIDTONCHAR

## 描述

该函数将 `rowid` 值转换为 `NVARCHAR2` 数据类型的值。

## 语法

```sql
ROWIDTONCHAR(rowid)
```

## 参数解释

参数 `rowid` 是一个 `ROWID` 格式的值。

## 返回类型

返回 `NVARCHAR2` 数据类型。

## 示例

将表 `tbl1` 中 `ROWID` 值转换为 `NVARCHAR2` 类型的值并返回对应字节长度。

```sql
obclient> SELECT LENGTHB(ROWIDTONCHAR(ROWID)),LENGTHB(ROWID),ROWIDTONCHAR(ROWID) FROM tbl1;
+------------------------------+----------------+---------------------+
| LENGTHB(ROWIDTONCHAR(ROWID)) | LENGTHB(ROWID) | ROWIDTONCHAR(ROWID) |
+------------------------------+----------------+---------------------+
|                           34 |             17 | *AAIKAQAAAAAAAAA=   |
|                           34 |             17 | *AAIKAgAAAAAAAAA=   |
|                           34 |             17 | *AAIKAwAAAAAAAAA=   |
+------------------------------+----------------+---------------------+
3 rows in set
```
