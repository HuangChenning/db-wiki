---
title: "为已有表设置透明加密"
book: "管理数据库"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005375457.html"
tags:
  - oceanbase
  - distributed
  - manage
---

# 为已有表设置透明加密

#### 功能适用性

OceanBase 数据库社区版暂不支持数据透明加密。

#### 说明

全量合并完成后，数据加密可能仍在进行中。此时查询 `oceanbase.V$OB_ENCRYPTED_TABLES` 视图，`STATUS` 可能为 `ENCRYPTING`（加密中），表示加密任务尚未结束，并不代表合并失败。请等待 `ENCRYPTED` 变为 `YES` 且 `STATUS` 变为 `NORMAL` 后，再确认加密已完成。

#### 说明

渐进合并过程中，您可以通过查询 `V$OB_ENCRYPTED_TABLES` 视图来实时关注加密的完成情况。
