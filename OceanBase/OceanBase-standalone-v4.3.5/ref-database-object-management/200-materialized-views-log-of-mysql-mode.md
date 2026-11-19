---
title: "物化视图日志"
book: "数据库对象管理"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003578271.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 物化视图日志

#### 说明

对于 V4.3.5 版本，从 V4.3.5 BP4 版本开始支持物化视图日志自动管理功能，详细信息，参见 [物化视图日志自动管理](250-automatic-management-materialized-views-log-of-mysql-mode.md)。

#### 说明

mlog 的主键由基表的主键、所有分区键（如果存在）以及自增列 `sequence$$` 组成，形成复合主键。

#### 说明

OceanBase 数据库 mlog 暂时不支持指定分区（Partition），mlog 的 Partition 和基表的 Partition 是绑定关系。
