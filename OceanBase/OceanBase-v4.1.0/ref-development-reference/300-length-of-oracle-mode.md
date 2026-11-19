---
title: LENGTH
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001701520.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# LENGTH

## 描述

该函数返回字符串的长度。多字节字符（汉字、全角符等）按 1 个字符计算。

## 语法

```sql
LENGTH(char)
```

## 参数解释

`char` 属于 `CHAR`、`VARCHAR2`、`NCHAR`、`NVARCHAR2` 或 `CLOB` 数据类型的字符串。

## 返回类型

返回 `NUMBER` 数据类型。

## 示例

返回字符串 `OceanBase` 的长度。

```sql
obclient> SELECT LENGTH('OceanBase') "LENGTH" FROM DUAL;
+--------+
| LENGTH |
+--------+
|      9 |
+--------+
1 row in set
```
