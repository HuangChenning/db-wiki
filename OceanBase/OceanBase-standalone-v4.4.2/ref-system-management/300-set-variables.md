---
title: "设置变量"
book: "系统管理"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077402.html"
tags:
  - oceanbase
  - standalone
  - ref-system-management
---

# 设置变量

#### 说明

- 设置 Session 级别的变量仅对当前 Session 有效，对其他 Session无效。设置 Global 级别的变量对当前 Session 无效，需要重新登录建立新的 Session 才会生效。
- 设置 Global 级别变量要求当前用户拥有 `SUPER` 权限或 `ALTER SYSTEM` 权限。
