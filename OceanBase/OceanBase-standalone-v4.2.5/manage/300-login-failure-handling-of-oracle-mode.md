---
title: "登录失败处理"
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002702023.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 登录失败处理

#### 注意

解锁用户的操作一般由管理员完成，普通用户如果需要执行锁定和解锁操作，必须具备全局的 `ALTER USER` 权限。关于查看用户权限和授权的相关操作，参见 [查看用户权限](600-view-user-permissions-of-oracle-mode.md) 和 [直接授予权限](200-authority-of-oracle-mode.md)。

#### 注意

对于已经被锁定的用户无法通过 `ALTER PROFILE` 语句修改 `FAILED_LOGIN_ATTEMPTS` 的方式来进行解锁。对带有 `ALTER PROFILE` 语句的配置文件所做的更改仅影响其后续会话中的用户，而不影响其当前会话中的用户。
