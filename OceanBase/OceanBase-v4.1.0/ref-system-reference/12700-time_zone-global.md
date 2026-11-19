---
title: time_zone
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002186362.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# time_zone

time_zone 用于设置当前租户会话使用的时区，支持 `'+08:00'`的 offset 形式和 `Asia/Shanghai`的地域形式取值。

| **属性**  |                                                   **描述**                                                   |
|---------|------------------------------------------------------------------------------------------------------------|
| 参数类型    | varchar                 |
| 默认值     | +8:00                   |
| 取值范围    | -12:59 \~ +13:00        |
| 生效范围    | <li> GLOBAL   <li> SESSION    |
| 是否参与序列化 | 是                       |
