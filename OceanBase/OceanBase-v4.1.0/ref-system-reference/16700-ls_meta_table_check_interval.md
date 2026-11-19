---
title: ls_meta_table_check_interval
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699348.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# ls_meta_table_check_interval

ls_meta_table_check_interval 用于设置 DBA_OB_LS_LOCATIONS/CDB_OB_LS_LOCATIONS 视图的后台巡检线程的检查间隔。


|      **属性**      |  **描述**   |
|------------------|-----------|
| 参数类型             | 时间类型      |
| 默认值              | 1s        |
| 取值范围             | \[1ms, +∞) |
| 是否重启 OBServer 节点生效 | 否         |
