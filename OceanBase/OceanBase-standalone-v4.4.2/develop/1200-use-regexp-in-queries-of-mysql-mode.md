---
title: "查询中使用正则表达式"
book: "应用开发"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077951.html"
tags:
  - oceanbase
  - standalone
  - develop
---

# 查询中使用正则表达式

#### 注意

OceanBase 中不支持在 `REGEXP` 函数中直接使用 `BINARY` 关键字。如果需要进行二进制比较，请使用 `COLLATE` 子句指定二进制排序规则的字符集。

#### 注意

复杂的正则表达式可能影响查询性能。建议在高并发场景下谨慎使用，并考虑使用数据库索引来优化查询性能。
