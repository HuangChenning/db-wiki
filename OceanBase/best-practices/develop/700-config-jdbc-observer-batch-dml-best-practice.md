---
title: "配置 JDBC 和 OBServer 实现 Batch DML 最佳性能的最佳实践"
book: "开发"
version: master
source: "https://www.oceanbase.com/docs/common-best-practices-1000000001489651.html"
tags:
  - oceanbase
  - best-practices
  - develop
---

# 配置 JDBC 和 OBServer 实现 Batch DML 最佳性能的最佳实践

#### 说明

当您使用 OB Cloud 云数据库时，尽管使用相同的 JDBC 参数配置，但连接字符串可能略有不同。请参考以下文档来获取针对云环境的 JDBC 连接配置示例：[获取 OBCloud 云数据库连接参数](https://www.oceanbase.com/docs/common-oceanbase-cloud-1000000001346097) 和 [获取阿里云连接参数](https://help.aliyun.com/document_detail/2249617.html?spm=a2c4g.11186623.help-menu-26458.d_2_0_0_0.44fc5616rXVBqe)\
请确保根据您的云服务提供的特定连接信息进行相应调整，以确保顺利连接到 OceanBase 数据库。\

#### 说明

如果开启 `allowMultiQueries` 与 `rewriteBatchedStatements` 后出现了非预期报错，可以尝试关闭开关，并联系 OceanBase 技术服务人员确认原因。

#### 说明

由于 `rewriteBatchedStatements` 和 `useServerPrepStmts` 互斥，仅能选择其一，因此不能同时进行配置。
