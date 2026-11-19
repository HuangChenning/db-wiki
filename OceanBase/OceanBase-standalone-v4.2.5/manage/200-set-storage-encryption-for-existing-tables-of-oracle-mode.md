---
title: "为已有表设置透明加密"
book: "管理数据库"
version: V4.2.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000002702004.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 为已有表设置透明加密

#### 注意

配置项 `tde_method` 一旦设置就不能再修改，并且在存在备租户的场景下，需要在备租户中也设置相同的值。

#### 说明

对表执行全量合并后，待全量合并完成，所有表数据均已加密完成，您可以直接通过查看 `V$OB_ENCRYPTED_TABLES` 视图来确认加密完成情况。

#### 说明

渐进合并过程中，您可以通过查询 `V$OB_ENCRYPTED_TABLES` 视图来实时关注加密的完成情况。
