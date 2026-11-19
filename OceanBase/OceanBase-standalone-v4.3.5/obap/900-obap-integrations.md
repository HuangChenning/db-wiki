---
title: "AP 场景下的生态集成"
book: OceanBase AP
version: V4.3.5
source: "https://www.oceanbase.com/docs/common-oceanbase-database-standalone-1000000003577306.html"
tags:
  - oceanbase
  - standalone
  - obap
---

# AP 场景下的生态集成

本文介绍 **AP（Analytical Processing，分析型处理）场景**下，与 OceanBase 数据库兼容的生态工具与集成方式。AP 场景侧重数据分析、报表、数据仓库、实时/离线数据集成与 BI 可视化，与 TP（事务型处理）场景形成互补。

关于 OceanBase 数据库完整的生态集成列表（含 TP、AP、AI 等），参见 [生态集成概述](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000000903440)。

## 生态集成一览

| 模块 | 工具 | 集成项 | 说明 | MySQL 模式兼容性 |
|----|----|----|----|----|
| 数据集成 | AWS Glue | [AWS Glue](https://www.oceanbase.com/docs/common-oceanbase-cloud-1000000001478166) | AWS Glue 是无服务器数据集成服务，帮助用户发现、准备、移动和集成多源数据，支持分析、机器学习和应用开发，提供数据发现、现代 ETL、数据清理与转换及集中式编目。本文介绍使用 AWS Glue 迁移 OceanBase 数据。 | 完整支持 |
| 数据集成 | Apache Flink | [Apache Flink 与 OceanBase 数据库数据集成指南](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005146839) | Apache Flink 是开源的流批一体计算引擎，能高效处理实时数据流与批量数据。本指南帮助开发者掌握 Flink 与 OceanBase 的集成方式，根据场景选择 Connector 与集成方案。 | 完整支持 |
| 数据集成 | Apache Flink | [使用 Flink DirectLoad 实现 OceanBase 旁路导入](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005120315) | Flink DirectLoad 连接器专为 OceanBase 设计，利用旁路导入技术以高吞吐将大批量数据写入数据库。本文介绍如何使用该连接器实现 OceanBase 旁路导入。 | 完整支持 |
| 数据集成 | Apache Flink | [使用 Flink Connector OceanBase 实时同步数据到 OceanBase](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005149260) | Flink Connector OceanBase 基于 JDBC，支持将数据实时写入 OceanBase（MySQL/Oracle 兼容模式）。本文介绍如何使用该连接器实现 Flink 与 OceanBase 的实时数据同步。 | 完整支持 |
| 数据集成 | dbt | [使用 dbt 分析 OceanBase 数据](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002012917) | dbt（data build tool）是开源数据转换工具，通过 SQL 实现数据转化，将命令转化为表或视图。本文介绍如何使用 dbt-oceanbase，通过 dbt 分析 OceanBase 数据库中的数据。 | 完整支持 |
| 数据集成 | Spark Catalog | [使用 Spark Catalog 连接 OceanBase 数据库](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002824727) | OceanBase Spark Connector 支持 Spark Catalog，用户能以更简洁一致的方式访问和操作 OceanBase。本文指导完成 OceanBase Spark Catalog 的配置与使用。 | 完整支持 |
| 数据集成 | NiFi | [通过 Apache NiFi 集成 OceanBase 数据库](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002940687) | Apache NiFi 是自动化数据流处理平台，支持在系统间高效可靠地传输数据。通过读取 OceanBase Binlog，可将数据分发至文件系统、Kafka 或 HTTP 端点等。本文介绍如何通过 NiFi 集成 OceanBase。 | 完整支持 |
| 数据集成 | Dataphin | [使用 Dataphin 同步 OceanBase 数据](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005476952) | Dataphin 是阿里云的数据建设与治理平台。本文介绍如何在 Dataphin 中配置 OceanBase 数据源，实现离线和实时数据集成。 | 完整支持 |
| 数据集成 | RisingWave CDC | [使用 RisingWave CDC 接入 OceanBase MySQL 数据](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005476954) | RisingWave 是流式数据库，其 MySQL-CDC 功能可实时捕获 OceanBase MySQL 的数据变更并以流的形式处理分析。本文介绍如何利用 RisingWave CDC 接入 OceanBase MySQL 数据。 | 完整支持 |
| 数据集成 | Apache Flume | Apache Flume | Apache Flume 是分布式数据集成工具。OceanBase 与 Apache Flume 的集成支持程度为完整支持。 | 完整支持 |
| 中间件 | Apache Pulsar | Apache Pulsar | Apache Pulsar 是分布式消息与流处理平台。OceanBase 与 Apache Pulsar 的集成支持程度为完整支持。 | 完整支持 |
| 编排调度 | Airflow | [Airflow 集成 OceanBase 数据库](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000003349386) | Apache Airflow 是开源平台，用于开发、调度和监控面向批处理的工作流，工作流可用 Python 定义，并通过 Web 界面管理状态。本文介绍如何在 Airflow 中集成 OceanBase 数据库。 | 完整支持 |
| 编排调度 | DolphinScheduler | [为 DolphinScheduler 配置 OceanBase 数据源](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002012913) | DolphinScheduler 是开源的分布式工作流任务调度系统，支持多种任务类型。其支持 OceanBase 数据源，MySQL 模式可按 MySQL 方式配置。本文介绍如何为 DolphinScheduler 配置 OceanBase 数据源。 | 完整支持 |
| 可视化 | Superset | [使用 Superset 和 OceanBase 进行数据分析](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002012921) | Superset 是用于数据探索和可视化的开源业务智能工具。本文介绍如何使用 Superset 连接 OceanBase 数据库进行数据分析。 | 完整支持 |
| 可视化 | Excel | [在 Excel 中连接 OceanBase 并获取数据](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000005476955) | Excel 是广泛使用的电子表格与数据可视化工具。本文介绍如何在 WPS Office Excel 和 Microsoft Excel 中通过 ODBC 数据源方式连接 OceanBase 数据库，实现数据查询与分析。 | 完整支持 |
| 可视化 | Power BI | [在 Power BI 中连接 OceanBase 并获取数据](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002012920) | Power BI 是 Microsoft 提供的商业智能工具，可连接多种数据源进行数据转换、分析，并创建交互式数据可视化报告。本文介绍如何在 Power BI 中连接 OceanBase 并获取数据。 | 完整支持 |
| 可视化 | Quick BI | [在 Quick BI 中连接 OceanBase 并获取数据](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002012919) | Quick BI 是阿里云提供的自助式数据分析和可视化服务，支持通过拖拽对数据进行探索并创建图表和看板。本文介绍如何在 Quick BI 中连接 OceanBase 并获取数据。 | 完整支持 |
| 可视化 | Tableau | [在 Tableau 中连接 OceanBase 数据库](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002012918) | Tableau 用于梳理和展示大量数据，提供直观的界面和强大的数据处理能力，帮助从初级用户到数据科学家发现数据洞察。本文介绍如何在 Tableau 中连接 OceanBase 数据库。 | 完整支持 |
| 可视化 | 观远 BI | [在观远 BI 中连接 OceanBase 数据库](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002760310) | 观远 BI 是商业智能与数据分析平台。本文以 OceanBase MySQL 模式为例，介绍如何在观远 BI 中连接 OceanBase 数据库进行数据展示。 | 完整支持 |
| 可视化 | 永洪 BI | [在 vividime 中连接 OceanBase 数据库](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000002760311) | 永洪 BI（vividime）是商业智能与数据分析平台。本文以 OceanBase MySQL 模式为例，介绍如何在 vividime V11 中连接 OceanBase 数据库进行数据展示。 | 完整支持 |
| 可视化 | FineBI | FineBI | FineBI 是可视化分析工具。OceanBase 与 FineBI 的集成支持程度为基本兼容。 | 基本兼容 |
| 可视化 | Metabase | Metabase | Metabase 是开源可视化与自助分析工具。OceanBase 与 Metabase 的集成支持程度为完整支持。 | 完整支持 |
| 可视化 | 阿里 DataV | 阿里 DataV | 阿里 DataV 是数据可视化平台。OceanBase 与阿里 DataV 的集成支持程度为完整支持。 | 完整支持 |
| 可视化 | Redash | Redash | Redash 是开源数据可视化与查询工具。OceanBase 与 Redash 的集成支持程度为完整支持。 | 完整支持 |

## 数据集成

数据集成（Data Integration）将来自不同来源的数据集中到统一视图中，以支持**分析、报表与业务决策**，是 AP 场景的基础能力。数据可能分散在关系库、文件、应用、NoSQL 与云存储中，通过集成形成可分析的数据层。

上表**数据集成**模块中的工具（如 Flink、dbt、Spark Catalog、NiFi、Dataphin、RisingWave CDC、Apache Flume 等）均适用于 AP 数据管道与数仓建设。

## 中间件

在 AP 场景中，**Apache Pulsar** 等中间件可作为消息与流数据入口，与 OceanBase 配合完成实时数据链路。上表**中间件**模块中的工具适用于与 OceanBase 联动的流式与事件驱动分析架构。

## 编排调度

在 AP 场景中，编排调度工具用于管理、调度和协调数据处理任务与数据流，例如 ETL、数据清洗、校验与发布等。通过工作流编排，可稳定、可重复地执行分析型任务。

上表**编排调度**模块中的 Airflow、DolphinScheduler 等，均可在 AP 场景下与 OceanBase 配合使用，用于调度以 OceanBase 为源或目标的数据作业。

## 可视化

AP 场景下的可视化工具用于将数据转化为图表与看板，支持自助分析、报表与决策。上表**可视化**模块中的 Superset、Excel、Power BI、Quick BI、Tableau、观远 BI、永洪 BI、FineBI、Metabase、阿里 DataV、Redash 等，均支持连接 OceanBase，便于在 AP 场景下进行数据探索与展示。
