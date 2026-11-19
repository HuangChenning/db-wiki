---
title: auto_increment_increment
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002183496.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# auto_increment_increment

auto_increment_increment 用于设置自增步长，仅用于 MySQL 客户端登录。

| **属性**  |                                                   **描述**                                                   |
|---------|------------------------------------------------------------------------------------------------------------|
| 参数类型    | uint                    |
| 默认值     | 1                       |
| 取值范围    | \[1, 65535\]            |
| 生效范围    | <li> GLOBAL   <li> SESSION    |
| 是否参与序列化 | 是                       |
