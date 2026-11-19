---
title: ob_enable_transmission_checksum
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002186390.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# ob_enable_transmission_checksum

ob_enable_transmission_checksum 用于设置 Proxy 和 Server 之间是否进行数据包校验和，设置后实时生效。

| **属性**  |                                                    **描述**                                                    |
|---------|--------------------------------------------------------------------------------------------------------------|
| 参数类型    | bool                      |
| 默认值     | 1                         |
| 取值范围    | <li> 0：不进行校验和   <li> 1：进行校验和    |
| 生效范围    | <li> GLOBAL   <li> SESSION      |
| 是否参与序列化 | 是                         |
