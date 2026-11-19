---
title: character_set_connection
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002183475.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# character_set_connection

character_set_connection 用于设置收到语句后应转换的字符集。

| **属性**  |                                                                       **描述**                                                                        |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| 参数类型    | string                                                           |
| 默认值     | utf8mb4                                                          |
| 取值范围    | <li> utf8mb4   <li> binary   <li> gbk    |
| 生效范围    | <li> GLOBAL   <li> SESSION                                             |
| 是否参与序列化 | 是                                                                |
| 是否可以为空  | 是                                                                |
