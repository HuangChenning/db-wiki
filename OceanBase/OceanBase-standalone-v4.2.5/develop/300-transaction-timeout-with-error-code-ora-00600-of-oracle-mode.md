---
title: "事务超时，错误代码 ORA-00600"
book: "应用开发"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002702093.html"
tags:
  - oceanbase
  - standalone
  - develop
---

# 事务超时，错误代码 ORA-00600

#### 说明

OceanBase 数据库为了避免事务长时间不提交持有锁影响其他会话，设计了两个超时逻辑：事务空闲超时和事务未提交超时。通常只会有一个超时机制会先被触发。

#### 说明

以下设置变量的方法仅对当前会话有效，如果需要保证设置永久生效，请使用 `SET GLOBAL` 语法配置相同变量后，再重启会话使其生效。
