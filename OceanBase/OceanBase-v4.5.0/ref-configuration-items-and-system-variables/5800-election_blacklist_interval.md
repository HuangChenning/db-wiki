---
title: election_blacklist_interval
book: "配置项和系统变量"
version: V4.5.0
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000004479171.html"
tags:
  - oceanbase
  - distributed
  - ref-configuration-items-and-system-variables
---

# election_blacklist_interval

<main id="notice" type='explain'>
<h4>说明</h4>
<p>由于 V4.x 版本对系统架构进行了优化调整，选举的黑名单依赖于事件，不再依赖于时间，该配置项从 V4.0.0 版本开始删除。</p>
</main>

## 功能描述

`election_blacklist_interval` 用于设置主副本被废除后不允许再被选为主的时间间隔。

## 属性说明

|        属性        |     描述      |
|------------------|-------------|
| 参数类型                      | Time        |
| 默认值              | 1800s       |
| 取值范围             | \[0s, 24h\] |
| 是否重启 OBServer 节点生效 | 否           |
