---
title: "使用 LOAD DATA 语句导入数据"
book: "数据迁移"
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006077158.html"
tags:
  - oceanbase
  - standalone
  - data-migration
---

# 使用 LOAD DATA 语句导入数据

#### 说明

OceanBase 数据库支持加载位于 OSS、服务器端（OBServer 节点）和客户端（本地）的数据文件。

#### 说明

OceanBase 数据库支持 Oracle 模式和 MySQL 模式两种模式。以下示例是在 MySQL 模式下，展示如何使用 `LOAD DATA` 语句。

#### 注意

由于安全原因，设置系统变量 `secure_file_priv` 时，只能通过本地 Unix Socket 连接数据库执行修改该全局变量的 SQL 语句。更多信息，请参见 [secure_file_priv](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002015981)。

#### 注意

为了使用 `LOAD DATA LOCAL INFILE` 功能，请使用 V2.2.4 或之后的版本的 OBClient 客户端。如果您没有要求版本的 OBClient 客户端，也可以使用 MySQL 客户端来连接数据库。
