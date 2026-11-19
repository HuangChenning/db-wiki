---
title: RAWTONHEX
book: "SQL 参考"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000007053172.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# RAWTONHEX

## 描述

该函数将 `RAW` 值转换为对应的十六进制字符串。

## 语法

```sql
RAWTONHEX(raw)
```

## 参数解释

`raw` 指定要转换的 `RAW` 值。

## 返回类型

返回 `NVARCHAR2` 数据类型。

## 示例

将十六进制表示的 `RAW` 值转换为对应的十六进制字符串。

```sql
obclient> SELECT RAWTONHEX(HEXTORAW('4F6365616E42617365')) AS result FROM DUAL;
+--------------------+
| RESULT             |
+--------------------+
| 4F6365616E42617365 |
+--------------------+
1 row in set
```
