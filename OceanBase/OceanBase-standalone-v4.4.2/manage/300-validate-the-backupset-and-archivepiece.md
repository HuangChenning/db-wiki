---
title: "校验指定备份集或日志归档 Piece"
book: "管理数据库"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006547430.html"
tags:
  - oceanbase
  - standalone
  - manage
---

# 校验指定备份集或日志归档 Piece

#### 注意

如果不指定 `backup_set_id`，系统将会获取当前配置的备份路径下的所有备份集进行校验，从而导致产生大量的校验任务，耗时较长。如果确认不需要校验所有备份集，建议在校验命令中指定 `backup_set_id`。

#### 说明

MySQL 租户的管理员用户为 `root` 用户，Oracle 租户的管理员用户为 `SYS` 用户。

#### 注意

如果不指定 `backup_set_id`，系统将会获取当前配置的备份路径下的所有备份集进行校验，从而导致产生大量的校验任务，耗时较长。如果确认不需要校验所有备份集，建议在校验命令中指定 `backup_set_id`。

#### 注意

如果不指定 `piece_id`，系统将会获取当前配置的归档路径下的所有归档 Piece 进行校验，从而导致产生大量的校验任务，耗时较长。如果确认不需要校验所有归档 Piece，建议在校验命令中指定 `piece_id`。

#### 说明

MySQL 租户的管理员用户为 `root` 用户，Oracle 租户的管理员用户为 `SYS` 用户。

#### 注意

如果不指定 `piece_id`，系统将会获取当前配置的归档路径下的所有归档 Piece 进行校验，从而导致产生大量的校验任务，耗时较长。如果确认不需要校验所有归档 Piece，建议在校验命令中指定 `piece_id`。
