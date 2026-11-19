---
title: "执行物理恢复"
book: "管理数据库"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077237.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 执行物理恢复

#### 说明

如果未加密或恢复时可以访问原来的密钥管理服务，则跳过本步骤。

#### 说明

`external_kms_info` 用于存储一些密钥管理信息。有关该配置项的详细介绍，请参见 [external_kms_info](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005285804)。

#### 说明

对于 V4.4.2 版本，从 V4.4.2 BP3 版本开始，支持在 `uri` 中指定归档备份目的端路径 `backup_archive_dest`。只要配置了 `BACKUP_ARCHIVE_DEST`，发起恢复时即可始终在 `uri` 中携带归档备份路径，恢复期间系统会按需读取对应的 Piece。当旧的 Piece 位于归档备份目的端、对应的日志归档目的端中的副本已被清理，新 Piece 仍在日志归档目的端时，恢复任务可同时从两个目的端读取日志。

#### 注意

归档备份目的端仅保存已冻结（FROZEN）的 Piece，恢复到较新的位点时，通常仍需提供包含新 Piece 和 ACTIVE 尾部的日志归档目的端，建议恢复时同时提供日志归档路径和归档备份路径。恢复期间，如果任意必要的 Piece 在日志归档目的端和归档备份目的端均不存在，恢复将失败。

#### 注意

物理恢复不支持列存副本，在指定新租户的 Locality 时，不允许指定 C 副本。更多 C 副本的介绍及使用说明，参见 [列存副本](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005286303)。
