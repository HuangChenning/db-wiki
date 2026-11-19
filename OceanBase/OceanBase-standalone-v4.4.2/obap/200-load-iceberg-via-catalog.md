---
title: "通过 Catalog 加载 Iceberg 表"
book: OceanBase AP
version: V4.4.2
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000006338116.html"
tags:
  - oceanbase
  - standalone
  - obap
---

# 通过 Catalog 加载 Iceberg 表

#### 说明

HMS Catalog 与 REST Catalog 的区别在于**从哪套 Catalog 服务加载 Iceberg 表元数据**；Iceberg 表已支持的功能、列类型等在两种接入方式下一致。HMS Catalog 的创建与认证配置详见 [通过 Catalog 加载 Hive 表](100-load-hive-via-catalog.md)。

#### 说明

当前仅 OceanBase MySQL 模式支持通过 External Catalog 访问 Iceberg 表。

#### 注意

通过 HMS Catalog 访问的 Iceberg 表当前为只读。Iceberg 表的 `INSERT INTO` 能力是否可用，取决于 External Catalog 类型及当前版本说明，使用前请确认。
