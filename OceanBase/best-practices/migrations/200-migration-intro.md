---
title: "数据迁移概览"
book: "数据迁移和导入"
version: master
source: "https://www.oceanbase.com/docs/common-best-practices-1000000001489660.html"
tags:
  - oceanbase
  - best-practices
  - migrations
---

# 数据迁移概览

本文档面向需要将数据从本地或其他云环境迁移到 OceanBase 数据库的人员，介绍了数据库迁移的概念、方法和工具。在本文档中，下游目标环境为 OceanBase 数据库。

## 应用场景

数据迁移是数据库运维常见的操作，主要有如下的应用场景：

- 调整集群负载和机房搬迁。
- 数据库替换。
- 数据库逻辑复制，包括读写分离、数据库容灾、业务多活等。
- 数据复制。

## 迁移类型

本文档定义了以下主要的迁移类型：

- 数据库到数据库的迁移。
- 数据文件到数据库的迁移。

### 数据库到数据库的迁移

如果您希望从数据库迁移数据到 OceanBase 数据库，推荐使用 OMS。OMS 支持如下数据源：

- MySQL
- Oracle
- DB2 LUW
- TiDB
- PostgreSQL

如果 OMS 不支持您使用的数据库，请采用其他迁移方式。您可以把上游数据 Dump 出来，生成数据文件，再参考数据文件到数据库的迁移。

### 数据文件到数据库的迁移

如果您的数据文件是 CSV 文件，采用以下方式导入：

- MySQL 租户的 LOAD DATA 命令
- DataX 或 DataX Web 版
- OBLOADER

如果您的数据文件是 SQL 文件，采用以下方式导入：

- OBLOADER
- MySQL 或 obclient 命令
- Subtopic
- 数据库客户端导入

如果您的数据文件是 Parquet 文件，采用以下方式导入：

- OBLOADER
- LOAD DATA

如果您的数据文件是 ORC 文件，采用 OBLOADER 导入。

## 迁移工具

OceanBase 数据库提供丰富的数据迁移方法，包括：

- OceanBase 官方方案

  - OceanBase 提供的数据迁移服务 OMS，专门大规模数据迁移设计。
  - OceanBase 提供的导入数据工具 OBLOADER，专门为从数据文件导入设计。

- 命令行工具

  - 标准 SQL 命令 LOAD DATA 和 INSERT SQL，便于操作，适合小规模数据导入。
  - CREATE EXTERNAL TABLE 实现外部数据文件的直接查询，增加分析灵活性。
  - CREATE TABLE AS SELECT。

- 第三方集成工具

  Flink OceanBase Connector、DataX OceanBase Writer Plugin、Kafka 和 Canal 等。

### OMS

**基本特性：**

OMS 特性如下：

- 在线不停服迁移，业务应用无感知。
- 高性能的数据迁移，安全可靠。
- 一站式交互。

**适用场景：**

- 数据迁移适合大规模数据库到数据库的迁移。

**使用参考：**

- 关于 OMS 的详细介绍，参见 [OMS 使用文档](https://www.oceanbase.com/docs/oms-doc-cn)。

### OBLOADER

**基本特性：**

OBLOADER 特性如下：

- 支持从本地磁盘、NAS、HDFS、OSS、COS、OBS、Apache Hadoop、Aliyun OSS 和 AWS S3 导入数据库对象定义和表数据。
- 支持导入 mysqldump 导出的 INSERT SQL 格式的文件。
- 支持导入标准的 CSV、Insert SQL、Apache ORC 和 Apache Parquet 等格式的数据文件。
- 支持配置数据预处理的控制规则以及文件与表之间的字段映射关系。
- 支持导入限速、防导爆、断点恢复和错误自动重试。
- 支持指定自定义的日志目录，导入时可以保存坏数据和冲突数据。
- 支持导入工具自动对大文件进行切分且不占用额外的存储空间，无需人工切分文件。
- 支持对命令行中指定的敏感参数进行加密。包括：数据库的账号密码，云存储的账号密钥。

**适用场景：**

- OBLOADER 适合较大规模数据导入。

**使用参考：**

- 关于 OBLOADER 的详细介绍，参见 [OBLOADER 使用文档](https://www.oceanbase.com/docs/oceanbase-dumper-loader)。

### LOAD DATA

#### LOAD DATA LOCAL

**基本特性：**

LOAD DATA LOCAL 特性如下：

- 适用于本地文件导入 OB Cloud 云数据库。将本地文件以网络流的方式传输到 OB Cloud 云数据库并插入。
- 适用于小数据量场景。
- 仅支持一次传输一个文件。
- 目前支持 CSV、SQL 和 Parquet 文件单导入。

**适用场景：**

- LOAD DATA LOCAL 适合小规模数据导入。

**使用参考：**

- 关于 LOAD DATA LOCAL 的使用方法，参见 [使用 LOAD DATA 语句导入数据](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001049863)。

#### LOAD DATA FROM OSS

**基本特性：**

LOAD DATA FROM OSS 特性如下：

- 将 OSS 文件直接导入到 OB Cloud 云数据库中。
- 可支持一次导入多个 OSS 文件。
- 目前仅支持 CSV 文件导入。

**适用场景：**

- LOAD DATA FROM OSS 适合大规模数据导入。

**使用参考：**

- 关于 LOAD DATA FROM OSS 的操作指导，参见 [LOAD DATA（Oracle 模式）](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001054301) 和 [LOAD DATA（MySQL 模式）](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001053471)。

### INSERT SQL

**适用场景：**

- INSERT INTO VALUES 适合向内部表写入少量数据。
- INSERT INTO SELECT FROM \<table_name\> 适合向目标表写入另外一张表（内部表或外部表）的查询结果，即表与表之间的迁移。
- INSERT /*+ \[APPEND \|direct(need_sort,max_error,'full')\] enable_parallel_dml parallel(N)*/ INTO table_name select_sentence 旁路导入适合全量和增量旁路导入。

**使用参考：**

- 关于 INSERT SQL 的使用指导，参见 [INSERT（Oracle 模式）](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001054301) 和 [INSERT（MySQL 模式）](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001053471)。

### CREATE EXTERNAL TABLE

**适用场景：**

- 外表是数据库管理系统中的一项关键功能，通常数据库中的表存放于数据库的存储空间中，而外表的数据存储于外部存储服务中。

**使用参考：**

- 关于外表的使用指导，参见 [外表（Oracle 模式）](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001053129)和 [外表（MySQL 模式）](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001053137)。

### Flink

**适用场景：**

- Flink OceanBase Connector 适合从 Flink 实时导入数据。

**使用参考：**

- [通过 Flink 同步数据](https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001049848)

### Canal

**适用场景：**

- 适合从 Canal 实时导入数据。

**使用参考：**

- [通过 Canal 同步数据](%5B../800.integration/200.canal.md%5D(https://www.oceanbase.com/docs/common-oceanbase-database-cn-1000000001049845))

### Kafka

**适用场景：**

- 适合从 MySQL、Oracle 和 PostgreSQL 等数据库向 OceanBase 数据库迁移或同步数据。

**使用参考：**

- [OceanBase 数据库与 Kafka 集成最佳实践](https://www.oceanbase.com/docs/common-oceanbase-cloud-1000000001039437)

## 迁移方案选择

本节概述了各种常见数据源的迁移方案，旨在帮助您根据实际需求快速选择最适合的迁移策略。我们将按照数据源类型来分类介绍不同的迁移方案。

### 对象存储

将云厂商的对象存储中的数据导入到 OB Cloud 云数据库的方案见下表。

[TABLE]

### 文件系统

将本地文件系统及分布式文件系统中的数据导入到 OceanBase 数据库的方案见下表。

[TABLE]

### 流式系统

将流式系统中的数据导入到 OceanBase 数据库的方案见下表。

[TABLE]

### 数据库

将数据库中的数据导入到 OceanBase 数据库的方案见下表。

[TABLE]
