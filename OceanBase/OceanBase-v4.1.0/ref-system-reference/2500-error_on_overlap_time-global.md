---
title: error_on_overlap_time
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002186432.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# error_on_overlap_time

error_on_overlap_time 是动态参数，用于设置夏令时重叠区时间发生歧义时是否作报错处理。

| **属性**  |                                                      **描述**                                                       |
|---------|-------------------------------------------------------------------------------------------------------------------|
| 参数类型    | bool                           |
| 默认值     | OFF                            |
| 取值范围    | <li> ON：进行报错处理   <li> OFF：不进行报错处理    |
| 生效范围    | <li> GLOBAL   <li> SESSION           |
| 是否参与序列化 | 是                              |
