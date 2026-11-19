---
title: nls_timestamp_format
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002183534.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# nls_timestamp_format

`nls_timestamp_format` 用于控制 timestamp 或 timestamp ltz 类型转 str 的格式，以及 str 隐式转 timestamp 或 timestamp ltz 的格式。

| **属性**  |                                                   **描述**                                                   |
|---------|------------------------------------------------------------------------------------------------------------|
| 参数类型    | varchar                 |
| 默认值     | DD-MON-RR HH.MI.SSXFF AM|
| 取值范围    | N/A                     |
| 生效范围    | <li> Global   <li> Session    |
| 是否参与序列化 | 是                       |
