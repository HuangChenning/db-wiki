---
title: "资源限流最佳实践"
book: "运维管理"
version: master
source: "https://www.oceanbase.com/docs/common-best-practices-1000000001489654.html"
tags:
  - oceanbase
  - best-practices
  - management
---

# 资源限流最佳实践

#### 注意

- 当同一条 SQL 可以匹配多个限流规则时，会选择并发度最小的进行限流。
- 所有的 Outline 相关功能都只能针对本租户，不能通过系统租户对其他租户进行 Outline 相关操作。

#### 注意

对于 V4.2.x 版本，当前仅 V4.2.2 及以上版本支持模糊绑定方式；对于 V4.3.x 版本，暂不支持模糊绑定方式。
