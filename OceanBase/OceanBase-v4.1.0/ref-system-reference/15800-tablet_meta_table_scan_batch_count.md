---
title: tablet_meta_table_scan_batch_count
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699340.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# tablet_meta_table_scan_batch_count

tablet_meta_table_scan_batch_count 用于设置 Tablet meta table 迭代器使用过程中在内存里缓存的 Tablet 数量。


|      **属性**      |    **描述**    |
|------------------|--------------|
| 参数类型             | 整型           |
| 默认值              | 999          |
| 取值范围             | \[1, 65536\] |
| 是否重启 OBServer 节点生效 | 否            |
