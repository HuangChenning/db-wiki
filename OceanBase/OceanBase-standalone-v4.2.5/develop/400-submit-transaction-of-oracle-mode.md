---
title: "提交事务"
book: "应用开发"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002701963.html"
tags:
  - oceanbase
  - standalone
  - develop
---

# 提交事务

#### 说明

OceanBase 数据库会在 DDL 语句前和后隐式地发起一个 `COMMIT` 语句，也会提交事务。

#### 说明

如果事务隔离级别设置了可重复读，则已经开启事务的会话无法查询到新提交的数据。事务隔离级别的更多介绍请参见 [事务隔离级别](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001502865)。
