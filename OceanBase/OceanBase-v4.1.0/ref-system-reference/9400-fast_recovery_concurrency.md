---
title: fast_recovery_concurrency
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002168971.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# fast_recovery_concurrency

fast_recovery_concurrency 
==============================================

`fast_recovery_concurrency` 用于控制 RootService 调度的快速恢复任务在 OBServer 上执行的并发数。

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>从 V4.0.0 版本开始弃用。</p>
</main>

|        属性        |     描述     |
|------------------|------------|
| 参数类型             | 整型         |
| 默认值              | 10         |
| 取值范围             | \[1,1000\] |
| 是否重启 OBServer 节点生效 | 否          |
