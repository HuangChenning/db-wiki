---
title: ob_ratelimit_stat_period
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001699337.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# ob_ratelimit_stat_period

`ob_ratelimit_stat_period` 用于设置 OBServer 节点计算和更新最大带宽的时间间隔。


|        属性        |     描述      |
|------------------|-------------|
| 参数类型             | 时间类型        |
| 默认值              | 1s          |
| 取值范围             | \[100ms,+∞) |
| 是否重启 OBServer 节点生效 | 否           |
