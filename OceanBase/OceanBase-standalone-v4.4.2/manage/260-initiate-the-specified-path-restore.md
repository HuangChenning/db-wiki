---
title: "执行指定路径的恢复"
book: "管理数据库"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077234.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 执行指定路径的恢复

#### 说明

对于 V4.4.2 版本，从 V4.4.2 BP3 版本开始，支持在 `uri` 中指定归档备份目的端路径 `backup_archive_dest`。只要配置了 `BACKUP_ARCHIVE_DEST`，即可始终在 `uri` 中携带归档备份路径，系统会按需读取对应的 Piece。当旧的 Piece 位于归档备份目的端、对应的日志归档目的端中的副本已被清理，新 Piece 仍在日志归档目的端时，恢复任务可同时从两个目的端读取日志。

#### 注意

必须在 `ALTER SYSTEM RESTORE...PREVIEW` 命令执行成功后，再执行 `SHOW RESTORE PREVIEW` 命令，否则无法获取所需的结果。

#### 注意

如果待加载的 backup_set、archivelog_piece 或备份归档数据存放在对象存储上，则要求每条路径中的 `host`、`access_id` 以及 `access_key` 等参数信息均相同。

#### 注意

- 执行恢复命令时，要求与执行 `ADD RESTORE SOURCE` 命令的会话是同一个会话，如果不是同一个会话（原先的会话中断或者使用了新的会话），之前加载的恢复源列表就会被清空。
- 执行 `ADD RESTORE SOURCE` 命令后，在同一会话中不允许再通过指定备份目的端的恢复命令来恢复租户。
- 执行恢复命令后，无论是否恢复成功，之前加载的恢复源列表均会被清空。如果需要重新调用恢复命令，则需要重新加载恢复所需的 backup_set、archivelog_piece 以及备份归档路径。
- 归档备份目的端仅保存已冻结（FROZEN）的 Piece，恢复到较新的位点时，通常仍需提供包含新 Piece 和 ACTIVE 尾部的日志归档路径，建议同时加载日志归档路径和归档备份路径。恢复期间，如果任意必要的 Piece 在日志归档路径和归档备份路径中均不存在，恢复将失败。
