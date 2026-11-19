---
title: "使用 LOAD DATA 语句导入数据"
book: OceanBase AP
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006338107.html"
tags:
  - oceanbase
  - standalone
  - obap
---

# 使用 LOAD DATA 语句导入数据

#### 说明

全量旁路导入与增量旁路导入的适用范围、差异及更完整的旁路导入能力说明，请参见 [数据导入概述](100-data-import-overview.md)。

#### 说明

`FROM FILES` 中的 `LOCATION` 须为 OBServer 能访问的路径；目录及文件建议置于 `secure_file_priv` 允许的范围内（与 `LOAD DATA INFILE` 相同）。

#### 注意

由于安全原因，设置系统变量 `secure_file_priv` 时，只能通过本地 Unix Socket 连接数据库执行修改该全局变量的 SQL 语句。更多信息，请参见 [secure_file_priv](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005285634)。

#### 说明

`FROM FILES` 的 `LOCATION` 为服务端路径；`FORMAT` 中 `TYPE` 取值与大小写以当前租户模式手册为准，本示例与手册示例一致使用小写 `csv`。

#### 注意

由于安全原因，设置系统变量 `secure_file_priv` 时，只能通过本地 Unix Socket 连接数据库执行修改该全局变量的 SQL 语句。更多信息，请参见 [secure_file_priv](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005285634)。

#### 说明

OceanBase 数据库中的 `LOAD DATA` 语句仅支持加载 OBServer 节点本地的输入文件。因此，需要在导入之前将文件拷贝到某台 OBServer 上。

#### 注意

由于安全原因，设置系统变量 `secure_file_priv` 时，只能通过本地 Unix Socket 连接数据库执行修改该全局变量的 SQL 语句。更多信息，请参见 [secure_file_priv](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005285634)。

#### 说明

OceanBase 数据库中的 `LOAD DATA` 语句仅支持加载 OBServer 节点本地的输入文件。因此，需要在导入之前将文件拷贝到某台 OBServer 上。

#### 注意

由于安全原因，设置系统变量 `secure_file_priv` 时，只能通过本地 Unix Socket 连接数据库执行修改该全局变量的 SQL 语句。更多信息，请参见 [secure_file_priv](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005285634)。

#### 说明

`LOCAL INFILE` 表示由客户端读取本地文件并上传至服务端；连接命令需携带 `--local-infile`（或等效选项）。**`LOAD DATA LOCAL INFILE` 不支持旁路导入**，因此请勿添加 `APPEND` / `DIRECT(...)` Hint。

#### 说明

与 MySQL 模式相同，需使用 `--local-infile` 连接；`INFILE` 路径为客户端本地路径，且不支持旁路 Hint。
