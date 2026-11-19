---
title: net_read_timeout
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002183501.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# net_read_timeout

`net_read_timeout` 用于中断读数据之前等待连接的其它数据的秒数。

| **属性** |                                                   **描述**                                                   |
|--------|------------------------------------------------------------------------------------------------------------|
| 参数类型   | int                     |
| 默认值    | 30                      |
| 取值范围   | \[1, 31536000\]         |
| 生效范围   | <li> Global   <li> Session    |

当服务器从客户端读数据时，`net_read_timeout` 指控制何时中断的超时值。
