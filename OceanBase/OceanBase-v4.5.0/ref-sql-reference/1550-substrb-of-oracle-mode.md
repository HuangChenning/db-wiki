---
title: SUBSTRB
book: "SQL 参考"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000007053166.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# SUBSTRB

## 描述

该函数以字节为单位，从字符串中截取子字符串。

## 语法

```sql
SUBSTRB(char, position [, substring_length])
```

## 参数解释

| 参数 | 说明 |
|------|------|
| char | 指定要截取的字符串。 |
| position | 指定截取的起始字节位置。值为 `0` 时按 `1` 处理；值为负数时，从字符串末尾反向计算起始位置。 |
| substring_length | 可选。指定要截取的字节数。如果省略，则截取到字符串末尾。 |

## 返回类型

返回字符串类型。

## 示例

字符串 `中OceanBase` 中的汉字 `中` 占 3 个字节，以下示例从第 4 个字节开始截取 5 个字节。

```sql
obclient> SELECT SUBSTRB('中OceanBase', 4, 5) AS result FROM DUAL;
+--------+
| RESULT |
+--------+
| Ocean  |
+--------+
1 row in set
```
