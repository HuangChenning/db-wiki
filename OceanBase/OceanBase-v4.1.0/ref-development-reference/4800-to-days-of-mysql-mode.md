---
title: TO_DAYS
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001701620.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# TO_DAYS

## 声明

```javascript
TO_DAYS(date)
```

## 说明

返回指定 `date` 值对应的天数。天数指距离 `0000-01-01` 的天数。

## 示例

```javascript
obclient> SELECT TO_DAYS('2015-11-04'), TO_DAYS('20151104');
+-----------------------+---------------------+
| TO_DAYS('2015-11-04') | TO_DAYS('20151104') |
+-----------------------+---------------------+
|                736271 |              736271 |
+-----------------------+---------------------+
1 row in set 
```
