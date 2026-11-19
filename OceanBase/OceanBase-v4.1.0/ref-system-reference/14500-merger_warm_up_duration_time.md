---
title: merger_warm_up_duration_time
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002168959.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# merger_warm_up_duration_time

merger_warm_up_duration_time 
=================================================

`merger_warm_up_duration_time` 用于设置合并时，新版基线数据的预热时间。


<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>从 V4.0.0 版本开始弃用。</p>
</main>

|      **属性**      |   **描述**    |
|------------------|-------------|
| 参数类型             | 时间类型        |
| 默认值              | 0s          |
| 取值范围             | \[0s, 60m\] |
| 是否重启 OBServer 节点生效 | 否           |
