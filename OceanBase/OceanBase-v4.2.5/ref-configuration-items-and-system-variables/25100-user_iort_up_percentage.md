---
title: user_iort_up_percentage
book: "配置项和系统变量"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001502149.html"
tags:
  - oceanbase
  - distributed
  - ref-configuration-items-and-system-variables
---

# user_iort_up_percentage

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>由于调整了 IO 调度的算法，对应功能不再使用，该配置项从 V4.0.0 版本开始删除。</p>
</main>

## 功能描述

`user_iort_up_percentage` 用于设置用户磁盘 IO 时延阈值，即用户磁盘 IO 时延超过该阈值后，系统后台 IO 任务将被限流。

## 属性说明

|      **属性**      |  **描述**  |
|------------------|----------|
| 参数类型             | Int       |
| 默认值              | 100      |
| 取值范围             | \[0, +∞) |
| 是否重启 OBServer 节点生效 | 否        |
