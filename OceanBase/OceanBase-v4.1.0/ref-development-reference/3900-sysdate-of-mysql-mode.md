---
title: SYSDATE
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001701611.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# SYSDATE

## 声明

```sql
SYSDATE(fsp)
```

## 说明

返回当前日期和时间，格式为 `%Y-%m-%d %H.%i.%s`。

`fsp` 表示秒精度，即返回值的小数位秒部分包含多少位数字。有效值为 0 到 6 的整数，默认值为 0。

## 示例

```sql
obclient> SELECT SYSDATE();
+---------------------+
| SYSDATE()           |
+---------------------+
| 2021-07-15 14:10:06 |
+---------------------+
1 row in set 
```
