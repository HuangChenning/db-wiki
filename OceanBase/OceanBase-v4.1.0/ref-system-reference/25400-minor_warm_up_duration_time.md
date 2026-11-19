---
title: minor_warm_up_duration_time
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-0000000002180044.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# minor_warm_up_duration_time

`minor_warm_up_duration_time` 用于设置转储产生新转储文件的预热时间。

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>从 V4.0.0 版本开始弃用。</p>
</main>

|      **属性**      |   **描述**    |
|------------------|-------------|
| 参数类型             | 时间类型        |
| 默认值              | 30s         |
| 取值范围             | \[0s, 60m\] |
| 是否重启 OBServer 节点生效 | 否           |

当 `minor_warm_up_duration_time` 配置项的值为 0s 时，表示不进行预热。
