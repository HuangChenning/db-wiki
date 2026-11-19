---
title: merger_switch_leader_duration_time
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002168958.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# merger_switch_leader_duration_time

merger_switch_leader_duration_time 
=======================================================

`merger_switch_leader_duration_time` 用于设置每日合并时批量切主的时间间隔。

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>从 V4.0.0 版本开始弃用。</p>
</main>

|      **属性**      |   **描述**   |
|------------------|------------|
| 参数类型             | 时间类型       |
| 默认值              | 3m，表示 3 分钟 |
| 取值范围             | \[0s, 30m\] |
| 是否重启 OBServer 节点生效 | 否          |
