---
title: TIME_FORMAT
book: "应用开发参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001701613.html"
tags:
  - oceanbase
  - distributed
  - ref-development-reference
---

# TIME_FORMAT

## 声明

```sql
TIME_FORMAT(time,format)
```

## 说明

用法与 `DATE_FORMAT` 函数类似，但 `format` 只支持小时、分钟、秒和微秒的格式符。

如果时间值 `time` 包含大于 23 的小时部分，`%H` 和 `%k` 小时格式说明符生成大于 0..23 的值，其他小时格式说明符生成小时值（模 12）。

## 示例

```sql
obclient> SELECT TIME_FORMAT('100:00:00', '%H %k %h %I %l');
+--------------------------------------------+
| TIME_FORMAT('100:00:00', '%H %k %h %I %l') |
+--------------------------------------------+
| 100 100 04 04 4                            |
+--------------------------------------------+
1 row in set 
```
