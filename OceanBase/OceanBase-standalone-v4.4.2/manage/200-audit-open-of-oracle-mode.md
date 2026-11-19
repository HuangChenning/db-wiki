---
title: "开启安全审计"
book: "管理数据库"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077560.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 开启安全审计

#### 说明

OceanBase 数据库默认创建了 `ORAAUDITOR` 用户。该用户默认处于锁定状态，在使用审计前需要启用该用户。

#### 说明

审计记录支持写入内部表、写入本地磁盘文件和写入审计日志三种方式：

- 写入磁盘文件：通过异步写的方式记录在 `<安装目录>/audit/` 下，默认在 `/home/admin/oceanbase/audit/observer_xx_xxxxxx.aud`。
- 写入审计日志：审计记录写入审计日志文件，支持日志归档、压缩、轮转、清理及加密等管理策略，从 V4.4.2 BP2 版本开始支持。
- 写入内部表：审计信息直接写入系统表。内部表 `__all_tenant_security_audit_record`，存放审计记录；内部表 `__all_virtual_audit_operation` 或 `__all_virtual_audit_action`，存放审计相关 `ID` 和 `Name` 的映射。

#### 说明

Oracle 模式审计日志加密功能从 V4.4.2 BP2 版本开始支持。
