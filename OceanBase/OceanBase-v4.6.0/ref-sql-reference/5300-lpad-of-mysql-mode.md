---
title: LPAD
book: "SQL 参考"
version: V4.6.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005688039.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# LPAD

## 声明

```sql
LPAD(str,len,padstr)
```

## 说明

使用字符串 `padstr` 从左侧填充字符串 `str`，直到长度为 `len` 时为止。

如果 `str` 长度大于 `len`，则返回 `str` 左边 `len` 个字符。如果 `str` 长度小于 `len`，且 `padstr` 和 `str` 连接后大于 `len`，则返回连接后的右边 `len` 个字符。

## 示例

```sql
obclient> SELECT LPAD('Base',9,'Ocean');
+------------------------+
| LPAD('Base',9,'Ocean') |
+------------------------+
| OceanBase              |
+------------------------+
1 row in set

obclient> SELECT LPAD('Base',1,'Ocean');
+------------------------+
| LPAD('Base',1,'Ocean') |
+------------------------+
| B                      |
+------------------------+
1 row in set
```
