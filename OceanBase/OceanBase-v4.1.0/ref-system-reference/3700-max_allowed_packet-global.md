---
title: max_allowed_packet
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002183490.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# max_allowed_packet

`max_allowed_packet` 用于设置最大网络包大小，单位是 Byte。

| **属性**  |                                                       **描述**                                                       |
|---------|--------------------------------------------------------------------------------------------------------------------|
| 参数类型    | int                             |
| 默认值     | 4194304                         |
| 取值范围    | \[1024,1073741824\]             |
| 生效范围    | <li> Global   <li> Session            |
| 是否参与序列化 | 是                               |
| 是否可修改   | 该变量可通过 `SET GLOBAL` 语句修改 Global 生效方式下的取值，不可通过 `SET SESSION` 语句修改 Session 生效方式下的取值。<br>Session 值仅支持查看，且 Session 值只能与 Global 值相同。<br>使用时，客户端与 Server 端一般均需要调整。 |
