---
title: builtin_db_data_verify_cycle
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702083.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# builtin_db_data_verify_cycle

builtin_db_data_verify_cycle 用于设置数据坏块自检周期，单位为天。当值为 0 时表示不检查。


|      **属性**      |   **描述**   |
|------------------|------------|
| 参数类型             | 整型         |
| 默认值              | 20         |
| 取值范围             | \[0, 360\] |
| 是否重启 OBServer 节点生效 | 否          |
