---
title: "修改租户系统变量"
book: "管理数据库"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577608.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 修改租户系统变量

#### 注意

设置 Global 级别变量时，对于 MySQL 租户，要求当前用户拥有 `SUPER` 权限或 `ALTER SYSTEM` 权限；对于 Oracle 租户，要求当前用户拥有 `ALTER SYSTEM` 权限。设置前，请确认您的权限。用户权限的详细说明，参见 [用户和权限概述](100-user-and-permission-overview.md)。

#### 说明

Oracle 模式还可以通过 `ALTER SESSION SET ob_query_timeout = 20000000;` 语句修改 Session 级别的变量值。

#### 说明

Oracle 模式还可以通过 `ALTER SYSTEM SET ob_query_timeout = 20000000;` 语句修改 Global 级别的变量值。

#### 说明

通过 ON/OFF、TRUE/FALSE 或 1/0 三种方式进行布尔类型变量的设置是等效的。
