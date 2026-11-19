---
title: "数据文件导入 OceanBase 最佳实践"
book: "数据迁移和导入"
version: master
source: "https://www.oceanbase.com/docs/common-best-practices-1000000001489662.html"
tags:
  - oceanbase
  - best-practices
  - migrations
---

# 数据文件导入 OceanBase 最佳实践

#### 注意

请确保您的操作系统的语言包含目标字符集（如简体中文），并且 OceanBase 图形化客户端工具也支持目标字符集。推荐您将编码设置为 `UTF-8`。

#### 说明

此示例仅说明原理。生产中不常用。

#### 注意

- 参数调整会影响所有租户，您需要全局评估。
- 对于小内存（小于 8G）租户，大型查询可能挤占 MemStore 空间导致参数失效。

#### 说明

在数据导入后，将系统变量和参数务必重新修改为默认值。
