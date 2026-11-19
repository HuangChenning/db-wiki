---
title: ROWIDTOCHAR
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001701546.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# ROWIDTOCHAR

## 描述

该函数将 `rowid` 值转换为 `VARCHAR2` 数据类型的值。

## 语法

```sql
ROWIDTOCHAR(rowid)
```

## 参数解释

参数 `rowid` 是一个 `ROWID` 格式的值。

## 返回类型

返回 `VARCHAR2` 数据类型。

## 示例

查询表 `tbl1` 列 `ROWID` 中包含 `AAIKA` 的数据。

```sql
obclient> SELECT LENGTHB(ROWIDTOCHAR(ROWID)),ROWIDTOCHAR(ROWID)
          FROM tbl1
          WHERE ROWIDTOCHAR(ROWID) LIKE '%AAIKA%';
+-----------------------------+--------------------+
| LENGTHB(ROWIDTOCHAR(ROWID)) | ROWIDTOCHAR(ROWID) |
+-----------------------------+--------------------+
|                          17 | *AAIKAQAAAAAAAAA=  |
|                          17 | *AAIKAgAAAAAAAAA=  |
|                          17 | *AAIKAwAAAAAAAAA=  |
+-----------------------------+--------------------+
3 rows in set
```
