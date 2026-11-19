---
title: "Catalog 与外部表"
book: OceanBase AP
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006338115.html"
tags:
  - oceanbase
  - standalone
  - obap
---

# Catalog 与外部表

#### 说明

当前仅 OceanBase MySQL 模式支持 Catalog 能力。

#### 注意

- Catalog 是对底层数据的元数据抽象，不是存储位置本身。
- HMS Catalog 仅支持对接 Hive Metastore，无法直接指向任意 HDFS 路径。若需访问未注册到 HMS 的文件，应使用 `CREATE EXTERNAL TABLE ... LOCATION` 方式。

#### 注意

内部 Catalog 名称为 `internal`，通常可省略。

#### 说明

- 若未执行 `SET CATALOG` 和 `USE`，直接写 `SELECT * FROM hive_table;` 将在当前 Catalog（如 internal）中查找该表，可能报错。
- 切换上下文仅影响后续语句，不影响连接或事务状态。
