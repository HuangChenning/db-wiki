---
title: "物化视图日志自动管理"
book: "数据库对象管理"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000005411373.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 物化视图日志自动管理

#### 说明

在 OceanBase 数据库 V4.3.5 BP4 版本中：

- 对于新创建的租户，其配置项 `enable_mlog_auto_maintenance` 的默认值为 `True`，即默认启用 mlog 自动管理功能。
- 对于由 OceanBase 数据库低版本（即 V4.3.5 BP4 之前的版本）升级而来的租户，其配置项 `enable_mlog_auto_maintenance` 的默认值为 `False`，即默认关闭 mlog 自动管理功能。
