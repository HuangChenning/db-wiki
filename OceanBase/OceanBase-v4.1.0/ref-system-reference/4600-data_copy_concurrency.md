---
title: data_copy_concurrency
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002174544.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# data_copy_concurrency

data_copy_concurrency 
==========================================

`data_copy_concurrency` 用于设置系统中并发执行的数据迁移复制任务的最大并发数。

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>从 V4.0.0 版本开始弃用。</p>
</main>

| **属性** |  **描述**  |
|--------|----------|
| 参数类型   | 整型       |
| 默认值    | 20       |
| 取值范围   | \[1, +∞) |
| 是否需要重启 | 否        |
