---
title: "为已有表设置透明加密"
book: "管理数据库"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006078051.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 为已有表设置透明加密

#### 注意

配置项 `tde_method` 一旦设置，就不能再修改。

#### 说明

仅当租户上所有 OBServer 节点上的配置项 `tde_method` 的值均为 `internal`，该语句才能执行成功。

#### 说明

步骤 2～5 用于 `obcloud` 方式下的加密方式、KMS 配置及租户主密钥就绪。**若本租户已参考[生成租户主密钥（MySQL 模式）](200-configure-tenant-master-key-mysql.md)完成相同配置，可跳过这些步骤**。为方便阅读及操作，以下内容再次详细列出全部流程。

#### 注意

配置项 `tde_method` 一旦设置，就不能再修改。

#### 说明

仅当租户上所有 OBServer 节点上的配置项 `tde_method` 的值均为 `obcloud`，且已正确配置 `external_kms_info`，该语句才能执行成功。

#### 注意

以上为 `external_kms_info` 的示例值，请根据实际 KMS endpoint 与密钥信息替换。更多说明请参见 [tde_method](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005285832) 和 [external_kms_info](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005285804)。

#### 说明

全量合并完成后，数据加密可能仍在进行中。此时查询 `oceanbase.V$OB_ENCRYPTED_TABLES` 视图，`STATUS` 可能为 `ENCRYPTING`（加密中），表示加密任务尚未结束，并不代表合并失败。请等待 `ENCRYPTED` 变为 `YES` 且 `STATUS` 变为 `NORMAL` 后，再确认加密已完成。

#### 说明

渐进合并过程中，您可以通过查询 `V$OB_ENCRYPTED_TABLES` 视图来实时关注加密的完成情况。
