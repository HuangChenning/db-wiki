---
title: "Spark Catalog 与 OceanBase 集成最佳实践"
book: "开发"
version: master
source: "https://www.oceanbase.com/docs/common-best-practices-1000000002808478.html"
tags:
  - oceanbase
  - best-practices
  - develop
---

# Spark Catalog 与 OceanBase 集成最佳实践

## 背景与架构概述

### Spark Catalog 核心价值

Apache Spark 3.0 引入的 Spark Catalog 作为标准化元数据管理接口，通过统一元数据视图、动态 Schema 发现和标准化 API 三大核心能力，实现了跨异构数据源的元数据一致性管理。相较于传统 Hive Metastore，其显著优势体现在：

| 核心特性 | 技术实现说明 |
|----|----|
| 统一元数据视图 | 支持 OceanBase、HDFS、Iceberg 等异构数据源的元数据协同管理 |
| 动态 Schema 发现 | 自动推断外部数据源表结构，无需预定义 Schema |
| 标准化操作接口 | 通过统一 API 执行 DDL/DML |

### OceanBase Connector 适配方案

OceanBase Spark Connector 自 V1.1 版本起深度集成 Spark Catalog：

- **无缝接入**：项目完全开源，开源地址[GitHub](https://github.com/oceanbase/spark-connector-oceanbase)。
- **零代码接入**：零代码，支持全 SQL 交互。
- **性能增强**：自适应分区、并行读写、谓词下推等优化策略。
- **跨租户访问**：通过 Catalog 映射多租户数据源，实现跨业务单元联合查询。
- **分区表优化**：自动识别 OceanBase 数据库分区表，优化分区表读取性能。
- **自动 Schema 推断**：自动发现推断 OceanBase 数据库表结构。

## Spark 集群资源配置优化

### 硬件资源规划策略

以 128 核/1TB 内存服务器为例，建议采用以下资源配置策略：

| 硬件组件 | 物理规格 | Spark 资源配置策略                        | 计算示例       |
|----------|----------|-------------------------------------------|----------------|
| CPU      | 128核    | Worker 核数 = 物理核数 × 2.5              | 128×2.5=320 核 |
| 内存     | 1024GB   | 预留 24GB 系统内存，全量分配给 Spark 使用 | 1000GB 可用    |

### 关键配置参数调整

**系统级配置（spark-env.sh）**：规划硬件资源。

``` bash
# 内存资源配置
export SPARK_WORKER_MEMORY=1000G
# CPU 资源配置
export SPARK_WORKER_CORES=320
```

**作业级配置（spark-defaults.conf）**：调整 Spark Job 相关参数。

```
# Driver资源配置
spark.driver.cores=2
spark.driver.memory=4g

# Executor资源配置
spark.executor.memory=16g
spark.executor.cores=4

# 序列化优化
spark.serializer=org.apache.spark.serializer.KryoSerializer
```

### 调优目标验证

通过压力测试验证以下指标：

- 集群资源利用率 ≥95%
- 线性扩展能力验证（任务并行度与吞吐量呈正相关）
- 稳定性测试（72 小时持续负载）

## OceanBase Catalog 配置实践

### 基础连接配置

[TABLE]

### 读操作优化

根据您实际的硬件规格与资源条件，通过调整以下参数，提升 Spark 从 OceanBase 数据库的读取性能：

| **参数名称** | **默认值** | **参数解释** | **调优建议** |
|----|----|----|----|
| `spark.sql.catalog.your_catalog_name.fetch-size` | 100 | 设置 JDBC 驱动每次从 OceanBase 数据库获取的行数。 | 可以适当调大此值，减少网络交互次数，提高 Spark 每个 Task 读取 OceanBase 的性能。 |
| `spark.sql.catalog.your_catalog_name.max_records_per_partition` |  | 控制 Spark 读取 OceanBase 数据库时，最多多少条数据作为一个分区。默认为**空**，此时 Spark 根据数据量自动推算出该值。 | 一般不建议手动设置此值。 |
| `spark.sql.catalog.your_catalog_name.parallel_hint_degree` | 1 | Spark 读取 OceanBase 数据库时，Spark 下发到 OceanBase 数据库的 SQL 会自动带上 PARALLEL Hint。通过该参数可以设置 /\*+ PARALLEL(n) \*/ Hint 中的 n。 | 根据 OceanBase 数据库计算资源调为 `4-8`，提升并行度。 |

### 写操作优化

通过调整以下参数，提升 Spark 从 OceanBase 数据库的写入性能：

#### JDBC 写入优化

| **参数名称** | **参数说明** | **调优建议** |
|----|----|----|
| `spark.sql.catalog.your_catalog_name.batch-size` | 该参数控制 Spark 每个 Task 每积累 batch-size 条数据，进行一次写入。 | 调大该值可提高写入效率。 |

#### 旁路导入优化

[TABLE]

### 表管理规范

#### 非分区表

- **限制**：

  1.  不支持创建索引。
  2.  不能设置列默认值。

#### 分区表

- **兼容性限制**：

  - Spark 仅支持 `BUCKET` 分区，对应 OceanBase 数据库的 `KEY` 分区。例如：

    ``` sql
    CREATE TABLE test.test1 (
      user_id BIGINT COMMENT 'test_for_key',
      name VARCHAR(255)
    )
    PARTITIONED BY (bucket(16, user_id))
    COMMENT 'test_for_table_create'
    TBLPROPERTIES('replica_num' = 2, COMPRESSION = 'zstd_1.0');
    ```

  - **不支持多级分区**，仅允许一级分区。

- **推荐实践**：

  复杂分区表应在 OceanBase 数据库侧直接创建，Spark Catalog 可自动识别现有表结构。

## 生产环境建议

1.  **参数调优**

    根据业务负载动态调整 Spark 资源配置和 OceanBase 数据连接参数，关注线程并发、批量大小等关键指标。

2.  **管理分区**

    为提升查询效率，考虑根据业务需求对表进行合理的分区。

3.  **管理权限**

    确保在 OceanBase 数据库和 Spark 中妥善管理用户权限，防止未经授权的数据访问。

4.  **管理版本**

    定期检查更新版本，建议升级到最新版 `spark-connector-oceanbase`，集成性能优化和新功能。
