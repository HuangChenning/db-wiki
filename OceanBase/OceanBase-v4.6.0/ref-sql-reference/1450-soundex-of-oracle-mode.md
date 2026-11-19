---
title: SOUNDEX
book: "SQL 参考"
version: V4.6.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000007053242.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# SOUNDEX

## 描述

该函数返回字符串的语音表示，可用于比较发音相近但拼写不同的英文单词。

## 语法

``` sql
SOUNDEX(char)
```

## 参数解释

`char` 指定要转换的字符串。

## 返回类型

返回字符串类型。

## 示例

返回字符串 `OceanBase` 的语音表示。

``` sql
obclient> SELECT SOUNDEX('OceanBase') AS result FROM DUAL;
+--------+
| RESULT |
+--------+
| O251   |
+--------+
1 row in set
```
