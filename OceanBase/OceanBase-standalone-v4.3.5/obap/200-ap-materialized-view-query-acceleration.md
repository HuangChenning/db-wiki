---
title: "物化视图查询加速"
book: OceanBase AP
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006123835.html"
tags:
  - oceanbase
  - standalone
  - obap
---

# 物化视图查询加速

#### 注意

以下示例均是在 MySQL 模式下运行。

#### 说明

OceanBase 数据库支持物化视图日志自动管理功能。如果开启自动管理 mlog，那么在创建增量刷新物化视图前，用户无需创建基表的 mlog，OceanBase 数据库会自动创建对应的 mlog 或更新已存在的 mlog 表定义使其包含新建物化视图依赖的列。详细信息，参见 [物化视图日志自动管理（MySQL 模式）](../ref-database-object-management/250-automatic-management-materialized-views-log-of-mysql-mode.md) 和 [物化视图日志自动管理（Oracle 模式）](../ref-database-object-management/250-automatic-management-materialized-views-log-of-oracle-mode.md)。

#### 说明

OceanBase 数据库支持物化视图日志自动管理功能。如果开启自动管理 mlog，那么在创建实时物化视图前，用户无需创建基表的 mlog，OceanBase 数据库会自动创建对应的 mlog 或更新已存在的 mlog 表定义使其包含新建物化视图依赖的列。详细信息，参见 [物化视图日志自动管理（MySQL 模式）](../ref-database-object-management/250-automatic-management-materialized-views-log-of-mysql-mode.md) 和 [物化视图日志自动管理（Oracle 模式）](../ref-database-object-management/250-automatic-management-materialized-views-log-of-oracle-mode.md)。
