---
title: "为已有表设置透明加密"
book: "管理数据库"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006078053.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 为已有表设置透明加密

#### 说明（主密钥相关）

步骤 2～6 用于在 `internal` 方式下设置 `tde_method`、校验参数，并通过创建与打开 Keystore、执行 `ADMINISTER KEY MANAGEMENT SET KEY` 建立租户主密钥。**若本租户已完成相同配置，可跳过这些步骤**，直接创建加密表空间。说明与示例参见 [生成租户主密钥（Oracle 模式）](300-configure-tenant-master-key-oracle.md)。

#### 注意

配置项 `tde_method` 一旦设置，就不能再修改。

#### 说明

步骤 2～5 用于 `obcloud` 方式下的加密方式、KMS 配置及租户主密钥就绪。**若本租户已参考[生成租户主密钥（Oracle 模式）](300-configure-tenant-master-key-oracle.md)完成相同配置，可跳过这些步骤**。为方便阅读及操作，以下内容再次详细列出全部流程。

#### 注意

配置项 `tde_method` 一旦设置，就不能再修改。

#### 注意

以上为 `external_kms_info` 的示例值，请根据实际 KMS endpoint 与密钥信息替换。若使用其他 KMS 对接形态，字段格式可能不同，请参见 [tde_method](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005285832)、[external_kms_info](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005285804) 与 [生成租户主密钥（Oracle 模式）](300-configure-tenant-master-key-oracle.md)。

#### 说明

对表执行全量合并后，待全量合并完成，所有表数据均已加密完成，您可以直接通过查看 `V$OB_ENCRYPTED_TABLES` 视图来确认加密完成情况。

#### 说明

渐进合并过程中，您可以通过查询 `V$OB_ENCRYPTED_TABLES` 视图来实时关注加密的完成情况。
