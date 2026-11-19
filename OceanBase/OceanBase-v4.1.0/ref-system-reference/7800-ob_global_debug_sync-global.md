---
title: ob_global_debug_sync
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002186393.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# ob_global_debug_sync

ob_global_debug_sync 用于 debug 时设置同步点，与 debug_sync 不同，设置此变量会影响所有 Session。只有 debug_sync_timeout 配置项的值不为 0 时，该设置才有效。

| **属性** |   **描述**   |
|--------|------------|
| 参数类型   | varchar    |
| 默认值    | 空字符串       |
| 取值范围   | 无          |
| 生效范围   | SESSION    |
| 是否可见   | 否，所有租户均不可见 |
