---
title: server_data_copy_out_concurrency
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002174534.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# server_data_copy_out_concurrency

server_data_copy_out_concurrency 
=====================================================

`server_data_copy_out_concurrency` 用于设置单个节点迁出数据的最大并发数。

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>从 V4.0.0 版本开始弃用。</p>
</main>

|      **属性**      |   **描述**    |
|------------------|-------------|
| 参数类型             | 整型          |
| 默认值              | 2           |
| 取值范围             | \[1, 1000\] |
| 是否重启 OBServer 节点生效 | 否           |
