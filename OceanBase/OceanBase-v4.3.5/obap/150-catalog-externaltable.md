---
title: "Catalog 与外部表"
book: OceanBase AP
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000006319715.html"
tags:
  - oceanbase
  - distributed
  - obap
---

# Catalog 与外部表

#### 说明

当前仅 OceanBase MySQL 模式支持 Catalog 能力。

#### 注意

Catalog 是对底层数据的元数据抽象，不是存储位置本身。若需按路径直接访问未注册到 Catalog 的文件，应使用 `CREATE EXTERNAL TABLE ... LOCATION` 方式。

#### 注意

内部 Catalog 名称为 `internal`，通常可省略。

#### 说明

- 若未执行 `SET CATALOG` 和 `USE`，直接写 `SELECT * FROM odps_table;` 将在当前 Catalog（如 internal）中查找该表，可能报错。
- 切换上下文仅影响后续语句，不影响连接或事务状态。
