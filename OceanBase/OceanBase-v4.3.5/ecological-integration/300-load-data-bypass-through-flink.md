---
title: Flink DirectLoad
book: "生态集成"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005120315.html"
tags:
  - oceanbase
  - distributed
  - ecological-integration
---

# Flink DirectLoad

#### 注意

如果您需要实时流式写入或处理无界数据流，请使用项目中的 `flink-connector-oceanbase` 连接器，它基于 JDBC 实现，支持无界流和实时写入。

#### 注意

连接租户的用户需要拥有该数据库的 `CREATE`、`INSERT`、`DROP` 和 `SELECT` 权限。更多有关用户权限的信息，请参见 [MySQL 模式下的权限分类](../manage/100-permission-classification-of-mysql.md)。

#### 注意

连接 OBServer 服务端时，sys 租户下查询系统视图 `DBA_OB_SERVERS` 即可获取 OBServer 的 RPC 端口号。

#### 说明

以上使用了最小参数集。更多参数配置请参考后续章节中的 -配置参数详解。
