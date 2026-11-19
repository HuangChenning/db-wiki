---
title: NOW
book: "SQL 参考"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002018209.html"
tags:
  - oceanbase
  - distributed
  - ref-sql-reference
---

# NOW

## 声明

```javascript
NOW([scale])
```

## 说明

返回当前日期时间，考虑时区设置。该函数为 `CURRENT_TIMESTAMP()` 的别名。

`scale` 表示微秒部分精度，有效值为 `0` 到 `6` 的整数，默认值为 `0`。

## 示例

```sql
obclient> SELECT NOW(6);
+----------------------------+
| NOW(6)                     |
+----------------------------+
| 2021-07-20 16:30:54.816317 |
+----------------------------+
1 row in set
```
