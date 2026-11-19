---
title: ASCII
book: "SQL 参考"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004481563.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# ASCII

## 描述

该函数返回字符表达式最左端字符的 ASCII 码值。

## 语法

```sql
ASCII(char)
```

## 参数解释

|  参数  |                        说明                         |
|------|---------------------------------------------------|
| char | `CHAR`、`VARCHAR2`、`NCHAR` 或 `NVARCHAR2` 数据类型的表达式。 |

## 返回类型

返回 `NUMBER` 数据类型。

## 示例

使用 `ASCII` 函数返回 **A** 、 **a** 和空格的 ASCII 码值。

```sql
obclient> SELECT ASCII('A') A, ASCII('a') a, ASCII(' ') space FROM DUAL;
+------+------+-------+
| A    | A    | SPACE |
+------+------+-------+
|   65 |   97 |    32 |
+------+------+-------+
1 row in set
```

使用 `ASCII` 函数返回 **A** 、 **a** 、 **中** 和空格的 ASCII 码值。

```sql
obclient> SELECT ASCII('A') A, ASCII('a') a, ASCII(' ') space,ASCII('中') hz FROM DUAL;
+------+------+-------+----------+
| A    | A    | SPACE | HZ       |
+------+------+-------+----------+
|   65 |   97 |    32 | 14989485 |
+------+------+-------+----------+
1 row in set
```
