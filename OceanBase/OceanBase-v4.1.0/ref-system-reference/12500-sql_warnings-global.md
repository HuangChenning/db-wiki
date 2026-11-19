---
title: sql_warnings
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002183530.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# sql_warnings

sql_warnings 用于在出现告警时控制单行 INSERT 语句是否生成信息字符串。

| **属性** |                                                        **描述**                                                         |
|--------|-----------------------------------------------------------------------------------------------------------------------|
| 参数类型   | bool                               |
| 默认值    | OFF                                |
| 取值范围   | <li> ON：生成一个信息字符串   <li> OFF：不生成信息字符串    |
| 生效范围   | <li> GLOBAL   <li> SESSION               |
