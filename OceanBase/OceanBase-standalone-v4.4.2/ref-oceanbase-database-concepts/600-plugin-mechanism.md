---
title: "插件机制"
book: "系统原理"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077365.html"
tags:
  - oceanbase
  - standalone
  - ref-oceanbase-database-concepts
---

# 插件机制

#### 注意

OceanBase 数据库插件机制目前为实验特性，暂不建议在生产环境使用。其功能范围和稳定性正在逐步完善。现阶段，插件机制主要支持以下场景：

- 分词器插件：用于扩展数据库的全文搜索能力，支持用户自定义分词逻辑。
- 功能验证：用户可以通过实验特性提前体验插件机制，并为后续的功能扩展提供宝贵的反馈意见。

#### 说明

各个插件接口（Plugin Interfaces）都有自己的版本号。
