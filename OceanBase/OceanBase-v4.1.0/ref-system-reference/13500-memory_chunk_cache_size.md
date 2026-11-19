---
title: memory_chunk_cache_size
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001700949.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# memory_chunk_cache_size

memory_chunk_cache_size 用于设置内存分配器缓存的内存块容量。


|      **属性**      |  **描述**   |
|------------------|-----------|
| 参数类型             | 容量单位      |
| 默认值              | 0M        |
| 取值范围             | \[0M, +∞) |
| 是否重启 OBServer 节点生效 | 否         |



当 memory_chunk_cache_size 配置项的值为 0 时，表示系统自适应。
