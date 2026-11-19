---
title: merger_completion_percentage
book: "配置项和系统变量"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002015827.html"
tags:
  - oceanbase
  - distributed
  - ref-configuration-items-and-system-variables
---

# merger_completion_percentage

<main id="notice" type='explain'>
<h4>说明</h4>
<p>由于该配置项自引入后使用率较低，经过综合评估，该配置项从 V4.0.0 版本开始删除。</p>
</main>

## 功能描述

`merger_completion_percentage` 用于设置合并完成副本数的百分比阈值，达到该阈值则认为本轮合并完成调度。

## 属性说明

|      **属性**      |   **描述**   |
|------------------|------------|
| 参数类型             | Int         |
| 默认值              | 100        |
| 取值范围             | \[5, 100\] |
| 是否重启 OBServer 节点生效 | 否          |
