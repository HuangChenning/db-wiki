---
title: "发起归档日志备份"
book: "管理数据库"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000007140646.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 发起归档日志备份

#### 说明

对于 V4.4.2 版本，从 V4.4.2 BP3 版本开始支持备份归档日志。

#### 说明

归档日志的备份目的端不允许与日志归档目的端相同，即 BACKUP_ARCHIVE_DEST 与 LOG_ARCHIVE_DEST 中的存储路径信息必须不同。

#### 说明

归档日志的备份目的端不允许与日志归档目的端相同，即 BACKUP_ARCHIVE_DEST 与 LOG_ARCHIVE_DEST 中的存储路径信息必须不同。

#### 说明

备份目的端的配置生效后，后续发起的归档日志备份将使用该目的端。如果未配置备份目的端，归档日志备份任务无法正常执行。

#### 说明

归档日志备份按照 Piece 并行调度，以文件级别的方式将数据从日志归档目的端拷贝至备份目的端，单个 Piece 的拷贝会按照日志流目录拆分并行。拷贝速度取决于 Piece 的数据大小以及两个目的端存储的读写吞吐和请求时延，该过程不会在 OBServer 本地产生额外的 IO 开销。

#### 说明

对于归档日志备份 Job 记录，视图中展示的 `BACKUP_SET_ID` 和 `PLUS_ARCHIVELOG` 没有实际意义。
