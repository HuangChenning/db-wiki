---
title: sql_throttle_current_priority
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002183522.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# sql_throttle_current_priority

sql_throttle_current_priority 用于设置限流优先级，只有 sql_throttle_current_priority 小于 sql_throttle_priority 的那些 Session 上的请求才会被限流。

| **属性** |                                                   **描述**                                                   |
|--------|------------------------------------------------------------------------------------------------------------|
| 参数类型   | int                     |
| 默认值    | 100                     |
| 取值范围   | 无取值范围，推荐值100            |
| 生效范围   | <li> GLOBAL   <li> SESSION    |
