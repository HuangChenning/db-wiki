---
title: Flink Connector OceanBase
book: "生态集成"
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005149260.html"
tags:
  - oceanbase
  - distributed
  - ecological-integration
---

# Flink Connector OceanBase

#### 说明

需要将下载的驱动 JAR 文件放入 Flink 的 `lib` 目录下，具体操作步骤，参见后续章节。

#### 注意

文件名必须是 `flink-sql-connector-oceanbase-<version>.jar`，这是 Flink SQL 识别连接器的关键。

#### 注意

连接租户的用户需要拥有该数据库的 `CREATE`、`INSERT`、`DROP` 和 `SELECT` 权限。更多有关用户权限的信息，请参见 [MySQL 模式下的权限分类](../manage/100-permission-classification-of-mysql.md)。

#### 说明

- 由于主键冲突，`id=1` 的记录会被更新为最新的值（Tom, 89）。
- 连接器通过 JDBC 协议与 OceanBase 通信，使用标准的 UPSERT 语义。

#### 说明

Oracle 模式同样支持 UPSERT 语义，主键冲突时会自动更新为最新值。

#### 说明

该连接器基于 JDBC 协议，通过 Druid 连接池管理数据库连接。
