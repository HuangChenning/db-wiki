---
title: "OceanBase 数据流转方案"
book: "数据迁移和导入"
version: master
source: "https://www.oceanbase.com/docs/common-best-practices-1000000001489661.html"
tags:
  - oceanbase
  - best-practices
  - migrations
---

# OceanBase 数据流转方案

本文旨在总结 OceanBase 数据库中数据流入流出的路径，帮助您全面了解 OceanBase 数据库在不同场景下的数据流转方案。

OceanBase 数据流转有以下方案：

- 数据导入导出至 OceanBase 数据库
- OceanBase 数据库的主备库同步
- 数据迁移同步至 OceanBase 数据库
- OceanBase 数据流转至增量解析系统
- OceanBase 数据流转至消息队列

其中，OceanBase 数据库既可以作为主库读写数据，也可以作为备库同步数据。OceanBase 数据库既可以作为数据迁移的源库，也可以作为目标库。

## 数据导入导出

您可以通过以下方式在 OceanBase 数据库中导入和导出数据：

- 基于 SQL：

  - 您可以使用 `SELECT INTO OUTFILE` 语句导出数据。
  - 您可以使用 `LOAD DATA INFILE` 语句导入数据。

- 基于工具：

  - 您可以使用 OceanBase 提供的 OBDUMPER 导出数据。您可以使用 OBDUMPER 将数据库中定义的对象和表数据以指定的文件格式导出到存储介质中。
  - 您可以使用 OBLOADER 导入数据。

您可以将标准的 CSV、Insert SQL、ORC 和 Parquet 等格式数据文件，通过 LOAD DATA 或 OBLOADER 等多种方式导入 OceanBase 数据库中。您可以使用此方式导入各种规模的数据。您可以根据需求选择最适合的数据导入导出方式。

## 主备库同步

您可以在 OceanBase V4.x 版本中使用物理备库功能，该功能按租户粒度提供。物理备库方案包含以下组成部分：

1.  一个主租户：负责提供读写服务。
2.  一个或多个备租户：通过 Redo 日志实时同步主租户上的数据变更。

请注意，OceanBase 的物理备库仅支持异步同步模式。

在 OceanBase V4.x 版本中，您可以选择以下两种物理备库的部署方式：

1.  基于日志归档的备库
2.  基于网络的备库

这两种部署方式采用不同的数据同步方式，您可以根据实际需求选择合适的方案。两种备库的同步性能：

- 受多种因素影响，如数据库负载、存储设备性能、网络带宽等。
- 网络备库：同步实时性高，通常在秒级。
- 日志归档备库：同步延迟稍大，一般在秒级到分钟级。

两种备库的应用场景：

- 主备库同步基于 OceanBase 同构和物理复制技术。
- 适用于主备同城/异地容灾、读写分离等场景。

### 基于日志归档的备库

在基于日志归档的物理备库中，Redo 日志来自主租户或其他备租户的归档日志。备租户仅与归档日志交互，不与主租户或其他备租户直接通信。

### 基于网络的备库

在基于网络的备库中，备租户通过网络直接连接主租户或其他备租户，实时读取日志。要求备库和主库网络保持畅通。备租户持续向主租户的日志传输服务请求日志。日志来源可以是主租户的在线日志或归档日志（如果主租户开启了日志归档）。系统可以自动在两种日志来源间切换，对备租户和用户来说是无感知的。

## 数据迁移同步

### OMS

OMS（OceanBase Migration Service）是 OceanBase 提供的数据迁移和同步工具，支持同构或异构数据源与 OceanBase 数据库之间的数据交互。OMS 支持在线迁移存量数据和实时同步增量数据。数据迁移适用于数据库升级、跨实例数据迁移、数据库拆分、扩容等业务场景。

OMS 的数据同步功能支持实时同步 OceanBase 等数据库的增量数据至自建的 Kafka、RocketMQ 等消息队列中。数据同步适用于云端商业智能分析、实时数据仓库构建、数据查询和报表分流、数据异地多活、数据异地灾备、数据聚合和实时数据仓库构建等。

### CDC

OceanBase 通过 Binlog Service 提供 CDC。为了让用户在使用 OceanBase 数据库的 MySQL 模式替换 MySQL 时能直接使用 Canal 或 Debezium，OceanBase 推出了 Binlog Service。Binlog Service 收集 OceanBase 的事务日志并转换为 MySQL Binlog 的服务，可用于实时数据订阅。

## 迁移方案对比

[TABLE]
