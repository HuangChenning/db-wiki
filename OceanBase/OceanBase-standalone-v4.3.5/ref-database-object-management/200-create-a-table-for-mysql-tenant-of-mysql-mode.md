---
title: "创建表"
book: "数据库对象管理"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577967.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 创建表

#### 说明

基于性能和后期维护的需要，建议建表时为表设计主键或者唯一键。如果没有合适的字段作为主键，可以在创建表时不指定主键，待表创建成功后系统会为无主键表指定自增列作为隐藏主键。有关自增列的介绍请参见 [定义自增列](300-define-an-auto-increment-column-of-mysql-mode.md)。

#### 说明

通过设置 `WITH COLUMN GROUP(all columns)` 选项创建行存表，即使用户后来执行了 `DROP COLUMN GROUP(all columns)` 命令来删除这个列组，表仍然保持为行存储格式。

#### 说明

- 参数 `MERGE_ENGINE` 在创建表时指定之后，其配置值将不可修改。
- 对于 OceanBase 数据库 V4.3.5 版本，从 V4.3.5 BP3 版本开始支持 `MERGE_ENGINE` 参数。

#### 说明

当前版本配置项 `default_table_organization` 仅适用于 OceanBase 数据库 MySQL 模式用户租户，sys （系统）租户和 Oracle 模式用户租户不支持。

#### 说明

OceanBase 数据库 V4.3.5 BP4 版本开始支持创建临时表。
