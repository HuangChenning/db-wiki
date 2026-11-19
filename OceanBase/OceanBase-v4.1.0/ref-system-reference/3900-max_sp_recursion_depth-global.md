---
title: max_sp_recursion_depth
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002183494.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# max_sp_recursion_depth

max_sp_recursion_depth 用于设置可以递归调用任一指定存储过程的最大层次。默认值为 0 ，表示当前存储过程不可递归调用。

| **属性**  |                                                   **描述**                                                   |
|---------|------------------------------------------------------------------------------------------------------------|
| 参数类型    | int                     |
| 默认值     | 0                       |
| 取值范围    | \[0, 255\]              |
| 生效范围    | <li> GLOBAL   <li> SESSION    |
| 是否参与序列化 | 是                       |
