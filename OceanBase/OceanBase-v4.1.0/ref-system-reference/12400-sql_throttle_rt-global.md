---
title: sql_throttle_rt
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002183528.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# sql_throttle_rt

sql_throttle_rt 用于指定 RT 值，单位为微秒。如果查询的 RT 值不小于该值，则不允许执行该查询。

| **属性** |     **描述**      |
|--------|-----------------|
| 参数类型   | numeric         |
| 默认值    | -1              |
| 取值范围   | 无取值范围，与实际业务负载相关 |
| 生效范围   | GLOBAL          |
