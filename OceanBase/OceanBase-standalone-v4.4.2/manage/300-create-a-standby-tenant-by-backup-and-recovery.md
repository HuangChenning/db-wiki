---
title: "使用备份恢复（带日志）功能创建备租户"
book: "管理数据库"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077536.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 使用备份恢复（带日志）功能创建备租户

#### 说明

设置归档目的端、开启归档模式、设置备份目的端以及执行数据备份等操作均支持在系统租户（`sys` 租户）或用户租户下执行，在系统租户下执行时，需要在对应命令的结尾加 `tenant = 'tenant_name'`，本文以在用户租户下的操作为例，提供操作指导。

#### 注意

为了保证数据备份期间的日志都能被归档，必须先开启租户的归档模式后，再执行数据备份。
