---
title: LENGTHC
book: "SQL 参考"
version: V4.6.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000007053247.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# LENGTHC

## 描述

该函数以 Unicode 完整字符为单位返回字符串长度。

## 语法

``` sql
LENGTHC(char)
```

## 参数解释

`char` 指定要计算长度的字符串。

## 返回类型

返回 `NUMBER` 数据类型。

## 示例

字符串 `中OceanBase` 包含 10 个 Unicode 完整字符。

``` sql
obclient> SELECT LENGTHC('中OceanBase') AS result FROM DUAL;
+--------+
| RESULT |
+--------+
|     10 |
+--------+
1 row in set
```
