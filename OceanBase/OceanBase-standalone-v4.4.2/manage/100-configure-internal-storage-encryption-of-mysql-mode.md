---
title: "为新创建的表设置透明加密"
book: "管理数据库"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006078050.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 为新创建的表设置透明加密

#### 注意

配置项 `tde_method` 一旦设置，就不能再修改。

#### 说明

仅当租户上所有 OBServer 节点上的配置项 `tde_method` 的值均为 `internal`，该语句才能执行成功。

#### 说明

步骤 2～5 用于 `obcloud` 方式下的加密方式、KMS 配置及租户主密钥就绪。**若本租户已参考[生成租户主密钥（MySQL 模式）](200-configure-tenant-master-key-mysql.md)完成相同配置，可跳过这些步骤**。为方便阅读及操作，以下内容再次详细列出全部流程。

#### 注意

以上为示例值，请根据实际 KMS endpoint 和密钥信息替换。更多说明请参见 [tde_method](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005285832) 和 [external_kms_info](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005285804)。
