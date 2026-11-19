---
title: ob_log_level
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002186397.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# ob_log_level

ob_log_level 用于设置 Session 级的日志级别，如果不指定则使用系统中的日志级别。

| **属性** |        **描述**         |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 参数类型   | varchar               |
| 默认值    | disabled              |
| 取值范围   | <li> trace   <li> info   <li> warn   <li> error    |
| 生效范围   | <li> GLOBAL   <li> SESSION  |
