---
title: "基于常态化 Memleak 的内存泄露诊断机制"
book: "系统管理"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077381.html"
tags:
  - oceanbase
  - standalone
  - ref-system-management
---

# 基于常态化 Memleak 的内存泄露诊断机制

#### 注意

- 在 OceanBase 数据库中，名称以 "\_" 开头的配置项称为隐藏配置项，仅供开发人员在故障排查或紧急运维时使用。
- 在设置配置项的值时，需要满足如下要求：`_min_malloc_sample_interval <= _max_malloc_sample_interval`。
- 配置项 `_min_malloc_sample_interval` 和 `_max_malloc_sample_interval` 不建议用户随意修改，如果修改不当会导致集群性能变差。
