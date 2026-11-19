---
title: restore_concurrency
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002180051.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# restore_concurrency

restore_concurrency 
========================================

`restore_concurrency` 用于设置从备份恢复租户数据时的最大并发度。

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>从 V4.0.0 版本开始弃用。</p>
</main>


|      **属性**      |   **描述**   |
|------------------|------------|
| 参数类型             | 整型         |
| 默认值              | 0          |
| 取值范围             | \[0, 512\] |
| 是否重启 OBServer 节点生效 | 否          |
