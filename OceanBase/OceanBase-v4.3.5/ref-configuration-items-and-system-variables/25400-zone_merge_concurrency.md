---
title: zone_merge_concurrency
book: "配置项和系统变量"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002015706.html"
tags:
  - oceanbase
  - distributed
  - ref-configuration-items-and-system-variables
---

# zone_merge_concurrency

<main id="notice" type='explain'>
<h4>说明</h4>
<p>由于 V4.x 版本不再支持按 Zone 控制合并，该配置项从 V4.0.0 版本开始删除。</p>
</main>

## 功能描述

`zone_merge_concurrency` 用于设置在合并时，支持多少个 Zone 并发。当值为 0 时，由系统根据部署情况自动选择最佳并发度。

## 属性说明

|      **属性**      |  **描述**  |
|------------------|----------|
| 参数类型             | Int      |
| 默认值              | 0        |
| 取值范围             | \[0, +∞) |
| 是否重启 OBServer 节点生效 | 否        |
