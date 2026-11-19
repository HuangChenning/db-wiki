---
title: PERIOD_DIFF
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001701604.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
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
