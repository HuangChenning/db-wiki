---
title: ob_query_timeout
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002186412.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# ob_query_timeout

`ob_query_timeout` 用于设置 SQL 最大执行时间，单位是微秒。

| **属性**  |                                                   **描述**                                                   |
|---------|------------------------------------------------------------------------------------------------------------|
| 参数类型    | int                     |
| 默认值     | 10000000                |
| 取值范围    | \[0, 3216672000000000\] |
| 生效范围    | <li> Global   <li> Session    |
| 是否参与序列化 | 是                       |
