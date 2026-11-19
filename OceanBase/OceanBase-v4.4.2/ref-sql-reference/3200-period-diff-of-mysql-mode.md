---
title: PERIOD_DIFF
book: "SQL 参考"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005288239.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# PERIOD_DIFF

## 声明

```javascript
PERIOD_DIFF(p1, p2)
```

## 说明

以月份为单位返回两个日期之间的间隔。日期只能包含年月信息，格式只能为 `YYYYMM` 或 `YYMM`。

## 示例

```javascript
obclient> SELECT PERIOD_DIFF(200802, 200703);
+----------------------------+
| PERIOD_DIFF(200802,200703) |
+----------------------------+
|                         11 |
+----------------------------+
1 row in set
```
