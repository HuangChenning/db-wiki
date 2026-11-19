---
title: group_concat_max_len
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002183474.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# group_concat_max_len

group_concat_max_len 用于设置允许的 GROUP_CONCAT() 函数结果的最大长度，单位为字节。

| **属性**  |                                                   **描述**                                                   |
|---------|------------------------------------------------------------------------------------------------------------|
| 参数类型    | uint                    |
| 默认值     | 1024                    |
| 取值范围    | \[4, 18446744073709551615\]                                                                                |
| 生效范围    | <li> GLOBAL   <li> SESSION    |
| 是否参与序列化 | 是                       |
