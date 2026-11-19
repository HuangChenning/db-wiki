---
title: "事务管理概述"
book: "应用开发"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002701966.html"
tags:
  - oceanbase
  - standalone
  - develop
---

# 事务管理概述

#### 说明

如果会话中的变量 `autocommit` 的值为 `0`，并且没有显式提交事务，程序异常中断时，OceanBase 数据库会自动回滚最后一个未提交的事务。
