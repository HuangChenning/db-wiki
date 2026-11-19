---
title: UPPER
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702825.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# UPPER

## 描述

该函数将字符串中英文字母全部转为大写。

## 语法

```sql
UPPER(char)
```

## 参数解释

`char` 是要转换的字符串，数据类型可以为 `CHAR`、`VARCHAR2`、`NCHAR`、`NVARCHAR2` 或 `CLOB`。

## 返回类型

返回与 `char` 相同的数据类型。

## 示例

将字符串 `OceanBase` 全部转换为大写。

```sql
obclient> SELECT UPPER('OceanBase') "UPPER" FROM DUAL;
+-----------+
| UPPER     |
+-----------+
| OCEANBASE |
+-----------+
1 row in set
```
