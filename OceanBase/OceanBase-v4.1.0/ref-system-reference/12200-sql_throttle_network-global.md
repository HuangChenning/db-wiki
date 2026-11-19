---
title: sql_throttle_network
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002183524.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# sql_throttle_network

sql_throttle_network 用于指定请求排队时间，如果请求排队时间大于或等于该值，则不允许执行查询。

| **属性** |    **描述**     |
|--------|---------------|
| 参数类型   | numeric       |
| 默认值    | -1            |
| 取值范围   | 与系统负载相关，单位 us |
| 生效范围   | GLOBAL        |
