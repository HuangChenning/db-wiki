---
title: merger_completion_percentage
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002168957.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# merger_completion_percentage

merger_completion_percentage 
=================================================

`merger_completion_percentage` 用于设置合并完成副本数的百分比阈值，达到该阈值则认为本轮合并完成调度。

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>从 V4.0.0 版本开始弃用。</p>
</main>

|      **属性**      |   **描述**   |
|------------------|------------|
| 参数类型             | 整型         |
| 默认值              | 100        |
| 取值范围             | \[5, 100\] |
| 是否重启 OBServer 节点生效 | 否          |
