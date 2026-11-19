---
title: "OceanBase 热点表最佳实践"
book: "开发"
version: master
source: "https://www.oceanbase.com/docs/common-best-practices-1000000003564513.html"
tags:
  - oceanbase
  - best-practices
  - develop
---

# OceanBase 热点表最佳实践

#### 说明

更多关于 OceanBase 数据库分区表和热点表优化的详细信息，请参考 [OceanBase 官方文档](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000003381057)。

#### 注意

复制表适用于对写入延迟不敏感，但对读取延迟要求高的场景。

#### 注意

关键字限流是一种快速缓解热点问题的有效方法，但需要合理设置限流阈值，避免影响正常业务。当超过最大并发数时，SQL 会直接失败，需要应用层实现重试机制。
