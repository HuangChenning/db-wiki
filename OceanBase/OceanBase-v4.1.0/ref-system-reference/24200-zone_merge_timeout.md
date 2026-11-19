---
title: zone_merge_timeout
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002180034.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# zone_merge_timeout

zone_merge_timeout 
=======================================

`zone_merge_timeout` 用于设置单个 zone 的合并超时时间。

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>从 V4.0.0 版本开始弃用。</p>
</main>

|      **属性**      |  **描述**   |
|------------------|-----------|
| 参数类型             | 时间类型      |
| 默认值              | 3h        |
| 取值范围             | \[1s, +∞) |
| 是否重启 OBServer 节点生效 | 否         |
