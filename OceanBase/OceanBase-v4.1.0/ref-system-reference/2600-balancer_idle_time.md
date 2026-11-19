---
title: balancer_idle_time
book: "系统参考"
version: V4.1.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-10000000001702077.html"
tags:
  - oceanbase
  - distributed
  - ref-system-reference
---

# balancer_idle_time

balancer_idle_time 
=======================================

`balancer_idle_time` 用于设置负载均衡等后台任务线程空闲时的唤醒间隔时间。


|      **属性**      |   **描述**   |
|------------------|------------|
| 参数类型             | 时间类型       |
| 默认值              | 5m，表示 5 分钟 |
| 取值范围             | \[10s, +∞) |
| 是否重启 OBServer 节点生效 | 否          |
