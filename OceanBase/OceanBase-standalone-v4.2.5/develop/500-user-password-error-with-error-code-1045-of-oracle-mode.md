---
title: "用户密码错误，错误代码 ERROR 1045"
book: "应用开发"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002702089.html"
tags:
  - oceanbase
  - standalone
  - develop
---

# 用户密码错误，错误代码 ERROR 1045

#### 说明

解锁用户的操作一般由管理员完成，普通用户如果需要执行解锁操作，必须具备全局 `ALTER USER` 权限。

#### 说明

为用户设置密码时，用户密码需要符合当前租户的密码复杂度。密码复杂度相关操作及说明请参见 [密码复杂度](../manage/200-password-complexity-of-oracle-mode.md)。
