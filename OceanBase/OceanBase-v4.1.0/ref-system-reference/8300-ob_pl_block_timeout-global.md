---
title: ob_pl_block_timeout
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002186399.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# ob_pl_block_timeout

ob_pl_block_timeout 用于设置 PL 的最大超时时间，单位 us。

|   属性    |                                                     描述                                                     |
|---------|------------------------------------------------------------------------------------------------------------|
| 参数类型    | int                     |
| 默认值     | 3216672000000000        |
| 取值范围    | \[0, 9223372036854775807\]                                                                                 |
| 生效范围    | <li> GLOBAL   <li> SESSION    |
| 是否参与序列化 | 是                       |
