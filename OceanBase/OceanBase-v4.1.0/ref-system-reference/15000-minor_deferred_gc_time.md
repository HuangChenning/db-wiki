---
title: minor_deferred_gc_time
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002168961.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# minor_deferred_gc_time

`minor_deferred_gc_time` 用于设置合并之后 SSTable 延迟回收的时间间隔。

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>从 V4.0.0 版本开始弃用。</p>
</main>

|      **属性**      |   **描述**    |
|------------------|-------------|
| 参数类型             | 时间类型        |
| 默认值              | 0s          |
| 取值范围             | \[0s, 24h] |
| 是否重启 OBServer 节点生效 | 否           |
