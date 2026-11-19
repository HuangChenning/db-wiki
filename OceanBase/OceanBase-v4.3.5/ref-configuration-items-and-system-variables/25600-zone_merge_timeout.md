---
title: zone_merge_timeout
book: "配置项和系统变量"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002015664.html"
tags:
  - oceanbase
  - distributed
  - ref-configuration-items-and-system-variables
---

# zone_merge_timeout

<main id="notice" type='explain'>
<h4>说明</h4>
<p>由于 V4.x 版本不再支持按 Zone 控制合并，该配置项从 V4.0.0 版本开始删除。</p>
</main>

## 功能描述

`zone_merge_timeout` 用于设置单个 zone 的合并超时时间。

## 属性说明

|      **属性**      |  **描述**   |
|------------------|-----------|
| 参数类型                      | Time      |
| 默认值              | 3h        |
| 取值范围             | \[1s, +∞) |
| 是否重启 OBServer 节点生效 | 否         |
