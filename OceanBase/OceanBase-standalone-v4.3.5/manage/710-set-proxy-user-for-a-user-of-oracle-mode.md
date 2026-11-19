---
title: "使用代理用户"
book: "管理数据库"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003578184.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 使用代理用户

#### 注意

指定代理用户生效的角色权限时，对于带密码的角色权限，需要在连接数据库后手动通过 `SET ROLE role_name IDENTIFIED BY role_password;` 命令激活该角色。
