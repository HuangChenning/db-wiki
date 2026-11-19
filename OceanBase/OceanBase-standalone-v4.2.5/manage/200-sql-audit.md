---
title: SQL Audit
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002702031.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# SQL Audit

#### 说明

- 租户抖动时，表现一般是 “租户 CPU 被打满” 和 “所有 SQL RT 飙升”，此时首要判断 SQL RT 飙升是否是第一案发现场（是 SQL 自己的问题导致 RT 飙升，还是其他问题导致 SQL RT 飙升）。
- 上面介绍的这条 SQL 是一大利器，基于 `SQL_ID` 做聚合，按照资源占用量倒序排序（资源占用量可以认为是 `avg_exec_time * cnt`），观察 top 几条 SQL 是否存在明显异常，从而判断是否是第一案发现场。
