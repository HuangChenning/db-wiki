---
title: "开启安全审计"
book: "管理数据库"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577824.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 开启安全审计

#### 说明

OceanBase 数据库默认创建了 `ORAAUDITOR` 用户。该用户默认处于锁定状态，在使用审计前需要启用该用户。

#### 说明

审计记录支持写入内部表和写入本地磁盘文件两种方式：

- 写入磁盘文件：通过异步写的方式记录在 `<安装目录>/audit/` 下，默认在 `/home/admin/oceanbase/audit/observer_xx_xxxxxx.aud`。
- 写入内部表：审计信息直接写入系统表。内部表 `__all_tenant_security_audit_record`，存放审计记录；内部表 `__all_virtual_audit_operation` 或 `__all_virtual_audit_action`，存放审计相关 `ID` 和 `Name` 的映射。

#### 说明

只有 `ORAAUDITOR` 用户主动设置了审计规则后，才会开始审计。
