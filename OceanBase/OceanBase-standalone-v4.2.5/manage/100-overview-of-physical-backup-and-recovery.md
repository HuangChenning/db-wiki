---
title: "物理备份与恢复概述"
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002701800.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 物理备份与恢复概述

#### 注意

在进行物理备份操作时，需要先开启日志归档模式后，才能执行数据备份。

#### 说明

数据备份会备份系统变量和租户配置项，但不会备份集群级配置项以及私有系统表数据。
