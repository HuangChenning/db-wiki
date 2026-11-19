---
title: px_task_size
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699344.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# px_task_size

px_task_size 
=================================

px_task_size 用于设置 SQL 并行查询引擎每个任务处理的数据量大小。


|      **属性**      |  **描述**   |
|------------------|-----------|
| 参数类型             | 容量单位      |
| 默认值              | 2M        |
| 取值范围             | \[2M, +∞) |
| 是否重启 OBServer 节点生效 | 否         |
