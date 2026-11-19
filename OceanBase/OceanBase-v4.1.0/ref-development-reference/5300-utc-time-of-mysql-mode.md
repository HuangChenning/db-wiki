---
title: UTC_TIME
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001701625.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# UTC_TIME

## 声明

```sql
UTC_TIME([fsp])
```

## 说明

将当前 UTC 时间以 `%H:%i:%s` 格式返回。

`fsp` 参数用于指定分秒精度，有效值为 0 到 6 之间的整数。

## 示例

```sql
obclient> SELECT UTC_TIME(), UTC_TIME() + 0, UTC_TIME() + 6;
+------------+----------------+----------------+
| UTC_TIME() | UTC_TIME() + 0 | UTC_TIME() + 6 |
+------------+----------------+----------------+
| 13:07:35   |         130735 |         130741 |
+------------+----------------+----------------+
1 row in set 
```
