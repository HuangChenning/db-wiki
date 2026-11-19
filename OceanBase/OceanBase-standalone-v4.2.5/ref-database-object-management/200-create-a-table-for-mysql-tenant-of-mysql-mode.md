---
title: "创建表"
book: "数据库对象管理"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003150287.html"
tags:
  - oceanbase
  - standalone
  - ref-database-object-management
---

# 创建表

#### 说明

基于性能和后期维护的需要，建议建表时为表设计主键或者唯一键。如果没有合适的字段作为主键，可以在创建表时不指定主键，待表创建成功后系统会为无主键表指定自增列作为隐藏主键。有关自增列的介绍请参见 [定义自增列](300-define-an-auto-increment-column-of-mysql-mode.md)。
