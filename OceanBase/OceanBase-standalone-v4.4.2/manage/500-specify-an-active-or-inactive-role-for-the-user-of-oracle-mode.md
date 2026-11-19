---
title: "为用户指定生效或失效的角色"
book: "管理数据库"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006078377.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 为用户指定生效或失效的角色

#### 说明

通过 `SET ROLE` 语句生效或失效的角色，仅影响当前 Session，不影响之后的 Session。

#### 注意

生效用户被授予的所有角色时，如果被授予的角色中有指定了密码的角色，系统将会报错。
