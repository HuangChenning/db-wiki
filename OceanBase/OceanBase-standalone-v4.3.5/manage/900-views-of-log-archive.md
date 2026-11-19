---
title: "日志归档相关视图介绍"
book: "管理数据库"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577580.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 日志归档相关视图介绍

OceanBase 数据库支持通过各种视图查看归档的相关信息。

## CDB_OB_ARCHIVE_DEST

`CDB_OB_ARCHIVE_DEST` 用于展示集群中所有租户配置的日志的归档路径（`LOG_ARCHIVE_DEST` 参数的配置）。

| 字段      | 描述                                                |
|-----------|-----------------------------------------------------|
| TENANT_ID | 租户 ID                                             |
| DEST_NO   | 标识归档路径的参数，`0` 表示参数 `LOG_ARCHIVE_DEST` |
| NAME      | 属性名                                              |
| VALUE     | 属性值                                              |

## DBA_OB_ARCHIVE_DEST

`DBA_OB_ARCHIVE_DEST` 用于展示当前租户配置的日志的归档路径（`LOG_ARCHIVE_DEST` 参数的配置）。

| 字段    | 描述                                                |
|---------|-----------------------------------------------------|
| DEST_NO | 标识归档路径的参数，`0` 表示参数 `LOG_ARCHIVE_DEST` |
| NAME    | 属性名                                              |
| VALUE   | 属性值                                              |

## CDB_OB_ARCHIVELOG

`CDB_OB_ARCHIVELOG` 用于展示集群中所有租户当前的归档进度。

[TABLE]

## DBA_OB_ARCHIVELOG

`DBA_OB_ARCHIVELOG` 用于展示当前租户的归档进度。

[TABLE]

## CDB_OB_ARCHIVELOG_SUMMARY

`CDB_OB_ARCHIVELOG_SUMMARY` 用于展示集群所有租户的所有的归档信息。

[TABLE]

## DBA_OB_ARCHIVELOG_SUMMARY

`DBA_OB_ARCHIVELOG_SUMMARY` 用于展示当前租户所有的归档信息。

[TABLE]

## CDB_OB_ARCHIVELOG_PIECE_FILES

`CDB_OB_ARCHIVELOG_PIECE_FILES` 用于展示集群所有租户的所有的 Piece 信息。

[TABLE]

## DBA_OB_ARCHIVELOG_PIECE_FILES

`DBA_OB_ARCHIVELOG_PIECE_FILES` 用于展示当前租户所有的 Piece 信息。

[TABLE]
