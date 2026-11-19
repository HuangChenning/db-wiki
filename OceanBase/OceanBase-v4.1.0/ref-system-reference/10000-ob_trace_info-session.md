---
title: ob_trace_info
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002186429.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# ob_trace_info

ob_trace_info 用于透传 trace 信息，该信息最终可透持久化到 REDO 日志中。

| **属性** |      **描述**       |
|--------|-------------------|
| 参数类型   | varchar           |
| 默认值    | 空字符串              |
| 取值范围   | 字符串长度为\[0, 4096\] |
| 生效范围   | SESSION           |
