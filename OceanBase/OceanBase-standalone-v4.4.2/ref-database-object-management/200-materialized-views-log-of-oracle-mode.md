---
title: "物化视图日志"
book: "数据库对象管理"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006078099.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 物化视图日志

#### 说明

mlog 的主键由基表的主键、所有分区键（如果存在）以及自增列 `sequence$$` 组成，形成复合主键。

#### 说明

对于 V4.4.2 版本，从 V4.4.2 BP2 版本起，如果物化视图有新增依赖列，系统将采用 Online 在尾部加列，不再是通过创建新的 mlog 表并替换原有 mlog 表的方式进行操作。

#### 说明

对于 V4.4.2 版本，`mlog_trim_interval` 从 V4.4.2 BP2 版本开始不再生效。

#### 说明

在 OceanBase 数据库 V4.4.2 版本中：

- 对于新创建的租户，其配置项 `enable_mlog_auto_maintenance` 的默认值为 `True`，即默认启用 mlog 自动管理功能。
- 对于由 OceanBase 数据库低版本（即 V4.4.2 之前的版本）升级而来的租户，其配置项 `enable_mlog_auto_maintenance` 的默认值为 `False`，即默认关闭 mlog 自动管理功能。

#### 说明

OceanBase 数据库 mlog 暂时不支持指定分区（Partition），mlog 的 Partition 和基表的 Partition 是绑定关系。

#### 注意

Oracle 模式中视图 `sys.DBA_MVIEW_LOGS` 中字段 `MASTER` 匹配表名时，表名需使用大写字母。
