---
title: minor_deferred_gc_time
book: "配置项和系统变量"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004479018.html"
tags:
  - oceanbase
  - distributed
  - ref-configuration-items-and-system-variables
---

# minor_deferred_gc_time

<main id="notice" type='explain'>
<h4>说明</h4>
<p>由于该配置项从 V2.2.3x 版本开始已不再建议用户使用，该配置项从 V4.0.0 版本开始删除。</p>
</main>

## 功能描述

`minor_deferred_gc_time` 用于设置合并之后 SSTable 延迟回收的时间间隔。

## 属性说明

|      **属性**      |   **描述**    |
|------------------|-------------|
| 参数类型             | Time       |
| 默认值              | 0s          |
| 取值范围             | \[0s, 24h] |
| 是否重启 OBServer 节点生效 | 否           |
