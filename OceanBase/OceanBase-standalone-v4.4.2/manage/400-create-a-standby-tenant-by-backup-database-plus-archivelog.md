---
title: "使用 BACKUP DATABASE PLUS ARCHIVELOG 功能创建备租户"
book: "管理数据库"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077538.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 使用 BACKUP DATABASE PLUS ARCHIVELOG 功能创建备租户

#### 注意

为了保证数据备份期间的日志都能被归档，必须先开启租户的归档模式后，再执行数据备份。

#### 注意

不同于使用物理备份恢复（带日志）功能创建的备租户，通过该方式恢复出的备租户未指定日志恢复源，无法直接开启日志持续同步。需要设置日志恢复源后，才能开启日志的持续同步。
