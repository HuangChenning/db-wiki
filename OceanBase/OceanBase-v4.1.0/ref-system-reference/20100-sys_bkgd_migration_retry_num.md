---
title: sys_bkgd_migration_retry_num
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702100.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# sys_bkgd_migration_retry_num

sys_bkgd_migration_retry_num 用于设置副本迁移失败时最多重试次数。

|      **属性**      |   **描述**   |
|------------------|------------|
| 参数类型             | 整型         |
| 默认值              | 3          |
| 取值范围             | \[3, 100\] |
| 是否重启 OBServer 节点生效 | 否          |
