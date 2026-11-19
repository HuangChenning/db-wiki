---
title: "创建表"
book: "数据库对象管理"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577910.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 创建表

#### 说明

基于性能和后期维护的需要，建议建表时为表设计主键或者唯一键。如果没有合适的字段作为主键，可以为表增加一个数值列作为主键，并使用 Oracle 租户的序列为该列填充值。有关序列的介绍请参见 [管理序列](600-management-sequence-of-oracle-mode.md)。

#### 说明

通过设置 `WITH COLUMN GROUP(all columns)` 选项创建行存表，即使用户后来执行了 `DROP COLUMN GROUP(all columns)` 命令来删除这个列组，表仍然保持为行存储格式。

#### 说明

参数 `MERGE_ENGINE` 在创建表时指定之后，其配置值将不可修改。
