---
title: EMPTY_CLOB
book: "SQL 参考"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000007053085.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# EMPTY_CLOB

## 描述

该函数返回一个空的 `CLOB` 定位器。该定位器不为 `NULL`，LOB 长度为 0。

## 语法

```sql
EMPTY_CLOB()
```

## 返回类型

返回 `CLOB` 数据类型。

## 示例

返回一个空的 `CLOB` 定位器，并检查该定位器是否为 `NULL` 以及 LOB 长度。

```sql
obclient> SELECT CASE WHEN EMPTY_CLOB() IS NULL THEN 'NULL' ELSE 'NOT NULL' END AS clob_is_null,
          DBMS_LOB.GETLENGTH(EMPTY_CLOB()) AS clob_len
          FROM DUAL;
+--------------+----------+
| CLOB_IS_NULL | CLOB_LEN |
+--------------+----------+
| NOT NULL     |        0 |
+--------------+----------+
1 row in set
```
