---
title: row_compaction_update_limit
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699355.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# row_compaction_update_limit

row_compaction_update_limit 用于设置触发内存中行内数据合并的修改次数。


|      **属性**      |   **描述**    |
|------------------|-------------|
| 参数类型             | 整型          |
| 默认值              | 6           |
| 取值范围             | \[1, 6400\] |
| 是否重启 OBServer 节点生效 | 否           |
