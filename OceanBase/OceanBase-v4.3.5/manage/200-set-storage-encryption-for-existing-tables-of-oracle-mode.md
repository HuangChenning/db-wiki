---
title: "为已有表设置透明加密"
book: "管理数据库"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005375459.html"
tags:
  - oceanbase
  - distributed
  - manage
---

# 为已有表设置透明加密

#### 说明

对表执行全量合并后，待全量合并完成，所有表数据均已加密完成，您可以直接通过查看 `V$OB_ENCRYPTED_TABLES` 视图来确认加密完成情况。

#### 说明

渐进合并过程中，您可以通过查询 `V$OB_ENCRYPTED_TABLES` 视图来实时关注加密的完成情况。
