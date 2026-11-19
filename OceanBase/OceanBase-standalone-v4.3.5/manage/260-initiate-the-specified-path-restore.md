---
title: "执行指定路径的恢复"
book: "管理数据库"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577564.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 执行指定路径的恢复

#### 注意

必须在 `ALTER SYSTEM RESTORE...PREVIEW` 命令执行成功后，再执行 `SHOW RESTORE PREVIEW` 命令，否则无法获取所需的结果。

#### 注意

如果待加载的 backup_set 或 archivelog_piece 存放在对象存储上，则要求每个 backup_set 或 archivelog_piece 路径中的 `host`、`access_id` 以及 `access_key` 等参数信息均相同。

#### 注意

- 执行恢复命令时，要求与执行 `ADD RESTORE SOURCE` 命令的会话是同一个会话，如果不是同一个会话（原先的会话中断或者使用了新的会话），之前加载的恢复源列表就会被清空。
- 执行 `ADD RESTORE SOURCE` 命令后，在同一会话中不允许再通过指定备份目的端的恢复命令来恢复租户。
- 执行恢复命令后，无论是否恢复成功，之前加载的恢复源列表均会被清空。如果需要重新调用恢复命令，则需要重新加载恢复所需的 backup_set 和 archivelog_piece。
