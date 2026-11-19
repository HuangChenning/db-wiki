---
title: multiblock_read_gap_size
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002180045.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# multiblock_read_gap_size

multiblock_read_gap_size 
=============================================

`multiblock_read_gap_size` 用于设置一次 IO 聚合读取块缓存的最大容量。

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>从 V4.0.0 版本开始弃用。</p>
</main>


|      **属性**      |   **描述**   |
|------------------|------------|
| 参数类型             | 容量单位       |
| 默认值              | 0K         |
| 取值范围             | \[0k, 2M\] |
| 是否重启 OBServer 节点生效 | 否          |
