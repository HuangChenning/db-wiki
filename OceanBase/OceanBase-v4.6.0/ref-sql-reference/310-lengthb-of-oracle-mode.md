---
title: LENGTHB
book: "SQL 参考"
version: V4.6.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000007053246.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# LENGTHB

## 描述

该函数返回字符串的字节长度。

## 语法

``` sql
LENGTHB(char)
```

## 参数解释

`char` 指定要计算字节长度的字符串。

## 返回类型

返回 `NUMBER` 数据类型。

## 示例

字符串 `中OceanBase` 包含一个占 3 个字节的汉字和 9 个单字节字符，因此字节长度为 12。

``` sql
obclient> SELECT LENGTHB('中OceanBase') AS result FROM DUAL;
+--------+
| RESULT |
+--------+
|     12 |
+--------+
1 row in set
```
