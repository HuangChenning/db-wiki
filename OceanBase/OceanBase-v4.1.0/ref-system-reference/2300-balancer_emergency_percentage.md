---
title: balancer_emergency_percentage
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002173611.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# balancer_emergency_percentage

balancer_emergency_percentage 
==================================================

`balancer_emergency_percentage` 用于设置 UNIT 负载阈值，即当 UNIT 负载超过该阈值时，允许开启副本向外迁移，即使在合并期间也执行负载均衡。

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>从 V4.0.0 版本开始弃用。</p>
</main>

|      **属性**      |   **描述**   |
|------------------|------------|
| 参数类型             | 整型         |
| 默认值              | 80         |
| 取值范围             | \[1, 100\] |
| 是否重启 OBServer 节点生效 | 否          |
