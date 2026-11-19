---
title: ob_esi_io_concurrency
book: "配置项和系统变量"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001502170.html"
tags:
  - oceanbase
  - distributed
  - ref-configuration-items-and-system-variables
---

# ob_esi_io_concurrency

<main id="notice" type='explain'>
<h4>说明</h4>
<p>由于 V4.x 版本对物理备份恢复功能进行了架构的优化调整，该配置项对应的功能在 V4.x 版本中不再支持，从 V4.0.0 版本开始删除。</p>
</main>

## 功能描述

`ob_esi_io_concurrency` 用于设置 obesi 进程的并发 I/O 数。

## 属性说明

| **属性** | **描述** |
| --- | --- |
| 参数类型 | Int |
| 默认值 | 0 |
| 取值范围 | [0, +∞) |
| 是否重启 OBServer 节点生效 | 否 |
