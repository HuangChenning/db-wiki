---
title: "激活角色"
book: "管理数据库"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003578391.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 激活角色

#### 注意

如果用户是为自身设置默认激活已经被授予的角色，则不需要任何权限。

#### 说明

通过 `SET ROLE` 语句激活的角色，仅影响当前 Session，不影响之后的 Session。
